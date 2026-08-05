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
implementation guidance.

**Status:** First run (2026-08-05). No gaps checked off yet. All items below
are open.

## Missing

- [ ] https://csswizardry.com/2019/08/time-to-first-byte-what-it-is-and-why-it-matters/#what-is-ttfb — Time to First Byte (TTFB) as a performance metric and its contributors (latency, routing, application runtime, DB queries, SSR cost). TS-18 mentions LCP but never TTFB. Recommend a new subsection in `01-performance-optimization.adoc` after the LCP note (~L53).

- [ ] https://csswizardry.com/2019/08/time-to-first-byte-what-it-is-and-why-it-matters/#demystifying-ttfb — the `Server-Timing` HTTP response header as a way to surface server-side timing breakdowns to the front end. Not addressed anywhere in the standard. Recommend a new subsection in `01-performance-optimization.adoc`.

- [ ] `src/018/__TODO__/web-clients/_todo/loading-and-bundling.md:29` — HTTP/2 multiplexing and HTTP/2 Server Push as asset-delivery strategies that reduce round trips and enable per-browser polyfill pushing. TS-18 does not mention HTTP/2 or Server Push. Recommend a new subsection in `01-performance-optimization.adoc`.

- [ ] `src/018/__TODO__/web-clients/_todo/0200-progressive-enhancement.md:102` — `<script>` loading strategy: placing scripts before `</body>`, the `defer` and `async` attributes, and ordering scripts after stylesheets. TS-18 covers code splitting/lazy loading but not script-element loading attributes. Recommend a new subsection in `01-performance-optimization.adoc`.

- [ ] `src/018/__TODO__/web-clients/_todo/principles.md:19` and `src/018/__TODO__/web-clients/_todo/dom.md:5` — the cost of DOM reflows and repaints, and the guidance to prefer CSS animations over JavaScript-driven animations (and to animate unstyled containers when JS is unavoidable). Not addressed. Recommend a new subsection in `01-performance-optimization.adoc`.

- [ ] `src/018/__TODO__/web-clients/_todo/dom.md:65` (Best practices) — event delegation (attaching one listener to a parent rather than many to children) to reduce total listener count and improve performance. Not addressed. Recommend a new subsection in `01-performance-optimization.adoc`.

- [ ] `src/018/__TODO__/web-clients/_todo/0300-accessibility.md:199` (Valid, Semantic Markup) — the requirement that HTML markup be valid, validated with the W3C Markup Validation Service. TS-18's "Robust" principle says to use semantic HTML and ARIA but never requires valid markup as a baseline. Recommend placing at `02-web-accessibility.adoc` under "4. Robust" (~L210).

- [ ] `src/018/__TODO__/web-clients/_todo/0200-progressive-enhancement.md:38` and `:96` — `<noscript>` guidance: use it only to surface messages when content genuinely cannot work without JS; do not use it to fork the experience. TS-18 does not mention `<noscript>` at all. Recommend a new subsection in `02-web-accessibility.adoc` (or a progressive-enhancement section in `01-performance-optimization.adoc`).

- [ ] `src/018/__TODO__/web-clients/_todo/0300-accessibility.md:240` (Navigation) — the `<link rel="index|next|prev|contents">` head elements for document-level navigation metadata. Not addressed in TS-18's "Navigable" guidance. Recommend placing at `02-web-accessibility.adoc` under "2. Operable" (~L121).

- [ ] https://www.bramstein.com/writing/web-font-loading-patterns.html#prioritised-loading — prioritised/sequential font loading (load a small primary font first, then a larger secondary font, with the secondary gated on the primary succeeding). TS-18 mentions preloading only above-the-fold subsets, not staged/dependent loading. Recommend a new subsection in `03-fonts.adoc` under "Loading strategy" (~L46).

- [ ] https://www.bramstein.com/writing/web-font-loading-patterns.html#optimise-for-caching — the sessionStorage cache-state pattern: record that fonts have loaded so repeat page views render the custom font immediately (avoiding FOUT on navigation). Not addressed. Recommend a new subsection in `03-fonts.adoc` under "Loading strategy".

- [ ] https://www.bramstein.com/writing/web-font-loading-patterns.html#basic-font-loading — JavaScript-based font loaders (e.g. Font Face Observer) and the patterns built on them (basic, grouped, timeout-raced loading). TS-18 relies entirely on native `font-display`/preload and does not cover JS loader patterns. Note these predate `font-display` and are largely superseded, but the reference presents them. Recommend a new subsection in `03-fonts.adoc` (flag as a legacy alternative).

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

## Unresolved

- [ ] https://webstyleguide.com/ — only the contents/landing page was retrieved; the individual chapters (Strategy, IA, Interface Design, Typography, Images, Video, etc.) are separate pages that were not fetched. The out-of-scope call above is based on the table of contents alone. If any chapter (especially Typography, Images, or Page Structure) should be compared in depth, re-run with those chapter URLs as explicit references.

- [ ] The following binary PDFs in `src/018/__TODO__/web-clients/_todo/` were skipped silently per the gap-analysis rules (binary files are not text references): `Frontend Architecture for Design Systems.pdf`, `The Principles of Beautiful Web Design.pdf`, `Real Life Responsive Web Design (Smashing Book).pdf`, `Build Mobile Websites and Apps for Smart Devices.pdf`, `Beyond the 12 Factor App.pdf`. Not included in the comparison. If any should be treated as references, extract their text and re-run.

- [ ] `src/018/__TODO__/web-clients/_todo/encoding.md`, `modules-and-bundling.md`, and `0500-csp.md` are empty stubs (no substantive content), so no claims were extracted from them.