# TS-3 gap analysis

Gaps found comparing TS-3: Design docs against the following reference
resources:

- https://newsletter.posthog.com/p/how-we-choose-technologies

**Assessment.** A single-source analysis against PostHog's account of how it
chooses technologies, which found the RFC section silent on two points: how
to evaluate a candidate technology against real workloads, and what counts
as valid grounds for rejecting a proposal. Converted from the legacy format
on 2026-08-13.

**Status:** 2 of 2 actionable gaps closed (2026-08-13). This run converted
the file from the legacy format and closed both gaps. 0 missing, 0 partial,
0 out-of-scope, 0 unresolved remain.

## Missing

- [x] https://newsletter.posthog.com/p/how-we-choose-technologies says teams
      evaluate technologies "as close to reality as possible" — building
      proof-of-concepts tested with real slow queries, mirroring live
      traffic to project costs/performance, and treating POCs as quarterly
      goals. The gap: no guidance on running proof-of-concept evaluations of
      candidate technologies against realistic production workloads.
      Coverage check: TS-3's RFC section acknowledges that a prototype MAY
      be conducted as part of writing the RFC, but gives no methodology for
      how to evaluate a candidate technology against real workloads.
      Recommend placing in `03-requests-for-comments.adoc`, near the
      existing prototyping paragraph in "When an RFC is warranted".
      Cross-references: TS-14 (Performance testing).

      **Resolved.** Closed by a new "Evaluating candidate technologies"
      subsection in `03-requests-for-comments.adoc`, under "When an RFC is
      warranted". States that a prototype is most convincing when it tests
      candidates against realistic workloads and traffic shapes rather than
      a synthetic benchmark, recommends mirroring live traffic or running a
      shadow deployment, requires the evaluation be bounded to a scoped
      question and deadline, and requires the result — including a
      candidate ruled out — be recorded in the RFC's "Alternatives
      considered" section. Cross-references TS-14 (Performance testing) for
      the testing methodology such an evaluation draws on. Source added to
      the page's `== References`.

- [x] https://newsletter.posthog.com/p/how-we-choose-technologies says even
      well-researched RFCs are sometimes rejected, for reasons including
      lack of maturity, poor fit for other teams, more important criteria
      surfacing during review, and real-world evaluation contradicting
      expectations. The gap: no enumerated rejection criteria for technology
      decisions (maturity, cross-team fit, evaluation-vs-expectation
      divergence). Coverage check: TS-3 defines a "Rejected" lifecycle state
      and a review process that solicits stakeholder feedback, but gives no
      guidance on what constitutes valid grounds for rejecting a technology
      proposal. Recommend placing in `03-requests-for-comments.adoc`, under
      "Review", where the review process is described.

      **Resolved.** Closed by a new "Grounds for rejection" subsection in
      `03-requests-for-comments.adoc`, under "Review". States that a
      well-researched RFC is not entitled to acceptance, and enumerates four
      valid grounds — immaturity of a central technology, poor fit beyond
      the proposing team, a more important criterion surfacing during
      review, and real-world evaluation contradicting the design's original
      assumptions. Requires a rejection to state which ground applied and to
      be as specific as the "Alternatives considered" section it mirrors.
      Cross-references the new "Evaluating candidate technologies"
      subsection for the prototype-evaluation ground, and "Immutability" for
      why rejected RFCs are preserved rather than discarded. Source added to
      the page's `== References`.

## Partial

(The original analysis recorded no partial-coverage items.)

## Out-of-scope

(Converted from the legacy format; the format recorded no such items.)

## Unresolved

(Converted from the legacy format; the format recorded no such items.)
