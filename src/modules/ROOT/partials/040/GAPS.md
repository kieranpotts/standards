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

**Assessment (run 1).** The `__TODO__` directory is the author's own working
material, so a large share of it (the `css2/` drafts and the `architecture.md` /
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

### Run 2 — GitHub issue #64 reference resources

A second run compared TS-40 against the four external CSS resources bookmarked in
https://github.com/kieranpotts/standards/issues/64 :

- https://cssguidelin.es/ — Harry Roberts, *CSS Guidelines*. A high-level advice
  document covering syntax/formatting, commenting, naming (BEM-like), selectors,
  specificity, and architectural principles (OOCSS, SRP, OCP, DRY, composition,
  SoC).
- https://github.com/anthonyshort/idiomatic-sass — Anthony Short, *Idiomatic
  Sass*. OOP-Sass principles, BEM/Montage naming, and Sass-specific tooling
  (modules, packages, mixins, load paths, Bower).
- https://github.com/necolas/idiomatic-css — Nicolas Gallagher, *Idiomatic CSS*.
  General principles, whitespace, comments, and ruleset formatting.
- http://web.archive.org/web/20220227093948/http://rscss.io/ — Rico Sta. Cruz,
  *rscss*. A component-based methodology: two-word component names, one-word
  elements, dash-prefixed variants, nested-component rules, layouts, helpers.

**Assessment (run 2).** These are methodology/style-guide resources, so they sit
closer to TS-40's scope than run 1's general CSS references. Even so, most of
their content is either already covered by TS-40 (often via a different but
equivalent mechanism) or is explicitly out-of-scope:

- cssguidelin.es' *Syntax and Formatting* and *Commenting* sections, all of
  idiomatic-css, and the Sass-tooling half of idiomatic-sass (modules, packages,
  mixins, functions, load paths) are excluded by `01-overview.adoc:95-99` and
  the tooling/workflow exclusion at `01-overview.adoc:45-49`.
- cssguidelin.es' *Selector Performance* mechanics (right-to-left matching, key
  selector) and idiomatic-sass' performance notes are out-of-scope (performance
  optimization/tooling, `01-overview.adoc:46-49`); cssguidelin.es itself states
  selector performance "should be fairly low on your list of things to optimise."
- The alternative *naming conventions* — BEM `__`/`--` syntax, Montage
  namespacing, rscss's two-word component rule, dash-prefixed `-variant` names,
  underscore-prefixed `_helper` names — are deliberately divergent from TS-40's
  own conventions (CamelCase components, parent-prefixed modifiers,
  `UPPER_CASE` layout). TS-40 names BEM and the others in its overview and
  references and prescribes its own system; these are alternative methodologies,
  not gaps. (Note: TS-40 explicitly rejects the leading-dash modifier form at
  `07-modifiers.adoc:7-8`, reserving it for vendor extensions.)
- rscss's substantive methodology rules — think in components, keep positioning
  out of components, avoid over-nesting, one component per file, don't reach
  into nested components — are all already covered by TS-40 (components §,
  `06-components.adoc:75-77` and `:232-236`, `08-filesystem.adoc:4-6`). rscss
  prevents element-name bleed via `>` child selectors; TS-40 prevents it via
  parent-prefixed modifier names (`06-components.adoc:188-212`). Different
  mechanisms, same concern.
- cssguidelin.es' architectural principles (SRP, OCP, DRY, composition over
  inheritance, SoC, OOCSS structure/skin) are already covered by TS-40's
  `02-principles.adoc` (Composition `:282`, Open/closed `:319`, DRY `:331`,
  SoC `:218`) and reinforce the existing run-1 partial gap on surveying
  methodologies.
- cssguidelin.es' *IDs in CSS* ("never use IDs") and idiomatic-sass' *Never uses
  IDs* reinforce the existing run-1 missing gap on ID selectors; no new entry
  is created (the original citation is retained per the re-run rules).

The two genuinely new partial gaps from run 2 both fall under cssguidelin.es'
*Specificity* section: proactive `!important` for utility classes, and
specificity remediation hacks.

**Status:** Run 3 (close-gaps) closed 16 of 17 actionable gaps: all 3 Missing
items (modern layout primitives, custom properties, ID selectors) and 13 of
14 Partial items (specificity calculation and remediation hacks, `@supports`,
vendor prefixes, proactive `!important`, reset/`box-sizing`, `@charset`,
`@import`, `device-width` media queries, `inherit`/`initial`/`unset`,
type-qualification rationale, print style sheets, CSS-in-JS/CSS Modules
scoping). One Partial item — the OOCSS/BEM/SMACSS/SUIT CSS methodology
comparison — is self-flagged as a scope question in its own text and left
open for the user to decide. 12 Out-of-scope and 1 Unresolved item are
untouched, per the skill's rules. New `09-variables.adoc` added and wired
into the page. Date: 2026-08-14.

**Run 4 (`close-gaps`), 2026-08-16.** Closed the 2 Missing items that had
been filed by the 2026-08-15 Out-of-scope sweep as concrete, user-directed
adoptions separate from the still-pending scope-broadening RFC: the
app-namespace component-prefix heuristic, and the `js-` JavaScript-hook-class
fallback. Both written into `03-class-names.adoc`. TS-40 now has 0
actionable items. The one Partial item declined on 2026-08-14 (OOCSS/BEM/
SMACSS/SUIT CSS methodology comparison) remains terminally closed with no
content change, per that run's own note — not re-opened. 10 Out-of-scope
items remain open, all still pending the same scope-broadening RFC decision
recorded on 2026-08-15 (or, for two of them, already confirmed/routed) — see
the "Out-of-scope" section below for the per-item breakdown. The 1
Unresolved item (none — all sources were retrieved) is already closed.

**Run 5, 2026-08-16.** The user confirmed the OOCSS/BEM/SMACSS/SUIT CSS
methodology-comparison item's 2026-08-14 decline stands as final rather
than merely deferred; its checkbox ticked accordingly. TS-40 now has 0
unchecked items of any kind and is fully resolved by the flat-count
measure. Note this is not the same as "nothing left pending": 10
Out-of-scope items remain ticked-but-held against the still-unformalized
scope-broadening RFC recorded on 2026-08-15 (web-client security,
architecture/SPA/PWA, syntax formatting, performance/tooling, legacy-IE
content) — decided in direction but not yet written up. That RFC, not a
`close-gaps` run, is what would action them.

## Missing

- [x] `__TODO__/css3/0100-layout.md:9` and `__TODO__/css3/_todo/layout-and-positioning.md`
      ("use Grid for layout, Flexbox for components"), plus `CSS Master.pdf` Ch.4
      "Complex Layouts" and `The CSS Handbook by Flavio Copes.pdf` "Flexbox"/"CSS
      Grid": modern layout primitives (Flexbox, CSS Grid, container queries,
      intrinsic web design) are not addressed anywhere in the standard. The
      Layout section (`04-layout.adoc`) still illustrates layout with `float`,
      `display: table-cell`, and absolute positioning. Recommend a new section
      in `04-layout.adoc` (after line 1, or replacing/clarifying the "Grid
      systems" rule at `04-layout.adoc:187`, which reads ambiguously now that
      CSS Grid exists).

      **Resolved.** Closed by a new "Modern layout primitives" section in
      `04-layout.adoc`, placed immediately before the existing "Grid systems"
      section it clarifies. States that Flexbox/Grid/container queries do not
      change the standard's naming or grid-systems conventions, only how a
      layout section's internal positioning is implemented; recommends
      Flexbox for one-dimensional and Grid for two-dimensional arrangements;
      and documents `@container` as the size-based analog of the standard's
      existing viewport-based progressive enhancement, requiring the same
      unenhanced baseline. The existing "Grid systems" section gained one
      clause noting that a component-level grid system MAY now be implemented
      with CSS Grid. `float` and `display: table-cell` remain in
      `07-modifiers.adoc`'s and other pre-existing examples elsewhere in the
      standard as illustrations of older techniques; not rewritten, since the
      gap was the absence of modern coverage, not the presence of old
      examples. Sources (`CSS Master`, `The CSS Handbook`) added to the
      page's `== References`.

- [x] `__TODO__/css/0350-variables.md:1`, `The CSS Handbook by Flavio Copes.pdf`
      "Custom Properties" (`csshandbook.txt:1651`), and `CSS Master.pdf`: CSS
      Custom Properties (variables) — their cascade behaviour, `:root`
      scoping, and use for theming/modifier values — are not addressed anywhere
      in the standard, despite being architecturally relevant (they cascade and
      intersect with the modifier/system). Recommend a new section (e.g. a new
      `09-variables.adoc`, or a subsection in `02-principles.adoc` or
      `07-modifiers.adoc`).

      **Resolved.** Closed by a new `09-variables.adoc`, "Custom properties",
      appended after `08-filesystem.adoc` and wired into the page's include
      list. Covers `:root`-scoped global tokens, component-scoped custom
      properties overridden by a modifier class (tying the mechanism to this
      standard's existing modifier convention), the `var()` fallback value,
      and an explicit rule that custom properties change values while classes
      change which rules apply, so one MUST NOT substitute for the other.
      Chosen as a new numbered partial, not a subsection of
      `02-principles.adoc` or `07-modifiers.adoc`, because custom properties
      are a distinct topic with enough content (four subtopics) to warrant
      their own section, per the "new topic → new partial" default. Sources
      (`The CSS Handbook`, `CSS Master`) added to the page's `== References`.

- [x] `__TODO__/css/0100-selectors.md:69` ("ID selectors MUST NOT be used in any
      circumstance"), `CSS Master.pdf` Ch.2 "Avoid Using id Selectors"
      (`cssmaster.txt:2660`), and `The CSS Handbook by Flavio Copes.pdf`
      (`csshandbook.txt:666`): the standard implies a class-only contract
      (`03-class-names.adoc:171-183`, `AGENTS.md`) but never explicitly addresses
      ID selectors or their high-specificity consequences. Recommend an explicit
      rule in `03-class-names.adoc:37` (Naming conventions) or
      `02-principles.adoc:166` (Defensive programming).

      **Resolved.** Closed by a new paragraph in `03-class-names.adoc`,
      immediately before "Naming conventions" (rather than inside that
      section, since the new rule is about what is prohibited, not about a
      naming convention as such). States that ID selectors MUST NOT be used
      under any circumstance, explains that an ID-selector ruleset can never
      be reused, and cross-references the new specificity-calculation
      section's ID-versus-class-count rule. Source (`CSS Master`) already
      added to the page's `== References` by an earlier item in this batch.

- [x] `__TODO__/css/5000-architecture/` (routed in from the Out-of-scope
      review, 2026-08-15) — an app-namespace prefix for component class
      names shared across multiple apps. The user asked specifically for
      this heuristic to be adopted, overruling the original "alternative,
      unadopted methodology" classification. Recommend a new paragraph or
      subsection in `03-class-names.adoc`, alongside the existing
      component-naming conventions. Not yet written into any partial.

      **Resolved, 2026-08-16.** Closed by a new paragraph in
      `03-class-names.adoc`, immediately after the paragraph explaining
      case-based role hierarchy. States that a component's `CamelCase` name
      MAY be prefixed with a lower-case application namespace joined by a
      colon (`app1:NavBar`) where its markup is shared across multiple,
      independently-deployed applications, reserved for that specific
      collision case rather than applied by default.

- [x] https://cssguidelin.es/#naming-conventions (routed in from the
      Out-of-scope review, 2026-08-15) — a `js-` prefix convention for
      JavaScript hook classes, as an alternative or addition to TS-40's
      current `data-*`-attribute JS-hook approach
      (`03-class-names.adoc:171-183`). The user asked specifically for
      this to be adopted, overruling the original "alternative naming
      methodology" classification. Recommend a new paragraph in
      `03-class-names.adoc`, near the existing `data-*` JS-hook guidance,
      reconciling the two approaches (e.g. clarifying whether `js-`
      replaces or supplements `data-*`). Not yet written into any partial.

      **Resolved, 2026-08-16.** Closed by a new paragraph in
      `03-class-names.adoc`'s "Dynamic classes" section, immediately after
      the existing `data-*` guidance. Reconciled the two approaches by
      scoping `js-` to a fallback for when a codebase's existing tooling or
      a third-party library expects a class-based hook, not an alternative
      to `data-*` in the general case; states the `js-` class MUST NOT also
      carry styling, preserving the same separation of concerns the
      `data-*` convention protects. Source (cssguidelin.es) already present
      in the page's `== References`; annotated with this section.

## Partial

- [x] `__TODO__/css3/_200-selectors.md:18-43`, the Vanseo Design URL
      "Specificity Calculations", `CSS Master.pdf` Ch.1 "Selectors and
      Specificity" (`cssmaster.txt:2204`), and `The CSS Handbook by Flavio
      Copes.pdf` (`csshandbook.txt:515`) cover the specificity *calculation*
      (the A,B,C / four-slot system) — the standard repeatedly relies on
      specificity, `!important`, and selector depth (e.g. `07-modifiers.adoc:76`
      "Specificity and !important") but never explains how specificity is
      computed. Recommend adding the calculation to `07-modifiers.adoc:76` or a
      new subsection in `02-principles.adoc`.

      **Resolved.** Closed by extending `07-modifiers.adoc`'s existing
      "Specificity and !important" section with the four-part calculation
      (inline styles, ID selectors, classes/attributes/pseudo-classes,
      types/pseudo-elements), a worked comparison, the ID-versus-class-count
      rule, and source-order tie-breaking — placed before the section's
      existing content rather than in a new subsection, since the section
      already discusses specificity and assumed the reader knew how to
      compute it. Also notes that this standard's own conventions (single-
      class selectors) usually avoid needing the arithmetic. Sources (Vanseo
      Design, `CSS Master`, `The CSS Handbook`) added to the page's
      `== References`.

- [x] `CSS Master.pdf` Ch.7 "Conditional Rules with @supports"
      (`cssmaster.txt:8729`) and `The CSS Handbook by Flavio Copes.pdf` "Feature
      Queries" (`csshandbook.txt:4345`) cover the native `@supports` at-rule for
      feature-based progressive enhancement — the standard covers class-based
      feature detection via the `supports-` prefix (`03-class-names.adoc:203`,
      `07-modifiers.adoc:73`) but not the native `@supports` mechanism.
      Recommend adding `@supports` to the Progressive enhancement section
      (`02-principles.adoc:362`).

      **Resolved.** Closed by a new paragraph and code example in
      `02-principles.adoc`'s Progressive enhancement section, immediately
      after the vendor-prefix guidance. Shows `@supports (display: grid)`
      layered over a fallback declaration, and states when to prefer native
      `@supports` (pure-CSS enhancement) over a `supports-*` class (the same
      feature test also has to gate JavaScript behavior). Source (`CSS
      Master`) added to the page's `== References`.

- [x] `__TODO__/css3/_todo/properties.md`, `__TODO__/css3/_todo/general-style.md`
      ("vendor prefixes"), and `The CSS Handbook by Flavio Copes.pdf`
      (`csshandbook.txt:5268`) cover vendor-prefix conventions (avoid in
      production; if used, place before the standard property and document
      targeted browsers) — the standard uses vendor-prefixed properties in
      examples (`02-principles.adoc:409` `-webkit-border-image`,
      `06-components.adoc` `-webkit-animation`) without stating the convention.
      Recommend a note in `02-principles.adoc:399` (Progressive enhancement
      examples).

      **Resolved.** Closed by a new paragraph in `02-principles.adoc`,
      immediately after the `-webkit-border-image` example it documents.
      States that a vendor-prefixed property SHOULD NOT be used unless
      current browser-support data still requires it, MUST be written
      immediately before the standard property it prefixes, and SHOULD be
      accompanied by a note on which browsers still need it. Source (`The
      CSS Handbook`) added to the page's `== References`.

- [x] `__TODO__/css3/_todo/architecture.md:40-302` surveys OOCSS, BEM, SMACSS,
      and SUIT CSS (their categories, naming syntax, and rules); `CSS
      Master.pdf` Ch.2 "BEM"/"Atomic CSS" (`cssmaster.txt:2777`) adds BEM and
      Atomic CSS. The standard names these methodologies
      (`01-overview.adoc:87-93`) and lists them in References but gives no
      summary of what each prescribes, so a reader cannot compare or understand
      the standard's lineage. Recommend expanding `01-overview.adoc:87-93` into
      a brief comparative summary. (Borderline: the standard's purpose is to
      prescribe its own methodology, not survey others — flagged for the user.)

      **Declined, 2026-08-14.** TS-40's stated purpose is to prescribe its own
      methodology, not to survey alternatives; a comparative summary of
      OOCSS/BEM/SMACSS/SUIT CSS would be scope creep toward a different kind
      of document. The methodologies remain named in `01-overview.adoc:87-93`
      and linked in References, which is judged sufficient. No content
      change.

      **Closed, 2026-08-16.** The user confirmed the 2026-08-14 decline
      stands; no further action. Checkbox ticked to reflect that this item
      is finally settled, not merely deferred.

- [x] `CSS Master.pdf` Ch.4 "Choosing a Box Model with box-sizing"
      (`cssmaster.txt:3957`), `The CSS Handbook by Flavio Copes.pdf` "Normalizing
      CSS" (`csshandbook.txt:5234`), and the css-protips URL ("Use a CSS Reset" /
      "Inherit `box-sizing`") cover reset/normalize strategy and
      `box-sizing: border-box` — the standard mentions "Raw element resets" and
      `@import "reset"` (`08-filesystem.adoc:8`, `:60`) but gives no reset
      guidance or `box-sizing` recommendation. Recommend adding reset/box-sizing
      guidance to `08-filesystem.adoc:8` or `05-elements.adoc:1`.

      **Resolved.** Closed by a new paragraph and code example in
      `08-filesystem.adoc`, directly under the introductory paragraph.
      Recommends the reset style sheet set `box-sizing: border-box` on every
      element via the universal selector and `::before`/`::after`, and
      explains why this belongs in the reset rather than being redeclared per
      component. Source (`CSS Master`) added to the page's `== References`.

- [x] `__TODO__/css/0050-charset.md:10-15` prescribes the `@charset` rule
      (double quotes required, first line of the file) — the standard's
      filesystem example uses `@charset "UTF-8";` (`08-filesystem.adoc:10`) but
      does not state the formatting rule. Recommend a note at
      `08-filesystem.adoc:10`.

      **Resolved.** Closed by a new paragraph in `08-filesystem.adoc`,
      immediately after the `@charset`/`@import` code example. States that
      `@charset` MUST be the first line of the compiled style sheet, nothing
      may precede it, and it MUST be a double-quoted encoding string.

- [x] `The CSS Handbook by Flavio Copes.pdf` "Import" (`csshandbook.txt:774-781`)
      notes that `@import` must precede all other CSS (else ignored) and can take
      a media descriptor — the standard relies heavily on `@import`
      (`08-filesystem.adoc:8-19`) without stating either rule. Recommend a note
      in `08-filesystem.adoc:8-19`.

      **Resolved.** Closed by the same new paragraph in `08-filesystem.adoc`
      as the `@charset` item above. States that every `@import` MUST precede
      all other rules besides `@charset`, and shows an `@import` scoped with a
      media condition as an alternative to wrapping the imported file's own
      rules in a media query. Source (`The CSS Handbook`) added to the page's
      `== References`.

- [x] `CSS Master.pdf` Ch.7 "Don't Use device-width with Media Queries" and
      "Content-driven Media Queries" (`cssmaster.txt:8566-8570`) — the standard
      uses `min-width` rem breakpoints (`04-layout.adoc:45`,
      `05-elements.adoc:97`, with the rem tip at `:119`) but does not warn
      against `device-width` or advocate content-driven breakpoints. Recommend
      a note in `04-layout.adoc:45` or `05-elements.adoc:97`.

      **Resolved.** Closed by a new paragraph in `04-layout.adoc`, after the
      `.BANNER` media-query example it documents. States that breakpoints
      MUST use `min-width`/`max-width`, never `device-width` (which reports
      physical screen size, not rendered viewport width, and does not track
      resizing, split-screen, or zoom), and recommends choosing breakpoints
      where the content itself starts to look wrong rather than at
      device-specific round numbers. Source (`CSS Master`) already added to
      the page's `== References` by the "Modern layout primitives" item
      above.

- [x] `__TODO__/css3/_todo/cascade-control.md:1`, `The CSS Handbook by Flavio
      Copes.pdf` (`csshandbook.txt:740-766`), and the css-protips URL ("Use
      `unset` Instead of Resetting All Properties") cover the inheritance/reset
      keywords (`inherit`, `initial`, `unset`, `revert`, `all`) — the standard
      discusses resetting inherited properties extensively
      (`02-principles.adoc:71` Encapsulation, `05-elements.adoc:157`) but not the
      keyword mechanisms that achieve it. Recommend a brief note in
      `02-principles.adoc:71` or `05-elements.adoc`.

      **Resolved.** Closed by a new paragraph and code example in
      `02-principles.adoc`'s "Embrace the constraints of the cascade" section
      (placed here rather than Encapsulation, since this section is the one
      that discusses "resetting inherited styles"). Documents `inherit`,
      `initial`, `unset`, `revert`, and the `all` pseudo-property, and shows
      `all: unset` for fully isolating a component's element defaults.
      Sources (`The CSS Handbook`, css-protips) added to the page's
      `== References`.

- [x] `__TODO__/css2/_architecture.md` (the `contain`/`all` properties,
      Web Components polyfills, and CSS Modules as scoping mechanisms) and the
      Painless CSS URL (CSS-in-JS) cover alternative scoping mechanisms — the
      standard's overview claims applicability "whether … generated by a
      CSS-in-JS framework" (`README.adoc:12-14`) and mentions `@scope` and the
      Shadow DOM (`01-overview.adoc:22-34`) but does not address CSS-in-JS
      frameworks or CSS Modules. Recommend expanding `01-overview.adoc:12-34`.

      **Resolved.** Closed by a new paragraph in `01-overview.adoc`,
      immediately after the existing native-scoping (`@scope`/Shadow DOM)
      discussion it extends. States that tooling-generated scoping (CSS-in-JS,
      CSS Modules) is not a substitute for this standard's naming and
      separation-of-concerns conventions, since automatic uniqueness says
      nothing about whether a class is a layout section, component, or
      modifier — the tooling changes how the class name reaches the DOM, not
      what role it plays. The `contain`/Web Components polyfill material in
      `__TODO__/css2/_architecture.md` is not covered: `contain` is a
      performance/rendering-isolation property outside this standard's
      explicit performance exclusion (`01-overview.adoc:46-49`), and Web
      Components polyfills are legacy-browser tooling, also out of scope.
      Source (Painless CSS) added to the page's `== References`.

- [x] `__TODO__/css3/_todo/printers.md:1` and `The CSS Handbook by Flavio
      Copes.pdf` "CSS for print" (`csshandbook.txt:5346`, recommending a
      separate file loaded with `media="print"`) — the standard uses `@media
      print` in examples (`04-layout.adoc:67`, `05-elements.adoc:114`) but gives
      no dedicated print-style guidance. Recommend a note in `04-layout.adoc`
      or `05-elements.adoc:114`.

      **Resolved.** Closed by a new paragraph and code example in
      `08-filesystem.adoc`, after the `@import` media-descriptor guidance.
      Recommends a dedicated print style sheet imported with a `print` media
      condition rather than scattered `@media print` blocks, and keeps the
      existing inline `@media print` examples in `04-layout.adoc` and
      `05-elements.adoc` valid for smaller projects. Placed in the filesystem
      standard rather than `04-layout.adoc`/`05-elements.adoc` because the
      gap is about file organization, not the `@media print` syntax itself,
      which the standard already demonstrates.

- [x] `__TODO__/css2/_principles.md` (Defensive Programming section) explains
      *why* component/layout classes must not be type-qualified: type-qualifying
      raises specificity so modifier/utility classes can no longer override them
      (the `button.Button` vs `.background-midgrey` example) — the standard
      states the rule (`02-principles.adoc:188-194`) but omits the
      modifier-override rationale. Recommend adding the rationale at
      `02-principles.adoc:188`.

      **Resolved.** Closed by a new paragraph and code example immediately
      after the existing type-qualification rule in `02-principles.adoc`'s
      Defensive programming section, using the source's own `button.Button`
      versus `.background-midgrey` example. Explains that type-qualifying
      raises a selector's specificity above an unqualified modifier's, so the
      modifier can no longer reliably override the component, and refers the
      reader to this same batch's new "Specificity and !important" section
      (in `07-modifiers.adoc`) and the existing "Composition" section to
      ground the claim.

- [x] https://cssguidelin.es/#specificity ("`!important`") endorses the
      *proactive* use of `!important` on utility/helper classes that must always
      win — `.one-half { width: 50% !important; }`, `.hidden { display: none
      !important; }` — applied before any specificity problem arises, as a
      guarantee. The standard discusses `!important` (`07-modifiers.adoc:76-92`)
      but frames it narrowly as reserved for "cases where a property must not be
      overridable by the client's own style sheets" (`:88`); it does not address
      the proactive utility-class pattern where `!important` guarantees a class
      always beats project CSS. Recommend expanding the `!important` guidance at
      `07-modifiers.adoc:88` to cover the proactive utility-class case (or
      explicitly reject it). (Borderline — the standard's existing rationale
      overlaps; flagged for the user.)

      **Resolved.** Closed by a new paragraph in `07-modifiers.adoc`'s
      Specificity and !important section. Carves out a narrow exception to
      the "reserved" rule for single-purpose utility classes (`.hidden`,
      a fixed-width helper) that MUST always win as a deliberate guarantee,
      distinguishing that proactive case from ordinary modifiers, where
      `!important` remains a sign the modifier should be qualified instead.
      Judged not out-of-scope: cssguidelin.es' proactive pattern is a distinct
      case from the standard's existing "must not be overridable" rationale,
      not a restatement of it.

- [x] https://cssguidelin.es/#specificity ("Hacking Specificity") gives two
      remediation techniques for when a high-specificity selector cannot be
      refactored: self-chaining a class to double its specificity without adding
      location dependency (`.site-nav.site-nav {}`), and selecting an ID-bearing
      element via an attribute selector (`[id="foo"] {}`) to get class-level
      specificity. The standard's philosophy is to avoid specificity trouble
      entirely (shallow selectors, no IDs, avoid `!important`) but it is silent
      on what to do when an offending high-specificity ruleset cannot be removed
      (eg. third-party or legacy CSS). Recommend a note in `02-principles.adoc`
      (Defensive programming or a new subsection) on safe specificity escalation.

      **Resolved.** Closed by a new paragraph in `07-modifiers.adoc`'s
      Specificity and !important section, rather than `02-principles.adoc` as
      originally recommended — placed alongside the proactive-`!important`
      guidance above it, since both are specificity-escalation techniques
      answering the same question. Shows the self-chained class
      (`.NavBar.NavBar {}`) and the ID-by-attribute-selector
      (`[id="legacy-widget"] {}`) techniques, and frames both as remediation
      for CSS outside this standard's control, not patterns to use within a
      codebase that follows it.

## Out-of-scope

- [x] `__TODO__/css/` (terminology, charset formatting, selector/property/value
      formatting, comments, docblocks) and `__TODO__/css3/_todo/general-style.md`
      cover CSS *syntax formatting* and *comment/documentation* conventions. The
      standard explicitly excludes these (`01-overview.adoc:95-99`). Flagged for
      the user to confirm.

      **Overruled, pending a scope-broadening RFC, 2026-08-15.** The user
      wants TS-40 broadened to also cover CSS syntax formatting and to act
      as a property/technique reference (see items below with the same
      note). This is a redefinition of a published standard's stated
      scope — normally an RFC decision — but the user asked to record the
      decision now without drafting the RFC yet. Not written into any
      partial; the overview text (`01-overview.adoc`) is unchanged for
      now. Treat this as a held decision pending formal write-up.

- [x] `__TODO__/css3/_todo/` topic notes on individual properties and techniques
      — `transitions.md`, `backgrounds-and-borders.md`, `filters.md`,
      `forms-and-buttons.md`, `hiding-things.md`, `typography-and-fonts.md`,
      `units.md`, `pseudo-elements.md`, `selectors-and-specificity.md`,
      `layout-and-positioning.md` (vertical centering) — and the css-protips URL
      (`:not()`, `:empty`, `:root`, `nth-child`, lobotomized owl,
      `aspect-ratio`, `object-fit`, intrinsic-ratio boxes, margin hacks). These
      are property/technique references; the standard is an architecture
      methodology, not a property reference. Flagged for the user to confirm.

      **Overruled, pending a scope-broadening RFC, 2026-08-15.** Same
      pending scope-broadening decision as the item above.

- [x] `__TODO__/css3/_todo/performance.md` and `CSS Master.pdf` Ch.3 "Debugging
      and Optimization" (minification, CSS Lint, UnCSS, critical-path CSS,
      HTTP/2 concatenation, reflows) cover performance and tooling. The standard
      mentions "rendering speed" as a methodology benefit and covers
      shallow-selector architecture, but performance optimization and tooling
      are explicitly out-of-scope (`01-overview.adoc:46-49`).

      **Overruled, pending a scope-broadening RFC, 2026-08-15.** Same
      pending scope-broadening decision.

- [x] `CSS Master.pdf` Ch.2 "Managing Styles for Legacy Browsers" (IE
      conditional comments) is legacy-IE-specific. The standard's
      progressive-enhancement approach (`02-principles.adoc:399-414`) already
      covers the modern strategy; IE-specific techniques are out-of-scope.

      **Overruled, pending a scope-broadening RFC, 2026-08-15.** The user
      confirmed this dated/superseded IE-specific content should still be
      bundled into the same pending scope-broadening decision, rather than
      confirmed out on its own dated-content grounds.

- [x] The Painless CSS URL's Mistake #9 (SEO / semantic HTML) is covered by
      TS-39 (HTML) and TS-19 (SEO), not TS-40. Mistakes #2 and #1 (reading
      documentation, learning CSS systematically) are meta/learning advice.

      **Confirmed out-of-scope.** 2026-08-15. Duplicate of TS-39/TS-19
      coverage, plus generic learning advice; nothing to add.

- [x] `__TODO__/css2/_todo-styleguide.md` and `CSS Master.pdf` Ch.2 "Pattern
      Libraries" cover living style guides, pattern libraries, and
      style-guide-driven development. The overview explicitly states "A web
      design methodology is not a visual style guide or UI pattern library"
      (`01-overview.adoc:45-49`); workflow is also excluded.

      **Overruled, routed to TS-18, 2026-08-15.** The user agreed this
      doesn't belong in TS-40 but should live in TS-18 (Web GUIs) instead
      of being dropped. Filed as a new Missing item in TS-18's `GAPS.md`.

- [x] `__TODO__/css/5000-architecture/` (one-word element names, double-dash
      `--` modifiers, two-word component names, app-namespace prefixes) and
      `__TODO__/css2/_conventions.md` (special-character class names like
      `OFF_CANVAS/BANNER`) are an *alternative, unadopted* methodology whose
      naming heuristics partly contradict the standard's own examples (eg.
      `Logo`, `Card`, `Box`). Treated as not adopted rather than as gaps;
      flagged for the user to overrule if any heuristic (e.g. an app-namespace
      prefix for components shared across apps) is wanted.

      **Overruled, 2026-08-15.** The user asked specifically for the
      app-namespace-prefix heuristic (for components shared across apps)
      to be adopted. Filed as a new Missing item below, to be written up
      via `close-gaps`; a concrete, scoped addition, not part of the
      pending scope-broadening RFC.

- [x] https://cssguidelin.es/#syntax-and-formatting (Multiple Files, Table of
      Contents, 80 Characters Wide, Titling, Anatomy of a Ruleset, Indenting,
      Meaningful Whitespace, HTML quoting/multiclass grouping) and the entire
      https://github.com/necolas/idiomatic-css (whitespace, comments, ruleset
      format, declaration order) cover CSS *syntax formatting* and *commenting*.
      TS-40 explicitly excludes these (`01-overview.adoc:95-99`).

      **Overruled, pending a scope-broadening RFC, 2026-08-15.** Same
      pending scope-broadening decision as the syntax-formatting item
      above.

- [x] https://github.com/anthonyshort/idiomatic-sass from "Naming Conventions"
      onward (Selectors, Properties, Ordering, Nesting, Indentation, File
      Structure, Functions, Mixins, Modules/Packages, Namespacing, Load Paths,
      Bower package management) is Sass-specific *tooling and preprocessor
      workflow*. TS-40 excludes tooling (`01-overview.adoc:45-49`) and states it
      applies equally to plain CSS or Sass (`01-overview.adoc:101-102`).

      **Overruled, pending a scope-broadening RFC, 2026-08-15.** Same
      pending scope-broadening decision.

- [x] https://cssguidelin.es/#css-selectors "Selector Performance" (browsers
      read selectors right-to-left; the key selector; descendant vs. child
      selector cost) and idiomatic-sass' nesting-depth-as-performance notes
      cover CSS selector *performance mechanics*. Performance optimisation and
      tooling are out-of-scope (`01-overview.adoc:46-49`); cssguidelin.es itself
      says selector performance "should be fairly low on your list of things to
      optimise."

      **Overruled, pending a scope-broadening RFC, 2026-08-15.** Same
      pending scope-broadening decision.

- [x] https://cssguidelin.es/#naming-conventions (BEM `__`/`--` syntax, hyphen-
      delimited-only, no camelCase), https://github.com/anthonyshort/idiomatic-sass
      "Naming Conventions" (BEM, Montage `namespace-BlockName-childName`), and
      http://rscss.io/ (two-word dashed component names; one-word elements;
      dash-prefixed `-variant` names; underscore-prefixed `_helper` names) are
      *alternative naming methodologies*. TS-40 names BEM, SMACSS, SUIT CSS, and
      OOCSS in its overview (`01-overview.adoc:87-93`) and references, and
      prescribes its own conventions (CamelCase components, parent-prefixed
      lower-case modifiers, `UPPER_CASE` layout). TS-40 explicitly rejects the
      leading-dash modifier form (`07-modifiers.adoc:7-8`). Alternative
      conventions are not gaps; flagged for the user to overrule if any specific
      heuristic (e.g. a `js-` hook prefix, which cssguidelin.es advocates over
      TS-40's `data-*` approach at `03-class-names.adoc:171-183`) is wanted.

      **Overruled, 2026-08-15.** The user asked specifically for the
      `js-` hook-prefix convention to be adopted alongside/instead of the
      current `data-*` JS-hook approach. Filed as a new Missing item
      below, to be written up via `close-gaps`; a concrete, scoped
      addition, not part of the pending scope-broadening RFC.

- [x] https://cssguidelin.es/#css-selectors "Quasi-Qualified Selectors"
      (`/*ul*/.nav`) and "Naming UI Components" (`data-ui-component` attribute)
      are *formatting/annotation techniques* for signalling a class's intended
      context. TS-40 addresses the same concerns via defensive type-qualification
      (`02-principles.adoc:166-194`) and abstract naming
      (`03-class-names.adoc:212-231`); the commented-out and attribute-based
      variants are formatting/annotation conventions, out-of-scope.

      **Overruled, pending a scope-broadening RFC, 2026-08-15.** Same
      pending scope-broadening decision.

## Unresolved

- [x] None. All reference resources were retrieved.

  - *Run 1:* The two PDFs are binary but were readable via `pdftotext`
    (`/tmp/cssmaster.txt`, `/tmp/csshandbook.txt` — temporary extraction files,
    not part of the project). The three `.URL` bookmarks were fetched
    successfully.

  - *Run 2:* All four issue-#64 URLs were fetched successfully.
    https://cssguidelin.es/ returned the full single-page document.
    https://github.com/anthonyshort/idiomatic-sass and
    https://github.com/necolas/idiomatic-css returned their README content via
    GitHub's rendered page. The rscss resource is offline; it was retrieved from
    the Web Archive snapshot, with the main content pages (components, elements,
    variants, nested-components, layouts, helpers, css-structure, pitfalls)
    fetched individually from the archived `rscss.io` site.