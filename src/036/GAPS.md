# TS-36 gap analysis

Gaps found comparing TS-36: ECMAScript (JavaScript/TypeScript) against the
following reference resources:

- https://ricostacruz.com/rsjs/ (rsjs — "Reasonable System for JavaScript
  Structure")

**Assessment.** RSJS is a guide for structuring JavaScript in *non-SPA,
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

**Status:** Re-run, 2026-08-05. All four in-scope gaps (2 missing, 2 partial)
  have been addressed in the standard and are checked off below. The 15
  web-client out-of-scope items have been relocated to `src/018/GAPS.md`
  (TS-18: Web GUIs) at the maintainer's direction; see the note under
  Out-of-scope below.

## Missing

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

## Partial

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

## Unresolved

- (none — the single reference URL was fetched successfully in full.)