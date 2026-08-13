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

- **Format**: AsciiDoc (`.adoc`) for all standard content, in a native
  [Antora](https://antora.org) module — this repository is a content source
  for [kieranpotts.com](https://kieranpotts.com), consumed the same way as the
  `garden`, `thoughts`, and `bookmarks` sibling repositories. Markdown (`.md`)
  for repository meta-documents (README, AGENTS, CONTRIBUTING, etc.) and for
  each standard's `GAPS.md`/`TODO.md`, none of which are part of the
  published site.

- **No build tooling in this repository**: There is no build script or
  preview server here. The website repository runs the actual Antora build;
  this repository only has to be a valid Antora content source.

## Project structure

- **`src/antora.yml`**: The Antora component descriptor (`name: standards`).

- **`src/modules/ROOT/pages/`**: One page per technical standard,
  `<NNN>.adoc` (eg. `031.adoc`), plus `index.adoc`, the master index of all
  standards. A page is the entry point for its standard — title, intro,
  `toc::[]`, then `include::` directives pulling in that standard's partials.

- **`src/modules/ROOT/partials/<NNN>/`**: Everything else that belongs to
  standard `TS-<N>` but isn't the page itself: numbered content files
  included from the page, that standard's `GAPS.md` (and `TODO.md`, when a
  deep-dive is in progress), and any subdirectories.

- **`src/modules/ROOT/images/<NNN>/`**: That standard's referenced images and
  diagrams.

- **`src/modules/ROOT/nav.adoc`**: The component's navigation menu — every
  standard, in numeric order.

- **`docs/`**: Repository meta-documentation, including the style guide
  (`docs/style-guide.md`).

- **`template/`**: A representative entry for new standards, with lorem-ipsum
  body text that demonstrates the established document structure, formatting,
  and conventions. Copy this directory as the starting point for a new standard.

### Standard file layout

```
src/modules/ROOT/
├── pages/
│   ├── index.adoc
│   └── NNN.adoc                 ← Entry point for TS-N.
├── partials/
│   └── NNN/
│       ├── GAPS.md
│       ├── 01-<topic>.adoc
│       ├── 02-<topic>.adoc
│       ├── ...
│       └── NN-<group>/          ← Used when a topic warrants its own
│           ├── README.adoc      ←   section with multiple files.
│           ├── 01-<item>.adoc
│           └── ...
└── images/
    └── NNN/                     ← Referenced images and diagrams.
```

Subdirectories under `partials/NNN/` MUST be prefixed with a two-digit number
matching their position in the page's include order.

The `examples/` subdirectory (under `partials/NNN/`) is reserved for
standalone example files (eg. template reports, worked examples) that are
referenced inline from prose, but not included via `include::` directives.

### Cross-references

A page's `include::` directives target its own partials with the
`partial$` resource ID: `include::partial$NNN/01-topic.adoc[leveloffset=+1]`.
A partial including a sibling in the same subdirectory uses a bare relative
path, unprefixed: `include::./01-item.adoc[leveloffset=+1]`.

A cross-reference from any `.adoc` file to another standard uses an Antora
`xref:`, targeting that standard's page directly — never a relative
`link:../NNN/...` path, and never a subsection fragment (each standard is one
merged page, so a fragment would need to replicate Asciidoctor's section-ID
algorithm for no real benefit over landing on the right page):
`xref:NNN.adoc[*TS-N: Title*]`. The bold markup sits inside the macro's
brackets, tight around the link text — not wrapped around the whole macro.

`GAPS.md`/`TODO.md` files are Markdown, outside Antora's reach, and keep their
own convention: a link to another standard cites its canonical published URL,
eg. `https://kieranpotts.com/standards/031`.

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
