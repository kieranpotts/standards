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
- https://zellwk.com/blog/ignoring-files-from-npm-package/ (Liew — "How to
  ignore files from your npm package")
- https://jdxcode.medium.com/for-the-love-of-god-dont-use-npmignore-f93c08909d8d
  (Jeff D. — "For the love of god, don't use .npmignore")
- https://web.archive.org/web/20260305114536/https://2ality.com/2021/06/typescript-esm-nodejs.html
  (Rauschmayer, 2ality — "TypeScript and native ESM on Node.js"; archived copy)
- https://medium.com/cameron-nokes/the-30-second-guide-to-publishing-a-typescript-package-to-npm-89d93ff7bccd
  (Nokes — "The 30-second guide to publishing a TypeScript package to NPM")
- https://dev.to/yugjadvani/how-to-write-better-typescript-code-best-practices-for-clean-effective-and-scalable-code-38d2
  (Jadvani — "How to Write Better TypeScript Code")
- https://github.com/airbnb/javascript (Airbnb — *Airbnb JavaScript Style Guide*; the
  main guide only — the React and CSS-in-JavaScript companion guides are
  out-of-scope for TS-36)
- https://deno.com/blog/document-javascript-package (Deno — "How to document
  your JavaScript package", a JSDoc best-practices guide for package authors)
- https://github.com/nodeshift/nodejs-reference-architecture/blob/main/docs/functional-components/webframework.md
  (nodeshift — Node.js reference architecture, "Web Framework" page)
- https://www.linkedin.com/posts/progressivethinker_javascript-frontend-technology-activity-7274626911429967872-3_2G/
  (Ahuja — "JavaScript Array Methods" cheatsheet)

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

**Assessment (zellwk.com — "How to ignore files from your npm package").** A
short beginner-level explainer of the three mechanisms npm uses to decide
which files go into a published package: `.gitignore`, `.npmignore`, and the
`files` manifest field. It is squarely within TS-36's stated scope — the
standard has a `files` subsection (`src/036/06-packages-and-tooling.adoc:130`)
and a "Distributing packages" section (`src/036/06-packages-and-tooling.adoc:465`)
that covers `npm pack` verification. TS-36 covers the `files` whitelist concept
and `npm pack` verification, but omits `.gitignore` and `.npmignore` as npm
mechanisms entirely, the critical interaction between them (`.npmignore`
overrides `.gitignore`), the always-included file set, and the recommendation
to pick one method deliberately.

**Assessment (jdxcode — "For the love of god, don't use .npmignore").** An
argument from a maintainer who accidentally leaked AWS credentials by adding
a `.npmignore` that silently disabled npm's `.gitignore` consultation. It is
within TS-36's scope (package manifests, distributing packages). The article
overlaps the zellwk piece on the three mechanisms but adds the security
rationale for preferring `files` whitelisting, the `/`-anchoring convention for
`files` entries, the one valid `.npmignore` use case (excluding a subdir from a
whitelisted dir), the tar-inspection one-liner, and the npm@6 packed-file
display behavior. The tooling feature requests at the end (npm/yarn should
warn or fail; `npm init` should default to `files`) are out-of-scope.

**Assessment (2ality — "TypeScript and native ESM on Node.js").** A practical
guide to producing TypeScript packages that emit native ESM for Node.js. It is
within TS-36's scope (TypeScript, modules, package exports) but sits at the
intersection the standard handles least thoroughly: TypeScript *compiler
configuration*. TS-36 has a TypeScript section (`src/036/08-typescript.adoc`)
covering type safety, operators, undefined handling, declaration files, and
decorators, but no `tsconfig.json` guidance at all — no mention of `module`,
`moduleResolution`, `target`, `lib`, `strict`, `allowSyntheticDefaultImports`/
`esModuleInterop`, or `NodeNext`. The standard covers package `exports`
(`src/036/06-packages-and-tooling.adoc:232`), conditional exports, `"type":
"module"`, and file extensions in relative imports, so the article's package-
exports and extension material is largely already covered. The gaps are
concentrated in TypeScript-specific ESM configuration (`tsconfig` settings,
`typesVersions`, CJS-default-import compiler options) and two narrow package-
exports details (`null` exclusion, the within-package-vs-cross-package extension
convention). The VS Code settings and regex workflow tips are out-of-scope.

**Assessment (Nokes — "The 30-second guide to publishing a TypeScript package
to NPM").** A short 2018 walkthrough of the mechanics of publishing a
TypeScript package: emitting `.d.ts` files, pointing consumers at them via the
`types` manifest field, keeping compiled output out of Git, automating the
build with a `prepublish` script, and verifying locally with `npm link`. It is
within TS-36's scope (TypeScript declaration files, package manifests,
distributing packages). TS-36 covers declaration-file generation conceptually
(`src/036/08-typescript.adoc:263`), the `dist`-excluded-from-VCS convention
(`src/036/06-packages-and-tooling.adoc:602`), and `npm pack`-based local
verification (`src/036/06-packages-and-tooling.adoc:472`), so those points are
not findings. The gaps are the `types` manifest field (not in TS-36's manifest
field list), the `declaration` compiler option (overlaps the existing 2ality
tsconfig gap), the rule that public-facing types must be exported, the
`prepublish`/`prepare` lifecycle hook, and `npm link` as a verification
alternative. The `npm init`/`tsc --init` scaffolding tips are out-of-scope.

**Assessment (dev.to — Jadvani, "How to Write Better TypeScript Code").** A
beginner-level list of 10 TypeScript tips (strict tsconfig options, interface
vs type, unknown over any, readonly, utility types, explicit return types,
null/undefined handling, enums, never for exhaustive checks, pure functions).
It is within TS-36's scope (TypeScript) but narrower than TS-36's TypeScript
section where they overlap (non-null assertions, possibly-undefined handling,
declaration files, decorators — TS-36 covers each more deeply). TS-36's
null/undefined and pure-function tips are already covered. The gaps are the
TypeScript features TS-36 does not address at all: the `interface` vs `type`
distinction, the `readonly` modifier, built-in utility types (`Partial`/`Pick`/
`Omit`), enums (and the `as const` alternative the comments recommend), and
`never` for exhaustive checks. The strict-tsconfig-options tip overlaps the
existing 2ality `tsconfig` gap. The explicit-return-types tip is recorded but
noted as contested — the article's own commenters disagree.

**Assessment (Airbnb JavaScript Style Guide).** A comprehensive, widely-cited
JS coding-conventions guide covering types, references, objects, arrays,
destructuring, strings, functions, arrow functions, classes, modules,
iterators/generators, properties, variables, hoisting, equality, blocks,
control statements, comments, whitespace, commas, semicolons, coercion,
naming, accessors, events, jQuery, ES6+ styles, standard library, testing, and
performance. It is the same scope as TS-36, and the great majority of its rules
are already covered by TS-36 (often with TS-36 taking the more modern position).
Three deliberate conflicts are NOT recorded as gaps — they are disagreements,
not omissions: Airbnb says omit filename extensions in imports (10.10) while
TS-36 requires them; Airbnb says prefer default exports (10.6) while TS-36 calls
default exports bad practice; Airbnb uses camelCase for variables while TS-36
mandates `lower_case` (snake_case). The genuine gaps are the distinctive Airbnb
rules TS-36 does not address: `Number.isNaN`/`Number.isFinite` over their global
counterparts (standard library), the rule against TC39 proposals below stage 3,
the rule against `++`/`--`, acronym/initialism casing in identifiers, generator
guidance, mutable-export bindings, and the accessor pattern (prefer
`getVal()`/`setVal()` functions over getter/setter syntax). The jQuery and
Events sections are out-of-scope (DOM/jQuery, delegated to TS-37), and the
Performance section is out-of-scope (engine micro-optimization).

**Assessment (deno.com — "How to document your JavaScript package").** A JSDoc
best-practices guide for package authors (summaries, type info, tags, examples,
what to document, markdown, internal linking, keeping docs current, auditing).
It is squarely within TS-36's JSDoc/TSDoc scope, and TS-36's JSDoc section is in
many ways more prescriptive (a fuller tag list, type syntax, function/class
rules, file-level docblocks, release-stage tags, VS Code integration). The gaps
are refinements TS-36 omits: the `@module` tag for multi-module packages (not in
TS-36's tag list), `@linkcode`/`@linkplain` inline link tags, the
first-paragraph-as-summary emphasis for IDE tooltips, the requirement to
document each property/method of interfaces and classes, markdown features
beyond TS-36's narrow permitted list (headings, lists, blockquotes,
`[!IMPORTANT]`), and the `@example` title/description convention. The
Deno-specific audit tooling (`deno doc --lint`, `deno test --doc`) and the
docs-driven-development process recommendation are out-of-scope (runtime-specific
tooling and workflow, not coding conventions).

**Assessment (nodeshift nodejs-reference-architecture — "Web Framework").** A
Node.js reference-architecture page recommending Express 4.x with `~4.x.y`
version pinning, separate business/admin ports, liveness/readiness endpoints,
global middleware before routes, Helmet, `--max-http-header-size`, and a
`"test"` npm script. It is entirely application-level Node.js architecture, which
TS-36 explicitly delegates to TS-38 (Node.js Applications) — see
`src/036/AGENTS.md:696`. The `"test"` npm script convention is already covered
by TS-36's manifest templates (`src/036/06-packages-and-tooling.adoc:683`,
`:757`, `:786`). Every other item is out-of-scope for TS-36.

**Assessment (LinkedIn — Ahuja, "JavaScript Array Methods").** A beginner
cheatsheet of seven array methods (`map`, `filter`, `find`, `findIndex`,
`fill`, `some`, `every`). It is narrower than TS-36 in every area it touches —
TS-36's functional-programming section covers array iteration methods and
immutability more deeply. Per the "reference narrower than the standard" edge
case, no gaps.

**Status:** Re-run, 2026-08-05 (updated with five additional reference
resources from GitHub issue #54).
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
  - zellwk.com / jdxcode npm-package-contents: first run against these
    references. 5 missing and 4 partial gaps identified below; all open.
    2 out-of-scope items (tooling feature requests) grouped under
    Out-of-scope.
  - 2ality TypeScript-ESM-Node.js: first run against this reference. 4 missing
    and 2 partial gaps identified below; all open. 2 out-of-scope items (IDE
    config, editor workflow) grouped under Out-of-scope.
  - Nokes publishing-a-TypeScript-package: first run against this reference.
    3 missing and 2 partial gaps identified below; all open. 1 out-of-scope
    item (scaffolding commands) grouped under Out-of-scope.
  - rsjs: re-verified — all 4 in-scope gaps (2 missing, 2 partial) remain
    addressed (confirmed present in the standard: "No inline scripts" and
    "Passing server data to client scripts" in `src/036/05-modules.adoc:552`,
    `:565`; vendor-bundle separation in `src/036/06-packages-and-tooling.adoc:879`;
    `globalThis.App` legacy namespace in `src/036/02-syntax-and-style.adoc:148`).
  - dev.to Jadvani TypeScript tips: first run against this reference. 6 missing
    and 2 partial gaps identified below; all open. The strict-options tip
    overlaps the existing 2ality `tsconfig` gap.
  - Airbnb JavaScript Style Guide: first run against this reference. 6 missing
    and 1 partial gaps identified below; all open. 3 conflicts with TS-36 noted
    in the assessment (not recorded as gaps). jQuery, Events, and Performance
    sections out-of-scope.
  - deno.com JSDoc guide: first run against this reference. 1 missing and 5
    partial gaps identified below; all open. 2 out-of-scope items (Deno tooling,
    docs-driven-dev process) grouped under Out-of-scope.
  - nodeshift webframework: first run against this reference. 0 missing, 0
    partial; all items out-of-scope (Node.js app architecture, delegated to
    TS-38); the `"test"` script convention is already covered by TS-36.
  - LinkedIn array-methods cheatsheet: first run. 0 gaps (reference narrower
    than the standard).
  - The standard's `.adoc` files were not modified between the prior run and
    this one, so all previously-open gaps remain open unchanged.

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

- [ ] https://zellwk.com/blog/ignoring-files-from-npm-package/#excluding-files-with-gitignore,
      https://jdxcode.medium.com/for-the-love-of-god-dont-use-npmignore-f93c08909d8d#meanwhile
      — npm consults the repository's `.gitignore` to decide which files to
      exclude from a published package when no `.npmignore` is present.
      TS-36 mentions `.gitignore` only as a file that exists in the repository
      tree (`src/036/06-packages-and-tooling.adoc:594`); it never states that
      npm uses it as the default package-contents filter. Recommend a note in
      the `=== files` subsection (`src/036/06-packages-and-tooling.adoc:130`)
      or a new subsection under "Distributing packages"
      (`src/036/06-packages-and-tooling.adoc:465`) explaining npm's three
      mechanisms and their precedence.

- [ ] https://zellwk.com/blog/ignoring-files-from-npm-package/#blacklisting-files-with-npmignore,
      https://jdxcode.medium.com/for-the-love-of-god-dont-use-npmignore-f93c08909d8d#the-hidden-gotcha
      — `.npmignore` as a package-contents blacklist, and the critical gotcha
      that creating a `.npmignore` causes npm to consult it *instead of*
      `.gitignore` (not in addition to it). TS-36 does not mention `.npmignore`
      at all. Recommend placing in the `=== files` subsection
      (`src/036/06-packages-and-tooling.adoc:130`) or a new subsection under
      "Distributing packages" (`src/036/06-packages-and-tooling.adoc:465`).

- [ ] https://jdxcode.medium.com/for-the-love-of-god-dont-use-npmignore-f93c08909d8d#the-hidden-gotcha
      — the security hazard: because `.npmignore` overrides `.gitignore`, any
      gitignored dotfile (e.g. `.envrc` with credentials, `.nyc_output`) is
      silently included in the published package unless manually re-listed in
      `.npmignore`. TS-36's `files` subsection says the field should be used
      "to avoid leaking development-only files"
      (`src/036/06-packages-and-tooling.adoc:133`) but never explains the
      `.npmignore`-overrides-`.gitignore` failure mode that makes blacklisting
      dangerous. Recommend a clause in the `=== files` subsection or
      "Distributing packages" warning that `.npmignore` disables npm's
      `.gitignore` consultation and can leak secrets.

- [ ] https://zellwk.com/blog/ignoring-files-from-npm-package/#whitelisting-files-with-the-files-property,
      https://jdxcode.medium.com/for-the-love-of-god-dont-use-npmignore-f93c08909d8d#whitelisting
      — the set of files npm always includes regardless of the `files` field
      (`package.json`, `README`/`README.md`, `LICENSE`/`LICENCE`, and the
      `main`/`bin`/`exports` targets) so authors need not list them. TS-36's
      `files` subsection (`src/036/06-packages-and-tooling.adoc:130`) and
      manifest template (`src/036/06-packages-and-tooling.adoc:77`) do not
      state which files are always included. Recommend a sentence in the
      `=== files` subsection listing the always-included set.

- [ ] https://jdxcode.medium.com/for-the-love-of-god-dont-use-npmignore-f93c08909d8d#the-one-time-npmignore-is-ok
      — the one valid use of `.npmignore`: combined with `files` to exclude a
      subdirectory from an otherwise-whitelisted directory (e.g. `files:`
      `["/lib"]` plus `.npmignore` entry `__test__` so `/lib/__test__` is
      excluded while `/lib/index.js` is included). TS-36 does not mention
      `.npmignore` at all. Recommend a note in the `=== files` subsection
      (`src/036/06-packages-and-tooling.adoc:130`) describing this as the only
      case where `.npmignore` is acceptable.

- [ ] https://web.archive.org/web/20260305114536/https://2ality.com/2021/06/typescript-esm-nodejs.html#the-basics
      — `tsconfig.json` configuration for emitting native ESM on Node.js: the
      `module` (`"ES2020"`/`"NodeNext"`), `moduleResolution`
      (`"Node"`/`"NodeNext"`), `target`, `lib`, `strict`, `declaration`, and
      `rootDir`/`outDir` settings. TS-36 has no `tsconfig.json` guidance at all
      — none of these compiler options are mentioned anywhere in the standard.
      Recommend a new "TypeScript compiler configuration" subsection under
      "TypeScript" (`src/036/08-typescript.adoc`). (Scope call: flagged for
      user confirmation — TS-36's TypeScript section covers language usage but
      not compiler configuration; the standard may intend to delegate tsconfig
      guidance to TS-38 or a dedicated tooling TS.)

- [ ] https://web.archive.org/web/20260305114536/https://2ality.com/2021/06/typescript-esm-nodejs.html#typescript-47-better-support-package-exports-and-nodes-esm
      — the `typesVersions` field in `package.json`: the pre-TypeScript-4.7
      workaround that maps TypeScript type-definition paths to match a
      package's `exports` map, and the fact that TypeScript 4.7+ understands
      `exports` natively so `typesVersions` is no longer needed. TS-36 does not
      mention `typesVersions` anywhere, and its package-manifest field
      subsections (`src/036/06-packages-and-tooling.adoc:108` onward) omit it.
      Recommend a `=== typesVersions` subsection under "Package manifests"
      (`src/036/06-packages-and-tooling.adoc:36`) noting it as a legacy
      workaround for TypeScript < 4.7.

- [ ] https://web.archive.org/web/20260305114536/https://2ality.com/2021/06/typescript-esm-nodejs.html#the-basics
      — the `allowSyntheticDefaultImports` (and related `esModuleInterop`)
      TypeScript compiler option, needed to import legacy CommonJS modules
      using default-import syntax where `module.exports` is the default
      export. TS-36 covers the *runtime* CJS-into-ESM import pattern
      (`src/036/05-modules.adoc:447`, "import the whole module using the
      default import syntax") but never mentions the TypeScript compiler
      option that enables this syntax. Recommend a clause in the "Importing
      CJS into ESM" subsection (`src/036/05-modules.adoc:447`) or the new
      TypeScript-compiler-configuration subsection noting
      `allowSyntheticDefaultImports`/`esModuleInterop`.

- [ ] https://web.archive.org/web/20260305114536/https://2ality.com/2021/06/typescript-esm-nodejs.html#exposing-a-subtree-while-hiding-parts-of-it
      — the `null` value in a package `exports` map to exclude/hide a
      subpath from an otherwise-exposed pattern (e.g.
      `"./internal/*": null` prevents deep imports into `./dist/src/internal/`
      while `"./*": "./dist/src/*"` exposes everything else). TS-36's
      `exports` section (`src/036/06-packages-and-tooling.adoc:232`) covers
      patterns and encapsulation but never mentions the `null` exclusion
      mechanism. Recommend a clause in the `=== exports` subsection
      (`src/036/06-packages-and-tooling.adoc:232`) noting that mapping a
      subpath to `null` hides it.

- [ ] https://medium.com/cameron-nokes/the-30-second-guide-to-publishing-a-typescript-package-to-npm-89d93ff7bccd#2-add-types-index-d-ts-to-your-package-json
      — the `types` field in `package.json` (e.g. `"types":
      "dist/index.d.ts"`), which tells the TypeScript compiler where to find a
      package's type definitions, typically matching the `main` entry point's
      `.d.ts` counterpart. TS-36's package-manifest field subsections
      (`src/036/06-packages-and-tooling.adoc:108` onward) omit the `types`
      field entirely, and the manifest template
      (`src/036/06-packages-and-tooling.adoc:54`) does not include it.
      Recommend a `=== types` subsection under "Package manifests"
      (`src/036/06-packages-and-tooling.adoc:36`) and an entry in the
      template. (Where `exports` is used with TypeScript, `typesVersions` or
      per-condition `types` keys may also apply — see the existing
      `typesVersions` gap above.)

- [ ] https://medium.com/cameron-nokes/the-30-second-guide-to-publishing-a-typescript-package-to-npm-89d93ff7bccd#1-add-declaration-true-to-your-tsconfigjson
      — the rule that when `declaration: true` is set, any type that is part
      of a public-facing API (and is not an inline type) MUST be `export`-ed,
      or the compiler will complain about private types. TS-36's declaration-
      files section (`src/036/08-typescript.adoc:247`) discusses generating
      `.d.ts` files but never states that public API types must be explicitly
      exported for declarations to emit cleanly. Recommend a clause in
      "Declaration files" (`src/036/08-typescript.adoc:247`) noting that
      public-facing types MUST be exported.

- [ ] https://medium.com/cameron-nokes/the-30-second-guide-to-publishing-a-typescript-package-to-npm-89d93ff7bccd#4-run-your-build
      — the `prepublish` (modern equivalent: `prepare`) npm lifecycle script
      for automating the TypeScript compilation step before publishing (e.g.
      `"prepublish": "tsc"`). TS-36's `scripts` subsection
      (`src/036/06-packages-and-tooling.adoc:174`) and "Distributing packages"
      section (`src/036/06-packages-and-tooling.adoc:465`) do not mention npm
      lifecycle hooks (`prepublish`, `prepare`, `prepublishOnly`) for
      automating build-before-publish. Recommend a note in "Distributing
      packages" (`src/036/06-packages-and-tooling.adoc:465`) or the `scripts`
      subsection on using `prepare`/`prepublishOnly` to compile before
      publishing.

- [ ] https://github.com/airbnb/javascript#standard-library--isnan (rules 29.1–29.2)
      — use `Number.isNaN` over the global `isNaN`, and `Number.isFinite` over
      the global `isFinite`, because the global forms coerce non-numbers to
      numbers and return misleading results. TS-36's coercion section
      (`src/036/01-language-fundamentals.adoc:144`) covers
      `Number()`/`String()`/`Boolean()` but never mentions the
      `Number.isNaN`/`Number.isFinite` vs global `isNaN`/`isFinite` distinction;
      TS-36 itself uses the global `isNaN(date.getTime())` at
      `src/036/11-runtimes.adoc:231`, exactly the pattern Airbnb warns against.
      Recommend a new "Standard library" note under "Types and coercion"
      (`src/036/01-language-fundamentals.adoc:144`).

- [ ] https://github.com/airbnb/javascript#tc39-proposals (rule 28.2) — do not
      use TC39 proposals that have not reached stage 3 (they are not finalized
      and may change or be withdrawn). TS-36 has no rule restricting the use of
      non-standardized language features. Recommend a clause in "Using a subset
      of TypeScript" (`src/036/08-typescript.adoc:78`) or a new note in
      `src/036/01-language-fundamentals.adoc`.

- [ ] https://github.com/airbnb/javascript#variables--unary-increment-decrement
      (rule 13.6) — avoid unary `++`/`--`, use `+= 1`/`-= 1` instead (ASI
      footguns, more expressive mutation). TS-36 has no such rule and in fact
      uses `i++` in for-loop examples (`src/036/01-language-fundamentals.adoc:366`,
      `src/036/03-functions.adoc:140`, `src/036/10-functional-programming.adoc:136`).
      Missing — note the conflict with existing examples. (Scope call: flagged
      for user confirmation — TS-36's examples endorse `++`.) Recommend a
      clause in "Statements, control flow" (`src/036/01-language-fundamentals.adoc`).

- [ ] https://github.com/airbnb/javascript#naming--Acronyms-and-Initialisms
      (rule 23.9) — acronyms and initialisms in identifiers SHOULD be
      all-uppercase or all-lowercase (e.g. `SMSContainer`, not `SmsContainer`).
      TS-36's naming section (`src/036/02-syntax-and-style.adoc:41`) covers
      class/function/variable casing but not acronym casing. Recommend a
      clause in "Naming conventions" (`src/036/02-syntax-and-style.adoc:41`).

- [ ] https://github.com/airbnb/javascript#generators--nope (rules 11.2–11.3)
      — generator function guidance. TS-36 has no generator/`yield` guidance at
      all. Airbnb's rationale ("don't use generators — they don't transpile well
      to ES5", rule 11.2) is dated: ES5 transpilation is no longer a concern and
      generators are standard ES6, so TS-36's "use standard ECMAScript syntax"
      stance would not prohibit them. Missing, but flagged as borderline — the
      Airbnb rationale is obsolete; the only durable content is the `function*`
      spacing rule (11.3). (Scope call: user may consider this out-of-scope.)
      Recommend, if added, a brief note in "Functions" (`src/036/03-functions.adoc`)
      confirming generators are standard and the `function*` spacing convention.

- [ ] https://github.com/airbnb/javascript#modules--no-mutable-exports
      (rule 10.5) — do not export mutable bindings (`let`); export `const`
      references only. TS-36's modules section (`src/036/05-modules.adoc`)
      covers named/default exports and its FP section covers immutability
      generally, but neither addresses the specific rule against exporting
      mutable bindings. Recommend a clause in "Named exports"
      (`src/036/05-modules.adoc:289`).

- [ ] https://dev.to/yugjadvani/how-to-write-better-typescript-code-best-practices-for-clean-effective-and-scalable-code-38d2#use-types-and-interfaces-wisely
      (tip #2) — when to use `interface` (extensible object shapes, declaration
      merging) vs `type` alias (unions, intersections, complex compositions).
      TS-36's TypeScript section (`src/036/08-typescript.adoc`) uses `interface`
      in examples (`:181`) but never discusses when to prefer `interface` over
      `type`. Recommend a clause in "TypeScript" (`src/036/08-typescript.adoc`).

- [ ] https://dev.to/yugjadvani/how-to-write-better-typescript-code-best-practices-for-clean-effective-and-scalable-code-38d2#use-readonly-and-immutable-types-for-safety
      (tip #4) — the `readonly` modifier for properties/parameters to prevent
      accidental mutation at the type level. TS-36 covers immutability via
      `Object.freeze` (FP section) but never mentions TypeScript's `readonly`
      modifier. Recommend a clause in "TypeScript" (`src/036/08-typescript.adoc`).

- [ ] https://dev.to/yugjadvani/how-to-write-better-typescript-code-best-practices-for-clean-effective-and-scalable-code-38d2#5-define-utility-types-for-reusability
      (tip #5) — TypeScript's built-in utility types (`Partial`, `Pick`, `Omit`,
      `Readonly`, `Record`, etc.) for deriving variants without repeating
      definitions. TS-36 does not mention utility types. Recommend a clause in
      "TypeScript" (`src/036/08-typescript.adoc`).

- [ ] https://dev.to/yugjadvani/how-to-write-better-typescript-code-best-practices-for-clean-effective-and-scalable-code-38d2#8-utilize-enum-for-meaningful-values
      (tip #8 + comments) — enums, and the community recommendation (in the
      article's comments) to prefer `as const` objects + `keyof` over TypeScript
      enums. TS-36 does not mention enums at all, nor the controversy. Recommend
      a clause in "TypeScript" (`src/036/08-typescript.adoc`) covering the
      `as const` alternative.

- [ ] https://dev.to/yugjadvani/how-to-write-better-typescript-code-best-practices-for-clean-effective-and-scalable-code-38d2#9-use-never-for-exhaustive-checks
      (tip #9) — the `never` type as an exhaustiveness-checking tool in `switch`
      statements over union types, so adding a new case without handling it is a
      compile error. TS-36 does not cover `never`. Recommend a clause in
      "TypeScript" (`src/036/08-typescript.adoc`).

- [ ] https://dev.to/yugjadvani/how-to-write-better-typescript-code-best-practices-for-clean-effective-and-scalable-code-38d2#6-define-return-types-explicitly
      (tip #6) — whether to annotate function return types explicitly. TS-36
      does not address this. The article recommends always specifying them; its
      commenters disagree (prefer inference except for overloads or drift-prone
      functions). Missing/borderline — the community is split. (Scope call:
      flagged for user confirmation.) Recommend a clause in "TypeScript"
      (`src/036/08-typescript.adoc`) if the maintainers want a position.

- [ ] https://deno.com/blog/document-javascript-package#but-what-should-i-document
      — the `@module` JSDoc tag for packages that expose multiple modules, used
      in a file-level docblock to provide a module description and examples.
      TS-36's JSDoc tag list (`src/036/AGENTS.md:208`) omits `@module`, and its
      file-level-docblock rule (`src/036/AGENTS.md:246`) says
      `@file`/`@fileOverview` are not used (leading prose is the description) but
      does not mention `@module` for multi-module packages. Recommend adding
      `@module` to the tag list and a note in the file-level-docblock rule
      (`src/036/02-syntax-and-style.adoc`, JSDoc section).

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

- [ ] https://zellwk.com/blog/ignoring-files-from-npm-package/#which-method-to-use
      — the three mechanisms (`.gitignore`, `.npmignore`, `files`) and their
      precedence: `files` takes priority over the other two, and `.npmignore`
      takes priority over `.gitignore`. TS-36's `files` subsection
      (`src/036/06-packages-and-tooling.adoc:130`) covers only the `files`
      whitelist and omits the other two mechanisms and the precedence order.
      Partial rather than missing because TS-36 does recommend `files` (the
      highest-precedence mechanism); the gap is the absence of the full
      picture. Recommend extending the `=== files` subsection
      (`src/036/06-packages-and-tooling.adoc:130`) to describe the three
      mechanisms and their precedence, or a new subsection under
      "Distributing packages".

- [ ] https://jdxcode.medium.com/for-the-love-of-god-dont-use-npmignore-f93c08909d8d#whitelisting
      — the rationale for preferring whitelisting (`files`) over blacklisting
      (`.gitignore`/`.npmignore`): blacklisting is whack-a-mole, projects
      relying on it routinely ship unnecessary files (tests, log files, sqlite
      databases), and a single missed dotfile can leak secrets. TS-36's
      `files` subsection (`src/036/06-packages-and-tooling.adoc:130`)
      recommends `files` but does not explain why whitelisting is safer than
      blacklisting. Partial rather than missing because TS-36 does recommend
      `files`. Recommend a clause in the `=== files` subsection stating the
      whitelisting-over-blacklisting rationale.

- [ ] https://jdxcode.medium.com/for-the-love-of-god-dont-use-npmignore-f93c08909d8d#whitelisting
      — the convention of prefixing `files` entries with `/` to anchor them to
      the package root, so that e.g. `"lib"` does not also match a `test/lib`
      directory. TS-36's manifest template
      (`src/036/06-packages-and-tooling.adoc:77`) uses `"lib/**/*"` without a
      leading `/` and does not discuss anchoring. Partial rather than missing
      because the template's `lib/**/*` glob happens to avoid the named
      collision in practice, but the rule is unstated. Recommend a note in the
      `=== files` subsection (`src/036/06-packages-and-tooling.adoc:130`) on
      anchoring `files` entries with `/`.

- [ ] https://jdxcode.medium.com/for-the-love-of-god-dont-use-npmignore-f93c08909d8d#meanwhile
      — `npm publish` does not display the files packed (pre-npm@6); npm@6+
      began showing which files will be packed, and the one-liner
      `npm pack && tar -xvzf *.tgz && rm -rf package *.tgz` inspects the
      tarball contents without publishing. TS-36's "Distributing packages"
      section (`src/036/06-packages-and-tooling.adoc:472`) covers `npm pack`
      and installing the archive into an empty directory for verification — a
      more thorough check — but does not mention the quick tar-inspection
      one-liner or the npm@6 packed-file display. Partial rather than missing
      because TS-36 already mandates `npm pack` verification. Recommend a
      brief note in "Distributing packages"
      (`src/036/06-packages-and-tooling.adoc:465`) mentioning the tar
      one-liner as a faster alternative.

- [ ] https://web.archive.org/web/20260305114536/https://2ality.com/2021/06/typescript-esm-nodejs.html#recommendations-for-using-package-exports
      — the module-specifier convention: use filename extensions for imports
      *within* the current package (e.g. `'../tools/config-parser.js'`) but
      avoid extensions for imports *from another package* via its exported
      entry points (e.g. `'format-checker/strict'`). TS-36 requires extensions
      in relative imports (`src/036/05-modules.adoc:99`, "You MUST specify the
      file name") and its examples consistently use `.js`, but it never
      addresses the cross-package convention of omitting extensions for
      `exports`-mapped entry points. Partial rather than missing because the
      within-package rule is covered; the gap is the cross-package counterpart.
      Recommend a clause in "Internal imports"
      (`src/036/05-modules.adoc:107`) or "Package exports"
      (`src/036/06-packages-and-tooling.adoc:232`) stating the
      within-package-vs-cross-package extension convention.

- [ ] https://web.archive.org/web/20260305114536/https://2ality.com/2021/06/typescript-esm-nodejs.html#the-basics
      — the specific TypeScript constraint that `"type": "module"` is
      *required* for TypeScript ESM packages because TypeScript does not
      support the `.mjs` extension (it emits `.js` only). TS-36 covers both
      pieces separately — `.mjs` is "NOT RECOMMENDED" and "many development
      tools – notably TypeScript – do not recognize it"
      (`src/036/05-modules.adoc:412`), and `"type": "module"` is the
      recommended toggle (`src/036/05-modules.adoc:416`) — but never joins them
      into the explicit rule that TypeScript ESM packages MUST set `"type":
      "module"` because it is the only available ESM toggle for `.js` output.
      Partial rather than missing because both facts are stated; the gap is the
      combined TypeScript-specific recommendation. Recommend a sentence in
      "Toggling interpreters" (`src/036/05-modules.adoc:397`) or the `type`
      manifest subsection (`src/036/06-packages-and-tooling.adoc:146`).

- [ ] https://medium.com/cameron-nokes/the-30-second-guide-to-publishing-a-typescript-package-to-npm-89d93ff7bccd#1-add-declaration-true-to-your-tsconfigjson
      — the `declaration` compiler option in `tsconfig.json` (set to `true`
      to emit `.d.ts` files alongside compiled JS). TS-36's declaration-files
      section (`src/036/08-typescript.adoc:263`) states that "declaration
      files are generated automatically by the compiler" for TypeScript-
      authored libraries, but never names the `declaration` compiler option
      that controls this behavior. Partial rather than missing because the
      concept of automatic `.d.ts` generation is covered; the gap is the
      specific compiler option (which overlaps the existing 2ality `tsconfig`
      gap). Recommend a clause in "Declaration files"
      (`src/036/08-typescript.adoc:247`) naming the `declaration` option, or
      coverage in the new TypeScript-compiler-configuration subsection
      recommended by the 2ality gap.

- [ ] https://medium.com/cameron-nokes/the-30-second-guide-to-publishing-a-typescript-package-to-npm-89d93ff7bccd#5-run-npm-publish
      — `npm link` (and `npm link <package-name>` in a consumer project) as a
      local verification alternative to `npm pack` + install. TS-36's
      "Distributing packages" section (`src/036/06-packages-and-tooling.adoc:472`)
      mandates `npm pack` and installing the archive into an empty directory —
      a more thorough verification — but does not mention `npm link` as a
      faster iterative alternative. Partial rather than missing because TS-36
      already covers local verification more rigorously; the gap is the
      absence of `npm link` as an additional option. Recommend a brief note in
      "Distributing packages" (`src/036/06-packages-and-tooling.adoc:465`)
      mentioning `npm link` for rapid local iteration.

- [ ] https://github.com/airbnb/javascript#accessors--no-getters-setters
      (rules 24.2–24.4) — prefer `getVal()`/`setVal()` functions over JavaScript
      getter/setter syntax (getters/setters cause unexpected side effects and are
      harder to test); boolean accessors use `isVal()`/`hasVal()`; be consistent.
      TS-36 mentions named accessor properties descriptively
      (`src/036/04-objects-and-classes.adoc:42`) and mandates boolean methods
      read as assertions (`isEmpty()`, `src/036/02-syntax-and-style.adoc:80`), and
      notes consistent getter/setter naming
      (`src/036/12-architecture-and-design.adoc:22`). What TS-36 omits: the
      prescriptive rule to prefer `getVal()`/`setVal()` functions over getter/setter
      syntax. Partial rather than missing because TS-36 covers boolean naming and
      accessor existence. Recommend a clause in "Objects and classes"
      (`src/036/04-objects-and-classes.adoc`).

- [ ] https://dev.to/yugjadvani/how-to-write-better-typescript-code-best-practices-for-clean-effective-and-scalable-code-38d2#3-prefer-unknown-over-any
      (tip #3) — prefer `unknown` over `any` for uncertain types, because `unknown`
      forces narrowing before use while `any` disables the type checker. TS-36's
      non-null assertion section mentions `any`/`unknown` as alternatives
      (`src/036/08-typescript.adoc:112`) and the JSDoc rule says `any` SHOULD be
      avoided (`src/036/AGENTS.md:219`), but never states the "prefer `unknown`
      over `any`" rule with its rationale. Partial rather than missing because
      both types are named in passing. Recommend a clause in "TypeScript"
      (`src/036/08-typescript.adoc:112`).

- [ ] https://dev.to/yugjadvani/how-to-write-better-typescript-code-best-practices-for-clean-effective-and-scalable-code-38d2#1-leverage-strict-typing-options
      (tip #1),
      https://web.archive.org/web/20260305114536/https://2ality.com/2021/06/typescript-esm-nodejs.html#the-basics
      — the granular strict-mode `tsconfig.json` options (`noImplicitAny`,
      `strictNullChecks`, `strictFunctionTypes`) recommended in addition to
      `"strict": true`. TS-36 mentions `strictNullChecks` only in a NOTE as
      something that can be switched off (`src/036/08-typescript.adoc:120`); it
      never recommends enabling strict mode or its sub-options. This overlaps the
      existing 2ality `tsconfig` gap (see Missing above) which covers `strict`
      broadly; the dev.to article reinforces it with the specific recommended
      sub-options. Partial rather than missing because `strictNullChecks` is
      named (in passing). Recommend coverage in the new
      TypeScript-compiler-configuration subsection proposed by the 2ality gap
      (`src/036/08-typescript.adoc`).

- [ ] https://deno.com/blog/document-javascript-package#link-internally-to-other-parts-of-your-documentation
      — the `@linkcode` and `@linkplain` inline link tags (variants of `@link`
      that render as inline code / plain links). TS-36's JSDoc tag list includes
      `@link` (inline) but not `@linkcode` or `@linkplain`
      (`src/036/AGENTS.md:208`). Partial rather than missing because `@link` is
      covered. Recommend adding `@linkcode`/`@linkplain` to the tag list.

- [ ] https://deno.com/blog/document-javascript-package#a-brief-intro-to-jsdoc
      — the first paragraph of a JSDoc comment is the symbol's summary, shown in
      IDE tooltips, auto-complete, and search, and is the most important
      paragraph. TS-36 says descriptions are optional and written on the
      docblock's first line (`src/036/AGENTS.md:204`) but does not emphasize the
      first-paragraph-as-summary's role in tooltips/autocomplete or its primacy.
      Partial rather than missing because the first-line description rule exists.
      Recommend a clause in the JSDoc "Descriptions" rule
      (`src/036/02-syntax-and-style.adoc`, JSDoc section).

- [ ] https://deno.com/blog/document-javascript-package#but-what-should-i-document
      — the rule to document every exported symbol's members: each property and
      method of a class or interface, not just the symbol itself. TS-36 mandates
      exported symbols have `@type` (`src/036/AGENTS.md:237`) and classes have
      class-level docblocks + constructor params (`src/036/AGENTS.md:240`), but
      does not explicitly require documenting each property/method of an interface
      or each method/property of a class. Partial rather than missing because
      class-level and constructor documentation is covered. Recommend extending
      the JSDoc "Classes"/exported-types rules (`src/036/02-syntax-and-style.adoc`,
      JSDoc section).

- [ ] https://deno.com/blog/document-javascript-package#use-markdown-for-a-better-documentation-experience
      — markdown features in JSDoc beyond TS-36's narrow permitted list: section
      headings (`#`), bullet lists (`-`), blockquotes (`>`), and `[!IMPORTANT]`
      callouts. TS-36 permits "backticks, `*bold*`, `_italic_`, `[text](url)`"
      (`src/036/AGENTS.md:206`). Partial rather than missing because a markdown
      subset is permitted. Recommend extending the markdown list in the JSDoc
      "Descriptions" rule.

- [ ] https://deno.com/blog/document-javascript-package#add-examples-to-jsdoc
      — the `@example` title/description convention: text immediately after
      `@example` serves as the example title, and text beneath the code block
      becomes its description (rendered in generated docs). TS-36 requires
      `@example` be correct and executable in isolation (`src/036/AGENTS.md:256`)
      but does not describe the title/description sub-syntax. Partial rather than
      missing because the `@example` correctness rule exists. Recommend a clause
      in the `@example` rule (`src/036/02-syntax-and-style.adoc`, JSDoc section).

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

- [ ] https://jdxcode.medium.com/for-the-love-of-god-dont-use-npmignore-f93c08909d8d#npm-and-yarn-patch-this-please
      — the recommendation that npm/yarn should fail or warn (and emit the
      exact files being packed) if a user uses `.npmignore` without `files`,
      and that `npm init`/`yarn init` should default to including `files`.
      Flagged out-of-scope: these are feature requests against the npm/yarn
      CLIs, not ECMAScript coding conventions. Plausible home if kept: none
      within TS-36; belongs in TS-38 (Node.js Applications) if anywhere.

- [ ] https://web.archive.org/web/20260305114536/https://2ality.com/2021/06/typescript-esm-nodejs.html#visual-studio-code
      — VS Code settings (`javascript.preferences.importModuleSpecifierEnding`,
      `typescript.preferences.importModuleSpecifierEnding`) to make
      auto-imports include `.js` extensions. Flagged out-of-scope: this is
      IDE-specific configuration, not an ECMAScript coding convention. No
      plausible home within TS-36.

- [ ] https://web.archive.org/web/20260305114536/https://2ality.com/2021/06/typescript-esm-nodejs.html#visual-studio-code
      — a regex search-and-replace pattern for retroactively adding `.js`
      extensions to existing local imports. Flagged out-of-scope: this is an
      editor workflow tip, not a coding convention. No plausible home within
      TS-36.

- [ ] https://medium.com/cameron-nokes/the-30-second-guide-to-publishing-a-typescript-package-to-npm-89d93ff7bccd#if-you-havent-written-your-ts-based-package-yet
      — the scaffolding commands `npm init -y` and `tsc --init` for
      generating a default `package.json` and `tsconfig.json`. Flagged
      out-of-scope: these are getting-started workflow tips, not coding
      conventions. No plausible home within TS-36.

- [ ] https://github.com/airbnb/javascript#events (rule 25.1) — pass an object
      literal ("hash") rather than a raw value as an event payload, so subsequent
      contributors can add fields without updating every handler. Flagged
      out-of-scope: DOM/Backbone event conventions belong in TS-37 (Web Platform
      APIs) or TS-18 (Web GUIs), which TS-36 delegates browser/DOM guidance to.
      (The underlying "prefer structured payloads" principle is already covered
      by TS-36's API-consistency rule, `src/036/12-architecture-and-design.adoc`.)

- [ ] https://github.com/airbnb/javascript#jquery (rules 26.1–26.4) — jQuery
      `$`-prefix convention, lookup caching, and scoped `find` queries. Flagged
      out-of-scope: jQuery is a legacy DOM library; TS-36 delegates browser/DOM
      guidance to TS-37.

- [ ] https://github.com/airbnb/javascript#ecmascript-5-compatibility (rule 27.1)
      and `#performance` — ES5 compatibility-table references and the
      performance-links section. Flagged out-of-scope: ES5 transpilation is
      obsolete, and performance micro-optimization is out-of-scope per TS-36's
      "don't over-optimize early" stance (`src/036/AGENTS.md:762`).

- [ ] https://deno.com/blog/document-javascript-package#audit-your-jsdoc —
      Deno-specific JSDoc audit tooling: `deno doc`, `deno doc --lint`,
      `deno test --doc`, and the `jsdoc` CLI. Flagged out-of-scope: these are
      Deno-runtime-specific (or generic) CLI tools, not ECMAScript coding
      conventions. Plausible home if kept: none within TS-36 (a tooling/CI
      standard if anywhere).

- [ ] https://deno.com/blog/document-javascript-package#keep-jsdoc-up-to-date-with-code-changes
      — docs-driven development as a process for keeping JSDoc current, and
      `deno test --doc` for type-checking doc examples. Flagged out-of-scope: a
      workflow/process recommendation, not a coding convention.

- [ ] https://github.com/nodeshift/nodejs-reference-architecture/blob/main/docs/functional-components/webframework.md
      — the entire page (Express 4.x recommendation with `~4.x.y` version
      pinning; separate business/admin ports via `PORT`/`ADMIN_PORT` env vars;
      liveness/readiness endpoints; global middleware before routes; Helmet for
      HTTP headers; `--max-http-header-size`/`NODE_OPTIONS`; testability via
      component/route decomposition). Flagged out-of-scope: this is Node.js
      application architecture, which TS-36 explicitly delegates to TS-38 (Node.js
      Applications) — see `src/036/AGENTS.md:696`. The `"test"` npm script
      convention is the only in-scope item and is already covered by TS-36's
      manifest templates (`src/036/06-packages-and-tooling.adoc:683`, `:757`,
      `:786`).

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

- https://zellwk.com/blog/ignoring-files-from-npm-package/ and
  https://jdxcode.medium.com/for-the-love-of-god-dont-use-npmignore-f93c08909d8d
  were fetched successfully in full.

- https://web.archive.org/web/20260305114536/https://2ality.com/2021/06/typescript-esm-nodejs.html
  was fetched successfully in full (Internet Archive copy).

- https://medium.com/cameron-nokes/the-30-second-guide-to-publishing-a-typescript-package-to-npm-89d93ff7bccd
  was fetched successfully in full.

- https://dev.to/yugjadvani/how-to-write-better-typescript-code-best-practices-for-clean-effective-and-scalable-code-38d2,
  https://github.com/airbnb/javascript (raw README.md),
  https://deno.com/blog/document-javascript-package,
  https://github.com/nodeshift/nodejs-reference-architecture/blob/main/docs/functional-components/webframework.md,
  and https://www.linkedin.com/posts/progressivethinker_javascript-frontend-technology-activity-7274626911429967872-3_2G/
  were fetched successfully in full. The Airbnb React and CSS-in-JavaScript
  companion guides were not fetched (out-of-scope for TS-36).