# TS-1: Software Requirements Specification

This is a compact version of technical standard TS-1 for AI agents.

Use this when writing, reviewing, or evaluating software requirements
specifications (SRS), acceptance criteria, the structure of a spec (context vs
requirements), Gherkin feature files, qualities (non-functional requirements),
the proposal lifecycle, or Definition of Ready checklists.

A reference implementation is maintained at
[kieranpotts/specs](https://github.com/kieranpotts/specs).

Do NOT use this when writing a product requirements document (PRD). The PRD is
an upstream, informal, product-owned artifact that provides input to
requirements discovery. The SRS turns the PRD into a formal, testable,
maintained specification.

## Rules

- **Requirements MUST be written in business language.**

  Requirements MUST be understandable to business stakeholders.

  Requirements SHOULD be written and maintained in collaboration between the
  customers (or a representative such as a product owner) and the development
  team.

- **Requirements MUST be written as acceptance criteria.**

  Acceptance criteria (ACs) — aka. conditions of satisfaction — MUST be written
  from the perspective of end users.

  ACs SHOULD define user needs without prescribing solutions. ACs SHOULD NOT
  include technical implementation details, or even make reference to software.

- **ACs MUST cover both functional and non-functional requirements.**

  A solution is "correct" only if it meets both. See also:

  - [TS-13: Functional Testing](../013/AGENTS.md)
  - [TS-14: Performance Testing](../014/AGENTS.md)

- **Specs MUST distinguish context from requirements.**

  - **Context** is descriptive, describing what _is_. Examples:

    - Overview (mission/problem/scope).
    - Constraints (regulatory/legal/business + assumptions + dependencies)
    - Model (domain entities + relationships)
    - Actors (participants + privilege hierarchy).
    - Glossary (ubiquitous language).

  - **Requirements** are prescriptive, describing what _should be_. SHOULD be
    organized into:

    - **Behaviors** (functional requirements).
    - **Qualities** (non-functional requirements).

- **Behaviors SHOULD be documented across five sections.**

  - **Features** (concrete, scenario-level behaviors, organized by the actors
    who are permitted to access them).
  - **Rules** (policies, invariants, and lifecycle transitions spanning many
    features).
  - **Access** (which actors may exercise which capabilities).
  - **Interfaces** (the external contract — operations, resources, events).
  - **Journeys** (how features combine into end-to-end flows).

  Recommended tree:

  ```
  specification/
  ├── context/            Overview, constraints, model, actors, glossary.
  └── requirements/
      ├── behaviors/      Features, rules, access, interfaces, journeys.
      └── qualities/
  proposals/              Immutable archive.
  ```

  Privileges are inherited down the actor hierarchy. An actor holds every
  capability of the actors below it. State each capability once, against the
  lowest-privileged actor that holds it.

- **Every requirement MUST have a stable identifier.**

  - `F` features, `Q` qualities, `R` rules.
  - Two-part where one artifact holds several verifiable statements: `F3.2` is
    the second scenario of feature `F3`; `Q1.4` the fourth threshold of quality
    `Q1`. Rules are atomic, so single-part.
  - Identifiers are permanent. Never reuse one, even after the requirement is
    removed.

- **RECOMMENDED to use Gherkin for functional requirements.**

  Gherkin is a business-readable DSL that provides a testable specification
  format parseable by frameworks such as Cucumber, SpecFlow, Behat, JBehave, and
  Lettuce.

  `.feature` files live under `requirements/behaviors/features/`.

  Basic Gherkin structure:

  - A file MUST contain at most one `Feature` block.

  - Structure comes from **keywords**, not indentation — parsers ignore
    leading whitespace outside doc strings. Two-space nesting is convention.

  - Scenarios are composed of steps using keywords:
    `Given`, `When`, `Then`, `And`, `But`. An `*` may stand in for any of them.

  - Aim for five or fewer steps per scenario, and one or two `When` steps.

  - Steps name actions in business terms, not the mechanics of performing them.
    "When the customer submits their credentials", not "When the customer fills
    the username field and presses the login button".

  - A `Background` section MAY hold repeated `Given` steps shared across all
    scenarios in a file.

  - A step MAY carry an argument: a doc string (`"""`) for prose, or a data
    table (`|`) for structured values. A step data table is not an `Examples`
    table — it is an argument to one step, not a scenario generator.

  - A `Rule:` block groups the scenarios illustrating one business rule, and
    SHOULD name the rule's identifier. (Later language addition — confirm
    framework support.)

  - Tags (`@…`) select subsets for the test runner, and MAY cross-reference
    requirement identifiers (`@R3`, `@Q1.4`) to bind a scenario to what it
    verifies. Keep the tag vocabulary small and agreed.

  - Scenario outlines with `Examples` tables allow parameterized scenarios. Each
    row generates one ordinary `Scenario`. Do NOT automate scenario outlines via
    UI automation (eg. Selenium) — they should communicate directly with the
    business rule implementation.

  - A scenario SHOULD NOT restate a centrally-stated rule. Reference it by
    identifier instead.

  Feature file template:

  ```feature
  Feature: <title>
    In order to <realize some business value>
    As a <user type>
    I want to <achieve some goal>

    Background:
      Given <state>

    Scenario: <title>
      Given <state or precondition>
      When <event or action>
      Then <expected outcome>
  ```

- **Executable specifications SHOULD gate the build.**

  Where a requirement is expressed as an executable specification — a Gherkin
  scenario, a quality benchmark, a security scan — the build SHOULD fail when
  that check fails. A specification that can be silently violated is only as
  trustworthy as whoever remembers to check it by hand.

- **Distinguish dynamic qualities from static qualities.**

  Non-functional requirements (NFRs) define operational constraints such as
  security, performance, scalability, availability, data retention, etc. The
  scope of NFRs is dynamic quality attributes, which are externally-observable
  at runtime.

  NFRs SHOULD NOT cover static qualities, which are observable at compile-time,
  such as internal code design, modularity, etc. These are design choices, not
  requirements.

- **NFRs SHOULD be measurable, testable acceptance criteria.**

  Wherever a quality is objectively measurable, it MUST be stated as a concrete
  threshold, ideally at a named percentile and load: "list responses within
  300 ms at the 95th percentile under normal load", not "the API should be
  fast."

  Where possible, specify metrics (MTBF, MTTR, crash rate) or conformance to
  published standards. Cite a version and conformance level: "WCAG 2.2 Level
  AA", not "accessible"; TLS 1.3, not SSL/TLS.

  The exception is the genuinely subjective — UX, for example — which is
  satisfied through user research, A/B testing, or satisfaction surveys rather
  than a threshold.

- **Some NFRs SHOULD be expressed as user stories.**

  Quality attributes that lend themselves to conventional functional testing —
  notably authentication and authorization — SHOULD be expressed as user
  stories within the functional requirements, rather than as standalone
  qualities.

- **NFRs MUST be identified as early as possible.**

  Many NFRs are architecturally significant, heavily influencing fundamental
  design choices such as technology stacks and databases, and are therefore much
  harder to change later than functional requirements.

  Some NFRs, such as uptime guarantees, are also reflected in service level
  agreements (SLAs) and so matter directly to business stakeholders.

- **A specification is a living document bound to production.**

  The main line MUST describe the as-is production system. A proposal's spec
  edits MUST be merged in the same change-set as the code that implements them,
  and MUST NOT be merged ahead of it.

  Reconcile any divergence found during implementation back into the spec before
  release.

  Persist the spec under the same version control as the code. Wikis and issue
  trackers drift.

- **Changes go through a proposal lifecycle, recorded permanently.**

  `DRAFT` → `PROPOSED` → `ACCEPTED` → `RELEASED` → `SUPERSEDED`,
  or `PROPOSED` → `REJECTED`.

  `PROPOSED` → `DRAFT` (rework) is the only permitted backward transition. No
  skipped states.

  An `ACCEPTED` proposal MAY continue to evolve during implementation. That is
  expected, and does not need re-approval. What was approved is the intent. If
  the *intent* turns out to be wrong, supersede the proposal rather than
  rewriting it.

  Keep two artifacts side by side: the mutable spec, and an immutable
  append-only archive of every proposal (including rejected ones).

  Merged proposals are immutable and get a stable id.

  To revisit a decision, supersede the prior proposal with a new proposal.

  Scope each proposal atomically (one feature/quality). Group dependent ones
  under an epic.

  Review cross-functionally: product for scope and intent, QA for ambiguous
  acceptance criteria, engineering for feasibility.

  Record rejections as carefully as acceptances. Revert the spec edits, but
  preserve the proposal document.

- **Specify the end state, not a changelog.**

  Write "authenticated callers can filter by species," not "add a species
  filter."

  The spec says _what_ (timeless present). The proposal says _why_ (motivation,
  alternatives, trade-offs).

  Don't smuggle rationale into the spec or restate the spec in the proposal.

  Rollout mechanics — migration steps, sequencing, feature flags — MUST NOT
  appear in the specification.

- **Trace requirements to their implementation.**

  Where tooling allows, link each requirement to its implementing component,
  test suite, and tracking ticket, citing its identifier (`F3.2`, `Q1.4`).

- **A Definition of Ready (DoR) is RECOMMENDED.**

  The DoR SHOULD be a short checklist confirming requirements readiness before
  development begins. Example criteria:

  - Are requirements clear and unambiguous?

  - Are acceptance criteria defined in a testable, automatable format?

  - Is it clear who the stakeholders are?

  - Does the team have the knowledge and resources to complete the task?

  - Can the work be done independently and implemented in small increments?

  - Can the design be iterated based on feedback?

  Its counterpart, the Definition of Done, is a delivery concern — see
  [TS-12: Quality Assurance](../012/AGENTS.md).

## Elicitation techniques

Gherkin is the format for detailed ACs, but not the tool for discovering them.
Earlier in a spec's life:

- **Use case analysis** — a complete interaction between an actor and the
  system in pursuit of a goal. Maps an actor's full scope before it is broken
  down.

- **Event storming** — a workshop technique for exploring a domain. Domain
  events (orange), commands (blue), actors (small yellow), aggregates (large
  yellow), hotspots (pink). Good fit for event-driven architectures.

- **Story mapping** — arranges stories into a backbone of journey steps,
  sliced horizontally into releases. Stories SHOULD meet INVEST (Independent,
  Negotiable, Valuable, Estimable, Small, Testable). Split along workflow steps,
  rule variations, data variations, or operations — never by architectural
  layer.

- **Example mapping** — a timeboxed workshop breaking one story into rules
  (yellow), examples (green), and questions (red). Red cards block. Translates
  directly into Gherkin, so it is the RECOMMENDED final step before scenarios
  are written.
