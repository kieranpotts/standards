# TS-36 deep dive

Findings from a deep review of TS-36: ECMAScript (JavaScript/TypeScript)

~5,880 lines across 15 `.adoc` files (14 numbered sections + `README.adoc`) and an
`AGENTS.md`.

Assessed against the repository [style guide](../../docs/style-guide.md),
[TS-26: Technical Writing Style Guide](../026/README.adoc),
[TS-28: AsciiDoc](../028/README.adoc), [TS-27: Markdown](../027/README.adoc), and
the [template](../../template/).

**Assessment.** The standard is broad and largely sound: 14 coherent sections
cover the language, modules, packages, tooling, types, asynchrony, FP, runtimes,
and quality, ported from legacy drafts into the project's AsciiDoc conventions.
The problems are concentrated in two places: correctness defects carried over
from the source drafts (a few wrong claims and broken code examples), and
line-length/xref conformance violations introduced during the bulk port. The
single dominant category is conventions (long lines from link-heavy reference
and prose paragraphs), followed by a handful of factual errors and broken
cross-references.

**Status:** All four tiers applied and verified. Tier 1 (Correctness) — 13
  items (9 contradictions + 4 factual). Tier 2 (Coherence) — 3 items resolved
  (private-members duplication confirmed already cross-referenced; Date and
  Decorators left in place by user decision), 1 originally deferred to Tier 4
  (recurring short titles) and since resolved (see below). Tier 3
  (Completeness) — 2 items resolved (Node version examples generalized to
  placeholder notation across 5 spots in 11-runtimes.adoc and 3 spots in
  06-packages-and-tooling.adoc — the latter two weren't separately named in the
  original item but shared the identical defect; TypeScript minimum-version
  floor dropped in favour of the existing always-upgrade policy). A new
  style-guide rule was added (`docs/style-guide.md` §Conventions) prohibiting
  pinned real version numbers of fast-moving tools in illustrative examples, to
  prevent recurrence repo-wide. Tier 4 (Conventions) — all 11 §5 convention
  items resolved (README.adoc references and long-line prose across
  02/05/10-*.adoc rewrapped; `[source,...]` attributes added to
  14-barrel-files.adoc and 08-typescript.adoc; en-dash/bold-terminology/
  semicolon conformance fixed); §6 `AGENTS.md` regenerated from stub via the
  `agentify` skill (855 lines, 19 topic subsections, cross-references verified
  against `src/README.adoc`); all 7 §7 prose defects resolved, including a
  full-sweep rewrite of general-behaviour "we"/"our" in 01/07/08/10/11 (scope
  confirmed with user for 10 and 11) while preserving the one genuine
  team-position exception in 10 (`We SHOULD apply FP principles to our code`).
  While re-reading 11-runtimes.adoc, found and fixed a leftover defect from the
  Tier 3 pass: two spots still pinned literal Node version numbers/codenames
  (Dubnium/Hydrogen, a dated Feb 2022/2023 example, and a duplicate `.Example`
  block), violating the very style-guide rule Tier 3 introduced — not caught by
  that pass's own verification (see §8). The deferred recurring-short-titles
  item was converted from reactive to proactive by user decision and resolved:
  27 explicit `[#id]` anchors added across the 13 duplicate-title groups. All
  four tiers of the deep dive are now fully resolved; nothing left open.
  Tier 4 (§5-§7, §8) committed as 35a3b12; the short-titles anchor pass is
  staged but not yet committed.

## Priority order

1. **Correctness.** Contradictions, factual errors, and broken
   cross-references/examples. A reader cannot comply with a standard that says
   two incompatible things, and a wrong claim about the language is worse than a
   style slip.

2. **Coherence.** Structural problems. Structure must settle before content is
   added to it.

3. **Completeness.** Coverage gaps and staleness. Filled into a structure that
   has stopped moving.

4. **Conventions.** Style-guide conformance, `AGENTS.md` drift, and prose
   defects. Last, because content edits invalidate cosmetic fixes made too
   early.

## 1. Contradictions

- [x] 01-language-fundamentals.adoc:145 listed "Object" among "six primitive
  types" while 01:147 said "Most things in JavaScript are objects" — Object is
  not a primitive, so the two statements conflicted. Fixed: rewritten to "seven
  types: six primitives (`undefined`, `null`, `boolean`, `number`, `string`,
  `symbol`) and `object`". (Also resolves the §2 factual item.)

- [x] 05-modules.adoc:193-199 recommended `require('./config.json')` to load
  JSON, which is CommonJS and contradicted the section's own ESM mandate at
  05:3-7. Fixed: replaced with the ESM import-attribute form
  (`import config from './config.json' with { type: 'json' }`), an `fs`+
  `JSON.parse` fallback, and an explicit note that `require()`-based JSON
  loading MUST NOT be used.

- [x] 01-language-fundamentals.adoc:276-278 stated that function expressions
  MUST end with a semicolon but the example lacked one. Fixed: added the trailing
  `;` to `const doSomething = function () { ... };`.

- [x] 13-quality-assurance.adoc:44 had `Cat.meet()` throw `new Error(...)` but
  the test at 13:70-73 asserted `.to.throw(TypeError)`. Fixed: changed `meet()`
  to throw `TypeError`, matching the test and the standard's own guidance that
  `TypeError` suits an invalid/missing parameter.

- [x] 06-packages-and-tooling.adoc:793 used ESM `import` but then `__dirname`
  (undefined in ESM). Fixed: replaced `path.resolve(__dirname, './dist')` with
  `fileURLToPath(new URL('./dist', import.meta.url))` (and `import { fileURLToPath }
  from 'node:url'`), dropping the now-unneeded `path` import.

- [x] 04-objects-and-classes.adoc:110 had `const b = {foo:'bar'}` then `b = a`
  (a TypeError: assignment to const). Fixed: changed `const b` to `let b` so the
  reassignment is valid.

- [x] 03-functions.adoc:4 split the `<<Naming conventions>>` xref across two
  lines. Fixed: rewrapped so the xref sits intact on one source line.

- [x] 06-packages-and-tooling.adoc:159 split the
  `<<Package command line interfaces>>` xref across two lines. Fixed: rewrapped
  so the xref sits intact on one line.

- [x] The `<<Functions>>` xref (used in 02:150, 02:543, 02:850) resolved to
  three sections titled "Functions". Decision (per the recommended option):
  renamed the two 02 Comments subsections — `=== Functions` (02:629) to
  `=== Documenting functions` and `==== Functions` (02:450) to `==== Function
  types` — and retargeted the 02:543 and 02:850 xrefs at `<<Documenting
  functions>>`. `02:150`'s `<<Functions>>` now resolves uniquely to section 03
  (the only remaining "Functions" heading). Verified: no xref-ambiguity
  remains. No anchor needed on 03.

## 2. Factual errors

- [x] 01-language-fundamentals.adoc:145 — resolved by the §1 fix above
  (rewritten to seven types: six primitives + `object`).

- [x] 05-modules.adoc:4 called CommonJS "proprietary." Fixed: dropped
  "and proprietary" (now "Node's default module system").

- [x] 05-modules.adoc:122-130 stated `NODE_PATH` affects ESM `import`. Fixed:
  clarified it extends lookup for `require()` and "does not affect ESM
  `import`."

- [x] 01-language-fundamentals.adoc:259 said bitwise operators "are slow".
  Fixed: reworded to the accurate concern — they "coerce operands to 32-bit
  integers and obscure intent when misused."

## 3. Structural problems

- [x] "Version number constraints" was a duplicate title in both 07 and 11.
  Fixed: renamed 11's section to "Node version constraints" and replaced the
  restated content with a cross-reference to 07. The duplicate title is gone;
  07 keeps the full version-constraint rule.

- [x] The private-members rule is stated in two places: 04-objects-and-classes
  .adoc:237-277 ("Authors MUST NOT use TypeScript's `private` modifier ...")
  and 08-typescript.adoc:83-84 ("we use ECMAScript's `#` prefix ... rather than
  TypeScript's `private` modifier"). Same rule, two locations. Keep it in one and
  cross-reference. Resolved: on re-reading, 08:83-85 already states the rule only
  as a one-sentence *example* of the broader "prefer standard ECMAScript over
  TS-specific notation" principle and immediately cross-references
  `<<Private members>>`, which resolves uniquely to 04:237. The full normative
  rule lives in 04; 08's mention is a cross-referenced example, not a duplicate
  rule. No edit needed.

- [x] 11-runtimes.adoc:233 ("== Date") documents a language native object under
  "Runtimes". Date is not a runtime concern; it belongs in 01 Language
  fundamentals (or its own section). [User decision — minor.] Resolved: left in
  place. The section is not about the `Date` type but about runtime/engine
  portability pitfalls of `Date` (`new Date('invalid')` returning an instance,
  `toISOString()` always UTC, `toLocaleString()` output varying across engines
  and ECMA-402 availability) — genuine runtime concerns. Moving it would also
  collide with 01's existing structure. No edit.

- [x] 08-typescript.adoc:265 ("== Decorators") covers an ECMAScript feature that
  is not TypeScript-specific. It may fit better under 03 Functions or 04 Objects
  and classes. [User decision — minor.] Resolved: left in place. The section
  explicitly frames decorators as TS-originated ("first reached most JavaScript
  developers via TypeScript and Angular") and currently ECMAScript-bound
  ("usable today via transpilation"); decorator syntax is still stage-3 and in
  practice used almost exclusively via TS. Moving it would split the
  member/class/field decorator material awkwardly. No edit.

- [x] Several short section titles recur across files (Operators, Loops, Arrays,
  Classes, Objects, Promises, Parameters, Callbacks, References, `engines`,
  `type`, `scripts`, Performance). None is currently an xref target, but each is
  a latent xref-ambiguity risk if one is ever referenced. Worth a pass to
  disambiguate (explicit anchors) where titles repeat. [Low priority.] Deferred
  to Tier 4 (Conventions) by user decision. Mechanical xref-uniqueness check
  across TS-36 confirmed zero ambiguous targets today; handle reactively when a
  real xref needs disambiguation. Resolved (converted from reactive to
  proactive by user decision): added an explicit `[#id]` anchor above each of
  the 27 duplicate-titled headings (13 title groups, 2-3 occurrences each),
  using descriptive kebab-case ids that distinguish each occurrence by content
  (e.g. `#operators` vs `#typescript-operators`; `#engines-package-manifest`
  vs `#engines-repository-manifest`). Existing title-text xrefs (`<<...>>`)
  are unaffected — none targeted a duplicate title, and the new explicit ids
  are additive, giving future xrefs an unambiguous target without changing
  current auto-generated anchor resolution. Verified no duplicate ids and no
  new line-length violations.

## 4. Coverage gaps

- [x] 11-runtimes.adoc:11-14, 42-43, 29-37, 83 and 06:84 gave concrete Node
  version examples dated 2022-2023 referencing Node 10/12/14/16/18, all EOL by
  2026. [User decision: generalise, and capture the policy in the style guide.]
  Fixed: all five spots in 11-runtimes.adoc rewritten to state the release
  policy in prose (current = odd major above active LTS; maintenance = the two
  even majors before it) with `engines` JSON examples using angle-bracket
  placeholders (`^<active-lts>.x.x`, etc.) instead of literal versions; the
  Dubnium–Hydrogen codename/patch-version list replaced with a generic
  statement that each major's LTS start is a specific patch, not `.0.0`,
  documented in that major's own changelog. The same defect also existed at
  06:670 and 06:719 (not separately named in this item) and was fixed
  identically. Added a new rule to `docs/style-guide.md` (§Conventions):
  illustrative examples MUST NOT pin real version numbers of fast-moving tools
  where the point is a policy/pattern, not a testable requirement — use
  placeholder notation instead.

- [x] 08-typescript.adoc:88 set "The minimum supported TypeScript version is
  4.5.0" (from 2021), stale for a 2026 standard. [User decision: drop the
  floor, keep the policy.] Fixed: removed the numeric floor; reworded to "No
  specific minimum version is mandated; a recent, actively-supported release
  SHOULD always be used," consistent with the section's existing
  always-upgrade-to-latest policy.

## 5. Convention conformance

- [x] README.adoc:35-97 — every reference entry places author + link + publisher
  + annotation on one source line, exceeding the 160-char hard limit (e.g. :35
  277, :57 272, :83 237). Per TS-28/23 only unbreakable URLs are excepted; wrap
  the publisher and annotation onto a continuation line (indented two spaces),
  matching the style-guide reference example. Fixed: all 30 entries rewrapped
  onto author/link/publisher/annotation lines; the 3 remaining over-160 lines
  are single unbreakable link macros (the documented TS-28 exception).

- [x] 02-syntax-and-style.adoc has many lines over 160 chars (mechanical check:
  :354, :356, :358, :487, :523, :547, :603, :643, :661, :690, :718, :747, :778,
  :840, :872, :901, :905, :934, :961, :983, :985, :987, :1018, :1040, :1044,
  :1053, :1055). Soft-wrap the prose to ≤160, keeping inline link macros on one
  line. Fixed: all flagged lines (line numbers had drifted from earlier Tier
  1-3 edits; a fresh mechanical check found 28 current offenders) rewrapped;
  file is now clean.

- [x] 05-modules.adoc:528 is a single 799-char paragraph containing seven
  inline links. Wrap at sentence/clause boundaries, keeping each link macro
  intact. Fixed, plus one more over-160 line found at the same mechanical
  check (:489).

- [x] 10-functional-programming.adoc:22 (165), :525 (175), :533 (248), :787
  (162), :788 (247) — link-heavy lines exceed 160. Wrap surrounding prose, keep
  link macros intact. Fixed.

- [x] 14-barrel-files.adoc:12-47 — the TS/JS code blocks use bare `----`
  without a `[source,<lang>]` attribute. TS-28/06 requires a language attribute
  (e.g. `[source,typescript]`). [Pre-existing barrel-files content.] Fixed:
  `[source,typescript]` added to the four TS/JS blocks; `[source,plaintext]`
  added to the one non-language directory-tree diagram.

- [x] 08-typescript.adoc:153-156 — the compiler error message is in a bare
  `----` block; TS-28/06 recommends `[source,plaintext]` for non-language
  code. Fixed.

- [x] 07-dependency-management.adoc:20 uses an ASCII hyphen-minus (" - ") as a
  dash ("regularly - best practice") where the rest of TS-36 uses an en dash
  ("–"). Use an en dash for consistency. Fixed.

- [x] 14-barrel-files.adoc:7 uses an em dash ("—") for a parenthetical aside
  where the rest of TS-36 uses an en dash ("–"). Use an en dash for
  consistency. Fixed.

- [x] 01:181 (`*truthy*`/`*falsy*`), 09:142 (`*async iterators*`), and
  10:543-544 (`*tacit programming*`/`*point-free style*`/`*point-free
  composition*`) use bold for new terms at their point of definition. TS-26/06
  reserves bold for UI elements and italics for introducing a new term. Use
  italics. Fixed.

- [x] 06:875-882 bold lead-ins `*Package cohesion*` and `*Package coupling*`
  are followed by an en dash, not terminated with a period. The style guide
  requires lead-in labels to be bold and terminated with a period
  (`*Package cohesion.* ...`). The `*`Promise.all`* – ...` pattern at 09:73-84
  is the same shape; apply consistently. Fixed both spots (06's two lead-ins,
  09's four `Promise.*` combinator bullets).

- [x] 10-functional-programming.adoc:886 and :902 end function-expression examples
  with a trailing `;`, inconsistent with the other examples in TS-36 (which omit
  semicolons). Drop for consistency. Fixed.

## 6. `AGENTS.md` drift

- [x] AGENTS.md is a stub (`<!-- TODO -->`) and does not cover any of the 14
  sections' rules. It should be regenerated to reflect the current content (the
  `agentify` skill is the intended tool). Fixed: regenerated from scratch via
  the `agentify` skill (855 lines, 19 topic subsections under `## Rules`, plus
  `## References`). All RFC 2119 keywords preserved faithfully; sibling
  cross-references (TS-27, TS-37, TS-38, TS-47, TS-52, TS-12, TS-13) verified
  to exist and resolve.

## 7. Prose defects

- [x] First-person "we/our" is used for general behaviour, not only genuine
  team-position, contrary to TS-26/01 (which reserves "we" for the author's or
  team's position). Representative general-behaviour uses: 01:46/52/60,
  07:34-45/120-123, 08:80-88, 10:60/107/292/592/600/671/908, 11:24/71-77.
  Genuine team-position statements such as 10:923 ("We SHOULD apply FP
  principles to our code") are acceptable and should be kept. Recommend a pass
  to convert general-behaviour "we" to impersonal or "you". [Judgment call —
  user may set scope.] Resolved: 01/07/08 fixed to the representative lines
  named above. For 10/11, user chose a full sweep rather than just the named
  lines (10-functional-programming.adoc had ~50 "we"/"our" instances,
  including tutorial-walkthrough narration not originally flagged); all
  general-behaviour instances converted to impersonal/"you" phrasing across
  both files, preserving the one genuine team-position exception verbatim
  (10: "We SHOULD apply functional programming principles to our
  JavaScript/TypeScript code").

- [x] 10:88-92 — the claim that `val1 === val2` "will always return `false`
  because every value is guaranteed to exist in a different memory space" is
  muddled: it is true of any two distinct object references, not a consequence
  of immutability. Reword for clarity. Fixed: reworded to state reference
  equality directly, then explain why immutability makes that a useful change
  check.

- [x] 05:99 — "you cannot import directories ... you MUST specify the `index.js`
  file name" overstates the case (ESM supports directory imports via package
  `exports`); the real point is that relative imports need explicit extensions.
  Tighten. Fixed: reworded to state the actual point (ESM relative imports
  don't auto-resolve to `index.js` the way CJS `require()` does). Also fixed
  the same overstatement where it had been echoed into the new `AGENTS.md`.

- [x] 12-architecture-and-design.adoc:11 — "constructed using Domain-Driven
  Design (DDD) building methods" is awkward ("building methods"). Reword, e.g.
  "built using Domain-Driven Design (DDD)". Fixed.

- [x] 03-functions.adoc:17-24 — the example places `function fooBar () {}` and
  `const fooBar = () => {}` in one block; the `const` redeclares the
  function-declared `fooBar` (a `SyntaxError` if run as one snippet). Split into
  two blocks or rename one identifier. Fixed: renamed the second identifier to
  `bazQux`.

- [x] 01:368-370 — prose says guard `for...in` with "hasOwnProperty" but the
  example uses `Object.hasOwn`. Use the same identifier in prose and code
  (`Object.hasOwn` is the current API). Fixed.

## 8. Regression found during Tier 4 re-read

- [x] While re-reading 11-runtimes.adoc for the "we/our" pass, found the Tier 3
  fix for pinned Node versions (§4 above) was incomplete: two spots still
  pinned literal version numbers/codenames — a dated "in February 2022 ...
  v17 ..." example, the "Dubnium"/"Hydrogen" codename example
  (`v10.13.0`/`v18.12.0`), and a duplicate `.Example` JSON block
  (`^14.15.0 || ...`) that just repeated the placeholder example above it with
  real numbers. All three directly violated the style-guide rule Tier 3 itself
  introduced, and Tier 3's own verification pass hadn't caught them. Fixed:
  removed the dated example and codename illustration, deleted the duplicate
  `.Example` block, and cleaned up stray blank lines left over from the Tier 3
  edit.