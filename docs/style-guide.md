# Style guide

This style guide defines the file layout, naming, and content structure conventions specific to authoring the
technical standards in this repository.

For prose-level writing conventions — voice, headings, terminology, citations, punctuation — see
[TS-26: Technical writing style guide](https://kieranpotts.com/standards/026). For AsciiDoc syntax generally, see
[TS-28: AsciiDoc](https://kieranpotts.com/standards/028).

[`template/`](../template/) is a complete, compliant worked example, only with lorem-ipsum body text. Copy it as the
starting point for a new standard, and treat it as the canonical demonstration of every mechanical rule below.

## Page structure

- A standard's page (`pages/NNN.adoc`) MUST begin with a level-1 title in the form `= TS-N: Title`, followed by
  `:toc: macro` and `:toc-title: Contents`, any `:link-*:` attributes, the introduction (included from
  `partials/NNN/00-introduction.adoc`), `toc::[]`, then the `include::` directives for the standard's numbered
  content files.

- Content files (`partials/NNN/01-topic.adoc`, `02-topic.adoc`, etc.) MUST start with a level-1 section header (`=`),
  which becomes a level-2 heading when included with `[leveloffset=+1]`. `00-introduction.adoc` is the only exception
  — it does not have a section header.

- `include::` directives MUST use `[leveloffset=+1]` and target their partial with the `partial$` resource ID, eg
  `include::partial$NNN/01-topic.adoc[leveloffset=+1]`.

- Cross-references to _other_ standards MUST use a bold Antora cross-reference (`xref:NNN.adoc[*TS-N: Title*]`), never a
  relative link (`link:../NNN/...`).

- Within a technical standard, all partials are merged into a ingle document from `include::` directives from the main
  page. Therefore, cross-references _within_ the same standard MUST use the explicit-anchor convention from TS-28
  (`[[id]]` / `<<id>>`), never a `link:` to the partial file.

## File naming

- Content files MUST be named with a two-digit numeric prefix followed by a hyphen and a descriptive kebab-case name,
  `01-topic-name.adoc`.

- The prefix MUST be purely numeric. A letter suffix (`01a-`, `05b-`) SHOULD NOT be used to slot a new section between
  two existing ones. Instead, renumber the files.

- Images live under `images/NNN/`, referenced from `partials/NNN/` (or the page itself) with a family-relative
  `image::NNN/<file>[]`.

- Subdirectory names under `partials/NNN/` MUST be prefixed with a two-digit number matching their position in the
  page's include order.

- File names MUST use only lowercase ASCII letters, digits, and hyphens.

## Content structure

- A standard's page MUST include all its partials via `include::` directives in the order they should appear. There
  MUST NOT be content files in a standard's `partials/NNN/` directory that are not included by the page – except
  examples, which MUST go in an `examples/` subdirectory.

- The introduction MUST be split out into its own `partials/NNN/00-introduction.adoc` partial, included from the page
  before `toc::[]`: `include::partial$NNN/00-introduction.adoc[leveloffset=+1]`. It SHOULD describe the scope and
  purpose of the standard, and SHOULD link to related standards where appropriate.

- A references section MAY be added to list external sources that informed the content of the standard. It MUST be
  split out into its own `partials/NNN/99-references.adoc` partial, included from the page after a horizontal rule:
  `include::partial$NNN/99-references.adoc[leveloffset=+1]`. See TS-26 for the entry format and the `:link-<slug>:`
  attribute rules.
