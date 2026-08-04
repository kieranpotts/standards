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

**Status:** Tier 1 (Correctness) applied and verified — 13 items (9
  contradictions + 4 factual). Tiers 2–4 open. No tiers committed yet.

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

- [ ] "Version number constraints" is a section title in both
  07-dependency-management.adoc and 11-runtimes.adoc, and 11:104-110 restates
  07's `^`/`~` material (then cross-references it). Duplicate title plus
  overlapping content invites drift. Consolidate the version-constraint rule in
  07; in 11 keep only the Node-specific `engines` note or rename the section.

- [ ] The private-members rule is stated in two places: 04-objects-and-classes
  .adoc:237-277 ("Authors MUST NOT use TypeScript's `private` modifier ...")
  and 08-typescript.adoc:83-84 ("we use ECMAScript's `#` prefix ... rather than
  TypeScript's `private` modifier"). Same rule, two locations. Keep it in one and
  cross-reference.

- [ ] 11-runtimes.adoc:233 ("== Date") documents a language native object under
  "Runtimes". Date is not a runtime concern; it belongs in 01 Language
  fundamentals (or its own section). [User decision — minor.]

- [ ] 08-typescript.adoc:265 ("== Decorators") covers an ECMAScript feature that
  is not TypeScript-specific. It may fit better under 03 Functions or 04 Objects
  and classes. [User decision — minor.]

- [ ] Several short section titles recur across files (Operators, Loops, Arrays,
  Classes, Objects, Promises, Parameters, Callbacks, References, `engines`,
  `type`, `scripts`, Performance). None is currently an xref target, but each is
  a latent xref-ambiguity risk if one is ever referenced. Worth a pass to
  disambiguate (explicit anchors) where titles repeat. [Low priority.]

## 4. Coverage gaps

- [ ] 11-runtimes.adoc:11-14, 42-43, 29-37, 83 and 06:84 give concrete Node
  version examples dated 2022-2023 referencing Node 10/12/14/16/18, all EOL by
  2026. The "support the three active/maintenance LTS" policy is sound; the
  concrete numbers are stale. [User decision: update to current LTS or
  generalise the examples.]

- [ ] 08-typescript.adoc:88 sets "The minimum supported TypeScript version is
  4.5.0" (from 2021), stale for a 2026 standard. [User decision: bump or
  reword.]

## 5. Convention conformance

- [ ] README.adoc:35-97 — every reference entry places author + link + publisher
  + annotation on one source line, exceeding the 160-char hard limit (e.g. :35
  277, :57 272, :83 237). Per TS-28/23 only unbreakable URLs are excepted; wrap
  the publisher and annotation onto a continuation line (indented two spaces),
  matching the style-guide reference example.

- [ ] 02-syntax-and-style.adoc has many lines over 160 chars (mechanical check:
  :354, :356, :358, :487, :523, :547, :603, :643, :661, :690, :718, :747, :778,
  :840, :872, :901, :905, :934, :961, :983, :985, :987, :1018, :1040, :1044,
  :1053, :1055). Soft-wrap the prose to ≤160, keeping inline link macros on one
  line.

- [ ] 05-modules.adoc:528 is a single 799-char paragraph containing seven
  inline links. Wrap at sentence/clause boundaries, keeping each link macro
  intact.

- [ ] 10-functional-programming.adoc:22 (165), :525 (175), :533 (248), :787
  (162), :788 (247) — link-heavy lines exceed 160. Wrap surrounding prose, keep
  link macros intact.

- [ ] 14-barrel-files.adoc:12-47 — the TS/JS code blocks use bare `----`
  without a `[source,<lang>]` attribute. TS-28/06 requires a language attribute
  (e.g. `[source,typescript]`). [Pre-existing barrel-files content.]

- [ ] 08-typescript.adoc:153-156 — the compiler error message is in a bare
  `----` block; TS-28/06 recommends `[source,plaintext]` for non-language
  code.

- [ ] 07-dependency-management.adoc:20 uses an ASCII hyphen-minus (" - ") as a
  dash ("regularly - best practice") where the rest of TS-36 uses an en dash
  ("–"). Use an en dash for consistency.

- [ ] 14-barrel-files.adoc:7 uses an em dash ("—") for a parenthetical aside
  where the rest of TS-36 uses an en dash ("–"). Use an en dash for
  consistency.

- [ ] 01:181 (`*truthy*`/`*falsy*`), 09:142 (`*async iterators*`), and
  10:543-544 (`*tacit programming*`/`*point-free style*`/`*point-free
  composition*`) use bold for new terms at their point of definition. TS-26/06
  reserves bold for UI elements and italics for introducing a new term. Use
  italics.

- [ ] 06:875-882 bold lead-ins `*Package cohesion*` and `*Package coupling*`
  are followed by an en dash, not terminated with a period. The style guide
  requires lead-in labels to be bold and terminated with a period
  (`*Package cohesion.* ...`). The `*`Promise.all`* – ...` pattern at 09:73-84
  is the same shape; apply consistently.

- [ ] 10-functional-programming.adoc:886 and :902 end function-expression examples
  with a trailing `;`, inconsistent with the other examples in TS-36 (which omit
  semicolons). Drop for consistency.

## 6. `AGENTS.md` drift

- [ ] AGENTS.md is a stub (`<!-- TODO -->`) and does not cover any of the 14
  sections' rules. It should be regenerated to reflect the current content (the
  `agentify` skill is the intended tool).

## 7. Prose defects

- [ ] First-person "we/our" is used for general behaviour, not only genuine
  team-position, contrary to TS-26/01 (which reserves "we" for the author's or
  team's position). Representative general-behaviour uses: 01:46/52/60,
  07:34-45/120-123, 08:80-88, 10:60/107/292/592/600/671/908, 11:24/71-77.
  Genuine team-position statements such as 10:923 ("We SHOULD apply FP
  principles to our code") are acceptable and should be kept. Recommend a pass
  to convert general-behaviour "we" to impersonal or "you". [Judgment call —
  user may set scope.]

- [ ] 10:88-92 — the claim that `val1 === val2` "will always return `false`
  because every value is guaranteed to exist in a different memory space" is
  muddled: it is true of any two distinct object references, not a consequence
  of immutability. Reword for clarity.

- [ ] 05:99 — "you cannot import directories ... you MUST specify the `index.js`
  file name" overstates the case (ESM supports directory imports via package
  `exports`); the real point is that relative imports need explicit extensions.
  Tighten.

- [ ] 12-architecture-and-design.adoc:11 — "constructed using Domain-Driven
  Design (DDD) building methods" is awkward ("building methods"). Reword, e.g.
  "built using Domain-Driven Design (DDD)".

- [ ] 03-functions.adoc:17-24 — the example places `function fooBar () {}` and
  `const fooBar = () => {}` in one block; the `const` redeclares the
  function-declared `fooBar` (a `SyntaxError` if run as one snippet). Split into
  two blocks or rename one identifier.

- [ ] 01:368-370 — prose says guard `for...in` with "hasOwnProperty" but the
  example uses `Object.hasOwn`. Use the same identifier in prose and code
  (`Object.hasOwn` is the current API).