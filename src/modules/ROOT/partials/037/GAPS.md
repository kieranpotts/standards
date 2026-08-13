# TS-37 gap analysis

Gaps found comparing TS-37: Web Platform APIs against the following reference
resources:

- https://www.trysmudford.com/blog/hyper-responsive-web-components/
- https://daverupert.com/2024/10/super-web-components-sunshine/
- https://adactio.com/journal/20618

**Assessment.** TS-37 is currently a stub: `src/modules/ROOT/pages/037.adoc` contains
only a TODO introductory placeholder and "See also" links to TS-18 and TS-63,
and `src/modules/ROOT/partials/037/AGENTS.md` is an empty `<!-- TODO -->`. The standard therefore
covers none of the substantive material in the three references. Because the
standard's stated scope ("Web Platform APIs") plainly encompasses the web
component family of platform APIs (Custom Elements, Shadow DOM, slots,
Declarative Shadow DOM), almost every web-component claim in the references is
a genuine **missing** gap. Pure CSS layout/typography techniques raised by the
references (container queries, fluid `clamp()` type, intrinsic flex layouts,
`text-wrap: balance`, the `ch` unit) are noted as **out-of-scope** — they read
more like TS-18 (Web GUIs) material than TS-37 API guidance, but they are
flagged for the user to confirm or overrule. No "partial" gaps exist because
there is no existing body text to be shallower than the references.

**Status:** Initial run. All gaps open. Last run 2026-08-05.

## Missing

- [ ] https://www.trysmudford.com/blog/hyper-responsive-web-components/
      ("Hyper-responsive web components") is not addressed anywhere in the
      standard. It frames web components as the solution for portable,
      embeddable widgets that must render on any third-party site, in any
      position, at any viewport, with any content. Recommend a new section in
      `src/modules/ROOT/pages/037.adoc`.

- [ ] https://www.trysmudford.com/blog/hyper-responsive-web-components/
      ("Three immediate approaches") is not addressed anywhere in the
      standard. It compares three portable-component strategies — a script
      that injects HTML (suffers CSS leakage both ways), an `<iframe>` (style
      encapsulation but cannot dynamically resize to content and a `<form>`
      POST navigates the iframe not the page), and a web component with Shadow
      DOM — and their tradeoffs. Recommend a new section in
      `src/modules/ROOT/pages/037.adoc`.

- [ ] https://www.trysmudford.com/blog/hyper-responsive-web-components/
      ("Writing an encapsulated web component") is not addressed anywhere in
      the standard. It shows building an encapsulated web component with
      `attachShadow({ mode: 'open' })`, `connectedCallback`, and
      `customElements.define`, with no build system required. Recommend a new
      section in `src/modules/ROOT/pages/037.adoc`.

- [ ] https://www.trysmudford.com/blog/hyper-responsive-web-components/
      ("Writing an encapsulated web component", paragraph on HTML
      fault-tolerance) is not addressed anywhere in the standard. It notes
      that because HTML is intrinsically fault-tolerant, any HTML placed
      between the component tags renders automatically if the web component
      script fails to load — a progressive-enhancement / graceful-degradation
      property of custom elements. Recommend a new section in
      `src/modules/ROOT/pages/037.adoc`.

- [ ] https://www.trysmudford.com/blog/hyper-responsive-web-components/
      (Note after "Applying container-driven typography") is not addressed
      anywhere in the standard. It documents a leak in Shadow DOM
      encapsulation: a web component has no `:root`, so internal `rem` values
      resolve against the host page's `html/:root` font-size, and a page that
      alters that size scales the component. Recommend a new section in
      `src/modules/ROOT/pages/037.adoc`.

- [ ] https://daverupert.com/2024/10/super-web-components-sunshine/ ("The
      good parts") is not addressed anywhere in the standard. It catalogs
      situations where web components are a good fit: leaf nodes;
      presentational wrappers around other components via `<slot>` (with the
      caveat "Not everything needs to be a web component"); design systems;
      progressively enhancing regular HTML; View Source / debuggability of
      `my-button` vs `div.spf50`; buildless sites; one-off projects with low
      maintenance burden; prototyping; low-memory / fast performance profile;
      style encapsulation via Shadow DOM; small atomic template updates via
      tagged-template-literal libraries; components shared across different
      tech stacks (acquisitions, departmental autonomy); packaging
      accessibility/animation/CSS demos for distribution; third-party embed
      widgets; large applications built with Shadow DOM; and enabling
      designers-who-can-code. Recommend a new section in
      `src/modules/ROOT/pages/037.adoc`.

- [ ] https://daverupert.com/2024/10/super-web-components-sunshine/ ("The
      not-so great parts") is not addressed anywhere in the standard. It
      catalogs the rough edges of web components: Shadow DOM's steep initial
      learning curve and "gotcha moments"; SSR via Declarative Shadow DOM is
      possible but under-documented and often library-specific (Enhance being
      a notable out-of-the-box solution); using web components as a
      page-level abstraction with a WC router is inadvisable — prefer
      server-generated HTML as the page abstraction; long-standing
      accessibility problems with Cross-Root ARIA (label in document vs input
      in shadow root), with `referencetarget` rolling out in Chromium as the
      fix; and friction around building a compiler for JS-framework-based web
      components. Recommend a new section in `src/modules/ROOT/pages/037.adoc`.

- [ ] https://daverupert.com/2024/10/super-web-components-sunshine/ ("The
      not-so great parts" — SSR bullet) is not addressed anywhere in the
      standard. It calls out that web components can be server-rendered using
      Declarative Shadow DOM, but the sparse literature suggests the practice
      is kludgy or library-specific, and names Enhance as a framework doing
      it out of the box. Recommend a new section in `src/modules/ROOT/pages/037.adoc`.

- [ ] https://daverupert.com/2024/10/super-web-components-sunshine/ ("The
      not-so great parts" — Accessibility bullet) is not addressed anywhere in
      the standard. It describes the Cross-Root ARIA problem (associating a
      label in the document with an input inside a shadow root), existing
      workarounds, and the `referencetarget` attribute rolling out in Chromium
      to resolve it. Recommend a new section in `src/modules/ROOT/pages/037.adoc`.

- [ ] https://adactio.com/journal/20618 ("HTML web components", opening
      paragraphs) is not addressed anywhere in the standard. It argues web
      components are portable web standards that will outlive any framework
      (citing Jake Lazaroff: "web components will outlive your JavaScript
      framework"), in contrast to React as legacy/lock-in technology.
      Recommend a new section in `src/modules/ROOT/pages/037.adoc`.

- [ ] https://adactio.com/journal/20618 ("HTML web components", "I have a
      suggestion for you") is not addressed anywhere in the standard. It
      warns against bringing React's mindset to web components — the React
      pattern of empty shell components with props doing the heavy lifting —
      and instead asks "what would HTML do?", using HTML up to its limit and
      then enhancing. Recommend a new section in `src/modules/ROOT/pages/037.adoc`.

- [ ] https://adactio.com/journal/20618 (Robin / Dave quotations) is not
      addressed anywhere in the standard. It positions web components as
      "small, reusable chunks of code that extend the language of HTML" and
      "HTML with superpowers" — augmenting existing markup with just enough
      behaviour — rather than monolithic React-style Button/Table/Input
      components. Recommend a new section in `src/modules/ROOT/pages/037.adoc`.

- [ ] https://adactio.com/journal/20618 ("Where does the shadow DOM come
      into all of this?") is not addressed anywhere in the standard. It
      recommends treating Shadow DOM as a last resort and seeing how far
      regular-HTML composibility goes first. Recommend a new section in
      `src/modules/ROOT/pages/037.adoc`.

- [ ] https://adactio.com/journal/20618 (Eric Meyer `super-slider` example)
      is not addressed anywhere in the standard. It demonstrates wrapping
      existing `label` + `input type="range"` markup in a custom element and
      adding JS capabilities styled with regular CSS — "the Light Side of
      the Web", no Shadow DOM. Recommend a new section in
      `src/modules/ROOT/pages/037.adoc`.

- [ ] https://adactio.com/journal/20618 (Jim Nielsen `icon-list` example) is
      not addressed anywhere in the standard. It shows using custom elements
      solely to attach functionality (no Shadow DOM, no templates, no slots)
      — wrapping a `ul` of `li`s. Recommend a new section in
      `src/modules/ROOT/pages/037.adoc`.

- [ ] https://adactio.com/journal/20618 ("HTML web components" definition)
      is not addressed anywhere in the standard. It defines "HTML web
      components" (a custom element extending existing markup) vs "JavaScript
      web components" (an empty shell relying exclusively on JS), and
      contrasts React's mindset of replacement with web components'
      mindset of augmentation. Recommend a new section in
      `src/modules/ROOT/pages/037.adoc`.

- [ ] https://adactio.com/journal/20618 (Jim Nielsen response, "Web
      components have their own grain") is not addressed anywhere in the
      standard. It notes web components' unique power of rendering before
      JavaScript (impossible for React components), which encourages
      composing core content with HTML and wrapping it in a custom element
      that enhances — augmentation over replacement. Recommend a new section
      in `src/modules/ROOT/pages/037.adoc`.

- [ ] https://adactio.com/journal/20618 (Jim Nielsen response, "On The Web,
      Augmentation Wins in the Long Run") is not addressed anywhere in the
      standard. It argues augmentative approaches win on the web because the
      platform's grain favours enhancement for resilience, and that the best
      framework ideas are subsumed into the platform (XHTML→HTML5, XHR→fetch,
      Sass/jQuery→browser, TypeScript→browser, React component model→browser
      via web components). Recommend a new section in `src/modules/ROOT/pages/037.adoc`.

## Partial

_(None. TS-37 has no body content, so no reference point is covered more
shallowly than in the references — everything is either wholly missing or
out-of-scope.)_

## Out-of-scope

- [ ] https://www.trysmudford.com/blog/hyper-responsive-web-components/
      ("Responsive typography & space") covers this, but it plausibly sits
      outside this standard's stated purpose because fluid typography via
      `clamp()` with viewport units (Utopia) is a CSS/layout concern more
      characteristic of TS-18 (Web GUIs) than TS-37's Web Platform APIs scope.
      Flagged for the user to confirm or overrule.

- [ ] https://www.trysmudford.com/blog/hyper-responsive-web-components/
      ("Applying container-driven typography") covers this, but it
      plausibly sits outside this standard's stated purpose because CSS
      container queries (`container-type: inline-size`, the `cqi` unit,
      `@container`) and `@supports`-based progressive enhancement are
      CSS/layout features. Could be argued either way (platform feature vs
      GUI technique); flagged for the user to confirm or overrule — note it
      may better belong in TS-18.

- [ ] https://www.trysmudford.com/blog/hyper-responsive-web-components/
      ("Intrinsic layouts" and "Limitations of intrinsic design") covers
      this, but it plausibly sits outside this standard's stated purpose
      because the Every Layout "Sidebar" intrinsic flex/grid pattern and
      `@container`-driven content hiding are CSS layout techniques more
      characteristic of TS-18 (Web GUIs). Flagged for the user to confirm or
      overrule.

- [ ] https://www.trysmudford.com/blog/hyper-responsive-web-components/
      ("The finer details") covers this, but it plausibly sits outside this
      standard's stated purpose because `text-wrap: balance` and the `ch`
      unit for line-length control are CSS typography features more
      characteristic of TS-18 (Web GUIs). Flagged for the user to confirm or
      overrule.

## Unresolved

- [ ] TS-37 is a stub (`src/modules/ROOT/pages/037.adoc` holds only a TODO intro and
      "See also" links; `src/modules/ROOT/partials/037/AGENTS.md` is `<!-- TODO -->`). With no body
      text, the standard's precise scope boundary is unverifiable — in
      particular the line between TS-37 "Web Platform APIs" and TS-18 "Web
      GUIs" for CSS features (container queries, fluid typography) cannot be
      confirmed from the standard itself. The out-of-scope items above are
      best-effort calls; re-run this analysis once TS-37 has substantive
      content.