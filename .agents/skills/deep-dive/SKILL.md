---
name: deep-dive
description: >-
  Review one technical standard in this repository in depth, record every
  finding in a tiered remediation plan, then work that plan tier by tier. Use
  when the user says "deep dive TS-<N>", "review TS-<N> thoroughly", "what's
  next on the plan?", or asks to continue an existing review. Do not use it for
  a quick proofread of a single file.
compatibility: requires Read, Write, Edit, Glob, Grep, Bash (git, python3)
license: CC0-1.0
---

# Deep dive

Review a single technical standard in depth, collect every finding into a
`TODO.md` beside it, and then — once the user has seen the plan and asked for
it — work that plan one tier at a time. The review and the remediation are
separate: the plan has standalone value, so do not start fixing until asked.

## Parameters

Determine the following information from the surrounding context and
environment, if possible. If you're uncertain about the required parameters,
prompt the user for clarification.

- **The target standard — REQUIRED.** One technical standard, identified as
  `TS-<N>`. Its number zero-padded to three digits identifies its files, so
  TS-1 is the page `src/modules/ROOT/pages/001-<slug>.adoc` plus everything
  under `src/modules/ROOT/partials/001/`. If the user does not name one, and
  the context or the working directory already establishes a standard, treat
  that as the target.

- **The tier to work — OPTIONAL.** Which tier of an existing plan to
  remediate. Absent an instruction to remediate, produce the plan and stop.
  Absent a named tier, take the lowest-numbered tier that is still open.

## Success criteria

- `src/modules/ROOT/partials/<NNN>/TODO.md` MUST exist, MUST name the
  yardsticks the standard was measured against, and MUST record every finding
  as a flat checklist bullet under its category heading — no sub-headings,
  tables, or per-finding subsections.

- Every finding MUST cite a `<file>:<line>` location and MUST say why the
  thing it cites is a defect, so the user can judge it without re-deriving the
  analysis.

- Every finding MUST be assigned to one of the four tiers, and any tier that
  was worked MUST have been worked whole, in tier order, with the user given
  the chance to commit before the next one starts.

- Every worked item MUST be ticked and annotated with what was actually done,
  including items that turned out to need no change, items resolved
  differently from how they were written, and fixes that failed. A finding
  that was wrong is itself worth recording.

- The mechanical verification in step 8 MUST have run over every tier worked,
  and its results — including anything that could not be verified, and why —
  MUST be in the report back to the user.

- Nothing MUST be staged or committed, and no file outside the standard's page
  and its `src/modules/ROOT/partials/<NNN>/` directory MUST have been
  modified. The user commits, and the user approves any wider sweep.

## Instructions

1.  Resolve the target from the standards index at
    `src/modules/ROOT/pages/index.adoc`, then check for
    `src/modules/ROOT/partials/<NNN>/TODO.md`. If it exists, this is a
    resumption: read it, find the first unchecked item, and report the
    remaining scope to the user before doing any work.

2.  Read everything, in full, before reviewing anything.

    Read the standard's page (`src/modules/ROOT/pages/<NNN>-<slug>.adoc`),
    every file it pulls in via `include::`, any subdirectory under
    `partials/<NNN>/` carrying its own `README.adoc`, and the standard's
    `AGENTS.md` if it has one.

    Then read the yardsticks you will measure against:

    - `docs/style-guide.md` — normative for everything under `src/`.
    - `src/modules/ROOT/partials/026/` (TS-26: Technical Writing Style Guide)
      — prose conventions.
    - `src/modules/ROOT/partials/027/` (TS-27: Markdown) — applies to
      `TODO.md` and `AGENTS.md`.
    - `src/modules/ROOT/partials/028/` (TS-28: AsciiDoc) — syntax, links,
      line length.
    - `template/` — the reference structure for a standard.

    Name these in the `TODO.md` header, so a reader knows what the findings
    were measured against.

3.  Where the style guide is silent on a question of style, sample the sibling
    standards for the de-facto convention rather than inventing one.

    ```sh
    grep -lE '^== References$' src/modules/ROOT/pages/*.adoc | wc -l
    find src/modules/ROOT/partials -name '[0-9][0-9][a-z]-*.adoc'
    ```

4.  Collect findings into the seven categories below. Take one category at a
    time and read the whole standard for it. Do not stop at the first defect
    in a file.

    1.  Contradictions. The same rule stated two ways. These are the most
        damaging defects, because a reader cannot comply with both. Look
        especially for a rule restated in a second location that has since
        drifted.

    2.  Factual errors. Claims about a language, protocol, or standard that
        are wrong. Verify anything checkable against primary sources, not
        against your own recollection.

    3.  Structural problems. Content in the wrong section; a section that has
        become a catch-all; the same material at length in two places; an
        ordering that contradicts the prose describing it.

    4.  Coverage gaps. A rule the standard implies but never states, or a case
        it does not handle. Find these by asking what a reader would need that
        the standard does not give them.

    5.  Convention conformance. Divergences from the yardsticks read in step
        2 — file naming, references, quotes, dashes, bold lead-ins, line
        length, link syntax.

    6.  `AGENTS.md` drift. Compare it against the source rule by rule: rules
        it invents, rules it omits, rules whose strength it has changed. This
        file is acted on by agents, so its defects propagate.

    7.  Prose defects. Typos, hedging, filler, unfalsifiable normative
        statements ("as early as possible"), first-person "we", and examples
        that do not demonstrate the rule they illustrate.

5.  Write `TODO.md`, following the bundled template. Assign every finding to a
    tier, and keep the tiers in this dependency order:

    | Tier | Category | Rationale |
    | --- | --- | --- |
    | 1 | Correctness | A contradiction makes the standard unusable. |
    | 2 | Coherence | Structure must settle before content is added. |
    | 3 | Completeness | Gaps are filled into a settled structure. |
    | 4 | Conventions | Cosmetic; do last, when content has stopped moving. |

    The order is not arbitrary. Fixing conventions first means re-fixing them
    after the content moves.

6.  Report the tier counts and the items needing a user decision, then stop.
    Do NOT begin remediation until the user asks for it.

7.  When the user asks you to proceed, take exactly one tier. Within it: apply
    the fixes, tick each checkbox and append what was done in the same bullet,
    update the `**Status:**` line, verify (step 8), report, and stop.

8.  Verify mechanically before reporting a tier complete. Each check below
    exists because its absence has produced a false report.

    - Count characters, not bytes. `awk 'length>80'` counts bytes, and an em
      dash is three bytes in UTF-8, so every em-dash line reads two columns
      wider than it is. Use Python:

      ```python
      for i, l in enumerate(open(fn).read().split('\n'), 1):
          if len(l) > 80: print(f'{fn}:{i} ({len(l)})')
      ```

    - Check xref uniqueness, not existence. An xref to a title held by two
      sections is ambiguous and resolves unpredictably. Assert exactly one
      match:

      ```python
      for t in re.findall(r'<<([^>,]+?)(?:,[^>]*)?>>', text):
          if len(heads.get(t, [])) != 1: print("PROBLEM:", t)
      ```

    - Resolve every `xref:`, `include::`, and `link:` target. An `xref:` to
      another standard's page is `NNN-<slug>.adoc` — confirm that file exists
      under `pages/`. An `include::` from a page targets `partial$NNN/<file>`
      — confirm that file exists under `partials/NNN/`; a bare relative
      `include::` inside a partial targets a sibling in the same
      subdirectory. A `link:` should only remain for genuinely external URLs
      — anything pointing at another standard is a style-guide violation, not
      a broken link, and belongs in the Conventions tier. Before reporting a
      broken reference as your own breakage, check it against a clean tree
      (`git stash`). The repository has pre-existing broken references, and
      attributing them to your change wastes the user's time.

    - Prove a reorder moved nothing: after relocating a section, assert the
      file's word multiset is identical before and after.

    - Bound every script with `timeout 60`, and prefer `while IFS= read -r`
      over `for x in $(...)`, which word-splits on spaces and silently
      corrupts multi-word values. An unbounded loop over a large tree will
      hang the session.

    - Check the diff size against expectation. If a change of 152 link joins
      reports 4994 deletions, something else happened. Investigate before
      proceeding.

## Rules

- Where a finding has two defensible resolutions, you MUST put it to the user
  with a recommendation, and MUST record their decision and its rationale in
  `TODO.md` so the reasoning survives. Where the resolution is obvious, just
  apply it — the user reviews your changes from the Git working tree.

- You MUST keep scope to the one target standard. A sweep will surface defects
  elsewhere; confirm they predate your work, report them, and leave them alone
  unless the user asks otherwise.

- You MUST re-read a file you drafted earlier before editing it again. The
  user edits between tiers, and if they have trimmed your prose you MUST match
  their wording rather than restoring your own.

- You MUST NOT leave `AGENTS.md` asserting what the user has cut from the
  standard. Update it to match their latest edits.

- Edits to the standard MUST follow TS-28 and `docs/style-guide.md`, and
  `TODO.md` MUST follow TS-27. A review that breaks the conventions it is
  enforcing is self-defeating.

- Renaming or renumbering a file MUST use `git mv`, so history follows the
  file. Rename highest-numbered first, to avoid collisions. Afterwards, you
  MUST rebuild the page's `include::` list and update `TODO.md`'s own file
  references.

## Edge cases

- The standard is a stub, holding only a heading and a placeholder.

  There is nothing to review. Report this and stop.

- The plan's own claims have gone stale.

  `TODO.md` records what was true when it was written. Re-verify an item's
  premise before acting on it. A note saying a retrofit "requires renumbering
  identifiers" may be wrong by the time you reach it.

## Assets

- [TODO.md template](./assets/deep-dive/TODO.md) \
  The structure to follow when writing or updating the plan in step 5.
