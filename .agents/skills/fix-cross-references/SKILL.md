---
name: fix-cross-references
description: >-
  Finds and fixes broken internal cross-references (TS numbers, titles, and
  relative paths) between technical standards. Use when asked to
  "fix references in TS-N" or "fix all broken cross-references".
compatibility: requires Read, Write, Edit, Bash (grep/find)
license: MIT
metadata:
  interactive: no
  preferred_model: prose-writing
---

# Fix cross-references

**Input:** You may be given a specific target technical standard (eg. TS-10) or
asked to perform a project-wide scan. If the target is a specific standard, you
MUST verify its existence in `src/README.adoc`. If the request is ambiguous,
prompt the user for clarification.

**Output:** You MUST update the files containing broken references and report all
changes made. If a reference cannot be resolved with certainty, you MUST leave it
untouched and list it in the "Unresolved" section of your report. Do NOT commit
changes.

## Instructions

1.  **Build reference index.**

    Read `src/README.adoc` to create a mapping of technical standard identifiers
    (eg. `TS-31`) to their official titles and directory paths (eg. `src/031/`).

2.  **Determine scan scope.**

    - **Specific standard:** Scan all `.adoc` and `.md` files within
      `src/<NNN>/` and its subdirectories.

    - **Project-wide:** Scan all `.adoc` and `.md` files within the `src/`
      directory.

3.  **Identify cross-references.**

    Search for patterns indicating a reference to another technical standard.
    This includes:

    - Text matching `TS-\d{2,3}`.
    - Relative paths matching `\.\./\d{3}/`.
    - Link text containing `TS-` identifiers.

4.  **Validate each reference.**

    For every identified reference, check the following:

    - **Identifier validity.** Does the `TS-NNN` number exist in the index?

    - **Title accuracy.** If a title is provided (eg. `TS-31: Unix Shells`),
      does it match the index exactly?

    - **Path correctness.** Does the relative path correctly lead from the
      current file to the target standard's directory?

5.  **Apply fixes.**

    Update the file with the correct TS number, title, and relative path.
    Maintain the original formatting and link style.

6.  **Review and report.**

    Verify that all modified references now resolve correctly. Provide a
    summary of changes, grouped by file.

## Rules

-   **Single source of truth.** Only use `src/README.adoc` to verify TS
    numbers and titles.

-   **Precision.** Only modify references that are demonstrably broken. Do
    not "clean up" references that are technically correct but stylistically
    inconsistent, unless specifically asked.

-   **Path depth integrity.** Always calculate relative paths based on the
    current file's distance from the `src/` root.

-   **Preserve formatting.** If a reference is part of a specific AsciiDoc or
    Markdown construct (eg. a link or a list item), do not alter the
    surrounding syntax.

-   **Standard-specific targets:**

    - References within `.adoc` files should typically point to `README.adoc`
      or other `.adoc` files.

    - References within `AGENTS.md` files MUST point to the target's `AGENTS.md`
      (as per the `agentify` skill convention).

## Edge cases

-   **External standards.** References to standards outside the `src/` directory
    (eg. official RFCs or external industry standards) that do not follow the
    `TS-NNN` pattern MUST be ignored.

-   **Stubs.** If a reference points to a standard that exists in the index but
    has no corresponding directory in `src/`, report it as a broken link.

-   **Multiple matches.** If a search returns multiple potential candidates for
    a reference, do not guess. Mark it as unresolved.

## Success criteria

-   **All identified broken internal references** in the target scope have been
    corrected.

-   **All corrected TS numbers and titles** match `src/README.adoc` exactly.

-   **All relative paths** correctly resolve to the target directory based on the
    current file's depth.

-   **No valid references were accidentally altered.**

-   **A clear report** listing fixed and unresolved references was provided.
