# TODO

Outstanding work across the technical standards in this repository: standards
that are still stubs (no substantive content written), and standards whose
`GAPS.md` gap analysis still has open items.

This file is a manually-maintained index, regenerated from the tree. The
counts below were last regenerated on **2026-08-13**. Re-derive them with the
script in [Regenerating this file](#regenerating-this-file) before trusting
them after any content work.

## Next batch

Agreed on 2026-08-13, not yet started: close the gaps in every remaining
standard holding **six or fewer** actionable items — sixteen standards, 48
gaps, one `close-gaps` run each. That clears the whole cheap tier and takes
the actionable total from 645 to 597.

| TS | Title | Actionable | Format | Notes |
| --- | --- | ---: | --- | --- |
| TS-46 | Distributed data and caching | 1 | Template | |
| TS-61 | AI tools | 1 | Legacy | |
| TS-3 | Design docs | 2 | Legacy | |
| TS-9 | Version control | 2 | Legacy | |
| TS-10 | Releasing | 2 | Legacy | |
| TS-11 | Versioning | 2 | Template | 8 out-of-scope, 1 unresolved |
| TS-14 | Performance testing | 2 | Legacy | |
| TS-49 | Cloud platform engineering | 2 | Legacy | |
| TS-8 | Issue tracking | 3 | Legacy | |
| TS-23 | Messages and events | 3 | Template | 2 out-of-scope |
| TS-2 | Software design qualities | 4 | Legacy | Legacy `**Status:**` syntax |
| TS-4 | Modeling | 4 | Template | 1 out-of-scope, 1 unresolved |
| TS-48 | Environment variables | 4 | Template | |
| TS-57 | Logging, monitoring, observability | 4 | Legacy | |
| TS-12 | Quality assurance | 6 | Legacy | |
| TS-31 | Unix shells and POSIX standards | 6 | Template | |

TS-38 and TS-44 also hold six or fewer, and are deliberately excluded: both
are stubs, and `close-gaps` stops on a stub because there is no structure to
extend. They are unblocked only by authoring those standards.

### What this batch will exercise for the first time

The nine runs completed so far all hit one narrow path — a single-gap,
legacy-format file with no status line. Four paths remain untested, and this
batch covers all of them. Expect the first round of reports to find defects
in `close-gaps` the way the earlier rounds did.

- **Template-format files** (TS-46, TS-11, TS-23, TS-4, TS-48, TS-31) skip
  the legacy conversion entirely.
- **A legacy file that already carries a status line** — only TS-2 and TS-5
  have one, in the older `**Status: … **` syntax, and the instruction to
  rewrite it has never run.
- **Multi-gap batching.** Every run so far closed exactly one gap.
- **Steps 8 and 9** — confirming out-of-scope items and re-fetching resources
  that failed. Eleven out-of-scope items and two unresolved resources sit in
  this batch, mostly in TS-11.

Out-of-scope items are decisions, not authoring work, so TS-11 and TS-4 will
come back partly as questions rather than finished content. That is the
design working, not a run failing.

## Stub standards

These pages have no substantive content yet — just a heading, `// TODO`
placeholder(s), and no `include::partial$NNN/...[]` includes.

| TS | Title | Notes |
| --- | --- | --- |
| [TS-24](src/modules/ROOT/pages/024.adoc) | User manuals | Has a short outline but is flagged to be split into separate Technical Documentation / User Documentation standards. |
| [TS-35](src/modules/ROOT/pages/035.adoc) | Python | Pure stub (`// Introduction.` placeholder only). |
| [TS-37](src/modules/ROOT/pages/037.adoc) | Web platform APIs | Pure stub aside from "See also" cross-references. Has a `GAPS.md` with 18 actionable items. |
| [TS-38](src/modules/ROOT/pages/038.adoc) | Node.js applications | Pure stub. `GAPS.md` explicitly notes this. |
| [TS-42](src/modules/ROOT/pages/042.adoc) | Vue | Pure stub (`// TODO: Introductory text…`). |
| [TS-44](src/modules/ROOT/pages/044.adoc) | Non-relational (NoSQL) databases | Pure stub. `GAPS.md` explicitly notes this. |
| [TS-55](src/modules/ROOT/pages/055.adoc) | Authentication and authorization | Pure stub (`// TODO` only). |

No open gap in any other standard's `GAPS.md` cross-references a stub, so the
stubs and the gap-closing work are independent. Writing a stub will not close
gaps recorded elsewhere — unlike TS-6, whose authoring closed six of TS-5's.

## Open gap analyses

Forty-one standards have a `GAPS.md`. Nine are fully resolved and are omitted
from the table below — TS-6, TS-13, TS-20, TS-25, TS-36, TS-41, TS-50, TS-52,
and TS-54. The other thirty-two have open items.

### The two GAPS.md formats

The files are in two formats, and the columns mean different things in each.
The counts below are of the thirty-two files with open items, tallying with
the table's rows. Of the nine fully-resolved files, only TS-6 is still in the
legacy format; the other eight were converted as they were worked.

- **Template format** (18 files). Follows the `gap-analysis` skill's bundled
  template: flat `- [ ]` checklists under `## Missing`, `## Partial`,
  `## Out-of-scope`, and `## Unresolved` headings.

- **Legacy format** (14 files). One `## <gap title>` subsection per gap, with
  `**Source**` / `**What the source says**` / `**Coverage check**` /
  `**Gap**` bullets, closed by appending a `**RESOLVED**` bullet. Some also
  carry a `**Cross-references**` field naming other standards the gap touches;
  the template format has no equivalent.

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
| [TS-38](src/modules/ROOT/partials/038/GAPS.md) | Node.js applications | 1 | — | — | Legacy — also a stub |
| [TS-46](src/modules/ROOT/partials/046/GAPS.md) | Distributed data and caching | 1 | 0 | 0 | Template |
| [TS-61](src/modules/ROOT/partials/061/GAPS.md) | AI tools | 1 | — | — | Legacy |
| [TS-3](src/modules/ROOT/partials/003/GAPS.md) | Design docs | 2 | — | — | Legacy |
| [TS-9](src/modules/ROOT/partials/009/GAPS.md) | Version control | 2 | — | — | Legacy |
| [TS-10](src/modules/ROOT/partials/010/GAPS.md) | Releasing | 2 | — | — | Legacy |
| [TS-11](src/modules/ROOT/partials/011/GAPS.md) | Versioning | 2 | 8 | 1 | Template |
| [TS-14](src/modules/ROOT/partials/014/GAPS.md) | Performance testing | 2 | — | — | Legacy |
| [TS-44](src/modules/ROOT/partials/044/GAPS.md) | Non-relational (NoSQL) databases | 2 | — | — | Legacy — also a stub |
| [TS-49](src/modules/ROOT/partials/049/GAPS.md) | Cloud platform engineering | 2 | — | — | Legacy |
| [TS-8](src/modules/ROOT/partials/008/GAPS.md) | Issue tracking | 3 | — | — | Legacy |
| [TS-23](src/modules/ROOT/partials/023/GAPS.md) | Messages and events | 3 | 2 | 0 | Template |
| [TS-2](src/modules/ROOT/partials/002/GAPS.md) | Software design qualities | 4 | — | — | Legacy — 1 of 5 resolved |
| [TS-4](src/modules/ROOT/partials/004/GAPS.md) | Modeling | 4 | 1 | 1 | Template |
| [TS-48](src/modules/ROOT/partials/048/GAPS.md) | Environment variables | 4 | 0 | 0 | Template |
| [TS-57](src/modules/ROOT/partials/057/GAPS.md) | Logging, monitoring, observability | 4 | — | — | Legacy |
| [TS-12](src/modules/ROOT/partials/012/GAPS.md) | Quality assurance | 6 | — | — | Legacy |
| [TS-31](src/modules/ROOT/partials/031/GAPS.md) | Unix shells and POSIX standards | 6 | 0 | 0 | Template |
| [TS-5](src/modules/ROOT/partials/005/GAPS.md) | Application architecture | 7 | — | — | Legacy — 6 of 13 resolved |
| [TS-7](src/modules/ROOT/partials/007/GAPS.md) | Code design | 13 | — | — | Legacy |
| [TS-27](src/modules/ROOT/partials/027/GAPS.md) | Markdown | 15 | 6 | 1 | Template |
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
| [TS-39](src/modules/ROOT/partials/039/GAPS.md) | HTML | 136 | 5 | 4 | Template |
| | **Total** | **645** | **115** | **43** | |

Eighteen of the thirty-two standards hold six or fewer actionable items each.
Seven standards — TS-39, TS-43, TS-16, TS-18, TS-33, TS-15, TS-21 — hold 466
of the 645 between them, and each needs several passes rather than one.

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

- **Assorted defects in TS-9**, found while retargeting its cross-references
  and left alone as out-of-scope: a bold-prose pseudo-link that should be an
  `<<...>>` reference (`13-pr-config.adoc:104`); "as little divergence as
  people" for "possible" (`10-workflows.adoc:673`); an em dash without
  surrounding spaces (`05-branches.adoc:425`); Markdown `**bold**` rather
  than AsciiDoc `*bold*`
  in five places; two over-80 lines that are not link macros; and three stale
  `// TODO:` comments about image consistency.

- **Link text that does not match the target's title.** Some cross-references
  label the target in title case (`TS-43: Relational Databases and SQL`)
  where the page's own title is sentence case (`TS-43: Relational databases
  and SQL`). Not audited in full.

- **Reference lists in a trailing partial.** `docs/style-guide.md` (lines
  150–153) says a reference list MUST NOT be split into a separate partial.
  Eight standards do exactly that: TS-17, TS-18, TS-21, TS-23, TS-29, TS-31,
  TS-32, and TS-33. Twenty-three pages carry a `== References` section.

- **A broken sentence in the `deep-dive` skill.**
  `.agents/skills/deep-dive/SKILL.md:55` reads "The mechanical verification in
  MUST have run" — a step reference has gone missing.

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
