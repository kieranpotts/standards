# Style guide

This style guide defines the language, formatting, and structural conventions for authoring the technical standards in this repository. It is the authoritative reference for contributors and AI agents editing content under `src/`.

For prose-level writing conventions that apply within any individual document — voice, headings, terminology, citations — see [TS-26: Technical Writing Style Guide](../src/026/README.adoc). For AsciiDoc syntax specifics, see [TS-28: AsciiDoc](../src/028/README.adoc). The repository structure and file layout are documented in [AGENTS.md](../AGENTS.md).

The capitalized words REQUIRED, MUST, MUST NOT, RECOMMENDED, SHOULD, SHOULD NOT, OPTIONAL, and MAY are to be interpreted as described in [IETF RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

## Language and tone

- All content MUST be written in American English (en-US).

- The target audience is experienced software engineers and technical leads. Content SHOULD assume familiarity with mainstream software development concepts. Foundational concepts do not need to be explained.

- Write in a direct, authoritative style. Avoid hedging language. State what the standard requires or recommends, and why — briefly.

- Use the RFC 2119 requirement keywords (MUST, SHOULD, MAY, etc.) in body prose to signal normative requirements, exactly as they are used throughout the existing standards.

## AsciiDoc formatting

- Every standard's `README.adoc` MUST begin with a level-1 title in the form `= TS-N: Title`, followed by `:toc: macro` and `:toc-title: Contents` attributes, then an introductory paragraph, then `toc::[]`, then the `include::` directives.

- Content files (`01-topic.adoc`, `02-topic.adoc`, etc.) MUST NOT contain a document-level title (level 0, `=`). They start with a level-1 section header (`=`), which becomes a level-2 heading when included with `[leveloffset=+1]`.

- All `include::` directives in a README MUST use the `[leveloffset=+1]` attribute.

- Cross-references to other standards MUST use relative AsciiDoc link syntax: `link:../NNN/README.adoc[TS-N: Title]`.

- Code blocks MUST specify the language where applicable: `[source,bash]`, `[source,sh]`, `[source,json]`, etc.

- Admonition blocks (TIP, NOTE, IMPORTANT, WARNING, CAUTION) SHOULD use the long-form open-block delimited syntax (`======`), not the single-line paragraph syntax.

- Use `''''` (four single-quotes on their own line) to insert a horizontal rule, eg. before a `== References` section.

For the full AsciiDoc language reference, see [TS-28: AsciiDoc](../src/028/README.adoc).

## File naming

- Content files MUST be named with a two-digit numeric prefix followed by a hyphen and a descriptive kebab-case name: `01-topic-name.adoc`.

- Asset directories MUST be named `_/`.

- Subdirectory names MUST be prefixed with a two-digit number matching their position in the parent README's include order.

- File names MUST use only lowercase ASCII letters, digits, and hyphens.

## Content structure

- A standard's `README.adoc` MUST include all content files via `include::` directives in the order they should appear. There MUST NOT be content files in a standard's directory that are not included by the README – except examples (which MUST go in an `examples/` subdirectory).

- The introductory section in `README.adoc` SHOULD describe the scope and purpose of the standard, and SHOULD link to related standards where appropriate.

- A `== References` section MAY be added at the end of `README.adoc` (after `''''`) to list external sources. References MUST be formatted as a bulleted list of AsciiDoc hyperlinks with a short descriptive label.

- Do not add content to stubs (standards with only a `README.adoc` containing placeholder text) unless explicitly asked to. Stubs are intentional placeholders for future work.

## Writing new content

- New section content MUST be placed in a new numbered `.adoc` file, not appended directly to `README.adoc`.

- When adding a new content file, the `include::` directive MUST be inserted into `README.adoc` in the correct position to maintain logical ordering.

- Do not reorder existing include directives unless explicitly asked to.

## Conventions

URLs containing variables are written according to [IETF RFC 6570: URI Template](https://tools.ietf.org/html/rfc6570). For example, a URL containing a variable called `account_id` would be shown as `api.example.com/v1/accounts/{account_id}`.
