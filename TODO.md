# TODO

> **Next up:** TS-21 gaps.

Outstanding work across the technical standards in this repository: standards
that are still stubs (no substantive content written), and standards whose
`GAPS.md` gap analysis still has open items.

This file is a manually-maintained index, regenerated from the tree. The
counts below were last regenerated on **2026-08-14** — this run closed all 29
of TS-26's actionable items across three `close-gaps` batches, the last of
which also reversed and closed 4 of TS-26's original 9 out-of-scope items at
the user's explicit direction, importing a roughly 1,373-entry A-Z glossary
as a new partial (see the table note below); a fifth out-of-scope item was
confirmed out-of-scope and its gap routed instead to TS-15, adding 1 new
actionable item there (50 → 51). This is on top of the same-day closure of
TS-29's gaps in full (29 actionable items and all 3 out-of-scope items
resolved, across four `close-gaps` batches plus a follow-up decision pass on
the out-of-scope items and the one remaining Partial item), TS-43's gaps in
full, TS-16's actionable items in full (1 out-of-scope batch and 1 unresolved
resource remain), and 16 of TS-40's 17 (the last declined, see
[Known inconsistencies](#known-inconsistencies)).
Re-derive the counts with the script in
[Regenerating this file](#regenerating-this-file) before trusting them after
any content work.

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

Forty-one standards have a `GAPS.md`. Twenty-seven are fully resolved and are
omitted from the table below — TS-2, TS-3, TS-5, TS-6, TS-7, TS-8, TS-9,
TS-10, TS-11, TS-12, TS-13, TS-14, TS-20, TS-23, TS-25, TS-31, TS-36, TS-41,
TS-43, TS-46, TS-48, TS-49, TS-50, TS-52, TS-54, TS-57, and TS-61. The other
twelve have open items — TS-37 and TS-39 are also stubs, so their open items
live in the table below but writing the standard is tracked separately,
above.

TS-29 is now fully worked — all 29 actionable items and all 3 out-of-scope
items are resolved — but it stays in the open-items table below, not the
fully-resolved list, because its 2 unresolved YouTube references keep it
short of zero unchecked items of *any* kind. See
[What the columns mean](#what-the-columns-mean) for why that distinction
matters, and TS-4/TS-16/TS-27 for the same shape.

TS-10 and TS-41 were previously omitted from this file entirely — an
oversight in an earlier regeneration, not a change in their content. TS-41
was fully resolved (0 unchecked items of any kind) as soon as it was
restored to tracking, and appears in the fully-resolved list above. TS-10
had 2 open actionable items when restored; both were closed on 2026-08-13 by
a `close-gaps` run, which found the content had already been written into
TS-5 and TS-57's own directories, so TS-10 itself needed no change. It now
also appears in the fully-resolved list above.

TS-38 and TS-44 were previously listed as fully resolved; that was wrong. Both
carry a genuinely open, unresolved legacy-format gap (1 for TS-38, 2 for
TS-44) — neither has ever been closed. They are not in the actionable-count
table below because both standards are stubs, and `close-gaps` stops on a
stub. They are tracked here instead, alongside the other stubs, until the
standard is authored.

### The two GAPS.md formats

The files are in two formats, and the columns mean different things in each.
The counts below are of the ten non-stub files with open items, tallying
with the table's rows (TS-37 and TS-39 are also stubs, so twelve rows total).
Of the twenty-seven fully-resolved files, only TS-6 is still in the legacy
format; the other twenty-six were converted as they were worked.

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
| [TS-16](src/modules/ROOT/partials/016/GAPS.md) | Command line interfaces (CLIs) | 0 | 9 | 1 | Template — all 59 actionable items closed 2026-08-14 |
| [TS-26](src/modules/ROOT/partials/026/GAPS.md) | Technical writing style guide | 0 | 6 | 2 | Template — all 29 actionable items closed 2026-08-14, across three batches; 4 of 9 out-of-scope items also reversed and closed |
| [TS-27](src/modules/ROOT/partials/027/GAPS.md) | Markdown | 0 | 6 | 1 | Template — all 15 actionable items closed 2026-08-13 |
| [TS-29](src/modules/ROOT/partials/029/GAPS.md) | JSON Schema | 0 | 0 | 2 | Template — all 29 actionable and all 3 out-of-scope items closed 2026-08-14 |
| [TS-40](src/modules/ROOT/partials/040/GAPS.md) | CSS | 1 | 12 | 0 | Template — 16 of 17 actionable items closed 2026-08-14; 1 declined and left open |
| [TS-37](src/modules/ROOT/partials/037/GAPS.md) | Web platform APIs | 18 | 4 | 1 | Template — also a stub |
| [TS-21](src/modules/ROOT/partials/021/GAPS.md) | HTTP APIs | 49 | 13 | 4 | Template |
| [TS-15](src/modules/ROOT/partials/015/GAPS.md) | User interfaces | 51 | 7 | 12 | Template — gained 1 item 2026-08-14, routed in from TS-26 |
| [TS-33](src/modules/ROOT/partials/033/GAPS.md) | Java | 55 | 3 | 4 | Template |
| [TS-18](src/modules/ROOT/partials/018/GAPS.md) | Web GUIs | 56 | 26 | 5 | Template |
| [TS-39](src/modules/ROOT/partials/039/GAPS.md) | HTML | 136 | 5 | 4 | Template — also a stub |
| | **Total** | **366** | **91** | **37** | |

TS-29 (JSON Schema) was closed out on 2026-08-14 across four `close-gaps`
batches plus a same-day follow-up: the first batch closed the eight
core-vocabulary items (Validation, Applicator, Boolean composition,
if/then/else, dependentRequired/dependentSchemas, Meta-Data/Annotations,
`format`, and Content); the second closed Unevaluated keywords, Core
keywords (`$id`/`$comment`/`$defs`/`$anchor`/`$dynamicAnchor`/`$dynamicRef`/
`$vocabulary`), validator tooling, and JSON Patch, plus the composition and
schema-boilerplate Partial items; the third closed Schema versioning, six
LinkedIn best-practices items, and the JTD Partial item; the fourth closed
four PayPal-sourced modeling-pattern items (monetary values, phone numbers,
vendor-prefixed `format`, error/envelope schemas) and a file-organization
item, with the user choosing a new prose "Modeling patterns" section over an
`examples/` subdirectory. All three Out-of-scope items were then confirmed
by the user: CloudEvents and storage-platform concerns excluded outright
(storage platforms flagged as a candidate for a future gap analysis of the
relational-databases standard, not actioned there), and validation-code APIs
excluded from normative coverage but given a one-sentence mention in
`21-useful-links.adoc` at the user's request. The last open Partial item
(`tour.json-schema.org`) was dismissed once the user identified the source
as an interactive playground rather than fetchable reference material. TS-29
stays out of the fully-resolved list only because 2 Unresolved YouTube
references remain unfetchable. TS-29's partials were renumbered four times
over the course of this work — see the page's `include::` list for the
current mapping, not any historical numbering cited in old commit messages.

TS-26 (Technical writing style guide) was closed out on 2026-08-14 — all 29
actionable items resolved — across three `close-gaps` batches. The first
closed the comma/quotation-mark/apostrophe/dash/hyphenation/
exclamation-question-mark/colon-capitalization cluster (all in
`13-punctuation.adoc`), plus abbreviation mechanics, dates/numbers,
code-block formatting, emphasis/typography, and referencing mechanics. The
second closed that/which, collective-noun agreement, overused words, and
sentence fragments (all in `14-sentences-and-paragraphs.adoc`), contractions
and a passive-voice detection heuristic (`01-voice-and-tense.adoc`), heading
formatting and acronym expansion (`02-headings.adoc`), and nested/variable
lists (`08-lists.adoc`) — one item in that batch, the list-period rule,
needed no change since `08-lists.adoc` already covered it. The third closed
the two remaining Partial items — commonly-confused words and
person-first/gender-neutral language — and, at the user's explicit
direction, reversed 4 of the file's 9 Out-of-scope items (honorifics/
titles, place/country names, sports/currencies/measures, and the A-Z
spelling list itself) by importing the full ~1,373-entry A-Z word list from
`9999-reference.md` as a new `16-glossary.adoc` partial, merged with
overlapping content from `OLD-NOTES.md`/`OLD-NOTES-2.md`. A fifth
Out-of-scope item — `copywriting.adoc`'s UI/short-message conventions — was
confirmed out-of-scope for TS-26 (its content is UI microcopy register, not
documentation prose) and instead routed to TS-15 (User interfaces) as a new
Missing item there, at the user's request. TS-26 stays in this table, not
the fully-resolved list, because its remaining 6 Out-of-scope items and 2
Unresolved YouTube-adjacent references keep it short of zero unchecked
items of any kind — the same shape as TS-4, TS-16, TS-27, and TS-29.

TS-39 sits at the top by actionable count but is a stub — see
[Stub standards](#stub-standards) — so `close-gaps` cannot work it until the
standard has been authored. TS-4, TS-16, and TS-27 all have zero actionable
items but stay in this table rather than joining the fully-resolved list,
because each has an unresolved resource still open — TS-4's reference
directory no longer exists anywhere in the repository and re-fetching it has
failed on every run so far; TS-16's is `Program-Behavior.html`, still
unfetchable as of the 2026-08-14 run (not re-attempted, since its content was
already captured via a sub-agent in a prior run); TS-27's is a stub reference
file (see the file's `## Unresolved` entry) not yet re-fetched. TS-29 and
TS-26 now join this group for the same reason — two unfetched references
each: YouTube for TS-29; for TS-26, a binary PDF with no text-extraction
tool available, and a set of link-collection files whose ~40 linked URLs
were never individually fetched.

TS-40 (CSS) had 16 of 17 actionable items closed on 2026-08-14. The one
remaining item — a comparative summary of OOCSS/BEM/SMACSS/SUIT CSS
methodologies — was explicitly declined as scope creep (the standard
prescribes its own methodology, not a survey of others; see
[Known inconsistencies](#known-inconsistencies)) and left unticked in
`GAPS.md`, so it stays in this table at Actionable=1 rather than joining the
fully-resolved list. All 12 out-of-scope items and its one placeholder
"Unresolved" entry (no reference resources were actually left unfetched) are
otherwise settled.

TS-16 (Command line interfaces) was closed out on 2026-08-14 — all 59
actionable items (9 Missing, 50 Partial) resolved in one run across 8 of its
11 partials — but stays in this table (at 0 actionable) because its 9
out-of-scope items and 1 unresolved reference remain open.

TS-7 (Code design) and TS-41 were closed out on 2026-08-13 — all of TS-7's 13
actionable items resolved across two runs, TS-41 found already at zero — and
have left this table for the fully-resolved list.

TS-27 (Markdown) was closed out on 2026-08-13 — all 15 actionable items
resolved in one run — but stays in this table (at 0 actionable) because its
one unresolved item and six out-of-scope items remain open.

TS-10 (Releasing) was closed out on 2026-08-13 — both actionable items
turned out to already be resolved in TS-5 and TS-57's own directories, so
TS-10 needed no content of its own — and has left this table for the
fully-resolved list.

One standard — TS-39 — now holds 136 of the 366 actionable items on its own,
over a third of the total, and will need several passes once it is authored.
TS-18 (56) and TS-15 (51) are next largest.

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
  TS-32, and TS-33 (TS-29's own references live in `20-references.adoc` as
  of the 2026-08-14 gap-closing work, having been renumbered four times).
  Twenty-three pages carry a `== References` section.

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

- **DECLINED — TS-40's methodology-comparison gap.** A `close-gaps` run on
  2026-08-14 closed 16 of TS-40's 17 actionable items. The remaining one
  proposed expanding `01-overview.adoc` into a comparative summary of
  OOCSS/BEM/SMACSS/SUIT CSS. The item's own text flagged it as borderline
  (the standard's purpose is to prescribe its own methodology, not survey
  others); on review, declined for that reason and left open — `- [ ]`,
  unticked — in TS-40's `GAPS.md` with a dated rationale note, rather than
  resolved or deleted. TS-40 stays in the actionable-count table at 1
  pending any future reversal of this decision.

- **RESOLVED — TS-43 closed out in one run.** All 61 of TS-43's actionable
  items (59 Missing, 2 Partial) were closed by a `close-gaps` run on
  2026-08-14, across six new content partials
  (`02-sql-style.adoc` through `07-transactions-and-consistency.adoc`). One
  genuine naming conflict surfaced mid-run — general column-naming guidance
  says avoid a bare `id`, while primary-key guidance mandates it — resolved
  by scope: `id` is reserved for the primary key, every other identifier
  column follows the descriptive-naming rule. TS-43 moved to the
  fully-resolved list; its 6 out-of-scope and 4 persistently-unfetchable
  reference items remain open in its own `GAPS.md`, since neither is an
  actionable count.

- **RESOLVED — TS-16 closed out in one run.** All 59 of TS-16's actionable
  items (9 Missing, 50 Partial) were closed by a `close-gaps` run on
  2026-08-14, extending 8 of its 11 existing partials (no new partial or
  page edit was needed). GNU Coding Standards is cited generically as an
  index-page reference in `016.adoc`'s `== References`, while several newly
  closed sections cite specific GNU sub-pages (`--version`,
  `Command-Line-Interfaces`); the existing index-page citation was judged
  sufficient provenance rather than adding near-duplicate entries — worth a
  second look if a future `deep-dive` pass audits the reference list. TS-16
  stays in the actionable-count table at 0 because its 9 out-of-scope items
  and 1 unresolved reference (`Program-Behavior.html`, persistently
  unfetchable) remain open.

- **RESOLVED — TS-29 closed out across four runs plus a decision pass.**
  All 29 of TS-29's actionable items were closed by four `close-gaps`
  batches on 2026-08-14 (8, 6, 8, and 5 items respectively — see the table
  note above for the breakdown), followed by the same-day resolution of all
  3 Out-of-scope items and the 1 remaining Partial item on the user's
  explicit direction. TS-29's partials were renumbered four times over the
  course of this work (`03`–`08` inserted first, then `05`–`06`, then
  `17`–`18`, then `19`); always verify against the page's current
  `include::` list rather than any historical `NN-` prefix cited in an
  older resolution note. TS-29 stays out of the fully-resolved list only
  because its 2 Unresolved YouTube references remain unfetchable — an
  identical situation to TS-4, TS-16, and TS-27.

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
the open-items table. TS-29 is the same shape after its 2026-08-14
gap-closing work: 0 actionable, 0 out-of-scope, but 2 Unresolved references
still unchecked. A legacy-format file must be checked the same way — count
`## <gap title>` subsections against `**RESOLVED**` markers, per the script
above — rather than assumed resolved because it is short or old: TS-38 and
TS-44 were wrongly marked fully resolved in a prior pass for exactly this
reason.
