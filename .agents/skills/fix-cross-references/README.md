# Fix cross-references

This skill instructs agents to scan technical standards for broken internal
cross-references and to repair them.

It ensures that all references to other standards (TS numbers, titles, and
relative paths) are accurate and consistent across the entire project.

## What it does

Builds a reference index from `src/README.adoc` and scans `.adoc` and `.md`
files in the target scope (either a specific standard or the entire `src/`
directory).

The agent is instructed to:

- **Validate identifiers.** Ensure `TS-NNN` numbers exist in the project index.

- **Verify titles.** Check that standard titles in references (eg.
  `[TS-31: Unix Shells]`) match the index exactly.

- **Correct paths.** Calculate and fix relative paths based on the file's
  depth relative to the `src/` root.

- **Maintain consistency.** Ensure `AGENTS.md` files point to other `AGENTS.md`
  files, while `.adoc` files point to the source standards.

- **Avoid guesswork.** Mark ambiguous references as unresolved rather than
  making incorrect assumptions.

## How to invoke

> Fix references in TS-10
> Fix all broken cross-references
