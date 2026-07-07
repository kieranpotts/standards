---
name: agentify
description: Compacts a technical standard (README.adoc + included files) into a token-efficient AGENTS.md for AI agent consumption. Use when asked to "agentify TS-N" or create/update an AGENTS.md for a technical standard.
compatibility: requires Read, Write, Edit, Bash (grep/find)
license: MIT
---

# Agentify

<!-- TODO: Review these skills against the latest template. -->

Use this skill when asked to agentify a technical standard, eg. "agentify TS-31", or when asked to create or update an `AGENTS.md` for a standard in `src/`.

Do NOT use this skill to edit the underlying `README.adoc` source files. The `.adoc` files are always the source-of-truth. This skill reads from them and writes only to `AGENTS.md`.

## Instructions

1.  **Resolve the target directory.**

    The argument is a TS identifier, eg. `TS-31` or `TS-31: Unix Shells`. Look up the correct directory number in `src/README.adoc`. The directory name is zero-padded to three digits: `src/031/`.

    If the argument is ambiguous or the standard is not in the index, stop and ask the user to clarify.

2.  **Read all source files.**

    Read `src/<NNN>/README.adoc`. It may contain `include::` directives pointing to numbered files (`01-topic.adoc`, `02-topic.adoc`, etc.) and possibly subdirectories with their own `README.adoc` and included files.

    Read every included file in full. The complete content of all included files is the source of truth — not just the top-level README.

3.  **Check whether `AGENTS.md` already exists.**

    Run: `ls src/<NNN>/AGENTS.md`

    - **Does not exist** → proceed to step 4 (create).
    - **Already exists** → proceed to step 5 (update).

4.  **Create `AGENTS.md` from scratch.**

    Write `src/<NNN>/AGENTS.md` using the template at `./assets/AGENTS.md` as the structural guide.

    Follow the compaction rules below.

5.  **Update an existing `AGENTS.md`.**

    Read the existing `AGENTS.md` in full. Then compare it against the source `.adoc` files rule by rule:

    - **Missing rules**: rules present in the `.adoc` source but absent from `AGENTS.md` — add them.
    - **Stale content**: rules in `AGENTS.md` that contradict or no longer match the `.adoc` source — update them.
    - **Stale cross-references**: TS numbers or file paths that do not match the current index in `src/README.adoc` — fix them.
    - **Typos and grammar errors**: fix any found in `AGENTS.md` while reviewing.
    - Do NOT remove rules that are present in `AGENTS.md` unless they directly contradict the `.adoc` source.

6.  **Verify cross-references.**

    Any cross-reference to another TS standard (eg. `[TS-31: Unix Shells](../031/AGENTS.md)`) MUST be validated against `src/README.adoc`. Use the index there as the single source-of-truth for current TS numbers and titles.

7.  **Review against the success criteria**, below, before finishing.

## Rules

-   **Be token-efficient.**

    `AGENTS.md` is consumed by AI agents at the start of every task. Every token costs latency and money. Omit anything that can be derived from context, is obvious to a competent IT engineer, or is only relevant to humans reading the standard for the first time.

    Do NOT reproduce extended historical rationale, prose introductions, or "why this matters" explanations unless they are necessary to apply the rule correctly.

-   **Preserve normative content exactly.**

    RFC 2119 keywords (MUST, MUST NOT, SHOULD, SHOULD NOT, MAY, RECOMMENDED, OPTIONAL) carry normative weight. Do not paraphrase them in ways that change the strength of the requirement. It is acceptable to omit non-normative elaboration, but the normative statement itself must be preserved faithfully.

-   **Keep code examples.**

    ✅/❌ examples are high signal for agents. Keep them. You may trim a long example to the smallest version that still illustrates the rule, but do not remove examples entirely unless the rule is self-evident without them.

-   **Use the template structure.**

    Follow the structure in `./assets/AGENTS.md`:

    - Frontmatter title and intro paragraph.
    - `## Rules` section — bulleted list, each rule bolded, with details below.
    - `## Examples` section — canonical full examples (OPTIONAL, include only if the source contains end-to-end examples worth preserving).
    - `## References` section — links to source standard and any closely related standards.

-   **Cross-reference other AGENTS.md files, not README.adoc.**

    When a rule refers to another technical standard, link to that standard's `AGENTS.md` (eg. `../031/AGENTS.md`), not its `README.adoc`. This keeps agent context chains compact. Exception: use `README.adoc` paths only in the `## References` section, where human-readable source links are appropriate.

-   **Inherit from parent standards explicitly.**

    If the standard extends another (eg. TS-32 Bash extends TS-31 Unix Shells), state this at the top of the file: `"All rules from [TS-31: Unix Shells](../031/AGENTS.md) apply here."` Do not re-state rules that are already covered by the parent standard unless the child standard overrides or extends them.

-   **Fix errors found in `AGENTS.md` during review.**

    Typos, grammar errors, and stale TS number references in an existing `AGENTS.md` are in scope and MUST be fixed as part of an update pass.

## Edge cases

-   **Subdirectory includes**:

    Some standards (eg. TS-8) have subdirectories like `03-issue-types/` with their own `README.adoc` and numbered include files. Read all of these — they are part of the standard.

-   **Stub standards**:

    Some standards contain only a heading and a placeholder. Do not create an `AGENTS.md` for a stub. Report to the user that the standard is a stub and ask whether to proceed anyway.

-   **Standards that extend other standards**:

    When a standard says "see also TS-N" or "extends TS-N", link to the parent's `AGENTS.md` at the top of the file and do not duplicate its rules.

-   **Relative path depth**:

    Files in subdirectories (eg. `src/008/03-issue-types/05-feature.adoc`) need `../../NNN/` to reference other standards, not `../NNN/`. Always verify path depth when writing cross-references.

## Success criteria

- **All normative rules from the source `.adoc` files are represented**, either directly in this `AGENTS.md` or by inheritance from a linked parent standard.

- **All cross-references resolve correctly.** Every `../NNN/` path matches a directory that exists in `src/`, and every TS title matches the index in `src/README.adoc`.

- **The file is token-efficient.** No extended introductory prose, no rationale paragraphs that don't change how a rule is applied, no content duplicated from a linked parent standard.

- **The template structure is followed** — title, intro, `## Rules`, optional `## Examples`, `## References`.

## References

- [AGENTS.md template](./assets/AGENTS.md): The structural template for all output files.

- [TS index](../../../src/README.adoc): The authoritative list of current TS numbers and titles. Always consult this when writing or validating cross-references.
