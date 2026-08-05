# TS-40 gap analysis

Gaps found comparing TS-40: *CSS* against the following reference resources
(the standard's `__TODO__` directory — the author's working notes and source
material, plus bookmarked external resources):

- `__TODO__/css/` — "Nirvarnia CSS" coding-style and architecture notes (an
  earlier, partly-unadopted methodology).
- `__TODO__/css2/` — earlier drafts of TS-40 itself (Nirvarnia CSS methodology).
- `__TODO__/css3/` — topical reference notes on CSS features.
- `__TODO__/css3/_todo/architecture.md`, `introduction.md`, `principles.md` —
  earlier long-form drafts including a survey of external methodologies.
- `__TODO__/css3/_todo/CSS Master.pdf` (Tiffany Brown, O'Reilly) — general CSS
  reference book; text extracted via `pdftotext`.
- `__TODO__/css3/_todo/The CSS Handbook by Flavio Copes.pdf` — general CSS
  introduction; text extracted via `pdftotext`.
- `__TODO__/css3/_todo/*.URL` bookmarks, fetched:
  https://github.com/AllThingsSmitty/css-protips ,
  https://painlesscss.com/top-10-css-mistakes.html ,
  http://vanseodesign.com/css/css-specificity-inheritance-cascaade/ .

**Assessment.** The `__TODO__` directory is the author's own working material,
so a large share of it (the `css2/` drafts and the `architecture.md` /
`introduction.md` / `principles.md` long-form drafts) is the source from which
TS-40 was condensed and is already covered. The genuinely external resources
(the two PDFs and the three bookmarked URLs) are broad general CSS references;
the bulk of their content (individual properties, transforms, transitions,
SVG, debugging tooling, preprocessors) sits outside TS-40's stated purpose —
which is a CSS *architecture / design methodology*, explicitly excluding syntax
formatting, comments/documentation, tooling, and team workflow. The gaps that
remain are mostly "partial": foundational mechanisms TS-40 leans on (specificity
calculation, `@supports`, custom properties) and modern layout primitives
(Flexbox, CSS Grid) that the standard — clearly written before they were
ubiquitous — does not address.

**Status:** First run. All gaps below are open. Date: 2026-08-05.

## Missing

- [ ] `__TODO__/css3/0100-layout.md:9` and `__TODO__/css3/_todo/layout-and-positioning.md`
      ("use Grid for layout, Flexbox for components"), plus `CSS Master.pdf` Ch.4
      "Complex Layouts" and `The CSS Handbook by Flavio Copes.pdf` "Flexbox"/"CSS
      Grid": modern layout primitives (Flexbox, CSS Grid, container queries,
      intrinsic web design) are not addressed anywhere in the standard. The
      Layout section (`04-layout.adoc`) still illustrates layout with `float`,
      `display: table-cell`, and absolute positioning. Recommend a new section
      in `04-layout.adoc` (after line 1, or replacing/clarifying the "Grid
      systems" rule at `04-layout.adoc:187`, which reads ambiguously now that
      CSS Grid exists).

- [ ] `__TODO__/css/0350-variables.md:1`, `The CSS Handbook by Flavio Copes.pdf`
      "Custom Properties" (`csshandbook.txt:1651`), and `CSS Master.pdf`: CSS
      Custom Properties (variables) — their cascade behaviour, `:root`
      scoping, and use for theming/modifier values — are not addressed anywhere
      in the standard, despite being architecturally relevant (they cascade and
      intersect with the modifier/system). Recommend a new section (e.g. a new
      `09-variables.adoc`, or a subsection in `02-principles.adoc` or
      `07-modifiers.adoc`).

- [ ] `__TODO__/css/0100-selectors.md:69` ("ID selectors MUST NOT be used in any
      circumstance"), `CSS Master.pdf` Ch.2 "Avoid Using id Selectors"
      (`cssmaster.txt:2660`), and `The CSS Handbook by Flavio Copes.pdf`
      (`csshandbook.txt:666`): the standard implies a class-only contract
      (`03-class-names.adoc:171-183`, `AGENTS.md`) but never explicitly addresses
      ID selectors or their high-specificity consequences. Recommend an explicit
      rule in `03-class-names.adoc:37` (Naming conventions) or
      `02-principles.adoc:166` (Defensive programming).

## Partial

- [ ] `__TODO__/css3/_200-selectors.md:18-43`, the Vanseo Design URL
      "Specificity Calculations", `CSS Master.pdf` Ch.1 "Selectors and
      Specificity" (`cssmaster.txt:2204`), and `The CSS Handbook by Flavio
      Copes.pdf` (`csshandbook.txt:515`) cover the specificity *calculation*
      (the A,B,C / four-slot system) — the standard repeatedly relies on
      specificity, `!important`, and selector depth (e.g. `07-modifiers.adoc:76`
      "Specificity and !important") but never explains how specificity is
      computed. Recommend adding the calculation to `07-modifiers.adoc:76` or a
      new subsection in `02-principles.adoc`.

- [ ] `CSS Master.pdf` Ch.7 "Conditional Rules with @supports"
      (`cssmaster.txt:8729`) and `The CSS Handbook by Flavio Copes.pdf` "Feature
      Queries" (`csshandbook.txt:4345`) cover the native `@supports` at-rule for
      feature-based progressive enhancement — the standard covers class-based
      feature detection via the `supports-` prefix (`03-class-names.adoc:203`,
      `07-modifiers.adoc:73`) but not the native `@supports` mechanism.
      Recommend adding `@supports` to the Progressive enhancement section
      (`02-principles.adoc:362`).

- [ ] `__TODO__/css3/_todo/properties.md`, `__TODO__/css3/_todo/general-style.md`
      ("vendor prefixes"), and `The CSS Handbook by Flavio Copes.pdf`
      (`csshandbook.txt:5268`) cover vendor-prefix conventions (avoid in
      production; if used, place before the standard property and document
      targeted browsers) — the standard uses vendor-prefixed properties in
      examples (`02-principles.adoc:409` `-webkit-border-image`,
      `06-components.adoc` `-webkit-animation`) without stating the convention.
      Recommend a note in `02-principles.adoc:399` (Progressive enhancement
      examples).

- [ ] `__TODO__/css3/_todo/architecture.md:40-302` surveys OOCSS, BEM, SMACSS,
      and SUIT CSS (their categories, naming syntax, and rules); `CSS
      Master.pdf` Ch.2 "BEM"/"Atomic CSS" (`cssmaster.txt:2777`) adds BEM and
      Atomic CSS. The standard names these methodologies
      (`01-overview.adoc:87-93`) and lists them in References but gives no
      summary of what each prescribes, so a reader cannot compare or understand
      the standard's lineage. Recommend expanding `01-overview.adoc:87-93` into
      a brief comparative summary. (Borderline: the standard's purpose is to
      prescribe its own methodology, not survey others — flagged for the user.)

- [ ] `CSS Master.pdf` Ch.4 "Choosing a Box Model with box-sizing"
      (`cssmaster.txt:3957`), `The CSS Handbook by Flavio Copes.pdf` "Normalizing
      CSS" (`csshandbook.txt:5234`), and the css-protips URL ("Use a CSS Reset" /
      "Inherit `box-sizing`") cover reset/normalize strategy and
      `box-sizing: border-box` — the standard mentions "Raw element resets" and
      `@import "reset"` (`08-filesystem.adoc:8`, `:60`) but gives no reset
      guidance or `box-sizing` recommendation. Recommend adding reset/box-sizing
      guidance to `08-filesystem.adoc:8` or `05-elements.adoc:1`.

- [ ] `__TODO__/css/0050-charset.md:10-15` prescribes the `@charset` rule
      (double quotes required, first line of the file) — the standard's
      filesystem example uses `@charset "UTF-8";` (`08-filesystem.adoc:10`) but
      does not state the formatting rule. Recommend a note at
      `08-filesystem.adoc:10`.

- [ ] `The CSS Handbook by Flavio Copes.pdf` "Import" (`csshandbook.txt:774-781`)
      notes that `@import` must precede all other CSS (else ignored) and can take
      a media descriptor — the standard relies heavily on `@import`
      (`08-filesystem.adoc:8-19`) without stating either rule. Recommend a note
      in `08-filesystem.adoc:8-19`.

- [ ] `CSS Master.pdf` Ch.7 "Don't Use device-width with Media Queries" and
      "Content-driven Media Queries" (`cssmaster.txt:8566-8570`) — the standard
      uses `min-width` rem breakpoints (`04-layout.adoc:45`,
      `05-elements.adoc:97`, with the rem tip at `:119`) but does not warn
      against `device-width` or advocate content-driven breakpoints. Recommend
      a note in `04-layout.adoc:45` or `05-elements.adoc:97`.

- [ ] `__TODO__/css3/_todo/cascade-control.md:1`, `The CSS Handbook by Flavio
      Copes.pdf` (`csshandbook.txt:740-766`), and the css-protips URL ("Use
      `unset` Instead of Resetting All Properties") cover the inheritance/reset
      keywords (`inherit`, `initial`, `unset`, `revert`, `all`) — the standard
      discusses resetting inherited properties extensively
      (`02-principles.adoc:71` Encapsulation, `05-elements.adoc:157`) but not the
      keyword mechanisms that achieve it. Recommend a brief note in
      `02-principles.adoc:71` or `05-elements.adoc`.

- [ ] `__TODO__/css2/_architecture.md` (the `contain`/`all` properties,
      Web Components polyfills, and CSS Modules as scoping mechanisms) and the
      Painless CSS URL (CSS-in-JS) cover alternative scoping mechanisms — the
      standard's overview claims applicability "whether … generated by a
      CSS-in-JS framework" (`README.adoc:12-14`) and mentions `@scope` and the
      Shadow DOM (`01-overview.adoc:22-34`) but does not address CSS-in-JS
      frameworks or CSS Modules. Recommend expanding `01-overview.adoc:12-34`.

- [ ] `__TODO__/css3/_todo/printers.md:1` and `The CSS Handbook by Flavio
      Copes.pdf` "CSS for print" (`csshandbook.txt:5346`, recommending a
      separate file loaded with `media="print"`) — the standard uses `@media
      print` in examples (`04-layout.adoc:67`, `05-elements.adoc:114`) but gives
      no dedicated print-style guidance. Recommend a note in `04-layout.adoc`
      or `05-elements.adoc:114`.

- [ ] `__TODO__/css2/_principles.md` (Defensive Programming section) explains
      *why* component/layout classes must not be type-qualified: type-qualifying
      raises specificity so modifier/utility classes can no longer override them
      (the `button.Button` vs `.background-midgrey` example) — the standard
      states the rule (`02-principles.adoc:188-194`) but omits the
      modifier-override rationale. Recommend adding the rationale at
      `02-principles.adoc:188`.

## Out-of-scope

- [ ] `__TODO__/css/` (terminology, charset formatting, selector/property/value
      formatting, comments, docblocks) and `__TODO__/css3/_todo/general-style.md`
      cover CSS *syntax formatting* and *comment/documentation* conventions. The
      standard explicitly excludes these (`01-overview.adoc:95-99`). Flagged for
      the user to confirm.

- [ ] `__TODO__/css3/_todo/` topic notes on individual properties and techniques
      — `transitions.md`, `backgrounds-and-borders.md`, `filters.md`,
      `forms-and-buttons.md`, `hiding-things.md`, `typography-and-fonts.md`,
      `units.md`, `pseudo-elements.md`, `selectors-and-specificity.md`,
      `layout-and-positioning.md` (vertical centering) — and the css-protips URL
      (`:not()`, `:empty`, `:root`, `nth-child`, lobotomized owl,
      `aspect-ratio`, `object-fit`, intrinsic-ratio boxes, margin hacks). These
      are property/technique references; the standard is an architecture
      methodology, not a property reference. Flagged for the user to confirm.

- [ ] `__TODO__/css3/_todo/performance.md` and `CSS Master.pdf` Ch.3 "Debugging
      and Optimization" (minification, CSS Lint, UnCSS, critical-path CSS,
      HTTP/2 concatenation, reflows) cover performance and tooling. The standard
      mentions "rendering speed" as a methodology benefit and covers
      shallow-selector architecture, but performance optimization and tooling
      are explicitly out-of-scope (`01-overview.adoc:46-49`).

- [ ] `CSS Master.pdf` Ch.2 "Managing Styles for Legacy Browsers" (IE
      conditional comments) is legacy-IE-specific. The standard's
      progressive-enhancement approach (`02-principles.adoc:399-414`) already
      covers the modern strategy; IE-specific techniques are out-of-scope.

- [ ] The Painless CSS URL's Mistake #9 (SEO / semantic HTML) is covered by
      TS-39 (HTML) and TS-19 (SEO), not TS-40. Mistakes #2 and #1 (reading
      documentation, learning CSS systematically) are meta/learning advice.

- [ ] `__TODO__/css2/_todo-styleguide.md` and `CSS Master.pdf` Ch.2 "Pattern
      Libraries" cover living style guides, pattern libraries, and
      style-guide-driven development. The overview explicitly states "A web
      design methodology is not a visual style guide or UI pattern library"
      (`01-overview.adoc:45-49`); workflow is also excluded.

- [ ] `__TODO__/css/5000-architecture/` (one-word element names, double-dash
      `--` modifiers, two-word component names, app-namespace prefixes) and
      `__TODO__/css2/_conventions.md` (special-character class names like
      `OFF_CANVAS/BANNER`) are an *alternative, unadopted* methodology whose
      naming heuristics partly contradict the standard's own examples (e.g.
      `Logo`, `Card`, `Box`). Treated as not adopted rather than as gaps;
      flagged for the user to overrule if any heuristic (e.g. an app-namespace
      prefix for components shared across apps) is wanted.

## Unresolved

- [ ] None. All reference resources were retrieved. The two PDFs are binary but
      were readable via `pdftotext` (`/tmp/cssmaster.txt`, `/tmp/csshandbook.txt`
      — temporary extraction files, not part of the project). The three `.URL`
      bookmarks were fetched successfully.