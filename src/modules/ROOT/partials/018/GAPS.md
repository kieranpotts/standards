# TS-18 gap analysis

Gaps found comparing TS-18: Web GUIs against the following reference
resources:

- `__TODO__/018/web-clients/` (draft "web client design" material, `index.md` + `_todo/`)
- `__TODO__/018/web-clients-2/7000-security/` (web client security: XSRF, MITM, XSS, bearer auth)
- `__TODO__/018/web-clients/_todo/*.URL` (five web resources, fetched):
  - https://webstyleguide.com/ — Web Style Guide (Lynch & Horton)
  - https://stephaniewalter.design/blog/the-ultimate-guide-to-not-fck-up-push-notifications/
  - https://csswizardry.com/2019/08/time-to-first-byte-what-it-is-and-why-it-matters/
  - https://www.bramstein.com/writing/web-font-loading-patterns.html
  - https://w3ctag.github.io/design-principles/ — W3C TAG Web Platform Design Principles
- https://ricostacruz.com/rsjs/ (rsjs — "Reasonable System for JavaScript
  Structure"; relocated from TS-36's gap analysis as web-client JS-structure
  material)
- GitHub issue https://github.com/kieranpotts/standards/issues/61 ("Web UIs"),
  expanded into its eight listed URLs:
  - https://expressionstatement.com/html-form-validation-is-heavily-underused
  - https://css-tricks.com/tooltip-best-practices/
  - https://www.youtube.com/watch?v=-Ln-8QM8KhQ (already in TS-18 references)
  - https://web.dev/articles/top-cwv
  - https://vercel.com/blog/how-vercel-adopted-microfrontends
  - https://frontendmasters.com/blog/patterns-for-memory-efficient-dom-manipulation/
  - https://neurodiversity.design/
  - https://csswizardry.com/2024/12/a-layered-approach-to-speculation-rules/

**Assessment.** TS-18 is narrow: it covers three pillars — performance
optimization, WCAG 2.2 accessibility at Level AA, and web font handling. The
`__TODO__` references are far broader (a draft web-client-engineering book
plus a security tree plus five external resources). Most of the reference
material therefore falls outside TS-18's three stated pillars and is recorded
as out-of-scope below. Within the three pillars, the genuine gaps are a
handful of performance topics the standard omits entirely (TTFB, script
loading, progressive-enhancement baseline, HTTP/2), several accessibility
implementation details the standard asserts only at success-criterion level
(skip-link implementation, `<track>`/VTT, `<fieldset>`, `<noscript>`, valid
markup), and a set of JS-based font-loading patterns from the Bram Stein
reference that the standard does not address. Font coverage is otherwise
strong; accessibility coverage is strong at the criterion level but thin on
implementation guidance. The issue-#61 resources add performance gaps around Core Web Vitals (INP, bfcache, Speculation Rules, layout-inducing animations), tooltip and native-form-validation implementation guidance, a set of memory-efficient DOM-manipulation patterns for the proposed JS-behaviors section, and a cognitive-accessibility gap the standard's own framing invites.

**Status:** Third run (2026-08-05). The second run added the RSJS reference
  and relocated its web-client JS-structure items here from TS-36's gap
  analysis (at the maintainer's direction — web-client JS structure belongs in
  TS-18 rather than TS-37). This effectively expands TS-18's scope beyond its
  current three pillars; the architecture-leaning items also border on TS-5
  (application architecture). Flagged for the maintainer to confirm the scope
  expansion. This third run adds the eight resources listed in GitHub issue
  #61. The standard's `.adoc` files have not changed since the second run, so
  all previously-open gaps remain open; the new issue-#61 gaps are appended
  below. No gaps checked off yet.

**Fourth run, 2026-08-06.** Re-run against Brandur Leppka's "Implementing
Stripe-like Idempotency Keys in Postgres" (https://brandur.org/idempotency-keys),
section "Beyond APIs". One point was routed to TS-18: double form submission
prevention via a hidden idempotency-key input. It is Missing — TS-18 has no
form-submission-integrity guidance (only a WCAG confirm-before-consequential-
action rule and pointer-release activation, which address different problems).
One new Missing gap added; all prior gaps remain open.

**Fifth run, 2026-08-14.** Four CSS layout/typography items (fluid `clamp()`
typography, container queries, intrinsic flex/grid layouts, `text-wrap:
balance`/`ch`) relocated here from TS-37's gap analysis (`../037/GAPS.md`) on
the maintainer's scope confirmation that this material belongs in TS-18
rather than TS-37. All four added as new Missing items; no gaps checked off
in this run. All prior gaps remain open.

**Sixth run (`close-gaps`), 2026-08-14.** 59 of 60 actionable items (44 of 45
Missing, all 15 Partial) closed in one run, across expansions to the three
existing partials (`01-performance-optimization.adoc`,
`02-web-accessibility.adoc`, `03-fonts.adoc`) plus two new partials —
`04-javascript-behaviors.adoc` (component-behavior conventions, memory-
efficient DOM manipulation, and form-submission integrity) and
`05-css-layout-and-typography.adoc` (fluid typography, container queries,
intrinsic layouts, readable measure) — inserted before the existing
references partial, which was renumbered from `04-references.adoc` to
`06-references.adoc` to make room. One Missing item
(neurodiversity.design) was deliberately left open: its own note already
flagged that only a thin landing page was ever retrieved, and that remains
true — re-fetching the per-principle pages is a precondition for writing
real content, not something this run could responsibly fabricate around.

This run was conducted jointly with a `close-gaps` run against TS-15 (User
interfaces), on the user's request, specifically to catch gaps that would be
better routed between the two standards. None were found in either
direction: every TS-18 gap closed here is web-implementation-specific
(HTTP/CSS/DOM/WCAG mechanics with concrete markup, headers, or CSS
properties), and every TS-15 gap closed in that companion run is a
platform-agnostic HCI/UX principle (Nielsen heuristics, Laws of UX) that
applies equally to a CLI or a native app. The two standards' new content
does cross-reference each other in several places — TS-18's response-time
material points to TS-15's thresholds rather than repeating them, and
TS-18's error-message-attribute guidance points to TS-15's error-message
wording conventions — but no gap item itself needed to move.

Several closed items carry a scope flag inherited from earlier runs (the
rsjs component-behavior items and the form-submission-integrity item note
they border TS-5 (application architecture) or expand TS-18 beyond its
original three pillars). None of those flags were resolved in this run;
they are restated in the run summary reported to the user, for the user to
confirm or overrule, consistent with how this file has always treated a
scope call as the user's decision rather than the gap-closing agent's.

**Seventh run (`close-gaps`), 2026-08-15.** The one Missing item left open
by the sixth run — neurodiversity.design — was closed. All eight
per-principle pages (Font, Typography, Colour, Buttons/Links/Inputs,
Interface, Numbers, Animations, Communications) retrieved successfully on
re-fetch, closing both this item and its paired Unresolved entry. Closed by
a new "5. Neurodiversity" section in `02-web-accessibility.adoc`. TS-18 now
has 0 actionable items; 26 Out-of-scope and 5 Unresolved items remain open,
none of them actioned in this run.

**Eighth run (`gap-analysis`), 2026-08-15.** Worked the five remaining
Unresolved items. The five binary PDFs were extracted with `pdftotext` and
skimmed — four yielded no actionable gap (dated tooling/architecture books,
or content thinner than an already-tracked item); one (*Real Life Responsive
Web Design*, a Smashing Book anthology) yielded two genuine new Missing
items from its Responsive Images and SVG chapters. The three "empty stub"
`.md` files were re-read directly and confirmed genuinely empty/near-empty
(two 0-byte files, one heading-only placeholder) — the prior
characterization was accurate. The webstyleguide.com root item was
partially actioned: its separately-fetched Images chapter
(`/11-images.html`) is now tracked as its own Missing item; the root item
itself stays open for its other unassessed chapters. The YouTube video was
re-attempted via `WebFetch` (one retry, as instructed) and again returned
only footer/nav chrome — re-confirmed unfetchable, dismissed. Three new
Missing items added; three Unresolved items resolved/re-confirmed, one
partially actioned, one (webstyleguide.com root) left open. TS-18 now has 3
actionable items (all Missing), 26 Out-of-scope, and 1 open Unresolved item
(the webstyleguide.com root chapters not yet assessed).

**Ninth run (`close-gaps`), 2026-08-15.** All 3 remaining Missing items
closed: a new "Images" section in `01-performance-optimization.adoc`
(format selection plus `srcset`/`sizes`/`<picture>` responsive-image
markup), and a new inline-SVG-accessibility bullet in
`02-web-accessibility.adoc`'s "1. Perceivable" > *Text alternatives*
(`<title>`/`<desc>`/`role="img"`/`aria-labelledby`), cross-linked from
`03-fonts.adoc`'s icon-fonts bullet. webstyleguide.com's Images chapter and
both Smashing Book chapters (re-verified via `pdftotext`) fed the content;
the Yoav Weiss chapter's own `w`/`x`/`sizes` syntax detail was not present
in this extraction, so that portion was written from the stable HTML
Living Standard specification instead. TS-18 now has 0 actionable items.
26 Out-of-scope items and 1 Unresolved item (webstyleguide.com's other
chapters) remain open — neither actioned in this run.

**Tenth run (`close-gaps`), 2026-08-15.** 8 of the 9 Missing items added by
the previous day's Out-of-scope sweep were closed, across three new
partials and edits to two existing ones. New partials:
`07-responsive-design.adoc` (mobile-first methodology, content-based/`rem`
breakpoints, the viewport meta tag), `08-push-notifications.adoc`
(permission-request timing, the double-permission anti-pattern, user
control), and `09-browser-support.adoc` (market-share support policy plus
feature detection/polyfilling, combined into one partial since both answer
"which environments must this GUI work in, and how"). `06-references.adoc`
was renumbered to `10-references.adoc` to make room, using `git mv`; the
page's include list was rebuilt accordingly. Existing-partial edits: a new
"Profiling" section and a "Structured data" subsection in
`01-performance-optimization.adoc` and `02-web-accessibility.adoc`
respectively (the TS-39-routed RDFa item), a new "Pattern libraries and
living style guides" section in `04-javascript-behaviors.adoc` (the
TS-40-routed item), and the AA-as-floor reframing plus a new "Beyond Level
AA" section in `02-web-accessibility.adoc` covering the three named AAA
stretch items. The one remaining Missing item (DOM/scripting/fetch/CORS,
`__TODO__/018/web-clients/_todo/dom.md` and siblings) was left open at the
user's direction, since it is explicitly flagged as needing a TS-18-vs-
TS-37 placement decision before writing, to avoid duplicating content
across both standards. Two Out-of-scope-originated items (Windows app
design, Shopify Polaris) were also deferred at the user's direction — both
need an assessment of what content is actually web-implementation-relevant
before writing, not just transcription. TS-18 now has 2 actionable items
(both Missing, both deferred as above), 26 Out-of-scope items, and 1
Unresolved item — none of the last two categories actioned in this run.

**Eleventh run (`close-gaps`), 2026-08-16.** All 3 remaining Missing items
closed, resuming work deferred by the tenth run pending user decisions that
have now been made. The DOM/scripting/fetch/CORS item was split between
TS-18 (component-behavior conventions, in a new "DOM interaction
conventions" section of `04-javascript-behaviors.adoc`) and TS-37 — Web
platform APIs (raw event/fetch/CORS mechanics, in a new
`06-dom-events-and-http-requests.adoc` partial there), cross-linked both
ways; see the item's own resolution note for the full breakdown of what
went where and what was deliberately left unwritten as dated or
out-of-scope. The Windows app design item was confirmed out-of-scope after
fetching the (redirected) source and finding only a thin landing page with
no web-transferable content. The Shopify Polaris item was resolved: its own
site is now a thin navigation hub (Polaris React is archived as of this
run), but its archived token-reference page yielded a generalizable
design-token naming convention, written into `04-javascript-behaviors.adoc`
alongside the existing pattern-library guidance. TS-18 now has 0 actionable
items. 26 Out-of-scope items and 1 Unresolved item remain open — neither
actioned in this run.

## Missing

- [x] https://csswizardry.com/2019/08/time-to-first-byte-what-it-is-and-why-it-matters/#what-is-ttfb — Time to First Byte (TTFB) as a performance metric and its contributors (latency, routing, application runtime, DB queries, SSR cost). TS-18 mentions LCP but never TTFB. Recommend a new subsection in `01-performance-optimization.adoc` after the LCP note (~L53). Reinforced by https://web.dev/articles/top-cwv#3-use-a-cdn-to-optimize-ttfb, which frames TTFB as CDN-optimizable and additionally recommends caching static HTML at the edge (even briefly) and moving dynamic logic to edge compute — TS-18's CDN/Squid bullets (L31-34) cover CDN and proxy caching but not edge-cached HTML or edge compute.

      **Resolved.** Closed by `01-performance-optimization.adoc`, new "Time
      to First Byte" section: the four contributors, plus edge-cached HTML
      and edge compute added to the CDN bullet. Source added to
      `06-references.adoc`.

- [x] https://csswizardry.com/2019/08/time-to-first-byte-what-it-is-and-why-it-matters/#demystifying-ttfb — the `Server-Timing` HTTP response header as a way to surface server-side timing breakdowns to the front end. Not addressed anywhere in the standard. Recommend a new subsection in `01-performance-optimization.adoc`.

      **Resolved.** Closed by the same "Time to First Byte" section's
      `Server-Timing` bullet.

- [x] `__TODO__/018/web-clients/_todo/loading-and-bundling.md:29` — HTTP/2 multiplexing and HTTP/2 Server Push as asset-delivery strategies that reduce round trips and enable per-browser polyfill pushing. TS-18 does not mention HTTP/2 or Server Push. Recommend a new subsection in `01-performance-optimization.adoc`.

      **Resolved.** Closed by `01-performance-optimization.adoc`, new
      "HTTP/2 and asset delivery" section, covering multiplexing and the
      bundling-vs-native-modules trade-off. Server Push itself is not
      recommended — it has been removed from Chrome and deprecated across
      major browsers since this gap was recorded — so the section
      recommends native HTTP/2 multiplexing instead; this is a deliberate
      correction of the original source's advice to reflect current browser
      support, not an oversight.

- [x] `__TODO__/018/web-clients/_todo/0200-progressive-enhancement.md:102` — `<script>` loading strategy: placing scripts before `</body>`, the `defer` and `async` attributes, and ordering scripts after stylesheets. TS-18 covers code splitting/lazy loading but not script-element loading attributes. Recommend a new subsection in `01-performance-optimization.adoc`.

      **Resolved.** Closed by `01-performance-optimization.adoc`, new
      "Script loading" section: end-of-body/`defer` placement, `defer` vs.
      `async`, and script-after-stylesheet ordering.

- [x] `__TODO__/018/web-clients/_todo/principles.md:19` and `__TODO__/018/web-clients/_todo/dom.md:5` — the cost of DOM reflows and repaints, and the guidance to prefer CSS animations over JavaScript-driven animations (and to animate unstyled containers when JS is unavoidable). Not addressed. Recommend a new subsection in `01-performance-optimization.adoc`.

      **Resolved.** Closed by `01-performance-optimization.adoc`, new
      "Reflows, repaints, and layout thrashing" section: preferring CSS
      animation, and animating an unstyled wrapper when JS-driven animation
      is unavoidable.

- [x] `__TODO__/018/web-clients/_todo/dom.md:65` (Best practices) — event delegation (attaching one listener to a parent rather than many to children) to reduce total listener count and improve performance. Not addressed. Recommend a new subsection in `01-performance-optimization.adoc`. Reinforced by https://frontendmasters.com/blog/patterns-for-memory-efficient-dom-manipulation/#use-event-delegation-to-bind-fewer-events.

      **Resolved.** Closed by the same section's event-delegation bullet,
      cross-linked to "JavaScript behaviors" for the component-scoped
      application of the same technique.

- [x] `__TODO__/018/web-clients/_todo/0300-accessibility.md:199` (Valid, Semantic Markup) — the requirement that HTML markup be valid, validated with the W3C Markup Validation Service. TS-18's "Robust" principle says to use semantic HTML and ARIA but never requires valid markup as a baseline. Recommend placing at `02-web-accessibility.adoc` under "4. Robust" (~L210).

      **Resolved.** Closed by a new bullet in `02-web-accessibility.adoc`,
      "1. Perceivable" > *Adaptable*, requiring valid markup per the W3C
      Markup Validation Service and cross-linking to "4. Robust". (Placed
      under *Adaptable* rather than *Robust* itself, since that is where the
      standard's other structural-markup requirements already live; the
      bullet cross-links "4. Robust" for the assistive-technology
      consequence the original item's rationale describes.)

- [x] `__TODO__/018/web-clients/_todo/0200-progressive-enhancement.md:38` and `:96` — `<noscript>` guidance: use it only to surface messages when content genuinely cannot work without JS; do not use it to fork the experience. TS-18 does not mention `<noscript>` at all. Recommend a new subsection in `02-web-accessibility.adoc` (or a progressive-enhancement section in `01-performance-optimization.adoc`).

      **Resolved.** Closed by a new bullet in `02-web-accessibility.adoc`,
      "3. Understandable" > *Predictable*, cross-linked to the
      progressive-enhancement framing in "Performance optimization" (see
      the Partial item below for that framing itself).

- [x] `__TODO__/018/web-clients/_todo/0300-accessibility.md:240` (Navigation) — the `<link rel="index|next|prev|contents">` head elements for document-level navigation metadata. Not addressed in TS-18's "Navigable" guidance. Recommend placing at `02-web-accessibility.adoc` under "2. Operable" (~L121).

      **Resolved.** Closed by a new bullet under "2. Operable" > *Navigable*
      in `02-web-accessibility.adoc`.

- [x] https://www.bramstein.com/writing/web-font-loading-patterns.html#prioritised-loading — prioritised/sequential font loading (load a small primary font first, then a larger secondary font, with the secondary gated on the primary succeeding). TS-18 mentions preloading only above-the-fold subsets, not staged/dependent loading. Recommend a new subsection in `03-fonts.adoc` under "Loading strategy" (~L46).

      **Resolved.** Closed by a new bullet in `03-fonts.adoc`, "Loading
      strategy" section, stating the prioritised/sequential pattern. Source
      added to `06-references.adoc`.

- [x] https://www.bramstein.com/writing/web-font-loading-patterns.html#optimise-for-caching — the sessionStorage cache-state pattern: record that fonts have loaded so repeat page views render the custom font immediately (avoiding FOUT on navigation). Not addressed. Recommend a new subsection in `03-fonts.adoc` under "Loading strategy".

      **Resolved.** Closed by the same section's `sessionStorage` bullet.

- [x] https://www.bramstein.com/writing/web-font-loading-patterns.html#basic-font-loading — JavaScript-based font loaders (e.g. Font Face Observer) and the patterns built on them (basic, grouped, timeout-raced loading). TS-18 relies entirely on native `font-display`/preload and does not cover JS loader patterns. Note these predate `font-display` and are largely superseded, but the reference presents them. Recommend a new subsection in `03-fonts.adoc` (flag as a legacy alternative).

      **Resolved.** Closed by expanding the `font-display` bullet in
      `03-fonts.adoc` (see the FOIT/FOUT Partial item below), which folds in
      the Font Face Observer / class-toggling pattern as an explicitly
      flagged legacy alternative, rather than a separate subsection — the
      two are one continuous explanation of the same FOIT/FOUT problem.

The following items were relocated from TS-36's gap analysis (rsjs). They are
recorded as missing on the maintainer's scope call that web-client JS structure
belongs in TS-18. They would all sit in a proposed new section/file
(`05-javascript-behaviors.adoc` or similar), since TS-18 currently has no
JavaScript-behavior content. The architecture-leaning ones also border on TS-5
(application architecture) — flagged for the maintainer to confirm.

Note: rsjs's event-delegation point (`#use-event-delegation`) is not
re-listed here — it is already tracked as missing above (from the
`web-clients` reference, performance angle).

- [x] https://ricostacruz.com/rsjs/#think-in-component-behaviors — the
      "component behavior" pattern: a piece of JavaScript affects exactly one
      DOM subtree (a component), kept in its own behavior file. TS-18 has no
      guidance on how client-side JavaScript is organized around GUI
      components. Recommend a new section (proposed
      `05-javascript-behaviors.adoc`). Borders on TS-5 (application
      architecture) — flagged.

      **Resolved.** Closed by a new `04-javascript-behaviors.adoc` partial
      (numbered 04, not the originally-proposed 05, to keep the standard's
      partials contiguous — see the run summary), "Component behaviors"
      section, "Think in component behaviors" bullet. The TS-5 border flag
      is noted for the user in this run's summary rather than resolved
      silently; the content stayed in TS-18 per the maintainer's prior scope
      call recorded in this file's run history above.

- [x] https://ricostacruz.com/rsjs/#one-component-per-file — one self-contained
      behavior file per component, kept in a `behaviors/` directory and named
      after its selector. TS-18 does not address front-end behavior file
      organization. Recommend a new section (proposed
      `05-javascript-behaviors.adoc`). Borders on TS-5 — flagged.

      **Resolved.** Closed by the same section's "One behavior file per
      component" bullet.

- [x] https://ricostacruz.com/rsjs/#load-components-in-all-pages — the strategy
      of concatenating all behaviors into one main bundle that is safe to load
      on every page (because each behavior is localized to its selector), so
      behaviors are reusable across pages without per-page script includes.
      TS-18 does not address this loading strategy. Recommend a new section
      (proposed `05-javascript-behaviors.adoc`); the performance angle also
      touches `01-performance-optimization.adoc`. Borders on TS-5 — flagged.

      **Resolved.** Closed by the same section's "Load all behaviors on
      every page" bullet, cross-linked to the code-splitting guidance in
      "Performance optimization" for when the bundle grows large enough to
      need it instead.

- [x] https://ricostacruz.com/rsjs/#use-a-data-attribute — the convention of
      marking components and their inner hooks with `data-js-___` attributes
      (rather than classes or IDs) to disambiguate JavaScript hooks from CSS
      styling hooks. TS-18 has no selector/hook convention guidance. Recommend
      a new section (proposed `05-javascript-behaviors.adoc`).

      **Resolved.** Closed by the same section's `data-js-*` bullet.

- [x] https://ricostacruz.com/rsjs/#dont-overload-class-names — where classes
      are used for JS hooks, prefix them with `js-` and do not attach JS
      behaviors to classes that carry styles, so restyling does not break
      behavior and the source of a behavior is obvious. TS-18 does not address
      the JS/CSS hook separation. Recommend a new section (proposed
      `05-javascript-behaviors.adoc`).

      **Resolved.** Closed by the same bullet as the `data-js-*` item above
      (they were written together as one bullet on the hook convention).

- [x] https://ricostacruz.com/rsjs/#use-document-ready — binding behaviors
      inside the `DOMContentLoaded` (document-ready) handler so the target
      element is guaranteed to exist. TS-18 has no DOM-lifecycle guidance for
      behavior initialization. Recommend a new section (proposed
      `05-javascript-behaviors.adoc`).

      **Resolved.** Closed by the "Bind on document-ready, and guard against
      absence" bullet in "Component behaviors".

- [x] https://ricostacruz.com/rsjs/#avoid-side-effects — bailing out early
      (e.g. `if (!$nav.length) return;`) when a behavior's target element is
      absent from the page, so the behavior has no effect and throws no error
      on pages that do not use it. TS-18 has no guidance on this DOM-presence
      guard. Recommend a new section (proposed `05-javascript-behaviors.adoc`).

      **Resolved.** Closed by the same bullet as the document-ready item
      above (the guard is part of the same bullet).

- [x] https://ricostacruz.com/rsjs/#dynamic-content — re-running behavior
      initialization on dynamically-injected DOM (AJAX modals, etc.) with an
      idempotent include-guard pattern so already-initialized elements are
      skipped. TS-18 has no guidance on binding behaviors to dynamic content.
      Recommend a new section (proposed `05-javascript-behaviors.adoc`).

      **Resolved.** Closed by the "Re-initialize behaviors bound to dynamic
      content" bullet in "Component behaviors".

- [x] https://ricostacruz.com/rsjs/#organize-your-helpers — placing
      cross-behavior reusable functions in a `helpers/` directory and a shared
      namespace. TS-18 does not address front-end utility organization.
      Recommend a new section (proposed `05-javascript-behaviors.adoc`).
      Borders on TS-5 — flagged.

      **Resolved.** Closed by the "Organize shared helpers separately"
      bullet in "Component behaviors".

- [x] https://ricostacruz.com/rsjs/#third-party-libraries — integrating
      third-party scripts (select2, WOW.js, etc.) as component behaviors bound
      to dedicated hooks, so they follow the same localization rules as
      first-party behaviors. TS-18 has no guidance on third-party script
      integration into the GUI. Recommend a new section (proposed
      `05-javascript-behaviors.adoc`). Borders on TS-5 — flagged.

      **Resolved.** Closed by the "Integrate third-party scripts as
      behaviors too" bullet in "Component behaviors". Source (rsjs) added to
      `06-references.adoc`.

The following items are from the resources listed in GitHub issue #61
(https://github.com/kieranpotts/standards/issues/61). The DOM-manipulation and
JS-behavior items would sit in the proposed `05-javascript-behaviors.adoc`
section (see the rsjs items above); the performance items sit in
`01-performance-optimization.adoc`; the form-validation item sits in
`02-web-accessibility.adoc`.

- [x] https://expressionstatement.com/html-form-validation-is-heavily-underused — native HTML form validation (the constraint validation API): the `required` attribute, `type="email"`/`"number"`/`"url"`, `pattern`, `maxlength`, and the `setCustomValidity` DOM method for custom/async validation. TS-18's "Input assistance" requires labels, error identification in text, and error suggestions, but never names the native validation attributes/methods that deliver them. Missing. Recommend placing at `02-web-accessibility.adoc` under "3. Understandable" > Input assistance (~L191).

      **Resolved.** Closed by a new bullet in `02-web-accessibility.adoc`,
      "3. Understandable" > *Input assistance*, naming the constraint
      validation API and `setCustomValidity()`, cross-linked to TS-15's
      "Error messages" and TS-21 for HTTP-level validation. Source added to
      `06-references.adoc`.

- [x] https://web.dev/articles/top-cwv#inp — Interaction to Next Paint (INP) as a Core Web Vital and the technique of yielding to the main thread to break up long tasks (the Scheduler API and `scheduler.yield()`). TS-18 never mentions INP or long-task breaking. Missing. Recommend a new subsection in `01-performance-optimization.adoc`.

      **Resolved.** Closed by `01-performance-optimization.adoc`, new
      "Interaction responsiveness" section: INP as a Core Web Vital and
      `scheduler.yield()` task-breaking.

- [x] https://web.dev/articles/top-cwv#3-avoid-large-rendering-updates — forced layout and layout thrashing: reorganize DOM reads and writes in JavaScript to avoid interleaving layout reads with mutating writes, and keep DOM size small (large DOMs make layout recalculation expensive). TS-18 does not address layout thrashing. Missing. Recommend a new subsection in `01-performance-optimization.adoc`. (Related to the general reflow/repaint gap above, but this is the specific read/write-ordering technique.)

      **Resolved.** Closed by the same "Reflows, repaints, and layout
      thrashing" section as the general reflow/repaint gap above: the
      "Avoid layout thrashing" and "Keep the overall DOM size small"
      bullets.

- [x] https://web.dev/articles/top-cwv#3-avoid-large-rendering-updates — CSS containment (`contain`) to lazily render off-screen DOM and avoid unnecessary layout/render work. Not addressed. Missing. Recommend a new subsection in `01-performance-optimization.adoc`.

      **Resolved.** Closed by the same section's `contain` bullet.

- [x] https://web.dev/articles/top-cwv#1-ensure-the-lcp-resource-is-discoverable-from-the-html-source-and-prioritized — the `fetchpriority="high"` HTML attribute to raise the priority of the LCP image resource so it loads sooner. Not addressed. Missing. Recommend placing at `01-performance-optimization.adoc` near the preload bullet (~L19).

      **Resolved.** Closed by a new `fetchpriority="high"` bullet in
      "Rendering and asset delivery", next to the preload bullet.

- [x] https://web.dev/articles/top-cwv#1-ensure-the-lcp-resource-is-discoverable-from-the-html-source-and-prioritized — the `loading="lazy"` image attribute, and the specific guidance to remove it from the LCP image to avoid load delay. TS-18 covers lazy-loading JavaScript but not the native `loading="lazy"` image attribute. Missing. Recommend placing at `01-performance-optimization.adoc` near the image-size bullet (~L66).

      **Resolved.** Closed by a new `loading="lazy"` bullet in "Rendering
      and asset delivery", next to the image-size bullet, including the
      explicit MUST NOT on the LCP image.

- [x] https://web.dev/articles/top-cwv#2-aim-for-instant-navigations and https://web.dev/articles/top-cwv#2-ensure-pages-are-eligible-for-bfcache — the back/forward cache (bfcache): pages must meet eligibility criteria (avoid `Cache-Control: no-store`, avoid `unload` event listeners) to be restored instantly from memory on back/forward navigation, which also eliminates layout shifts. Not addressed. Missing. Recommend a new subsection in `01-performance-optimization.adoc`.

      **Resolved.** Closed by `01-performance-optimization.adoc`, new
      "Instant navigations" section, bfcache eligibility bullet.

- [x] https://csswizardry.com/2024/12/a-layered-approach-to-speculation-rules/ and https://web.dev/articles/top-cwv#2-aim-for-instant-navigations — the Speculation Rules API (`<script type="speculationrules">`): `prefetch` (pays the next page's TTFB up-front) and `prerender` (pays TTFB, FCP, and LCP up-front), with eagerness levels (`immediate`, `moderate`, `eager`), `href_matches`/`selector_matches` predicates, and an opt-in/opt-out hook pattern (e.g. `data-prefetch`, `data-prefetch=prerender`, `data-prefetch=false`) for a layered approach. TS-18 covers hover-based HTML pre-fetch (L11-17) but not the Speculation Rules API. Missing. Recommend a new subsection in `01-performance-optimization.adoc`.

      **Resolved.** Closed by the same "Instant navigations" section's
      Speculation Rules bullet: `prefetch`/`prerender`, eagerness levels,
      predicates, and the opt-in/opt-out hook pattern. Sources added to
      `06-references.adoc`.

- [x] https://csswizardry.com/2024/12/a-layered-approach-to-speculation-rules/#clearing-speculation-rules-cache-with-clear-site-data — the `Clear-Site-Data` HTTP response header extended with `prefetchCache` and `prerenderCache` directives (Chrome 138+) to forcibly purge speculative-loading caches. Not addressed. Missing. Recommend placing at `01-performance-optimization.adoc` alongside the Speculation Rules item above.

      **Resolved.** Closed by the same section's `Clear-Site-Data` bullet.

- [x] https://web.dev/articles/top-cwv#3-avoid-animations-and-transitions-that-use-layout-inducing-css-properties — never animate or transition CSS properties that require layout updates (`margin`, `border`, `top`, `left`); prefer `transform`/`translateX` so work happens on the compositor/GPU and does not cause layout shifts. TS-18 covers `prefers-reduced-motion` but not the layout-inducing-animation guidance. Missing. Recommend a new subsection in `01-performance-optimization.adoc` (the CLS angle) and/or a cross-link from `02-web-accessibility.adoc` (animations).

      **Resolved.** Closed by the "Never animate or transition a CSS
      property that requires a layout update" bullet in "Reflows, repaints,
      and layout thrashing".

- [x] https://frontendmasters.com/blog/patterns-for-memory-efficient-dom-manipulation/#prefer-hidingshowing-over-creating-new-elements — prefer hiding/showing existing (server-rendered) elements over destroying and recreating them with JavaScript, to keep the DOM mostly static and avoid garbage-collection churn. Not addressed. Missing. Recommend a new section (proposed `05-javascript-behaviors.adoc`).

      **Resolved.** Closed by `04-javascript-behaviors.adoc`,
      "Memory-efficient DOM manipulation" section, "Prefer showing and
      hiding existing elements" bullet.

- [x] https://frontendmasters.com/blog/patterns-for-memory-efficient-dom-manipulation/#prefer-textcontent-over-innertext — prefer `textContent` over `innerText` for reading element content, because `innerText` forces a reflow to account for current styles. Not addressed. Missing. Recommend a new section (proposed `05-javascript-behaviors.adoc`).

      **Resolved.** Closed by the same section's `textContent` bullet.

- [x] https://frontendmasters.com/blog/patterns-for-memory-efficient-dom-manipulation/#use-insertadjacenthtml-over-innerhtml — prefer `insertAdjacentHTML` over `innerHTML` for inserting HTML, because `innerHTML` destroys the existing DOM first. Not addressed. Missing. Recommend a new section (proposed `05-javascript-behaviors.adoc`).

      **Resolved.** Closed by the same section's `insertAdjacentHTML`
      bullet.

- [x] https://frontendmasters.com/blog/patterns-for-memory-efficient-dom-manipulation/#approach-1-use-the-template-tag — the `<template>` element plus `appendChild`/`insertAdjacentElement` as the fastest pattern for creating and inserting fully-formed DOM nodes. Not addressed. Missing. Recommend a new section (proposed `05-javascript-behaviors.adoc`).

      **Resolved.** Closed by the same section's `<template>` bullet.

- [x] https://frontendmasters.com/blog/patterns-for-memory-efficient-dom-manipulation/#approach-2-use-createdocumentfragment — `createDocumentFragment` to prepare multiple nodes and insert them in a single operation, minimizing reflows. Not addressed. Missing. Recommend a new section (proposed `05-javascript-behaviors.adoc`).

      **Resolved.** Closed by the same section's `createDocumentFragment`
      bullet.

- [x] https://frontendmasters.com/blog/patterns-for-memory-efficient-dom-manipulation/#manage-references-when-nodes-are-removed — `WeakMap` and `WeakRef` to associate data with DOM nodes so that removing a node allows the associated data to be garbage-collected rather than leaked. Not addressed. Missing. Recommend a new section (proposed `05-javascript-behaviors.adoc`).

      **Resolved.** Closed by the same section's `WeakMap`/`WeakRef` bullet.

- [x] https://frontendmasters.com/blog/patterns-for-memory-efficient-dom-manipulation/#cleaning-up-event-listeners — event-listener cleanup: `removeEventListener`, the `addEventListener` `once` option, and `AbortController` to unbind groups of listeners at once. TS-18 has no event-listener lifecycle guidance. Missing. Recommend a new section (proposed `05-javascript-behaviors.adoc`).

      **Resolved.** Closed by the same section's event-listener-cleanup
      bullet, covering `removeEventListener`, the `once` option, and
      `AbortController`. Source (frontendmasters.com) added to
      `06-references.adoc`.

- [x] https://neurodiversity.design/ — neurodiversity / cognitive-accessibility design guidance: the Neurodiversity Design System covers Font, Typography, Colour, Buttons/Links/Inputs, Interface, Communications, Numbers, and Animations for neurodivergent learners (e.g. font shapes that help dyslexic readers; typography that supports reading on screens). TS-18's opening states it covers "cognitive disabilities" and targets WCAG 2.2 Level AA, but its body provides no neurodiversity-specific guidance beyond `prefers-reduced-motion` (animations) and general colour contrast. Missing (with a scope nuance: TS-18 explicitly claims cognitive disabilities, so this is in scope; much of the NDS goes beyond WCAG AA, but TS-18's own framing invites it). Recommend a new subsection in `02-web-accessibility.adoc`. NOTE: only the NDS landing page was retrieved — see Unresolved.

      **Left open, 2026-08-14.** Not actioned in this run. As the item's
      own note flags, only the NDS landing page was ever retrieved — two
      inline snippets and a category list, not enough substantive content
      to write a section from without fabricating detail the source does
      not actually provide. Re-fetching the per-principle pages (see the
      paired Unresolved item below) is a precondition for closing this, not
      optional polish.

      **Resolved, 2026-08-15.** The eight per-principle pages (Font,
      Typography, Colour, Buttons/Links/Inputs, Interface, Numbers,
      Animations, Communications) retrieved successfully this run — the
      persistent-fetch-failure that blocked the 2026-08-14 run had cleared.
      Closed by a new "5. Neurodiversity" section appended to
      `02-web-accessibility.adoc`, after the standard's existing four WCAG
      principle sections (Perceivable/Operable/Understandable/Robust),
      since the guidance is cross-cutting and does not map cleanly onto any
      single one of the four. Covers: typeface shape and spacing for
      dyslexia (humanist sans-serif, distinct letterforms, single-storey
      a/g, line-height and letter-spacing targets); a 7:1 AAA contrast
      preference and colour-overlay themes over the standard's own 4.5:1 AA
      floor, plus consistent functional colour-coding; visually distinct
      interactive states and larger click targets (Fitts's Law); consistent
      layout with only essential elements visible, to reduce ADHD-relevant
      choice overload; numeric-input auto-formatting, digit grouping, and
      pairing bare numbers with a visual representation, for dyscalculia;
      animation bounds (at most one-third of the viewport, no parallax or
      auto-looping) to avoid triggering vestibular disorders, layered on top
      of the standard's existing `prefers-reduced-motion` requirement in
      "2. Operable" rather than replacing it; and plain, consistent,
      solution-focused written microcopy. Learner personas and LMS-specific
      UX-research content from the same site were excluded, per the
      out-of-scope item below. Source added to `06-references.adoc`, citing
      the site root and naming the eight principle pages actually used.

- [x] https://www.trysmudford.com/blog/hyper-responsive-web-components/
      ("Responsive typography & space") — fluid typography via `clamp()` with
      viewport units (the Utopia approach) for type that scales smoothly
      between a minimum and maximum size across the viewport range, without
      the stepped jumps of fixed breakpoints. TS-18 has no fluid-typography
      guidance; its fonts section covers loading, fallbacks, and CLS, not
      sizing strategy. Missing. Relocated from TS-37's gap analysis
      (`../037/GAPS.md`) — the maintainer confirmed on 2026-08-14 that this
      is CSS/layout material belonging in TS-18 rather than TS-37 (Web
      platform APIs). Recommend a new subsection in `03-fonts.adoc`, or a new
      CSS-layout section if one is added to cover the sibling items below.

      **Resolved.** Closed by a new `05-css-layout-and-typography.adoc`
      partial (numbered 05 — see the run summary for the final partial
      numbering), "Fluid typography" section, with a `clamp()` code example.
      Placed in its own new CSS-layout partial, as the item itself
      anticipated, rather than folded into `03-fonts.adoc` — the four
      relocated items are cohesive enough as a group to warrant the
      dedicated section. Source added to `06-references.adoc`.

- [x] https://www.trysmudford.com/blog/hyper-responsive-web-components/
      ("Applying container-driven typography") — CSS container queries
      (`container-type: inline-size`, the `cqi` unit, `@container`) for
      sizing type and layout against a component's own container rather than
      the viewport, plus `@supports`-based progressive enhancement for
      browsers without container-query support. Not addressed anywhere in
      TS-18. Missing. Relocated from TS-37's gap analysis (`../037/GAPS.md`)
      — the maintainer confirmed on 2026-08-14 that this is CSS/layout
      material belonging in TS-18. Recommend a new CSS-layout section (see
      the sibling items below).

      **Resolved.** Closed by the same partial's "Container queries"
      section, with a `container-type`/`@container` code example and the
      `@supports` progressive-enhancement note.

- [x] https://www.trysmudford.com/blog/hyper-responsive-web-components/
      ("Intrinsic layouts" and "Limitations of intrinsic design") — the Every
      Layout "Sidebar" intrinsic flex/grid pattern (content-driven wrapping
      without explicit breakpoints) and `@container`-driven content hiding
      for when intrinsic layout alone is not enough. Not addressed anywhere
      in TS-18. Missing. Relocated from TS-37's gap analysis
      (`../037/GAPS.md`) — the maintainer confirmed on 2026-08-14 that this
      is CSS/layout material belonging in TS-18. Recommend a new CSS-layout
      section (see the sibling items above and below).

      **Resolved.** Closed by the same partial's "Intrinsic layouts"
      section, with the Sidebar flex pattern as a code example and a note
      on combining it with container queries when wrapping alone is
      insufficient.

- [x] https://www.trysmudford.com/blog/hyper-responsive-web-components/
      ("The finer details") — `text-wrap: balance` for balancing heading line
      lengths, and the `ch` unit for constraining body-text line length to a
      readable measure. Not addressed anywhere in TS-18. Missing. Relocated
      from TS-37's gap analysis (`../037/GAPS.md`) — the maintainer confirmed
      on 2026-08-14 that this is CSS/layout material belonging in TS-18.
      Recommend a new CSS-layout section (see the sibling items above); the
      four relocated items together could form one new
      `05-css-layout-and-typography.adoc` section, since TS-18 currently has
      no CSS-layout content distinct from its performance/accessibility/font
      pillars.

      **Resolved.** Closed by the same partial's "Readable measure and
      heading balance" section, covering both `ch` and `text-wrap: balance`,
      confirming the exact new-partial numbering this item anticipated (the
      partial ended up numbered 05, not 05 exactly as originally guessed but
      matching the same slot in the final page order — see the run
      summary).

- [x] https://brandur.org/idempotency-keys ("Beyond APIs") covers double
      form submission prevention, which is not addressed anywhere in the
      standard. The reference describes the technique: when rendering a
      form initially, add a hidden `<input type="hidden">` containing an
      idempotency key; this value stays the same across multiple
      submissions, and the server uses it to dedup the request — important
      when a submission has non-idempotent side effects (eg. charging the
      user) and a user clicks "Submit" twice in quick succession. TS-18 has
      no form-submission-integrity guidance: the WCAG-derived requirement
      that consequential submissions be reviewable/confirmable beforehand
      (`02-web-accessibility.adoc:199-201`) and the pointer-release
      activation guidance (`:149-151`) address different problems (informed
      consent and accidental activation), and neither covers server-side
      dedup via an idempotency key nor alternatives like disabling the
      submit button after click or POST-redirect-GET. Recommend a new
      "Form submission integrity" subsection (proposed
      `05-javascript-behaviors.adoc` or a new forms section) covering
      double-submit prevention. Note: the client-side hidden-input technique
      is squarely a web-GUI concern; the server-side dedup half overlaps
      TS-21 (HTTP APIs) — see the idempotency-key entries in
      `../021/GAPS.md`. Flagged: TS-18's current pillars are performance,
      accessibility, and fonts, so form-integrity is a scope expansion (but
      form handling is a core web-GUI concern).

      **Resolved.** Closed by `04-javascript-behaviors.adoc`, "Form
      submission integrity" section: the hidden-input idempotency-key
      pattern, cross-linked to TS-21's "Safeness and idempotency" for the
      server-side half, plus the submit-button-disable and
      POST-redirect-GET complements. Source added to `06-references.adoc`.
      The scope-expansion flag is noted for the user in this run's summary;
      the content stayed in TS-18 since form handling is squarely a web-GUI
      concern on the client side, consistent with how the rsjs items above
      were resolved.

- [x] https://webstyleguide.com/11-images.html — the Web Style Guide's Images chapter (Lynch & Horton) covers image-format selection (GIF/JPEG/PNG/SVG use cases and trade-offs), compression trade-offs, and alt-text conventions. Not currently in TS-18: the standard requires text alternatives (`02-web-accessibility.adoc`, "Text alternatives") but gives no format-selection guidance for images at all. Recommend a new subsection, likely in `01-performance-optimization.adoc` (format choice affects payload) or a new "Images" section alongside fonts. Content not yet written — this item records the gap only; see the two related Missing items below (`srcset`/`sizes`/`<picture>` and SVG accessibility) for adjacent image-markup gaps found independently in the same run.

      **Resolved.** Closed by a new "Images" section in
      `01-performance-optimization.adoc`, opening with format selection:
      JPEG for photographs, PNG preferred over GIF for line art/logos, and
      SVG for icons and simple vector shapes, plus a note to test formats
      empirically. Cross-linked to <<Icon fonts>> and the accessibility
      text-alternative requirements. Source added to `06-references.adoc`.

- [x] `__TODO__/018/web-clients/_todo/Real Life Responsive Web Design (Smashing Book).pdf`, Chapter 7 "Responsive Images" (Yoav Weiss) — the `srcset`/`sizes` responsive-image markup (`w` descriptors for variable-width images, `x` descriptors for fixed-width/DPR-only cases, the `sizes` attribute for telling the browser an image's expected display width) and the `<picture>`/`<source>` element for *art direction* (serving genuinely different crops/images per breakpoint, as opposed to the same image at different quality levels). TS-18 mentions `srcset` only in passing, once, as part of the `data-src`-anti-pattern bullet in "Rendering and asset delivery" (`01-performance-optimization.adoc`) — it never explains the `w`/`x`/`sizes` syntax or the `<picture>` art-direction pattern at all. Recommend a new subsection in `01-performance-optimization.adoc`, near the existing image-sizing bullets, or folded into whatever new "Images" section results from the webstyleguide.com/11-images.html item above.

      **Resolved.** Closed by the same new "Images" section: `w` descriptors
      with `sizes` for variable-width images, `x` descriptors for
      fixed-display-size images needing only resolution variants, and
      `<picture>`/`<source>` reserved for art direction (a genuinely
      different image per breakpoint) versus `srcset`/`sizes` for
      resolution-only variation. The PDF's own chapter text (re-checked via
      `pdftotext`) confirmed the `<picture>`-for-art-direction distinction
      and deferred the `w`/`x`/`sizes` syntax detail to Yoav Weiss's own
      chapter, which this extraction did not capture in full; that syntax
      is stable, well-documented HTML Living Standard behavior, so it was
      written from the platform specification rather than the PDF extract.
      Sources (both book chapters) added to `06-references.adoc`.

- [x] `__TODO__/018/web-clients/_todo/Real Life Responsive Web Design (Smashing Book).pdf`, Chapter 4 "Mastering SVG for Responsive Web Design" (Sara Soueidan) — SVG accessibility: the `<title>` and `<desc>` elements as an SVG image's text alternative (analogous to `alt` on `<img>`), and the `role="img"` plus `aria-labelledby` pattern to work around inconsistent browser/screen-reader support for SVG 1.1's native accessibility elements. TS-18 recommends inline SVGs/SVG sprites in place of icon fonts (`03-fonts.adoc`, "Icon fonts") specifically for their accessibility benefit, but never states how to actually make an SVG accessible — the `<title>`/`<desc>`/ARIA markup itself. Recommend a new bullet or subsection in `02-web-accessibility.adoc`, "1. Perceivable" > *Text alternatives*, cross-linked from the icon-fonts bullet in `03-fonts.adoc`.

      **Resolved.** Closed by a new bullet in `02-web-accessibility.adoc`,
      "1. Perceivable" > *Text alternatives*. Requires `<title>` (and
      `<desc>` for longer explanations) as an inline SVG's text
      alternative, plus `role="img"`/`aria-labelledby` to work around
      inconsistent SVG 1.1 accessibility support, with the caution to omit
      `role="img"` where the SVG contains an interactive element. Verified
      against the PDF's own worked example. Cross-linked from the
      icon-fonts bullet in `03-fonts.adoc`. Source added to
      `06-references.adoc`.

- [x] `__TODO__/039/html/_todo/semantic-web.md:1` (routed in from TS-39's
      Out-of-scope review, 2026-08-15) — "Semantic Web" background (RDF,
      RDF/XML, RDF Schema, OWL) and its actionable web-client subset: how
      to actually markup a page with RDFa/structured data as a GUI
      implementation concern (the vocabulary/syntax mechanics, not just
      the choice of schema). TS-39 judged the general RDF/OWL background
      out of its own HTML-authoring scope; the user directed it be routed
      to TS-18 rather than dropped, since it's a web-client implementation
      topic. Add a cross-reference from TS-19 (SEO), since structured
      data/RDFa markup is largely consumed by search engines. Not yet
      written into any partial.

      **Resolved.** Closed by a new "Structured data" subsection in
      `02-web-accessibility.adoc`, "4. Robust". Recommends schema.org
      vocabulary in JSON-LD over RDFa/Microdata (a self-contained block
      rather than markup-threaded attributes), and cross-links TS-19 (SEO)
      for how the markup affects search-result presentation, plus notes
      why the mechanics live here rather than in TS-19: it is markup that
      lives in the page the GUI renders. RDF/OWL's general background
      (outside the actionable web-client subset) was not written up —
      TS-39's routing note scoped this item to the markup mechanics only.

- [x] `__TODO__/css2/_todo-styleguide.md` and `CSS Master.pdf` Ch.2
      "Pattern Libraries" (routed in from TS-40's Out-of-scope review,
      2026-08-15) — living style guides, pattern libraries, and
      style-guide-driven development. TS-40 (CSS) explicitly states it is
      not a visual style guide or UI pattern library, and workflow is
      also outside its scope; the user agreed this doesn't belong in
      TS-40 but should live in TS-18 (Web GUIs) rather than being
      dropped. Not yet checked against TS-18's current content or written
      into any partial.

      **Resolved.** Closed by a new "Pattern libraries and living style
      guides" section in `04-javascript-behaviors.adoc`, placed alongside
      the component-behavior conventions since a pattern library catalogs
      the same components those conventions organize. Covers building the
      library from the application's own component markup/styles rather
      than hand-copied examples, documenting component states and
      variants, and using it as the canonical check before building a new
      component. `CSS Master.pdf` was not re-extracted for this run — the
      `__TODO__/css2/_todo-styleguide.md` source and the routing note's
      own summary were sufficient to write the section without
      fabricating detail beyond what was already recorded.

- [x] https://developer.microsoft.com/en-us/windows/apps/design (routed in
      from TS-15's Out-of-scope review, 2026-08-15) — Windows-specific app
      design (UWP/WinUI foundations, input types, form factors). TS-15
      (User interfaces) judged this platform-specific and out of its own
      general-principles scope; the user felt it may have a place in
      TS-18 instead. Not yet checked against TS-18's current content or
      written into any partial — needs assessment for what, if anything,
      is web-implementation-relevant versus purely Windows-native.

      **Confirmed out-of-scope, 2026-08-16.** Fetched: the URL redirects to
      `https://learn.microsoft.com/windows/uwp/design/`, which is a thin
      landing page (128 words) linking out to Fluent Design's own
      UWP/WinUI-native design-principles, guidelines, and toolkit pages. It
      carries no content of its own — no HTML/CSS/JS technique, design
      token, or accessibility guidance that is web-implementation-relevant
      independent of the Fluent/XAML tooling it's written for. The
      assessment the item asked for found nothing to route to TS-18;
      genuinely nothing here transfers to a web GUI.

- [x] https://polaris.shopify.com/ (routed in from TS-15's Out-of-scope
      review, 2026-08-15) — Shopify Polaris's design-system mechanics:
      design tokens, coded component packaging, commerce-domain
      iconography. TS-15 judged this design-system implementation detail
      rather than general interface principles; the user agreed it fits
      TS-18 (web-implementation-specific) better. Not yet checked against
      TS-18's current content or written into any partial.

      **Resolved, 2026-08-16.** `polaris.shopify.com` and
      `shopify.dev/docs/api/polaris` are both thin navigation hubs with no
      substantive content of their own (Polaris React itself is archived as
      of August 2026, superseded by "Polaris Web Components"). The
      generally-applicable mechanic was found instead at the archived
      token-reference page,
      `shopify.github.io/polaris-react-archive/tokens/color`: a
      hierarchical, semantic design-token naming scheme
      (`--p-color-bg-fill-brand-hover` — category/subcategory/semantic-
      intent/state) mapped to CSS custom properties. Closed by a new bullet
      in `04-javascript-behaviors.adoc`, "Pattern libraries and living
      style guides", generalizing the naming scheme past Polaris itself.
      Commerce-domain content (checkout components, commerce iconography,
      admin/POS/customer-account surfaces) was not written up — it is
      Shopify-specific, not a web-GUI-implementation mechanic. Source added
      to `10-references.adoc`.

- [x] https://stephaniewalter.design/blog/the-ultimate-guide-to-not-fck-up-push-notifications/
      (moved from Out-of-scope, overruled 2026-08-15) — push-notification
      UX: do not request permission on page load, ask in context, avoid
      the "double permission" pattern, timing/precision/personalization,
      user control and opt-out. Originally judged a distinct feature
      topic outside TS-18's three stated pillars; the user overruled that
      and asked for a new notifications section. Recommend a new section,
      most likely its own partial given how self-contained the topic is.
      Not yet written into any partial.

      **Resolved.** Closed by a new `08-push-notifications.adoc` partial:
      no permission request on page load, asking in context, the
      double-permission anti-pattern, explaining what/how-often before
      requesting, relevance/precision of timing, and discoverable
      opt-out. Source added to `10-references.adoc`.

- [x] `__TODO__/018/web-clients/_todo/responsive-design.md` (moved from
      Out-of-scope, overruled 2026-08-15) — responsive design methodology:
      mobile-first, `min-width` media queries, content-based breakpoints,
      the viewport `<meta>` tag, rem-based breakpoints, container queries.
      TS-18's accessibility section already covers reflow at 320px and
      orientation, but not the broader methodology. The user asked for a
      new section. Recommend a new partial, since this is a substantial,
      coherent topic of its own. Not yet written into any partial.

      **Resolved.** Closed by a new `07-responsive-design.adoc` partial:
      mobile-first with `min-width` media queries, content-based
      breakpoints (not device-specific ones), `rem`-based breakpoints, a
      cross-link to container queries for component-level responsiveness,
      and the viewport `<meta>` tag. Cross-links the existing 320px reflow
      requirement in <<1. Perceivable>> rather than repeating it.

- [x] `__TODO__/018/web-clients/_todo/browsers.md` (moved from
      Out-of-scope, overruled 2026-08-15) — browser/device support policy:
      a market-share threshold (e.g. 1%), supporting the last two major
      versions of each supported browser, not testing pre-release betas.
      Originally judged as testing/support policy belonging to TS-14/
      TS-15; the user overruled that and asked for it to be kept in
      TS-18. Recommend a new section, e.g. alongside or near the
      accessibility/browser-support content. Not yet written into any
      partial.

      **Resolved.** Closed by the "Browser support policy" subsection of
      a new `09-browser-support.adoc` partial: a market-share (~1%)
      threshold measured from the application's own traffic, the last-
      two-major-versions rule, and the prohibition on testing against
      pre-release betas.

- [x] `__TODO__/018/web-clients/_todo/feature-detection.md` and
      `polyfilling.md` (moved from Out-of-scope, overruled 2026-08-15) —
      feature detection vs. user-agent detection, CSS feature detection
      (`@supports`), and dynamic polyfilling strategy. Originally judged
      an implementation technique outside the three stated pillars; the
      user overruled that and asked for it to be kept in TS-18. Recommend
      a new section, likely near the progressive-enhancement content in
      `01-performance-optimization.adoc`. Not yet written into any
      partial.

      **Resolved.** Closed by the "Feature detection and polyfilling"
      subsection of the new `09-browser-support.adoc` partial (placed
      alongside browser support policy rather than in
      `01-performance-optimization.adoc`, since both are the same
      "which environments must this GUI work in, and how" concern):
      feature detection over user-agent sniffing, `@supports` for CSS
      (with a cross-link to <<Container queries>> as a worked example),
      dynamic/conditional polyfill loading, and preferring a Baseline
      platform feature over a polyfill where support allows.

- [x] `__TODO__/018/web-clients/_todo/dom.md`, `dom2.md`, `scripting.md`,
      `window-events.md`, `web-client-apis.md`, `fetch-ajax.md` (moved
      from Out-of-scope, overruled 2026-08-15) — DOM manipulation, event
      handling, scripting patterns, XHR/`fetch`, and CORS implementation
      details. The user asked for this to be written into TS-18, but
      flagged that it may actually belong in TS-37 (Web platform APIs)
      instead, with a cross-reference from TS-18 either way — that
      placement decision is still open. Recommend resolving the TS-18-
      vs-TS-37 placement question before writing any content, to avoid
      duplicating the same material in two standards. Not yet written
      into any partial.

      **Resolved, split between TS-18 and TS-37, 2026-08-16.** The user
      decided: component-behavior conventions stay in TS-18; raw platform
      API mechanics move to TS-37. All six source files were read in full
      to determine the boundary — most of the content is a dated (2010s-era,
      IE8/9/10-compatibility-focused) dump, much of which is either already
      superseded by current platform behavior, already covered elsewhere in
      TS-18/TS-37, or too thin/obsolete to write from (`web-client-apis.md`
      in particular has no actionable content — it is a meta-commentary on
      not being able to keep up with the platform). The durable, current,
      non-duplicated subset was extracted:

      *Written into TS-18*, `04-javascript-behaviors.adoc`, new "DOM
      interaction conventions" section: restricting interactive behavior to
      semantically interactive elements (`<a>`, `<button>`, `<input>`, etc.,
      injecting a `<button>` into a non-interactive container rather than
      making the container itself interactive — from `dom.md`'s "Best
      practices"); the `onclick=`/inline-event-attribute prohibition,
      restated for the `data-js-*` hook convention already in <<Component
      behaviors>> (from `dom2.md`'s "Event attributes" and "HTML event
      attributes" sections); and preferring `requestAnimationFrame` over
      `setTimeout`/`setInterval` for the rare animation that cannot be
      expressed in CSS (from `dom2.md`'s "Animating the DOM" section,
      cross-linked to the existing CSS-animation-preferred guidance in
      <<Reflows, repaints, and layout thrashing>>). Cross-links to TS-37 for
      the underlying platform APIs. Source (WHATWG DOM Standard) added to
      `10-references.adoc`.

      *Written into TS-37* (which was already fully resolved, 0 open items,
      before this run — a separate, un-batched write against that
      standard, done at the user's explicit direction rather than routed
      through TS-37's own `close-gaps` flow, since the split decision was
      the user's to make and both halves were being written in the same
      session): new `06-dom-events-and-http-requests.adoc` partial, "Event
      propagation" (bubbling/capturing, `addEventListener`'s `useCapture`
      argument, `stopPropagation()`), "Choosing an event type" (pointer,
      keyboard, and form-element event types; the deprecated
      `keyCode`/`charCode`/`which` properties versus current
      `KeyboardEvent.key`; from `dom.md`'s "Safe events"/"Keyboard events"
      and `dom2.md`'s extensive keyboard-event material), "Observing DOM
      mutations" (`MutationObserver` replacing deprecated `MutationEvents`;
      from `dom.md`), "`fetch`" (preferred over `XMLHttpRequest`; the
      `response.ok`-must-be-checked-explicitly pitfall; the
      markup-must-never-be-fetched restriction, cross-linked to TS-18's
      progressive-enhancement framing; `FormData` for form submission
      including file uploads; from `fetch-ajax.md` and `dom2.md`'s
      `FormData`/file-upload material, rewritten from `XMLHttpRequest` to
      the current `fetch` API since XHR is legacy), and "CORS"
      (`Access-Control-Allow-Origin`, the credentials-plus-wildcard
      restriction, preflight requests; from `fetch-ajax.md`'s CORS stub,
      expanded from the current CORS specification since the stub itself
      had no content — the item was a bare `TODO`). Wired into
      `src/modules/ROOT/pages/037.adoc`; `06-references.adoc` renumbered to
      `07-references.adoc` via `git mv` to make room. Source (WHATWG DOM
      Standard, WHATWG Fetch Standard) added to TS-37's own
      `07-references.adoc`.

      Content deliberately NOT written, as dated/superseded/out of either
      standard's scope: browser-specific quirks and workarounds throughout
      all six files (Safari iOS click-bubbling bugs, `XDomainRequest`,
      `mouseenter`/`mouseleave` cross-browser gaps, IE-specific attribute
      handling) — these targeted browsers no longer in any current
      support-policy baseline (see TS-18's <<Browser support policy>>);
      `<canvas>`/WebGL/`<svg>` element introductions (already adjacent
      content — SVG accessibility — exists in TS-18's
      `02-web-accessibility.adoc`, and a from-scratch `<canvas>`/WebGL
      primer is graphics-API territory, not GUI-behavior or platform-API
      guidance either standard claims); Shadow DOM (`dom2.md` mentions it
      only in passing — already covered in full by TS-37's own
      `03-shadow-dom.adoc`); DOM-extension-via-prototype discouragement and
      `document.write` discouragement (both already dated advice about
      practices no current codebase would reach for, not omitted for scope
      reasons but because they add nothing a reader doesn't already know
      not to do); `hashchange`/`deviceorientation` window events
      (`window-events.md` — each is a single unelaborated paragraph, too
      thin to write a section from without padding); `web-client-apis.md`
      in full (pure meta-commentary, no technical content).

- [x] `__TODO__/018/web-clients/_todo/0300-accessibility.md:484` (7:1
      contrast), `:508` (sign-language tracks), and the lower-secondary
      reading-level guidance (`:159`) (reframed, overruled 2026-08-15) —
      these target WCAG Level AAA. The user asked for TS-18 to state
      Level AA as the *minimum* requirement, not the ceiling, and to also
      cover these AAA items as optional/stretch guidance above that
      floor. Recommend: (1) editing the existing AA-target statement in
      `02-web-accessibility.adoc` to frame it explicitly as a minimum;
      (2) adding a new subsection or set of bullets covering 7:1 contrast,
      sign-language tracks for video, and lower-secondary reading-level
      simplification, clearly marked as AAA-level stretch goals rather
      than the baseline requirement. Not yet written into any partial.

      **Resolved.** Closed in `02-web-accessibility.adoc`: the opening
      "Level AA is the target RECOMMENDED" statement now explicitly
      states AA as a floor, cross-linking a new "Beyond Level AA" section
      appended after "5. Neurodiversity". That section covers the three
      named AAA items as OPTIONAL stretch goals — 7:1 contrast (4.5:1 for
      large text), sign-language video tracks alongside pre-recorded
      audio content, and lower-secondary reading level for non-technical
      content — each cross-linked to the related AA/neurodiversity
      guidance it builds on rather than duplicating it.

- [x] https://frontendmasters.com/blog/patterns-for-memory-efficient-dom-manipulation/#profiling-debugging
      (moved from Out-of-scope, overruled 2026-08-15) — the Chrome
      DevTools Memory-tab (heap snapshots) and Performance-tab (JavaScript
      execution timeline, rendering/painting) profiling workflow.
      Originally judged testing/process material belonging to TS-14/
      TS-15; the user overruled that and asked for it to be kept in
      TS-18. Recommend a new section, e.g. in
      `01-performance-optimization.adoc`, covering the profiling workflow
      as a practical diagnostic technique. Not yet written into any
      partial.

      **Resolved.** Closed by a new "Profiling" section in
      `01-performance-optimization.adoc`, before "Reflows, repaints, and
      layout thrashing": the Performance tab's timeline for confirming a
      suspected bottleneck, and the Memory tab's heap-snapshot comparison
      technique for finding a leak, cross-linked to the
      `WeakMap`/`WeakRef`/listener-cleanup patterns in
      <<Memory-efficient DOM manipulation>> as the most common fix.
      Reuses the existing frontendmasters.com reference entry (annotation
      updated) rather than adding a duplicate.

## Partial

- [x] `__TODO__/018/web-clients/_todo/0200-progressive-enhancement.md:7` and `:86` — progressive enhancement as the framing for performance: serve a static baseline that works without JS/CSS, then layer enhancements. TS-18 says "server-render as much HTML as possible" but does not require the no-JS baseline or the progressive-enhancement model, and never states that anything requiring JS must be injected by JS. Recommend strengthening `01-performance-optimization.adoc` L7-9 (server-render bullet) and cross-linking to accessibility.

      **Resolved.** Closed by a new paragraph in `01-performance-optimization.adoc`'s
      introduction, naming the progressive-enhancement model explicitly and
      stating anything requiring JavaScript MUST be injected by JavaScript.
      Cross-linked from the new `<noscript>` bullet in
      `02-web-accessibility.adoc`.

- [x] `__TODO__/018/web-clients/_todo/loading-and-bundling.md:4` — module bundling vs. module loading as a strategy (bundling for HTTP/1.x, native modules for HTTP/2; trade-offs of cache invalidation granularity and mobile bandwidth). TS-18 mentions "code splitting" but not the broader bundling-vs-loading decision or its HTTP/2 interaction. Recommend expanding `01-performance-optimization.adoc` L57-61 (code splitting bullet).

      **Resolved.** Closed by the new "HTTP/2 and asset delivery" section
      (the bundling-vs-native-modules trade-off) plus a cross-link from the
      code-splitting bullet, distinguishing code splitting (what to serve)
      from module bundling (how it is packaged).

- [x] `__TODO__/018/web-clients/_todo/0300-accessibility.md:240` (Enable "skip to content") — full implementation pattern for the skip link (visibly-on-focus, first tabbable link, paired "jump back to top" link, code sample). TS-18 requires a skip-navigation mechanism but gives no implementation guidance. Recommend expanding `02-web-accessibility.adoc` L121-123 (Navigable intro).

      **Resolved.** Closed by a new bullet and HTML code example in
      `02-web-accessibility.adoc`, "2. Operable" > *Navigable*: first
      focusable, visible-on-focus, paired "back to top" link.

- [x] `__TODO__/018/web-clients/_todo/0300-accessibility.md:240` (Provide context) — breadcrumbs, sitemaps, and current-location indication within navigation. TS-18 requires consistent navigation and two ways to locate pages but does not mention breadcrumbs or current-location indicators. Recommend placing at `02-web-accessibility.adoc` under "2. Operable" (~L133).

      **Resolved.** Closed by expanding the "two methods to locate content"
      bullet with breadcrumbs and sitemap examples.

- [x] `__TODO__/018/web-clients/_todo/0300-accessibility.md:360` and `:408` — grouping long forms with `<fieldset>`/`<legend>` for assistive-tech navigation. TS-18 requires descriptive labels but does not mention fieldset grouping. Recommend expanding `02-web-accessibility.adoc` L191 (Input assistance / form labels).

      **Resolved.** Closed by expanding the form-labels bullet in "3.
      Understandable" > *Input assistance* with the `<fieldset>`/`<legend>`
      grouping requirement.

- [x] `__TODO__/018/web-clients/_todo/0300-accessibility.md:414` — time-limit adjustment detail: warn users at least 20 seconds before expiry and offer a simple one-action extension. TS-18 says users must be able to turn off / adjust to 10x / extend on request, but does not specify the 20-second warning. Recommend expanding `02-web-accessibility.adoc` L105-108 (Enough time).

      **Resolved.** Closed by expanding the time-limit bullet in "2.
      Operable" > *Enough time* with the 20-second warning and one-action
      extension requirement.

- [x] `__TODO__/018/web-clients/_todo/0300-accessibility.md:427` (Multimedia) — the `<track>` element and VTT format for captions, transcripts, and audio descriptions, with code samples. TS-18 requires captions/transcripts/audio-descriptions as outcomes but does not name the `<track>` element or VTT. Recommend expanding `02-web-accessibility.adoc` L29-35 (Time-based media).

      **Resolved.** Closed by a new bullet and HTML `<video>`/`<track>` code
      example in "1. Perceivable" > *Time-based media*.

- [x] `__TODO__/018/web-clients/_todo/0300-accessibility.md:460` — media and interactive content (including games) should be paused by default. TS-18 covers pausable auto-playing audio but not pause-by-default for video/games. Recommend expanding `02-web-accessibility.adoc` L63-64 (Distinguishable / audio).

      **Resolved.** Closed by expanding the auto-playing-audio bullet in "1.
      Perceivable" > *Distinguishable* with the pause-by-default requirement
      for video and interactive content/games.

- [x] `__TODO__/018/web-clients/_todo/0300-accessibility.md:51` (ARIA) — specific ARIA landmark roles (`banner`, `navigation`, `main`) and `aria-label` for naming navigation regions. TS-18 mentions ARIA generally but does not name landmarks. Recommend expanding `02-web-accessibility.adoc` L222-223 (Robust / semantic HTML + ARIA).

      **Resolved.** Closed by expanding the semantic-HTML/ARIA bullet in "4.
      Robust" > *Compatible* with the `banner`/`navigation`/`main` landmark
      roles and the multi-nav `aria-label` requirement.

- [x] https://www.bramstein.com/writing/web-font-loading-patterns.html#custom-font-display — the FOIT (Flash of Invisible Text) vs. FOUT (Flash of Unstyled Text) mechanism, and the JS-based class-toggling FOUT pattern. TS-18 says `font-display: swap` "prevents invisible text" but does not explain the FOIT/FOUT behaviour it is preventing. Recommend expanding `03-fonts.adoc` L66-71 (font-display bullet).

      **Resolved.** Closed by expanding the `font-display` bullet in
      `03-fonts.adoc` with the FOIT/FOUT explanation and the legacy Font
      Face Observer class-toggling pattern.

- [x] https://www.bramstein.com/writing/web-font-loading-patterns.html#loading-groups-of-fonts — grouped font loading (load a whole family together via `Promise.all`) to avoid faux styles and collapse multiple reflows into one. TS-18 discusses CLS/fallback tuning but not grouped loading to reduce reflows. Recommend expanding `03-fonts.adoc` L83-87 (Fallbacks).

      **Resolved.** Closed by a new bullet in `03-fonts.adoc`'s "Loading
      strategy" section (placed alongside the other loading-strategy
      content rather than under "Fallbacks", since grouped loading is a
      loading-order decision, not a fallback-metrics one).

The following Partial items are from the resources listed in GitHub issue #61.

- [x] https://css-tricks.com/tooltip-best-practices/ — tooltip implementation patterns: tooltips are text-only non-interactive popovers (use a `dialog` for interactive content); label an icon tooltip with `aria-labelledby` and provide a contextual description with `aria-describedby`; use `role="tooltip"`; do not use the `title` attribute; do not combine `aria-haspopup` with `role="tooltip"`; open on hover/focus and close on mouseout/blur; tooltips are inaccessible on touch devices (prefer visible labels); use a toggletip (`<button>` + `role="status"` live region) for informational popups. TS-18 asserts the WCAG 1.4.13 outcome (dismissible via Escape, hoverable, persistent) at `02-web-accessibility.adoc` L84-86 but gives none of this implementation guidance. Partial. Recommend expanding `02-web-accessibility.adoc` L84-86.

      **Resolved.** Closed by expanding the tooltip bullet in "1.
      Perceivable" > *Distinguishable* with the full implementation
      guidance: `dialog` vs. tooltip, `aria-labelledby`/`aria-describedby`,
      `role="tooltip"`, the `title`-attribute and `aria-haspopup`
      prohibitions, touch inaccessibility, and the toggletip pattern.
      Source added to `06-references.adoc`.

- [x] https://web.dev/articles/top-cwv#2-avoid-unnecessary-javascript — the broader guidance to minimize JavaScript shipped: prefer Baseline widely-available platform features over JS reimplementations, use the Chrome DevTools coverage tool to find unused code, and periodically prune tag-manager tags. TS-18 covers code splitting and lazy loading (L57-64) but frames JS only as "serve only the subset required" rather than the broader minimize-JS / remove-unused-code message. Partial. Recommend expanding `01-performance-optimization.adoc` L57-61.

      **Resolved.** Closed by the "Minimize the JavaScript actually shipped"
      bullet in the new "Script loading" section: Baseline platform
      features, the DevTools coverage tool, and tag-manager pruning.

- [x] https://web.dev/articles/top-cwv#1-ensure-the-lcp-resource-is-discoverable-from-the-html-source-and-prioritized — LCP image discoverability: use `<img src>`/`srcset` (not `data-src` which requires JS); prefer SSR over CSR so the image markup is in the HTML source; preload the LCP image with `<link rel="preload">` if it must be referenced from CSS/JS. TS-18 recommends server-rendering (L7-9) and preloading (L19-22) but does not address the `data-src` anti-pattern or the image-specific discoverability guidance. Partial. Recommend expanding `01-performance-optimization.adoc` L19-22 and L7-9.

      **Resolved.** Closed by expanding the server-render bullet
      (`data-src` anti-pattern, SSR-over-CSR for LCP images) and the
      preload bullet (preloading the LCP resource when it must be
      referenced from CSS/JS) in "Rendering and asset delivery".

- [x] https://web.dev/articles/top-cwv#1-set-explicit-sizes-on-any-content-loaded-from-the-page — the `aspect-ratio` CSS property (Baseline widely available) to reserve space for images and non-image elements with a dynamic width, and `min-height` as a fallback to reduce layout-shift severity for dynamic content of unknown size. TS-18 covers fixed `width`/`height` on images (L66-70) but not `aspect-ratio` or `min-height`. Partial. Recommend expanding `01-performance-optimization.adoc` L66-70.

      **Resolved.** Closed by expanding the image-sizing bullet in
      "Rendering and asset delivery" with `aspect-ratio` and the
      `min-height` fallback.

## Out-of-scope

- [x] `__TODO__/018/web-clients-2/7000-security/200-xsrf.md` (Cross-site request forgery) — XSRF mechanisms (synchronizer token, double-submit token, JSON obfuscation, session expiry, re-authentication). Flagged: TS-18's stated pillars are performance, accessibility, and fonts; web client security is not among them, though a `7000-security/` tree exists in `__TODO__`, suggesting the maintainers may intend to add it. Confirm whether security belongs in TS-18 or a separate standard.

      **Overruled, pending a scope-broadening decision, 2026-08-15.** The
      user wants web-client security added as a fourth pillar to TS-18,
      alongside performance, accessibility, and fonts. This is a scope
      redefinition of a published standard; the user asked to record the
      decision without formalizing it (via RFC or an overview-text edit)
      yet. Bundled with the three items below (MITM, XSS, Bearer auth) —
      same pending security-pillar decision.

- [x] `__TODO__/018/web-clients-2/7000-security/300-mitm.md` (Man-in-the-middle) — HTTPS everywhere, `Secure` cookie flag, securing logs/dumps/backups. Flagged for the same scope reason as XSRF.

      **Overruled, pending a scope-broadening decision, 2026-08-15.** Same
      pending security-pillar decision as XSRF above.

- [x] `__TODO__/018/web-clients-2/7000-security/400-xss.md` (Cross-site scripting) — input sanitization, output escaping, `HttpOnly` cookies, avoiding web storage for session data, third-party/CDN script risk. Flagged for the same scope reason as XSRF.

      **Overruled, pending a scope-broadening decision, 2026-08-15.** Same
      pending security-pillar decision.

- [x] `__TODO__/018/web-clients-2/7000-security/700-bearer-auth.md` (Bearer auth) — token storage trade-offs (memory vs. cookie vs. session/local storage), `HttpOnly` tokens, refresh tokens, revocation, same-origin API proxies. Flagged for the same scope reason as XSRF.

      **Overruled, pending a scope-broadening decision, 2026-08-15.** Same
      pending security-pillar decision.

- [x] https://stephaniewalter.design/blog/the-ultimate-guide-to-not-fck-up-push-notifications/ — push-notification UX (do not request permission on page load; ask in context; the "double permission" pattern; timing/precision/personalization; user control and opt-out). Flagged: push notifications are a distinct feature topic, not one of TS-18's three pillars. Confirm whether to add a notifications section to TS-18.

      **Overruled, 2026-08-15.** The user asked for a new notifications
      section to be added. Filed as a new Missing item below, to be
      written up via `close-gaps`.

- [x] `__TODO__/018/web-clients/_todo/0400-architecture.md` — web client architecture (static site, dynamic site, SPA, MPA, micro frontends, PWA, server/client logic split). Plausibly sits outside TS-18 because `AGENTS.md` defers general application architecture to TS-5. Flagged for confirmation.

      **Overruled, pending a scope-broadening decision, 2026-08-15.** The
      user wants TS-18 to cover web client architecture, reversing its
      documented deferral to TS-5. Recorded as a decision without
      formalizing it yet. Bundled with the three items below (SPA
      frameworks, PWA, microfrontends) — same pending architecture-scope
      decision.

- [x] `__TODO__/018/web-clients/_todo/single-pade-applications.md` and `application-frameworks.md` and `application-state.md` — SPA frameworks, MV* patterns, models as single source of truth, framework agnosticity. Out of scope: application architecture (TS-5).

      **Overruled, pending a scope-broadening decision, 2026-08-15.** Same
      pending architecture-scope decision as `0400-architecture.md` above.

- [x] `__TODO__/018/web-clients/_todo/responsive-design.md` — responsive design methodology (mobile-first, `min-width` media queries, content-based breakpoints, the viewport `<meta>` tag, rem-based breakpoints, container queries). Flagged: TS-18's accessibility section covers reflow at 320px and orientation, but responsive design methodology is not one of the three stated pillars. Confirm whether responsive design belongs in TS-18 (the `__TODO__` placement suggests the maintainers think it might).

      **Overruled, 2026-08-15.** The user asked for a new responsive
      design section to be added — a concrete, self-contained topic,
      unlike the broader architecture/security bundles. Filed as a new
      Missing item below, to be written up via `close-gaps`.

- [x] `__TODO__/018/web-clients/_todo/browsers.md` — browser/device support policy (1% market-share threshold, last two major versions, not testing betas). Out of scope: testing/support policy (TS-14 / TS-15).

      **Overruled, 2026-08-15.** The user asked for this to be kept in
      TS-18. Filed as a new Missing item below, to be written up via
      `close-gaps`.

- [x] `__TODO__/018/web-clients/_todo/feature-detection.md` and `polyfilling.md` — feature detection vs. user-agent detection, CSS feature detection, dynamic polyfilling. Flagged: implementation technique, not one of the three pillars. Confirm scope.

      **Overruled, 2026-08-15.** The user asked for this to be kept in
      TS-18. Filed as a new Missing item below, to be written up via
      `close-gaps`.

- [x] `__TODO__/018/web-clients/_todo/dom.md`, `dom2.md`, `scripting.md`, `window-events.md`, `web-client-apis.md`, `fetch-ajax.md` — DOM/events/scripting/XHR/CORS/web-client-API implementation details. Out of scope: low-level implementation guidance beyond TS-18's three pillars.

      **Overruled, placement undecided between TS-18 and TS-37,
      2026-08-15.** The user asked for this to be written in, but flagged
      that it may actually belong in TS-37 (Web platform APIs) instead,
      with a cross-reference from TS-18 either way. Filed as a new
      Missing item below in TS-18 pending that placement decision, and
      not yet duplicated into TS-37 to avoid double-booking the same
      content in two standards at once.

- [x] `__TODO__/018/web-clients/_todo/i18n.md` — internationalization (localization, translation, dialects, UTF-8/Unicode). Out of scope: i18n is a separate concern (likely its own standard).

      **Overruled pending a new standard, 2026-08-15.** The user decided
      internationalization warrants a dedicated new technical standard,
      not yet created. Held here rather than routed, pending that
      standard's creation.

- [x] `__TODO__/018/web-clients/_todo/seo.md` — SEO. Out of scope: TS-19 covers SEO.

      **Confirmed out-of-scope for TS-18, routed to TS-19, 2026-08-15.**
      Filed as a new item in TS-19's `GAPS.md`.

- [x] `__TODO__/018/web-clients/_todo/pwa.md` — Progressive Web Apps as a packaging/installability model. Out of scope: TS-18 already references service workers for caching; PWA as an architecture is out of scope (TS-5).

      **Overruled, pending a scope-broadening decision, 2026-08-15.** Same
      pending architecture-scope decision as `0400-architecture.md` above.

- [x] `__TODO__/018/web-clients/_todo/audits.md` — website audit / technical due-diligence checklists. Out of scope: process/auditing (TS-14 / TS-15).

      **Confirmed out-of-scope for TS-18, routed to TS-15, 2026-08-15.**
      Filed as a new item in TS-15's `GAPS.md`.

- [x] `__TODO__/018/web-clients/_todo/0300-accessibility.md:60` (Testing) — the assistive-technology test matrix (JAWS, VoiceOver, NVDA, ZoomText, Dragon) and the manual/automated accessibility audit process. Out of scope: TS-18's `AGENTS.md` states that "Accessibility testing process is covered by TS-14: Performance testing."

      **Confirmed out-of-scope for TS-18, routed to TS-14, 2026-08-15.**
      Matches TS-18's documented deferral and the earlier CI/Axe item
      routed the same way from TS-39. Filed as a new item in TS-14's
      `GAPS.md`, alongside that earlier one.

- [x] `__TODO__/018/web-clients/_todo/0300-accessibility.md:484` (7:1 contrast), `:508` (sign-language tracks), and the lower-secondary reading-level guidance (`:159`) — these target WCAG Level AAA. Out of scope: TS-18 explicitly targets Level AA.

      **Reframed, 2026-08-15.** The user asked for TS-18 to state AA as
      the *minimum* requirement while also covering AAA guidelines, not
      simply reversing the AA-only target. Filed as a new Missing item
      below — a concrete, precisely-scoped change — to be written up via
      `close-gaps`: adjust the existing AA-target statement, then add the
      three named AAA items (7:1 contrast, sign-language tracks, reading-
      level simplification) as stretch/optional guidance above the floor.

- [x] https://w3ctag.github.io/design-principles/ — the W3C TAG Web Platform Design Principles (priority of constituencies, safe-to-visit, trusted UI, user activation, feature detectability, etc.). Out of scope: this document is aimed at designers of web-platform specifications/APIs, not at builders of web GUIs.

      **Confirmed out-of-scope.** 2026-08-15.

- [x] https://webstyleguide.com/ — Web Style Guide (Lynch & Horton) covers Strategy, Research, Process, Information Architecture, Site/Page Structure, Interface Design, Graphic Design, Typography, Editorial Style, Images, and Video. Out of scope: broader UI/usability guidance (TS-15). Only the table-of-contents page was retrievable; the per-chapter content was not fetched (see Unresolved).

      **Overruled, pending a scope-broadening decision, 2026-08-15.** The
      user suggested TS-19 (SEO) could be expanded into a broader Content
      Strategy and SEO standard, which might be a better home for this
      remaining content-strategy/process material (Interface Design and
      Typography chapters were already routed to TS-15 earlier this run;
      Images was already closed against TS-18 itself). Held pending that
      decision — not fetched, not routed, not written in.

The following items were relocated from TS-36's gap analysis (rsjs). They are
out-of-scope for TS-18 because they are library-specific, jQuery-specific, or
dated tooling recipes rather than web-GUI design/implementation guidance.

- [x] https://ricostacruz.com/rsjs/#consider-using-onmount — recommending the
      `onmount` library specifically is a library/tooling recommendation for
      jQuery-era DOM lifecycles, outside TS-18's scope.

      **Confirmed out-of-scope.** 2026-08-15.

- [x] https://ricostacruz.com/rsjs/#use-each-when-needed — using `jQuery.each`
      to initialize per-element state is a jQuery-specific pattern, outside
      TS-18's scope.

      **Confirmed out-of-scope.** 2026-08-15.

- [x] https://ricostacruz.com/rsjs/#load-3rd-party-resources-asynchronously —
      async-loading external vendor scripts (e.g. Google Maps) via a helper
      that defers a global to a callback is a legacy pattern superseded by
      dynamic `import()`. The script-loading-strategy gap is already tracked
      above from the `web-clients` reference. Out of scope as a dated
      technique.

      **Confirmed out-of-scope.** 2026-08-15.

- [x] https://ricostacruz.com/rsjs/#loading-component-files — the appendix
      recipes for bulk-loading `behaviors/` via Rails Sprockets `require_tree`,
      Browserify `require-globify`, Webpack `require.context`, and Brunch
      `glob-brunch` are dated tooling recipes for concatenation pipelines,
      outside TS-18's scope.

      **Confirmed out-of-scope.** 2026-08-15.

The following Out-of-scope items are from the resources listed in GitHub
issue #61.

- [x] https://vercel.com/blog/how-vercel-adopted-microfrontends — microfrontends architecture: vertical (split-by-path) vs horizontal (split-by-feature) microfrontends, Next.js Multi-Zones, monorepo with Turborepo, and incremental migration via feature flags. Out of scope: application architecture (TS-5). This overlaps with the existing `0400-architecture.md` out-of-scope item above. The prefetch/prerender performance angle (Speculation Rules to mitigate hard navigations between microfrontends) is captured as a missing gap above.

      **Overruled, pending a scope-broadening decision, 2026-08-15.** Same
      pending architecture-scope decision as `0400-architecture.md` above.

- [x] https://frontendmasters.com/blog/patterns-for-memory-efficient-dom-manipulation/#profiling-debugging — the Chrome DevTools Memory-tab (heap snapshots) and Performance-tab (JavaScript execution timeline, rendering/painting) profiling workflow. Out of scope: testing/process (TS-14 / TS-15).

      **Overruled, 2026-08-15.** The user asked for this to be kept in
      TS-18. Filed as a new Missing item below, to be written up via
      `close-gaps`.

- [x] https://neurodiversity.design/ (Learner Personas) — neurodivergent learner personas (e.g. dyspraxia, dyslexia, ADHD) as a UX-research tool, scoped to Learning Management Systems. Out of scope: persona-based UX research and LMS-specific design (plausibly TS-15). The NDS design-principle content is captured as a missing gap above.

      **Confirmed out-of-scope for TS-18, routed to TS-15, 2026-08-15.**
      Fits alongside the new "User research" section just added to TS-15
      this run. Filed as a new item in TS-15's `GAPS.md`.

## Unresolved

- [x] https://webstyleguide.com/ — only the contents/landing page was retrieved; the individual chapters (Strategy, IA, Interface Design, Typography, Images, Video, etc.) are separate pages that were not fetched. The out-of-scope call above is based on the table of contents alone. If any chapter (especially Typography, Images, or Page Structure) should be compared in depth, re-run with those chapter URLs as explicit references.

      **Partially actioned, 2026-08-15.** The main session separately fetched
      the Images chapter, https://webstyleguide.com/11-images.html, and found
      format-selection guidance (GIF/JPEG/PNG/SVG use cases, compression
      trade-offs, alt-text conventions) not currently in TS-18. That chapter
      is now tracked as its own Missing item below. The site root item itself
      remains unresolved for its other chapters (Typography, Interface
      Design are routed to TS-15 per the maintainer; Strategy, IA, Page
      Structure, Video were not separately assessed).

      **Resolved, 2026-08-15.** Fetched and assessed all remaining chapters
      (Front Matter's table of contents confirmed the full chapter list):
      Strategy, Research, Process, Information Architecture, Site
      Structure, Page Structure, Graphic Design, Editorial Style, and
      Video. (Typography and Interface Design were already fetched and
      routed to TS-15; Images was already fetched and closed above.)

      The great majority of the remaining chapters are content-strategy,
      project-management, editorial-workflow, and video-production
      material — team assembly, project charters, card-sorting research
      method, CMS selection, social-media posting cadence, brainstorming
      technique, video equipment and interview technique — all outside
      TS-18's three declared pillars (performance, WCAG accessibility, web
      fonts) plus its JavaScript-behaviors and CSS-layout partials. This
      matches the pattern already established for TS-26's out-of-scope
      content-strategy/marketing exclusions; confirmed out-of-scope for
      the same reason, not a gap.

      A handful of technical points overlap content TS-18 (or a sibling
      standard) already covers, so no new gap: semantic HTML5 landmark
      elements and ARIA landmark roles (Site Structure, Page Structure
      chapters) are already required via `02-web-accessibility.adoc`'s
      "Use semantic HTML elements... Identify the page's major regions
      with ARIA landmark roles" guidance; responsive images via
      `srcset`/`<picture>` (Page Structure chapter) is already covered in
      full by the new <<Images>> section; descriptive link text over
      "click here" (Editorial Style chapter) is already covered by TS-26
      (Technical writing style guide), `09-links.adoc`; mobile-first
      responsive breakpoints (Page Structure chapter) is already covered
      in TS-15 (User interfaces), `01-design-principles.adoc`.

      One genuine gap was found: the Video chapter's explicit prohibition
      on video autoplay, requiring playback to be user-initiated with the
      title/description/duration available beforehand. TS-18's existing
      time-based-media guidance covers captions, transcripts, and audio
      descriptions in detail but never addressed autoplay. Closed by a
      new bullet at the start of `02-web-accessibility.adoc`'s
      "Time-based media" subsection. Source added to `06-references.adoc`.

      No further webstyleguide.com chapters remain unassessed; this item
      is now fully resolved.

- [x] The following binary PDFs in `__TODO__/018/web-clients/_todo/` were skipped silently per the gap-analysis rules (binary files are not text references): `Frontend Architecture for Design Systems.pdf`, `The Principles of Beautiful Web Design.pdf`, `Real Life Responsive Web Design (Smashing Book).pdf`, `Build Mobile Websites and Apps for Smart Devices.pdf`, `Beyond the 12 Factor App.pdf`. Not included in the comparison. If any should be treated as references, extract their text and re-run.

      **Resolved, 2026-08-15.** All five PDFs extracted with `pdftotext` and
      skimmed in full (tables of contents plus the chapters most likely to
      be relevant). Findings per book:

      - *Beyond the Twelve-Factor App* (Kevin Hoffman) — entirely backend
        cloud-application architecture (API-first design, config/credentials,
        logs, statelessness, port binding, telemetry). No web-GUI content.
        Out of scope for TS-18 (TS-5/TS-8/TS-31 territory, not assessed
        further here).

      - *Frontend Architecture for Design Systems* (Micah Godbolt) — design
        system tooling, workflow, task runners, testing/documentation
        infrastructure (Pattern Lab, style-guide generators). Process/tooling
        concerns outside TS-18's implementation-level pillars, and dated
        (2016, pre-dates current build tooling). No actionable gap found.

      - *The Principles of Beautiful Web Design* (Beaird & George) — visual
        and graphic design craft (layout composition, color theory, texture,
        typography as aesthetics, image sourcing/art direction). Its one
        technical subsection, "File Formats and Resolutions" (JPEG/GIF/PNG),
        is dated (2014, IE6/IE7 references, no WebP/AVIF/SVG guidance) and
        thinner than the already-identified webstyleguide.com/11-images.html
        gap below; not added separately to avoid duplicating that item.

      - *Build Mobile Websites and Apps for Smart Devices* (Castledine,
        Eftos, Wheeler) — 2011-era mobile web development built entirely
        around PhoneGap/Cordova native-app packaging. Obsolete tooling and
        architecture (TS-5 territory where still relevant); no actionable
        gap for TS-18's current pillars.

      - *Real Life Responsive Web Design* (Smashing Book #5) — a multi-author
        anthology; two chapters yielded genuine, current, actionable gaps not
        already in TS-18, added as new Missing items below: Yoav Weiss's
        "Responsive Images" chapter (`srcset`/`sizes`/`<picture>` markup) and
        Sara Soueidan's "Mastering SVG" chapter (SVG accessibility via
        `<title>`/`<desc>` and ARIA). Its Flexbox and offline/Application
        Cache chapters are dated (2015, pre-dating mature Service Worker
        practice and the CSS Grid/Flexbox fluency TS-18 already assumes) and
        yielded nothing beyond what TS-18 already covers.

- [x] `__TODO__/018/web-clients/_todo/encoding.md`, `modules-and-bundling.md`, and `0500-csp.md` are empty stubs (no substantive content), so no claims were extracted from them.

      **Re-confirmed, 2026-08-15.** Re-read directly rather than relying on
      the prior characterization. `encoding.md` and `modules-and-bundling.md`
      are literally 0 bytes. `0500-csp.md` contains only a single Markdown H1
      heading, `# Content Security Policy (CSP)`, with no body text — a
      title placeholder, not substantive content. The "empty stub"
      characterization was accurate for all three; no claims to extract.

- [x] https://neurodiversity.design/ — only the landing page was retrieved. The per-principle pages (Numbers, Font, Typography, Colour, Buttons/Links/Inputs, Interface, Communications, Animations) were not fetched, so the cognitive-accessibility gap above is based on the landing page's category list and two inline snippets ("the right typography can support neurodivergent learners' reading on screens"; "specific font shapes that make dyslexic readers, read better") only. Re-run with the individual principle-page URLs to compare in depth.

      **Dismissed, 2026-08-15.** All eight per-principle pages retrieved
      successfully on re-fetch (the previous run's failure did not recur).
      Content compared against TS-18 and closed as the Missing item above.

- [x] https://www.youtube.com/watch?v=-Ln-8QM8KhQ — this video is already listed in TS-18's own `04-references.adoc`. The comparison is against the creator's video description (extracted via the helper script), not a full transcript. The description's chapters (Server-Rendered HTML, Prefetching HTML, CDN Caching, Client Caching with Service Worker, Preloading Assets, Critical CSS, LCP, Fixed-Size Images, JavaScript) map almost 1-1 to TS-18's existing `01-performance-optimization.adoc` content, so no new gaps were identified from it. A full transcript was not fetched, so spoken-only details could not be verified.

      **Dismissed, 2026-08-15.** Re-attempted via `WebFetch` as instructed
      (one retry only). The page still returns only YouTube's footer/nav
      chrome (About/Press/Copyright/Contact/etc. links and the copyright
      notice) — no transcript or video description content, the same
      unfetchable result as before. This is the expected outcome: YouTube
      pages don't expose transcripts to this fetch tool. Re-confirmed
      unfetchable; not re-attempted further. The prior comparison against
      the video description stands as the best available evidence, and
      found no new gaps.