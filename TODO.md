# TODO

Outstanding work across the technical standards in this repository: standards
that are still stubs (no substantive content written), and standards whose
`GAPS.md` gap analysis still has open items.

This file is a manually-maintained index, regenerated from the tree. The
counts below were last regenerated on **2026-08-15** — this run reflects
four `close-gaps` batches run the same day against TS-20 (Network APIs),
TS-26 (Technical writing style guide), TS-18 (Web GUIs), and a confirm-only
pass against TS-40 (CSS), described in their own section below. TS-20's
batch closed both of its items and left it fully resolved; TS-26's closed
its one remaining item; TS-18's closed its one remaining item
(neurodiversity.design) after a re-fetch of the source succeeded; TS-40's
one remaining item was re-confirmed as declined, not reversed, so nothing
changed there. Earlier the same day, five `close-gaps` batches against
TS-33 (Java), described in their own section below, closed all 55 of its
actionable items. The prior regeneration, on **2026-08-14**, applied a
joint `close-gaps` pass against
TS-15 (User interfaces) and TS-18 (Web GUIs), run together at the user's
explicit request specifically to catch gaps that would be better routed
between the two standards. None were found in either direction: every item
TS-18 closed is web-implementation-specific (HTTP headers, CSS properties,
DOM APIs, WCAG markup) and every item TS-15 closed is a platform-agnostic
HCI/UX principle that applies equally to a CLI or a native app, so no item
moved between the two files.

TS-15 was closed out in full: all 51 actionable items (47 Missing, 4 Partial)
resolved in one run, across ten new content partials
(`02-feedback-and-communication.adoc` through `10-visual-rhythm-and-text.adoc`)
plus expansions to the existing "Keep it tidy" and "Embrace affordances"
sections and a new usability-definition paragraph on the page itself. TS-15
stays in the open-items table below, not the fully-resolved list, because 7
Out-of-scope items and 12 Unresolved references remain open in its own
`GAPS.md` — neither was actioned in this run, since neither counts as
actionable work.

TS-18 had 59 of its 60 actionable items (44 of 45 Missing, all 15 Partial)
closed the same run, across expansions to its three existing partials
(performance, accessibility, fonts) plus two new partials —
`04-javascript-behaviors.adoc` (component-behavior conventions, memory-
efficient DOM manipulation, form-submission integrity) and
`05-css-layout-and-typography.adoc` (fluid typography, container queries,
intrinsic layouts, readable measure) — inserted before the standard's
references partial, renumbered from `04-references.adoc` to
`06-references.adoc` to make room. One Missing item (neurodiversity.design)
was deliberately left open: the source was only ever thinly retrieved (a
landing page, not its per-principle pages), so writing a section from it
would have meant fabricating detail the source does not provide — re-fetching
those pages is a precondition for closing it, not optional polish. TS-18
stays in the open-items table at Actionable=1, Scope=26, Unresolved=5.
Several items closed this run carry a scope flag inherited from earlier
runs — the rsjs component-behavior conventions and the form-submission-
integrity section note they border TS-5 (application architecture) or
expand TS-18 beyond its original three pillars (performance, accessibility,
fonts). The content was written into TS-18 per the maintainer's prior scope
calls already recorded in its `GAPS.md`, and the flags are restated there
for the user to confirm or overrule; they were not resolved silently.

This is on top of the prior same-day authoring of TS-39 (HTML) from scratch,
the last remaining stub in the repository at the time. Thirteen new content
partials were written, closing all 136 of its Missing/Partial items in one
run; its 5 Out-of-scope items and 4 Unresolved references were carried
forward, so it left the stub table but stayed out of the fully-resolved
list. This was on top of the same-day authoring of TS-44 (Non-relational
(NoSQL) databases), TS-38 (Node.js applications), TS-55 (Authentication and
authorization), TS-42 (Vue), TS-35 (Python), TS-24 (User manuals), and TS-37
(Web platform APIs) from scratch, and the same-day closure of TS-21's,
TS-26's, TS-29's, TS-43's, TS-16's, and TS-40's actionable items. See the
table notes below, and the standard-by-standard history preserved in
[Known inconsistencies](#known-inconsistencies), for the detail behind each
of those.

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

Forty-one standards have a `GAPS.md`. Twenty-nine are fully resolved (zero
unchecked items of any kind) and are omitted from the table below — TS-2,
TS-3, TS-5, TS-6, TS-7, TS-8, TS-9, TS-10, TS-11, TS-12, TS-13, TS-14, TS-20,
TS-23, TS-25, TS-31, TS-36, TS-37, TS-38, TS-41, TS-44, TS-46, TS-48, TS-49,
TS-50, TS-52, TS-54, TS-57, and TS-61. TS-20 joined this list on 2026-08-15:
its Scope and Unresolved counts were already zero (the file's only source
re-fetched successfully back on 2026-08-13, and the legacy-format
conversion recorded no Out-of-scope or Unresolved items), so closing its
last Actionable item today brought it to zero unchecked items of any kind —
see the note below.

Twelve have open items and appear in the table below: TS-4, TS-39, TS-16,
TS-21, TS-29, TS-43, TS-26, TS-27, TS-40, TS-15, TS-33, and TS-18.
TS-15 and TS-18 are both new to the 2026-08-14 run's zero/near-zero
actionable state — see the note above. TS-33 reached zero actionable items
on 2026-08-15 — see the note below — but stays in this table rather than
joining the fully-resolved list, for the same reason as TS-15/TS-18/TS-4/
TS-16/etc.: its 3 Out-of-scope and 4 Unresolved items are still open.

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
  be retrieved when the analysis ran. Each needs re-fetching before it can
  become a gap or be dismissed. Template format only.

### Standards, ordered by actionable count

| TS | Title | Actionable | Scope | Unresolved | Format |
| --- | --- | ---: | ---: | ---: | --- |
| [TS-4](src/modules/ROOT/partials/004/GAPS.md) | Modeling | 0 | 0 | 1 | Template — 1 unresolved resource, repeatedly unfetchable |
| [TS-39](src/modules/ROOT/partials/039/GAPS.md) | HTML | 0 | 5 | 4 | Template — authored from a pure stub 2026-08-14; all 136 actionable items closed in one run; no longer a stub |
| [TS-16](src/modules/ROOT/partials/016/GAPS.md) | Command line interfaces (CLIs) | 0 | 9 | 1 | Template — all 59 actionable items closed 2026-08-14 |
| [TS-21](src/modules/ROOT/partials/021/GAPS.md) | HTTP APIs | 0 | 0 | 1 | Template — all 39 Partial items and all 13 out-of-scope items closed 2026-08-14, across six batches; 3 of 4 unresolved Stack-Overflow-adjacent items dismissed |
| [TS-29](src/modules/ROOT/partials/029/GAPS.md) | JSON Schema | 0 | 0 | 2 | Template — all 29 actionable and all 3 out-of-scope items closed 2026-08-14 |
| [TS-43](src/modules/ROOT/partials/043/GAPS.md) | Relational databases and SQL | 0 | 6 | 4 | Template — all 61 actionable items closed 2026-08-14; table row restored after being omitted in a prior regeneration |
| [TS-26](src/modules/ROOT/partials/026/GAPS.md) | Technical writing style guide | 0 | 6 | 2 | Template — all 30 actionable items closed (29 on 2026-08-14 across three batches, plus 1 more on 2026-08-15); 4 of 9 out-of-scope items also reversed and closed |
| [TS-27](src/modules/ROOT/partials/027/GAPS.md) | Markdown | 0 | 6 | 1 | Template — all 15 actionable items closed 2026-08-13 |
| [TS-40](src/modules/ROOT/partials/040/GAPS.md) | CSS | 1 | 12 | 0 | Template — 16 of 17 actionable items closed 2026-08-14; 1 declined and left open; re-confirmed as declined, not reversed, 2026-08-15 |
| [TS-15](src/modules/ROOT/partials/015/GAPS.md) | User interfaces | 0 | 7 | 12 | Template — all 51 actionable items closed 2026-08-14, jointly with TS-18 |
| [TS-33](src/modules/ROOT/partials/033/GAPS.md) | Java | 0 | 3 | 4 | Template — all 55 actionable items closed 2026-08-15, across five batches |
| [TS-18](src/modules/ROOT/partials/018/GAPS.md) | Web GUIs | 0 | 26 | 4 | Template — all 60 actionable items closed (59 on 2026-08-14 jointly with TS-15, plus the last one — neurodiversity.design — on 2026-08-15 once its source re-fetched successfully) |
| | **Total** | **1** | **80** | **36** | |

TS-20 (Network APIs) left the fully-resolved list on 2026-08-14, gaining 1
new Missing item routed in from TS-21 while confirming TS-21's own
out-of-scope items (general rate-limit response headers,
`X-RateLimit-Limit`/`Remaining`/`Reset`), not yet reviewed against TS-20's
current content at the time. It was closed out the next day, 2026-08-15,
and moved back to the fully-resolved list above: the item was closed by
extending the existing "Rate limiting and backoff" section in
`04-reliability-and-resilience.adoc` with the three headers, sourced from
the Port of Antwerp-Bruges API guidelines (the item's other cited source, a
GitHub Microsoft-guidelines CORS-section anchor, turned out on re-fetch to
be a mismatched citation with no header guidance). TS-20 had no open Scope
or Unresolved items already, so this brought it to zero unchecked items of
any kind.

TS-15 (User interfaces) was closed out in full on 2026-08-14, jointly with
TS-18 — see the note at the top of this file. All 51 actionable items (47
Missing, 4 Partial) were resolved: ten new content partials
(`02-feedback-and-communication.adoc` through `10-visual-rhythm-and-text.adoc`)
covering feedback and response-time thresholds, error prevention and
messages, memory/cognitive load, flexibility, help, respecting conventions
and mental models, managing choice and complexity, targeting, visual
perception (aesthetics, ordering, Gestalt grouping), motivation and pacing,
inputs/context/bias, API design principles, and spacing/microcopy/voice-and-
tone; plus expansions to the existing "Keep it tidy" and "Embrace
affordances" sections, and a new usability-definition paragraph on the page
itself. TS-15 stays in this table at Actionable=0 because its 7 Out-of-scope
items and 12 Unresolved references remain open — the same shape as TS-4,
TS-16, TS-21, TS-27, TS-29, and TS-43 above.

TS-18 (Web GUIs) had 59 of its 60 actionable items closed the same run,
jointly with TS-15. The three existing partials (performance optimization,
accessibility, fonts) were substantially expanded — TTFB, HTTP/2, script
loading, layout thrashing, INP, bfcache, Speculation Rules, accessibility
implementation detail (skip links, `<track>`/VTT, ARIA landmarks, native
form validation, tooltip patterns), and font-loading patterns (FOIT/FOUT,
sessionStorage caching, prioritised loading) — and two new partials were
added: `04-javascript-behaviors.adoc` (component-behavior conventions from
rsjs, memory-efficient DOM manipulation, form-submission integrity) and
`05-css-layout-and-typography.adoc` (the four items relocated from TS-37's
gap analysis: fluid typography, container queries, intrinsic layouts,
readable measure). The references partial was renumbered
`04-references.adoc` → `06-references.adoc` to make room, and gained roughly
13 new source entries. One Missing item (neurodiversity.design) was
deliberately left open, since only a thin landing page was ever fetched for
it — not enough to write from without fabricating detail. TS-18 stayed in
this table at Actionable=1, Scope=26, Unresolved=5 after that run.

TS-18's last item — neurodiversity.design — was closed on 2026-08-15, once
all eight of the source's per-principle pages (Font, Typography, Colour,
Buttons/Links/Inputs, Interface, Numbers, Animations, Communications)
retrieved successfully on re-fetch, where only the thin landing page had
been reachable before. Closed by a new "5. Neurodiversity" section
appended to `02-web-accessibility.adoc`, after the standard's four WCAG
principle sections, since the guidance is cross-cutting and does not map
onto any one of them. This brought TS-18 to Actionable=0; its Scope=26 and
Unresolved=4 (one Unresolved item dismissed alongside the Missing item it
was paired with) remain open, so it stays in this table rather than joining
the fully-resolved list.

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
Missing item there, which TS-15's 2026-08-14 `close-gaps` run subsequently
closed (see the "Microcopy and UI text" section noted above). TS-26 stayed
in this table, not the fully-resolved list, because its remaining 6
Out-of-scope items and 2 Unresolved YouTube-adjacent references kept it
short of zero unchecked items of any kind — the same shape as TS-4, TS-16,
TS-27, and TS-29.

TS-26 gained one more Missing item the same day, routed in from TS-21 while
confirming TS-21's own out-of-scope items: `api-style-guide.md`'s
document-level authoring conventions (RFC 2119 keyword rendering, all-caps
REST/JSON, fixed-width machine-readable text, URI Template syntax). Closed
on 2026-08-15: two of the four sub-items were already covered
(fixed-width rendering in `06-emphasis.adoc`, all-caps acronyms in
`04-abbreviations.adoc`) and needed no change; the other two were genuinely
missing and closed by a new "Normative language" section in
`01-voice-and-tense.adoc` (RFC 2119 keyword declaration and capitalization)
and an extension to the existing "Placeholders" section in
`11-code-blocks.adoc` (inline-prose URI Template syntax). TS-26 reached
Actionable=0 (30 of 30 actionable items resolved in total); its 6
Out-of-scope items and 2 Unresolved references remain open, so it stays in
this table.

TS-39 was authored from a pure stub on 2026-08-14 and now has zero
actionable items but stays in this table rather than joining the
fully-resolved list, because 5 Out-of-scope items and 4 Unresolved
references remain open. TS-4, TS-16, and TS-27 all have zero actionable
items but stay in this table rather than joining the fully-resolved list,
because each has an unresolved resource still open — TS-4's reference
directory no longer exists anywhere in the repository and re-fetching it has
failed on every run so far; TS-16's is `Program-Behavior.html`, still
unfetchable (not re-attempted, since its content was already captured via a
sub-agent in a prior run); TS-27's is a stub reference file (see the file's
`## Unresolved` entry) not yet re-fetched. TS-29 and TS-26 join this group
for the same reason — two unfetched references each: YouTube for TS-29; for
TS-26, a binary PDF with no text-extraction tool available, and a set of
link-collection files whose ~40 linked URLs were never individually fetched.
TS-15 joins this group too, with 12 Unresolved references — the largest
Unresolved count in the repository — mostly JavaScript-rendered design-system
sites (Apple HIG, Salesforce Lightning, Material Design) and dead links that
returned 404 or connection errors when fetched.

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

TS-21 (HTTP APIs) was closed out on 2026-08-14, in two sessions across six
`close-gaps` batches: all 8 Missing items in the first three batches (an
earlier session), then all 39 Partial items in the next three batches
(hypermedia/actions/uploads/bulk-correlation; async operations/error
handling/versioning/headers; concurrency control/PATCH/common types/version-
justification checklist; then a dedicated batch for the 9 remaining
independent Partial items; then a final dedicated batch for the six
interrelated Brandur idempotency-key entries, which substantially
restructured `10-safeness-and-idempotency.adoc` with new sections on
naturally-idempotent design, genuinely non-idempotent operations,
idempotency-key locking, atomic phases, foreign state mutations, and passive
safety). All 13 Out-of-scope items were then walked with the user in a
follow-up pass: 9 confirmed out-of-scope outright; 2 confirmed out-of-scope
for TS-21 but routed to TS-26 and TS-20's own `GAPS.md` files as new Missing
items instead of being dropped; 1 closed with a cross-reference added to
TS-21 itself (PII in URLs → TS-52/TS-53); and 1 closed by a new "Alternative
HTTP API styles" section in TS-21 briefly surveying HAL/JSON:API/Siren/Ion/
OData/JSON-LD, which also folded in the JSON-RPC out-of-scope item. This
required inserting a new partial before the standard's references partial,
renumbering `20-references.adoc` → `21-references.adoc` via `git mv`. 3 of
TS-21's 4 Unresolved items (Stack-Overflow-adjacent, Cloudflare-blocked) were
re-attempted and dismissed; the fourth (a YouTube transcript) was left open,
keeping TS-21 in this table at 0 actionable / 0 out-of-scope / 1 unresolved.

TS-43 (Relational databases and SQL) was restored to this table's rows on
2026-08-14 — it was previously omitted, despite genuinely having 6 open
Out-of-scope items and 4 Unresolved references in its own `GAPS.md`, an
oversight in an earlier regeneration rather than new work. Its actionable
count has been 0 since the 2026-08-14 `close-gaps` run described above.

TS-39 (HTML) was authored from a pure stub on 2026-08-14, closing all 136 of
its actionable items — over two fifths of the repository's prior total — in
one run, rather than needing the several passes a batch-oriented
`close-gaps` run would ordinarily take. Thirteen new content partials were
written (`01-fundamentals.adoc` through `13-accessibility.adoc`), covering
document fundamentals, the document head, text content, tables, hyperlinks,
forms and buttons, images, SVG, audio/video and embedded content, scripting
conventions and templates, metadata schemas and semantics,
internationalization, and accessibility. Five internal contradictions in the
source reference material were each resolved as an explicit editorial
decision recorded in the standard's own prose rather than left unreconciled:
`<dl>` and `<caption>` are permitted, not blanket-forbidden; `<b>`/`<i>`/
`<small>` are permitted for their specific semantic meanings, not
blanket-forbidden; RDFa Lite is preferred over Microdata for Schema.org; and
`<base href>` carries no trailing slash. TS-39's 5 Out-of-scope items and 4
Unresolved references were carried forward unresolved, so it stays in the
open-items table above (at Actionable=0) rather than joining the
fully-resolved list.

TS-33 (Java) was closed out across five `close-gaps` batches on 2026-08-15,
run back-to-back the same day: the first closed the 22-item Javadoc-content
cluster in `07-comments.adoc` (tag semantics, description phrasing, scope
exceptions, thread-safety documentation) plus the summary-fragment
contradiction with TS-33's own primary source (Google's Java Style Guide),
which the standard had misquoted; the second closed the standard's largest
single finding, a new "Nullability" section in `06-types.adoc` covering
`Optional`, method-chain `NullPointerException` risk, and eight nullability-
annotation libraries (correcting a copy-paste error in the source's own
library table along the way); the third closed the remaining Oracle
`codeconventions-comments#385` items in `07-comments.adoc`, withdrawing one
(a multi-line block-comment format that would have contradicted TS-33's own
pre-existing example) rather than forcing it in; the fourth closed a
modern-Java-features cluster spread across six files (records, `package-
info.java`/`module-info.java` structures, switch expressions, text blocks,
the unnamed-variable `_` syntax, grouping parentheses, `Object.finalize`,
explicit constructors); and the fifth closed the final 4 Missing and 8
Partial items, including two genuine scope calls the user was asked to
settle directly rather than have decided silently — writing in Java Platform
Module System directive-ordering guidance (previously left open as
possibly out-of-scope), and adopting Google's broader visibility-based
Javadoc-scope obligation (every non-`private` class/member, including record
components) in place of TS-33's narrower `public`/`protected`-only rule.
All 55 of TS-33's actionable items are now closed; it stays in the
open-items table above (at Actionable=0) only because its 3 Out-of-scope and
4 Unresolved items remain open, the same shape as TS-4, TS-16, TS-21, TS-27,
TS-29, TS-43, and TS-15. TS-33's own `GAPS.md` carries the full per-item
resolution notes; see the standard-by-standard history there for what each
batch actually wrote.

## Standards with neither a stub nor a GAPS.md

TS-1, TS-17, TS-19, TS-22, TS-28, TS-30, TS-32, TS-34, TS-45, TS-47, TS-51,
TS-53, TS-55, TS-56, TS-58, TS-59, TS-60, TS-62, and TS-63 all have
substantive content and no recorded gap analysis. A gap analysis
(`/gap-analysis`) could be run against any of them; none is known to be
missing content today.

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
  that reason. A twelfth instance of this pitfall recurred on 2026-08-14 in
  TS-18's `06-references.adoc`, referencing the newly-added "Reflows,
  repaints, and layout thrashing" section — fixed the same way, with an
  explicit `[#reflows-repaints-and-layout-thrashing]` anchor.

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

- **RESOLVED — TS-43 closed out in one run; table omission fixed
  2026-08-14.** All 61 of TS-43's actionable items (59 Missing, 2 Partial)
  were closed by a `close-gaps` run on 2026-08-14, across six new content
  partials (`02-sql-style.adoc` through `07-transactions-and-consistency.adoc`).
  One genuine naming conflict surfaced mid-run — general column-naming
  guidance says avoid a bare `id`, while primary-key guidance mandates it —
  resolved by scope: `id` is reserved for the primary key, every other
  identifier column follows the descriptive-naming rule. TS-43's 6
  out-of-scope and 4 persistently-unfetchable reference items remain open in
  its own `GAPS.md`, since neither is an actionable count — but a prior
  regeneration of this file incorrectly stated TS-43 "moved to the
  fully-resolved list" and omitted its row from the open-items table
  entirely. It never belonged there: 6 open out-of-scope items and 4
  unresolved references is not "zero unchecked items of any kind". Corrected
  in the same-day 2026-08-14 regeneration that closed out TS-21, restoring
  TS-43's row to the table.

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
  user and relocated as 4 new Missing items in TS-18's `GAPS.md` (actionable
  56 → 60) rather than dropped — subsequently closed by TS-18's 2026-08-14
  `close-gaps` run as the new `05-css-layout-and-typography.adoc` partial.
  TS-37's `GAPS.md` reached zero unchecked items of any kind, so it moved
  directly from the stub table to the fully-resolved list — the first
  standard in this file's history to do so in a single run, rather than
  first losing its stub status and later being worked by a separate
  `close-gaps` pass.

- **RESOLVED — TS-38 authored from a pure stub and fully resolved in one
  run.** TS-38 (Node.js applications) previously held only a `// TODO`
  placeholder and a legacy-format `GAPS.md` with one open gap (no guidance on
  the stateless-service / horizontal-scaling pattern, sourced from the
  Pragmatic Engineer's Bluesky piece — the same source TS-41 already cited
  for a different purpose). On 2026-08-14 it was authored from scratch — an
  introductory paragraph on the page plus six new content partials
  (`01-module-system.adoc` through `06-stateless-scaling.adoc`) covering the
  CJS/ESM module system, package and dependency management, configuration
  and environment, process lifecycle and signals, error handling and
  logging, and stateless horizontal scaling. Scope was deliberately kept to
  Node.js application/runtime concerns, cross-referencing rather than
  duplicating TS-36 (the JavaScript/TypeScript language itself), TS-21 (HTTP
  API design), TS-52 (secrets management), TS-49 (containerized deployment),
  and TS-6 (the underlying statelessness/idempotency principles). The one
  recorded gap was closed against the new "Stateless scaling" section, and
  the source added to the page's `== References`. TS-38's `GAPS.md` reached
  zero unchecked items of any kind, so it moves directly from the stub table
  to the fully-resolved list, joining TS-37 as the second standard to make
  that move in a single run. Unlike every other stub authored so far, TS-38
  did have a `GAPS.md`, so the resolution note lives in that pre-existing
  legacy-format file rather than requiring a new one — the file's own
  single-gap shape needed no conversion to the template format to record
  the closure. Its `**RESOLVED.**` marker (period inside the bold, unlike
  every other legacy file's `**RESOLVED**`) is a known trap for the
  mechanical regeneration script — see
  [Regenerating this file](#regenerating-this-file).

- **RESOLVED — TS-44 authored from a pure stub and fully resolved in one
  run.** TS-44 (Non-relational (NoSQL) databases) previously held only a
  `// TODO` placeholder and a legacy-format `GAPS.md` with two open gaps: no
  guidance on polyglot persistence (sourced from an Allegro Tech engineering-
  culture post) and no NoSQL database selection criteria (sourced from the
  same Pragmatic Engineer Bluesky piece already cited by TS-38 and TS-41). On
  2026-08-14 it was authored from scratch — an introductory paragraph on the
  page plus five new content partials (`01-data-models.adoc` through
  `05-operational-considerations.adoc`) covering key-value/document/wide-
  column/graph/search data models, query-first schema and modeling patterns
  (embedding vs referencing, denormalization, aggregate boundaries), NoSQL-
  specific consistency and replication trade-offs, database selection
  (polyglot persistence and selection criteria), and operational concerns
  (indexing, backup, monitoring, schema evolution). Scope was deliberately
  kept to NoSQL-specific concerns, cross-referencing rather than duplicating
  TS-43 (which already owns the ACID/BASE/CAP-theorem treatment in depth),
  TS-46 (general distributed-data and caching guidance), TS-5 (per-service
  architecture and persistence decoupling), and TS-45 (data migration
  mechanics). Both recorded gaps were closed against the new "Polyglot
  persistence" and "NoSQL database selection criteria" sections, and both
  sources added to the page's `== References`. TS-44's `GAPS.md` reached zero
  unchecked items of any kind, so it moves directly from the stub table to
  the fully-resolved list, joining TS-37 and TS-38 as the third standard to
  make that move in a single run. Like TS-38, TS-44 already had a `GAPS.md`,
  so the resolution notes live in that pre-existing legacy-format file rather
  than requiring a new one — its own two-gap shape needed no conversion to
  the template format to record the closure.

- **RESOLVED — TS-15 and TS-18 closed out jointly in one run.** A
  `close-gaps` run on 2026-08-14 was applied to both TS-15 (User interfaces)
  and TS-18 (Web GUIs) together, at the user's explicit request, specifically
  to catch gaps recorded against the wrong one of the two standards. Both
  files' items were re-read against each other's scope before any content was
  written; none needed to move. TS-15 closed all 51 of its actionable items
  and stays in the open-items table only for its Out-of-scope/Unresolved
  counts (see the table note above). TS-18 closed 59 of 60, leaving one
  (neurodiversity.design) open pending a proper source re-fetch, and gained
  two new partials plus a renumbered references partial (see the table note
  above). Several TS-18 items closed in this run carry an inherited scope
  flag (bordering TS-5, application architecture) that was restated for the
  user rather than resolved silently, consistent with how this file has
  always treated a scope call as the user's decision.

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
the open-items table. TS-29 and TS-15 are the same shape: TS-29 has 0
actionable / 0 out-of-scope but 2 Unresolved references still unchecked;
TS-15 has 0 actionable but 7 Out-of-scope and 12 Unresolved still unchecked.
A legacy-format file must be checked the same way — count `## <gap title>`
subsections against `**RESOLVED**` markers, per the script above — rather
than assumed resolved because it is short or old: TS-38 and TS-44 were
wrongly marked fully resolved in a prior pass for exactly this reason.

The legacy-format script also has one known false negative: it matches the
literal string `**RESOLVED**`, but TS-38's `GAPS.md` closes its one gap with
`**RESOLVED.**` (the period sits inside the bold markup, not after it) — the
only file in the repository written that way. The script reports TS-38 as
`actionable=1` even though the gap is genuinely closed; verify any legacy
file the script reports as non-zero by reading it before trusting the count,
the same caution the script's template branch already needs for its
Out-of-scope/Unresolved blind spots.
