# Unwrap prose

**Temporary.** Migrates the standards, one at a time, from soft-wrapped prose
to one source line per paragraph, list item, and table cell, as now required
by TS-28 § Line length and wrapping. Delete this skill once every standard has
been converted.

The conversion is done by a script, [`scripts/unwrap.py`](./scripts/unwrap.py).
It only ever joins lines, never splits or rewords them, and it leaves verbatim
blocks, hard line breaks, and `verse`/`%hardbreaks` content alone. Before
writing each file, it checks that:

1. The text is unchanged apart from whitespace.
2. The file renders to the same HTML with Asciidoctor.js.

A file whose rendering changes is not written. The difference is shown for the
agent (or you) to judge: usually it is inline formatting that a wrap had
broken, which now renders correctly, and can be accepted with `--force`.

Lines that might be wrapped continuations but look like the start of a new
block — a list marker, a block title — are left alone and reported. The agent
resolves these by hand, along with AsciiDoc markup examples inside verbatim
blocks.

The script needs Node.js and `@asciidoctor/core`, which it borrows from the
website repository's `node_modules` by default.

## How to invoke

> Unwrap TS-1.

> Unwrap the next standard.

The script can also be run directly:

```sh
python3 .agents/skills/unwrap-prose/scripts/unwrap.py TS-1 --check  # Report only.
python3 .agents/skills/unwrap-prose/scripts/unwrap.py TS-1          # Rewrite.
python3 .agents/skills/unwrap-prose/scripts/unwrap.py template/     # Any path.
```

## Recommended models

The work is mostly mechanical. Any capable model will do.
