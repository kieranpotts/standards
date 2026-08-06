# TS-18 gap analysis

Gaps found comparing TS-18: Web GUIs against the following reference
resources:

- `src/018/__TODO__/web-clients/` (draft "web client design" material, `index.md` + `_todo/`)
- `src/018/__TODO__/web-clients-2/7000-security/` (web client security: XSRF, MITM, XSS, bearer auth)
- `src/018/__TODO__/web-clients/_todo/*.URL` (five web resources, fetched):
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

## Missing

- [ ] https://csswizardry.com/2019/08/time-to-first-byte-what-it-is-and-why-it-matters/#what-is-ttfb — Time to First Byte (TTFB) as a performance metric and its contributors (latency, routing, application runtime, DB queries, SSR cost). TS-18 mentions LCP but never TTFB. Recommend a new subsection in `01-performance-optimization.adoc` after the LCP note (~L53). Reinforced by https://web.dev/articles/top-cwv#3-use-a-cdn-to-optimize-ttfb, which frames TTFB as CDN-optimizable and additionally recommends caching static HTML at the edge (even briefly) and moving dynamic logic to edge compute — TS-18's CDN/Squid bullets (L31-34) cover CDN and proxy caching but not edge-cached HTML or edge compute.

- [ ] https://csswizardry.com/2019/08/time-to-first-byte-what-it-is-and-why-it-matters/#demystifying-ttfb — the `Server-Timing` HTTP response header as a way to surface server-side timing breakdowns to the front end. Not addressed anywhere in the standard. Recommend a new subsection in `01-performance-optimization.adoc`.

- [ ] `src/018/__TODO__/web-clients/_todo/loading-and-bundling.md:29` — HTTP/2 multiplexing and HTTP/2 Server Push as asset-delivery strategies that reduce round trips and enable per-browser polyfill pushing. TS-18 does not mention HTTP/2 or Server Push. Recommend a new subsection in `01-performance-optimization.adoc`.

- [ ] `src/018/__TODO__/web-clients/_todo/0200-progressive-enhancement.md:102` — `<script>` loading strategy: placing scripts before `</body>`, the `defer` and `async` attributes, and ordering scripts after stylesheets. TS-18 covers code splitting/lazy loading but not script-element loading attributes. Recommend a new subsection in `01-performance-optimization.adoc`.

- [ ] `src/018/__TODO__/web-clients/_todo/principles.md:19` and `src/018/__TODO__/web-clients/_todo/dom.md:5` — the cost of DOM reflows and repaints, and the guidance to prefer CSS animations over JavaScript-driven animations (and to animate unstyled containers when JS is unavoidable). Not addressed. Recommend a new subsection in `01-performance-optimization.adoc`.

- [ ] `src/018/__TODO__/web-clients/_todo/dom.md:65` (Best practices) — event delegation (attaching one listener to a parent rather than many to children) to reduce total listener count and improve performance. Not addressed. Recommend a new subsection in `01-performance-optimization.adoc`. Reinforced by https://frontendmasters.com/blog/patterns-for-memory-efficient-dom-manipulation/#use-event-delegation-to-bind-fewer-events.

- [ ] `src/018/__TODO__/web-clients/_todo/0300-accessibility.md:199` (Valid, Semantic Markup) — the requirement that HTML markup be valid, validated with the W3C Markup Validation Service. TS-18's "Robust" principle says to use semantic HTML and ARIA but never requires valid markup as a baseline. Recommend placing at `02-web-accessibility.adoc` under "4. Robust" (~L210).

- [ ] `src/018/__TODO__/web-clients/_todo/0200-progressive-enhancement.md:38` and `:96` — `<noscript>` guidance: use it only to surface messages when content genuinely cannot work without JS; do not use it to fork the experience. TS-18 does not mention `<noscript>` at all. Recommend a new subsection in `02-web-accessibility.adoc` (or a progressive-enhancement section in `01-performance-optimization.adoc`).

- [ ] `src/018/__TODO__/web-clients/_todo/0300-accessibility.md:240` (Navigation) — the `<link rel="index|next|prev|contents">` head elements for document-level navigation metadata. Not addressed in TS-18's "Navigable" guidance. Recommend placing at `02-web-accessibility.adoc` under "2. Operable" (~L121).

- [ ] https://www.bramstein.com/writing/web-font-loading-patterns.html#prioritised-loading — prioritised/sequential font loading (load a small primary font first, then a larger secondary font, with the secondary gated on the primary succeeding). TS-18 mentions preloading only above-the-fold subsets, not staged/dependent loading. Recommend a new subsection in `03-fonts.adoc` under "Loading strategy" (~L46).

- [ ] https://www.bramstein.com/writing/web-font-loading-patterns.html#optimise-for-caching — the sessionStorage cache-state pattern: record that fonts have loaded so repeat page views render the custom font immediately (avoiding FOUT on navigation). Not addressed. Recommend a new subsection in `03-fonts.adoc` under "Loading strategy".

- [ ] https://www.bramstein.com/writing/web-font-loading-patterns.html#basic-font-loading — JavaScript-based font loaders (e.g. Font Face Observer) and the patterns built on them (basic, grouped, timeout-raced loading). TS-18 relies entirely on native `font-display`/preload and does not cover JS loader patterns. Note these predate `font-display` and are largely superseded, but the reference presents them. Recommend a new subsection in `03-fonts.adoc` (flag as a legacy alternative).

The following items were relocated from TS-36's gap analysis (rsjs). They are
recorded as missing on the maintainer's scope call that web-client JS structure
belongs in TS-18. They would all sit in a proposed new section/file
(`05-javascript-behaviors.adoc` or similar), since TS-18 currently has no
JavaScript-behavior content. The architecture-leaning ones also border on TS-5
(application architecture) — flagged for the maintainer to confirm.

Note: rsjs's event-delegation point (`#use-event-delegation`) is not
re-listed here — it is already tracked as missing above (from the
`web-clients` reference, performance angle).

- [ ] https://ricostacruz.com/rsjs/#think-in-component-behaviors — the
      "component behavior" pattern: a piece of JavaScript affects exactly one
      DOM subtree (a component), kept in its own behavior file. TS-18 has no
      guidance on how client-side JavaScript is organized around GUI
      components. Recommend a new section (proposed
      `05-javascript-behaviors.adoc`). Borders on TS-5 (application
      architecture) — flagged.

- [ ] https://ricostacruz.com/rsjs/#one-component-per-file — one self-contained
      behavior file per component, kept in a `behaviors/` directory and named
      after its selector. TS-18 does not address front-end behavior file
      organization. Recommend a new section (proposed
      `05-javascript-behaviors.adoc`). Borders on TS-5 — flagged.

- [ ] https://ricostacruz.com/rsjs/#load-components-in-all-pages — the strategy
      of concatenating all behaviors into one main bundle that is safe to load
      on every page (because each behavior is localized to its selector), so
      behaviors are reusable across pages without per-page script includes.
      TS-18 does not address this loading strategy. Recommend a new section
      (proposed `05-javascript-behaviors.adoc`); the performance angle also
      touches `01-performance-optimization.adoc`. Borders on TS-5 — flagged.

- [ ] https://ricostacruz.com/rsjs/#use-a-data-attribute — the convention of
      marking components and their inner hooks with `data-js-___` attributes
      (rather than classes or IDs) to disambiguate JavaScript hooks from CSS
      styling hooks. TS-18 has no selector/hook convention guidance. Recommend
      a new section (proposed `05-javascript-behaviors.adoc`).

- [ ] https://ricostacruz.com/rsjs/#dont-overload-class-names — where classes
      are used for JS hooks, prefix them with `js-` and do not attach JS
      behaviors to classes that carry styles, so restyling does not break
      behavior and the source of a behavior is obvious. TS-18 does not address
      the JS/CSS hook separation. Recommend a new section (proposed
      `05-javascript-behaviors.adoc`).

- [ ] https://ricostacruz.com/rsjs/#use-document-ready — binding behaviors
      inside the `DOMContentLoaded` (document-ready) handler so the target
      element is guaranteed to exist. TS-18 has no DOM-lifecycle guidance for
      behavior initialization. Recommend a new section (proposed
      `05-javascript-behaviors.adoc`).

- [ ] https://ricostacruz.com/rsjs/#avoid-side-effects — bailing out early
      (e.g. `if (!$nav.length) return;`) when a behavior's target element is
      absent from the page, so the behavior has no effect and throws no error
      on pages that do not use it. TS-18 has no guidance on this DOM-presence
      guard. Recommend a new section (proposed `05-javascript-behaviors.adoc`).

- [ ] https://ricostacruz.com/rsjs/#dynamic-content — re-running behavior
      initialization on dynamically-injected DOM (AJAX modals, etc.) with an
      idempotent include-guard pattern so already-initialized elements are
      skipped. TS-18 has no guidance on binding behaviors to dynamic content.
      Recommend a new section (proposed `05-javascript-behaviors.adoc`).

- [ ] https://ricostacruz.com/rsjs/#organize-your-helpers — placing
      cross-behavior reusable functions in a `helpers/` directory and a shared
      namespace. TS-18 does not address front-end utility organization.
      Recommend a new section (proposed `05-javascript-behaviors.adoc`).
      Borders on TS-5 — flagged.

- [ ] https://ricostacruz.com/rsjs/#third-party-libraries — integrating
      third-party scripts (select2, WOW.js, etc.) as component behaviors bound
      to dedicated hooks, so they follow the same localization rules as
      first-party behaviors. TS-18 has no guidance on third-party script
      integration into the GUI. Recommend a new section (proposed
      `05-javascript-behaviors.adoc`). Borders on TS-5 — flagged.

The following items are from the resources listed in GitHub issue #61
(https://github.com/kieranpotts/standards/issues/61). The DOM-manipulation and
JS-behavior items would sit in the proposed `05-javascript-behaviors.adoc`
section (see the rsjs items above); the performance items sit in
`01-performance-optimization.adoc`; the form-validation item sits in
`02-web-accessibility.adoc`.

- [ ] https://expressionstatement.com/html-form-validation-is-heavily-underused — native HTML form validation (the constraint validation API): the `required` attribute, `type="email"`/`"number"`/`"url"`, `pattern`, `maxlength`, and the `setCustomValidity` DOM method for custom/async validation. TS-18's "Input assistance" requires labels, error identification in text, and error suggestions, but never names the native validation attributes/methods that deliver them. Missing. Recommend placing at `02-web-accessibility.adoc` under "3. Understandable" > Input assistance (~L191).

- [ ] https://web.dev/articles/top-cwv#inp — Interaction to Next Paint (INP) as a Core Web Vital and the technique of yielding to the main thread to break up long tasks (the Scheduler API and `scheduler.yield()`). TS-18 never mentions INP or long-task breaking. Missing. Recommend a new subsection in `01-performance-optimization.adoc`.

- [ ] https://web.dev/articles/top-cwv#3-avoid-large-rendering-updates — forced layout and layout thrashing: reorganize DOM reads and writes in JavaScript to avoid interleaving layout reads with mutating writes, and keep DOM size small (large DOMs make layout recalculation expensive). TS-18 does not address layout thrashing. Missing. Recommend a new subsection in `01-performance-optimization.adoc`. (Related to the general reflow/repaint gap above, but this is the specific read/write-ordering technique.)

- [ ] https://web.dev/articles/top-cwv#3-avoid-large-rendering-updates — CSS containment (`contain`) to lazily render off-screen DOM and avoid unnecessary layout/render work. Not addressed. Missing. Recommend a new subsection in `01-performance-optimization.adoc`.

- [ ] https://web.dev/articles/top-cwv#1-ensure-the-lcp-resource-is-discoverable-from-the-html-source-and-prioritized — the `fetchpriority="high"` HTML attribute to raise the priority of the LCP image resource so it loads sooner. Not addressed. Missing. Recommend placing at `01-performance-optimization.adoc` near the preload bullet (~L19).

- [ ] https://web.dev/articles/top-cwv#1-ensure-the-lcp-resource-is-discoverable-from-the-html-source-and-prioritized — the `loading="lazy"` image attribute, and the specific guidance to remove it from the LCP image to avoid load delay. TS-18 covers lazy-loading JavaScript but not the native `loading="lazy"` image attribute. Missing. Recommend placing at `01-performance-optimization.adoc` near the image-size bullet (~L66).

- [ ] https://web.dev/articles/top-cwv#2-aim-for-instant-navigations and https://web.dev/articles/top-cwv#2-ensure-pages-are-eligible-for-bfcache — the back/forward cache (bfcache): pages must meet eligibility criteria (avoid `Cache-Control: no-store`, avoid `unload` event listeners) to be restored instantly from memory on back/forward navigation, which also eliminates layout shifts. Not addressed. Missing. Recommend a new subsection in `01-performance-optimization.adoc`.

- [ ] https://csswizardry.com/2024/12/a-layered-approach-to-speculation-rules/ and https://web.dev/articles/top-cwv#2-aim-for-instant-navigations — the Speculation Rules API (`<script type="speculationrules">`): `prefetch` (pays the next page's TTFB up-front) and `prerender` (pays TTFB, FCP, and LCP up-front), with eagerness levels (`immediate`, `moderate`, `eager`), `href_matches`/`selector_matches` predicates, and an opt-in/opt-out hook pattern (e.g. `data-prefetch`, `data-prefetch=prerender`, `data-prefetch=false`) for a layered approach. TS-18 covers hover-based HTML pre-fetch (L11-17) but not the Speculation Rules API. Missing. Recommend a new subsection in `01-performance-optimization.adoc`.

- [ ] https://csswizardry.com/2024/12/a-layered-approach-to-speculation-rules/#clearing-speculation-rules-cache-with-clear-site-data — the `Clear-Site-Data` HTTP response header extended with `prefetchCache` and `prerenderCache` directives (Chrome 138+) to forcibly purge speculative-loading caches. Not addressed. Missing. Recommend placing at `01-performance-optimization.adoc` alongside the Speculation Rules item above.

- [ ] https://web.dev/articles/top-cwv#3-avoid-animations-and-transitions-that-use-layout-inducing-css-properties — never animate or transition CSS properties that require layout updates (`margin`, `border`, `top`, `left`); prefer `transform`/`translateX` so work happens on the compositor/GPU and does not cause layout shifts. TS-18 covers `prefers-reduced-motion` but not the layout-inducing-animation guidance. Missing. Recommend a new subsection in `01-performance-optimization.adoc` (the CLS angle) and/or a cross-link from `02-web-accessibility.adoc` (animations).

- [ ] https://frontendmasters.com/blog/patterns-for-memory-efficient-dom-manipulation/#prefer-hidingshowing-over-creating-new-elements — prefer hiding/showing existing (server-rendered) elements over destroying and recreating them with JavaScript, to keep the DOM mostly static and avoid garbage-collection churn. Not addressed. Missing. Recommend a new section (proposed `05-javascript-behaviors.adoc`).

- [ ] https://frontendmasters.com/blog/patterns-for-memory-efficient-dom-manipulation/#prefer-textcontent-over-innertext — prefer `textContent` over `innerText` for reading element content, because `innerText` forces a reflow to account for current styles. Not addressed. Missing. Recommend a new section (proposed `05-javascript-behaviors.adoc`).

- [ ] https://frontendmasters.com/blog/patterns-for-memory-efficient-dom-manipulation/#use-insertadjacenthtml-over-innerhtml — prefer `insertAdjacentHTML` over `innerHTML` for inserting HTML, because `innerHTML` destroys the existing DOM first. Not addressed. Missing. Recommend a new section (proposed `05-javascript-behaviors.adoc`).

- [ ] https://frontendmasters.com/blog/patterns-for-memory-efficient-dom-manipulation/#approach-1-use-the-template-tag — the `<template>` element plus `appendChild`/`insertAdjacentElement` as the fastest pattern for creating and inserting fully-formed DOM nodes. Not addressed. Missing. Recommend a new section (proposed `05-javascript-behaviors.adoc`).

- [ ] https://frontendmasters.com/blog/patterns-for-memory-efficient-dom-manipulation/#approach-2-use-createdocumentfragment — `createDocumentFragment` to prepare multiple nodes and insert them in a single operation, minimizing reflows. Not addressed. Missing. Recommend a new section (proposed `05-javascript-behaviors.adoc`).

- [ ] https://frontendmasters.com/blog/patterns-for-memory-efficient-dom-manipulation/#manage-references-when-nodes-are-removed — `WeakMap` and `WeakRef` to associate data with DOM nodes so that removing a node allows the associated data to be garbage-collected rather than leaked. Not addressed. Missing. Recommend a new section (proposed `05-javascript-behaviors.adoc`).

- [ ] https://frontendmasters.com/blog/patterns-for-memory-efficient-dom-manipulation/#cleaning-up-event-listeners — event-listener cleanup: `removeEventListener`, the `addEventListener` `once` option, and `AbortController` to unbind groups of listeners at once. TS-18 has no event-listener lifecycle guidance. Missing. Recommend a new section (proposed `05-javascript-behaviors.adoc`).

- [ ] https://neurodiversity.design/ — neurodiversity / cognitive-accessibility design guidance: the Neurodiversity Design System covers Font, Typography, Colour, Buttons/Links/Inputs, Interface, Communications, Numbers, and Animations for neurodivergent learners (e.g. font shapes that help dyslexic readers; typography that supports reading on screens). TS-18's opening states it covers "cognitive disabilities" and targets WCAG 2.2 Level AA, but its body provides no neurodiversity-specific guidance beyond `prefers-reduced-motion` (animations) and general colour contrast. Missing (with a scope nuance: TS-18 explicitly claims cognitive disabilities, so this is in scope; much of the NDS goes beyond WCAG AA, but TS-18's own framing invites it). Recommend a new subsection in `02-web-accessibility.adoc`. NOTE: only the NDS landing page was retrieved — see Unresolved.

- [ ] https://brandur.org/idempotency-keys ("Beyond APIs") covers double
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

## Partial

- [ ] `src/018/__TODO__/web-clients/_todo/0200-progressive-enhancement.md:7` and `:86` — progressive enhancement as the framing for performance: serve a static baseline that works without JS/CSS, then layer enhancements. TS-18 says "server-render as much HTML as possible" but does not require the no-JS baseline or the progressive-enhancement model, and never states that anything requiring JS must be injected by JS. Recommend strengthening `01-performance-optimization.adoc` L7-9 (server-render bullet) and cross-linking to accessibility.

- [ ] `src/018/__TODO__/web-clients/_todo/loading-and-bundling.md:4` — module bundling vs. module loading as a strategy (bundling for HTTP/1.x, native modules for HTTP/2; trade-offs of cache invalidation granularity and mobile bandwidth). TS-18 mentions "code splitting" but not the broader bundling-vs-loading decision or its HTTP/2 interaction. Recommend expanding `01-performance-optimization.adoc` L57-61 (code splitting bullet).

- [ ] `src/018/__TODO__/web-clients/_todo/0300-accessibility.md:240` (Enable "skip to content") — full implementation pattern for the skip link (visibly-on-focus, first tabbable link, paired "jump back to top" link, code sample). TS-18 requires a skip-navigation mechanism but gives no implementation guidance. Recommend expanding `02-web-accessibility.adoc` L121-123 (Navigable intro).

- [ ] `src/018/__TODO__/web-clients/_todo/0300-accessibility.md:240` (Provide context) — breadcrumbs, sitemaps, and current-location indication within navigation. TS-18 requires consistent navigation and two ways to locate pages but does not mention breadcrumbs or current-location indicators. Recommend placing at `02-web-accessibility.adoc` under "2. Operable" (~L133).

- [ ] `src/018/__TODO__/web-clients/_todo/0300-accessibility.md:360` and `:408` — grouping long forms with `<fieldset>`/`<legend>` for assistive-tech navigation. TS-18 requires descriptive labels but does not mention fieldset grouping. Recommend expanding `02-web-accessibility.adoc` L191 (Input assistance / form labels).

- [ ] `src/018/__TODO__/web-clients/_todo/0300-accessibility.md:414` — time-limit adjustment detail: warn users at least 20 seconds before expiry and offer a simple one-action extension. TS-18 says users must be able to turn off / adjust to 10x / extend on request, but does not specify the 20-second warning. Recommend expanding `02-web-accessibility.adoc` L105-108 (Enough time).

- [ ] `src/018/__TODO__/web-clients/_todo/0300-accessibility.md:427` (Multimedia) — the `<track>` element and VTT format for captions, transcripts, and audio descriptions, with code samples. TS-18 requires captions/transcripts/audio-descriptions as outcomes but does not name the `<track>` element or VTT. Recommend expanding `02-web-accessibility.adoc` L29-35 (Time-based media).

- [ ] `src/018/__TODO__/web-clients/_todo/0300-accessibility.md:460` — media and interactive content (including games) should be paused by default. TS-18 covers pausable auto-playing audio but not pause-by-default for video/games. Recommend expanding `02-web-accessibility.adoc` L63-64 (Distinguishable / audio).

- [ ] `src/018/__TODO__/web-clients/_todo/0300-accessibility.md:51` (ARIA) — specific ARIA landmark roles (`banner`, `navigation`, `main`) and `aria-label` for naming navigation regions. TS-18 mentions ARIA generally but does not name landmarks. Recommend expanding `02-web-accessibility.adoc` L222-223 (Robust / semantic HTML + ARIA).

- [ ] https://www.bramstein.com/writing/web-font-loading-patterns.html#custom-font-display — the FOIT (Flash of Invisible Text) vs. FOUT (Flash of Unstyled Text) mechanism, and the JS-based class-toggling FOUT pattern. TS-18 says `font-display: swap` "prevents invisible text" but does not explain the FOIT/FOUT behaviour it is preventing. Recommend expanding `03-fonts.adoc` L66-71 (font-display bullet).

- [ ] https://www.bramstein.com/writing/web-font-loading-patterns.html#loading-groups-of-fonts — grouped font loading (load a whole family together via `Promise.all`) to avoid faux styles and collapse multiple reflows into one. TS-18 discusses CLS/fallback tuning but not grouped loading to reduce reflows. Recommend expanding `03-fonts.adoc` L83-87 (Fallbacks).

The following Partial items are from the resources listed in GitHub issue #61.

- [ ] https://css-tricks.com/tooltip-best-practices/ — tooltip implementation patterns: tooltips are text-only non-interactive popovers (use a `dialog` for interactive content); label an icon tooltip with `aria-labelledby` and provide a contextual description with `aria-describedby`; use `role="tooltip"`; do not use the `title` attribute; do not combine `aria-haspopup` with `role="tooltip"`; open on hover/focus and close on mouseout/blur; tooltips are inaccessible on touch devices (prefer visible labels); use a toggletip (`<button>` + `role="status"` live region) for informational popups. TS-18 asserts the WCAG 1.4.13 outcome (dismissible via Escape, hoverable, persistent) at `02-web-accessibility.adoc` L84-86 but gives none of this implementation guidance. Partial. Recommend expanding `02-web-accessibility.adoc` L84-86.

- [ ] https://web.dev/articles/top-cwv#2-avoid-unnecessary-javascript — the broader guidance to minimize JavaScript shipped: prefer Baseline widely-available platform features over JS reimplementations, use the Chrome DevTools coverage tool to find unused code, and periodically prune tag-manager tags. TS-18 covers code splitting and lazy loading (L57-64) but frames JS only as "serve only the subset required" rather than the broader minimize-JS / remove-unused-code message. Partial. Recommend expanding `01-performance-optimization.adoc` L57-61.

- [ ] https://web.dev/articles/top-cwv#1-ensure-the-lcp-resource-is-discoverable-from-the-html-source-and-prioritized — LCP image discoverability: use `<img src>`/`srcset` (not `data-src` which requires JS); prefer SSR over CSR so the image markup is in the HTML source; preload the LCP image with `<link rel="preload">` if it must be referenced from CSS/JS. TS-18 recommends server-rendering (L7-9) and preloading (L19-22) but does not address the `data-src` anti-pattern or the image-specific discoverability guidance. Partial. Recommend expanding `01-performance-optimization.adoc` L19-22 and L7-9.

- [ ] https://web.dev/articles/top-cwv#1-set-explicit-sizes-on-any-content-loaded-from-the-page — the `aspect-ratio` CSS property (Baseline widely available) to reserve space for images and non-image elements with a dynamic width, and `min-height` as a fallback to reduce layout-shift severity for dynamic content of unknown size. TS-18 covers fixed `width`/`height` on images (L66-70) but not `aspect-ratio` or `min-height`. Partial. Recommend expanding `01-performance-optimization.adoc` L66-70.

## Out-of-scope

- [ ] `src/018/__TODO__/web-clients-2/7000-security/200-xsrf.md` (Cross-site request forgery) — XSRF mechanisms (synchronizer token, double-submit token, JSON obfuscation, session expiry, re-authentication). Flagged: TS-18's stated pillars are performance, accessibility, and fonts; web client security is not among them, though a `7000-security/` tree exists in `__TODO__`, suggesting the maintainers may intend to add it. Confirm whether security belongs in TS-18 or a separate standard.

- [ ] `src/018/__TODO__/web-clients-2/7000-security/300-mitm.md` (Man-in-the-middle) — HTTPS everywhere, `Secure` cookie flag, securing logs/dumps/backups. Flagged for the same scope reason as XSRF.

- [ ] `src/018/__TODO__/web-clients-2/7000-security/400-xss.md` (Cross-site scripting) — input sanitization, output escaping, `HttpOnly` cookies, avoiding web storage for session data, third-party/CDN script risk. Flagged for the same scope reason as XSRF.

- [ ] `src/018/__TODO__/web-clients-2/7000-security/700-bearer-auth.md` (Bearer auth) — token storage trade-offs (memory vs. cookie vs. session/local storage), `HttpOnly` tokens, refresh tokens, revocation, same-origin API proxies. Flagged for the same scope reason as XSRF.

- [ ] https://stephaniewalter.design/blog/the-ultimate-guide-to-not-fck-up-push-notifications/ — push-notification UX (do not request permission on page load; ask in context; the "double permission" pattern; timing/precision/personalization; user control and opt-out). Flagged: push notifications are a distinct feature topic, not one of TS-18's three pillars. Confirm whether to add a notifications section to TS-18.

- [ ] `src/018/__TODO__/web-clients/_todo/0400-architecture.md` — web client architecture (static site, dynamic site, SPA, MPA, micro frontends, PWA, server/client logic split). Plausibly sits outside TS-18 because `AGENTS.md` defers general application architecture to TS-5. Flagged for confirmation.

- [ ] `src/018/__TODO__/web-clients/_todo/single-pade-applications.md` and `application-frameworks.md` and `application-state.md` — SPA frameworks, MV* patterns, models as single source of truth, framework agnosticity. Out of scope: application architecture (TS-5).

- [ ] `src/018/__TODO__/web-clients/_todo/responsive-design.md` — responsive design methodology (mobile-first, `min-width` media queries, content-based breakpoints, the viewport `<meta>` tag, rem-based breakpoints, container queries). Flagged: TS-18's accessibility section covers reflow at 320px and orientation, but responsive design methodology is not one of the three stated pillars. Confirm whether responsive design belongs in TS-18 (the `__TODO__` placement suggests the maintainers think it might).

- [ ] `src/018/__TODO__/web-clients/_todo/browsers.md` — browser/device support policy (1% market-share threshold, last two major versions, not testing betas). Out of scope: testing/support policy (TS-14 / TS-15).

- [ ] `src/018/__TODO__/web-clients/_todo/feature-detection.md` and `polyfilling.md` — feature detection vs. user-agent detection, CSS feature detection, dynamic polyfilling. Flagged: implementation technique, not one of the three pillars. Confirm scope.

- [ ] `src/018/__TODO__/web-clients/_todo/dom.md`, `dom2.md`, `scripting.md`, `window-events.md`, `web-client-apis.md`, `fetch-ajax.md` — DOM/events/scripting/XHR/CORS/web-client-API implementation details. Out of scope: low-level implementation guidance beyond TS-18's three pillars.

- [ ] `src/018/__TODO__/web-clients/_todo/i18n.md` — internationalization (localization, translation, dialects, UTF-8/Unicode). Out of scope: i18n is a separate concern (likely its own standard).

- [ ] `src/018/__TODO__/web-clients/_todo/seo.md` — SEO. Out of scope: TS-19 covers SEO.

- [ ] `src/018/__TODO__/web-clients/_todo/pwa.md` — Progressive Web Apps as a packaging/installability model. Out of scope: TS-18 already references service workers for caching; PWA as an architecture is out of scope (TS-5).

- [ ] `src/018/__TODO__/web-clients/_todo/audits.md` — website audit / technical due-diligence checklists. Out of scope: process/auditing (TS-14 / TS-15).

- [ ] `src/018/__TODO__/web-clients/_todo/0300-accessibility.md:60` (Testing) — the assistive-technology test matrix (JAWS, VoiceOver, NVDA, ZoomText, Dragon) and the manual/automated accessibility audit process. Out of scope: TS-18's `AGENTS.md` states that "Accessibility testing process is covered by TS-14: Performance Testing."

- [ ] `src/018/__TODO__/web-clients/_todo/0300-accessibility.md:484` (7:1 contrast), `:508` (sign-language tracks), and the lower-secondary reading-level guidance (`:159`) — these target WCAG Level AAA. Out of scope: TS-18 explicitly targets Level AA.

- [ ] https://w3ctag.github.io/design-principles/ — the W3C TAG Web Platform Design Principles (priority of constituencies, safe-to-visit, trusted UI, user activation, feature detectability, etc.). Out of scope: this document is aimed at designers of web-platform specifications/APIs, not at builders of web GUIs.

- [ ] https://webstyleguide.com/ — Web Style Guide (Lynch & Horton) covers Strategy, Research, Process, Information Architecture, Site/Page Structure, Interface Design, Graphic Design, Typography, Editorial Style, Images, and Video. Out of scope: broader UI/usability guidance (TS-15). Only the table-of-contents page was retrievable; the per-chapter content was not fetched (see Unresolved).

The following items were relocated from TS-36's gap analysis (rsjs). They are
out-of-scope for TS-18 because they are library-specific, jQuery-specific, or
dated tooling recipes rather than web-GUI design/implementation guidance.

- [ ] https://ricostacruz.com/rsjs/#consider-using-onmount — recommending the
      `onmount` library specifically is a library/tooling recommendation for
      jQuery-era DOM lifecycles, outside TS-18's scope.

- [ ] https://ricostacruz.com/rsjs/#use-each-when-needed — using `jQuery.each`
      to initialize per-element state is a jQuery-specific pattern, outside
      TS-18's scope.

- [ ] https://ricostacruz.com/rsjs/#load-3rd-party-resources-asynchronously —
      async-loading external vendor scripts (e.g. Google Maps) via a helper
      that defers a global to a callback is a legacy pattern superseded by
      dynamic `import()`. The script-loading-strategy gap is already tracked
      above from the `web-clients` reference. Out of scope as a dated
      technique.

- [ ] https://ricostacruz.com/rsjs/#loading-component-files — the appendix
      recipes for bulk-loading `behaviors/` via Rails Sprockets `require_tree`,
      Browserify `require-globify`, Webpack `require.context`, and Brunch
      `glob-brunch` are dated tooling recipes for concatenation pipelines,
      outside TS-18's scope.

The following Out-of-scope items are from the resources listed in GitHub
issue #61.

- [ ] https://vercel.com/blog/how-vercel-adopted-microfrontends — microfrontends architecture: vertical (split-by-path) vs horizontal (split-by-feature) microfrontends, Next.js Multi-Zones, monorepo with Turborepo, and incremental migration via feature flags. Out of scope: application architecture (TS-5). This overlaps with the existing `0400-architecture.md` out-of-scope item above. The prefetch/prerender performance angle (Speculation Rules to mitigate hard navigations between microfrontends) is captured as a missing gap above.

- [ ] https://frontendmasters.com/blog/patterns-for-memory-efficient-dom-manipulation/#profiling-debugging — the Chrome DevTools Memory-tab (heap snapshots) and Performance-tab (JavaScript execution timeline, rendering/painting) profiling workflow. Out of scope: testing/process (TS-14 / TS-15).

- [ ] https://neurodiversity.design/ (Learner Personas) — neurodivergent learner personas (e.g. dyspraxia, dyslexia, ADHD) as a UX-research tool, scoped to Learning Management Systems. Out of scope: persona-based UX research and LMS-specific design (plausibly TS-15). The NDS design-principle content is captured as a missing gap above.

## Unresolved

- [ ] https://webstyleguide.com/ — only the contents/landing page was retrieved; the individual chapters (Strategy, IA, Interface Design, Typography, Images, Video, etc.) are separate pages that were not fetched. The out-of-scope call above is based on the table of contents alone. If any chapter (especially Typography, Images, or Page Structure) should be compared in depth, re-run with those chapter URLs as explicit references.

- [ ] The following binary PDFs in `src/018/__TODO__/web-clients/_todo/` were skipped silently per the gap-analysis rules (binary files are not text references): `Frontend Architecture for Design Systems.pdf`, `The Principles of Beautiful Web Design.pdf`, `Real Life Responsive Web Design (Smashing Book).pdf`, `Build Mobile Websites and Apps for Smart Devices.pdf`, `Beyond the 12 Factor App.pdf`. Not included in the comparison. If any should be treated as references, extract their text and re-run.

- [ ] `src/018/__TODO__/web-clients/_todo/encoding.md`, `modules-and-bundling.md`, and `0500-csp.md` are empty stubs (no substantive content), so no claims were extracted from them.

- [ ] https://neurodiversity.design/ — only the landing page was retrieved. The per-principle pages (Numbers, Font, Typography, Colour, Buttons/Links/Inputs, Interface, Communications, Animations) were not fetched, so the cognitive-accessibility gap above is based on the landing page's category list and two inline snippets ("the right typography can support neurodivergent learners' reading on screens"; "specific font shapes that make dyslexic readers, read better") only. Re-run with the individual principle-page URLs to compare in depth.

- [ ] https://www.youtube.com/watch?v=-Ln-8QM8KhQ — this video is already listed in TS-18's own `04-references.adoc`. The comparison is against the creator's video description (extracted via the helper script), not a full transcript. The description's chapters (Server-Rendered HTML, Prefetching HTML, CDN Caching, Client Caching with Service Worker, Preloading Assets, Critical CSS, LCP, Fixed-Size Images, JavaScript) map almost 1-1 to TS-18's existing `01-performance-optimization.adoc` content, so no new gaps were identified from it. A full transcript was not fetched, so spoken-only details could not be verified.