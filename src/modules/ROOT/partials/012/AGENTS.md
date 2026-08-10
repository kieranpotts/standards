# TS-12: Quality Assurance

This is a compact version of technical standard TS-12 for AI agents.

Use this when designing or reviewing the _process_ of quality assurance —
quality culture, the Definition of Done, code review, quality gates, testing
environments, and quality metrics. QA is a continuous discipline woven into
every stage of the lifecycle, not a phase or a separate team's responsibility.

Do NOT use this for the specifics of testing — see
[TS-13: Functional Testing](../013/AGENTS.md) and
[TS-14: Performance Testing](../014/AGENTS.md). For release strategies (canary,
staged rollouts) which are also quality-control practices, see
[TS-10: Releasing](../010/AGENTS.md). For requirements clarity (the single
largest source of defects), see
[TS-1: Software Requirements Specification](../001/AGENTS.md).

## Rules

### Quality culture

- **Quality is built in, not inspected in.**

  Testing and review are verification activities — they confirm the presence
  or absence of quality that was (or was not) established during design and
  implementation. The earlier a defect is introduced and the later it is
  detected, the more expensive it is to fix; prevention is always cheaper than
  detection. Quality practices MUST be integrated into the daily work of every
  team member, not deferred to a separate phase or delegated to a separate
  team. Writing tests is part of implementation; reviewing code _is_
  productive work; monitoring production is a development concern.

- **Quality is a shared responsibility, not the job of a "QA team".**

  When a dedicated QA team exists, developers tend to write code quickly and
  leave defect detection to the testers — producing more defects, longer
  feedback cycles, and adversarial dev/QA relationships. The RECOMMENDED
  model embeds testing, review, and quality verification in the development
  team's workflow: every developer writes tests, reviews code, and monitors
  the systems they build. Dedicated quality engineers MAY still exist, but
  their role is to coach and improve the quality process, not to be the sole
  gatekeepers of quality.

- **Prefer prevention over detection.**

  Prevention practices include: clear testable requirements (see
  [TS-1](../001/AGENTS.md) — ambiguous requirements are the single largest
  source of defects); design review before implementation (catches problems
  orders of magnitude cheaper than in code); test-driven development (forces
  thinking through requirements, edge cases, and interface design before
  production code — see [TS-13](../013/AGENTS.md)); pair/mob programming
  (catches defects at the moment of introduction, when context is fresh and
  the fix is trivial); and coding standards plus automated static analysis on
  every change (prevents whole classes of defect from entering the codebase).

- **Practice continuous improvement; treat incidents as learning.**

  Teams SHOULD regularly reflect on quality practices and identify
  improvements. Conduct blameless post-mortems focused on process
  improvements, not individual fault. Track where defects are introduced and
  where detected — a growing gap signals a process problem. Invest in
  developer education (testing techniques, security, code quality —
  compounding dividends). Celebrate quality improvements, not just feature
  delivery.

### Definition of Done

- **Every team MUST have a Definition of Done (DoD): a shared, explicit,
  non-negotiable checklist satisfied before any work item is considered
  complete.**

  The DoD is a contract between the team and its stakeholders defining what
  "done" means so the word is never ambiguous. Without it, "done" becomes
  subjective and quality erodes. The DoD is more important than a Definition
  of Ready (DoR): DoR describes when work _may begin_; DoD describes when work
  _has ended_. The DoD is also more stable — it tends to remain consistent
  across work items while the DoR varies.

- **Define the DoD collaboratively; every item MUST be objectively
  verifiable.**

  Developers, testers, product owners, and operations define it together; a
  reviewer should be able to determine without ambiguity whether each
  criterion is met. Typical criteria: code compiles and passes existing
  tests; new code has corresponding automated tests (unit/integration/
  acceptance as appropriate); CI/CD pipeline passes; static analysis passes
  with no new warnings/violations; peer reviewed by at least one team member;
  documentation updated for user-facing changes; deployed to staging/
  pre-production and verified; new config/env vars documented; security
  reviewed (input validation, access control, data handling). Each item
  SHOULD exist because its absence has, in the past, led to problems — if a
  criterion consistently adds no value, remove it; if new defect categories
  emerge, add a criterion.

- **The DoD SHOULD evolve as the team matures; apply it consistently.**

  A new team may start minimal (compiles, tests pass, reviewed) and expand
  over time. Imposing a comprehensive DoD on a team lacking the infrastructure
  or discipline to support it is counterproductive. Display the DoD
  prominently (wiki, contributing guidelines); review it periodically at
  retrospectives. Apply it consistently — do NOT make exceptions for "small
  changes" or "urgent fixes"; inconsistent application erodes trust in the DoD
  itself. When a defect reaches production, check whether the DoD would have
  prevented it; if not, consider adding a criterion that would.

### Code review

- **All code changes, including test code, MUST be peer reviewed by at least
  one other team member before integration.**

  For critical systems or significant changes, review by two or more
  reviewers is RECOMMENDED. Code review creates shared ownership, knowledge
  transfer, and collective standards — not merely bug-finding.

- **Automated tooling handles syntax/formatting; human review focuses on what
  machines cannot evaluate.**

  Review for: correctness (does it do what it should, edge cases, error
  conditions); design (well-structured, follows architecture and patterns,
  modular and cohesive); clarity (readable, understandable by someone
  unfamiliar with the area); test coverage (accompanied by appropriate tests
  that verify meaningful behavior, not just exercise paths); security (input
  validation, access controls, sensitive-data handling); and completeness
  (full scope including docs, config, migration scripts).

- **Authors: keep changes small and focused; provide context; respond
  constructively.**

  Large sprawling changes are difficult to review thoroughly and reviewers
  miss issues — aim for changes addressing a single concern. Provide context
  in the change description (problem, approach, why); reviewers should not
  have to reverse-engineer intent. Treat review comments as contributions to
  shared quality, not personal criticisms.

- **Reviewers: review promptly (within one working day); be specific and
  constructive; distinguish blocking issues from suggestions; don't bikeshed;
  approve when good enough, not perfect.**

  Delayed reviews block integration, slow delivery, and force context
  switching. "This is wrong" is unhelpful; "This does not handle null input —
  consider adding a guard clause" is actionable. Clearly label comment
  severity. Focus on correctness, design, and security rather than stylistic
  preferences handled by formatters. Every change is an increment, not a
  final draft.

- **Pair programming is continuous, synchronous code review.**

  Two developers work together (driver writes, navigator reviews in real
  time). Particularly effective for complex or high-risk changes, onboarding,
  and problems where the solution is unclear — catches defects at introduction
  when correction cost is lowest. Pair programming and asynchronous review are
  not mutually exclusive; pair-programmed code MAY still benefit from a
  lighter async review, especially from someone outside the pair.

### Quality gates

- **Quality gates MUST be automated wherever possible.**

  A quality gate is a checkpoint where specific quality criteria must be met
  before work proceeds. Manual gates are slow, inconsistent, and easily
  bypassed under deadline pressure; automated gates are fast, consistent, and
  impartial. Gates turn aspirational standards into mandatory requirements.

- **Position gates at multiple pipeline stages with progressively broader
  scope and higher cost.**

  - **Pre-commit** (developer's machine): fastest loop — formatting, linting,
    local unit tests, static analysis for common errors. Must be fast (a few
    seconds) or developers will disable/work around them.
  - **Check-in** (on push to shared repo, in CI): full unit suite, full-rule
    static analysis, build verification, dependency vulnerability scanning,
    coverage regression analysis. MUST block integration if any check fails;
    a broken build is a team-level priority that takes precedence over new
    work.
  - **Integration** (on merge to a trunk/release branch): full test suite
    (unit, integration, system), performance regression checks, security
    scanning (SAST/DAST/dependency), accessibility for UI changes, compliance
    for regulated systems.
  - **Pre-deployment** (after build, before deploy): smoke tests against the
    artifact, target-environment config validation, database migration
    verification, production-deployment approval workflows where policy
    requires.

- **Embed gates in CI/CD; no escape hatches; treat the pipeline as production
  infrastructure.**

  Every change triggers the appropriate checks automatically; failed checks
  block progression with no exceptions; results are visible to the whole team
  (not just the author); testing/staging deployments are fully automated;
  production deployments MAY include manual approval, but the deployment
  process itself MUST be automated (manual deployment is error-prone and
  unreproducible). Run cheapest, fastest checks first. Keep gate criteria
  explicit and version-controlled alongside the code (auditable, reviewable).
  Monitor gate execution times — slow pipelines reduce productivity and create
  bypass pressure; invest in parallelization, caching, and infrastructure.
  Do NOT create escape hatches — once bypasses exist, they will be used and
  the gates become meaningless. Treat the CI/CD pipeline itself as production
  infrastructure: monitor, maintain, and test it with the same rigor as the
  application.

### Testing environments

- **Testing environments are first-class infrastructure; the key principle is
  environmental fidelity.**

  Tests can only be as reliable as the environments in which they run. The
  closer a testing environment is to production, the more reliable its
  results — environmental differences are a primary source of "works on my
  machine" failures and false confidence from passing suites. Most
  organizations maintain a hierarchy:

  - **Local development** — developer workstations; fast feedback loop;
    mocked/simplified external dependencies.
  - **Integration** — shared; combines multiple developers' changes; runs the
    full stack; target of CI/CD deployments.
  - **Staging** — pre-production mirroring production config as closely as
    possible; final verification before release. Differences from production
    (infrastructure, data, config, scale) undermine the value of staging
    tests.
  - **Production** — the live environment; also a testing environment (see
    below).

- **Automate provisioning; keep staging close to production; isolate
  environments; manage test data deliberately.**

  Environments SHOULD be reproducible from configuration and scripts via
  infrastructure-as-code, not manually assembled. Staging SHOULD match
  production (same OS, database engines, network topology, config
  management); document any known differences. Provide developers the ability
  to run meaningful tests locally — if local testing requires extensive
  manual setup or unavailable external dependencies, developers will skip or
  under-test. Isolate test environments from one another and from production
  (tests in one should not affect another's state or behavior). Manage test
  data deliberately: environments need realistic data, but test data MUST NOT
  include real user data unless properly anonymized.

- **Demo environments MUST have sufficient representative data to demonstrate
  all application capabilities.**

  Enables effective demonstration by non-technical teams (sales, customer
  success) without developer involvement or manual setup before each demo.
  Refresh demo environments regularly to keep data current and reflect the
  latest software version.

- **Production testing is necessary, not reckless; design it to minimize risk
  to real users while maximizing signal.**

  No staging environment can fully replicate real-world conditions (live
  user behavior, fluctuating traffic, real data volumes, unpredictable
  third-party interactions). Modern architectures support incremental rollouts,
  real-time monitoring, feature flags, and rapid rollbacks, making production
  testing routine. Methods:

  - **Smoke tests** — automated checks immediately after deployment, before
    the release reaches users; verify deployment success and critical
    functionality (from simple health checks to substantive end-to-end
    workflows).
  - **Synthetic transactions** — automated scripts simulating real user
    interactions without actual users; continuously execute predefined
    workflows (place an order, authenticate, query a report) for ongoing
    verification.
  - **Parallel runs** — two implementations of the same functionality process
    the same requests, only one produces the user-visible response; results
    compared to detect discrepancies. Particularly valuable during
    migrations or legacy replacement.

  Best practices: maintain dedicated test accounts and synthetic users,
  clearly separated from real users; test transactions MUST NOT affect real
  users or real data; ensure test transactions are identifiable and excludable
  from business metrics/analytics; monitor production continuously (logs,
  metrics, distributed traces) — production testing is only valuable when
  results are observable; always have a tested, automated rollback strategy.
  For release strategies (canary, A/B, staged rollouts) see
  [TS-10](../010/AGENTS.md); for chaos engineering and resilience testing see
  [TS-13](../013/AGENTS.md).

### Quality metrics

- **Measure outcomes, not outputs; choose metrics carefully.**

  Poorly chosen metrics create perverse incentives — measured on test count
  alone, teams write trivial tests; measured on defect count, they argue
  about what counts. The best metrics measure _outcomes_ (software quality)
  rather than _outputs_ (volume of quality activities).

- **Defect metrics: defect escape rate, defect density, MTTD, MTTR.**

  - **Defect escape rate** — defects found in production relative to total
    defects found. A rising rate signals gates aren't catching problems
    before release. One of the most important quality metrics.
  - **Defect density** — defects per unit of code (per thousand lines or per
    module). Identifies which parts of the codebase are most problematic and
    may need refactoring or more thorough testing.
  - **Mean time to detect (MTTD)** — how long a defect exists before
    discovery. Long MTTD for production defects suggests gaps in
    monitoring/alerting; long MTTD for pre-production defects suggests gaps
    in testing.
  - **Mean time to resolve (MTTR)** — how long it takes to fix a defect once
    discovered. Reflects codebase complexity and the effectiveness of the
    debugging and deployment process.

- **Test metrics: coverage (with caveats), flaky test rate, build success
  rate.**

  - **Test coverage** — percentage of code exercised by automated tests.
    Useful indicator of untested areas but a poor measure of test quality —
    high coverage with weak assertions provides false confidence (see
    [TS-13](../013/AGENTS.md)).
  - **Test pass rate / flaky test rate** — consistently high pass rate is
    expected; the more informative metric is the flaky test rate (proportion
    intermittently passing and failing without code changes). Flaky tests
    erode trust in the suite and SHOULD be fixed or removed promptly.
  - **Build success rate** — percentage of CI builds passing all gates. A
    low rate indicates either gates are too strict (unlikely, but possible) or
    that check-in code quality is poor.

- **Process metrics: lead time for changes, defect-resolution cycle time,
  review turnaround time.**

  - **Lead time for changes** — commit to production deployment. Gates too
    slow or numerous increase lead time without proportional quality gains.
  - **Cycle time for defect resolution** — defect report to deployed fix.
    Reflects the team's ability to respond to quality issues.
  - **Review turnaround time** — review requested to review completed. Slow
    reviews block delivery and signal a process bottleneck.

- **Use metrics for learning and improvement, not judgment or blame.**

  Track metrics over time to identify trends (a single month's defect count
  is noise; a six-month upward trend is a signal). Make metrics visible to
  the team (dashboards, retrospectives, planning) — metrics seen only by
  management are disconnected from those who can act. Use metrics to ask
  questions, not draw conclusions (a rising escape rate prompts "why are more
  defects reaching production?" — the metric doesn't answer it; investigation
  does). Be cautious about tying metrics to individual performance
  evaluations — when metrics become targets, they cease to be good metrics
  (developers penalized for low coverage will write meaningless tests to
  inflate the number). Review the metrics themselves periodically — if a
  metric isn't driving useful conversations or actions, stop measuring it
  and replace it.

## References

- [TS-12 source](../../pages/012-quality-assurance.adoc)
- [TS-1: Software Requirements Specification](../001/AGENTS.md)
- [TS-10: Releasing](../010/AGENTS.md)
- [TS-13: Functional Testing](../013/AGENTS.md)
- [TS-14: Performance Testing](../014/AGENTS.md)
