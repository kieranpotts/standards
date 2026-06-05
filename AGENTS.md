# Technical Standards

## Project overview

This repository contains a set of general-purpose technical standards for software development, curated to support the creation of high-quality software products. The standards cover the full software development lifecycle: requirements specification, system design, code design, testing, deployment, and monitoring.

The standards are written for a technical audience — software engineers, architects, and technical leads. They are reference material, not tutorials.

Content changes MUST preserve the established document structure, writing style, and formatting conventions described below.

## Tech stack

- **Format**: AsciiDoc (`.adoc`) for all standard content. Markdown (`.md`) for repository meta-documents only (README, AGENTS, CONTRIBUTING, etc.).

- **No build tooling**: There is no build script or preview server. The AsciiDoc files are the source-of-truth and are rendered by the GitHub UI and compatible AsciiDoc readers.

## Repository structure

- `src/`: The main content. Each technical standard lives in a zero-padded numbered subdirectory (`001/`, `002/`, etc.). Each subdirectory contains a `README.adoc` entry point plus zero or more numbered content files that are included from the README.

- `src/README.adoc`: The master index of all standards.

- `docs/`: Repository meta-documentation, including the style guide (`docs/style-guide.md`).

- `template/`: Blank templates for new standards.

### Standard directory structure

```
NNN/
├── README.adoc         ← Entry point.
├── 01-<topic>.adoc
├── 02-<topic>.adoc
├── ...
└── _/                  ← Referencd images and diagrams.
```

Subdirectories (used when a topic warrants its own section with multiple files) follow the same pattern — a `README.adoc` that includes numbered files:

```
NNN/
├── README.adoc
├── 01-<topic>.adoc
├── NN-<group>/
│   ├── README.adoc
│   ├── 01-<item>.adoc
│   └── ...
└── _/
```

Subdirectory names MUST be prefixed with a two-digit number matching their position in the parent README's include order.

The `examples/` subdirectory is reserved for standalone example files (eg. template reports, worked examples) that are referenced inline from prose, but not included via `include::` directives.

## Rules

The capitalized words REQUIRED, MUST, MUST NOT, RECOMMENDED, SHOULD, SHOULD NOT, OPTIONAL, and MAY, in the context of this document and any agent instructions or skills for this project, are to be interpreted as described in [IETF RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

### Language and tone

- All content MUST be written in American English (en-US).

- The target audience is experienced software engineers and technical leads. Content SHOULD assume familiarity with mainstream software development concepts. Foundational concepts do not need to be explained.

- Write in a direct, authoritative style. Avoid hedging language. State what the standard requires or recommends, and why — briefly.

- Use the RFC 2119 requirement keywords (MUST, SHOULD, MAY, etc.) in body prose to signal normative requirements, exactly as they are used throughout the existing standards.

### AsciiDoc formatting

- Every standard's `README.adoc` MUST begin with a level-1 title in the form `= TS-N: Title`, followed by `:toc: macro` and `:toc-title: Contents` attributes, then an introductory paragraph, then `toc::[]`, then the `include::` directives.

- Content files (`01-topic.adoc`, `02-topic.adoc`, etc.) MUST NOT contain a document-level title (level 0, `=`). They start with a level-1 section header (`=`), which becomes a level-2 heading when included with `[leveloffset=+1]`.

- All `include::` directives in a README MUST use the `[leveloffset=+1]` attribute.

- Cross-references to other standards MUST use relative AsciiDoc link syntax: `link:../NNN/README.adoc[TS-N: Title]`.

- Code blocks MUST specify the language where applicable: `[source,bash]`, `[source,sh]`, `[source,json]`, etc.

- Admonition blocks (TIP, NOTE, IMPORTANT, WARNING, CAUTION) SHOULD use the long-form open-block delimited syntax (`======`), not the single-line paragraph syntax.

- Use `''''` (four single-quotes on their own line) to insert a horizontal rule, eg. before a `== References` section.

### File naming

- Content files MUST be named with a two-digit numeric prefix followed by a hyphen and a descriptive kebab-case name: `01-topic-name.adoc`.

- Asset directories MUST be named `_/`.

- Subdirectory names MUST be prefixed with the two-digit position number as described above.

- File names MUST use only lowercase ASCII letters, digits, and hyphens.

### Content structure

- A standard's `README.adoc` MUST include all content files via `include::` directives in the order they should appear. There MUST NOT be content files in a standard's directory that are not included by the README – except examples (which MUST go in an `examples/` subdirectory).

- The introductory section in `README.adoc` SHOULD describe the scope and purpose of the standard, and SHOULD link to related standards where appropriate.

- A `== References` section MAY be added at the end of `README.adoc` (after `''''`) to list external sources. References MUST be formatted as a bulleted list of AsciiDoc hyperlinks with a short descriptive label.

- Do not add content to stubs (standards with only a `README.adoc` containing placeholder text) unless explicitly asked to. Stubs are intentional placeholders for future work.

### Writing new content

- New section content MUST be placed in a new numbered `.adoc` file, not appended directly to `README.adoc`.

- When adding a new content file, the `include::` directive MUST be inserted into `README.adoc` in the correct position to maintain logical ordering.

- Do not reorder existing include directives unless explicitly asked to.
