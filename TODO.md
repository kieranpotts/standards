# TODO

Outstanding work across the technical standards in this repository: standards
that are still stubs (no substantive content written), and standards whose
`GAPS.md` gap analysis still has open items.

This file is a manually-maintained index, regenerated from the tree. The
counts below were last regenerated on **2026-08-15**, after a fourth
`close-gaps` wave (TS-26, TS-15, TS-18) closed all 7 of their combined open
`## Missing`/`## Partial` items, at the user's explicit direction to
"complete all remaining open items — both missing and partial." TS-40's one
remaining Partial item was deliberately left declined, per the user's
explicit choice, rather than reversed. **Every standard in this repository
now has 0 actionable (`## Missing`/`## Partial`) items**, except TS-40's one
declined item. What remains open across the repository is entirely
`## Out-of-scope` items (79, awaiting a human confirm/overrule decision) and
`## Unresolved` items (1, TS-18's un-individually-assessed webstyleguide.com
chapters) — no further content-writing work is outstanding.

Before that run, two `close-gaps` batch runs (TS-43, then TS-33) closed all
15 of their combined open `## Missing` items, and a full mechanical re-scan
of every open standard's `GAPS.md` — reading each file's actual
`## Missing` / `## Partial` / `## Out-of-scope` / `## Unresolved` sections
directly, rather than trusting this file's own prior prose summaries —
turned up two standing errors in this file's own bookkeeping:

- **TS-27 was not actually fully resolved.** Every previous regeneration —
  including the one recorded immediately below, from earlier the same day —
  classified TS-27 as having "zero unchecked items of any kind" once its
  last Unresolved item was closed, but the file's own `## Out-of-scope`
  section still carries 6 unticked items (Google Developer Documentation
  Style Guide material the analysis judged out of TS-27's Markdown-syntax
  scope, plus one reference-list disagreement over which Markdown spec to
  cite) that were never counted.

- **TS-15, TS-18, and TS-26 still have open `## Missing` items that an
  earlier draft of this regeneration mistakenly reported as already
  closed**, by trusting each standard's own prior narrative Status text
  instead of reading its checklist directly. TS-15 has 2 open Missing items
  (wayfinding/navigation, typography — both routed in from TS-18's
  webstyleguide.com material and recorded in TS-15's `GAPS.md`, but never
  actually written into `01-design-principles.adoc` or any other partial).
  TS-18 has 3 open Missing items (image-format selection, responsive-image
  markup, SVG accessibility) plus its 1 Unresolved webstyleguide.com item.
  TS-26 has 1 open Missing item (instructional-step phrasing). TS-40's 1
  open Partial item (the declined OOCSS/BEM/SMACSS/SUIT CSS
  methodology-comparison gap) was already correctly tracked throughout. In
  every case, the content-writing work these Missing items describe has not
  happened yet — they were recorded as new gaps during the 2026-08-15
  `__TODO__`/webstyleguide.com re-fetch sweep, and no `close-gaps` run has
  been made against them since.

The mechanical script in [Regenerating this file](#regenerating-this-file)
counts each heading's unticked items directly from the file
(`grep -n '^- \[ \]'` under each `## ` heading), and running it against every
open standard's actual content — not just reading each file's own narrative
Status lines, and not just carrying forward a previous regeneration's totals
— is what surfaced both mismatches. All open counts in the table below were
verified this way, by direct inspection of each standard's `GAPS.md`, as of
this regeneration. This same full re-scan also found three standards with
substantive content that had fallen out of every list in this file — not
stubs, not gap-analyzed, and not in the "no GAPS.md" list below — TS-24,
TS-35, and TS-42, now added to that list where they belong.

Earlier the same day: a `close-gaps` batch run against TS-43 closed all 7 of
its open `## Missing` items (EAV/OOP schema anti-patterns, the `_lookup`
table-suffix convention, and four foreign-key/constraint-selection points),
leaving only its 6 Out-of-scope items open. A second `close-gaps` batch run
against TS-33 closed all 8 of its open `## Missing` items (the
`equals()`/`hashCode()` contract, `==`/`!=`-with-`String` prohibition,
floating-point/`BigDecimal` guidance, the overly-broad-`catch` prohibition,
the methods-must-not-return-null rule, the utility-class-private-constructor
rule, inner-assignment avoidance, and empty-statement avoidance), leaving
only its 3 Out-of-scope and 2 Unresolved (scope-call) items open. Both
standards' full run histories are in their own `GAPS.md` files; this file
only summarizes the outcome.

Before that, on the same day, a full re-fetch/re-fetch-attempt of all 36
`Unresolved` reference items across every standard's `GAPS.md` was run at the
user's explicit request. It surfaced, and worked through, a significant
correction: the `__TODO__/` local scratch tree — the original source draft
material most standards were authored from — is not actually gone. It is
present on disk, globally gitignored (via `~/local.gitignore`), which is why
every prior "re-fetch failed, no `__TODO__` directory exists anywhere" note
in this file's history was mistaken: those searches were Git-scoped and never
saw a gitignored tree. `pdftotext` (available in this environment) made its
binary PDFs readable for the first time. Six standards' local-`__TODO____`
items were re-ingested and gap-checked in full that day: TS-4 (no new gap;
directories corrected from "gone" to "found, content assessed"), TS-39 (1 new
gap, now closed), TS-43 (7 new gaps, since closed above), TS-26 (PDF judged
out-of-scope; 1 new gap from a link-collection triage), TS-33 (8 new gaps,
since closed above), and TS-18 (2 new gaps: responsive-image markup, SVG
accessibility, plus a webstyleguide.com image-format item). TS-15 gained 2
new gaps (wayfinding, typography) routed in from a webstyleguide.com chapter
the user asked to be treated as TS-15 material rather than TS-18's. Every
other Unresolved item — YouTube transcripts, JS-rendered SPAs, dead links,
Cloudflare-blocked pages, gnu.org's persistent 429/403 — was genuinely
re-attempted (multiple retries, backoffs, and in gnu.org's case a `curl`
fallback) and confirmed still unfetchable, then ticked off as dismissed with
a dated note. See [Known inconsistencies](#known-inconsistencies) for the
full account of the `__TODO__` discovery, and each standard's own `GAPS.md`
for the detailed, per-item resolution notes — this file only summarizes.

Before that run, four `close-gaps` batches were run the same day against
TS-20 (Network APIs), TS-26 (Technical writing style guide), TS-18 (Web
GUIs), and a confirm-only pass against TS-40 (CSS); TS-20's batch closed
both of its items and left it fully resolved; TS-26's closed its one
remaining item; TS-18's closed its one remaining item (neurodiversity.design)
after a re-fetch of the source succeeded; TS-40's one remaining item was
re-confirmed as declined, not reversed, so nothing changed there. Earlier
the same day, five `close-gaps` batches against TS-33 (Java) closed all 55
of its actionable items. The prior regeneration, on **2026-08-14**, applied
a joint `close-gaps` pass against TS-15 (User interfaces) and TS-18 (Web
GUIs). TS-15 was closed out in full: all 51 actionable items resolved in
one run. TS-18 had 59 of its 60 actionable items closed the same run. This
was on top of the same-day authoring of TS-39 (HTML), TS-44, TS-38, TS-55,
TS-42, TS-35, TS-24, and TS-37 from scratch, and the same-day closure of
TS-21's, TS-26's, TS-29's, TS-43's, TS-16's, and TS-40's actionable items.
See [Known inconsistencies](#known-inconsistencies) for the standard-by-
standard history behind each of those.

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

Forty-one standards have a `GAPS.md`. Thirty-two are fully resolved (zero
unchecked items of any kind) and are omitted from the table below — TS-2,
TS-3, TS-4, TS-5, TS-6, TS-7, TS-8, TS-9, TS-10, TS-11, TS-12, TS-13, TS-14,
TS-20, TS-21, TS-23, TS-25, TS-29, TS-31, TS-36, TS-37, TS-38, TS-41, TS-44,
TS-46, TS-48, TS-49, TS-50, TS-52, TS-54, TS-57, and TS-61. TS-38's `GAPS.md`
shows `actionable=1` under a naive mechanical count, but this is the file's
own long-documented false negative (its `**RESOLVED.**` marker has a period
inside the bold markup, which the regeneration script's literal string match
misses) — it is genuinely fully resolved; see
[Regenerating this file](#regenerating-this-file).

Nine have open items and appear in the table below: TS-18, TS-15, TS-40,
TS-16, TS-26, TS-43, TS-33, TS-27, and TS-39. Only one — TS-40 — still has
genuine content-writing work outstanding, and it is declined and
deliberately left open, not undone work: see the per-standard note below.
TS-18, TS-15, and TS-26 closed their last remaining Missing/Partial items
on 2026-08-15 (see their per-standard notes). All nine standards in the
table now have zero open `## Missing`/`## Partial` items except TS-40, and
remain in this table only for their `## Out-of-scope` items (TS-33 also
carries 2 Unresolved scope-call items, and TS-18 carries 1 Unresolved
reference item).

### The two GAPS.md formats

The files are in two formats, and the columns mean different things in each.

- **Template format** (38 files). Follows the `gap-analysis` skill's bundled
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
  for a human to confirm the exclusion or overrule it. Template format only.

- **Unresolved** — `## Unresolved` items. Reference resources that could not
  be retrieved when the analysis ran, or open scope questions not yet
  settled by the user. Template format only.

### Standards, ordered by actionable count

| TS | Title | Actionable | Scope | Unresolved | Format |
| --- | --- | ---: | ---: | ---: | --- |
| [TS-39](src/modules/ROOT/partials/039/GAPS.md) | HTML | 0 | 5 | 0 | Template — all 137 actionable items closed (136 on 2026-08-14, plus 1 more — responsive-table keyboard accessibility — found and closed 2026-08-15 during the `__TODO__` PDF re-ingestion) |
| [TS-16](src/modules/ROOT/partials/016/GAPS.md) | Command line interfaces (CLIs) | 0 | 9 | 0 | Template — all 59 actionable items closed 2026-08-14; its 1 Unresolved item (gnu.org) confirmed persistently unfetchable 2026-08-15 and dismissed |
| [TS-43](src/modules/ROOT/partials/043/GAPS.md) | Relational databases and SQL | 0 | 6 | 0 | Template — all 68 actionable items closed (61 on 2026-08-14, plus 7 more 2026-08-15 via a `close-gaps` batch against the `__TODO__` PDF/link-collection re-ingestion findings) |
| [TS-27](src/modules/ROOT/partials/027/GAPS.md) | Markdown | 0 | 6 | 0 | Template — all 15 actionable items closed 2026-08-13; corrected 2026-08-15 back into this table — its 6 Out-of-scope items were never actually ticked, despite an earlier regeneration's prose claiming "zero unchecked items of any kind" |
| [TS-33](src/modules/ROOT/partials/033/GAPS.md) | Java | 0 | 3 | 2 | Template — all 63 actionable items closed (55 on 2026-08-14/15, plus 8 more 2026-08-15 via a `close-gaps` batch against the `__TODO__` PDF re-ingestion findings — the `equals()`/`hashCode()` contract, `==` vs `.equals()` for `String`, floating-point/`BigDecimal`, broad-`catch` prohibition, utility-class private constructors, inner-assignment and empty-statement avoidance); 2 Unresolved items remain — pre-existing scope-call questions for the user (Javadoc-content rules bordering TS-7/TS-26; Java Platform Module System directive-ordering), not fetch failures |
| [TS-26](src/modules/ROOT/partials/026/GAPS.md) | Technical writing style guide | 0 | 5 | 0 | Template — all 32 actionable items closed 2026-08-15; its last item (instructional-step phrasing) closed the same day via `close-gaps`, a new "Instructional steps" section in `14-sentences-and-paragraphs.adoc` |
| [TS-40](src/modules/ROOT/partials/040/GAPS.md) | CSS | 1 | 12 | 0 | Template — 16 of 17 actionable items closed 2026-08-14; 1 declined and left open at the user's explicit choice; re-confirmed as declined, not reversed, 2026-08-15 |
| [TS-15](src/modules/ROOT/partials/015/GAPS.md) | User interfaces | 0 | 7 | 0 | Template — all 53 actionable items closed 2026-08-15; its last 2 items (wayfinding/navigation, typography) closed the same day via `close-gaps` — new "Wayfinding and navigation" and "Typography" sections in `01-design-principles.adoc` and `10-visual-rhythm-and-text.adoc` |
| [TS-18](src/modules/ROOT/partials/018/GAPS.md) | Web GUIs | 0 | 26 | 1 | Template — all 63 actionable items closed 2026-08-15; its last 3 items (image-format selection, responsive images `srcset`/`sizes`/`picture`, SVG accessibility) closed the same day via `close-gaps` — a new "Images" section in `01-performance-optimization.adoc` and a new inline-SVG-accessibility bullet in `02-web-accessibility.adoc`; 1 Unresolved item remains — `webstyleguide.com`'s other chapters (Strategy, IA, Page Structure, Video), not yet individually assessed |
| | **Total** | **1** | **79** | **3** | |

Eight of the nine standards in the table above — TS-39, TS-16, TS-43, TS-27,
TS-33, TS-26, TS-15, TS-18 — have **zero** open `## Missing`/`## Partial`
items. What remains open for them is `## Out-of-scope` items awaiting the
user's confirm/overrule decision, plus TS-33's 2 genuine scope-call
`## Unresolved` items and TS-18's 1 unfetched-chapters `## Unresolved`
item — none of that is content-writing work.

Only TS-40 (1 declined Partial item) still has an open `## Missing`/
`## Partial` item, and it is deliberately left open at the user's explicit
choice, not outstanding work awaiting a `close-gaps` run. As of
2026-08-15's fourth `close-gaps` wave — run against TS-26, TS-15, and
TS-18 at the user's explicit request to "complete all remaining open items
— both missing and partial" — **every genuine content-writing gap
recorded anywhere in this repository has been closed.**

TS-43 (Relational databases and SQL) closed its final 7 Missing items on
2026-08-15 via a `close-gaps` batch run: EAV and object-oriented-schema
anti-pattern avoidance (a new "Modeling data as relations" section in
`04-schema-design.adoc`); the `_lookup` reference/lookup-table suffix
convention (`03-naming-conventions.adoc`, "Table names"); and four
foreign-key/constraint-selection points from "Old, Good Database Design" —
`ON DELETE` action semantics (`NO ACTION`/`RESTRICT`, `CASCADE`,
`SET NULL`, `SET DEFAULT`, plus the sentinel-value anti-pattern, a new
"Choosing a foreign key's `ON DELETE` action" subsection), `UNIQUE`
constraint vs. index (a new paragraph in "Choosing keys"), and no business
logic in `DEFAULT`/`CHECK` (a new paragraph in "Default values"). All
extended existing partials; no file was renumbered. Two sources (Simon
Holywell's SQL Style Guide, "Old, Good Database Design" via the Wayback
Machine) were added to the page's `== References`. TS-43 now has 0
actionable items — only its 6 Out-of-scope items (pure MySQL DBA/operations
material, and the schema-less stub) remain open, awaiting the user's
decision from the original analysis run.

TS-33 (Java) closed its final 8 Missing items on 2026-08-15 via a
`close-gaps` batch run against the `SDCP-2-Java-v1.0.0-290722-0931.pdf`
re-ingestion findings: the `equals()`/`hashCode()` contract and the
overly-broad-`catch` prohibition (both in `05-programming-constructs.adoc`'s
"Exceptions" section); the utility-class-private-constructor rule and
inner-assignment avoidance (both in the same file's "Classes and
interfaces" / "Variable declarations" sections); `String` `==`/`!=`
comparison and floating-point/`BigDecimal` guidance (two new sections,
"Strings" and "Numeric precision", in `06-types.adoc`); the
methods-must-not-return-null rule (folded into `06-types.adoc`'s existing
"Nullability" section); and empty-statement avoidance
(`04-code-style.adoc`'s "Brace style" section). All extended existing
partials; no file was renumbered, and no reference-list entry was added for
the PDF source (an internal document, not an externally citable published
URL, consistent with how the standard's other `__TODO__/033/` staging-file
items were handled). TS-33 now has 0 actionable items — only 3 Out-of-scope
items (thread-safety design deferred to TS-7, tooling/build-choice PDFs,
the archived Oracle Code Conventions introduction) and 2 Unresolved
scope-call items (Javadoc-content boundary with TS-7/TS-26; Java Platform
Module System directive-ordering) remain open.

TS-27 (Markdown) was **incorrectly** carried on the fully-resolved list by
every regeneration from 2026-08-15's earlier run onward. Its `GAPS.md` has 0
actionable items — genuinely closed — but its `## Out-of-scope` section
still has 6 unticked items: four Google Developer Documentation Style Guide
items (documentation process philosophy, capitalization conventions, title
capitalization, and a document-layout/`[TOC]` recommendation, all judged to
belong to TS-26 or to conflict with TS-27's deliberate scope decisions), one
more `[TOC]`-directive item in the same vein, and one reference-list
disagreement over citing the original 2004 Markdown.pl spec versus TS-27's
GFM/CommonMark stance. None of these were ever ticked; the earlier
regeneration's prose summary ("now zero unchecked items of any kind") did
not match the file it was describing. This was only found by running the
mechanical `grep -c '^- \[ \]'` check directly against every `GAPS.md`
rather than trusting each standard's own narrative Status entries — see
[Regenerating this file](#regenerating-this-file). TS-27 is restored to the
open-items table above, and its 6 Out-of-scope items await the user's
confirm/overrule decision like every other standard's.

TS-39 (HTML) reached zero Unresolved items on 2026-08-15: re-ingesting its
four previously-unread PDFs via `pdftotext` (the `__TODO__` tree, thought
gone, was rediscovered still present locally) found one genuine new gap — a
responsive/scrollable-table keyboard-accessibility pattern
(`tabindex="0"`/`role="region"`/`aria-labelledby`, added only when a table's
content overflows) from Heydon Pickering's *Inclusive Components*, not
previously covered by `04-tables.adoc`. The other three PDFs (general HTML5
tutorials) and the accessibility-landmarks PNG added nothing new — their
content already overlaps TS-39's existing 13 partials or falls outside its
scope (Canvas/Web Storage/offline APIs, deferred to TS-37; CSS3, deferred to
TS-40). The `style.ons.gov.uk` `.URL` bookmark was genuinely re-attempted
twice and remains unfetchable (JavaScript-rendered, no server-side fallback
content) — this is TS-39's one remaining true fetch failure, but it no
longer blocks the standard from being "fully resolved" in the strict sense
used by this file, because its Missing item was closed against other
sources; only Out-of-scope items remain open in TS-39's own `GAPS.md`.

TS-18 (Web GUIs) gained 3 new Missing items on 2026-08-15: image-format
selection (GIF/JPEG/PNG/SVG use cases, compression trade-offs, alt-text
conventions — from webstyleguide.com's Images chapter, fetched after its
root page's table of contents was retrieved during this run's Unresolved
sweep), responsive-image markup (`srcset`/`sizes`/`w`/`x` descriptors,
`<picture>`/`<source>` art direction — from a Yoav Weiss chapter in "Real
Life Responsive Web Design", one of five previously-unread PDFs
rediscovered in its local `__TODO__` tree), and SVG accessibility
(`<title>`/`<desc>`, `role="img"`/`aria-labelledby` — from a Sara Soueidan
chapter in the same book). The other four PDFs (a 12-factor-style
server-side book, a design-system tooling book, a dated visual-design book,
and an obsolete 2011 PhoneGap/Cordova book) contributed nothing in scope.
TS-18's 3 "empty stub" files (`encoding.md`, `modules-and-bundling.md`,
`0500-csp.md`) were re-verified as genuinely empty or near-empty — the
prior characterization held. Its YouTube reference item was re-confirmed
persistently unfetchable and dismissed. **All 3 Missing items were closed
the same day** via a `close-gaps` batch run: a new "Images" section in
`01-performance-optimization.adoc` (format selection plus responsive-image
markup) and a new inline-SVG-accessibility bullet in
`02-web-accessibility.adoc`. TS-18 now stands at Actionable=0, Scope=26,
Unresolved=1 — webstyleguide.com's other chapters (Strategy, Research,
Process, IA, Site Structure, Page Structure, Graphic Design, Editorial
Style, Video) were never individually fetched and remain open for a future
pass, if wanted.

TS-15 (User interfaces) gained 2 new Missing items on 2026-08-15:
wayfinding and navigation (the four-component orientation/route/
mapping/closure model, persistent navigation and breadcrumbs, the 80/20
prioritization principle) and typography (typeface-pairing discipline,
alignment, emphasis restraint, leading) — both from webstyleguide.com's
Interface Design and Typography chapters. These were originally an
Unresolved item on TS-18's `GAPS.md` (only the site's table of contents had
been fetched); the user directed that, once fetched, this platform-agnostic
HCI/UX content be routed to TS-15 rather than TS-18, consistent with how the
two standards have always divided the boundary (TS-18 = web-implementation-
specific; TS-15 = general interface design). TS-15's own 11 dead/unreachable
Unresolved URLs (Airbnb, Apple HIG, Salesforce Lightning, Material Design,
Nordnet, WeWork Plasma, Ubuntu, designguidelines.co, Usability Post,
design.google/library) were all genuinely re-attempted and remain
unfetchable or resolve to unrelated content — each dismissed with a dated
note. One, usability.gov's legacy deep links, now redirects to a live
successor site (digital.gov) with real content, but it only reinforces
material TS-15 already captures (its own usability-definition paragraph
already cites usability.gov by name); no new gap. The `ui`/`ui2` "empty
directories" were found to not be literally empty (a `hackscorp/standards`
table-of-contents stub with no substantive prose of its own) — re-confirmed
as non-substantive, though `ui/`'s `_todo/` subdirectory (layout,
styleguide, performance, popups, accessibility, i18n drafts) was not
individually mined this run and could be worth a dedicated future pass.
**Both Missing items were closed the same day** via a `close-gaps` batch
run: a new "Wayfinding and navigation" section in
`01-design-principles.adoc` and a new "Typography" section in
`10-visual-rhythm-and-text.adoc`. TS-15 now stands at Actionable=0,
Scope=7, Unresolved=0.

TS-4 (Modeling) and TS-27 (Markdown)'s Missing/Partial items both reached
zero on 2026-08-15 — but see the correction above: TS-27's Out-of-scope
items were never actually zero, and this file wrongly said otherwise until
this regeneration. TS-4's three "screenshot" directories (27 PNG images plus
one `.uxf` UMLet file) were viewed and confirmed to be exactly what the
original analysis guessed: small UML diagrams using notation TS-4 already
documents, and the `.uxf` a genuine duplicate of an existing worked example.
TS-27's `__TODO__/027/markdown.adoc` stub was re-confirmed as contentless,
and its previously-uncited sibling file `_markdown.md` (the well-known
"adam-p/markdown-here" cheat sheet) was found and compared against TS-27's
content — every topic it covers already has its own, more detailed,
GFM/CommonMark-specific partial. Neither standard's re-examination produced
a new gap. TS-4 has zero unchecked items of any kind and is genuinely fully
resolved; TS-27 is not (see above) and remains in the open-items table.

TS-21 (HTTP APIs) and TS-29 (JSON Schema) both reached zero unchecked items
of any kind on 2026-08-15 (previously they stood at 0 actionable / 0
out-of-scope / 1 and 2 Unresolved respectively). Their remaining Unresolved
items were all YouTube video references; all were genuinely re-attempted via
WebFetch and confirmed to still return only YouTube's footer/navigation
chrome with no transcript or description text — a persistent limitation of
this environment's fetch tooling against YouTube, not a transient failure.
Each was dismissed with a dated note; no new gaps were derivable without
transcript access. Both moved to the fully-resolved list, and — unlike
TS-27 — this was directly re-verified during this regeneration by counting
each file's total unchecked items (`grep -c '^- \[ \]'`), which returns 0
for both.

TS-16 (Command line interfaces) reached zero Unresolved items on 2026-08-15.
Its one remaining item — `gnu.org`'s Program-Behavior.html — was retried
three times via WebFetch (429 Too Many Requests each time, across 5s, 15s,
and 20s backoffs) and once via direct `curl` with a browser User-Agent (403
Forbidden), confirming the failure is persistent and environment-level, not
transient. Since the page's CLI-relevant content was already captured via a
GNU Coding Standards index sub-agent in an earlier run, no gap is left
unaddressed; dismissed. TS-16 stays in the open-items table only for its 9
Out-of-scope items, which await the user's confirm/overrule decision.

## Standards with neither a stub nor a GAPS.md

TS-1, TS-17, TS-19, TS-22, TS-24, TS-28, TS-30, TS-32, TS-34, TS-35, TS-42,
TS-45, TS-47, TS-51, TS-53, TS-55, TS-56, TS-58, TS-59, TS-60, TS-62, and
TS-63 all have substantive content and no recorded gap analysis. TS-24,
TS-35, and TS-42 are added to this list as of 2026-08-15's regeneration —
all three were authored from scratch on 2026-08-14 (alongside TS-37, TS-38,
TS-39, TS-44, and TS-55) but had fallen out of every list in this file until
this run's full re-scan caught the omission. A gap analysis (`/gap-analysis`)
could be run against any of them; none is known to be missing content today.

## Known inconsistencies

Surfaced on 2026-08-13 while writing the `close-gaps` skill. These are
repo-level decisions and defects, not gap-closing work, but the first two
govern how all new content should be written.

- **This file's own count for TS-27 was wrong from 2026-08-15's earlier
  run until this regeneration.** Every prose Status summary in this file
  claimed TS-27 reached "zero unchecked items of any kind" once its last
  Unresolved item closed, but `partials/027/GAPS.md`'s `## Out-of-scope`
  section has 6 items that were never ticked. This regeneration found the
  mismatch by running `grep -c '^- \[ \]'` directly against every
  standard's `GAPS.md`, rather than trusting the file's own narrative
  Status lines — a caution worth repeating for future regenerations: a
  Status entry is a claim about the file, not a substitute for counting
  it. TS-27 is restored to the open-items table.

- **RESOLVED — the `__TODO__/` scratch tree was never actually gone.**
  Discovered 2026-08-15, mid-way through a full re-fetch sweep of every
  standard's Unresolved reference items. `~/local.gitignore` (a global,
  machine-level gitignore, not this repository's own `.gitignore`)
  contains a bare `__TODO__` entry, so the tree — the original local source
  draft material most standards were authored from, including binary PDFs,
  `.URL` bookmarks, and hundreds of images — never appeared in `git status`,
  was never committed, and consequently was invisible to every prior
  re-fetch attempt that searched Git history or the working tree via
  Git-aware tooling. Multiple standards' `GAPS.md` files carried confident,
  specific claims that this tree "no longer exists anywhere" or "was never
  committed... not a versioned or remotely-hosted resource" (TS-4's
  Unresolved item, first written 2026-08-13, is the clearest example) —
  these claims were true only in the narrow sense that Git never saw it;
  the tree was present on disk the entire time. A plain filesystem `find`
  from the repository root (not `git`-scoped) surfaces it immediately. This
  is now the documented way to check: **do not conclude a local `__TODO__/`
  reference is permanently gone from a Git-history or Git-status search
  alone** — always also check the plain filesystem, since a global
  (machine-level, not repository-level) gitignore entry can hide a tree
  from every Git-aware tool while leaving it fully present and readable.
  Six standards' previously-"unfetchable" local items were re-ingested once
  this was discovered — see the per-standard notes above and in
  [Open gap analyses](#open-gap-analyses) for what each found. `pdftotext`
  (present in this environment at `/usr/bin/pdftotext`) made the tree's
  several dozen binary PDFs readable for the first time; TS-40's `GAPS.md`
  had already established this tool's use on 2026-08-14, but no other
  standard's gap analysis had applied it until this run.

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
  that reason. A twelfth instance of this pitfall recurred on 2026-08-14 in
  TS-18's `06-references.adoc`, referencing the newly-added "Reflows,
  repaints, and layout thrashing" section — fixed the same way, with an
  explicit `[#reflows-repaints-and-layout-thrashing]` anchor. A thirteenth
  instance turned up on 2026-08-15 in TS-43's new `== References` section:
  a cross-reference to `04-schema-design.adoc`'s new "Choosing a foreign
  key's `ON DELETE` action" heading failed because Asciidoctor's natural
  `<<...>>` matching does not handle a heading whose title itself contains
  backticked code spans reliably across a line-wrapped reference entry.
  Fixed the same way, with an explicit
  `[#choosing-a-foreign-keys-on-delete-action]` anchor.

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
  of the 2026-08-14 gap-closing work, having been renumbered four times;
  TS-21's now live in `21-references.adoc`, renumbered from
  `20-references.adoc` the same day to make room for a new
  "Alternative HTTP API styles" partial; TS-18's now live in
  `06-references.adoc`, renumbered from `04-references.adoc` the same day to
  make room for its two new JavaScript-behaviors and CSS-layout partials).
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

- **DECLINED — TS-40's methodology-comparison gap.** A `close-gaps` run on
  2026-08-14 closed 16 of TS-40's 17 actionable items. The remaining one
  proposed expanding `01-overview.adoc` into a comparative summary of
  OOCSS/BEM/SMACSS/SUIT CSS. The item's own text flagged it as borderline
  (the standard's purpose is to prescribe its own methodology, not survey
  others); on review, declined for that reason and left open — `- [ ]`,
  unticked — in TS-40's `GAPS.md` with a dated rationale note, rather than
  resolved or deleted. TS-40 stays in the actionable-count table pending any
  future reversal of this decision.

- **RESOLVED — TS-16 closed out in one run; its Unresolved item dismissed
  2026-08-15.** All 59 of TS-16's actionable items (9 Missing, 50 Partial)
  were closed by a `close-gaps` run on 2026-08-14, extending 8 of its 11
  existing partials. Its one Unresolved item (`gnu.org`'s
  Program-Behavior.html) was re-attempted three times via WebFetch and once
  via `curl` on 2026-08-15, all failing (429/403) — confirmed persistent,
  dismissed. TS-16 stays in the actionable-count table because its 9
  out-of-scope items remain open, awaiting the user's confirm/overrule
  decision.

- **RESOLVED — TS-37 authored from a pure stub and fully resolved in one
  run.** TS-37 (Web platform APIs) previously held only a `// TODO`
  introductory placeholder and "See also" cross-references, with 18 Missing
  and 4 Out-of-scope items open in its `GAPS.md`. On 2026-08-14 it was
  authored from scratch — an introductory paragraph on the page plus five new
  content partials (`01-when-to-use-web-components.adoc` through
  `05-limitations.adoc`, with `06-references.adoc`) covering when to use web
  components, the HTML-vs-JavaScript web component distinction, Shadow DOM
  (including the `:root`/`rem` leak and cross-root ARIA accessibility gap),
  building a custom element, and platform limitations. All 18 Missing items
  were closed against this new content. The 4 Out-of-scope items (CSS fluid
  typography via `clamp()`, container queries, intrinsic flex/grid layouts,
  `text-wrap: balance`/`ch`) were confirmed out-of-scope for TS-37 by the
  user and relocated as 4 new Missing items in TS-18's `GAPS.md` — closed by
  TS-18's 2026-08-14 `close-gaps` run.

- **RESOLVED — TS-38 authored from a pure stub and fully resolved in one
  run.** TS-38 (Node.js applications) previously held only a `// TODO`
  placeholder and a legacy-format `GAPS.md` with one open gap. On 2026-08-14
  it was authored from scratch — six new content partials
  (`01-module-system.adoc` through `06-stateless-scaling.adoc`) — and its
  recorded gap closed against the new "Stateless scaling" section. Its
  `**RESOLVED.**` marker (period inside the bold, unlike every other legacy
  file's `**RESOLVED**`) is a known trap for the mechanical regeneration
  script — see [Regenerating this file](#regenerating-this-file).

- **RESOLVED — TS-44 authored from a pure stub and fully resolved in one
  run.** TS-44 (Non-relational (NoSQL) databases) previously held only a
  `// TODO` placeholder and a legacy-format `GAPS.md` with two open gaps. On
  2026-08-14 it was authored from scratch — five new content partials
  (`01-data-models.adoc` through `05-operational-considerations.adoc`) —
  closing both recorded gaps.

- **PARTIALLY RESOLVED — TS-15 and TS-18's 2026-08-14 joint `close-gaps` run
  closed 51/51 of TS-15's and 59/60 of TS-18's actionable items; both then
  gained new open items on 2026-08-15 that remain unwritten.** On
  2026-08-15, re-fetching Unresolved items across both standards found: for
  TS-18, a webstyleguide.com Images-chapter item, responsive-image markup,
  and SVG accessibility (3 new Missing items, from its previously-unread
  PDFs and a follow-up webstyleguide.com fetch); for TS-15, wayfinding/
  navigation and typography (2 new Missing items, routed in from TS-18's
  webstyleguide.com Unresolved item at the user's explicit direction, since
  the content is platform-agnostic HCI rather than web-implementation-
  specific). Neither set has been closed yet — no `close-gaps` run has been
  made against either since they were recorded. See the per-standard notes
  in [Open gap analyses](#open-gap-analyses) for full detail.

- **RESOLVED — TS-4's Unresolved item closed 2026-08-15, once the
  `__TODO__` tree's continued existence was discovered.** Its sole
  remaining open item was a local `__TODO__/` file or directory previously
  believed permanently gone. Re-examined directly once the tree was found
  still present (globally gitignored, not deleted — see the entry above);
  produced no new gap. TS-4 reached zero unchecked items of any kind and
  moved to the fully-resolved list. (TS-27's equivalent claim, made the
  same day, was incorrect — see the correction at the top of this section.)

- **RESOLVED — TS-21 and TS-29's remaining Unresolved items (YouTube
  transcripts) dismissed 2026-08-15.** Both items were genuinely
  re-attempted via WebFetch; YouTube's pages returned only footer/navigation
  chrome with no transcript or description text in every case, confirming
  the limitation is persistent for this environment, not transient. Both
  standards reached zero unchecked items of any kind and moved to the
  fully-resolved list; re-verified directly during the 2026-08-15
  regeneration that found the TS-27 discrepancy.

- **RESOLVED — TS-43's remaining 7 Missing items closed 2026-08-15 via
  `close-gaps`.** See the per-standard note in
  [Open gap analyses](#open-gap-analyses).

- **RESOLVED — TS-33's remaining 8 Missing items closed 2026-08-15 via
  `close-gaps`.** See the per-standard note in
  [Open gap analyses](#open-gap-analyses).

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
heading name was typo'd. This is exactly how TS-27's 6 stranded
Out-of-scope items were found on 2026-08-15: its per-heading breakdown
matched, but a prior regeneration's own prose Status summary had claimed a
zero count that the file never actually reached. Trust the grep over any
standard's own narrative Status line — the Status line is written by the
same kind of process that can make this mistake.

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
items. TS-16, TS-27, TS-33, TS-39, TS-43, TS-26, TS-15, and TS-18 are the
current examples that make this distinction matter: every one of them has 0
actionable items, but each has at least one open Out-of-scope or Unresolved
item, keeping it in the open-items table. TS-40 is a different case — it
has one open `## Partial` item too (declined, left open at the user's
explicit choice), so it belongs in the table for a more basic reason: a
human decision, not authoring, is what's outstanding.

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
awaiting authorship, not a candidate for `gap-analysis`. TS-24, TS-35, and
TS-42 fell out of this file's "neither a stub nor a GAPS.md" list for at
least one full regeneration cycle before this check caught it on 2026-08-15;
re-run this diff every time, rather than trusting the previous run's list by
hand.

**Do not conclude a local `__TODO__/` reference is permanently gone from a
Git-scoped search alone.** `~/local.gitignore` (a global, machine-level
gitignore) hides the entire `__TODO__/` tree from `git status`, `git log
--all`, and any other Git-aware search, even though the tree is fully
present and readable on disk. Always additionally check with a plain
filesystem `find` (not `git`-scoped) before recording a local reference as
unrecoverable — see
[Known inconsistencies](#known-inconsistencies) for the 2026-08-15 discovery
that several standards' Unresolved items had wrongly concluded otherwise.
