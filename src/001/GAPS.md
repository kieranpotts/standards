# GAPS — TS-1 Software Requirements Specification

Coverage gaps identified by comparing external sources against this standard.

---

## Prioritizing quality attributes by relative importance

- **Source**: https://stackoverflow.blog/2022/01/17/plan-for-tradeoffs-you-cant-optimize-all-software-quality-attributes/
- **What the source says**: Quality attributes must be prioritized relative to one another, just as functional requirements are, so that designers and architects know which qualities matter most for a given product.
- **Coverage check**: TS-1 covers MoSCoW prioritization of individual proposals (which may be quality requirements) but does not address ranking the quality attributes themselves by importance as an input to design decisions.
- **Gap**: No guidance on prioritizing quality attributes relative to one another for a given product.

---

## Cost-benefit balancing of quality goals

- **Source**: https://stackoverflow.blog/2022/01/17/plan-for-tradeoffs-you-cant-optimize-all-software-quality-attributes/
- **What the source says**: The value of achieving a quality goal must be weighed against the cost of achieving it (e.g. 24/7 availability required expensive redundant systems that were cheaper than the downtime they prevented).
- **Coverage check**: Neither TS-1 nor TS-2 discusses the cost of achieving quality attributes or a value-vs-cost framing. TS-50 covers cloud spend but not the general principle.
- **Gap**: No standard covers the economic trade-off of quality goals — weighing business value against implementation cost.
- **Cross-references**: TS-2 (Software Design Qualities), TS-50 (Cloud Economics)

---

## Eliciting and clarifying nonfunctional/quality requirements

- **Source**: https://stackoverflow.blog/2022/01/17/plan-for-tradeoffs-you-cant-optimize-all-software-quality-attributes/
- **What the source says**: Business analysts must probe what stakeholders mean by vague terms like "reliable" or "user-friendly," including how one would tell whether the system meets the quality bar and examples of not meeting it.
- **Coverage check**: TS-1's requirements elicitation section covers five techniques (impact mapping, use cases, event storming, story mapping, example mapping) but all are framed around discovering functional scope. The qualities section covers specifying NFRs measurably but not the elicitation questioning technique for surfacing what stakeholders actually mean.
- **Gap**: No guidance on elicitation techniques tailored to nonfunctional/quality requirements.