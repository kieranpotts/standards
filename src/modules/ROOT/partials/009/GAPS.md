# GAPS — TS-9 Version control

Gaps found comparing TS-9: Version control against the following reference
resources:

- https://blog.pragmaticengineer.com/pragmatic-engineer-test/
- https://zarar.dev/good-software-development-habits/

**Assessment.** Both sources are practice-level checklists rather than deep
references, and each yielded a single gap against TS-9: an organizational
collaboration pattern (internal open source) that the standard's existing
repository-ownership and fork-and-pull material did not name or recommend,
and a refactoring discipline (Kent Beck's "make the change easy, then make
the easy change") that the standard's commit-type taxonomy did not capture.
This file was converted from the legacy format on 2026-08-13.

**Status:** 2 of 2 actionable gaps closed (2026-08-13). Converted from the
legacy format in the same run. The internal-open-source model was closed by
a new "Internal open source" section in `03-repositories.adoc`; the refactor
discipline was closed by a new "Refactor commit discipline" subsection in
`04-commits.adoc`. 0 missing, 0 partial, 0 out-of-scope, 0 unresolved. The
file is fully worked.

## Missing

- [x] https://blog.pragmaticengineer.com/pragmatic-engineer-test/ says any
      engineer can access and contribute to most other codebases, with
      appropriate code ownership in place — an "internal open source"
      collaboration model across an organization's repositories. The gap:
      TS-9 does not frame or recommend an internal-open-source collaboration
      model. The organizational access/contribution pattern and its
      governance implications are unaddressed. Coverage check: TS-9 has the
      building blocks (repository boundaries, CODEOWNERS, PR-based review,
      fork-and-pull workflows) but frames them around repository ownership
      and branch mechanics, not as an organization-wide access-and-
      contribution model. It does not discuss cross-repository contribution
      rights or the tradeoffs of an internal-open-source topology. Recommend
      a new section in `03-repositories.adoc`.

      **Resolved.** Closed by a new "Internal open source" section in
      `03-repositories.adoc`, placed directly after "Repository scope" and
      before "Self-contained repositories". Recommends the internal-open-
      source model as the RECOMMENDED default, describes it as the same
      fork-and-pull mechanics used for external contributors applied within
      the organization, states the benefit/cost tradeoff (unblocked
      contribution and shared codebase knowledge versus review load on the
      owning team and wider credential/secrets exposure), and makes code
      ownership (cross-referencing "Code owners" in `13-pr-config.adoc`) the
      control that makes the tradeoff favorable — with a fallback to the
      narrower team-scoped model for organizations not yet ready to
      configure code ownership everywhere. Source added to the page's
      `== References`.

- [x] https://zarar.dev/good-software-development-habits/ says Kent Beck's
      maxim — first make the change easy (which may be hard), then make the
      easy change — and recommends targeting at least half of all commits as
      refactorings. The gap: the "make the change easy, then make the easy
      change" discipline is not captured. Coverage check: TS-9 defines a
      `Refactor` revision type but does not state the two-step sequencing or
      the commit-ratio heuristic. Recommend placing at `04-commits.adoc`
      (Revision types / Refactor). Cross-references: TS-7 (Code design),
      TS-8 (Issue tracking).

      **Resolved.** Closed by a new "Refactor commit discipline" subsection
      in `04-commits.adoc`, directly after the "Quality revisions versus
      refactoring" sidebar within the Revision types section. States Beck's
      two-step sequencing as a default way of working (not just a fallback
      for refactors discovered mid-task, cross-referencing the existing
      `git stash` tip under "Atomic commits"), recommends roughly half of a
      project's commits be `refactor` commits, and names a low refactor-
      commit proportion as a signal that changes are being forced into
      unprepared code. Cross-references TS-7 (Code design) and TS-8 (Issue
      tracking), where the same gap was independently recorded for the
      design and ticketing sides of refactoring — those items remain open in
      their own files; this closes only TS-9's version-control-practice
      angle. Source added to the page's `== References`.

## Partial

(The original analysis recorded no partial-coverage items.)

## Out-of-scope

(Converted from the legacy format; the format recorded no such items.)

## Unresolved

(Converted from the legacy format; the format recorded no such items.)
