# Requirements Specification

This is a compact version of technical standard TS-1 for AI agents.

Use this when writing, reviewing, or evaluating software requirements specifications (SRS), acceptance criteria, Gherkin feature files, non-functional requirements, or Definition of Ready checklists.

## Rules

The capitalized words REQUIRED, MUST, MUST NOT, RECOMMENDED, SHOULD, SHOULD NOT, OPTIONAL, and MAY are to be interpreted as described in [IETF RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

-   **Requirements SHOULD be written in language derived from the business domain.**

    They SHOULD be understandable to business stakeholders and SHOULD be written and maintained in collaboration between the customers (or a representative such as a product owner) and the development team.

-   **Requirements SHOULD be written as acceptance criteria.**

    Acceptance criteria (ACs) — aka. conditions of satisfaction — SHOULD be written from the perspective of end users, defining user needs without prescribing solutions. ACs SHOULD NOT include technical implementation details or make reference to software.

-   **ACs MUST be written in a consistent style using business-domain language.**

-   **ACs MUST cover both functional and non-functional requirements.**

    A solution is "correct" only if it meets both. See [TS-13: Functional Testing](../013/AGENTS.md) and [TS-14: Performance Testing](../014/AGENTS.md).

-   **For complex systems, it is RECOMMENDED to use the Gherkin language for functional requirements.**

    Gherkin is a business-readable DSL that provides a testable specification format parseable by frameworks such as Cucumber, SpecFlow, Behat, JBehave, and Lettuce.

    Basic Gherkin structure:
    - Each feature is described in a `.feature` file.
    - Features contain one or more **Scenarios**.
    - Scenarios are composed of **Steps** using `Given`, `When`, `Then`, `And`, `But` keywords.
    - Aim for five or fewer steps per scenario.
    - A **Background** section can hold repeated `Given` steps shared across all scenarios in a file.
    - **Scenario Outlines** with `Examples` tables allow parameterised scenarios. Do NOT automate scenario outlines via UI automation (eg. Selenium); they should communicate directly with the business rule implementation.

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

-   **NFRs SHOULD be specified as measurable, testable acceptance criteria.**

    Non-functional requirements (NFRs) define operational constraints: security, performance, scalability, availability, data retention, etc. Where possible, specify metrics (MTBF, MTTR, crash rate) or conformance to published standards (eg. AES-256, WCAG, GDPR). NFRs that map cleanly to authorization/authentication rules SHOULD be expressed as user stories within the functional requirements.

-   **NFRs MUST be identified as early as possible.**

    Many NFRs are architecturally significant and difficult to change later.

-   **It is RECOMMENDED that projects have a Definition of Ready (DoR).**

    The DoR SHOULD be a short checklist confirming requirements readiness before development begins. Example criteria:
    - Are requirements clear and unambiguous?
    - Are acceptance criteria defined in a testable, automatable format?
    - Does the team have the knowledge and resources to complete the task?
    - Can the work be done independently and implemented in small increments?

## References

- [TS-1: Requirements Specification](./README.adoc) — source standard
- [TS-13: Functional Testing](../013/AGENTS.md) — verification of functional requirements
- [TS-14: Performance Testing](../014/AGENTS.md) — verification of non-functional/performance requirements
