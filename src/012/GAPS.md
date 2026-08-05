# TS-12 gap analysis

Gaps found comparing TS-12: Quality Assurance against the following reference
resources (the standard's `__TODO__/` draft-material directory):

- `src/012/__TODO__/qa/manual.md`
- `src/012/__TODO__/qa/automated.md`
- `src/012/__TODO__/quality-metrics/backlog.md`
- `src/012/__TODO__/quality-metrics/incidents.md`
- `src/012/__TODO__/quality-metrics/index.md`
- `src/012/__TODO__/quality-metrics/security/index.md`
- `src/012/__TODO__/testing/TODO.md`
- `src/012/__TODO__/testing/0100-static/index.md`
- `src/012/__TODO__/testing/0100-static/0100-type-checking.md/index.md`
- `src/012/__TODO__/testing/0200-runtime/0100-automation.md`
- `src/012/__TODO__/testing/0200-runtime/0200-levels/index.md`
- `src/012/__TODO__/testing/0200-runtime/0200-levels/0100-acceptance/index.md`
- `src/012/__TODO__/testing/0200-runtime/0200-levels/0200-unit/index.md`
- `src/012/__TODO__/testing/0200-runtime/0200-levels/0200-unit/0100-scope.md`
- `src/012/__TODO__/testing/0200-runtime/0200-levels/0200-unit/0150-coverage.md`
- `src/012/__TODO__/testing/0200-runtime/0200-levels/0200-unit/0200-style.md`
- `src/012/__TODO__/testing/0200-runtime/0200-levels/0300-integration/index.md`
- `src/012/__TODO__/testing/0200-runtime/0300-style/index.md`
- `src/012/__TODO__/testing/0200-runtime/0300-style/0200-bdd/index.md`
- `src/012/__TODO__/testing/0200-runtime/0300-style/0200-bdd/0900-unit.md`
- `src/012/__TODO__/testing/0200-runtime/0400-coverage/index.md`
- `src/012/__TODO__/testing/0200-runtime/0500-strategies/0100-mutation.md`
- `src/012/__TODO__/testing/0200-runtime/0500-strategies/0200-exploratory.md`
- `src/012/__TODO__/testing/0200-runtime/0500-strategies/1000-loading.md`
- `src/012/__TODO__/testing/0200-runtime/0500-strategies/1100-smoke.md`
- `src/012/__TODO__/testing/0200-runtime/0500-strategies/index.md`

**Assessment.** The `__TODO__/` tree is dominated by testing-specific draft
material (test levels, BDD, coverage methodologies, mutation/exploratory/load
testing, TDD, mocking, UAT) that TS-12 explicitly defers to TS-13/TS-14 and is
therefore out of scope. The process-level content that does fall inside TS-12's
stated scope — defect management, technical-debt tracking, QA roles, the
manual/automated testing balance, and feedback-loop sizing — is almost entirely
missing from the published standard, which currently covers defect *metrics*
but not defect *handling*, and quality *measurement* but not technical-debt
*management*.

**Status:** First run (2026-08-05). No prior `GAPS.md` existed. All gaps below
are open.

## Missing

- [ ] `__TODO__/qa/manual.md:3-9` — a comprehensive test strategy REQUIRES a
      balance of automated and manual testing; manual testing shortens the
      feedback loop and lets the team ask questions not covered by automated
      tests (exploratory testing). The standard's production-testing section
      (`05-testing-environments.adoc:75-130`) lists only automated methods
      (smoke, synthetic, parallel runs) and defers exploratory/chaos testing
      to TS-13 without stating the strategic principle that manual and
      automated testing are complementary. Recommend a new subsection in
      `05-testing-environments.adoc` (or a new "Test strategy" section)
      articulating the manual/automated balance as a process-level decision.
      (Detailed manual testing *techniques* remain TS-13 scope; only the
      strategic balance is in scope here.)

- [ ] `__TODO__/quality-metrics/backlog.md:3-80` — technical debt as a tracked,
      managed quality concern: definitions, Ward Cunningham's original
      refactoring metaphor, the distinction between deliberate technical debt
      and shortcuts, the need to log and monitor debt, Martin Fowler's
      tech-debt quadrant for prioritization, and scenarios that warrant extra
      attention to the debt backlog. The standard mentions technical debt only
      in passing (`02-definition-of-done.adoc:10-12`) and measures defect
      metrics (`06-quality-metrics.adoc:17-37`) but never treats technical-debt
      management as a quality practice. Recommend a new "Technical debt"
      subsection in `06-quality-metrics.adoc`.

- [ ] `__TODO__/testing/TODO.md:311-321` — defect *management* workflow:
      in-sprint defects may be fixed immediately without a ticket; defects not
      fixed immediately MUST have a bug ticket raised with a detailed
      description and added to the sprint or product backlog; defects are
      prioritized when raised or during backlog refinement; outstanding defects
      are considered alongside user stories in sprint planning. The standard
      covers defect *metrics* (`06-quality-metrics.adoc:17-37`) but not the
      process for handling, ticketing, and prioritizing defects. Recommend a
      new "Defect management" section (new file, or a subsection of
      `06-quality-metrics.adoc`).

- [ ] `__TODO__/testing/TODO.md:337-343` — test-suite technical debt backlog:
      improving tests and the test framework, reactivating disabled tests,
      improving maintainability and reliability; the test lead maintains the
      test-tech-debt backlog, encourages the team to raise debt issues, and
      provides visibility of the impact of not addressing them. The standard
      does not address debt specific to the test suite and tooling. Recommend a
      new subsection in `06-quality-metrics.adoc` (alongside the general
      technical-debt gap above).

- [ ] `__TODO__/testing/TODO.md:366-369` — the "three amigos" session: a short
      pre-development collaboration between developer, business analyst, and
      tester to review the user story and its acceptance criteria and decide
      what testing is required. The standard lists "design review before
      implementation" as a prevention practice (`01-quality-culture.adoc:54-56`)
      but does not describe this concrete pre-implementation collaboration
      ceremony. Recommend adding to `01-quality-culture.adoc:43-69`
      (Prevention over detection). Note: this sits at the boundary with TS-1
      (acceptance criteria) and TS-13 (test planning); the user may prefer to
      locate it there.

## Partial

- [ ] `__TODO__/testing/TODO.md:323-335` — QA roles and responsibilities
      (whole team, developers, test lead, technical lead, business analyst,
      product owner) are enumerated with specific QA duties for each. The
      standard's "Shared ownership" section
      (`01-quality-culture.adoc:23-41`) covers the principle that quality is
      everyone's responsibility and that dedicated quality engineers coach
      rather than gatekeep, but does not enumerate role-specific QA
      responsibilities (e.g. the test lead owning the automation framework and
      defect-management flow; the technical lead managing technical debt; the
      product owner prioritizing defects alongside stories). Recommend
      expanding `01-quality-culture.adoc:23-41`.

- [ ] `__TODO__/testing/TODO.md:54,92-94` — feedback-loop sizing: small
      feedback loops allow quick, easy correction but miss broader issues;
      large feedback loops catch broader issues; both are needed. The
      standard emphasizes fast feedback loops at quality gates
      (`04-quality-gates.adoc:20-31,94-103`) and the value of prevention
      (`01-quality-culture.adoc:43-69`) but does not articulate the
      complementary trade-off between fast/precise and slow/broad feedback
      loops. Recommend a sentence or two in `01-quality-culture.adoc:43-69`
      or `04-quality-gates.adoc:79-110`.

## Out-of-scope

- [ ] `__TODO__/testing/TODO.md` (TDD, mocking, test coverage, naming tests,
      test best practices sections) and `__TODO__/testing/0200-runtime/0200-levels/`,
      `0300-style/`, `0400-coverage/`, `0500-strategies/` — detailed testing
      methodology (test-driven development practice, mocking strategy, code
      coverage methodologies and target levels, test levels and the test
      pyramid, BDD style, mutation/exploratory/load/smoke testing, naming
      tests). TS-12's README (`README.adoc:25-31`) explicitly defers "the
      specifics of testing" to TS-13 and TS-14, so this material plausibly
      belongs there rather than in TS-12. Flagged for the user to confirm.

- [ ] `__TODO__/testing/0100-static/` (static testing, static type checking) —
      static analysis as a testing technique. TS-12 references static analysis
      only as a *prevention/gate* mechanism (`01-quality-culture.adoc:67-69`,
      `04-quality-gates.adoc:26-28,43`); the technique itself is TS-13 territory.
      Flagged for the user to confirm.

- [ ] `__TODO__/testing/TODO.md` (UAT, end-user testing, compatibility testing,
      security testing, performance testing, accessibility testing, test data
      framework sections) — these are specific testing types/techniques
      explicitly deferred to TS-13/TS-14 by `README.adoc:25-31`. Flagged for
      the user to confirm.

- [ ] `__TODO__/testing/0200-runtime/0100-automation.md` — the benefits of
      automated runtime testing and policy on automated test coverage. This is
      testing-strategy content that sits with TS-13; TS-12 covers automation
      only at the level of *gates* (`04-quality-gates.adoc`). Flagged for the
      user to confirm.

- [ ] `__TODO__/quality-metrics/incidents.md`, `__TODO__/quality-metrics/security/index.md`,
      `__TODO__/qa/automated.md`, `__TODO__/quality-metrics/index.md`,
      `__TODO__/testing/0200-runtime/0500-strategies/index.md`,
      `__TODO__/testing/0200-runtime/0300-style/index.md`,
      `__TODO__/testing/0200-runtime/0200-levels/0200-unit/0150-coverage.md` —
      these files are title-only stubs or contain only commented-out draft
      notes, so they contributed no extractable claims. No gap can be derived
      from them. Flagged for the user to confirm whether the stubs represent
      intended future coverage that should be tracked separately.

## Unresolved

- [ ] `__TODO__/testing/0200-runtime/0200-levels/test-pyramid.drawio` and
      `test-pyramid.png` are binary files and were skipped silently per the
      gap-analysis procedure; no claims were extracted from them. The
      accompanying `index.md` describes the test-pyramid concept, which is
      classified out-of-scope above.