# GAPS — TS-3 Design Docs

Coverage gaps identified by comparing external sources against this standard.

---

## Evaluating candidate technologies against real-world conditions

- **Source**: https://newsletter.posthog.com/p/how-we-choose-technologies
- **What the source says**: Teams evaluate technologies "as close to reality as possible" — building proof-of-concepts tested with real slow queries, mirroring live traffic to project costs/performance, and treating POCs as quarterly goals.
- **Coverage check**: TS-3's RFC section acknowledges that a prototype MAY be conducted as part of writing the RFC, but gives no methodology for how to evaluate a candidate technology against real workloads.
- **Gap**: No guidance on running proof-of-concept evaluations of candidate technologies against realistic production workloads.
- **Cross-references**: TS-14 (Performance Testing)

---

## Criteria for rejecting a technology proposal

- **Source**: https://newsletter.posthog.com/p/how-we-choose-technologies
- **What the source says**: Even well-researched RFCs are sometimes rejected, for reasons including lack of maturity, poor fit for other teams, more important criteria surfacing during review, and real-world evaluation contradicting expectations.
- **Coverage check**: TS-3 defines a "Rejected" lifecycle state and a review process that solicits stakeholder feedback, but gives no guidance on what constitutes valid grounds for rejecting a technology proposal.
- **Gap**: No enumerated rejection criteria for technology decisions (maturity, cross-team fit, evaluation-vs-expectation divergence).