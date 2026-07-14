# Technical Standards

This repository contains a set of general-purpose technical standards for
software development, curated to support the creation of high-quality software
products. The standards cover the full software development lifecycle:
requirements specification, system design, code design, testing, deployment, and
monitoring.

The standards are written for a technical audience — software engineers,
architects, and technical leads. They are reference material, not tutorials.

Content changes MUST preserve the established document structure, writing style,
and formatting conventions described below.

## Tech stack

- **Format**: AsciiDoc (`.adoc`) for all standard content. Markdown (`.md`) for
  repository meta-documents only (README, AGENTS, CONTRIBUTING, etc.).

- **No build tooling**: There is no build script or preview server. The AsciiDoc
  files are the source-of-truth and are rendered by the GitHub UI and compatible
  AsciiDoc readers.

## Project structure

- **`src/`**: The main content. Each technical standard lives in a zero-padded
  numbered subdirectory (`001/`, `002/`, etc.). Each subdirectory contains a
  `README.adoc` entry point plus zero or more numbered content files that are
  included from the README.

- **`src/README.adoc`**: The master index of all standards.

- **`docs/`**: Repository meta-documentation, including the style guide
  (`docs/style-guide.md`).

- **`template/`**: A representative entry for new standards, with lorem-ipsum
  body text that demonstrates the established document structure, formatting,
  and conventions. Copy this directory as the starting point for a new standard.

### Standard directory structure

```
NNN/
├── README.adoc         ← Entry point.
├── 01-<topic>.adoc
├── 02-<topic>.adoc
├── ...
└── _/                  ← Referenced images and diagrams.
```

Subdirectories (used when a topic warrants its own section with multiple files)
follow the same pattern — a `README.adoc` that includes numbered files:

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

Subdirectory names MUST be prefixed with a two-digit number matching their
position in the parent README's include order.

The `examples/` subdirectory is reserved for standalone example files (eg.
template reports, worked examples) that are referenced inline from prose, but
not included via `include::` directives.

## Rules

The language, formatting, file-naming, and content-structure conventions for
authoring standards are defined in the [style guide](docs/style-guide.md). Those
conventions are normative for all content under `src/`, and that document is the
single source of truth for them.


## Skills

Skills specific to this project are installed in the
[.agents/skills/](./.agents/skills/) directory.

See that directory's README for a list of the available skills and their
use cases.
