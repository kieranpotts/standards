# TS-40: CSS

This is a compact version of technical standard TS-40 for AI agents.

Use this when writing or reviewing CSS: class naming conventions, separating
layout from content, building reusable components, modifier classes, or organizing
CSS source files.

## Rules

The capitalized words REQUIRED, MUST, MUST NOT, RECOMMENDED, SHOULD, SHOULD NOT,
OPTIONAL, and MAY are to be interpreted as described in
[IETF RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

- **Every class MUST fulfil exactly one role: layout, component, or modifier.**

  - _Layout_ classes position content. Applied to sectioning elements (`<main>`,
    `<header>`, `<footer>`, `<article>`, `<aside>`, `<address>`, `<nav>`,
    `<section>`) and `<div>`. Written `UPPER_CASE` (eg. `NAV_MAJOR`). MUST NOT
    set inheritable properties, typographic styles, or style form controls.

  - _Component_ classes encapsulate a reusable UI component built from multiple
    elements. Written `CamelCase` (eg. `NavBar`). MUST NOT be applied to
    sectioning elements.

  - _Modifier_ classes vary the default presentation of an element, component,
    or layout section. Written `lower-case` (eg. `box-shadow`). Dynamically
    injected modifiers are prefixed `is-` (`is-open`). Feature-detection classes
    are prefixed `supports-`.

  A single class MUST NOT mix these roles.

- **Prefer the cascade by default. Use classes to scope exceptions.**

  Start by giving base HTML elements sensible default styles. Use classes as
  namespaces to scope styles to a fragment of markup.

- **Keep selectors shallow and loosely coupled to HTML structure.**

  Avoid descendant/child/sibling selectors more than one level deep. Prefer a
  new class over a structural selector. Never select an element based on its
  position in the layout (eg. `.SIDEBAR h2 {}`).

- **Qualify classes defensively, except on interchangeable elements.**

  `type.class` selectors (eg. `p.dropcap`) make a class's intended context
  explicit and prevent accidental misuse. Global classes intended for universal
  use are qualified with `*` (eg. `*.clearfix`). Never qualify a class against
  `<div>`, `<span>`, or a sectioning element — these MUST remain freely
  interchangeable.

- **Use prefixes to scope modifier classes to a parent component or layout section.**

  Modifier classes belonging to a component or layout section MUST be prefixed
  with that parent's lower-cased name (eg. `headline-tagline` inside `Headline`,
  `banner-homepage` on `BANNER`), to prevent cross-contamination from unrelated
  same-named classes elsewhere in the codebase.

- **Choose class names that will outlive changes to content, position, or presentation.**

  Layout and component names SHOULD be a little abstract (`BANNER`, `AlertBox`),
  not overly literal. Modifier names SHOULD be explicit and specific (`rounded-corners`).

- **Components and modifiers MUST progressively enhance elements…**

  … and MUST NOT regressively degrade them.**

- **`data-*` attributes are the interface between HTML and JavaScript.**

  Classes are the exclusive interface between HTML and CSS. They MUST NOT
  be repurposed for anything else.

- **Avoid `!important`.**

  Prefer raising a modifier's specificity by qualifying it against the element
  types, components, or layout sections it applies to, instead of reaching for
  `!important` to beat a higher-specificity ruleset.

- **Grid systems MUST NOT be used to create page layout.**

  Use uniquely named layout sections instead (see TS-40 § Layout). Grid systems
  are acceptable as components, for arranging content within a layout section.

- **Source order matters.**

  Organize stylesheets in the following order:

  1. Raw element resets.
  2. Base element styles.
  3. Component styles (ordered alphabetically, so child components like
    `DialogAlert` follow parents like `Dialog`).
  4. Layout section styles.
  5. Modifier styles.
