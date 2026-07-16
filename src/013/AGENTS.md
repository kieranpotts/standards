# TS-13: Functional Testing

This is a compact version of technical standard TS-13 for AI agents.

Use this when designing, writing, or reviewing functional tests — test
strategies, test types, test levels, coverage, test doubles, TDD, and test
design. Functional testing evaluates the correct operation of a software system
across normal operation, edge cases, and error conditions, recording observed
behaviors against expected outcomes from the requirements.

Do NOT use this for non-functional test types (performance, security,
accessibility, usability, compliance, recovery) — those are covered by
[TS-14: Performance Testing](../014/AGENTS.md). For the QA process around
testing (Definition of Done, code review, quality gates, metrics) see
[TS-12: Quality Assurance](../012/AGENTS.md). All test code is subject to the
same coding standards as application code.

## Rules

- **Testing MUST be a fundamental, integral part of the development process —
  not a separate phase following implementation.**

  All test code is subject to the same coding standards as application code.

### Test strategies

Test strategies address _how_ and _when_ tests are deployed across the
lifecycle (test types define _what_, test levels define _where_).

- **Regression testing: re-run existing tests after code changes to catch
  regressions.**

  The primary defense against change-introduced defects. Any test type (unit,
  integration, system, acceptance) can serve as a regression test — the label
  describes the practice of repeatedly running tests to detect unintended side
  effects. Most critical after bug fixes, feature additions, refactoring,
  dependency updates, and infrastructure changes. Maintain an automated suite
  that executes quickly and frequently (speed is essential — slow suites get
  run less often); integrate into CI on every change; prioritize by criticality
  and likelihood of being affected; review/update the suite regularly (remove
  obsolete tests, add coverage for new features and recently fixed bugs); use
  version control and diffs to focus effort on changed areas.

- **Smoke testing: quickly determine whether a new build is stable enough to
  warrant further testing.**

  Cover only the most critical functionality and common user paths — not
  thorough; purpose is to catch catastrophic failures early. Most valuable as
  the first stage of a testing pipeline: if smoke tests fail, reject the build
  immediately. Keep smoke tests fast (minutes, not hours); automate and run as
  the first step after every build; reject any failing build for immediate
  investigation; update when the definition of "critical functionality"
  changes.

- **Negative testing: intentionally test with invalid inputs, unexpected
  conditions, and error scenarios.**

  Verify the system handles gracefully what it _should not_ have to do. A
  system that works under ideal conditions but crashes under adverse conditions
  is not fit for production. Focus areas: invalid inputs (empty fields,
  out-of-range values, wrong types, long strings, special chars, injection
  payloads); boundary conditions (exact edges of valid ranges, where off-by-one
  and overflow are most likely); resource exhaustion (OOM, full disks, pool
  exhaustion, timeouts); concurrency issues (race conditions, deadlocks, data
  corruption); dependency failures (unavailable databases, network timeouts,
  corrupted external responses). Design cases systematically (for each input,
  consider null/empty/boundary/malformed); verify error messages are
  informative without exposing internals (stack traces, schemas, paths);
  ensure errors are logged with timestamps, context, correlation IDs;
  confirm data integrity is maintained (partial operations rolled back or
  atomic); validate error paths don't introduce vulnerabilities (eg. failing
  open on authentication errors).

- **Exploratory testing: simultaneously learn, design tests, and execute them
  without predetermined scripts.**

  Leverages human intuition and curiosity to discover issues scripted tests
  miss — effective for evaluating unfamiliar features, discovering
  unanticipated edge cases and interaction effects, and supplementing automated
  regression tests. Not ad hoc or random: most effective in structured sessions
  with clear objectives, time limits, and systematic documentation. Allocate
  time-boxed sessions with a defined theme; document findings immediately with
  reproduction steps; encourage deviation from planned paths when noticing
  interesting behavior; use as a complement to (not replacement for) automated
  tests; rotate testers across areas for fresh perspectives.

- **Risk-based testing: allocate test effort in proportion to risk.**

  Risk = likelihood of failure × impact of failure. Likelihood factors: code
  complexity, change frequency, developer experience, historical defect rates.
  Impact factors: users affected, financial impact, regulatory implications,
  safety. High on both → deepest, most rigorous testing; low on both → basic
  validation. Assess risk early and revisit as the system evolves; use risk to
  guide test types, depth, and automation investment (not just prioritization);
  focus edge/boundary/negative testing on high-risk components; accept lighter
  testing for low-risk low-change components but maintain basic path coverage;
  track defect data to validate and refine assessments.

- **Mutation testing: evaluate the quality of the test suite by introducing
  deliberate defects (mutations).**

  If existing tests detect a mutation (at least one fails), the mutant is
  "killed"; if all pass, it "survives" — indicating a gap. The _mutation score_
  is the percentage killed. Common mutations: replacing arithmetic operators,
  inverting conditionals, removing method calls/returns, replacing constants,
  negating booleans. Computationally expensive (each mutation needs a separate
  run) — apply selectively. Focus on critical/complex areas; use after bug fixes
  (reverting the fix should produce surviving mutants); run on integration of
  modified code as a CI gate; investigate survivors (each is a genuine coverage
  gap or an equivalent mutation — both are informative); use language/
  ecosystem-appropriate tools.

- **Chaos testing: proactively test resilience by deliberately introducing
  failures into production or production-like environments.**

  Discover weaknesses in the system's ability to withstand and recover from
  turbulent conditions _before_ they occur naturally. Foundational principle
  (per Netflix): empirical evidence of what _actually_ happens beats
  hypothetical reasoning. Experiments: infrastructure failures (kill VMs,
  containers, simulate DC outages); network disruption (latency, packet loss,
  DNS failures, partitioning); resource pressure (fill disks, exhaust memory,
  saturate CPU); dependency failures (external services error, slow, become
  unavailable); clock manipulation (skew clocks to expose time-dependent bugs).
  Start small in non-production before progressing to production; define a
  _steady state_ (normal healthy behavior) and measure each experiment against
  it; automate experiments to run regularly; establish clear procedures for
  halting unacceptable impact; use results to drive architectural improvements
  (not just incident response); build a culture where controlled failure is a
  learning opportunity.

### Test types

Test types define _what_ quality attribute is being tested and _how_ the
verification is performed. This section covers functional-correctness types;
non-functional types are in [TS-14](../014/AGENTS.md).

- **Static analysis: examine code without executing it.**

  Identifies potential defects, security vulnerabilities, code quality issues,
  and standards-compliance violations from the static structure. Cheap and
  fast (no build or isolated runtime), so easily automated and deeply
  integrated into development. Run on commits, check-ins, and integrations;
  block integrations until all checks pass; establish clear coding conventions
  and configure tools to enforce them consistently; track static-analysis
  metrics over time; use a variety of tools specializing in different concerns
  (conventions, security, dependency analysis).

- **Behavioral (black-box) testing: validate behavior without considering
  internal implementation.**

  Validate expected outputs for given inputs. Ideal for requirements
  verification; also verifies smaller components and integrations. Undertaken at
  multiple levels (unit, integration, system, end-to-end acceptance). Design
  cases from requirements and user stories (for unit/integration, the
  requirements are those of the components-under-test, not the user-oriented
  system requirements); prefer dummy data representing realistic production
  scenarios; aim for high path coverage, but edge cases, boundary values,
  invalid inputs, and error conditions are more important.

- **White-box (internal) testing: examine internal logic paths and data
  flows.**

  Useful for complex algorithms, input validation, and error handling within
  components; most often used for comprehensive path coverage (each logical
  branch executes at least once). Commonly combined with black-box behavioral
  testing, often interwoven in the same suites (especially unit tests) —
  together they provide the highest confidence. Strive for comprehensive
  _critical_ path coverage (prioritize critical paths plus edge/boundary/
  invalid/error — more important than 100%, which is often unattainable); do
  combine white-box and black-box tests for a single component/integration; as
  a general rule white-box tests are not appropriate for higher-level (system,
  acceptance) tests.

- **Approval (snapshot / golden master) testing: validate that output is
  identical across runs for a given input.**

  Two phases: baseline capture (record output as the "approved" snapshot),
  then comparison runs (any difference fails). Particularly valuable for
  stabilizing legacy code with little or no coverage (capture current behavior
  as a safety net while refactoring — any unintended change is flagged
  immediately) and for visual GUI validation (pixel-by-pixel screenshot
  comparison). Limitation: verifies only that the code does what it _did
  before_, not what it _should_ do — a complement to, not a replacement for,
  behavioral and acceptance tests. Use as a first step when stabilizing legacy;
  store approved snapshots in version control alongside test code (changes
  reviewed in normal code review); inspect failures carefully (intentional →
  update the snapshot; unintentional → investigate the regression); for UI,
  accept minor rendering differences (sub-pixel antialiasing, font rendering)
  and configure comparison thresholds; prefer behavioral tests for new
  development.

### Test levels

Test levels define _where_ in the architecture testing occurs — from
components in isolation up through the complete system. Defects can exist within
components, in interactions between them, or in emergent whole-system behavior;
each level addresses a different class. As level increases, so do scope,
real-dependency count, fidelity to production — and cost (slower, harder to set
up, harder to debug, more environmentally sensitive).

- **Unit tests: verify individual components or functions in isolation.**

  A "unit" is the smallest testable part (function, method, class, module —
  depending on language/architecture). Fast and precise (when a unit test fails
  the source is usually obvious). Unit testing is as much a design tool as a QA
  tool — difficult-to-test code is often tightly coupled, overly complex, or
  poorly modularized; testability problems point to design problems.
  Dependencies are commonly replaced with test doubles (use judiciously —
  lightweight doubles preferred, real dependencies wherever practical).
  Best practices: each unit test verifies one specific behavior (prefer many
  small focused tests); fast (hundreds/thousands complete in seconds — slow
  tests won't be run often enough); minimize test doubles (replace only slow,
  non-deterministic, or unavailable dependencies — use real implementations
  wherever practical); name tests descriptively so a failing name alone
  communicates broken behavior; do not depend on external state (databases,
  file systems, network services — if it does, it's probably an integration
  test); organize the body into *given* (preconditions/setup), *when* (action
  under test), *then* (assertions) — encourages a single action per test.

- **Integration tests: verify multiple components work together correctly.**

  Catch boundary defects (mismatched data formats, incorrect call-sequence
  assumptions, transaction-management issues, protocol misunderstandings).
  Multi-layered architectures mean integration tests exist at multiple levels
  (two classes vs an app service and a database differ in scope, speed, setup).
  Two approaches: bottom-up (lowest-level first, higher levels added
  incrementally, lower levels real, higher levels exercised through "drivers")
  and top-down (highest-level first, lower dependencies replaced by stubs,
  real implementations substituted in as lower layers integrate). Most teams
  use a pragmatic combination. Integration tests are more _tactical_ than
  _strategic_ — if a project has comprehensive unit and acceptance/system tests,
  integrations are already exercised indirectly; integration tests are most
  valuable addressing specific known sources of failure (a flaky external
  dependency, a complex data transformation at a service boundary, a history of
  contract-breaking changes). Focus on boundaries and interfaces (data,
  contracts, error handling); use real dependencies wherever practical (closer
  to production = more likely to catch real defects); will be slower than unit
  tests — organize so they run both as part of the full suite and selectively;
  where doubles are necessary (eg. unavailable external services), prefer
  contract-based approaches verifying both sides independently; cover failure
  paths, not just the happy path (downstream timeout, lost DB connection,
  malformed message).

- **System tests: validate the entire application as a complete integrated
  system.**

  Evaluate compliance with functional and non-functional requirements in a
  production-like environment. Operate at the highest level of the application's
  own architecture, exercising the system through its external interfaces (UI,
  API, CLI, message queue); treat the application as a black box. Sometimes
  called end-to-end or feature tests. Slowest and most expensive, most
  environmentally sensitive — but highest fidelity (a passing system test is
  strong evidence a complete workflow works). Design around complete user
  workflows and business scenarios (not individual components/internal
  structures); run in production-mirroring environments (same OS, DB engine,
  network topology); keep the number manageable (use them for critical paths
  and high-risk scenarios, rely on unit/integration for breadth); automate and
  integrate into CI/CD (manual system testing doesn't scale and is
  inconsistent); when they fail, invest in diagnostic output (detailed logs,
  screenshots, request traces — failures are hard to debug due to large scope).

- **Acceptance tests: confirm the system meets business requirements and is
  ready for deployment.**

  Distinct from system tests in perspective and ownership: system tests are
  written by dev/QA against technical specifications; acceptance tests are
  defined in collaboration with stakeholders against business requirements (user
  stories, acceptance criteria, business rules). Two phases: alpha testing
  (at the dev site in a controlled environment, customer reps/product owners
  under close supervision, after system testing) and beta testing (at the
  customer's site or by external users in a real-world environment without
  direct supervision — broader usage patterns, environmental conditions, edge
  cases). Define acceptance criteria collaboratively with stakeholders before
  implementation (specific, measurable, testable); automate where possible
  using stakeholder-comprehensible tools (eg. BDD frameworks); conduct alpha
  with actual customer representatives (not developer/tester proxies); recruit
  a representative beta group with structured feedback collection/triaging;
  establish clear pass/fail criteria before testing begins; focus on _what_ the
  system does, not _how_ — tests should be resilient to internal refactoring.

- **Behavior-driven development (BDD) is the RECOMMENDED approach to writing
  acceptance tests.**

  BDD is about expressing tests in the language of the business domain so they
  function as _executable specifications_ — verifying that the system does what
  stakeholders asked for _and_ documenting what it is supposed to do (always
  up-to-date, verified by every run, reviewable/co-authorable by
  non-technical stakeholders). It is not about a particular tool (Cucumber,
  Behat). Keep tests focused on the _problem_ (desired behavior), not the
  _solution_ (implementation details) — a well-written BDD test should not
  mention button labels, form fields, URLs, or any implementation artifact; the
  same specification should be valid whether the system is a web app, a CLI
  tool, or a mobile app, changing only when the understanding of the _problem_
  changes. Write criteria in domain language collaboratively with
  stakeholders before implementation; do not couple tests to specific UIs or
  implementation details; use BDD as a forcing function for incremental
  development (write the specification, implement just enough to satisfy it,
  repeat); treat executable specifications as the authoritative definition of
  intended behavior — when a specification and the system disagree, the
  specification is right and the system is wrong. Acceptance tests are also the
  easiest to retrofit to legacy code (black-box, public interfaces only — no
  access to internals needed), making them valuable for stabilizing legacy
  before refactoring.

- **The test pyramid is a heuristic, not a prescriptive target; unit and
  acceptance tests are the two most important levels.**

  Traditional form: broad base of unit tests, narrower middle of integration,
  small peak of system/acceptance — most defects caught by fast cheap unit
  tests. But the pyramid's shape is a descriptive outcome of bottom-up
  test-driven design, not a target. Top-down (high-level failing system/
  acceptance tests first, working downward) produces a different distribution
  with fewer unit tests and easier large-scale refactoring. Neither is
  inherently superior; the right balance depends on architecture, methodology,
  and risk profile. What matters is that every level provides meaningful signal
  without excessive redundancy. _Regardless of distribution_, unit tests and
  acceptance tests are the two most important levels and should be central to
  any strategy: unit tests drive component design and catch fine-grained
  defects; acceptance tests validate user-perspective outcomes. When
  development is driven from these two levels (acceptance tests define _what_,
  unit tests drive _how_), the result is a robust, well-specified system.
  Integration and system tests are valuable tactical complements for specific
  risks, not the primary QA mechanism.

### Test coverage

- **Coverage measures how much of the codebase is executed by the test suite;
  interpret carefully.**

  High coverage does not guarantee good tests; low coverage does not
  necessarily indicate poor tests. Granularities:

  - **Statement coverage** — whether each statement has been executed at least
    once. Most basic and commonly reported.
  - **Branch coverage** (condition/decision coverage) — whether each branch of
    every conditional has been evaluated as both true and false. Strictly more
    rigorous than statement coverage (100% statement coverage can miss branches
    entirely).
  - **Path coverage** — whether every possible execution path has been
    traversed. Most thorough but often impractical (paths grow exponentially
    with branches).

- **Coverage is not the exclusive concern of unit tests; achieve it through the
  most appropriate combination of levels.**

  A system test exercising a complete workflow contributes to statement and
  branch coverage just as a unit test would; integration tests contribute at
  boundaries. The coverage tool doesn't distinguish which level exercised a
  line. A project does not need to unit test every function to achieve high
  coverage — if a path is well-covered by integration or system tests, a
  redundant unit test adds maintenance cost without proportional benefit.
  Complex branching logic deep inside a component may be impractical to cover
  through high-level tests and is best covered by targeted unit tests. The
  goal is adequate coverage through the most appropriate combination — not
  maximized coverage at any single level.

- **Treat coverage as a diagnostic tool, not a goal.**

  Rigid targets incentivize the wrong behavior (low-value tests that exercise
  trivial code to satisfy the metric, leaving complex/risky code undertested).
  Use reports to identify untested code, then make a deliberate decision about
  whether it warrants testing (focus on complex logic, error-handling paths,
  high-risk components); measure branch coverage in addition to statement
  coverage (statement alone is misleading); do not pursue 100% as an end in
  itself (the last few percent almost always exceeds the value gained); track
  trends over time (a declining trend in areas of active development is more
  useful than any absolute number); when setting thresholds, apply them
  per-component or per-module (critical modules may warrant higher thresholds
  than utility code).

### Test doubles

A test double is any object that stands in for a real dependency in a test, to
isolate the component-under-test. The lower the test level, the more useful
doubles tend to be (unit tests have more; system tests may have few or none).
Common-agreed definitions (the terms are widely misused — when in doubt prefer
"test double"):

- **fake** — a fully functioning implementation of the interface, developed and
  maintained alongside the real component (not in test code). Takes shortcuts
  (eg. an in-memory store instead of a database) but otherwise replicates
  behavior as closely as possible.
- **stub** — a lightweight fake. Implements the interface but only provides
  canned answers to calls. Makes no assertions; test code doesn't assert on
  its behavior. The lightest, "dumbest" double — just fills the interface and
  provides the data the test needs.
- **mock** — pre-programmed with expectations about the calls it will receive.
  Throws an error (failing the test) if expectations aren't met. Replicates
  less internal logic than a fake.
- **spy** — a lightweight mock. Records its calls for the test to assert
  against, but makes no assertions itself (eg. recording how many messages were
  sent to an email service).
- **dummy** — any test object or value used but never inspected. Commonly used
  to stand in for function parameters; usually primitive values or plain
  objects, at most very lightweight fakes. ("Dummy data" also refers to any
  data injected in place of production data in non-production environments.)

  Variations include partial mocks (backed by a real object, mocking some
  methods), capture-replay mocks (record real interactions for playback),
  approval/snapshot mocks (capture actual responses as approved snapshots),
  auto-generated contract stubs, and self-initializing fakes. In practice many
  doubles combine characteristics of multiple types.

- **Err toward high-fidelity tests with minimal mocking; replace real
  dependencies with doubles only to overcome specific problems.**

  _Fidelity_ = how closely the system-under-test matches its production
  behavior. High fidelity is the goal: as few dependencies as possible mocked;
  real dependencies (including vendor components installed via a package
  manager) preferred over doubles; when doubles are needed, lightweight ones
  (which replicate little of the real logic) preferred. Replace a real
  dependency with a double only to overcome a specific problem — the real
  implementation is slow, unreliable, non-deterministic, or difficult to
  instantiate (eg. requires a network connection). The biggest issue with
  overusing doubles is _brittleness_ — brittle tests fail not for real
  production problems but because the test itself is fragile. Double
  implementations can diverge from the real ones over time; tests continue to
  pass but no longer test real behavior, and confidence drops. Fakes are more
  prone to drift than mocks; stubs and spies tend to be more stable. Putting
  too much implementation detail into tests is the usual culprit.

- **Use fakes sparingly; maintain them alongside real implementations; give
  fakes their own tests.**

  Fakes should be used sparingly. Where required (eg. to swap a database
  abstraction for an in-memory store), maintain them alongside the real
  implementations — this increases the chances of keeping fakes up-to-date and
  keeps test code cleaner (less boilerplate). Fakes are, to all intents and
  purposes, _real_ implementations optimized for non-production environments;
  they belong with the application code, not the test code, and should have
  their own tests. Ideally only components communicating with external systems
  (file systems, databases, remote services) — anything unavailable or
  unreliable in test environments — will be swapped for fakes. Do not make
  tests as fast and lightweight as possible by using lots of doubles — that is
  an anti-pattern giving a false sense of dependability. If test-suite
  performance becomes an issue, adjust test setup (eg. greater parallelization)
  before lowering fidelity.

### Test-driven development

- **TDD is the RECOMMENDED approach to writing software.**

  Write tests first, then the code that makes them pass, in the short
  repeating *red-green-refactor* cycle: _red_ (write a small test for the next
  desired behavior; run it; it fails because the behavior doesn't exist),
  _green_ (write the simplest code that makes the test pass — nothing more),
  _refactor_ (improve the structure of code and test while keeping all tests
  passing). Each iteration adds one small increment of behavior and design.

- **TDD is test-driven _design_: writing the test first shifts left the
  experience of being a consumer of your own code.**

  You write a client for the component you're about to build, thinking about
  the interface and how it will be used before committing to an implementation.
  Code that is test-driven tends to be more modular, more maintainable, and
  easier to change; non-TDD approaches often produce more tactical, complex
  tests tightly coupled to the implementation. TDD is most commonly used
  bottom-up (component by component) but can be effective top-down too; it can
  be desirable at all test levels (unit, integration, system).

- **Developers SHOULD default to writing tests before code, while recognizing
  this as a guideline, not dogma.**

  The real objective is _self-testing code_ (Martin Fowler): a codebase you
  can confidently verify with a single command. TDD is the recommended means;
  the end matters more than the means. TDD has trade-offs: its tight cycle of
  small increments can sometimes work against design — with many tests in
  place, large-scale refactoring becomes harder (every structural change
  requires updating code and tests). Most valuable when the design direction
  is reasonably clear; during early exploration or prototyping with the design
  still in flux, it can be more practical to experiment first and write tests
  once the design stabilizes.

### Test design

- **Well-designed tests follow the FIRST principles.**

  - **Fast** — run quickly. A slow suite is run less frequently, reducing its
    value as feedback. Unit tests in particular should run in milliseconds.
    Slow tests usually signal unnecessary I/O, real network calls, or excessive
    setup — replace with doubles or eliminate through better design.
  - **Independent** — each test independent of all others. No reliance on
    shared mutable state or specific execution order. A test that passes only
    after another, or fails in isolation, indicates hidden coupling.
    Independence enables running any subset in any order, parallelizing, and
    diagnosing failures in isolation.
  - **Repeatable** — same result every time, in any environment. Tests that
    pass on one machine and fail on another, or fail intermittently due to
    timing, randomness, or external dependencies, undermine confidence.
    Eliminate non-determinism by controlling time, seeding randomness, and
    replacing external dependencies with doubles.
  - **Self-validating** — clear, automated pass/fail outcome. Should not
    require a developer to manually inspect output, logs, or a database. The
    assertion is the declaration of expected behavior; no human interpretation
    necessary.
  - **Timely** — written at the same time as or before the code they verify.
    Tests written long after the fact are harder to write well (the code may
    not have been designed with testability in mind). Writing tests early (or
    first, as in TDD) keeps code testable and ensures tests reflect intended
    behavior.

- **Tests are specifications; make them readable.**

  Give tests descriptive names that read as a statement of expected behavior
  (`calculatesTaxAtStandardRateForDomesticOrders`, not `testCalc`) — the name
  should make intent clear without reading the body. Structure each test
  consistently around the **arrange–act–assert (AAA)** pattern: set up
  preconditions, invoke the behavior under test, assert the expected outcome.
  Keep each phase visually distinct (blank lines or comments if the body is
  more than a few lines). Avoid logic in tests — conditionals, loops, and
  helper computations make tests harder to read and risk bugs in the test code
  itself. If a test requires complex setup, extract it into a clearly named
  fixture or factory rather than embedding it inline.

- **Aim for one logical assertion per test (a guideline, not a mechanical
  rule).**

  A test asserting many things is hard to read, and when it fails it isn't
  clear which assertion failed or which behavior broke. "One logical assertion"
  doesn't mean exactly one `assert` call — a single logical assertion may
  require several related checks — but each test should verify one distinct
  aspect of behavior. Where a single behavior genuinely produces multiple
  observable outcomes, asserting all in one test is acceptable. The spirit is
  focus and clarity, not line-count adherence.

## References

- [TS-13 source](README.adoc)
- [TS-12: Quality Assurance](../012/AGENTS.md)
- [TS-14: Performance Testing](../014/AGENTS.md)
