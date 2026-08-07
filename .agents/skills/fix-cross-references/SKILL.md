---
name: fix-cross-references
description: >-
  Find and repair broken internal cross-references — TS numbers, titles, and
  relative paths — between the technical standards in this repository. Use
  when the user says "fix references in TS-<N>", "fix all broken
  cross-references", or reports that a link between standards is wrong or
  stale. Do not use it to restyle references that already resolve correctly.
compatibility: requires Read, Edit, Glob, Grep
license: CC0-1.0
---

# Fix cross-references

Find and repair broken internal cross-references between technical standards:
wrong TS numbers, stale titles, and relative paths that no longer resolve.
Repair only what is demonstrably broken, and leave anything you cannot resolve
with certainty untouched.

## Parameters

Determine the following information from the surrounding context and
environment, if possible. If you're uncertain about the required parameters,
prompt the user for clarification.

- **The scope — REQUIRED.** Either one technical standard, identified as
  `TS-<N>`, or the whole of `src/`. For a single standard, scan every `.adoc`
  and `.md` file under its directory — that number zero-padded to three
  digits, so TS-31 is `src/031/` — and its subdirectories. For a repository
  scan, scan every `.adoc` and `.md` file under `src/`. If the user does not
  say, and the context or the working directory already establishes a
  `src/<NNN>/` standard, treat that as the scope.

## Success criteria

- Every reference in scope that named a TS number or title MUST now match the
  standards index at `src/README.adoc` exactly.

- Every relative path in scope MUST resolve to a directory or file that exists
  on disk, calculated from the referring file's own depth below `src/`.

- Every reference that could not be resolved with certainty MUST still hold
  its original text, and MUST be listed in the report as unresolved. A wrong
  guess is worse than a flagged uncertainty, because it looks fixed.

- References that already resolved correctly MUST be byte-identical to how
  they started, and the surrounding AsciiDoc or Markdown construct MUST be
  unchanged around every reference that was fixed.

- Nothing MUST be staged or committed, and no file outside the scope MUST have
  been modified.

## Instructions

1.  Read the standards index at `src/README.adoc` and build a mapping from
    each `TS-<N>` identifier to its official title and its directory. This
    index is the only authority for numbers and titles; do not infer either
    from a heading inside a standard.

2.  Establish the scope, then enumerate the `.adoc` and `.md` files it covers.

3.  Find the candidate references across those files. Search for text matching
    `TS-\d{1,3}`, relative paths matching `\.\./\d{3}/`, and link text
    carrying a `TS-` identifier.

4.  Validate each candidate on three axes:

    - Identifier. Does the TS number appear in the index?
    - Title. Where the reference states a title, does it match the index
      exactly?
    - Path. Does the relative path lead from this file to the target, given
      how deep this file sits below `src/`?

5.  Apply a fix only where a check failed, correcting the number, the title,
    or the path, and leaving the link syntax around it as it was.

6.  Confirm every reference you changed now resolves on disk, then report the
    fixes grouped by file, followed by the unresolved references and why each
    one could not be settled.

## Rules

- You MUST treat `src/README.adoc` as the single source of truth for TS
  numbers and titles.

- You MUST NOT modify a reference that already resolves. Restyling a correct
  but inconsistent reference is out of scope unless the user asks for it,
  because it inflates the diff and hides the real repairs in it.

- You MUST calculate every relative path from the referring file's own
  distance below `src/`. A file in a standard's subdirectory reaches a sibling
  standard through `../../NNN/`, not `../NNN/`.

- A reference inside an `AGENTS.md` MUST point at the target standard's
  `AGENTS.md`, so that agent context chains stay compact. A reference inside
  an `.adoc` file MUST point at the target's `.adoc` sources.

- You MUST NOT guess. Where a reference has more than one plausible target,
  leave it alone and report it as unresolved.

## Edge cases

- The reference is to a standard outside this repository.

  References to external standards — RFCs, ISO standards, vendor
  specifications — do not follow the `TS-<N>` pattern and MUST be left alone,
  even where they look superficially similar.

- The index lists a standard that has no directory under `src/`.

  The reference is broken, but you cannot repair it. Report it as a broken
  link rather than repointing it at some other standard.
