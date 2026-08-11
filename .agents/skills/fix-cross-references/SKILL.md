---
name: fix-cross-references
description: >-
  Find and repair broken internal cross-references — TS numbers, titles, and
  xref/include targets — between the technical standards in this repository.
  Use when the user says "fix references in TS-<N>", "fix all broken
  cross-references", or reports that a link between standards is wrong or
  stale. Do not use it to restyle references that already resolve correctly.
compatibility: requires Read, Edit, Glob, Grep
license: CC0-1.0
---

# Fix cross-references

Find and repair broken internal cross-references between technical standards:
wrong TS numbers, stale titles, and `xref:`/`include::` targets that no longer
resolve. Repair only what is demonstrably broken, and leave anything you
cannot resolve with certainty untouched.

Two distinct reference mechanisms are in play, and a fix MUST use the right
one for the file it's in:

- **`.adoc` files** (pages and partials) use Antora resource IDs: a
  cross-standard reference is `xref:NNN-slug.adoc[TS-N: Title]`, and a page's
  own includes are `include::partial$NNN/<file>.adoc[leveloffset=+1]`. Neither
  is a relative filesystem path — the `slug` in an `xref:` target MUST match
  the target standard's current title exactly, because that's how Antora
  resolves it; there is no depth to calculate.

- **`AGENTS.md`/`GAPS.md` files** are plain Markdown, outside Antora's reach,
  and keep the older convention: a relative link to another standard's
  `AGENTS.md`, eg. `../031/AGENTS.md`. Every one of these files lives at the
  same depth (`src/modules/ROOT/partials/<NNN>/`), so this is always exactly
  one `../`, regardless of how deeply nested the source content being
  summarized is.

## Parameters

Determine the following information from the surrounding context and
environment, if possible. If you're uncertain about the required parameters,
prompt the user for clarification.

- **The scope — REQUIRED.** Either one technical standard, identified as
  `TS-<N>`, or the whole of `src/`. For a single standard, scan its page
  (`src/modules/ROOT/pages/NNN-<slug>.adoc`) and every `.adoc`/`.md` file
  under `src/modules/ROOT/partials/<NNN>/`. For a repository scan, scan every
  `.adoc` and `.md` file under `src/modules/ROOT/`. If the user does not say,
  and the context or the working directory already establishes a standard,
  treat that as the scope.

## Success criteria

- Every reference in scope that named a TS number or title MUST now match the
  standards index at `src/modules/ROOT/pages/index.adoc` exactly.

- Every `xref:`/`include::` target in scope MUST resolve to a page or partial
  that actually exists, and every `AGENTS.md`/`GAPS.md` relative link MUST
  resolve to a file that exists.

- Every reference that could not be resolved with certainty MUST still hold
  its original text, and MUST be listed in the report as unresolved. A wrong
  guess is worse than a flagged uncertainty, because it looks fixed.

- References that already resolved correctly MUST be byte-identical to how
  they started, and the surrounding AsciiDoc or Markdown construct MUST be
  unchanged around every reference that was fixed.

- Nothing MUST be staged or committed, and no file outside the scope MUST have
  been modified.

## Instructions

1.  Read the standards index at `src/modules/ROOT/pages/index.adoc` and build
    a mapping from each `TS-<N>` identifier to its official title and its
    generated page filename (`NNN-slug.adoc`). This index is the only
    authority for numbers, titles, and slugs; do not infer any of them from a
    heading inside a standard.

2.  Establish the scope, then enumerate the `.adoc` and `.md` files it covers.

3.  Find the candidate references across those files. Search for text
    matching `TS-\d{1,3}`, `xref:` and `include::` targets, `../\d{3}/`
    relative paths (in `.md` files only), and link text carrying a `TS-`
    identifier.

4.  Validate each candidate on the axes that apply to its mechanism:

    - Identifier. Does the TS number appear in the index?
    - Title. Where the reference states a title, does it match the index
      exactly?
    - `xref:`/`include::` target (`.adoc` files). Does `NNN-slug.adoc` match
      the index's current slug for that TS number? Does the `partial$`
      target exist under `partials/NNN/`?
    - Relative path (`AGENTS.md`/`GAPS.md` files only). Is it exactly
      `../NNN/AGENTS.md` — one level, never more — and does that file exist?

5.  Apply a fix only where a check failed, correcting the number, the title,
    or the target, and leaving the link syntax around it as it was. Never
    convert an `xref:` to a `link:` or vice versa — the mechanism is fixed by
    which kind of file the reference lives in, not a stylistic choice.

6.  Confirm every reference you changed now resolves, then report the fixes
    grouped by file, followed by the unresolved references and why each one
    could not be settled.

## Rules

- You MUST treat `src/modules/ROOT/pages/index.adoc` as the single source of
  truth for TS numbers, titles, and slugs.

- You MUST NOT modify a reference that already resolves. Restyling a correct
  but inconsistent reference is out of scope unless the user asks for it,
  because it inflates the diff and hides the real repairs in it.

- An `xref:` target's slug MUST be recalculated from the target standard's
  *current* title, not copied from the stale reference. A standard's title
  can change without its number changing, which silently breaks every
  `xref:` that named its old slug.

- A reference inside an `AGENTS.md` MUST point at the target standard's
  `AGENTS.md`, so that agent context chains stay compact. A reference inside
  an `.adoc` file MUST point at the target's page via `xref:`.

- You MUST NOT guess. Where a reference has more than one plausible target,
  leave it alone and report it as unresolved.

## Edge cases

- The reference is to a standard outside this repository.

  References to external standards — RFCs, ISO standards, vendor
  specifications — do not follow the `TS-<N>` pattern and MUST be left alone,
  even where they look superficially similar.

- The index lists a standard that has no page under `src/modules/ROOT/pages/`.

  The reference is broken, but you cannot repair it. Report it as a broken
  link rather than repointing it at some other standard.

- An `xref:` in an `.adoc` file carries a `#fragment` or a custom, descriptive
  link text instead of the standard's exact title (eg.
  `[TS-32: Bash → Functions]`, `[TS-1: Use cases]`).

  This is not a stylistic variant to leave alone — this repo's style guide
  (`docs/style-guide.md`) explicitly bans section-fragment links between
  standards, because a standard is published as one merged page and Antora's
  section-ID algorithm isn't worth replicating for a deep link. Antora itself
  supports `#anchor` fragments and free-form link text (that's general
  platform capability, not this repo's convention), but here the link text
  MUST always be normalized to the plain `TS-N: Title` form and any `#anchor`
  dropped, landing the reader on the page rather than a section.

- The link text has malformed nested emphasis, eg.
  `*xref:011-versioning.adoc[TS-11: *Versioning*]*`.

  The inner `*...*` around the title is never intentional — it collides with
  the outer bold the style guide already requires around the whole macro.
  Strip the inner asterisks so the title text is exactly `TS-N: Title`.

- An `AGENTS.md`/`GAPS.md` link targets `../../pages/NNN-slug.adoc` instead of
  another standard's `AGENTS.md`.

  This is not a broken cross-reference — it's the standard's own "(source)"
  self-link back to its `.adoc` page, a different and legitimate pattern.
  Only relative links of the form `../NNN/AGENTS.md` (or `GAPS.md`) pointing
  at a *different* standard fall under this skill's `../NNN/` check; leave a
  same-standard `../../pages/` self-link untouched.
