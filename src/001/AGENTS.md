# TS-1: Requirements Specification

This is a compact version of technical standard TS-1 for AI agents.

Use this when writing, reviewing, or evaluating software requirements specifications (SRS): acceptance criteria, the structure of a spec (context vs requirements), Gherkin feature files, qualities (non-functional requirements), the proposal lifecycle, or Definition of Ready checklists.

A reference implementation is maintained at [kieranpotts/specs](https://github.com/kieranpotts/specs).

Do NOT use this when writing product product requirements documents (PRD). This is an upstream, informal, product-owned artifact tht provides input to discovery. The SRS turns the PRD into a formal, testable, maintained specification.

## Rules

The capitalized words REQUIRED, MUST, MUST NOT, RECOMMENDED, SHOULD, SHOULD NOT, OPTIONAL, and MAY are to be interpreted as described in [IETF RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

-   **Requirements MUST be written in business language.**

    Requirements MUST be understandable to business stakeholders.

    Requirements SHOULD be written and maintained in collaboration between the customers (or a representative such as a product owner) and the development team.

-   **Requirements MUST be written as acceptance criteria.**

    Acceptance criteria (ACs) — aka. conditions of satisfaction — MUST be written from the perspective of end users.

    ACs SHOULD define user needs without prescribing solutions. ACs SHOULD NOT include technical implementation details or make reference to software.

-   **ACs MUST cover both functional and non-functional requirements.**

    A solution is "correct" only if it meets both. See [TS-13: Functional Testing](../013/AGENTS.md) and [TS-14: Performance Testing](../014/AGENTS.md).

-   **Specs MUST distinguish context from requirements.**

    - *Context* is descriptive, describing what _is_. (what _is_). Examples: overview (mission/problem/scope), constraints (regulatory/legal/business + assumptions + dependencies), glossary (ubiquitous language), model (domain entities + relationships), actors (participants + privilege hierarchy).

    - *Requirements* are prescriptive, describing what _should be_. Examples: behaviors (functional) and qualities (non-functional).

-   **RECOMMENDED to use Gherkin for functional requirements.**

    Gherkin is a business-readable DSL that provides a testable specification format parseable by frameworks such as Cucumber, SpecFlow, Behat, JBehave, and Lettuce.

    Basic Gherkin structure:

    - Each feature is described in a `.feature` file.

    - Features contain one or more *Scenarios*.

    - Scenarios are composed of *Steps* using `Given`, `When`, `Then`, `And`, `But` keywords.

    - Aim for five or fewer steps per scenario.

    - A *Background* section can hold repeated `Given` steps shared across all scenarios in a file.

    - *Scenario Outlines* with `Examples` tables allow parameterised scenarios. Do NOT automate scenario outlines via UI automation (eg. Selenium) – they should communicate directly with the business rule implementation.

    Feature file template:

    ```feature
    Feature: {title}
      In order to {realize some business value}
      As a {user type}
      I want to {achieve some goal}

      Background:
        Given {state}

      Scenario: {title}
        Given {state or precondition}
        When {event or action}
        Then {expected outcome}
    ```

-  **Distinguish dynamic qualiities from static qualities.**

    Non-functional requirements (NFRs) define operational constraints such as security, performance, scalability, availability, data retention, etc. The scope of NFRs is *dynamic quality attributes*, which externally-observable at runtime, eg. security, latency, availability.

    NFRS SHOULD NOT cover *static qualitities*, which are observable at compile-time, such as internal code design, modularity, etc. These are design choices, not requirements.

-   **NFRs SHOULD be measurable, testable acceptance criteria.**

    Where possible, specify metrics (MTBF, MTTR, crash rate) or conformance to published standards (eg. AES-256, WCAG, GDPR).

-  **It MAY be appropriate to express some NFRs as user stories.**

    Example: NFRs that map cleanly to authorization/authentication rules SHOULD be expressed as user stories within the functional requirements.

-   **NFRs MUST be identified as early as possible.**

    Many NFRs are architecturally significant and expensive to change later. Avoid iterating on NFRs. Big-design-up-front is preferred for NFRs.

-   **A specification is a living document bound to production.**

    The main line MUST describe the as-is production system. An accepted change MUST NOT be merged until it is live in production (the one exception: a rejected proposal merges its document only, with spec edits reverted).

    Reconcile any divergence found during implementation back into the spec before release.

-   **Changes go through a proposal lifecycle, recorded permanently.**

    `DRAFT` → `PROPOSED` → `ACCEPTED` → `RELEASED` → `SUPERSEDED`, or `PROPOSED` → `REJECTED`. No backward or skipped transitions.

    Keep two artifacts side by side: the mutable spec, and an immutable append-only archive of every proposal (including rejected ones — record rejections as carefully as acceptances).

    Merged proposals are immutable and get a stable id. To revisit a decision, supersede the prior proposal with a new proposal.

    Scope each proposal atomically (one feature/quality). Group dependent ones under an epic.

-   **Specify the end state, not a changelog.**

    Write "authenticated callers can filter by species," not "add a species filter."

    The spec says _what_ (timeless present). The proposal says _why_ (motivation, alternatives, trade-offs).

    Don't smuggle rationale into the spec or restate the spec in the proposal.

-   **A Definition of Ready (DoR) is RECOMMENDED.**

    The DoR SHOULD be a short checklist confirming requirements readiness before development begins. Example criteria:

    - Are requirements clear and unambiguous?

    - Are acceptance criteria defined in a testable, automatable format?

    - Does the team have the knowledge and resources to complete the task?

    - Can the work be done independently and implemented in small increments?
