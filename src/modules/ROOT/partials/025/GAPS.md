# TS-25 gap analysis

Gaps found comparing TS-25: Technical documentation against the following
reference resources:

- https://blog.nelhage.com/post/computers-can-be-understood/

**Assessment.** The single source is an essay arguing that computer systems
are comprehensible if you are willing to read their source, and it yielded one
gap — missing coverage rather than partial treatment. TS-25 said when a
document can be skipped without saying anything about the bias that leads the
people closest to the code to skip it too often. Converted from the legacy
format on 2026-08-13.

**Status:** 1 of 1 actionable gaps closed (2026-08-13). This run converted the
file to the template format and closed the source-reading bias gap with a new
subsection in `11-when-not-to-document.adoc`. Nothing remains open: 0 missing,
0 partial, 0 out-of-scope awaiting the user, 0 unresolved.

## Missing

- [x] https://blog.nelhage.com/post/computers-can-be-understood/ says that
      engineers most comfortable reading unfamiliar codebases tend to
      undervalue documentation — "since they have gotten good at getting
      answers without it" — and are often worse at documenting their own
      systems than the median engineer, which is a team-level risk. The gap:
      TS-25 does not warn that engineers adept at reading source tend to
      under-invest in documentation, nor offer mitigations for that dynamic.
      Coverage check: TS-25's "when not to document" and "principles"
      sections cover when code can self-document and what makes docs good,
      but neither addresses this team dynamic: that strong source-reading
      skills create a bias against writing documentation. Recommend placing
      at `11-when-not-to-document.adoc`, as a closing subsection of the
      section whose judgment the bias distorts.

      **Resolved.** Closed by `11-when-not-to-document.adoc`, "The
      source-reading bias" subsection. States that the decision to skip a
      document is usually made by the person least likely to need it, that
      the engineers most comfortable reading unfamiliar codebases therefore
      risk habitually undervaluing documentation and can document their own
      systems worse than the median engineer, and that fluency at reading
      source suppresses the signal that would otherwise expose the omission —
      the author never gets stuck, so the cost lands on slower readers, on
      operators who cannot read the source at all, and on whoever is called
      out at three in the morning. Names this a property of teams rather than
      a failing of individuals, and reconciles it with the standard's
      existing position that only the source is authoritative (the "Process
      documentation" section) by separating accuracy from cost. Requires that
      "the code is self-documenting" be treated as a claim to be tested
      rather than one the code's author can settle alone, with three rules: a
      reader who has not read the implementation makes the call, and an
      answer given in a review thread SHOULD go into the documentation
      instead; newcomers draft the onboarding material and maintainers review
      it for accuracy, rather than the reverse; and a recurring question is a
      defect in the documentation, per the "Support-driven documentation"
      section. Names code review as the enforcement point for all three, per
      the "Ownership and staleness" section, and closes by noting that a
      reviewer who could have answered the question from the diff is not
      evidence the document was unnecessary. Source added to the page's
      `== References`.

## Partial

(Converted from the legacy format on 2026-08-13. The original analysis
recorded no partial-coverage items.)

## Out-of-scope

(Converted from the legacy format on 2026-08-13. The legacy format has no
concept of out-of-scope items, and the original analysis recorded none.)

## Unresolved

(Converted from the legacy format on 2026-08-13. The legacy format has no
concept of unresolved reference resources, and the original analysis recorded
none.)
