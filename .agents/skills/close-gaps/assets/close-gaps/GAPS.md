# TS-[N] gap analysis

Gaps found comparing TS-[N]: [Title] against the following reference
resources:

- [URL or file path]
- [URL or file path]

**Assessment.** Carried over unchanged from the analysis that wrote this
file. Where the file was converted from the legacy format, which has no
assessment paragraph, write one sentence naming the sources and the shape of
what they found, and say that the file was converted.

**Status:** [N] of [M] actionable gaps closed ([date]). [What this run
closed, in one clause.] [What remains, by heading: N missing, N partial, N
out-of-scope awaiting the user, N unresolved.] Update this line every run —
it is the first thing a resuming agent reads.

## Missing

- [x] [reference source, eg. URL#section or file:line] says [what the source
      says, from the legacy `**What the source says**` bullet]. The gap:
      [what the standard does not state, from `**Gap**`]. Coverage check:
      [where the standard currently stands, from `**Coverage check**`].
      Recommend placing at [file]:[line] or "new section".
      Cross-references: TS-[N] ([Title]).

      **Resolved.** Closed by `[NN-file].adoc`, "[Section title]" section.
      [What the section now says — the rule it states, the failure mode it
      names, the exception it carves out. Two or three clauses, enough that
      a reader who has not seen the diff knows what exists.] Cross-references
      TS-[N] ([Title]) for [the adjacent concern it hands off]. Source added
      to the page's `== References`.

- [x] [reference source] is not addressed anywhere in the standard.
      Recommend placing at [file]:[line].

      **No change needed.** The standard already covers this at
      `[NN-file].adoc:[line]`, under the heading "[Section title]", in
      wording that does not use the reference's terminology — which is why
      the analysis missed it. No content written.

- [x] [reference source] is not addressed anywhere in the standard.
      Recommend placing at [file]:[line].

      **Withdrawn.** The premise is stale. [What is actually the case now,
      and what changed since the analysis ran.] Recorded rather than
      deleted, so a later analysis does not re-find it.

- [ ] [reference source] is not addressed anywhere in the standard.
      Recommend placing at [file]:[line] or "new section".

## Partial

- [x] [reference source] covers this more thoroughly than [file]:[line] —
      specifically, [what the reference adds that the standard omits].

      **Resolved.** Closed by a new "[Subsection title]" subsection in
      `[NN-file].adoc`, extending the existing [section] rather than adding
      a section of its own. [What the subsection adds.] Source added to the
      page's `== References`.

- [ ] [reference source] covers this more thoroughly than [file]:[line] —
      specifically, [what the reference adds that the standard omits].

## Out-of-scope

- [x] [reference source] covers this, but it plausibly sits outside this
      standard's stated purpose because [reason]. Flagged for the user to
      confirm or overrule.

      **Confirmed out-of-scope** ([date]). The user confirmed the
      exclusion: [their reasoning, in their terms]. No content written.

- [ ] [reference source] covers this, but it plausibly sits outside this
      standard's stated purpose because [reason]. Flagged for the user to
      confirm or overrule. Recommendation: [confirm or overrule, and why].

## Unresolved

- [x] [reference resource] could not be retrieved when the analysis ran:
      [original error].

      **Dismissed** ([date]). Re-fetched successfully. [What the resource
      turned out to contain, and why it yields no gap — already covered,
      out of scope, or too thin to act on.]

- [ ] [reference resource] could not be retrieved when the analysis ran:
      [original error]. Re-fetch failed again on [date]: [new error]. The
      failure is persistent, not fresh.

---

## Notes on this example

This section is guidance about the template, and does not belong in a real
`GAPS.md`. Delete it, along with the rule above it, when copying.

- The four headings above — `## Missing`, `## Partial`, `## Out-of-scope`,
  `## Unresolved` — are the only ones a real file carries. The counting
  script in the root `TODO.md` keys on them, so any extra heading or
  sub-label between an item and its heading breaks the counts. All four
  appear even when empty; a heading with nothing under it carries a
  parenthetical saying so.

- Items come in two lengths, and both are correct. An item written directly
  by `gap-analysis` is short — source, what is missing, and a placement
  recommendation — because that is all its template captures. An item
  **converted from the legacy format** is longer, as the first one above is,
  because the legacy file recorded `**What the source says**`, `**Gap**`,
  and `**Coverage check**` separately and the conversion is required to be
  lossless. Do not pad a short item to match the long form, and do not
  compress a converted one to match the short form.

- The three closure forms — `**Resolved.**`, `**No change needed.**`, and
  `**Withdrawn.**` — all keep the item's original text above them, untouched.
  The note is an indented paragraph inside the same bullet, at the same
  six-space continuation indent as the item's own wrapped lines.

- `Cross-references:` as the last sentence of an item is where the legacy
  format's `**Cross-references**` field lands on conversion. It is kept
  per-item, not hoisted into the header, because its only value is telling a
  later agent that this specific gap may belong to another standard.

- An item closed by content written in a _different_ standard is ticked here
  with a note naming that standard's file, exactly as
  `src/modules/ROOT/partials/005/GAPS.md` does for the six gaps TS-6 closed.
  That only happens after the user has agreed to the split.
