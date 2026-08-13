# GAPS — TS-8 Issue tracking

Gaps found comparing TS-8: Issue tracking against the following reference
resources:

- https://blog.pragmaticengineer.com/pragmatic-engineer-test/
- https://zarar.dev/good-software-development-habits/

**Assessment.** Both sources found narrow, specific gaps rather than broad
missing coverage: one item questions whether engineer participation in
roadmap/backlog planning sits within the standard's stated scope, and two
items concern refactoring-ticket discipline that the standard's refactoring
section already partially addresses. Converted from the legacy format on
2026-08-13.

**Status:** 2 of 2 actionable gaps closed (2026-08-13). Closed the
technical-debt classification and prioritization gap with a new
"Classifying technical debt" section; the "make the change easy" gap was
closed in TS-7 (Code design) in a follow-up run and is recorded here as
resolved-by-TS-7. The out-of-scope item was confirmed excluded. 0
unresolved.

## Missing

(None — the original legacy analysis recorded no gaps as unconditionally
missing; the two actionable items were both partial-coverage gaps against
TS-8's existing refactoring content.)

## Partial

- [x] https://zarar.dev/good-software-development-habits/ says technical
      debt falls into three types: (1) things preventing you from doing
      work now, (2) things that will prevent you later, (3) things that
      might prevent you later. Minimize #1, focus on #2, and ignore #3. The
      gap: no classification of technical debt into types
      (blocking-now / will-block-later / might-block-later) and no
      prioritization guidance for triaging debt items. Coverage check:
      TS-8's refactoring issue type introduces the technical-debt metaphor
      and asks authors to weigh short-term cost vs. long-term benefit, but
      does not categorize debt into types or give a prioritization rule.
      Recommend a new subsection in `03-issue-types/09-refactoring.adoc`.
      Cross-references: TS-12 (Quality assurance).

      **Resolved.** Closed by `03-issue-types/09-refactoring.adoc`,
      "Classifying technical debt" section. Defines the three debt types
      (blocking now, will block later, might block later), states which to
      prioritize (minimize the first, focus on the second, generally leave
      the third alone), and gives the resulting priority order for
      competing refactoring tickets. Source added to the page's
      `== References`. This exact gap is also recorded, independently, in
      TS-12's GAPS.md ("Technical debt classification and prioritization"),
      cross-referencing TS-8 — that item remains open there and should be
      ticked as closed-by-TS-8 in a follow-up run against TS-12.

- [x] https://zarar.dev/good-software-development-habits/ says Kent Beck's
      maxim — first make the change easy, then make the easy change — and
      that a high proportion of commits (the author targets roughly half)
      should be refactoring commits. The gap: the "make the change easy,
      then make the easy change" discipline is not captured as a
      refactoring technique. Coverage check: TS-8's refactoring issue type
      covers refactoring as scoped in-flight work plus standalone
      refactoring tickets, but does not state the two-step sequencing or
      the commit-ratio heuristic. Recommend a new subsection in
      `03-issue-types/09-refactoring.adoc`. Cross-references: TS-7 (Code
      design), TS-9 (Version control).

      **Resolved.** Closed by `src/modules/ROOT/partials/007/01-bike-shedding.adoc`
      ("Make the change easy, then make the easy change" section), written
      as part of a TS-7 close-gaps run on 2026-08-13. That section states
      Kent Beck's two-step discipline as the code-design technique — a
      closer fit than TS-8's issue-tracking scope — and cross-references
      TS-9's own "Refactor commit discipline" subsection for the
      commit-level mechanics.

## Out-of-scope

- [x] https://blog.pragmaticengineer.com/pragmatic-engineer-test/ says teams
      should have a roadmap/backlog, and engineers should regularly
      contribute to the one for their team — i.e. engineers shape planned
      work, not just receive it. Coverage check: TS-8 explicitly excludes
      roadmap/long-term-backlog management from the issue tracker's scope,
      deferring it to "separate project-management tools" (see "Keeping the
      issue tracker focused"). It covers issue lifecycle, ownership, and
      assignment, but says nothing about whether/how engineers contribute to
      planning the backlog. Flagged for the user to confirm or overrule.
      Recommendation: confirm as out-of-scope. TS-8 is deliberately scoped to
      the issue tracker as a tool for ephemeral, short-lived work, and
      explicitly hands roadmap/backlog concerns to "purpose-built tools" and
      product-management processes outside this standard. Engineer
      participation in roadmap planning is a team-process and product-
      management concern, not an issue-tracking-system concern, so it likely
      belongs in a different standard (if any) rather than being folded into
      TS-8's deliberately narrow scope.

      **Confirmed out-of-scope (2026-08-13).** Roadmap/backlog participation
      is a team-process and product-management concern; TS-8 deliberately
      hands that off to purpose-built tools outside the issue tracker.

## Unresolved

(None — the file was converted from the legacy format, which recorded no
unresolved/unfetchable resources.)
