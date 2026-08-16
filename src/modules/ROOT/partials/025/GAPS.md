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
subsection in `11-when-not-to-document.adoc`.

**2026-08-15 addendum.** One new Missing item was added, routed here from
TS-26 (Technical writing style guide) while it was working its own
Out-of-scope backlog — the item itself started life routed to TS-26 from
TS-27 (Markdown), then TS-26 judged it lifecycle/process content rather
than sentence-level style and routed it on to TS-25 instead. Not yet
actioned. 1 missing, 0 partial, 0 out-of-scope awaiting the user, 0
unresolved.

**Run 2 (`close-gaps`), 2026-08-16.** Closed the remaining Missing item —
the documentation review-etiquette gap routed in from TS-26/TS-27 — with a
new "Reviewing documentation" subsection in `10-ownership.adoc`. TS-25 now
has 0 actionable items, 0 Out-of-scope items, and 0 Unresolved items — fully
resolved.

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

- [x] https://google.github.io/styleguide/docguide/style.html#minimum-viable-documentation
      and https://google.github.io/styleguide/docguide/style.html#better-is-better-than-best
      (routed in from TS-26's Out-of-scope review, 2026-08-15, which was
      itself routed in from TS-27's Out-of-scope review) — documentation
      process philosophy: "a small set of fresh and accurate docs is
      better than a sprawling, loose assembly of documentation in various
      states of disrepair," maintaining docs with the rigor applied to
      code and tests, regularly removing outdated content in small
      increments, and a review-etiquette standard distinct from code
      review ("when reasonable, LGTM immediately and trust that comments
      will be fixed appropriately"; authors should "avoid wasting cycles
      with trivial argument, capitulate early and move on"). TS-26
      confirmed this is documentation lifecycle/process content, not
      sentence-level style, and routed it here since that is exactly the
      scope split stated in both standards' opening paragraphs. Coverage
      check: `10-ownership.adoc` already covers staleness and ownership in
      similar spirit ("prefer documentation whose staleness is
      self-evident... over documentation whose staleness is silent"), but
      neither it nor any other partial addresses the review-etiquette
      half (approving documentation PRs quickly, not blocking on
      perfection) or the explicit "delete outdated content in small
      increments" practice. Recommend expanding `10-ownership.adoc`, or a
      new subsection, covering the review-etiquette angle specifically as
      the genuinely new material. Not yet checked in depth or written into
      any partial.

      **Resolved, 2026-08-16.** Re-fetched the source to confirm the exact
      wording before writing. Closed by a new "Reviewing documentation"
      subsection in `10-ownership.adoc`, after the existing staleness
      guidance it extends. States the minimum-viable-documentation
      principle (small, fresh, accurate beats sprawling and stale) and the
      small-increments deletion discipline verbatim from the coverage
      check; then covers the review-etiquette half that was the genuinely
      new material: a reviewer SHOULD approve immediately where
      reasonable rather than blocking on minor comments, SHOULD suggest a
      specific alternative rather than a vague one and raise a
      disagreement as their own follow-up rather than blocking on it, and
      an author SHOULD capitulate early on trivial argument rather than
      defend it at length. Cross-linked to the existing "Support-driven
      documentation" section, explaining why both share the same
      underlying concern (cheap-to-update documentation stays current).
      Source added to the page's `== References`.

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
