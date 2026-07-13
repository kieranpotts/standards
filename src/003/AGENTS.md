# TS-3: Design Docs

This is a compact version of technical standard TS-3 for AI agents.

Use this when writing, reviewing, or maintaining: a living description of a system's architecture (design docs), a record of why a significant technical decision was made (RFCs), or a point-in-time evaluation of an as-built system's structural health (architecture audits).

Reference implementations are maintained at [kieranpotts/design](https://github.com/kieranpotts/design), [kieranpotts/rfc](https://github.com/kieranpotts/rfc), and [kieranpotts/audits](https://github.com/kieranpotts/audits).

Do NOT use this for the SRS (see [TS-1](../001/AGENTS.md)) — the *what* the system does — or for the qualities a good design exhibits (see [TS-2](../002/AGENTS.md)).

## Rules

The capitalized words REQUIRED, MUST, MUST NOT, RECOMMENDED, SHOULD, SHOULD NOT, OPTIONAL, and MAY are to be interpreted as described in [IETF RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

-   **Keep each of the three artifacts in its lane.**

    Design docs state *what* the architecture is. RFCs state *why* a decision was made. Audits state *how healthy* the as-built system is. None restates another — each links to its neighbors instead.

-   **Design docs are living and decision-free.**

    Written in the present tense, describing production as it exists right now. A design-change PR does NOT merge until the corresponding change is live. Do NOT record rationale in a design doc — link to the RFC instead.

    Organize design docs into views extended from the 4+1 model: conceptual, logical, development, process, physical, technical, and a cross-cutting scenarios view. Keep each artifact in the view where it belongs.

-   **RFCs record one significant technical decision, permanently.**

    An RFC MUST be a single, atomic decision — motivation, alternatives considered, trade-offs accepted, and the outcome. Warranted when a change impacts multiple stakeholders and is worth building consensus on: architecture/data-model changes, stack or infra changes, interface changes, SLA-affecting changes, tooling/process changes, standards changes.

    Lifecycle: `DRAFT` → `PROPOSED` → `ACCEPTED` → `IMPLEMENTED` → `SUPERSEDED`, or `PROPOSED` → `REJECTED`. No backward or skipped transitions. Every RFC MUST have a discussion thread, separate from the PR's own comments.

    An RFC's document is immutable once merged (`IMPLEMENTED` or `REJECTED`) — only status, date, and cross-references may change thereafter. Never delete an RFC, including rejected ones. To revisit a decision, open a new RFC that supersedes it.

-   **Audits are standalone, point-in-time, and evaluation-only.**

    An audit is a snapshot of structural health, immutable once merged. To reassess, run a new audit — never edit a merged one.

    Findings MUST cite specific files and lines, state what is observed and the cost it imposes. A finding MAY point toward a fix, but MUST NOT work up an alternative design.

    An audit is deliberately blind to the design docs — it MUST NOT cross-reference them or report drift from them, to keep the review unbiased. Security and privacy are out of scope (see [TS-54: Threat Modeling](../054/AGENTS.md)).

    An audit MUST NOT change code, file issues, or open PRs against the audited repositories — discovery only. No discussion thread is required; plain PR review is sufficient, since an audit presents findings, not a decision.

-   **Store all three in version control, close to the code.**

    Markdown is acceptable for shorter documents (an RFC, an audit report); AsciiDoc is RECOMMENDED for longer, structured documents such as design docs with multiple views. Diagrams SHOULD be authored as text (Mermaid, PlantUML, Structurizr DSL). Every supporting artifact MUST be referenced from its document's entry point, or it isn't part of the record.

-   **Don't gate progress on wide review; do reconcile drift as it's found.**

    Seek crucial feedback directly rather than waiting on a wide review cycle. When a design doc is found to have drifted from production, fix it before the next merge — a description that is mostly true is one nobody can trust.
