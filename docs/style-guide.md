# Style guide

This style guide defines the file-layout, naming, and content-structure conventions specific to authoring the
technical standards in this repository.

For prose-level writing conventions — voice, headings, terminology, citations, punctuation — see
[TS-26: Technical writing style guide](https://kieranpotts.com/standards/026). For AsciiDoc syntax generally, see
[TS-28: AsciiDoc](https://kieranpotts.com/standards/028).

The [`template/`](../template/) directory is a representative entry with lorem-ipsum body text. Use it as a starting
point for new technical standards.

## Page structure

- Every standard's page (`pages/NNN.adoc`) MUST begin with a level-1 title in the form `= TS-N: Title`, followed by
  `:toc: macro` and `:toc-title: Contents` attributes, then an introductory paragraph, then `toc::[]`, then the
  `include::` directives.

- Content files (`01-topic.adoc`, `02-topic.adoc`, etc., under `partials/NNN/`) MUST start with a level-1 section header
  (`=`), which becomes a level-2 heading when included with `[leveloffset=+1]`.

- All `include::` directives on a page MUST use the `[leveloffset=+1]` attribute, and MUST target their partial with
  the `partial$` resource ID, eg `include::partial$NNN/01-topic.adoc[leveloffset=+1]`.

- Cross-references to other standards MUST use an Antora `xref:` targeting the other standard's page, and MUST be
  bold: `xref:NNN.adoc[*TS-N: Title*]`. Never use relative links (`link:../NNN/...`) for cross-referencing other
  technical standards in this repository.

## File naming

- Content files MUST be named with a two-digit numeric prefix followed by a hyphen and a descriptive kebab-case name:
  `01-topic-name.adoc`.

- The prefix MUST be purely numeric. A letter suffix (`01a-`, `05b-`) MUST NOT be used to slot a new section between
  two existing ones. Instead, renumber the files. Section files are referenced by title through xrefs rather than by
  filename, so renumbering is cheap.

- Images live under `images/NNN/`, referenced from `partials/NNN/` (or the page itself) with a family-relative
  `image::NNN/<file>[]`.

- Subdirectory names under `partials/NNN/` MUST be prefixed with a two-digit number matching their position in the
  page's include order.

- File names MUST use only lowercase ASCII letters, digits, and hyphens.

## Content structure

- A standard's page MUST include all its partials via `include::` directives in the order they should appear. There
  MUST NOT be content files in a standard's `partials/NNN/` directory that are not included by the page – except
  examples (which MUST go in an `examples/` subdirectory).

- The introductory section on the page SHOULD describe the scope and purpose of the standard, and SHOULD link to
  related standards where appropriate.

- A `== References` section MAY be added at the end of the page, after a horizontal rule, to list external sources.
  References MUST NOT be split into a separate partial. The page is their only home, so that every standard carries
  its references in the same place.

- Reference entries follow the fixed four-line form — author-date, title, publisher, then a required trailing
  annotation — specified in
  [TS-26 §Referencing: References sections in the technical standards](../src/modules/ROOT/partials/026/12-referencing.adoc).

  Every external URL used on a page (References entries and inline prose links alike) MUST be declared as a
  document-level AsciiDoc attribute near the top of the page, immediately below the `:toc-title:` line, and
  referenced by name wherever it's linked: `:link-<slug>: https://...`, used as `{link-<slug>}[_Title_]`. Never
  inline a raw `https://...[text]` macro in the body. The `<slug>` SHOULD identify the source concisely, eg author-year
  (`link-brandolini-2013`) or a short topic slug for sources with no clear author (`link-worse-is-better`). Where a
  single source has more than one citable URL (eg a book and a follow-up blog post), disambiguate with a suffix:
  `link-brandolini-2013-book`, `link-brandolini-2013-blog`.

- Do not add content to stubs (standards with only a page containing placeholder text) unless explicitly asked to.
  Stubs are intentional placeholders for future work.

## Writing new content

- New section content MUST be placed in a new numbered `.adoc` file under `partials/NNN/`, not appended directly to
  the page.

- When adding a new content file, the `include::` directive MUST be inserted into the page in the correct position to
  maintain logical ordering.

- Do not reorder existing include directives unless explicitly asked to.
