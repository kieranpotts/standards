# TS-36 gap analysis

Gaps found comparing TS-36: ECMAScript (JavaScript/TypeScript) against the
following reference resources:

- https://ricostacruz.com/rsjs/ (rsjs — "Reasonable System for JavaScript
  Structure")
- https://bitsofco.de/what-is-tree-shaking/ (Aderinokun — "What is tree
  shaking and how does it work?")
- https://www.sitepoint.com/premium/books/javascript-best-practice/read/1/
  (SitePoint — *JavaScript: Best Practice*, ch. 1 "The Anatomy of a Modern
  JavaScript Application"; chapters 2–8 are paywalled)
- https://mythbusters.js.org/ (Kikobeats — *MythBusters JS*, a JavaScript
  performance & readability handbook; source repo
  https://github.com/Kikobeats/js-mythbusters)

**Assessment (rsjs).** RSJS is a guide for structuring JavaScript in *non-SPA,
server-rendered web applications* — component behaviors bound to DOM
subtrees, `data-js-*` selector conventions, inline-script avoidance, meta-tag
data bootstrapping, jQuery-era initialization patterns, and legacy
concatenation/bundling recipes. TS-36's stated scope is *language coding
conventions* for ECMAScript (syntax, style, functions, classes, modules,
packages, dependencies, TypeScript, async, FP, runtimes, architecture,
testing). It explicitly delegates browser/DOM API guidance to TS-37 and
application-level Node concerns to TS-38. The overwhelming majority of RSJS
therefore sits outside TS-36's stated purpose — it is front-end/DOM
architecture, not language convention — and is recorded below as
out-of-scope for the user to confirm or overrule. A small number of items
overlap TS-36's in-scope sections (modules, bundling, global state) and are
recorded as missing or partial.

**Assessment (bitsofco.de tree-shaking).** The article is a single-concept
explainer aimed at beginners, entirely within TS-36's stated scope since
TS-36 explicitly covers bundling and tree shaking in its "Transpilation and
bundling" and "Dynamic imports and code splitting" sections. TS-36 covers
the core definition (eliminating unused exports) and the ES-modules
prerequisite. The gaps are the surrounding mechanics the article explains
that TS-36 omits: side effects and the `sideEffects` manifest field, the
limits of tree shaking, and concrete illustrations of what gets shaken.

**Assessment (SitePoint *JavaScript: Best Practice*, ch. 1).** A beginner-level
overview of the modern JS landscape. It is narrower than TS-36 in every
in-scope area it touches (let/const, arrow functions, classes, promises/async,
modules, CommonJS, npm, package.json, Babel, bundlers, linting) — TS-36 covers
each more deeply, including the `const`-binding-vs-value gotcha the article
illustrates (`src/036/02-syntax-and-style.adoc:120`). Per the "reference
narrower than the standard" edge case, those topics are not findings. The only
content the chapter covers that TS-36 does not is out-of-scope: build task
runners (Grunt/Gulp), SPA and Universal/Isomorphic application architecture,
deployment workflow and CI servers, and the KISS principle. Chapters 2–8 were
not retrievable (paywalled) and are listed under Unresolved.

**Assessment (MythBusters JS).** A JavaScript performance & readability
handbook (~30 short tip pages across Array, Date, Number, Function, RegExp,
Object, V8, and Workflow topics). It is overwhelmingly a *performance
micro-optimization* guide — V8 hidden classes, monomorphism, inline
initialization, sparse-array storage, property-access caching, loop reversal,
etc. TS-36 deliberately does not cover engine micro-optimization; its QA
section states "Don't over-optimize early. Optimize only once a program is
provably too slow, and only the slow parts." The great majority of the
handbook is therefore out-of-scope. The in-scope gaps are concentrated where
the handbook states *correctness/usage* guidance that TS-36 omits: RegExp
method and flag usage (TS-36 has no RegExp guidance at all), string-to-number
parsing specifics, the `new`-omission behavior of custom constructors,
deep-clone anti-patterns, and WeakMap for private state.

**Status:** Re-run, 2026-08-05.
  - rsjs: all four in-scope gaps (2 missing, 2 partial) have been addressed in
    the standard and are checked off below. The 15 web-client out-of-scope
    items have been relocated to `src/018/GAPS.md` (TS-18: Web GUIs) at the
    maintainer's direction; see the note under Out-of-scope below.
  - bitsofco.de tree-shaking: first run against this reference. 4 missing and
    3 partial gaps identified below; all open.
  - SitePoint *JavaScript: Best Practice*: first run against this reference.
    0 missing, 0 partial, 5 out-of-scope (see below); chapters 2–8 paywalled.
  - MythBusters JS: first run against this reference. 4 missing and 4 partial
    gaps identified below; all open. The remaining content is out-of-scope
    (engine micro-optimization) and grouped under Out-of-scope.

## Missing

- [ ] https://mythbusters.js.org/regexp/correct-methods.md#use-the-correct-method —
      TS-36 has no guidance on choosing between `RegExp.prototype.test`
      (boolean match), `String.prototype.match`/`matchAll` (retrieval with the
      `g` flag), and `.exec`. The handbook recommends `.test` for fast boolean
      checks and `.match` to retrieve all matches under the `g` flag. Recommend
      a new "RegExp" subsection under "Operators"
      (`src/036/01-language-fundamentals.adoc:213`) or a dedicated section;
      RegExp is a core language built-in and TS-36 does not delegate it
      elsewhere. (Scope call: flagged for user confirmation — TS-36 does not
      currently treat RegExp explicitly.)

- [ ] https://mythbusters.js.org/regexp/global-flag.md#global-flag-g — the
      `lastIndex` statefulness gotcha: repeated `RegExp.prototype.test()`
      calls on the same regex carrying the `g` flag advance `lastIndex` and
      produce inconsistent results until a failed match resets it. This is a
      well-known bug source and is not addressed in TS-36. Recommend placing
      alongside the RegExp method guidance above (new "RegExp" section).

- [ ] https://mythbusters.js.org/regexp/unicode-flag.md#unicode-flag-u — the
      rule that the `u` (unicode) flag is mandatory when matching Unicode
      strings, especially astral-plane characters (emoji, surrogate pairs) —
      without it `/^.$/` fails to match a single astral character. Not
      addressed in TS-36. Recommend placing in the new "RegExp" section.

- [ ] https://mythbusters.js.org/regexp/dot-all-flag.md#dot-all-flag-s — the
      `s` (dotAll) flag makes `.` match line terminators, replacing the
      `[\s\S]`/`[^]` workarounds needed for multi-line matching (e.g. across
      template-literal line breaks). Not addressed in TS-36. Recommend
      placing in the new "RegExp" section.

- [x] https://ricostacruz.com/rsjs/#no-inline-scripts — the rule that
      imperative JavaScript MUST NOT be inlined in HTML (`<script>...</script>`
      blocks, `onclick=` handlers) is not addressed anywhere in TS-36. TS-36
      has no HTML-authoring guidance at all. Recommend placing in a new
      "Front-end conventions" section, or deferring to TS-37 (Web Platform
      APIs). Classified missing rather than out-of-scope because TS-36's
      "Modules" section (`src/036/05-modules.adoc`) implicitly assumes all JS
      lives in `.js` files but never states the prohibition on inline scripts
      that makes that assumption load-bearing for web targets.
      **Addressed:** added a "No inline scripts" subsection under "Module
      systems for the web" in `src/036/05-modules.adoc`.

- [x] https://ricostacruz.com/rsjs/#bootstrap-data-with-meta-tags — the rule
      that data for scripts SHOULD be passed via `data-*` attributes or
      `<meta>` tags rather than inline `<script>` assignments to globals
      (e.g. `window.UserData = {...}`) is not addressed in TS-36. The
      "Modules" section (`src/036/05-modules.adoc`) and "Variable
      declarations" (`src/036/01-language-fundamentals.adoc`, "Avoid global
      variables") forbid global state in general but give no front-end
      mechanism for getting server-side data into client code. Recommend a
      new subsection under "Modules" or "Runtimes" covering data hand-off
      from server-rendered HTML.
      **Addressed:** added a "Passing server data to client scripts"
      subsection under "Module systems for the web" in
      `src/036/05-modules.adoc`, covering both `data-*` attributes and
      `<meta>` tags.

- [ ] https://bitsofco.de/what-is-tree-shaking/#what-about-side-effects —
      the concept of a *side effect* in the tree-shaking sense (code that
      performs an action when imported, not related to any export, e.g. a
      polyfill) is not addressed in TS-36. The "Transpilation and bundling"
      section (`src/036/06-packages-and-tooling.adoc:853`) discusses tree
      shaking only as "eliminating unused exports" without mentioning side
      effects as the exception that prevents automatic elimination.
      Recommend a new paragraph under "Transpilation and bundling"
      defining side effects and explaining why they defeat tree shaking.

- [ ] https://bitsofco.de/what-is-tree-shaking/#what-about-side-effects —
      the rule that tree shaking cannot automatically detect side effects,
      so they MUST be specified manually, is not addressed in TS-36.
      Recommend placing alongside the side-effect definition above, in the
      "Transpilation and bundling" section
      (`src/036/06-packages-and-tooling.adoc:853`).

- [ ] https://bitsofco.de/what-is-tree-shaking/#how-to-tree-shake — the
      `sideEffects` field in `package.json` (an array of files to exclude
      from tree shaking, or `false` to declare the package side-effect-free)
      is not covered in TS-36's package-manifest section. The manifest
      template at `src/036/06-packages-and-tooling.adoc:54` and the field
      subsections that follow omit it entirely. Recommend a new
      `=== sideEffects` subsection under "Package manifests"
      (`src/036/06-packages-and-tooling.adoc:36`) and an entry in the
      template.

- [ ] https://bitsofco.de/what-is-tree-shaking/#what-does-tree-shaking-shake-off —
      the caveat that tree shaking does *not* eliminate all unused code
      (it is best-effort and leaves some dead code behind) is not stated in
      TS-36. The "Transpilation and bundling" section
      (`src/036/06-packages-and-tooling.adoc:870`) presents tree shaking as
      eliminating unused exports without noting its limits. Recommend a
      sentence under "Transpilation and bundling" noting that tree shaking
      is best-effort and does not remove every unused reference.

## Partial

- [ ] https://mythbusters.js.org/number/parse-string.md#parsing-string — the
      handbook gives string-to-number conversion guidance that TS-36's
      coercion rules (`src/036/01-language-fundamentals.adoc:167`, "use
      `Number()`, `String()`, `Boolean()` without `new`"; "shorthand
      coercions `+val`, `!!val` work but are less clear") only touches in
      passing. What the reference adds: `parseInt`/`parseInt(_, 10)` stops at
      the first non-numeric character (truncated integer), `parseFloat`
      handles fractions but also stops, `Number()`/`+`/`*1`/`-0` return `NaN`
      for inputs with leading non-numeric characters, and `~~` coerces to a
      32-bit integer (discouraged — changes meaning above 2^31-1). Recommend
      a clause in "Types and coercion" (`src/036/01-language-fundamentals.adoc:144`)
      on choosing between `parseInt`/`parseFloat`/`Number()`.

- [ ] https://mythbusters.js.org/workflow/how-to-clone.md#dont-clone-serializing —
      the handbook warns that `JSON.parse(JSON.stringify(value))` cloning is
      lossy (drops function members, omits `undefined` object keys, turns
      array `undefined` entries into `null`, converts `Date` to ISO-8601
      strings) and throws on circular references. TS-36's FP/Immutability rule
      (`src/036/AGENTS.md:655`) notes that shallow copies are insufficient for
      nested structures and recommends a dedicated library (Immer,
      Immutable.js) for deep copies, but does not call out the JSON-clone
      anti-pattern. Recommend a sentence in the Immutability rule
      (`src/036/10-functional-programming.adoc`, FP section) warning against
      `JSON.parse(JSON.stringify())` for deep cloning.

- [ ] https://mythbusters.js.org/object/weak-map.md#when-to-use-weakmap-over-map —
      the handbook recommends `WeakMap` for associating private
      metadata/state with objects you do not control (e.g. DOM nodes,
      third-party objects) so the key can be garbage-collected, and notes
      native private class fields (`#`) are preferred for objects you own.
      TS-36 covers private `#` fields (`src/036/AGENTS.md:240`, "Prefer
      ECMAScript `#` private fields over TypeScript's `private` modifier")
      but does not mention `WeakMap`/`Map` as the private-state tool for
      foreign objects, nor the memory-leak avoidance rationale. Recommend a
      clause in "Objects and classes" (`src/036/04-objects-and-classes.adoc`)
      on `WeakMap` for external-object private state.

- [x] https://ricostacruz.com/rsjs/#separate-your-vendor-libs — RSJS
      recommends splitting third-party libraries into a separate `vendor.js`
      bundle so browsers cache it independently and app deploys don't
      invalidate it. TS-36's "Transpilation and bundling" rule
      (`src/036/06-packages-and-tooling.adoc`) covers transpilation strategy,
      native ESM preference, and lazy-loading via dynamic `import()` plus
      code-splitting, but does not address first-party vs. vendor bundle
      separation for cache stability. What the reference adds: a concrete
      cache-invalidation argument for keeping vendor code in its own bundle,
      and the related recommendation to split bundles when an app needs
      multiple entry points (e.g. public pages vs. private dashboards).
      **Addressed:** added a paragraph on first-party/vendor bundle
      separation to the "Transpilation and bundling" section of
      `src/036/06-packages-and-tooling.adoc`.

- [x] https://ricostacruz.com/rsjs/#keep-the-global-namespace-clean — RSJS
      prescribes a single `App` namespace object for publicly-accessible
      functions/classes, and a separate `Helpers` namespace for cross-behavior
      utilities (`src/036/01-language-fundamentals.adoc`, "Avoid global
      variables"). TS-36 covers the underlying concern — "Encapsulate state
      in modules, functions, and objects"; "Use `globalThis`"; "Avoid global
      variables" — and mandates ES modules, which supersedes the `App`/
      `Helpers` namespace pattern. What TS-36 omits: any guidance for the
      legacy/non-module case where globals are unavoidable (e.g. integrating
      with a host page that is not an ES module). This is partial rather than
      missing because TS-36's ES-modules-only stance is the more correct
      answer; the gap is only the absence of a fallback note.
      **Addressed:** added a legacy-integration fallback paragraph (single
      `globalThis.App` namespace object) to the "Scope and `this`" section of
      `src/036/02-syntax-and-style.adoc`.

- [ ] https://mythbusters.js.org/function/new.md#new-agnostic — the
      handbook describes making a constructor return an instance even when
      called without `new` (the "new-agnostic" pattern:
      `if (!(this instanceof User)) return new User(...)`). TS-36 mandates
      `class` over constructor functions (`src/036/AGENTS.md:308`) and permits
      function-declaration constructors only in a narrow case
      (`src/036/AGENTS.md:266`), but never states the relevant consequence: an
      ES2015 `class` constructor *throws* `TypeError` when invoked without
      `new`, so the missing-`new` footgun (silent `undefined` return; `this`
      leaking to the global object) that motivated the new-agnostic pattern is
      already eliminated by `class` — this is now language-enforced fail-fast,
      not a style-guide concern. What TS-36 omits: (a) an explicit note that
      `class` enforces `new` as a rationale for preferring it over constructor
      functions, and (b) for the permitted constructor-function case, any
      warning about the missing-`new` footgun. Recommend a clause in "Objects
      and classes" (`src/036/04-objects-and-classes.adoc`) noting that `class`
      enforces `new` (throws without it), and that constructor functions —
      where still used — MUST be called with `new`; the legacy new-agnostic
      guard is NOT recommended for new code.

- [ ] https://bitsofco.de/what-is-tree-shaking/#how-does-tree-shaking-work —
      the article explains *why* tree shaking requires ES modules by
      contrasting static `import` with dynamic CommonJS `require()`
      (conditional `require()` makes it impossible to determine which
      modules are needed before runtime). TS-36 states the requirement
      ("tree shaking … which requires ES modules",
      `src/036/06-packages-and-tooling.adoc:870`; "Static `import`
      declarations are evaluated at compile time, which enables static
      analysis, bundling, and tree shaking",
      `src/036/05-modules.adoc:618`) but never gives the dynamic-CJS contrast
      that makes the requirement load-bearing. What the reference adds: a
      concrete example of conditional `require()` defeating static analysis.
      Recommend a sentence in "Dynamic imports and code splitting"
      (`src/036/05-modules.adoc:616`) or "Transpilation and bundling"
      explaining why CommonJS cannot be tree-shaken.

- [ ] https://bitsofco.de/what-is-tree-shaking/#what-does-tree-shaking-shake-off —
      the article gives concrete examples of what tree shaking eliminates:
      named imports that are imported but never used (e.g.
      `import { add, multiply }` where only `add` is called → `multiply`
      dropped), and unused *properties* of imported objects (e.g. only the
      `name` property of an imported `myInfo` object is accessed → the
      `birthday` property is dropped). TS-36 says only "eliminating unused
      exports" (`src/036/06-packages-and-tooling.adoc:870`) and that named
      exports enable tree shaking (`src/036/05-modules.adoc:273`). What the
      reference adds: illustration that shaking operates at the granularity
      of individual named bindings and even object properties, not just
      whole modules. Recommend a clause in "Transpilation and bundling"
      (`src/036/06-packages-and-tooling.adoc:870`) stating the granularity.

- [ ] https://bitsofco.de/what-is-tree-shaking/#how-to-tree-shake — the
      article gives the concrete activation step for webpack: set
      `mode: "production"` in `webpack.config.js`. TS-36 names webpack as a
      bundler that enables tree shaking
      (`src/036/06-packages-and-tooling.adoc:869`) but gives no activation
      guidance. What the reference adds: the specific `mode: "production"`
      config. Partial rather than missing because TS-36 deliberately stays
      out of per-bundler config tutorials; flagged in case the maintainers
      want a one-line pointer. Recommend, if added, a brief note in
      "Transpilation and bundling" (`src/036/06-packages-and-tooling.adoc:853`).

## Out-of-scope

The 15 web-client/DOM out-of-scope items from the initial run (component
behaviors, `data-js-*` selectors, document-ready, event delegation, dynamic
content init, jQuery patterns, `onmount`, third-party-as-behavior, async
third-party loading, and the Rails/Browserify/Webpack/Brunch loading recipes)
were relocated on 2026-08-05 to `src/018/GAPS.md` (TS-18: Web GUIs) at the
maintainer's direction — web-client JS structure belongs in TS-18 rather than
TS-37. They have been re-classified against TS-18's scope there (10 missing,
4 out-of-scope; event delegation was already tracked in TS-18 from its
`web-clients` reference). See `src/018/GAPS.md` for the current entries.

- [ ] https://www.sitepoint.com/premium/books/javascript-best-practice/read/1/#build-systems-task-runners —
      the chapter recommends build systems / task runners (Grunt.js, Gulp.js)
      for orchestrating lint, transpile, bundle, and minify steps. TS-36's
      "Packages and tooling" section covers transpilation and bundling
      (`src/036/06-packages-and-tooling.adoc:853`) and the `scripts` manifest
      field (`src/036/06-packages-and-tooling.adoc:174`), but does not mention
      Grunt/Gulp or general-purpose task runners. Flagged out-of-scope because
      TS-36's tooling scope is language-level (package manifests,
      transpilation, bundling) not general build orchestration, and these
      runners are largely superseded by npm scripts. Plausible home if kept:
      "Transpilation and bundling" (`src/036/06-packages-and-tooling.adoc:853`).

- [ ] https://www.sitepoint.com/premium/books/javascript-best-practice/read/1/#application-architecture —
      the chapter describes Single Page Application (SPA) architecture
      (client-side UI rendering, remote API via Ajax) as the dominant web app
      architecture. TS-36's "Architecture and design" section
      (`src/036/12-architecture-and-design.adoc`) covers DDD layers and API
      design, not web application delivery architecture. Flagged out-of-scope
      — SPA architecture belongs in TS-18 (Web GUIs) or TS-37 (Web Platform
      APIs), which TS-36 explicitly delegates browser/web-app concerns to.

- [ ] https://www.sitepoint.com/premium/books/javascript-best-practice/read/1/#application-architecture —
      the chapter describes Universal / Isomorphic JavaScript applications
      (code executed on both server and client, server-rendered initial load
      for performance and SEO). TS-36 does not address isomorphic rendering.
      Flagged out-of-scope — this is web application architecture, not language
      convention; belongs in TS-18 or TS-37.

- [ ] https://www.sitepoint.com/premium/books/javascript-best-practice/read/1/#deployment —
      the chapter describes a deployment workflow: build to a `dist` directory,
      upload only built artifacts, and use CI servers (Jenkins, Travis CI,
      CircleCI) to build automatically after each commit and keep build
      artifacts out of version control. TS-36 notes `dist` as build output
      excluded from source control in its repository-structure guidance
      (`src/036/AGENTS.md:460`), so the "artifacts out of VCS" point is
      partially covered. The CI-server and deployment-workflow guidance is not
      covered. Flagged out-of-scope — deployment and CI are beyond a language
      coding standard; deployment is covered by a separate TS in this
      repository.

- [ ] https://www.sitepoint.com/premium/books/javascript-best-practice/read/1/#conclusion —
      the chapter closes with the KISS principle ("use only what you think you
      need and not everything you have available"). TS-36's "Architecture and
      design" section (`src/036/12-architecture-and-design.adoc`) covers DDD
      and API design but does not name KISS. Flagged out-of-scope — KISS is a
      generic software-design principle, not an ECMAScript convention; it
      plausibly belongs in a general design TS rather than TS-36.

- [ ] https://mythbusters.js.org/v8-tips/* (Float Number, Freeing memory,
      Hidden classes, Inline initialization, Monomorphic, Properties names,
      Sparse arrays, Use strict) — V8 engine internals and micro-optimization
      (value tagging, hidden-class transitions, monomorphism, array storage
      strategies, `delete` performance, property-name coercion trivia).
      Flagged out-of-scope: TS-36's stated purpose is language *coding
      conventions*, and its QA section explicitly says "Don't over-optimize
      early. Optimize only once a program is provably too slow, and only the
      slow parts." Engine-specific optimization belongs in a dedicated
      performance standard, not TS-36. (`use strict` itself is covered by
      TS-36 at `src/036/AGENTS.md:125`; only the performance angle is
      out-of-scope.)

- [ ] https://mythbusters.js.org/array/pop-or-shift.md,
      array/preallocation.md, function/bind.md, workflow/spread-syntax.md,
      workflow/variable-access.md, workflow/lookup-table.md, workflow/math.md,
      workflow/memoization.md — performance micro-optimizations (`.pop` vs
      `.shift`, array preallocation/reuse, `.bind` vs `.call` vs `self = this`,
      avoiding spread-in-`reduce`, caching property/`length` lookups, loop
      reversal, lookup tables vs `if`/`else`, precalculated `Math` constants,
      memoization). Flagged out-of-scope per TS-36's "don't over-optimize
      early" stance; several also overlap TS-36's existing guidance (e.g.
      `const`/`let`/`Object.freeze` in scope.md, pure functions in
      passing-by-value.md) which TS-36 already covers.

- [ ] https://mythbusters.js.org/workflow/defer.md — timer functions
      (`setTimeout`, `setImmediate`, `process.nextTick`, `Promise#then`) for
      deferring by a tick. Flagged out-of-scope: Node-specific scheduling
      belongs in TS-38 (Node.js Applications), and the angle is performance.

- [ ] https://mythbusters.js.org/date/timestamp.md — `Date.now()` vs
      `new Date().getTime()` allocation, monotonic clocks
      (`performance.now()`, `process.hrtime`), system-clock drift for elapsed
      time. Flagged out-of-scope: date/time handling is delegated to TS-47
      (Dates and Times); the `performance.now()`/`hrtime` angle is performance
      measurement.

- [ ] https://mythbusters.js.org/array/arguments.md,
      object/empty-prototype.md, workflow/null-or-undefined.md —
      partly-covered or legacy usage notes: `arguments` optimization
      (superseded by TS-36's rest-parameter/Spread guidance),
      `Object.create(null)` for dictionary objects (niche/perf), and
      `null`-vs-`undefined` / `value == null` (TS-36 mandates `===` and covers
      nullish coalescing, so the `== null` advice is contradicted rather than
      missing). Flagged out-of-scope.

## Unresolved

- https://www.sitepoint.com/premium/books/javascript-best-practice/read/2/
  through `/read/8/` (chapters 2–8: "Clean Code with ES6 Default Parameters &
  Property Shorthands", "JavaScript Performance Optimization Tips",
  "JavaScript Design Patterns: The Singleton", "JavaScript Object Creation",
  "Best Practices for Using Modern JavaScript Syntax", "Flow Control in Modern
  JS", "JavaScript's New Private Class Fields") could not be retrieved — the
  pages are paywalled (SitePoint Premium; only the table of contents and
  chapter 1's body are publicly visible). Not included in the comparison
  above. If a subscriber can supply the text, re-run the analysis to extend
  coverage.

- https://bitsofco.de/what-is-tree-shaking/, https://ricostacruz.com/rsjs/,
  and https://mythbusters.js.org/ (all ~30 tip pages via the docsify markdown
  source) were fetched successfully in full.