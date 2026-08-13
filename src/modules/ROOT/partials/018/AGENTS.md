# TS-18: Web GUIs

This is a compact version of technical standard TS-18 for AI agents.

Use this when designing or implementing web-based graphical user interfaces —
performance optimization, web accessibility (WCAG 2.2 conformance), and web font
handling. Covers client-side web GUI concerns specifically.

Do NOT use this for general application architecture (see
[TS-5: Application Architecture](../005/AGENTS.md)) or for non-web GUIs. For
broader UI guidance and usability testing see
[TS-15: User Interfaces](../015/AGENTS.md) (where it exists). Accessibility
testing process is covered by [TS-14: Performance Testing](../014/AGENTS.md).
For URL design, see [TS-63: URL Design](../063/AGENTS.md).

## Rules

### Performance optimization

- **Web GUIs SHOULD be designed to be as fast and responsive as possible.**

  The following optimizations are RECOMMENDED:

  - **Server-render** as much HTML as possible, preferably all of it. The
    browser's native HTML engine always renders HTML faster than custom
    client-side JavaScript can.
  - **Pre-fetch** as much HTML as possible. On link hover, the browser can
    pre-fetch the linked page. Further optimization: client-side JS pre-fetching
    _partial_ HTML and dynamically inserting it into the application's *shell*
    (global areas like navigation and footer usually don't require re-rendering
    on navigation).
  - Use `<link rel="preload">` in the HTML `<head>` to suggest the browser
    preload assets (CSS, JavaScript, web fonts), reducing blocking requests
    before initial render.
  - Use `<link rel="dns-prefetch">` to pre-fetch DNS records for third-party
    domains (CDN, third-party services, any assets not served from the same
    domain as the page).
  - Use a CDN to store and serve static assets.
  - Use a proxy tool (eg. Squid) to cache dynamic content pre-rendered by the
    server.
  - Use client-side HTTP **caching** aggressively (eg. `Cache-Control` header
    to specify how long a resource should be cached by the browser).
  - Use a client-side **service worker** to cache pre-rendered HTML and other
    dynamically-fetched assets (the service worker intercepts requests and
    serves cached versions; also helpful for offline support).
  - **Inline CSS** in a `<style>` tag in the HTML `<head>`, uglified. This
    SHOULD be restricted to just your *critical CSS* — the minimum CSS required
    to do an initial render. Additional CSS (required only for an enhanced UX)
    should be deferred until after the page renders. If the overall CSS size is
    small, it can all be inlined. This lets the browser start rendering as soon
    as HTML is received, without waiting for separate CSS resources — giving
    the fastest possible time to first paint (the Largest Contentful Paint /
    LCP metric: the time to fully render the largest element on the page, after
    all styles, fonts, images, and other dependencies are fetched).
  - For JavaScript, serve only the subset required to enable dynamic
    functionality on the current page. This is **code splitting** (tools
    available to do this automatically at compile time or dynamically on the
    server). Avoid loading _all_ your JavaScript on _all_ your pages.
  - Consider **lazy loading** additional JavaScript that enhances the UX but
    is not required for core functionality.
  - Put fixed `width` and `height` attributes on images, or use an inline
    `style` attribute to set `width` and `height` CSS properties on the images'
    containers. This lets the browser allocate space for an image before
    download, preventing the page from jumping as images load (counts as
    another re-render).
  - Don't be afraid to use age-old techniques like **image sprites** to reduce
    the number of requests for product thumbnails, icons, and other small
    images.

### Web accessibility

- **Web GUIs MUST be accessible to all users, including those with visual,
  auditory, motor, and cognitive disabilities.**

  All web GUIs SHOULD aim to conform with the
  [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/WAI/standards-guidelines/wcag/),
  the international standard for web content accessibility. The most recent
  version is WCAG 2.2. Conformance is measured at three levels: Level A
  (minimum), Level AA (standard), and Level AAA (enhanced). **Level AA is the
  target RECOMMENDED by this standard**, and is required by law in many
  jurisdictions. WCAG 2.2 defines success criteria organized under four
  principles.

#### 1. Perceivable

- **All content MUST be presentable to users in ways they can perceive.**

  - **Text alternatives**: All images and non-text content (icons, charts,
    audio, controls) MUST have a descriptive text alternative conveying their
    meaning. Purely decorative images SHOULD use empty `alt=""` (and optionally
    `role="presentation"`) so assistive technologies skip them.
  - **Time-based media**: Pre-recorded video with audio MUST have synchronized
    captions covering all speech and relevant sound effects. Pre-recorded
    audio-only content MUST have a text transcript. Pre-recorded video-only
    content MUST have an audio description or text alternative. Live video
    with audio MUST include real-time captions.
  - **Adaptable**: Visual information and relationships (headings, labels,
    groupings) MUST be communicated in code using semantic HTML elements (eg.
    `<label>`, `<ul>`, `<h1>`) or ARIA attributes. Content MUST appear in a
    logical reading order in source regardless of visual presentation.
    Instructions MUST NOT rely solely on sensory properties (color, shape,
    size, position) to convey meaning. Content MUST remain readable and usable
    in both portrait and landscape orientations. Common form fields (name,
    email, address) SHOULD use the `autocomplete` attribute to enable browser
    autofill.
  - **Distinguishable**: Color MUST NOT be the only means of conveying
    information — pair it with a supplementary cue (text label, icon,
    underline, pattern). Audio playing automatically for more than 3 seconds
    MUST be pausable or stoppable without relying on system-wide volume
    controls. Normal-sized text MUST have a contrast ratio of at least 4.5:1
    against its background; large text (over 24px regular, or over 19px bold)
    requires at least 3:1. Text MUST remain readable when zoomed to 200%. Text
    SHOULD be real text, not images of text (except for logotypes and other
    essential visual treatments). Content MUST reflow to a single column at a
    viewport width of 320px without requiring horizontal scrolling. Interactive
    controls and meaningful graphics MUST have a contrast ratio of at least
    3:1 against adjacent colors. Layout MUST NOT break when custom text spacing
    is applied (increased line height, letter spacing, word spacing).
    Tooltip-style content appearing on hover or keyboard focus MUST be
    dismissible (eg. via Escape), hoverable, and persistent until dismissed.

#### 2. Operable

- **All UI components and navigation MUST be operable by all users.**

  - **Keyboard accessible**: All functionality MUST be operable using a keyboard
    alone, unless the task inherently requires freehand input (eg. drawing).
    Focus MUST never become trapped in a UI component — it MUST always be
    possible to move focus in and out using standard keyboard controls.
    Single-character keyboard shortcuts, if used, MUST be remappable to include
    a modifier key or disableable entirely.
  - **Enough time**: Time limits SHOULD be avoided unless essential to the
    task. Where used, users MUST be able to turn them off, adjust to at least
    10x the default, or extend on request. Moving, scrolling, blinking, or
    auto-updating content persisting more than 5 seconds MUST be pausable,
    stoppable, or hideable.
  - **Seizures and physical reactions**: Content MUST NOT flash or flicker more
    than three times per second, unless the flash falls within safe size and
    luminance thresholds. Animations triggered by user interaction SHOULD be
    suppressible via the `prefers-reduced-motion` CSS media query or a
    site-level toggle.
  - **Navigable**: A skip-navigation mechanism MUST be provided so keyboard
    users can bypass repeated header and navigation blocks and jump directly
    to main content. Every page MUST have a unique, descriptive `<title>`.
    Keyboard focus order MUST follow a logical, meaningful sequence matching
    the reading order. The purpose of each link MUST be clear from the link
    text alone, or in combination with surrounding context. At least two
    methods MUST be available to locate pages or content (eg. a navigation
    menu and a site search). Headings and form labels MUST be descriptive. A
    visible focus indicator MUST always be shown when navigating via keyboard.
    Focused elements MUST NOT be fully obscured by sticky headers, banners, or
    other overlapping content.
  - **Input modalities**: Functionality relying on multi-point or path-based
    gestures (swiping, pinching) MUST also have an alternative that works with
    a single pointer (tap or click). Actions MUST trigger on pointer release
    (mouse-up or finger lift), not on press, so accidental activations can be
    cancelled by moving the pointer away before releasing. The visible label
    text of a button, link, or form field MUST also be present in its
    accessible (programmatic) name in the code, so voice control users can
    activate it by speaking the visible label. Functionality triggered by
    device motion (shaking, tilting) MUST also be achievable without motion,
    and motion-based input MUST be disableable. Touch and click targets MUST
    be at least 24x24px.

#### 3. Understandable

- **Content and UI behavior MUST be understandable by all users.**

  - **Readable**: Every page MUST identify its primary language using the
    `lang` attribute on the `<html>` element. Passages of content in a
    different language MUST be marked with the correct `lang` attribute on the
    containing element.
  - **Predictable**: No unexpected context change MUST occur when an element
    receives focus (eg. auto-opening a popup or navigating away). Changing a
    form field's value MUST NOT trigger unexpected context changes
    (auto-submitting the form, reloading the page). Navigation MUST appear in
    a consistent location and order across pages. Elements performing the same
    function MUST be labeled and behave consistently across the site. Help
    options (contact link, support widget) MUST appear in the same location
    across pages.
  - **Input assistance**: All form fields MUST have clear, descriptive labels
    or instructions. Errors and validation failures MUST be identified and
    described in text, not just by color or visual styling. Error messages
    MUST include a suggestion for how to fix the problem where possible.
    Before submitting forms that trigger consequential actions (payments, legal
    submissions), users MUST be able to review, correct, or confirm their input.
    Users MUST NOT be required to re-enter information already provided earlier
    in the same process. Authentication MUST NOT rely solely on memorized
    information — copy-paste, password managers, and alternative authentication
    methods (email magic links) MUST be supported.

#### 4. Robust

- **Content MUST be robust enough to be reliably interpreted by current and
  future assistive technologies.**

  - All interactive elements MUST expose an accessible name (what the element
    is), the correct semantic role (what it does), and any current value or
    state, so assistive technologies such as screen readers can correctly
    identify and interact with them.
  - Use semantic HTML elements wherever possible — supplemented by ARIA roles
    and properties only where native semantics are insufficient.
  - Status messages (form confirmation notices, error summaries, live content
    updates) MUST be coded using appropriate ARIA live-region roles (such as
    `role="status"` or `role="alert"`), so assistive technologies announce them
    without requiring keyboard focus to move to the message element.

### Fonts

- **Web fonts are part of the critical rendering path and MUST be treated with
  the same care as any other performance-critical asset.**

  They directly affect performance metrics such as largest contentful paint
  (LCP) and cumulative layout shift (CLS).

- **Serve only WOFF2 in modern web applications.**

  WOFF2 is the only web font format that SHOULD be served. It has universal
  browser support and is the most compressed and efficient format. Legacy
  formats (WOFF, TTF, OTF, EOT, SVG fonts) SHOULD NOT be served — they impose
  a performance cost on every visitor with no benefit for modern browsers.

- **Self-host fonts rather than loading from third-party CDNs (eg. Google
  Fonts).**

  Third-party font services add DNS lookups and network latency, leak visitor
  data to the third party (a GDPR concern in many jurisdictions), and provide
  no practical caching benefit (modern browsers partition caches per origin,
  so a font fetched on one site is never reused on another). Font files SHOULD
  be given long `Cache-Control` lifetimes (months up to a year), with
  versioned file names used for cache-invalidation when fonts change.

- **Subset fonts so only the glyphs actually needed are served.**

  A complete font family can be several hundred kilobytes or more; most glyphs
  are typically never rendered. Tools such as `fonttools` (`pyftsubset`),
  Glyphhanger, and Subfont can automate subsetting. Use the `unicode-range`
  descriptor in `@font-face` declarations to declare separate `@font-face`
  blocks per script (Latin, Latin Extended, Cyrillic); the browser downloads
  only the subsets it needs for the current page. Be conservative when
  subsetting non-Latin scripts (Arabic, Devanagari, CJK) — these rely on
  shaping tables (GSUB/GPOS) and contextual forms, so aggressive subsetting can
  break word rendering entirely. Test non-Latin subsets thoroughly.

- **Inline `@font-face` declarations in a `<style>` block in the HTML `<head>`;
  never use `@import`; preload critical fonts.**

  Fonts declared in external CSS are not discovered until that stylesheet is
  downloaded and parsed, delaying font requests unnecessarily. Each `@import`
  adds a sequential round trip before the font can be discovered, pushing font
  requests very late in the render waterfall. Preload critical fonts using
  `<link rel="preload" as="font" type="font/woff2" crossorigin>` in the `<head>`
  — this instructs the browser to begin fetching immediately, rather than
  waiting to encounter the `@font-face` rule. Preload only the subset(s) needed
  for above-the-fold content; preloading every subset defeats the purpose by
  forcing all of them to download regardless of need. Consider HTTP 103 Early
  Hints to push critical font preload hints before the main HTML response is
  delivered, reducing time-to-text on the first round trip.

- **Use `font-display` to control rendering during font load; `swap` is the
  RECOMMENDED default.**

  `font-display: swap` renders fallback text immediately and swaps to the
  custom font when it arrives, preventing invisible text. Consider
  `font-display: optional` for decorative or non-critical fonts — it permits
  the browser to skip the custom font entirely on slow connections.

- **Design a robust system font stack as the fallback for every custom font;
  treat fonts as progressive enhancement.**

  The page MUST be fully legible and usable even if a custom font never loads.
  Tune fallback metrics to minimize CLS when a custom font swaps in: use the
  `size-adjust`, `ascent-override`, `descent-override`, and
  `line-gap-override` descriptors inside `@font-face` to align the dimensions
  of the custom font with those of the fallback, so text does not reflow
  visibly when the swap occurs.

- **Use variable fonts only when they genuinely reduce payload.**

  Variable fonts (encoding multiple weights, widths, and styles in a single
  file) SHOULD be used when they genuinely reduce payload compared to loading
  multiple static font files. They are not a universal win — if only one or
  two weights are needed, separate static WOFF2 files subsetted to the required
  glyphs may be smaller. Audit and measure the payload before committing to a
  variable font. Variable fonts SHOULD be subsetted and scoped using
  `unicode-range` in the same way as static fonts.

- **Icon fonts MUST NOT be used.**

  They are inaccessible (screen readers announce their private-use Unicode
  characters as gibberish), fragile if the font file fails to load, and
  wasteful (the entire font file must be downloaded even when only a handful of
  icons are used). Use inline SVGs or SVG sprites instead — they are semantic,
  accessible, styleable with CSS, and can be loaded on demand.

## References

- [TS-18 source](../../pages/018.adoc)
- [TS-5: Application Architecture](../005/AGENTS.md)
- [TS-14: Performance Testing](../014/AGENTS.md)
- [TS-63: URL Design](../063/AGENTS.md)
- [WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/)
- [WCAG in Plain English](https://aaardvarkaccessibility.com/wcag-plain-english/)
