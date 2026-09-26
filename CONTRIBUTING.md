# Contributing

These technical standards are living documents. To make changes to a technical
standard, or to create a new one, use the normal pull request workflow via
GitHub.

To create a new standard, copy the [`template/`](template/) directory's `pages/` and `partials/` contents into
`src/modules/ROOT/`, renaming `NNN` to the next available zero-padded number in each path, then replace the
lorem-ipsum content. The template mirrors the real directory layout and demonstrates the established structure and
conventions. See the [style guide](docs/style-guide.md) for the normative rules.

Write prose in `.adoc` files as one line per paragraph, list item, and table
cell, however long, and let your editor soft-wrap it. Do not hard-wrap at a
column, and do not reflow existing prose as part of an unrelated change. See
[Line wrapping](docs/style-guide.md#line-wrapping) in the style guide.
