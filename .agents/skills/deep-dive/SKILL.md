---
name: deep-dive
description: >-
  Performs a deep review of a technical standard, producing a tiered
  remediation plan (TODO.md) and then working it tier by tier. Use when asked
  to "deep dive TS-N", "review TS-N thoroughly", or to continue an existing
  review from its TODO.md.
compatibility: requires Read, Write, Edit, Bash (grep/git/python3)
license: MIT
metadata:
  interactive: yes
  preferred_model: prose-writing
---

# Deep dive

**Input:** A single technical standard, eg. TS-1. You MUST prompt the user to
confirm the target if it is not obvious from context. If a `TODO.md` already
exists in the standard's directory, this is a resumption of a prior deep dive.
Read `TODO.md` to catch up with the current state of the deep dive.

**Output:** A `TODO.md` in the standard's directory recording every finding, and
— once the user approves working through it — edits to the standard itself. You
MUST save changes to disk. You MUST NOT commit. The user commits between tiers.

## Instructions

1.  **Resolve the target and check for an existing review.**

    Look up the standard in `src/README.adoc`. The directory is zero-padded to
    three digits — TS-1 is `src/001/`.

    Run `ls src/<NNN>/TODO.md`. If it exists, this is a resumption. Read the
    `TODO.md` file, identify the first unchecked item, and report the remaining
    scope to the user before doing any work.

2.  **Read everything, in full.**

    Read `src/<NNN>/README.adoc` and every file it pulls in via `include::`,
    including any subdirectories with their own `README.adoc`. Also read the
    standard's `AGENTS.md`, if one exists.

    Then read the yardsticks you will measure against:

    - `docs/style-guide.md` — normative for everything under `src/`.
    - `src/026/` (TS-26: Technical Writing Style Guide) — prose conventions.
    - `src/028/` (TS-28: AsciiDoc) — syntax, links, and line-length rules.
    - `src/027/` (TS-27: Markdown) — applies to `TODO.md` and `AGENTS.md`.
    - `template/` — the reference structure for a standard.

    Name these four in the `TODO.md` header, so a reader knows what the
    findings were measured against.

    Do NOT begin the review until every source file is read.

3.  **Sample sibling standards for de-facto conventions.**

    Where the style guide is silent on a style, look for patterns in a sample
    of other technical standards:

    ```bash
    grep -ln "^== References" src/*/README.adoc | wc -l
    ls src/*/[0-9][0-9][a-z]-*.adoc
    ```

4.  **Collect findings into the seven categories.**

    Work through the standard looking for each category in turn. Do not stop at
    the first defect in a file. Read the whole file for each category.

    1.  **Contradictions.** The same rule stated two ways. These are the most
        damaging defects, because a reader cannot comply with both. Search
        especially for a rule restated in a second location that has since
        drifted.

    2.  **Factual errors.** Claims about a language, protocol, or standard that
        are wrong. Verify anything checkable against primary sources rather
        than against your own recollection.

    3.  **Structural problems.** Examples: content in the wrong section; a
        section that has become a catch-all; the same material at length in two
        places; an ordering that contradicts the prose describing it.

    4.  **Coverage gaps.** A rule the standard implies but never states, or a
        case it does not handle. Identify these by asking what a reader would
        need that the standard does not give them.

    5.  **Convention conformance.** Divergences from `docs/style-guide.md`,
        TS-26, TS-27, and TS-28 — eg. file naming, references, quotes, dashes,
        bold lead-ins, line length, link syntax.

    6.  **`AGENTS.md` drift.** Compare it rule-by-rule against the source.
        Look for rules it invents, rules it omits, and rules whose strength it
        has changed. This file is acted on by agents, so its defects propagate.

    7.  **Prose defects.** Typos, hedging, filler, unfalsifiable normative
        statements ("as early as possible"), first-person "we", and examples
        that do not demonstrate the rule they illustrate.

5.  **Write `TODO.md`.**

    Use the structure in `./assets/TODO.md`. Every finding MUST have:

    - A checkbox (`- [ ]`), so progress is visible at a glance.
    - A plain `<file>:<line>` reference to the defect, eg. `07-qualities.adoc:43`.
    - A statement of *why* it is a defect, not merely that it is one.

    Keep findings as flat bullets. Do not introduce sub-headings, tables, or
    per-finding subsections. The file is a working checklist, and nesting makes
    it harder to scan and to tick off.

    Assign each finding to a tier, and order the tiers by dependency:

    | Tier | Category | Rationale |
    | --- | --- | --- |
    | 1 | Correctness | A contradiction makes the standard unusable. |
    | 2 | Coherence | Structure must settle before content is added. |
    | 3 | Completeness | Gaps are filled into a settled structure. |
    | 4 | Conventions | Cosmetic; do last, when content has stopped moving. |

    This order is not arbitrary. Fixing conventions first means re-fixing them
    after the content moves.

6.  **Present the plan and stop.**

    Report the tier counts and the items needing a user decision. Do NOT begin
    remediation until the user asks. The plan has standalone value.

7.  **Work one tier at a time.**

    When the user asks you to proceed, take exactly one tier. Within it:

    - Apply the fixes.
    - Tick each checkbox and append what was done, in the same bullet.
    - Update the `**Status:**` line.
    - Verify (step 8).
    - Report, and stop. The user commits before the next tier.

    Where an item turned out to need no change, or was resolved differently
    from how it was written, say so in the bullet rather than deleting it. A
    finding that was wrong is itself worth recording.

8.  **Verify before reporting.**

    Never report a tier complete without mechanical verification. See the
    "Verification" section below for what to check and how.

## Rules

- **Ask the user to make decisions.**

  Where a finding has two defensible resolutions, put it to the user, with a
  recommendation. Record the user's decision and its rationale in `TODO.md`, so
  the reasoning survives.

  Where the resolution is obvious, just go ahead and apply it. The user will
  review your changes from the Git working tree.

- **Keep scope to a single target technical standard.**

  Do NOT deviate to repo-wide changes without explicit user approval.

- **Preserve the user's edits.**

  The user edits files between tiers. Before editing a file you drafted
  earlier, re-read it. If the user has trimmed your prose, match their
  wording — do not restore your own.

  Do not leave `AGENTS.md` asserting what the user has cut from the standard.
  Update it to reflect the user's latest edits.

- **Follow the standards being reviewed.**

  `TODO.md` follows TS-27 (Markdown). Edits to the standard follow TS-28
  (AsciiDoc) and `docs/style-guide.md`.

## Verification

Run these after every tier. Each exists because its absence has produced a
false report.

- **Count characters, not bytes.** `awk 'length>80'` counts *bytes*. An em dash
  is three bytes in UTF-8, so every em-dash line reads two columns wider than
  it is. Use Python:

  ```python
  for i, l in enumerate(open(fn).read().split('\n'), 1):
      if len(l) > 80: print(f'{fn}:{i} ({len(l)})')
  ```

- **Check xref *uniqueness*, not existence.** An xref to a title held by two
  sections is ambiguous and resolves unpredictably. Assert exactly one match:

  ```python
  for t in re.findall(r'<<([^>,]+?)(?:,[^>]*)?>>', text):
      if len(heads.get(t, [])) != 1: print("PROBLEM:", t)
  ```

- **Resolve every link target on disk.** Both `link:` and `include::`. Before
  reporting a broken link as your own breakage, check it against a clean tree
  (`git stash`). The repository has pre-existing broken links, and
  attributing them to your change wastes the user's time.

- **Prove a reorder moved nothing.** After relocating a section, assert that
  the file's word multiset is identical before and after.

- **Bound every script.** Use `timeout 60` and prefer `while IFS= read -r` over
  `for x in $(...)`, which word-splits on spaces and silently corrupts
  multi-word values. An unbounded loop over a large tree will hang the session.

- **Check the diff size against expectation.** If a change of 152 link joins
  reports 4994 deletions, something else happened. Investigate before
  proceeding.

## Edge cases

- **Stub standards.** A standard with only a placeholder has nothing to
  review. Report this and stop.

- **`git mv` for renames.** Renaming or renumbering files MUST use `git mv` so
  history follows the file. Rename highest-numbered first to avoid collisions.
  Afterwards, rebuild the README's `include::` list and update `TODO.md`'s own
  file references.

- **Pre-existing defects in other standards.** A sweep will surface them.
  Confirm they predate your work, report them, and leave them alone unless the
  user asks. Do not silently expand scope.

- **The plan's own claims go stale.** `TODO.md` records what was true when
  written. Before acting on an item, re-verify its premise. A note saying a
  retrofit "requires renumbering identifiers" may be wrong by the time you
  reach it.

## Success criteria

- **Every finding in `TODO.md` cites a file and line**, and explains why it is a
  defect, so the user can judge it without re-deriving the analysis.

- **Findings are flat bullets** under their category heading — no
  sub-headings, tables, or per-finding subsections.

- **Tiers were worked in order**, one at a time, with the user given the
  opportunity to commit between them.

- **Every completed item is ticked and annotated** with what was done, and
  every decision records who made it and why.

- **Mechanical verification ran and is reported**, including anything that
  could not be verified and why.

- **Errors are recorded, not hidden** — wrong findings, failed fixes, and lost
  work are all written against the items they belong to.

- **Nothing was committed.**
