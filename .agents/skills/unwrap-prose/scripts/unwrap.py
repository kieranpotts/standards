#!/usr/bin/env python3
"""Remove soft wraps from the prose of one technical standard.

Joins the lines of each paragraph, list item, admonition, description-list
entry, and table cell onto a single source line, as TS-28 requires. Verbatim
content (listing, literal, passthrough, comment, and fenced blocks, and any
block or paragraph styled `verse`, `source`, `listing`, `literal`, `pass`,
`stem`, or `%hardbreaks`) is left untouched, as are lines that end in a hard
line break.

The script only ever joins lines; it never splits, reorders, or rewords them.
Where a line might be a wrapped continuation, but also looks like the start of
a new block (a list marker, a block title, a description-list term, and so
on), the script leaves it alone and reports it for a human to judge.

Every rewritten file is checked against two invariants before it is written:

1. Its text is unchanged apart from whitespace.
2. It renders to the same HTML with Asciidoctor.js, apart from whitespace
   outside `<pre>` elements.

A file that fails the render check is not written. The script prints the HTML
difference instead, for review. Rerun with `--force <file>` to accept a
difference that is an improvement (typically, inline formatting that a wrap
had broken, and that now renders).

Usage:

    unwrap.py TS-1                 # Rewrite TS-1's page and partials.
    unwrap.py 1 --check            # Report, write nothing, exit 1 if wraps remain.
    unwrap.py template/            # Rewrite every .adoc file under a path.
    unwrap.py TS-1 --force src/modules/ROOT/partials/001/02-persistence.adoc
"""

from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
MODULE = REPO / 'src' / 'modules' / 'ROOT'
DEFAULT_CORE = REPO.parents[1] / 'website' / 'default' / 'node_modules' / '@asciidoctor' / 'core'
RENDER_JS = Path(__file__).resolve().parent / 'render.cjs'

VERBATIM_DELIM = re.compile(r'^(-{4,}|\.{4,}|\+{4,}|/{4,})$')
COMPOUND_DELIM = re.compile(r'^(={4,}|\*{4,}|_{4,}|--)$')
TABLE_DELIM = re.compile(r'^\|={3,}$')
OTHER_TABLE_DELIM = re.compile(r'^[!,:]={3,}$')
FENCE = re.compile(r'^(`{3,})')
ATTR_LIST = re.compile(r'^\[.*\]$')
BLOCK_TITLE = re.compile(r'^\.[^\s.]')
SECTION = re.compile(r'^={1,6}\s+\S')
ATTR_ENTRY = re.compile(r'^:!?[\w-]+!?:(\s|$)')
COMMENT = re.compile(r'^//')
DIRECTIVE = re.compile(r'^(include|ifdef|ifndef|ifeval|endif)::')
BLOCK_MACRO = re.compile(r'^[a-z][\w-]*::\S*\[.*\]$')
LIST_ITEM = re.compile(r'^\s*(\*+|\.+|-|\d+\.|[a-zA-Z]\.|[ivxIVX]+\)|<\d+>|<\.>)\s+\S')
DLIST = re.compile(r'^\s*\S.*?(:{2,4}|;;)(\s+\S.*)?$')
LIST_CONTINUATION = re.compile(r'^\+$')
BREAK = re.compile(r"^('{3,}|<{3})$")
ADMONITION = re.compile(r'^(NOTE|TIP|IMPORTANT|WARNING|CAUTION):\s')
CELL = re.compile(r'^[\d.*+<^>adehlmsv]*\|')
HARD_BREAK = re.compile(r'\s\+$')

# Block styles whose line structure is significant.
NOJOIN_STYLE = re.compile(r'^\[(\s*(verse|source|listing|literal|pass|stem|latexmath|asciimath)\b|[^\]]*%hardbreaks)')


@dataclass
class Result:
    path: Path
    before: str
    after: str
    joins: int = 0
    notes: list[str] = field(default_factory=list)


def is_structural(line: str) -> bool:
    """True for a line that starts, delimits, or annotates a block."""
    s = line.strip()
    return bool(
        VERBATIM_DELIM.match(s) or COMPOUND_DELIM.match(s) or TABLE_DELIM.match(s)
        or OTHER_TABLE_DELIM.match(s) or FENCE.match(s) or ATTR_LIST.match(s)
        or SECTION.match(line) or ATTR_ENTRY.match(line) or COMMENT.match(s)
        or DIRECTIVE.match(line) or BLOCK_MACRO.match(line) or LIST_ITEM.match(line)
        or LIST_CONTINUATION.match(s) or BREAK.match(s) or ADMONITION.match(line)
        or DLIST.match(line) or BLOCK_TITLE.match(s)
    )


def unwrap(path: Path, text: str) -> Result:
    res = Result(path, text, text)
    lines = text.split('\n')
    out: list[str] = []

    if re.search(r'^:hardbreaks(-option)?:', text, re.M):
        res.notes.append('document sets :hardbreaks-option: — file skipped')
        return res

    # Stack of open compound blocks and tables; verbatim blocks are consumed
    # in an inner loop instead, since nothing inside them is touched.
    stack: list[str] = []
    para_open = False       # The previous line is prose that the next may continue.
    para_kind = ''          # 'para', 'item', or 'cell'.
    nojoin = False          # The current paragraph keeps its line structure.
    hard_break = False      # The previous line ends with a hard line break.
    pending_nojoin = False  # A preceding attribute list styled the next block.

    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        lineno = i + 1
        in_table = bool(stack) and stack[-1] == '|==='

        # Blank line: ends the paragraph.
        if not s:
            out.append(line)
            para_open = nojoin = hard_break = False
            i += 1
            continue

        # Verbatim blocks: copy through to the matching delimiter. (A block
        # delimiter always interrupts a paragraph in Asciidoctor.)
        fence = FENCE.match(s)
        verbatim = None
        if fence:
            verbatim = fence.group(1)
        elif VERBATIM_DELIM.match(s) or OTHER_TABLE_DELIM.match(s):
            verbatim = s
        elif (COMPOUND_DELIM.match(s) or TABLE_DELIM.match(s)) and pending_nojoin:
            verbatim = s
        if verbatim is not None:
            out.append(line)
            i += 1
            while i < len(lines) and lines[i].strip() != verbatim:
                out.append(lines[i])
                i += 1
            if i < len(lines):
                out.append(lines[i])
                i += 1
            else:
                res.notes.append(f'{lineno}: unclosed delimited block {verbatim!r}')
            para_open = nojoin = hard_break = pending_nojoin = False
            continue

        # Compound blocks and tables: track nesting; their contents are prose.
        if COMPOUND_DELIM.match(s) or TABLE_DELIM.match(s):
            if stack and stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
            out.append(line)
            para_open = nojoin = hard_break = pending_nojoin = False
            i += 1
            continue

        # Table cells.
        if in_table and CELL.match(s):
            out.append(line)
            para_open = bool(s.split('|')[-1].strip())
            para_kind = 'cell'
            nojoin = False
            hard_break = bool(HARD_BREAK.search(line))
            i += 1
            continue

        # Continuation of an open paragraph.
        if para_open and not is_structural(line):
            if nojoin or hard_break:
                out.append(line)
            else:
                out[-1] = out[-1].rstrip() + ' ' + s
                res.joins += 1
            hard_break = bool(HARD_BREAK.search(line))
            i += 1
            continue

        if para_open and not nojoin:
            if COMMENT.match(s):
                res.notes.append(f'{lineno}: not joined across a line comment')
            elif not LIST_CONTINUATION.match(s) and (
                    para_kind == 'para' or (para_kind == 'cell' and LIST_ITEM.match(line))):
                res.notes.append(f'{lineno}: not joined; looks structural mid-paragraph: {s[:70]!r}')

        # A line that is not joined onto the one before it.
        out.append(line)
        i += 1
        hard_break = False

        if ATTR_LIST.match(s):
            pending_nojoin = pending_nojoin or bool(NOJOIN_STYLE.match(s))
            para_open = False
            continue

        if BLOCK_TITLE.match(s) and not LIST_ITEM.match(line):
            para_open = False
            continue

        if LIST_CONTINUATION.match(s) or COMMENT.match(s) or BREAK.match(s) \
                or ATTR_ENTRY.match(line) or DIRECTIVE.match(line) \
                or BLOCK_MACRO.match(line) or SECTION.match(line):
            para_open = pending_nojoin = False
            continue

        # This line starts a paragraph, list item, admonition, or dlist entry.
        if LIST_ITEM.match(line):
            para_kind = 'item'
        elif DLIST.match(line):
            para_kind = 'item'
            if not DLIST.match(line).group(2):
                para_open = False  # A bare `term::`; its body starts next line.
                continue
        else:
            para_kind = 'para'

        literal = line[:1].isspace() and para_kind == 'para'
        nojoin = pending_nojoin or literal
        pending_nojoin = False
        para_open = True
        hard_break = bool(HARD_BREAK.search(line))

    if stack:
        res.notes.append(f'unclosed block(s) at end of file: {stack}')
    res.after = '\n'.join(out)
    return res


def normalize_html(html: str) -> str:
    parts = re.split(r'(<pre\b.*?</pre>)', html, flags=re.S)
    return ''.join(p if p.startswith('<pre') else re.sub(r'\s+', ' ', p) for p in parts).strip()


def render(docs: dict[str, str], core: Path) -> dict[str, str]:
    proc = subprocess.run(
        ['node', str(RENDER_JS), str(core)],
        input=json.dumps(docs), capture_output=True, text=True, check=False,
    )
    if proc.returncode != 0:
        sys.exit(f'render failed:\n{proc.stderr}')
    return json.loads(proc.stdout)


def html_diff(a: str, b: str, limit: int = 40) -> str:
    split = lambda h: re.sub(r'>\s*', '>\n', h).split('\n')
    diff = list(difflib.unified_diff(split(a), split(b), 'before', 'after', lineterm='', n=1))
    more = f'\n    … {len(diff) - limit} more lines' if len(diff) > limit else ''
    return '\n'.join('    ' + d for d in diff[:limit]) + more


def target_files(target: str) -> list[Path]:
    m = re.fullmatch(r'(?:TS-?)?(\d{1,3})', target, re.I)
    if m:
        nnn = f'{int(m.group(1)):03d}'
        files = sorted((MODULE / 'pages').glob(f'{nnn}*.adoc'))
        files += sorted((MODULE / 'partials' / nnn).rglob('*.adoc'))
        if not files:
            sys.exit(f'no files found for TS-{int(nnn)}')
        return files
    p = Path(target).resolve()
    if p.is_dir():
        return sorted(p.rglob('*.adoc'))
    if p.is_file():
        return [p]
    sys.exit(f'not a standard number or a path: {target}')


def rel(p: Path) -> str:
    try:
        return str(p.relative_to(REPO))
    except ValueError:
        return str(p)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('target', help='a standard (TS-1, 1) or a path to a file or directory')
    ap.add_argument('--check', action='store_true', help='write nothing; exit 1 if any wraps remain')
    ap.add_argument('--force', action='append', default=[], metavar='FILE',
                    help='write FILE even if its rendering changes (repeatable)')
    ap.add_argument('--core', default=os.environ.get('ASCIIDOCTOR_CORE', str(DEFAULT_CORE)),
                    help='path to the @asciidoctor/core package (default: the website repo\'s copy)')
    args = ap.parse_args()

    core = Path(args.core)
    if not (core / 'package.json').is_file():
        sys.exit(f'@asciidoctor/core not found at {core}; install the website repo\'s dependencies, '
                 'or pass --core / set ASCIIDOCTOR_CORE')
    forced = {Path(f).resolve() for f in args.force}

    results = [unwrap(p, p.read_text()) for p in target_files(args.target)]
    changed = [r for r in results if r.after != r.before]

    for r in changed:
        if re.sub(r'\s+', ' ', r.before).strip() != re.sub(r'\s+', ' ', r.after).strip():
            sys.exit(f'BUG: non-whitespace change in {rel(r.path)}; nothing written')

    docs = {}
    for n, r in enumerate(changed):
        docs[f'{n}:before'] = r.before
        docs[f'{n}:after'] = r.after
    html = render(docs, core) if docs else {}

    written = rejected = 0
    for n, r in enumerate(results):
        status = 'unchanged'
        diff = ''
        if r in changed:
            k = changed.index(r)
            a, b = normalize_html(html[f'{k}:before']), normalize_html(html[f'{k}:after'])
            if a == b or r.path.resolve() in forced:
                status = f'{r.joins} joins' + ('' if a == b else ' (render differs; forced)')
                if not args.check:
                    r.path.write_text(r.after)
                    written += 1
            else:
                status = f'{r.joins} joins — REJECTED: render differs, not written'
                diff = html_diff(a, b)
                rejected += 1
        print(f'{rel(r.path)}: {status}')
        for note in r.notes:
            print(f'    {note}')
        if diff:
            print(diff)

    total = sum(r.joins for r in changed)
    verb = 'would join' if args.check else 'joined'
    print(f'\n{verb} {total} lines in {len(changed)} files; {written} written, {rejected} rejected')
    if args.check:
        return 1 if changed else 0
    return 1 if rejected else 0


if __name__ == '__main__':
    sys.exit(main())
