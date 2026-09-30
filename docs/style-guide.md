# Style guide

This style guide defines the file layout, naming, and content structure conventions specific to authoring the
technical standards in this repository.

For prose-level writing conventions — voice, headings, terminology, citations, punctuation — see
[TS-26: Technical Writing Style Guide](https://kieranpotts.com/standards/026). For AsciiDoc syntax generally, see
[TS-28: AsciiDoc](https://kieranpotts.com/standards/028).

[`template/`](../template/) is a complete, compliant worked example, only with lorem-ipsum body text. Copy it as the
starting point for a new standard, and treat it as the canonical demonstration of every mechanical rule below.

## Page structure

- A standard's page (`pages/NNN.adoc`) MUST begin with a level-1 title in the form `= TS-N: Title`, followed by
  any `:link-*:` attributes, the introduction (included from `partials/NNN/01-introduction.adoc`), then the `include::`
  directives for the standard's numbered content files.

- Content files (`partials/NNN/02-topic.adoc`, `03-topic.adoc`, etc.) MUST start with a level-1 section header (`=`),
  which becomes a level-2 heading when included with `[leveloffset=+1]`. `00-attributes.adoc and `01-introduction.adoc`
  are the only exceptions — they do not have a section header.

- `include::` directives MUST use `[leveloffset=+1]` and target their partial with the `partial$` resource ID, eg.
  `include::partial$NNN/01-topic.adoc[leveloffset=+1]`.

- Cross-references to _other_ standards MUST use a bold Antora cross-reference (`xref:NNN.adoc[*TS-N: Title*]`), never a
  relative link (`link:../NNN/...`).

- Within a technical standard, all partials are merged into a ingle document from `include::` directives from the main
  page. Therefore, cross-references _within_ the same standard MUST use the explicit-anchor convention from TS-28
  (`[#id]` / `<<id>>`), never a `link:` to the partial file.

## Line wrapping

- Prose in `.adoc` files MUST NOT be soft wrapped. Each paragraph, list item, admonition, description-list entry, and
  table cell MUST sit on a single source line, however long. A soft wrap that falls inside a bold or italic span, a
  link macro, or an `xref:` can silently break its rendering. Leave visual wrapping to the editor.

- Verbatim content (source, listing, literal, passthrough, and verse blocks) keeps its own line structure, and a line
  ending in a hard line break (` +`) is intentional. Examples of AsciiDoc markup inside verbatim blocks SHOULD follow
  the same one-line-per-paragraph rule, so the examples demonstrate it.

This reiterates the normative rule in [TS-28: AsciiDoc § Line length and wrapping](https://kieranpotts.com/standards/028), which takes precedence. This Markdown file, like the repository's other Markdown files, is governed by [TS-27: Markdown § Line length and wrapping](https://kieranpotts.com/standards/027) instead, which now carries the same rule. Markdown files in this repository that are still soft wrapped are awaiting that conversion.

## File naming

- Content files MUST be named with a two-digit numeric prefix followed by a hyphen and a descriptive kebab-case name,
  `01-topic-name.adoc`.

- The prefix MUST be purely numeric. A letter suffix (`01a-`, `05b-`) SHOULD NOT be used to slot a new section between
  two existing ones. Instead, renumber the files.

- The one exception to the numeric prefix is TS-26. Its topics are a flat, alphabetical reference, so its topic files
  are named by topic alone (`a-an.adoc`, `abbreviations.adoc`, ...) and included in alphabetical order, so that the
  include order can be read straight from the file listing. Its `00-attributes.adoc`, `01-introduction.adoc`, and
  `99-references.adoc` keep their numeric prefixes, so they sort first and last. Do not use this exception for any
  other standard.

- Images live under `images/NNN/`, referenced from `partials/NNN/` (or the page itself) with a family-relative
  `image::NNN/<file>[]`.

- Subdirectory names under `partials/NNN/` MUST be prefixed with a two-digit number matching their position in the
  page's include order.

- File names MUST use only lowercase ASCII letters, digits, and hyphens.

## Content structure

- A standard's page MUST include all its partials via `include::` directives in the order they should appear. There
  MUST NOT be content files in a standard's `partials/NNN/` directory that are not included by the page – except
  examples, which MUST go in an `examples/` subdirectory.

- The introduction MUST be split out into its own `partials/NNN/01-introduction.adoc` partial:
  `include::partial$NNN/01-introduction.adoc[leveloffset=+1]`. It SHOULD describe the scope and
  purpose of the standard, and SHOULD link to related standards where appropriate.

- A references section MAY be added to list external sources that informed the content of the standard. It MUST be
  split out into its own `partials/NNN/99-references.adoc` partial:
  `include::partial$NNN/99-references.adoc[leveloffset=+1]`. The partial itself holds only the `*` bullet entries —
  every `:link-<slug>:` attribute, whether it's cited in the references list, the introduction, or elsewhere in the
  body, is declared once in the single page-top attribute block described above, sorted alphabetically by slug.

- A references section is a bibliography, not a plain link list. Each entry MUST be one `*` bullet on a single source
  line, in this fixed order. It is a reduced form of the citation format in TS-26, with a link on the title and a
  closing period.

  ```asciidoc
  * <author> (<year>). {link-<slug>}[_<title>_].
  ```

- Entries MUST be ordered as TS-26 (Citations) describes for a bibliography. The URL MUST NOT be inlined in an entry.
  Reference it by its `{link-<slug>}` attribute. An entry cites one work and carries one link. Where a source has no
  clear individual author, cite the organization or site as the author.

- Omit the publisher from an entry, unless the name of the site or publication is how readers recognize the source. In
  that case, write it after the linked title. Omit any other annotation. The linked title is enough to identify the
  source, and a reader who needs more follows the link.
