# TODO

Outstanding work across the technical standards in this repository: standards
that are still stubs (no substantive content written), and standards whose
`GAPS.md` gap analysis still has open items.

This file is a manually-maintained index, regenerated from the tree. The
counts below were last regenerated on **2026-08-13** (same day as the prior
regeneration — this run closed TS-27's gaps, surfaced a previously-untracked
TS-10, and resolved several items in
[Known inconsistencies](#known-inconsistencies)). Re-derive them with the
script in [Regenerating this file](#regenerating-this-file) before trusting
them after any content work.

## Stub standards

These pages have no substantive content yet — just a heading, `// TODO`
placeholder(s), and no `include::partial$NNN/...[]` includes.

| TS | Title | Notes |
| --- | --- | --- |
| [TS-24](src/modules/ROOT/pages/024.adoc) | User manuals | Has a short outline but is flagged to be split into separate Technical Documentation / User Documentation standards. |
| [TS-35](src/modules/ROOT/pages/035.adoc) | Python | Pure stub (`// Introduction.` placeholder only). |
| [TS-37](src/modules/ROOT/pages/037.adoc) | Web platform APIs | Pure stub aside from "See also" cross-references. Has a `GAPS.md` with 18 actionable items. |
| [TS-38](src/modules/ROOT/pages/038.adoc) | Node.js applications | Pure stub. `GAPS.md` has 1 open gap (legacy format), not yet resolved. |
| [TS-39](src/modules/ROOT/pages/039.adoc) | HTML | Has substantive intro prose and `toc::[]`, but no `include::partial$` directives — the `partials/039/` directory holds only `GAPS.md`. Its `GAPS.md` carries 136 actionable items, the largest in the repository. |
| [TS-42](src/modules/ROOT/pages/042.adoc) | Vue | Pure stub (`// TODO: Introductory text…`). |
| [TS-44](src/modules/ROOT/pages/044.adoc) | Non-relational (NoSQL) databases | Pure stub. `GAPS.md` has 2 open gaps (legacy format), not yet resolved. |
| [TS-55](src/modules/ROOT/pages/055.adoc) | Authentication and authorization | Pure stub (`// TODO` only). |

No open gap in any other standard's `GAPS.md` cross-references a stub, so the
stubs and the gap-closing work are independent. Writing a stub will not close
gaps recorded elsewhere — unlike TS-6, whose authoring closed six of TS-5's.

TS-47 (Dates and times) also has no `include::partial$` directive, but is not
a stub: its page carries the standard's content directly, monolithically,
rather than via the `partials/NNN/` pattern. The mechanical check in
[Regenerating this file](#regenerating-this-file) flags it as a false
positive — verify by reading the page before trusting the grep alone.

## Open gap analyses

Forty-one standards have a `GAPS.md`. Twenty-five are fully resolved and are
omitted from the table below — TS-2, TS-3, TS-5, TS-6, TS-7, TS-8, TS-9,
TS-11, TS-12, TS-13, TS-14, TS-20, TS-23, TS-25, TS-31, TS-36, TS-41, TS-46,
TS-48, TS-49, TS-50, TS-52, TS-54, TS-57, and TS-61. The other fourteen have
open items — TS-37 and TS-39 are also stubs, so their open items live in the
table below but writing the standard is tracked separately, above.

TS-10 and TS-41 were previously omitted from this file entirely — an
oversight in an earlier regeneration, not a change in their content. TS-10
has 2 open actionable items (0 scope, 0 unresolved) and now appears in the
table below; TS-41 is fully resolved (0 unchecked items of any kind) and now
appears in the fully-resolved list above instead.

TS-38 and TS-44 were previously listed as fully resolved; that was wrong. Both
carry a genuinely open, unresolved legacy-format gap (1 for TS-38, 2 for
TS-44) — neither has ever been closed. They are not in the actionable-count
table below because both standards are stubs, and `close-gaps` stops on a
stub. They are tracked here instead, alongside the other stubs, until the
standard is authored.

### The two GAPS.md formats

The files are in two formats, and the columns mean different things in each.
The counts below are of the fourteen files with open items that are not
stubs, tallying with the table's rows. Of the twenty-five fully-resolved
files, only TS-6 is still in the legacy format; the other twenty-four were
converted as they were worked.

- **Template format** (38 files). Follows the `gap-analysis` skill's bundled
  template: flat `- [ ]` checklists under `## Missing`, `## Partial`,
  `## Out-of-scope`, and `## Unresolved` headings.

- **Legacy format** (3 files: TS-6, TS-38, TS-44). One `## <gap title>`
  subsection per gap, with `**Source**` / `**What the source says**` /
  `**Coverage check**` / `**Gap**` bullets, closed by appending a
  `**RESOLVED**` bullet. Some also carry a `**Cross-references**` field
  naming other standards the gap touches; the template format has no
  equivalent. TS-38 and TS-44 remain legacy because they are stubs —
  `close-gaps` stops on a stub, so there is no work that would trigger their
  conversion.

Legacy-format files are converted to the template format as they are worked,
not in a separate sweep.

### What the columns mean

- **Actionable** — `## Missing` plus `## Partial` items. Content that needs
  writing. This is the number to plan against. For legacy-format files it is
  every unresolved `## <gap title>` subsection, which mixes both kinds.

- **Scope** — `## Out-of-scope` items. Not authoring work: each is flagged
  for a human to confirm the exclusion or overrule it. Template format only.

- **Unresolved** — `## Unresolved` items. Reference resources that could not
  be retrieved when the analysis ran. Each needs re-fetching before it can
  become a gap or be dismissed. Template format only.

### Standards, ordered by actionable count

| TS | Title | Actionable | Scope | Unresolved | Format |
| --- | --- | ---: | ---: | ---: | --- |
| [TS-4](src/modules/ROOT/partials/004/GAPS.md) | Modeling | 0 | 0 | 1 | Template — 1 unresolved resource, repeatedly unfetchable |
| [TS-27](src/modules/ROOT/partials/027/GAPS.md) | Markdown | 0 | 6 | 1 | Template — all 15 actionable items closed 2026-08-13 |
| [TS-10](src/modules/ROOT/partials/010/GAPS.md) | Releasing | 2 | 0 | 0 | Template |
| [TS-40](src/modules/ROOT/partials/040/GAPS.md) | CSS | 17 | 12 | 1 | Template |
| [TS-37](src/modules/ROOT/partials/037/GAPS.md) | Web platform APIs | 18 | 4 | 1 | Template — also a stub |
| [TS-26](src/modules/ROOT/partials/026/GAPS.md) | Technical writing style guide | 29 | 10 | 2 | Template |
| [TS-29](src/modules/ROOT/partials/029/GAPS.md) | JSON Schema | 29 | 3 | 2 | Template |
| [TS-21](src/modules/ROOT/partials/021/GAPS.md) | HTTP APIs | 49 | 13 | 4 | Template |
| [TS-15](src/modules/ROOT/partials/015/GAPS.md) | User interfaces | 50 | 7 | 12 | Template |
| [TS-33](src/modules/ROOT/partials/033/GAPS.md) | Java | 55 | 3 | 4 | Template |
| [TS-18](src/modules/ROOT/partials/018/GAPS.md) | Web GUIs | 56 | 26 | 5 | Template |
| [TS-16](src/modules/ROOT/partials/016/GAPS.md) | Command line interfaces (CLIs) | 59 | 9 | 1 | Template |
| [TS-43](src/modules/ROOT/partials/043/GAPS.md) | Relational databases and SQL | 61 | 6 | 4 | Template |
| [TS-39](src/modules/ROOT/partials/039/GAPS.md) | HTML | 136 | 5 | 4 | Template — also a stub |
| | **Total** | **563** | **104** | **41** | |

TS-39 sits at the top by actionable count but is a stub — see
[Stub standards](#stub-standards) — so `close-gaps` cannot work it until the
standard has been authored. TS-4 and TS-27 both have zero actionable items
but stay in this table rather than joining the fully-resolved list, because
each has an unresolved resource still open — TS-4's reference directory no
longer exists anywhere in the repository and re-fetching it has failed on
every run so far; TS-27's is a stub reference file (see the file's
`## Unresolved` entry) not yet re-fetched.

TS-7 (Code design) and TS-41 were closed out on 2026-08-13 — all of TS-7's 13
actionable items resolved across two runs, TS-41 found already at zero — and
have left this table for the fully-resolved list.

TS-27 (Markdown) was closed out on 2026-08-13 — all 15 actionable items
resolved in one run — but stays in this table (at 0 actionable) because its
one unresolved item and six out-of-scope items remain open.

Three standards — TS-39, TS-43, TS-16 — hold 256 of the 563 between them, and
each needs several passes rather than one.

## Standards with neither a stub nor a GAPS.md

TS-1, TS-17, TS-19, TS-22, TS-28, TS-30, TS-32, TS-34, TS-45, TS-47, TS-51,
TS-53, TS-56, TS-58, TS-59, TS-60, TS-62, and TS-63 all have substantive
content and no recorded gap analysis. A gap analysis (`/gap-analysis`) could
be run against any of them; none is known to be missing content today.

## Known inconsistencies

Surfaced on 2026-08-13 while writing the `close-gaps` skill. These are
repo-level decisions and defects, not gap-closing work, but the first two
govern how all new content should be written.

- **RESOLVED — a dropped `include::` on the TS-27 page.**
  `pages/027.adoc` carried two `include::` directives on one source line, so
  `08-code.adoc` was absent from the built page and the second directive
  rendered as literal text. Split onto separate lines on 2026-08-13.

- **RESOLVED — cross-reference bold markup.** The style guide required
  `xref:NNN.adoc[*TS-N: Title*]` while all 237 cross-references in the corpus
  used `*xref:NNN.adoc[TS-N: Title]*`, the form it names as wrong. Settled on
  2026-08-13 in favor of the style guide: all 237 were converted, `AGENTS.md`
  was corrected to match, and three cross-references that were split across
  source lines were joined.

- **RESOLVED — self-referencing cross-references.** Thirty-one `xref:` macros
  pointed at the page containing them (30 in TS-9, 1 in TS-49), rendering as
  a link to the page the reader was already on. They predated the move to one
  merged page per standard. Changed on 2026-08-13 to use `<<Section title>>`,
  each verified to resolve to exactly one heading.

- **RESOLVED — eleven broken `<<...>>` references.** Found by resolving every
  in-prose `<<...>>` reference in the repository against the headings and
  anchors of its own standard. Fixed on 2026-08-13 by retargeting each to the
  section it meant:

  - **Stale leading-underscore IDs** (8 refs) — `<<_review>>` ×2 (TS-3),
    `<<_modeling-levels,…>>` (TS-4), `<<_behavior-driven-development,…>>`
    (TS-13), `<<_references,…>>` (TS-40), `<<_the_agents_md_standard,…>>` ×3
    (TS-61), and `<<_reasoning_thinking_and_effort,…>>` (TS-61). These used
    plain Asciidoctor's default ID scheme, which Antora overrides, so they
    resolved to nothing.

  - **An anchor that was never defined** (1 ref) —
    `<<principles,Principles of good CSS>>` (TS-40); the section's slug is
    `principles-of-good-css`.

  - **Natural references to titles that do not exist** (2 refs) —
    `<<The nature of the technology>>` (TS-61), whose section is actually
    titled "The inherent nature of the technology".

  Checking this needs care, and three classes of false positive cost real
  time before the number settled at eleven. A checker MUST model Antora's ID
  generation (`idprefix=''`, `idseparator='-'`, so `= Layout` becomes
  `layout`, not `_layout`); MUST recognize inline `[[id]]` anchors inside
  list items as well as `[#id]` on its own line; MUST treat an anchor
  immediately above a heading as replacing that heading's generated ID
  rather than competing with it; and MUST skip delimited blocks, since
  `<<FK>>` in TS-4's PlantUML is diagram syntax, not a cross-reference.
  Note also that TS-3 deliberately carries underscore-prefixed *explicit*
  anchors (`[#_context_and_scope]` and four siblings), which are valid and
  MUST NOT be "corrected".

- **RESOLVED — cross-references whose section title contains a comma.** Ten
  `<<...>>` references were parsed wrongly: Asciidoctor reads everything
  before the first comma as the target and the remainder as link text, so
  `<<Booleans, nulls, and implicit typing>>` targeted a section named
  "Booleans", which does not exist, and rendered as a broken reference.
  Three titles were affected — `Service topology: discovery, gateways, and
  service mesh` (TS-6, 2 refs), `Booleans, nulls, and implicit typing`
  (TS-30, 5 refs), and `Role-following, and its shadow` (TS-61, 3 refs).
  Fixed on 2026-08-13 by giving each section an explicit anchor
  (`[#service-topology]`, `[#implicit-typing]`, `[#role-following]`) and
  referencing it as `<<anchor-id,Full title>>`, which keeps the headings,
  the table of contents, and any external deep links unchanged. Retitling
  the sections to drop the commas was the alternative, and was rejected for
  that reason.

- **PARTIALLY RESOLVED — assorted defects in TS-9**, found while retargeting
  its cross-references and originally left alone as out-of-scope. Fixed on
  2026-08-13:

  - The bold-prose pseudo-link converted to an `<<...>>` reference
    (`13-pr-config.adoc:104`).
  - The typo "as little divergence as people" corrected to "possible"
    (`10-workflows.adoc:673`).
  - The unspaced em dash fixed to match the style guide's spaced convention
    (`05-branches.adoc:425`, with lines 424–426 reflowed).
  - Markdown `**bold**` converted to AsciiDoc `*bold*` — this turned out to
    be **17 instances**, not the five originally estimated, across
    `04-commits.adoc`, `05-branches.adoc`, `06-releases.adoc`,
    `08-integrations.adoc`, `10-workflows.adoc`, and `13-pr-config.adoc`.
  - One stale image-consistency placeholder resolved: the literal
    `<desc>TODO</desc>` in `images/009/branch-lines.svg` replaced with a real
    description.

  Two items remain open, both larger than originally scoped:

  - **Over-80-character lines.** The original note said "two... that are not
    link macros"; there are actually **75+ pre-existing lines** over the
    80-character soft limit spread across nearly every file in
    `partials/009/`. This is a standard-wide rewrap pass, not a two-line fix
    — tracked here as its own follow-up, not yet started.
  - **Stale `// TODO:` image-consistency comments.** Only two literal
    `// TODO:` comments exist (`03-repositories.adoc:19` and `:32`, both
    about `fork-and-clone.svg` and `repositories.svg`), and both are still
    valid: the two images are drawio-exported and visually inconsistent with
    TS-9's other hand-coded SVGs. Fixing this means redrawing the diagrams —
    a design task, not a text edit — and is not yet started.

- **RESOLVED — link text that did not match the target's title.** A full
  audit of all 384 `xref:NNN.adoc[...]` macros across `src/` against each
  target page's real title found exactly two title-casing mismatches, fixed
  on 2026-08-13: `pages/047.adoc:104` (TS-43 link text) and
  `partials/009/04-commits.adoc:168` (TS-1 link text). `index.adoc` and
  `nav.adoc` use their own distinct, already-correct title conventions and
  were left untouched.

- **Reference lists in a trailing partial.** `docs/style-guide.md` (lines
  150–153) says a reference list MUST NOT be split into a separate partial.
  Eight standards do exactly that: TS-17, TS-18, TS-21, TS-23, TS-29, TS-31,
  TS-32, and TS-33. Twenty-three pages carry a `== References` section.

- **RESOLVED — a broken sentence in the `deep-dive` skill.**
  `.agents/skills/deep-dive/SKILL.md:55` read "The mechanical verification in
  MUST have run" — the step reference had gone missing. Fixed on 2026-08-13
  to "The mechanical verification in step 8 MUST have run", matching how the
  rest of the document refers to its own numbered instructions.

- **The stub-detection script has a false positive.** `grep -L
  'include::partial\$'` also matches TS-47 (Dates and times), whose page
  carries its content monolithically rather than via `partials/NNN/`
  includes. TS-47 is complete, not a stub. TS-39 (HTML) was the opposite
  case — a genuine stub the script correctly flags, but which the previous
  version of this file omitted from the stub table. Both were reconciled by
  hand on 2026-08-13; re-verify by reading the page, not just the grep
  result, whenever this script's stub list changes.

- **RESOLVED — TS-38 and TS-44 wrongly listed as fully resolved.** A prior
  regeneration of this file's "Open gap analyses" section listed TS-38 and
  TS-44 among the twenty-five fully-resolved standards. Neither is: TS-38's
  `GAPS.md` has one open legacy-format gap and TS-44's has two, and neither
  file has ever carried a `**RESOLVED**` marker. Both are stubs, so
  `close-gaps` cannot action them until the standard is authored; corrected
  on 2026-08-13 to note the open gaps against each in the stub table instead
  of silently dropping them from tracking.

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
items. TS-4 is the example that makes this distinction matter: it has 0
actionable items but 1 unresolved resource still unchecked, so it stays in
the open-items table. A legacy-format file must be checked the same way —
count `## <gap title>` subsections against `**RESOLVED**` markers, per the
script above — rather than assumed resolved because it is short or old:
TS-38 and TS-44 were wrongly marked fully resolved in a prior pass for
exactly this reason.
