# TODO

Outstanding work across the technical standards in this repository: standards
that are still stubs (no substantive content written), and standards whose
`GAPS.md` gap analysis still has open items.

This file is a manually-maintained index, regenerated from the tree. The
counts below were last regenerated on **2026-08-15**, after `close-gaps` runs
against TS-15 and TS-26 closed all of TS-15's remaining Missing items and all
but one of TS-26's — the last was re-scoped as documentation lifecycle/process
content and routed to TS-25's `GAPS.md` instead, since it didn't fit TS-26's
sentence-level style scope. TS-26 is now fully resolved; TS-15 drops to a
single deliberately-open Out-of-scope placeholder; TS-25 picks up the one
routed item. See [the table below](#standards-ordered-by-actionable-count) for
what remains.

Re-derive the counts with the script in
[Regenerating this file](#regenerating-this-file) before trusting them after
any content work.

## Stub standards

These pages have no substantive content yet — just a heading, `// TODO`
placeholder(s), and no `include::partial$NNN/...[]` includes.

No standard is currently in this state. TS-39 (HTML) was the last remaining
stub, authored from scratch on 2026-08-14. This table has been empty since
that run.

TS-47 (Dates and times) also has no `include::partial$` directive, but is not
a stub: its page carries the standard's content directly, monolithically,
rather than via the `partials/NNN/` pattern. The mechanical check in
[Regenerating this file](#regenerating-this-file) flags it as a false
positive — verify by reading the page before trusting the grep alone.

## Open gap analyses

Forty-two standards have a `GAPS.md`. Nine of them currently carry open items
of some kind: TS-7, TS-14, TS-15, TS-16, TS-18, TS-19, TS-25, TS-40 for
actionable/scope items still open, plus TS-38 for its known false-negative
(see below).

### The two GAPS.md formats

The files are in two formats, and the columns mean different things in each.

- **Template format** (39 files). Follows the `gap-analysis` skill's bundled
  template: flat `- [ ]` checklists under `## Missing`, `## Partial`,
  `## Out-of-scope`, and `## Unresolved` headings.

- **Legacy format** (3 files: TS-6, TS-38, TS-44, all fully resolved). One
  `## <gap title>` subsection per gap, with `**Source**` /
  `**What the source says**` / `**Coverage check**` / `**Gap**` bullets,
  closed by appending a `**RESOLVED**` (or, in TS-38's case,
  `**RESOLVED.**` — the mechanical script only matches the bare form; see
  [Regenerating this file](#regenerating-this-file)) bullet. Some also carry
  a `**Cross-references**` field naming other standards the gap touches; the
  template format has no equivalent.

Legacy-format files are converted to the template format as they are worked,
not in a separate sweep.

### What the columns mean

- **Actionable** — `## Missing` plus `## Partial` items. Content that needs
  writing. This is the number to plan against. For legacy-format files it is
  every unresolved `## <gap title>` subsection, which mixes both kinds.

- **Scope** — `## Out-of-scope` items. Not authoring work: each is flagged
  for a human to confirm the exclusion or overrule it.

- **Unresolved** — `## Unresolved` items. Reference resources that could not
  be retrieved when the analysis ran, or open scope questions not yet
  settled by the user.

### Standards, ordered by actionable count

| TS | Title | Actionable | Scope | Unresolved | Notes |
| --- | --- | ---: | ---: | ---: | --- |
| [TS-18](src/modules/ROOT/partials/018/GAPS.md) | Web GUIs | 3 | 0 | 0 | Unchanged since the 2026-08-15 `close-gaps` run. 3 items deliberately deferred: DOM/scripting/fetch/CORS (placement undecided between TS-18 and TS-37), and two items (Windows app design, Shopify Polaris) needing an assessment pass before writing. |
| [TS-19](src/modules/ROOT/partials/019/GAPS.md) | SEO | 3 | 0 | 0 | Unchanged since the file was created 2026-08-15 to receive routed items — no `gap-analysis` run of its own yet. |
| [TS-40](src/modules/ROOT/partials/040/GAPS.md) | CSS | 3 | 0 | 0 | Unchanged since the 2026-08-15 sweep. |
| [TS-14](src/modules/ROOT/partials/014/GAPS.md) | Performance testing | 2 | — | — | Unchanged since the 2026-08-15 sweep. |
| [TS-16](src/modules/ROOT/partials/016/GAPS.md) | Command line interfaces (CLIs) | 1 | 0 | 0 | Unchanged since the 2026-08-15 sweep. |
| [TS-7](src/modules/ROOT/partials/007/GAPS.md) | Code design | 1 | — | — | Unchanged since the 2026-08-15 sweep. |
| [TS-25](src/modules/ROOT/partials/025/GAPS.md) | Technical documentation | 1 | 0 | 0 | New row. Gained 1 Missing item on 2026-08-15, routed in from TS-26 while TS-26 was working its own Out-of-scope backlog: documentation process philosophy (keeping docs fresh, deleting cruft, doc-review etiquette) — lifecycle/process content, not sentence-level style, per both standards' own stated scope split. Not yet actioned. |
| [TS-15](src/modules/ROOT/partials/015/GAPS.md) | User interfaces | 0 | 1 | 0 | All 5 Missing items closed 2026-08-15 (`close-gaps`): trust-over-time principle, AI-experience design, user research (planning/conducting, personas, website audits). Only the one deliberately-open Out-of-scope item remains (design.google project-narrative essays, pending a fetch-and-reassess pass) — kept in this table for that reason alone. |
| | **Total** | **14** | **1** | **0** | |

Every other standard with a `GAPS.md` (33 of the 42) is fully resolved: zero
unchecked items of any kind. TS-26 joined that list on 2026-08-15 — all of
its Missing items were either closed or routed to another standard's
`GAPS.md`, and no Out-of-scope items remain open.

## Standards with neither a stub nor a GAPS.md

TS-1, TS-17, TS-22, TS-24, TS-28, TS-30, TS-32, TS-34, TS-35, TS-42, TS-45,
TS-47, TS-51, TS-53, TS-55, TS-56, TS-58, TS-59, TS-60, TS-62, and TS-63 all
have substantive content and no recorded gap analysis. A gap analysis
(`/gap-analysis`) could be run against any standard on this list; none is
known to be missing content today.

## Known inconsistencies

Surfaced on 2026-08-13 while writing the `close-gaps` skill, and added to
since. These are repo-level decisions and defects, not gap-closing work, but
the first two govern how all new content should be written.

- **The stub-detection script has a false positive.** `grep -L
  'include::partial\$'` also matches TS-47 (Dates and times), whose page
  carries its content monolithically rather than via `partials/NNN/`
  includes. TS-47 is complete, not a stub. Re-verify by reading the page,
  not just the grep result, whenever this script's stub list changes.

- **Reference lists in a trailing partial.** `docs/style-guide.md` (lines
  150–153) says a reference list MUST NOT be split into a separate partial.
  Eight standards do exactly that: TS-17, TS-18, TS-21, TS-23, TS-29, TS-31,
  TS-32, and TS-33. Twenty-three pages carry a `== References` section.

- **DECLINED — TS-40's methodology-comparison gap.** A `close-gaps` run on
  2026-08-14 closed 16 of TS-40's 17 actionable items. The remaining one
  proposed expanding `01-overview.adoc` into a comparative summary of
  OOCSS/BEM/SMACSS/SUIT CSS; declined as borderline and left open with a
  dated rationale note. Superseded in practice by 2026-08-15's broader
  pending scope-broadening decision for TS-40, which would touch the same
  overview section if formalized.

- **The legacy-format script has one known false negative.** It matches the
  literal string `**RESOLVED**`, but TS-38's `GAPS.md` closes its one gap
  with `**RESOLVED.**` (the period sits inside the bold markup, not after
  it) — the only file in the repository written that way. The script
  reports TS-38 as `actionable=1` even though the gap is genuinely closed;
  verify any legacy file the script reports as non-zero by reading it
  before trusting the count.

- **Do not conclude a local `__TODO__/` reference is permanently gone from a
  Git-scoped search alone.** `~/local.gitignore` (a global, machine-level
  gitignore) hides the entire `__TODO__/` tree from `git status`, `git log
  --all`, and any other Git-aware search, even though the tree is fully
  present and readable on disk. Always additionally check with a plain
  filesystem `find` (not `git`-scoped) before recording a local reference as
  unrecoverable. Discovered 2026-08-15; see this file's own version history
  for the full account of standards affected.

Earlier entries in this section — covering broken cross-references, dropped
`include::` directives, markdown-vs-AsciiDoc bold-markup cleanup,
self-referencing xrefs, comma-in-heading xref parsing, TS-9's formatting
defects, and TS-16/TS-27/TS-33/TS-37/TS-38/TS-43/TS-44's individual
`close-gaps` histories — are resolved and have been trimmed from this file;
consult Git history or each standard's own `GAPS.md` for the detail.

## Regenerating this file

Run from `src/modules/ROOT/partials/`:

```sh
for d in $(ls -d [0-9][0-9][0-9]/ | sort); do
  n="${d%/}"; g="$n/GAPS.md"; [ -f "$g" ] || continue
  if grep -q '^## Missing$' "$g"; then
    awk -v n="$n" '
      /^## /   { s = substr($0, 4) }
      /^- \[ \]/ { c[s]++ }
      END { printf "%s template actionable=%d scope=%d unresolved=%d\n",
              n, c["Missing"] + c["Partial"], c["Out-of-scope"],
              c["Unresolved"] }' "$g"
  else
    awk -v n="$n" '
      /^## /            { total++; resolved_here = 0 }
      /\*\*RESOLVED\*\*/ { if (!resolved_here) { done++; resolved_here = 1 } }
      END { printf "%s legacy actionable=%d\n", n, total - done }' "$g"
  fi
done
```

**Do not stop at the per-standard `actionable=`/`scope=`/`unresolved=`
breakdown above.** Also run a plain total-unchecked count per file —
`grep -c '^- \[ \]' <NNN>/GAPS.md` — and compare it against
`actionable + scope + unresolved` for that same file. A mismatch means the
per-heading `awk` count and the flat count disagree, which usually means a
checklist item exists outside the four recognized `## ` headings, or that a
heading name was typo'd, **or that an edit intended to tick an item silently
failed to apply**. Trust the grep over any standard's own narrative Status
line, and re-run the grep after every batch of edits, not just once at the
end.

Note that a standard can show `scope > 0` while its flat unchecked-count is
`0` — TS-43 is the current example. Its 6 held Out-of-scope items (pending a
possible new DBA/database-administration standard) are ticked `[x]` with a
note explaining the hold, per the "held pending a possible new standard"
disposition from the 2026-08-15 Out-of-scope sweep: decided, but not yet
actionable anywhere. That is different from TS-15's one item, which is
genuinely unticked and awaiting a decision. Only a genuinely unticked item
belongs in the open-items table for the "scope" reason; a ticked-but-held
item does not, since the per-heading `awk` script above only counts `- [ ]`
lines regardless of which disposition ticked the others.

Stub standards are those whose page has no `include::partial$` directive:

```sh
grep -L 'include::partial\$' src/modules/ROOT/pages/[0-9][0-9][0-9].adoc
```

This grep has one known false positive — TS-47, whose content is written
directly on the page rather than via partials. Verify each hit by reading the
page before adding it to the stub table: a stub has a `// TODO` placeholder
and essentially no prose; a false positive like TS-47 has complete sections.

A standard is "fully resolved" when its `GAPS.md` has zero unchecked items of
*any* kind — `grep -c '^- \[ \]'` returns 0 — not merely zero actionable
items. TS-15 is the current example that makes this distinction matter: it
has 0 actionable items and 1 deliberately-open Out-of-scope item, so it still
belongs in the open-items table despite having no content work left.

The legacy-format script also has one known false negative: it matches the
literal string `**RESOLVED**`, but TS-38's `GAPS.md` closes its one gap with
`**RESOLVED.**` (the period sits inside the bold markup, not after it) — the
only file in the repository written that way. The script reports TS-38 as
`actionable=1` even though the gap is genuinely closed; verify any legacy
file the script reports as non-zero by reading it before trusting the count,
the same caution the script's template branch already needs for its
Out-of-scope/Unresolved blind spots.

**To find standards with substantive content but no gap analysis**, diff the
standards that have a page against the standards that have a `GAPS.md`:

```sh
ls src/modules/ROOT/pages/[0-9][0-9][0-9].adoc | xargs -n1 basename | sed 's/\.adoc//' | sort > /tmp/all_ts.txt
ls src/modules/ROOT/partials/*/GAPS.md | sed -E 's#.*partials/([0-9]+)/GAPS.md#\1#' | sort > /tmp/gaps_ts.txt
comm -23 /tmp/all_ts.txt /tmp/gaps_ts.txt
```

Cross-check the result against the stub list — a standard in both is a stub
awaiting authorship, not a candidate for `gap-analysis`. Re-run this diff
every time, rather than trusting the previous run's list by hand.

**Do not conclude a local `__TODO__/` reference is permanently gone from a
Git-scoped search alone.** `~/local.gitignore` (a global, machine-level
gitignore) hides the entire `__TODO__/` tree from `git status`, `git log
--all`, and any other Git-aware search, even though the tree is fully
present and readable on disk. Always additionally check with a plain
filesystem `find` (not `git`-scoped) before recording a local reference as
unrecoverable.
