# TS-39 gap analysis

Gaps found comparing TS-39: HTML against the following reference
resources (the in-repository `__TODO__/039/` backlog of source
material intended to become this standard):

- `__TODO__/039/forms-and-inputs.adoc`
- `__TODO__/039/References.txt`
- `__TODO__/039/html/_index.md`
- `__TODO__/039/html/100-encoding.md`
- `__TODO__/039/html/_150-elements.md`
- `__TODO__/039/html/_200-head.md`
- `__TODO__/039/html/_250-metadata.md`
- `__TODO__/039/html/_300-hyperlinks.md`
- `__TODO__/039/html/_350-forms.md`
- `__TODO__/039/html/400-figures.md`
- `__TODO__/039/html/_420-images.md`
- `__TODO__/039/html/_440-av.md`
- `__TODO__/039/html/_700-accessibility.md`
- `__TODO__/039/html/_accessibility testing checklist.txt`
- `__TODO__/039/html/_todo/*.md`
- `__TODO__/039/html/_todo/HOUSE STYLE.md`
- `__TODO__/039/html/_todo/*.URL`
- `__TODO__/039/svg/_todo/*.URL`

**Assessment.** TS-39 is currently a **stub**: `README.adoc` contains only
the introductory prose (the "working standard" philosophy) and pulls in no
content via `include::`; `AGENTS.md` is `<!-- TODO -->`. The reference
material under `__TODO__/` is the backlog of draft source material that this
standard is meant to be built from, so virtually every concrete rule and
topic it contains is a gap. Coverage is therefore overwhelmingly "missing",
targeted at new sections that do not yet exist. A small number of items
(graphics-editor SVG authoring workflow, RDF/OWL "Semantic Web"
background, CI/tooling specifics) are flagged out-of-scope for an HTML
authoring standard.

**Status:** First run (2026-08-05). All gaps open. The standard has no
content files, so every gap's target location is "new section" (the
existing `README.adoc` is only the introduction). Re-run: read this file
first; carry forward every unchecked gap, and re-check any checked gap
against the standard's then-current content.

## Missing

### Encoding & doctype

- [ ] `__TODO__/039/html/100-encoding.md:3` — documents MUST be UTF-8;
      servers MUST send `Content-Type: text/html; charset=utf-8`; encoding
      MUST also be declared via `<meta charset="utf-8">` in `<head>` for
      local-file rendering. Recommend new section "Encoding".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:150` — `<!DOCTYPE html>`
      MUST be column 1, line 1, to prevent quirks mode. Recommend new
      section "Doctype".

### Document structure & source order

- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:12` — source order
      matters for accessibility; stripped of styling/tags a page should
      read coherently top-to-bottom; navigation sections get a (possibly
      visually hidden) heading. Recommend new section "Source order".
- [ ] `__TODO__/039/html/_todo/document-structure.md:1` — document
      structure, outline, and source order topic with reference list.
      Recommend new section "Document structure".
- [ ] `__TODO__/039/html/_todo/sections-and-document-outline.md:4`
      — semantic markup definition; HTML's primary role is semantics not
      presentation; sectioning elements (`<header>`, `<nav>`, `<footer>`,
      `<article>`, `<section>`) MUST be used wherever appropriate over
      generic `<div>`/`<span>`; `<section>` should contain a heading;
      `<figure>` for more than images. Recommend new section "Sections &
      document outline".

### Sectioning & body elements

- [ ] `__TODO__/039/html/_150-elements.md:5` — the allowed-element
      subset policy: MUST NOT use deprecated elements (`<acronym>`,
      `<center>`, `<hgroup>`) nor unsupported new ones (`<menu>`,
      `<dialog>`); explicit allow-list of body elements grouped by
      sections / text / tabular / forms / links / media / misc.
      Recommend new section "Allowed elements".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:404` — alternative
      (more detailed) allowed-element list plus an explicit forbidden
      list (h4–h6, `hgroup`, `abbr`, `dfn`, `dl`/`dt`/`dd`, `ins`/`del`,
      `legend`, `caption`, `blockquote`/`q`/`cite`, `s`/`u`/`kbd`/`samp`,
      `var`/`wbr`, `meter`/`progress`, `picture`, `details`/`summary`,
      `area`/`map`, `keygen`, reset buttons, several input types).
      Recommend new section "Allowed elements" (reconcile with the list
      above — they differ).

### Document head

- [ ] `__TODO__/039/html/_200-head.md:7` — baseline `<head>` (charset,
      viewport, title); the two `<meta>` tags MUST be first in source
      order. Recommend new section "Document head".
- [ ] `__TODO__/039/html/_200-head.md:21` — legal `<head>` elements
      (`<meta>`, `<link>`, `<title>`, `<style>`, `<script>`, `<base>`);
      `<noscript>` placement note. Recommend new section "Document head".
- [ ] `__TODO__/039/html/_200-head.md:51` — `<base>` strongly
      RECOMMENDED; form `scheme://domain` without trailing slash; relative
      URL conventions. Recommend new section "Base URL" (also
      `HOUSE STYLE.md:277` gives a conflicting `href` with trailing slash
      convention — reconcile).
- [ ] `__TODO__/039/html/_200-head.md:65` — `<title>` REQUIRED in all
      documents; website vs webapp title policies; en-dash delimiter for
      webapps; sentence case; branding boilerplate rules; title length
      (~55–60 chars) for SEO; accessibility implications; state-change
      reflection in title; `application-name` meta replication. Recommend
      new section "Title".
- [ ] `__TODO__/039/html/_200-head.md:109` — meta-tag guidance:
      `application-name` (webapps only), `description` (≤150 chars,
      unique per page, required for public pages), `keywords`,
      `author`, `referrer` (values + no dynamic injection),
      `robots`/`googlebot`, `Content-Security-Policy` meta. Recommend
      new section "Meta tags".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:245` — description meta
      120–150 chars full sentence; `keywords` as SEO reference only;
      `robots` `index`/`noindex` + `follow`/`nofollow` per page type
      (search/404 exceptions); viewport meta; WHATWG MetaExtensions as
      the full list. Recommend new section "Meta tags" (reconcile with
      `_200-head.md`).
- [ ] `__TODO__/039/html/_200-head.md:186` — `<link>` relationships:
      `stylesheet`, `manifest`, `canonical`, `alternate` (translations
      + feeds), `index`, pagination (`first`/`prev`/`next`/`last`),
      prefetching/prerender, icons. Recommend new section "Linked
      resources".

### Text content

- [ ] `__TODO__/039/html/_todo/text-content.md:5` — inline text
      element guidance: `<p>`, `<em>`, `<strong>`, `<blockquote>`, `<q>`,
      `<cite>`, `<abbr>`, `<dfn>`, `<code>`, `<samp>`, `<kbd>`, `<ins>`,
      `<del>`, `<sub>`/`<sup>` (semantics not presentation), `<address>`
      as sectioning. Recommend new section "Text content".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:614` — allowed inline
      element list (`a`, `b`, `bdi`, `bdo`, `br`, `code`, `data`, `em`,
      `i`, `mark`, `small`, `span`, `strong`, `sub`, `sup`, `time`) and
      per-element usage guidance (`em` vs `i`; `strong` vs `b`; `mark`;
      `small`; `<code>`+`<pre>`; do not use `<var>`/`<samp>`/`<kbd>`;
      `<data>`; `<time>`). Recommend new section "Inline text elements".
- [ ] `__TODO__/039/html/_todo/text-content.md:30` — heading
      hierarchy rules: convey structure not emphasis; ordered
      hierarchically; never consecutive same-level headings without
      intervening content; restrict depth (h1–h3 adequate); multiple
      `<h1>` allowed with sectioning. Recommend new section "Headings".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:471` — heading levels
      1–3 only; `<h1>` placement (outermost `<header>` + `<main>`; one on
      homepage); headings may be hyperlinked; no other inline elements
      inside headings. Recommend new section "Headings" (reconcile).
- [ ] `__TODO__/039/html/_todo/text-content.md:44` — list rules:
      three types; unordered/ordered usage by editorial significance;
      ordered numbers never hidden; `<ul>`/`<ol>` need ≥1 `<li>`;
      nesting ≤3 levels; `<dl>` requires `<dt>`+`<dd>`. Recommend new
      section "Lists".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:493` — list guidance:
      only `<ul>`/`<ol>` used (not `<dl>`); unordered for menus (must be
      in `<nav>`); ordered for significant order; `<ol type>` for nested
      numbering; no block elements inside `<ul>`/`<ol>` beyond lists;
      keep item text short. Recommend new section "Lists" (reconcile —
      `_150-elements.md`/`HOUSE STYLE.md` forbid `<dl>` while
      `text-content.md` permits it).
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:596` — `<hr>` represents
      a paragraph-level thematic break; never before headings or between
      sectioning elements; never purely presentational. Recommend new
      section "Horizontal rules".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:702` — `<pre>` for
      pre-formatted text where structure is typographic (plain-text
      emails, code, poems, ASCII art). Recommend new section
      "Pre-formatted text".

### Tables

- [ ] `__TODO__/039/html/_todo/tables.md:3` — tables only for tabular
      data (two+ dimensional relationships), never layout; `summary`
      attribute; `<caption>` for source/copyright not titles (use a
      heading); explicit `<thead>`/`<tbody>`/`<tfoot>`; `<th>` for
      column headings; avoid `border`. Recommend new section "Tables".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:706` — tables only for
      tabular data; example with thead/tbody/tfoot/caption. Recommend
      "Tables" (reconcile — `_200-head`/`HOUSE STYLE` forbid `caption`).

### Figures & images

- [ ] `__TODO__/039/html/400-figures.md:3` — content-referenced
      graphics MUST be in `<figure>`; `<figcaption>` RECOMMENDED at the
      bottom; caption is not a substitute for `alt`. Recommend new
      section "Figures".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:677` — `<figure>` for
      self-contained referenced content (chart, photo, code, quotation,
      table, video); allowed children; `<figcaption>` optional, max one,
      top or bottom only. Recommend new section "Figures" (reconcile).
- [ ] `__TODO__/039/html/_420-images.md:183` — raster image file
      formats (BMP, GIF, ICO, JPEG, PNG universally supported; JPEG/PNG
      preferred; WebP with `<picture>` fallback; APNG); MIME types &
      extensions. Recommend new section "Raster image formats".
- [ ] `__TODO__/039/html/_420-images.md:222` — image optimisation
      (compress to perceptible loss; <25 KB for mobile; export at
      rendered size; DPI irrelevant; RGB not CMYK; resampling algorithms;
      blur to reduce JPEG size). Recommend new section "Image
      optimisation".
- [ ] `__TODO__/039/html/_420-images.md:240` — serving raster images
      (lowercase extensions; correct `Content-Type`; separate
      cookie-free domain; `Expires`/`Cache-Control` ≥6 months; rename
      to bust cache; data URIs for many tiny images). Recommend new
      section "Serving images".
- [ ] `__TODO__/039/html/_420-images.md:256` — responsive images:
      default image + alternatives; `srcset` `x` descriptors for pixel
      density; `<picture>`/`<source>` with `media` for breakpoint art
      direction; source order significance; bandwidth is the browser's
      choice. Recommend new section "Responsive images".
- [ ] `__TODO__/039/html/_420-images.md:417` — alternative
      `srcset` `w`-descriptor + `sizes` methodology (media conditions,
      length units, `calc()`); flagged intricate/high-maintenance,
      generally advised against. Recommend new section "Responsive
      images" (include the caution).
- [ ] `__TODO__/039/html/_420-images.md:475` — image maps (`<area>`/
      `<map>`) still standard and supported but largely obsolete given
      SVG/canvas. Recommend new section "Image maps".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:749` — `<img>`:
      `src`/`width`/`height`/`alt` mandatory; no `ismap`/`usemap`;
      three formats (JPEG/PNG/SVG) with use-case guidance; `alt` rules
      (describe purpose not the image, <~50 chars; empty `alt` for
      presentational); `width`/`height` exactly matching pixel
      dimensions; data URIs for many small images; SVG via `<svg>`
      preferred. Recommend new section "Images" (reconcile across
      sources).
- [ ] `__TODO__/039/html/_todo/images-and-multimedia.md:3` —
      `width`/`height` MUST be on all images/audio/video/embedded media.
      Recommend new section "Images" / "Audio & video".

### SVG / vector graphics

- [ ] `__TODO__/039/html/_420-images.md:23` — SVG is the only web
      vector format; preferred over icon fonts (Font Awesome) and
      sprites; SHOULD be used for all graphical UI components. Recommend
      new section "Vector graphics".
- [ ] `__TODO__/039/html/_420-images.md:37` — linking vs inlining
      SVGs; inlining RECOMMENDED (fewer requests, more accessible,
      styleable); external SVGs must be self-contained (no external
      resource deps); `<object>` workaround caveats; inlined SVG `id`
      uniqueness across the document (consider Web Components/shadow DOM);
      linked SVGs MUST use `.svg` + `image/svg+xml`. Recommend new
      section "SVG linking vs inlining".
- [ ] `__TODO__/039/html/_420-images.md:71` — mandatory/recommended
      SVG attributes: `width`/`height` (mandatory, IE9-11 requires);
      `viewBox` (treat as mandatory); `x`/`y`; `version` (keep SVG 1.1
      compatible); `xmlns` (mandatory); `xmlns:xlink`; `<title>`/`<desc>`
      (accessibility, equivalent to `alt`); `role="presentation"` for
      purely presentational inlined SVG. Recommend new section "SVG
      attributes".
- [ ] `__TODO__/039/html/_420-images.md:157` — SVG filters
      (blur/colour manipulation; supported except IE≤9 / Android <4.4;
      examples TODO). Recommend new section "SVG filters".
- [ ] `__TODO__/039/html/_420-images.md:163` — SVG animation
      strategies (scripting DOM API, CSS transitions/transforms, SMIL
      `<animate>`/`<animateTransform>`; SMIL browser support;
      libraries Snap.svg/svg.js/Velocity.js). Recommend new section "SVG
      animations".
- [ ] `__TODO__/039/html/_420-images.md:179` — keyboard navigation
      considerations for inlined SVGs (cross-reference accessibility).
      Recommend new section "SVG keyboard navigation".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:777` — prefer embedding
      SVG via `<svg>` over `<img>`; six mandatory SVG attributes
      (`focusable`, `height`, `version`, `viewBox`, `width`, `xmlns`);
      `focusable="false"` to stop IE adding inlined SVGs to tab order.
      Recommend new section "SVG" (reconcile with `_420-images.md`).
- [ ] `__TODO__/039/svg/_todo/Tips for Creating and Exporting Better SVGs for the Web.URL:2`
      (https://www.sarasoueidan.com/blog/svg-tips-for-designers/) —
      see **Out-of-scope** below (designer/graphics-editor workflow).

### Audio, video & embedded media

- [ ] `__TODO__/039/html/_440-av.md:1` — Audio & Video topic (stub).
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:789` — `<audio>`/`<video>`
      treated as block-level; no `autoplay`/`loop` (users control
      playback); `muted` unreliable; `preload` advisory only; `<track>`
      WebVTT subtitles for accessibility (use despite IE9 gaps). Recommend
      new section "Audio & video".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:801` — embedded media:
      `<embed>` requires height/src/type/width; iframes (explicit
      width/height; `scrolling="no"` for Firefox; `name` vs `id`;
      `sandbox` for third-party widgets). Recommend new section "Embedded
      media & iframes".
- [ ] `__TODO__/039/html/_todo/images-and-multimedia.md:35` — iOS
      iframe scrolling workaround (scrolling="no" + framed document
      overflow handling). Recommend new section "Embedded media &
      iframes".

### Forms

- [ ] `__TODO__/039/html/_350-forms.md:3` — users MUST NOT be
      prevented from pasting into password fields (NCSC reference).
      Recommend new section "Forms" → "Passwords".
- [ ] `__TODO__/039/html/_todo/forms.md:3` — HTML5 input types
      (`number`, `search`, `range`, `email`, `date`, `url`) abstract
      validation to the browser; reference links. Recommend new section
      "Forms" → "Input types".
- [ ] `__TODO__/039/html/_todo/forms.md:18` — `<textarea>` `cols`/
      `rows` (integer, no unit); CSS overrides; tips (width 100% via
      CSS; `rows` for height with CSS `height: auto`); reset buttons
      discouraged. Recommend new section "Forms" → "Textarea".
- [ ] `__TODO__/039/html/_todo/forms.md:36` — specific-format inputs
      should offer options rather than free text where possible.
      Recommend new section "Forms".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:813` — `<form>` MUST
      encapsulate submitted input; all submitted controls inside the
      form; `action`/`method` (defaults current URL + GET);
      same-domain relative vs cross-domain absolute; `id` over `name`;
      `enctype` (`multipart/form-data` for file inputs, POST only).
      Recommend new section "Forms" → "The form element".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:833` — native
      validation/autocompletion/spellcheck disabled by default
      (`novalidate`); custom validation preferred; `spellcheck`
      guidance; `autocomplete="off"` on forms, `"on"` per free-form
      control; `autocapitalize="none"` (non-standard Safari iOS).
      Recommend new section "Forms" → "Validation & input attributes".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:860` — input-control
      allow-list (checkbox, email, file, hidden, number, password,
      radio, search, tel, text, url, select, textarea); new types
      supported, degrade to text in IE9; `range`/`datetime` not
      reliable; `name` mandatory. Recommend new section "Forms" →
      "Input controls" (reconcile with `_150-elements.md`).
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:892` — per-control
      guidance: text boxes (`maxlength`, `size` no-op); textarea
      (`cols`/`rows`); password (no default value); search; radio/checkbox
      (`value` mandatory, in `<label>`, `checked`, hidden default for
      unchecked checkboxes); `<select>` (≥12 values; no `multiple`);
      file upload (POST + multipart, `accept` advisory, `multiple`).
      Recommend new section "Forms" → "Input controls".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:1079` — `<fieldset>`
      groups related fields; every distinct field wrapped (even single
      controls); every input MUST have a label; `for`/`id` association;
      labels encapsulate checkboxes/radios; `<legend>` for grouped
      controls. Recommend new section "Forms" → "Labels, fieldsets &
      legends".

### Buttons

- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:1093` — only `<button>`
      with `type="button"` or `type="submit"`; never reset buttons or
      `<input>` button types; submit for submission, push for other
      behaviours; `name`/`value` only on submit; disable while action
      pending (prevent double-click); `autofocus`; `autocomplete="off"`
      on button. Recommend new section "Buttons".

### Hyperlinks

- [ ] `__TODO__/039/html/_300-hyperlinks.md:1` — Hyperlinks topic
      (stub).
- [ ] `__TODO__/039/html/_todo/links.md:7` — URLs MUST conform to RFC
      3986; spaces percent-encoded as `%20`; relative internal links vs
      absolute external; base URL trailing slash; `./` for homepage; no
      `../`; hash fragments match canonical URL; `rel="external"` on
      external links; avoid optional query params; never expose
      user/pass/port in published URLs. Recommend new section
      "Hyperlinks".
- [ ] `__TODO__/039/html/_todo/links.md:51` — all initially-rendered
      links MUST resolve to a useful resource; behaviour-controlling
      links generated by JS (with `href` pointing to base URL so
      right-click/open-in-new-tab works); never `javascript:` or event
      attributes in `href`; attach handlers unobtrusively. Recommend new
      section "Hyperlinks" → "JavaScript-driven links".
- [ ] `__TODO__/039/html/_todo/links.md:71` — avoid `mailto:` (use a
      form); `tel:` acceptable with `+` and country code, no trunk zero,
      no spaces/punctuation; visible text may differ from `tel:` value.
      Recommend new section "Hyperlinks" → "Telephone & email links".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:627` — `<a>` as
      block/inline special case; `href` mandatory & must resolve;
      internal links relative to base; `title` advisory only; allowed
      attributes (`download`, `hreflang`, `rel`, `target`, `type`);
      `download` unreliable in IE/Safari (use HTTP headers). Recommend
      new section "Hyperlinks" → "The anchor element".

### Metadata schemas

- [ ] `__TODO__/039/html/_250-metadata.md:1` — metadata overview;
      Schema.org + Microformats chosen; don't mix schemas; syntax vs
      vocabulary distinction. Recommend new section "Metadata".
- [ ] `__TODO__/039/html/_250-metadata.md:17` — Schema.org via RDFa
      Lite (preferred over Microdata): five attributes (`vocab`,
      `typeof`, `property`, `resource`, `prefix`); `vocab` on `<body>`;
      validate with validator.schema.org; don't double-up semantics
      already in HTML (`<main>`, `<nav>`, `<header>`, `<aside>`).
      Recommend new section "Schema.org".
- [ ] `__TODO__/039/html/_250-metadata.md:128` — Microformats
      (`rel="nofollow"` for non-endorsed/paid/user-comment links;
      `rel="license"`; `rel="tag"`); prefer Schema.org for structural
      info, Microformats for link-relationship semantics only; registry
      of `rel` values. Recommend new section "Microformats".
- [ ] `__TODO__/039/html/_250-metadata.md:162` — Open Graph protocol
      (Facebook) for social-share control via `<meta property="og:...">`;
      adopt if social media is a key channel. Recommend new section
      "Social graphs".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:442` — public pages
      extended with RDFa Lite + Schema.org, declared once on `<body>`.
      Recommend new section "Metadata" (reconcile).
- [ ] `__TODO__/039/html/_todo/metadata.md:20` — Schema.org microdata
      vs JSON-LD formats; prefer microdata for maintainability; validate
      with Google Structured Data testing tool; `data-*` for application
      data (distinct from metadata). Recommend new section "Metadata"
      (note: conflicts with `_250-metadata.md` which prefers RDFa Lite
      over Microdata — reconcile).

### Scripting & data

- [ ] `__TODO__/039/html/_todo/scripting-and-data.md:3` — adding
      JavaScript to pages; classes for CSS only, `data-*` for JS only;
      `is-`/`has-` modifier prefixes for script-added classes; `type`
      attribute defaults; inline styles only for JS transitions (e.g.
      drag-and-drop). Recommend new section "Scripting & data".
- [ ] `__TODO__/039/html/_todo/scripting-and-data.md:18` — progressive
      enhancement; ~5% lack full JS; static HTML baseline; JS-dependent
      components rendered by JS not server; prefer CSS animations over
      JS; bundle/minify/cache JS; `defer`/`async` semantics; legacy
      bottom-of-body placement; `noscript` for no-JS engines plus
      in-place messages for limited-API browsers. Recommend new section
      "Scripting & data" → "Progressive enhancement".
- [ ] `__TODO__/039/html/_todo/scripting-and-data.md:140` — `data-*`
      as the exclusive JS input mechanism; do not query by `class`/`id`;
      no inline-script parameters; server-rendered content kicks off
      behaviours; everything must work without error if enhancements
      fail. Recommend new section "Scripting & data" → "Data
      attributes".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:360` — all pages work
      without JS; "cut the mustard" feature test (`addEventListener` +
      `querySelector`); JS-dependent UI added dynamically; short
      synchronous cached init script; JS minified/cached ≥6 months;
      no inline JS; `data-*` for app parameters; `addEventListener`
      (never HTML event attributes). Recommend new section "Scripting"
      (reconcile).

### Templates

- [ ] `__TODO__/039/html/_todo/templates.md:3` — `<template>`
      element for reusable non-rendered markup (clone/modify/inject);
      browser support caveats; interim `<script type="text/template">`
      pattern. Recommend new section "Templates".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:1122` — until
      `<template>` widely supported, store client-side templates in
      `<script type="text/template">`. Recommend new section "Templates"
      (reconcile — note `<template>` is now widely supported; the
      reference is dated).

### Built-in widgets & CSP

- [ ] `__TODO__/039/html/_todo/built-in-widgets.md:3` — `<meter>`/
      `<progress>` elements; context-menu / `<menu>` topic (TODO).
      Recommend new section "Built-in widgets".
- [ ] `__TODO__/039/html/_todo/content-security-policy.md:1` —
      Content Security Policy topic (reference links only). Recommend
      new section "Content Security Policy" (also `_200-head.md:176`
      covers the CSP meta tag).

### Semantics & presentational markup

- [ ] `__TODO__/039/html/_todo/semantics.md:12` — semantic markup
      describes content not presentation; meaning delivered regardless
      of access method; separate content from presentation; use tags in
      scope only; don't reinvent the wheel. Recommend new section
      "Semantics".
- [ ] `__TODO__/039/html/_todo/semantics.md:25` — deprecated
      presentational tags to avoid (`b`, `i`, `big`, `small`, `blink`,
      `marquee`, `strike`, `tt`, `u`, `center`, `nobr`, `font`).
      Recommend new section "Presentational tags" (reconcile —
      `_150-elements.md` & `HOUSE STYLE.md` *permit* `b`, `i`, `small`
      with semantic usage guidance; this file forbids them outright).
- [ ] `__TODO__/039/html/_todo/semantics.md:45` — avoid presentational
      attributes (`border`, `align`, `valign`, `clear`); `style` attribute
      only for JS transitions. Recommend new section "Presentational
      attributes".

### i18n

- [ ] `__TODO__/039/html/_todo/i18n.md:1` — internationalisation &
      localisation topic; `dir` attribute vs CSS `direction`; `dir` as
      CSS layout toggle; `lang` usage references. Recommend new section
      "Internationalisation".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:176` — declare `lang`
      and `dir` on root `<html>`, always paired; RFC 4646 language tags
      (ISO 639-1 + ISO 3166-1 alpha-2); culture-specific locales
      preferred; `<bdo>` to override bidi; `<bdi>` for unknown direction
      (`dir="auto"` fallback). Recommend new section "Internationalisation"
      (reconcile).

### House style / coding conventions

- [ ] `__TODO__/039/html/_todo/style.md:1` — minimal markup without
      compromising semantics; well-formed & W3C-validated; lowercase
      tags/attributes; double quotes (single for JSON); boolean
      attributes valueless; explicit self-closing (`<br />`); escape
      `&`/`<`/`>`; four-space indentation (no tabs). Recommend new
      section "Coding style".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:2` — overall house
      style: written from scratch, ported components refactored, one
      author's voice; avoid superfluous `<div>`/`<span>`; prefer standard
      elements over custom controls. Recommend new section "House
      style".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:29` — indentation (4
      spaces, no tabs, block-level on new lines). Recommend new section
      "Coding style" → "Indentation".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:46` — tag names
      lowercase; every element expressly closed; XHTML self-closing
      syntax with one space; `<html>`/`<head>`/`<body>` explicitly
      included. Recommend new section "Coding style" → "Tags".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:58` — attributes
      lowercase, alphabetical order, double quotes, valueless booleans.
      Recommend new section "Coding style" → "Attributes".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:82` — `id` for hash
      fragments and DOM relationships only; hyphen-delimited lowercase
      ASCII, typically <15 chars; prefix with element node name
      (`input-`, `select-`) for relationship IDs. Recommend new section
      "Coding style" → "Identifiers".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:100` — `class` used
      exclusively for CSS hooks; never for JS DOM queries (use `data-*`).
      Recommend new section "Coding style" → "Classes".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:116` — UTF-8 file
      encoding; rarely need entities for special characters. Recommend
      new section "Coding style" → "File encoding".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:120` — escaping
      (`&`/`<`/`>`; `&quot;` inside double-quoted attributes;
      `&#039;` inside single-quoted, preferred over `&apos;`; literal
      special chars under UTF-8; zero-width space `&#8203;` for long
      URLs/emails, placed before punctuation; `&nbsp;`/`&ensp;`/`&emsp;`/
      `&thinsp;`/figure space). Recommend new section "Coding style" →
      "Escaping".
- [ ] `__TODO__/039/html/_todo/HOUSE STYLE.md:1134` — use the
      `hidden` attribute to toggle visibility (semantics for screen
      readers), preferred over CSS `display:none`/`visibility:hidden`.
      Recommend new section "Coding style" → "Visibility".

### Accessibility

- [ ] `__TODO__/039/html/_700-accessibility.md:1` — Accessibility
      topic (stub).
- [ ] `__TODO__/039/html/_todo/accessibility.md:5` — keyboard
      navigation is the cornerstone; every interactive element MUST be
      keyboard-accessible; `tabindex` (reordering, making non-interactive
      things navigable, disabling hidden controls; explicit increments
      of 100); `tabindex="-1"` for faux-hidden elements; custom
      components MUST be fully keyboard-operable. Recommend new section
      "Accessibility" → "Keyboard navigation".
- [ ] `__TODO__/039/html/_todo/accessibility.md:34` — modal popup
      focus management (focus moves to popup, nav disabled behind
      overlay, contained within popup, closable via Escape/close button,
      main nav reinstated). Recommend new section "Accessibility" →
      "Modals & focus management".
- [ ] `__TODO__/039/html/_todo/accessibility.md:43` — `accesskey`
      attribute (suggestion only, conflicts with system/AT shortcuts,
      i18n concerns); conventions for surfacing shortcuts; best practice
      is JS keyboard-event listeners instead. Recommend new section
      "Accessibility" → "Accesskey".
- [ ] `__TODO__/039/html/_todo/accessibility.md:90` — visibility &
      accessibility: `hidden` hides from all clients (semantics "not yet
      relevant"); CSS reset polyfill; hiding from some clients but not
      others (tabbed interfaces) needs media-query case-by-case
      approach; off-canvas/`text-indent`/zero-height/clip caveats;
      `print-only`/`speech-only` utility classes; screen-reader-only
      labels. Recommend new section "Accessibility" → "Visibility".
- [ ] `__TODO__/039/html/_todo/accessibility.md:186` — WAI-ARIA
      overview: roles, states, relationships; use standard HTML where
      possible; ARIA adds missing semantics (tabs, tree, tooltips,
      dialogs); some ARIA now obsolete via new HTML. Recommend new
      section "Accessibility" → "WAI-ARIA".
- [ ] `__TODO__/039/html/_todo/accessibility.md:273` — avoid
      redundant ARIA on natively-semantic elements (`<main role="main">`,
      `<nav role="navigation">`, `<button role="button">`, `required
      aria-required`, `hidden aria-hidden`); HTML5→ARIA role mappings;
      `role="presentation"` caveats. Recommend new section "Accessibility"
      → "Redundant ARIA".
- [ ] `__TODO__/039/html/_todo/accessibility.md:342` — full ARIA role
      taxonomy (alert, alertdialog, application, banner, button,
      combobox, dialog, grid, listbox, menu, tab, tablist, tabpanel,
      tooltip, tree, etc.). Recommend new section "Accessibility" →
      "ARIA roles".
- [ ] `__TODO__/039/html/_todo/accessibility.md:413` — ARIA
      states/properties (`aria-*` attributes) full list; dynamic
      state changes. Recommend new section "Accessibility" → "ARIA
      states & properties".
- [ ] `__TODO__/039/html/_todo/accessibility.md:457` — live regions
      (`aria-live` polite/assertive); announce dynamic updates.
      Recommend new section "Accessibility" → "Live regions".
- [ ] `__TODO__/039/html/_todo/accessibility.md:471` —
      `role="application"` vs `role="document"` (last-resort use).
      Recommend new section "Accessibility" → "Applications vs
      documents".
- [ ] `__TODO__/039/html/_todo/accessibility.md:487` —
      `role="presentation"` / `role="separator"` usage and caveats.
      Recommend new section "Accessibility" → "Presentational &
      separator roles".
- [ ] `__TODO__/039/html/_todo/accessibility.md:514` — labels,
      descriptions & tooltips: `aria-labelledby`, `aria-describedby`
      (multi-id, reusable), `aria-label` (lightweight, only when
      visible label absent). Recommend new section "Accessibility" →
      "Labelling & describing".
- [ ] `__TODO__/039/html/_todo/accessibility.md:563` — tooltips: no
      native element; `role="tooltip"` + `aria-describedby`; MUST be
      keyboard-activatable (focus/blur, Escape closes). Recommend new
      section "Accessibility" → "Tooltips".
- [ ] `__TODO__/039/html/_todo/accessibility.md:600` — alerts &
      dialogs: `role="alert"`, `role="alertdialog"`, `role="dialog"`;
      focus MUST move to dialog on open and return on close. Recommend
      new section "Accessibility" → "Alerts & dialogs".
- [ ] `__TODO__/039/html/_todo/accessibility.md:629` — custom
      buttons: `role="button"`, `aria-pressed`, `aria-controls`,
      `tabindex`; toolbar `role="toolbar"`; Spacebar/Enter MUST activate.
      Recommend new section "Accessibility" → "Custom buttons".
- [ ] `__TODO__/039/html/_todo/accessibility.md:697` — forms
      accessibility: `aria-invalid`, `aria-required` (only with custom
      validation), `aria-describedby` for tooltips, `aria-labelledby`
      for custom labels. Recommend new section "Accessibility" → "Forms".
- [ ] `__TODO__/039/html/_todo/accessibility.md:727` — `role="search"`
      for complex search components. Recommend new section "Accessibility"
      → "Search".
- [ ] `__TODO__/039/html/_todo/accessibility.md:749` — custom input
      controls (checkbox, radio/radiogroup, textbox, combobox, listbox,
      spinbutton, slider) with roles, `tabindex`, and keyboard events;
      `aria-checked`/`aria-activedescendant`/`aria-readonly`/
      `aria-autocomplete`. Recommend new section "Accessibility" →
      "Custom input controls".
- [ ] `__TODO__/039/html/_todo/accessibility.md:891` — accessible
      drag-and-drop (`aria-dropeffect`, `aria-grabbed`, grid roles,
      keyboard controls). Recommend new section "Accessibility" →
      "Drag-and-drop".
- [ ] `__TODO__/039/html/_todo/accessibility.md:926` — grid-like
      interfaces (`grid`/`gridcell`/`row`/`columnheader` for table-like
      layouts; not for CSS grid). Recommend new section "Accessibility"
      → "Grids".
- [ ] `__TODO__/039/html/_todo/accessibility.md:939` — tabbed
      interfaces & accordions (`tab`/`tablist`/`tabpanel`,
      `aria-expanded`/`aria-selected`, only one panel visible).
      Recommend new section "Accessibility" → "Tabs & accordions".
- [ ] `__TODO__/039/html/_todo/accessibility.md:943` — directory
      trees & treegrids (`tree`/`treeitem`/`treegrid`). Recommend new
      section "Accessibility" → "Trees".
- [ ] `__TODO__/039/html/_todo/accessibility.md:951` — custom
      navigation controls (`menu`/`menubar`/`menuitem`/
      `menuitemcheckbox`/`menuitemradio`); prefer native `<ul>` +
      `<input>` in `<nav>`. Recommend new section "Accessibility" →
      "Menus".
- [ ] `__TODO__/039/html/_todo/accessibility.md:963` — other UI
      components (`progressbar`, `scrollbar`, `status`, `timer`,
      `marquee`, `log`). Recommend new section "Accessibility" → "Other
      live-region components".
- [ ] `__TODO__/039/html/_todo/accessibility.md:977` — landmark
      roles; most superseded by HTML sectioning elements; `banner` and
      `contentinfo` still useful; `heading` role — don't (use standard
      headings). Recommend new section "Accessibility" → "Landmark
      roles".
- [ ] `__TODO__/039/html/_todo/accessibility.md:1011` — ARIA best
      practices (no nested `navigation`, no `navigation` on individual
      links, >1 descendant link, don't double-label, single `main`).
      Recommend new section "Accessibility" → "Best practices".
- [ ] `__TODO__/039/html/_todo/accessibility.md:2412` — keyboard
      navigation patterns for tabs (arrows/Home/End) and trees
      (arrows/Right-Left/Enter/Home/End). Recommend new section
      "Accessibility" → "Keyboard patterns".
- [ ] `__TODO__/039/html/_todo/accessibility.md:2542` — testing tips
      (keyboard-only testing, one-handed mobile testing in adverse
      environments, OS screen reader, real-user testing). Recommend new
      section "Accessibility" → "Testing".

### Accessibility testing checklist (WCAG-based)

- [ ] `__TODO__/039/html/_accessibility testing checklist.txt:3` —
      WCAG-four-principle accessibility checklist (Perceivable /
      Operable / Understandable / Robust) with concrete HTML-level
      requirements. Recommend new section "Accessibility checklist".
- [ ] `__TODO__/039/html/_accessibility testing checklist.txt:22`
      — text alternatives: all images `alt`; informative vs decorative;
      button values; input labels; media text; frame titles. Recommend
      new section "Accessibility checklist" → "Text alternatives".
- [ ] `__TODO__/039/html/_accessibility testing checklist.txt:37`
      — audio/video alternatives (transcripts, synchronised captions,
      audio descriptions). Recommend new section "Accessibility
      checklist" → "Time-based media".
- [ ] `__TODO__/039/html/_accessibility testing checklist.txt:49`
      — adaptable: logical source order; semantic markup for
      headings/landmarks/lists; sections or ARIA landmarks; tables for
      data only; `<fieldset>`/`<legend>` grouping; `autocomplete` on
      typed inputs; no shape/size/sound-only instructions; orientation.
      Recommend new section "Accessibility checklist" → "Adaptable".
- [ ] `__TODO__/039/html/_accessibility testing checklist.txt:68`
      — distinguishable: colour not sole method; contrast ratios
      (4.5:1 text, 3:1 large/UI components); 200% zoom; 320px responsive;
      text-spacing resilience; hover/focus-revealed content rules.
      Recommend new section "Accessibility checklist" → "Distinguishable".
- [ ] `__TODO__/039/html/_accessibility testing checklist.txt:92`
      — keyboard accessible: all functionality keyboard-operable;
      accesskey conflicts; no keyboard traps; shortcut remapping.
      Recommend new section "Accessibility checklist" → "Keyboard
      accessible".
- [ ] `__TODO__/039/html/_accessibility testing checklist.txt:101`
      — enough time: adjustable/extendable time limits; pausable
      auto-moving content. Recommend new section "Accessibility
      checklist" → "Enough time".
- [ ] `__TODO__/039/html/_accessibility testing checklist.txt:109`
      — seizures: no flashing >3×/second. Recommend new section
      "Accessibility checklist" → "Seizures".
- [ ] `__TODO__/039/html/_accessibility testing checklist.txt:115`
      — navigable: skip link; page title; logical nav order; link
      purpose from text/context; distinguishable same-text links;
      multiple ways to find pages; informative headings/labels; visible
      focus. Recommend new section "Accessibility checklist" →
      "Navigable".
- [ ] `__TODO__/039/html/_accessibility testing checklist.txt:129`
      — input modalities: single-point activation; `onclick`/`onmouseup`
      not `mousedown`; accessible name includes visible text;
      device-motion alternatives. Recommend new section "Accessibility
      checklist" → "Input modalities".
- [ ] `__TODO__/039/html/_accessibility testing checklist.txt:140`
      — readable: page `lang`; per-content `lang` for different
      languages. Recommend new section "Accessibility checklist" →
      "Readable".
- [ ] `__TODO__/039/html/_accessibility testing checklist.txt:147`
      — predictable: no focus-triggered page changes; consistent nav;
      consistent identification. Recommend new section "Accessibility
      checklist" → "Predictable".
- [ ] `__TODO__/039/html/_accessibility testing checklist.txt:156`
      — input assistance: required/format info in labels; accessible
      validation errors; fieldset/legend; error suggestions;
      reversible legal/financial changes. Recommend new section
      "Accessibility checklist" → "Input assistance".
- [ ] `__TODO__/039/html/_accessibility testing checklist.txt:168`
      — robust: valid HTML parsing (unique IDs, nesting); ARIA used
      appropriately; status messages announced via live regions.
      Recommend new section "Accessibility checklist" → "Robust".

## Partial

- [ ] `src/modules/ROOT/pages/039.adoc:25` states the *philosophy* of a "working
      standard" subset of HTML (useful, non-redundant, reliably
      supported) but provides no concrete rules. Every concrete rule in
      the reference material is therefore only partially foreshadowed,
      not actually specified. Recommend building out the new sections
      listed under **Missing**.
- [ ] `src/modules/ROOT/pages/039.adoc:19` foreshadows the redundancy concern
      (`<nav>` vs `role="navigation"` vs RDFa `SiteNavigationElement`)
      but the standard gives no rule for choosing among them. The
      reference resolves this (prefer native HTML; don't double-up —
      `__TODO__/039/html/_250-metadata.md:126` and
      `__TODO__/039/html/_todo/accessibility.md:273`). Recommend new
      section "Redundancy between HTML, ARIA, and metadata".
- [ ] `src/modules/ROOT/pages/039.adoc:17` foreshadows the unreliable-support concern
      (`<meter>` in Android WebView, `<dialog>` in Firefox/Safari) but
      the standard gives no support policy. The reference encodes a
      policy (`_150-elements.md:5`, `HOUSE STYLE.md:436` forbidden
      lists). Recommend new section "Browser support policy".

## Out-of-scope

- [ ] `__TODO__/039/svg/_todo/Tips for Creating and Exporting Better SVGs for the Web.URL:2`
      (https://www.sarasoueidan.com/blog/svg-tips-for-designers/) covers
      graphics-editor (Illustrator/Inkscape/Sketch) SVG authoring &
      export workflow — shape elements vs paths, text-to-outlines, path
      simplification, artboard fitting, export options, SVGO. This is
      designer/asset-creation guidance, not HTML authoring. Flagged for
      the user to confirm or overrule (relevant only if TS-39 expands to
      cover SVG asset production).
- [ ] `__TODO__/039/html/_todo/semantic-web.md:1` — "Semantic Web"
      background (RDF, RDF/XML, RDF Schema, OWL, Tim Berners-Lee
      provenance) is general background reading, not HTML authoring
      rules. Flagged for the user to confirm or overrule (the
      actionable subset — Schema.org/Microformats — is captured under
      **Missing** → "Metadata schemas").
- [ ] `__TODO__/039/html/_accessibility testing checklist.txt:7`
      — CI/Axe tooling configuration on the `dev` branch is process/
      tooling, not an HTML authoring rule. Flagged for the user to
      confirm or overrule.
- [ ] `__TODO__/039/html/_todo/misc.md:1` and
      `__TODO__/039/html/_todo/document-structure.md:5` and
      `__TODO__/039/html/_todo/semantics.md:5` etc. — these files
      are largely bare reference-link lists (further-reading URLs)
      without normative content. Flagged for the user to confirm or
      overrule (the underlying topics are captured under **Missing**
      where the other files give concrete rules).
- [ ] `__TODO__/039/html/_todo/Tutorials Overview • WAI Web Accessibility Tutorials.URL:2`
      (https://www.w3.org/WAI/tutorials/) — a tutorial index/landing
      page, not normative reference material. Its concrete techniques
      (images, tables, forms, menus, carousels, landmarks) are
      in-scope but are better sourced from the in-repository
      `accessibility.md`/checklist already captured under **Missing**.
      Flagged for the user to confirm or overrule.

## Unresolved

- [ ] `__TODO__/039/html/_todo/Web accessibility – Style.ONS.URL:2`
      (https://style.ons.gov.uk/category/writing-for-the-web/web-accessibility/)
      — fetch returned no textual content (the page is
      JavaScript-rendered). Not included in the comparison above.
- [ ] `__TODO__/039/html/_todo/Inclusive Components by Heydon Pickering.pdf`,
      `Introducing HTML5.pdf`, `Jump Start HTML5.pdf`,
      `HTML and CSS for the Real World.pdf` — binary PDF files, not
      read. Not included in the comparison above.
- [ ] `__TODO__/039/html/_todo/document-outline-sections.png` —
      binary image, not read. Not included in the comparison above.
- [ ] The reference material contains internal contradictions (e.g.
      `<dl>` permitted by `text-content.md` but forbidden by
      `_150-elements.md`/`HOUSE STYLE.md`; RDFa Lite preferred by
      `_250-metadata.md` but microdata preferred by `metadata.md`;
      `<b>`/`<i>`/`<small>` permitted-with-guidance by
      `_150-elements.md`/`HOUSE STYLE.md` but forbidden by
      `semantics.md`; `<base>` trailing-slash convention differs between
      `_200-head.md` and `HOUSE STYLE.md`; `<caption>` permitted by
      `tables.md` but forbidden by `HOUSE STYLE.md`). These are noted
      inline in the relevant **Missing** entries as "reconcile" — the
      standard's authors must resolve them when building the sections.