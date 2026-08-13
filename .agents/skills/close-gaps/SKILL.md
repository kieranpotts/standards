---
name: close-gaps
description: >-
  Close the open coverage gaps recorded in one technical standard's GAPS.md in
  this repository, by writing the missing content into that standard and
  recording each closure against its gap. Use when the user says "close the
  gaps in TS-<N>", "work TS-<N>'s GAPS.md", "close the next batch of gaps in
  TS-<N>", or asks to continue closing gaps. Do not use it to find gaps — that
  is the gap-analysis skill.
compatibility: >-
  requires Read, Write, Edit, Glob, Grep, WebFetch, Bash (git, python3)
license: CC0-1.0
---

# Close gaps

Take the gaps already recorded in one standard's `GAPS.md`, write the content
that closes a bounded batch of them, and record in that same file exactly what
was written and where. Finding gaps is the `gap-analysis` skill's job. This
skill only closes what an analysis has already recorded, and it works one
standard, in batches, until the file is exhausted.

## Parameters

Determine the following information from the surrounding context and
environment, if possible. If you're uncertain about the required parameters,
prompt the user for clarification.

- **The target standard — REQUIRED.** One technical standard, identified as
  `TS-<N>`. Its number zero-padded to three digits identifies its files, so
  TS-1 is the page `src/modules/ROOT/pages/001.adoc` plus everything under
  `src/modules/ROOT/partials/001/`. If the user does not name one, and the
  context or the working directory already establishes a standard, treat that
  as the target.

- **The batch — OPTIONAL.** Which gaps to take in this run, either named
  individually or given as a count. If the user does not say, take at most
  eight actionable items — `## Missing` plus `## Partial` — and stop. Take
  fewer where the batch would run past roughly 300 lines of new prose, and
  never take the whole file just because it is short enough to fit in
  context. The largest file, TS-39, holds 136 actionable items; a run that
  tries to close them all will produce shallow content and an unreviewable
  diff.

## Success criteria

- Every item in the batch MUST be ticked and annotated in `GAPS.md` with what
  was written and where — the destination file, the section title, and what
  the section actually says. The `**RESOLVED**` notes in
  `src/modules/ROOT/partials/006/GAPS.md` and
  `src/modules/ROOT/partials/002/GAPS.md` set the bar: a reader who has not
  seen the diff can tell from the note alone what now exists.

- Every item worked MUST be recorded, including items that turned out to need
  no change and items whose premise was wrong. No item MUST be deleted, and no
  item's original text MUST be rewritten.

- The `**Status:**` line MUST be updated, every run. It is the first thing a
  resuming agent reads.

- A `GAPS.md` in the legacy format MUST have been converted to the template
  format in the same run that works it, losing nothing — including the
  resolution notes of gaps closed before the conversion.

- Only `## Missing` and `## Partial` items MUST count as the batch's work.
  Ticking an `## Out-of-scope` or `## Unresolved` item MUST NOT be reported as
  closing a gap.

- New content MUST live under `src/modules/ROOT/partials/<NNN>/`, MUST be
  included from `src/modules/ROOT/pages/<NNN>.adoc`, and MUST conform to
  `docs/style-guide.md`, TS-26, and TS-28. `GAPS.md` MUST conform to TS-27.

- The mechanical verification in step 10 MUST have run, and its results —
  including anything that could not be verified, and why — MUST be in the
  report back to the user.

- Nothing MUST be staged or committed, and no file outside the target
  standard's page and its `src/modules/ROOT/partials/<NNN>/` directory MUST
  have been modified. The root `TODO.md` is outside that scope: the run
  MUST report its corrected row rather than editing it.

## Instructions

1.  Resolve the target from the standards index at
    `src/modules/ROOT/pages/index.adoc`, then read
    `src/modules/ROOT/partials/<NNN>/GAPS.md` in full. If there is no
    `GAPS.md`, there is nothing to close: say so, and offer `gap-analysis`
    instead. Read the root `TODO.md` for the recorded item counts, but trust
    the file over the index.

2.  Identify which of the two formats the file is in. Use
    `grep -q '^## Missing$'` — anchored at both ends, so that a legacy file
    with a gap titled, say, "Missing retry guidance" is not misread as
    template format.

    - **Template format.** Flat `- [ ]` checklists under `## Missing`,
      `## Partial`, `## Out-of-scope`, and `## Unresolved`.

    - **Legacy format.** One `## <gap title>` subsection per gap, each with
      `**Source**`, `**What the source says**`, `**Coverage check**`, and
      `**Gap**` bullets, sometimes `**Cross-references**`, and closed by
      appending a `**RESOLVED**` bullet.

3.  Read the standard in full before writing anything: its page
    (`src/modules/ROOT/pages/<NNN>.adoc`), every file it pulls in via
    `include::`, and any subdirectory under `partials/<NNN>/` carrying its own
    `README.adoc`. Then read the yardsticks — `docs/style-guide.md`,
    `src/modules/ROOT/partials/026/` (prose), `027/` (Markdown, for `GAPS.md`
    itself), `028/` (AsciiDoc), and `template/`.

4.  Convert a legacy-format file to the template format now, as the first edit
    of the run. Do not defer it to a later sweep, and do not work a legacy
    file in place. The conversion is lossless:

    - **The header.** The document title becomes `# TS-<N> gap analysis`,
      followed by the "Gaps found comparing TS-<N>: <Title> against the
      following reference resources:" preamble and a bulleted list of the
      distinct `**Source**` values found across the file.

      The template header carries two more parts that a legacy file usually
      lacks, and both MUST be written rather than skipped:

      - `**Assessment.**` One or two sentences naming the sources and the
        shape of what they found — mostly missing coverage, mostly partial
        treatment, or mostly already covered — and saying that the file was
        converted from the legacy format and on what date. Where the legacy
        file has no assessment, derive it from the converted items.

      - `**Status:**` Which gaps remain open, which have been closed, and the
        date. Where the legacy file already carries a status line, it will be
        in the older `**Status: 1 of 5 gaps resolved (2026-08-06).**` syntax,
        with the bold wrapping the whole sentence. Rewrite it into the
        template's `**Status:** …` form, where the bold covers only the label.
        Preserve what it says; change only the syntax and any count the run
        has moved.

      A legacy preamble sentence such as "Coverage gaps identified by
      comparing external sources against this standard." is boilerplate that
      the new preamble subsumes, and MAY be dropped. Nothing else may be.

    - **The items.** Each `## <gap title>` subsection becomes one checklist
      bullet, written in this order, which the bundled asset demonstrates:

      1.  The source citation — a URL with a section anchor where possible,
          or `<file>:<line>`, carried across verbatim.
      2.  What that source says, from `**What the source says**`.
      3.  The gap it leaves, from `**Gap**`.
      4.  Where the standard currently stands, from `**Coverage check**`.
      5.  A placement recommendation — `Recommend placing at <file>:<line>`,
          or "new section". Legacy items rarely name one; derive it from the
          coverage check, since an item that cannot be tied to a destination
          is not actionable.

      Condense, but do not summarize away. The `## <gap title>` heading text
      itself is not preserved — the item's own prose replaces it.

    - **The headings.** Classify each converted item as Missing or Partial
      from its `**Coverage check**`: "the standard says nothing about X" is
      Missing; "the standard covers X but not Y" is Partial. All four
      headings MUST be present even when empty, and any heading the legacy
      analysis recorded nothing under gets a parenthetical note saying the
      file was converted from the legacy format and that the original
      analysis recorded no such items. This routinely applies to
      `## Out-of-scope` and `## Unresolved`, which the legacy format has no
      concept of, and applies equally to `## Partial` when every converted
      item is Missing — as it is in any single-gap file.

    - A subsection carrying a `**RESOLVED**` bullet becomes a `- [x]` item
      whose resolution note is carried over word for word, in the step 7 form.
      Do not re-derive, shorten, or re-word an existing resolution note.

    - `**Cross-references**` has no slot in the template format. Preserve it
      as the final sentence of the converted bullet, in the form
      `Cross-references: TS-6 (Distributed system design), TS-49 (Cloud
      platform engineering).` Keeping it per-item rather than in the header
      is deliberate: the field's only value is its association with one
      specific gap, and that association is what tells a later agent the gap
      may belong to another standard.

    Finish the conversion completely before writing any content. Not for the
    user's benefit — the run ends as one dirty tree and `git diff` will show
    the conversion and the content work together regardless — but for yours:
    the classification, the item order, and the placement recommendations all
    have to be settled before you start ticking items against them, and a run
    that interleaves the two risks leaving the file half-converted if it stops
    early. A legacy file with no open gaps left is not converted at all —
    there is nothing to work, so churning it gains nothing.

5.  Select the batch. Count only `## Missing` and `## Partial` items. Prefer
    items that share a destination, so a section gets written once and whole,
    rather than accreting in three passes. Name the selected items to the
    user, then proceed — do not wait for approval on the batch itself. Stop
    and ask only where a decision is genuinely the user's: an item whose
    content belongs in another standard (see the rules below), or an
    out-of-scope item needing a scope call (step 8).

6.  Re-verify each item's premise before acting on it. `GAPS.md` records what
    was true when the analysis ran, and the standard has moved since. Confirm
    the cited `<file>:<line>` still exists and still says what the item claims,
    and grep the standard for the gap's subject in case the content has since
    been written under a different name. Where the item's summary of its
    source is too thin to write from, re-fetch the source. If the source
    cannot be fetched, leave the item open and record why; do not write the
    content from memory.

7.  Write the content, then record the closure against the item.

    Where the content goes is the highest-leverage decision in the run, and
    the two answers produce very different diffs for the same prose. Default
    to **extending an existing partial** — adding a new `== ` section inside
    it, or a paragraph within a section it already has — and reach for a new
    numbered partial only when the gap introduces a topic that no existing
    partial is about. Ask which partial a reader would expect to find the
    material in; if that question has an answer, that partial is the
    destination.

    The default is not neutral. Extending is a pure addition to one file.
    Inserting a new partial anywhere but the end renumbers every file after
    it, and a 67-line section can turn into a diff touching five files for
    no gain in the published page, which reads identically either way.

    A new partial goes into `src/modules/ROOT/partials/<NNN>/` numbered for
    its position, wired into the page with
    `include::partial$<NNN>/<file>.adoc[leveloffset=+1]`.

    - The page's include list is the section order. Appending a new partial is
      the cheap case. Inserting one in the middle means renumbering every file
      after it with `git mv`, highest-numbered first, then rebuilding the
      include list. Where the standard keeps its references in a trailing
      partial (`NN-references.adoc` — eight standards do), new sections go
      before it, so it is renumbered too.

    - Prose follows `docs/style-guide.md`, TS-26, and TS-28: American English,
      RFC 2119 keywords for normative statements, bold lead-ins terminated
      with a period, explicit Arabic numbering, 80-character lines, language
      on every code block, long-form admonition blocks, plain double quotes.

    - A cross-reference to another standard is
      `xref:NNN.adoc[*TS-N: Title*]`, with the bold tight around the link
      text inside the macro's brackets — never wrapped around the whole
      macro, never a relative path, never a section fragment. The whole macro
      MUST sit on one source line, even where that puts the line over 80
      characters.

    - A cross-reference to another section of the *same* standard is
      `<<Section title>>`, never an `xref:` to the standard's own page. Each
      standard is one merged page, so an `xref:` to its own page links the
      reader to the page they are already reading.

    - Where the gap cites a source, add that source to the standard's
      reference list. This is what TS-6 and TS-2 did for every source that fed
      new content, and it is why their reference lists read as a provenance
      trail. The entry follows the author-date form in the style guide, and
      its trailing annotation names the section the source fed, by
      `<<Section title>>` xref:

      ```asciidoc
      * Allegro Tech (2024).
        https://blog.allegro.tech/2024/04/ten-years-microservices.html[_Ten Years of Microservices at Allegro_].
        — The source for the service-sizing guidance in
        <<Microservices at scale>>.
      ```

      The list lives in a `== References` section on the page, after a `''''`
      rule, per the style guide. Create it there if the standard has none —
      most standards do not. Where the standard already keeps its references
      in a trailing partial, add the entry to that list where it is; relocating
      it is a style-guide divergence for `deep-dive`'s conventions tier to
      settle, not a side effect of closing a gap. Report it.

    Then tick the item and append the resolution note as an indented paragraph
    inside the same bullet, leaving the original text untouched:

    ```markdown
    - [x] `__TODO__/031/shell/unix/input.md:39-43` — hidden/silent input for
          passwords is not addressed. [...]

          **Resolved.** Closed by `13-read.adoc`, "Reading a password"
          section. Documents the POSIX-compliant `stty -echo` / `read` /
          `stty echo` sequence, requires the terminal state be restored from
          an `EXIT` trap so an interrupted script does not leave echo off,
          and notes that the reference's `read -s` is a Bashism excluded by
          this standard's POSIX scope. Source added to the page's
          `== References`.
    ```

    Two variants, for items that produced no content:

    - `**No change needed.**` — the standard already covers this, at
      `<file>:<line>`, in wording the item's author missed. Say where.

    - `**Withdrawn.**` — the item's premise is wrong or has gone stale. State
      what is actually the case. A finding that was wrong is worth recording;
      deleting it invites the next analysis to find it again.

8.  `## Out-of-scope` items are decisions, not work. Each one is the analysing
    agent's scope call, recorded for a human to confirm or overrule. Never
    action one silently, and never count one toward the batch. At the end of
    the run, list any that are still open with a recommendation for each, and
    let the user decide. When the user confirms an exclusion, tick the item
    and append `**Confirmed out-of-scope.**` with the date and the reasoning.
    When the user overrules it, move the item under `## Missing` or
    `## Partial` and work it like any other actionable item.

9.  `## Unresolved` items are reference resources that failed to fetch when
    the analysis ran. Re-fetch each one in the batch's run. If it now
    retrieves, compare it against the standard as `gap-analysis` would, and
    either add the resulting items under `## Missing` / `## Partial` — where
    they join the backlog rather than this batch — or tick it with
    `**Dismissed.**` and say what the resource turned out to contain. If it
    fails again, leave it unchecked and record the new error and the date, so
    the next agent can see the failure is persistent rather than fresh.

10. Update the `**Status:**` line, then verify mechanically before reporting.
    Each check below exists because its absence has produced a false report.

    - Count characters, not bytes. `awk 'length>80'` counts bytes, and an em
      dash is three bytes in UTF-8, so every em-dash line reads two columns
      wider than it is. Use Python:

      ```python
      for i, l in enumerate(open(fn).read().split('\n'), 1):
          if len(l) > 80: print(f'{fn}:{i} ({len(l)})')
      ```

      A line over 80 characters is only acceptable where a link macro or a
      table row cannot be broken.

    - Resolve every `xref:`, `include::`, and `link:` target you introduced.
      An `xref:` to another standard's page is `NNN.adoc` — confirm that file
      exists under `pages/`. An `include::` from a page targets
      `partial$NNN/<file>` — confirm that file exists under `partials/NNN/`.
      A bare relative `include::` inside a partial targets a sibling in the
      same subdirectory. A `link:` to another standard is a style-guide
      violation, not a broken link.

      Editing a page fires one IDE diagnostic per include, of the form
      `include file not found: .../pages/partial$NNN/01-….adoc`. Ignore
      them. They are a plain-Asciidoctor resolver failing on Antora's
      `partial$` resource ID, they appear for every page in the repository,
      and no run has ever caused one.

    - Check `<<Section title>>` xrefs resolve to exactly one heading. A new
      section can collide with an existing title, and an ambiguous xref
      resolves unpredictably:

      ```python
      for t in re.findall(r'<<([^>,]+?)(?:,[^>]*)?>>', text):
          if len(heads.get(t, [])) != 1: print("PROBLEM:", t)
      ```

    - **Only if the previous two checks found a broken reference**, confirm
      whether it predates the run before reporting it as your own breakage.
      Prefer reading the committed version — `git show HEAD:<path>` — over
      `git stash`. The run's entire product is an uncommitted working tree,
      and stashing it to satisfy a check is a risk taken for nothing. Where
      every reference resolved, skip this check; there is nothing to
      attribute.

    - Assert every partial under `partials/<NNN>/` is included exactly once by
      the page, that the include order matches the files' numeric order, and
      that no `.adoc` file is orphaned. The style guide forbids an included
      file that is not on the page, and a page entry with no file.

    - **Only if you renumbered a file**, check the diff size against
      expectation. Three new sections that report 2,000 changed lines mean a
      renumbering rewrote more than intended. Investigate before proceeding.
      A run that only extended existing partials cannot hit this, and its
      diff needs no such scrutiny.

    - Bound every script with `timeout 60`, and prefer `while IFS= read -r`
      over `for x in $(...)`, which word-splits on spaces and silently
      corrupts multi-word values.

11. Report: which items were closed and what was written for each, which were
    withdrawn or needed no change, what remains open in the file, the
    out-of-scope items awaiting the user's decision, and any unresolved
    resource that failed to fetch again.

    Every run also invalidates the target's row in the root `TODO.md`, which
    is outside the scope you may edit. Close the report with the corrected
    row — the new actionable, scope, and unresolved counts, and `Template`
    where the run converted the format — so the user can apply it, or
    regenerate the index with the script `TODO.md` carries for the purpose.
    A standard whose file is now fully worked leaves the table entirely and
    joins the fully-resolved list above it. Say so where it applies.

    Then stop. The user reviews the working tree and commits.

## Rules

- You MUST NOT stage or commit anything. The end state of a run is a dirty
  working tree for the user to review.

- You MUST keep scope to the one target standard: its page and its
  `src/modules/ROOT/partials/<NNN>/` directory. Defects you notice elsewhere
  are reported, not fixed.

- Where a gap's content plainly belongs in a different standard, you MUST put
  that to the user with a recommendation, and MUST NOT write into the other
  standard's directory on your own initiative. Six of TS-5's thirteen gaps
  were closed by content written in TS-6, which was the right call — but it
  was the user's call to make, because a unit of work stays within one
  standard. Record the decision, and the reasoning, in `GAPS.md`. Where the
  user agrees, closing those gaps becomes a separate run against the other
  standard, and this file's items are ticked with a note naming the file that
  closed them, exactly as TS-5's are.

- You MUST NOT report a batch complete on the strength of `## Out-of-scope` or
  `## Unresolved` items. Neither is content work, and a run that ticks only
  those has closed no gaps.

- You MUST NOT delete an item, rewrite its original text, or drop a prior
  resolution note. `GAPS.md` is an append-only record of what was found and
  what was done about it.

- You MUST NOT fabricate source content. Where the item's summary is too thin
  to write from and the source cannot be re-fetched, leave the item open and
  say so. Do not recall the source from memory.

- You MUST re-read a file you drafted in an earlier batch before editing it
  again. The user may have edited it between runs, and if they have trimmed
  your prose you MUST match their wording rather than restoring your own.

- New content MUST be written to the standard's own depth and register. A gap
  is closed by a section that a reader of that standard would expect to find
  there — not by a paraphrase of the reference source, and not by a stub that
  merely names the topic.

- Renaming or renumbering a file MUST use `git mv`, highest-numbered first, so
  Git history follows the file. Afterwards you MUST rebuild the page's
  `include::` list and update any `<file>` reference in `GAPS.md` that the
  renumbering invalidated.

## Edge cases

- The standard is a stub — a page with a `// TODO` placeholder and no
  `include::partial$` directives. There is no structure to extend, and writing
  a standard from scratch is a different job with different inputs. Report
  this and stop. Seven standards are in this state, four of them carrying a
  `GAPS.md`; TS-37's holds eighteen actionable items and TS-38's says outright
  that everything is a gap because nothing is written.

- The `GAPS.md` is already fully resolved. Report that and stop. Do not
  re-open closed items to re-verify them — that is a `gap-analysis` re-run.

- A gap's premise has gone stale. The standard has been edited since the
  analysis ran, so a cited line number may have moved, or the content may
  already exist. Re-verify before acting, and record the outcome as
  `**No change needed.**` or `**Withdrawn.**` rather than writing content that
  duplicates what is already there.

- A `TODO.md` from an in-progress `deep-dive` sits alongside the `GAPS.md`
  with tier 1 or tier 2 open. Structure has to settle before content is added
  to it, or the new content is written into a shape that is about to move.
  Report this and ask whether to proceed or to finish those tiers first.

- The batch's items all target one section that does not exist yet. Write the
  section once, coherently, and tick every item against it. Do not write one
  subsection per gap: `GAPS.md` items are units of analysis, not units of
  prose.

## Assets

- [GAPS.md worked example](./assets/close-gaps/GAPS.md) \
  A file that has been converted from the legacy format and had one batch
  worked. The reference for the conversion in step 4 and the resolution notes
  in step 7.
