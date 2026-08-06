# Antora Cross-Referencing Between Modules and Components

Research notes on how to create links between different modules and
components ("playbooks") in an AsciiDoc Antora website. Sourced from the
official Antora documentation.

## Terminology

Antora uses specific terms, and "playbook" means something different from
what it may colloquially suggest:

- **Playbook** — the site configuration file (`antora-playbook.yml`) that tells
  Antora which content sources to aggregate and how to build the site. There is
  only one playbook per site build.
- **Component** — the top-level content unit (e.g. `docs`, `api`,
  `tutorials`). Each component has a name defined by the `name` key in its
  `antora.yml`.
- **Module** — a subdivision within a component version (e.g. `ROOT`,
  `admin`, `user`). Module names come from the directory under `modules/`.
- **Version** — a version of a component (e.g. `3.1`, `latest`).

If by "playbook" you mean a separate **documentation component**, the answer
below covers exactly that. Cross-referencing between modules and between
components both use the same mechanism: the `xref:` macro with an Antora
**resource ID**.

## The core mechanism: `xref:` + resource ID

Antora builds links using the AsciiDoc `xref:` macro, where the target is
specified as a **resource ID** rather than a literal URL. A fully-qualified
resource ID has five coordinates in this order:

```
version@component:module:family$file
```

Only the coordinates that differ from the current page's context need to be
stated. Antora fills in the rest from the current page.

## Linking patterns

### 1. Same module (simplest case)

If the current page and target page are in the **same component version and
same module**, you only need the file coordinate (the path relative to the
`pages/` family directory):

```adoc
See xref:modes.adoc[] for details.
```

The `page$` family coordinate is implicit when using `xref:`.

### 2. Different module, same component

If the target is in a **different module** of the same component version, you
must specify the module coordinate:

```adoc
See xref:admin:modes.adoc[] for admin options.
```

Here `admin` is the module name and `modes.adoc` is the file relative to that
module's `pages/` directory.

### 3. Different component (e.g. a different "playbook"/doc set)

If the target is in a **different component**, you must specify both the
component and module coordinates:

```adoc
See xref:tutorials:ROOT:getting-started.adoc[] to begin.
```

- `tutorials` = component name (from `antora.yml` `name` key)
- `ROOT` = module name
- `getting-started.adoc` = file relative to that module's `pages/` directory

If you omit the version, Antora uses the **latest** version of that component.

### 4. Specific version of a component

To target a particular version, prefix with `version@`:

```adoc
See xref:2.0@tutorials:ROOT:getting-started.adoc[] (legacy guide).
```

### 5. File in a subdirectory

If the target page lives in a subdirectory of `pages/`, the file coordinate
includes that relative path:

```adoc
See xref:admin:fields/level/terrain.adoc[] for terrain details.
```

If both pages are in the **same subdirectory**, you can abbreviate with `./`:

```adoc
See xref:./terrain.adoc[] for terrain details.
```

## Link text and fragments

- **Default link text** — If you write `xref:modes.adoc[]` with empty brackets,
  Antora uses the target page's `reftext` attribute (or its default reference
  text, typically the document title).
- **Custom link text** — `xref:modes.adoc[Configuration modes]`
- **Deep link (fragment)** — append `#anchor-id` after the resource ID, e.g.
  `xref:modes.adoc#console-options[]`. When a fragment is present and no link
  text is given, Antora displays the published URL — so always supply link
  text with fragments:
  ```adoc
  xref:modes.adoc#console-options[Console options]
  ```

## Important rules and gotchas

- **Always use the `xref:` macro (not shorthand `<<...>>`) for cross-page
  links.** The shorthand form `<<other-page.adoc#>>` technically works but is
  discouraged because it blurs the distinction between internal and external
  references and isn't supported by all extensions.
- **The family coordinate `page$` is implicit with `xref:`** — you don't write
  it for page references. You only need `page$` if you reference a page via a
  non-page macro (rare).
- **The file coordinate is always relative to the family directory (`pages/`)**,
  not to the current file. This is the most common source of confusion — it
  differs from plain AsciiDoc `include::` relative paths.
- **Module names that collide with built-in AsciiDoc macros** (like `link`,
  `menu`, `kbd`) must be escaped with a backslash, e.g.
  `mono\link:modes.adoc[]`.
- **Broken xrefs surface as build warnings** — Antora emits a warning (and
  renders the literal target text) when a resource ID doesn't resolve, so a CI
  build is a good way to catch typos.
- **Referencing non-page resources** — attachments require `attachment$`,
  images via `xref:` require `image$`, partials included via `include::`
  require `partial$`, and examples require `example$`. Pages and images
  referenced by their dedicated macros (`xref:` / image macros) don't need the
  family coordinate.

## Quick reference table

| Target location | Example `xref:` |
| --- | --- |
| Same module | `xref:modes.adoc[]` |
| Same module, subdirectory | `xref:fields/level/terrain.adoc[]` |
| Same module, same subdirectory | `xref:./terrain.adoc[]` |
| Different module, same component | `xref:admin:modes.adoc[]` |
| Different component (latest version) | `xref:tutorials:ROOT:getting-started.adoc[]` |
| Specific version of a component | `xref:2.0@tutorials:ROOT:getting-started.adoc[]` |
| With custom link text | `xref:modes.adoc[Configuration modes]` |
| Deep link to a section | `xref:modes.adoc#console-options[Console options]` |

## Sources

- [Xref Macros and Page Links](https://docs.antora.org/antora/latest/page/use-xref/)
  — the canonical guide to the `xref:` macro structure.
- [Resource ID Coordinates](https://docs.antora.org/antora/latest/page/resource-id-coordinates/)
  — the five-coordinate model and when each is required.