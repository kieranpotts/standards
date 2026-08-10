---
name: agentify
description: >-
  Compact a technical standard in this repository into a token-efficient
  AGENTS.md for AI agent consumption. Use when the user says "agentify TS-<N>",
  or asks to create, update, or refresh the AGENTS.md for a technical standard.
  Do not use this skill to edit a standard's own AsciiDoc source files.
compatibility: requires Read, Write, Edit, Glob
license: CC0-1.0
---

# Agentify

Compact a single technical standard — its `README.adoc` and every file that
README pulls in — into a token-efficient `AGENTS.md` beside the source. Carry
the normative rules and the high-signal examples across, and leave the prose,
the rationale, and the glossaries behind.

## Parameters

Determine the following information from the surrounding context and
environment, if possible. If you're uncertain about the required parameters,
prompt the user for clarification.

- **The target standard — REQUIRED.** One technical standard, identified as
  `TS-<N>`. Its number zero-padded to three digits identifies its files, so
  TS-31 is the page `src/modules/ROOT/pages/031-<slug>.adoc` plus everything
  under `src/modules/ROOT/partials/031/`. If the user does not name one, and
  the context or the working directory already establishes a standard, treat
  that as the target.

## Success criteria

- `src/modules/ROOT/partials/<NNN>/AGENTS.md` MUST exist, and MUST carry every
  normative rule from the standard's source files, either directly or by
  inheritance from a linked parent standard.

- Every `../NNN/` path in the file MUST resolve to a directory that exists
  under `src/modules/ROOT/partials/`, and every TS number and title MUST match
  the standards index at `src/modules/ROOT/pages/index.adoc`.

- Every section MUST issue a rule, instruction, or constraint that an agent
  can act on. A standalone glossary, terminology overview, or
  conceptual-background section MUST NOT survive the compaction.

- The file MUST follow the bundled template's structure: title, intro,
  `## Rules`, an OPTIONAL `## Examples`, and `## References`.

- The standard's `.adoc` source files MUST be unchanged, and nothing MUST be
  staged or committed. This skill writes exactly one file.

## Instructions

1.  Resolve the target from the standards index at
    `src/modules/ROOT/pages/index.adoc`. If the target is ambiguous, or the
    index does not list it, stop and ask the user to clarify.

2.  Read the standard in full: its page (`src/modules/ROOT/pages/<NNN>-<slug>.adoc`),
    every file it pulls in via `include::`, and any subdirectory under
    `src/modules/ROOT/partials/<NNN>/` carrying its own `README.adoc` and
    numbered files. Subdirectory content is part of the standard, not an
    appendix to it. Do not start writing until all of it is read.

3.  Establish whether `src/modules/ROOT/partials/<NNN>/AGENTS.md` already
    exists. If it does not, write it from scratch, following the bundled
    template and the rules below.

4.  If it does exist, read it in full, then reconcile it against the source
    rule by rule:

    - Add rules present in the source but absent from `AGENTS.md`.
    - Rewrite rules that contradict, or no longer match, the source.
    - Correct stale TS numbers, titles, and relative paths.
    - Fix any typos and grammar errors you meet along the way.
    - Delete non-actionable content — glossaries, prose introductions,
      background rationale, "why this matters" narration.

    You MUST NOT delete a rule from an existing `AGENTS.md` unless it
    contradicts the source. A maintainer may have added it deliberately, and
    the source may simply be behind. Non-actionable content carries no such
    risk, so it is always removable.

5.  Verify every cross-reference against `src/modules/ROOT/pages/index.adoc`,
    then review the result against the success criteria above.

## Rules

- The file MUST be token-efficient.

  `AGENTS.md` is loaded at the start of every agent task, so every token costs
  latency and money. Omit anything derivable from context, obvious to a
  competent engineer, or written to orient a first-time human reader.

- Normative statements MUST be preserved at their original strength.

  RFC 2119 keywords carry the weight of the standard. You MAY drop the
  elaboration around a requirement, but you MUST NOT paraphrase the
  requirement itself into something stronger or weaker.

- Terms a rule depends on MUST be defined inline at the point of use, in as
  few words as possible, rather than collected into a section of their own.

- Worked ✅/❌ examples SHOULD be kept. They are high signal for agents. You
  MAY trim a long example down to the smallest version that still illustrates
  the rule, but SHOULD NOT drop it unless the rule is self-evident without it.

- A rule that refers to another technical standard MUST link to that
  standard's `AGENTS.md`, eg. `../031/AGENTS.md`, never its `README.adoc`.
  This keeps agent context chains compact. The `## References` section is the
  exception: human-readable `README.adoc` links belong there.

- Where the standard extends another, the top of the file MUST say so — eg.
  "All rules from [TS-31: Unix Shells](../031/AGENTS.md) apply here." — and
  MUST NOT restate the parent's rules unless this standard overrides or
  extends them.

- The `## References` section MUST stay minimal, and every link in it MUST
  carry a short trigger condition stating when to read it. Include only the
  source `README.adoc` and any canonical external specification a rule relies
  on. Sibling "see also" links, background reading, blog posts, and vendor
  pages are human-facing and waste agent context.

## Edge cases

- The standard is a stub, holding only a heading and a placeholder.

  There is nothing to compact. Report this and ask the user whether to
  proceed anyway, rather than writing an `AGENTS.md` with no content in it.

- The source rule you are compacting comes from a nested subdirectory of the
  standard (eg. `partials/008/03-issue-types/`).

  Every `AGENTS.md` still lives flat, at `partials/<NNN>/AGENTS.md`, regardless
  of how deep the source content it summarizes is nested. A cross-reference
  to another standard is still exactly one `../` — `../031/AGENTS.md` — never
  more, no matter how deep the rule's source was.

## Assets

- [AGENTS.md template](./assets/agentify/AGENTS.md) \
  The structure to follow when writing or updating the file in steps 3 and 4.

## References

- [TS-27: Markdown](https://raw.githubusercontent.com/kieranpotts/standards/refs/heads/latest/dev/src/modules/ROOT/partials/027/AGENTS.md) \
  Read before writing, for the Markdown conventions the generated `AGENTS.md`
  MUST follow — ATX headings, no indented paragraphs, 80-character soft wraps.
