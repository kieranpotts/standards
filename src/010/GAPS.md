# TS-10 gap analysis

Gaps found comparing TS-10: *Releasing* against the following reference
resources:

- https://12factor.net/build-release-run (Factor V: Build, Release, Run)
- https://12factor.net/admin-processes (Factor XII: Admin Processes)
- ("The Twelve-Factor App", Adam Wiggins, 2017)

**Assessment.** TS-10 assumes the existence of discrete, versioned release
artifacts throughout (`04-rollback.adoc`, `06-release-documentation.adoc`,
`03-release-approval-and-governance.adoc`) but never names or defines the
build/release/run stage model that produces them, nor states the immutability
constraint that makes rollback-by-redeployment a sound strategy in the first
place. This is the standard's largest single gap against the reference: the
three-stage separation is foundational to everything else TS-10 says about
releasing, yet is never made explicit. Admin Processes (Factor XII) is entirely
absent — TS-10 has no guidance on one-off administrative or maintenance tasks at
all, though it borders TS-49 (Cloud Platform Engineering) and TS-45 (Data
Migrations), which the user may prefer as the primary home for parts of it.

**Status:** First run, 2026-08-05. All gaps open.

**Second run, 2026-08-06.** Re-run against the UK Government Design
Principles (https://www.gov.uk/guidance/government-design-principles). Of
its 11 principles, only #5 ("Iterate. Then iterate again") was routed to
TS-10. It is out-of-scope: the repository's `src/README.adoc` explicitly
excludes "iterative and incremental development driven by feedback loops,"
and TS-10 is scoped to production-release mechanics (`README.adoc:13-14`
excludes pre-production). Recorded as out-of-scope, flagged for the user.
No in-scope gaps added; all prior gaps remain open.

**Third run, 2026-08-06.** Re-run against Jeff Hodges' "Notes on
Distributed Systems for Young Bloods"
(https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/).
One point was routed to TS-10: P12 ("Feature flags are how infrastructure
is rolled out"). Partial — TS-10 covers flags and gradual rollout but not
the infrastructure-migration framing (staged parallel-write / shadow-read /
comparison-check sequence, multi-version infrastructure as norm, per-user
migration). One new Partial gap added; all prior gaps remain open.

**Fourth run, 2026-08-06.** Re-run against tef's "Write code that is easy to
delete, not easy to extend" (https://programmingisterrible.com/post/139222674273/write-code-that-is-easy-to-delete-not-easy-to),
Step 7. One point was routed to TS-10: feature flags as release/branch
decoupling and runtime control. Partial — TS-10 covers deployment/release
decoupling and a trunk-based bullet, but not the Chrome long-lived-branch
rationale or the SRE runtime-operability angle. One new Partial gap added;
all prior gaps remain open.

## Missing

- [ ] https://12factor.net/build-release-run ("strict separation between the
      build, release, and run stages... Build stage: fetches vendors
      dependencies and compiles binaries and assets. Release stage: takes the
      build [...] and combines it with the deploy's current config. Run stage
      [...] runs the app in the execution environment") is not addressed
      anywhere in TS-10. The standard discusses release *strategies* (how a
      release reaches users) and release *artifacts* (`03-release-approval-and-
      governance.adoc:68`, `06-release-documentation.adoc:3-40`), but never
      defines the build/release/run pipeline that produces an artifact in the
      first place. Recommend a new introductory section (eg.
      `00-build-release-run.adoc`, included before `01-release-cadence.adoc`),
      since this is conceptually prior to cadence and strategy.

- [ ] https://12factor.net/build-release-run ("Every release should always
      have a unique release ID... Releases are an append-only ledger and a
      release cannot be mutated once it is created. Any change must create a
      new release") is not addressed. This is the principle that underwrites
      `04-rollback.adoc`'s entire premise — "redeploy the previous version's
      artifacts" only works if releases are immutable and individually
      addressable — but TS-10 never states it. Recommend stating this
      explicitly in the new build/release/run section proposed above, with a
      forward reference from `04-rollback.adoc:7-9`.

- [ ] https://12factor.net/admin-processes ("One-off admin processes should be
      run in an identical environment as the regular long-running processes of
      the app. They run against a release, using the same codebase and config
      as any process run against that release. Admin code must ship with
      application code to avoid synchronization issues") is not addressed
      anywhere in TS-10. The standard has no guidance on database migrations,
      one-off scripts, or other administrative tasks run against a release.
      Recommend a new section (eg. `08-admin-processes.adoc`), or explicitly
      deferring to TS-45 (Data Migrations) and TS-49 (Cloud Platform
      Engineering) if the user decides this belongs there instead. Flagged as a
      three-way boundary call between TS-10, TS-45, and TS-49 — see
      `../049/GAPS.md` for the corresponding item raised there.

## Partial

- [ ] https://12factor.net/build-release-run ("the build stage [...] can be
      fairly complex, since there are error conditions that can be checked at
      build time [...] the run stage [...] should be kept to as few moving
      parts as possible") overlaps with the risk-minimization framing running
      throughout TS-10 (eg. `05-change-freezes.adoc`,
      `03-release-approval-and-governance.adoc`), but the standard never
      states this specific principle — that build-time complexity is
      preferable to run-time complexity because build errors are caught during
      a supervised process while run-time errors occur unattended. Recommend
      folding into the new build/release/run section proposed above.

- [ ] https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/
      ("Feature flags are how infrastructure is rolled out") covers
      infrastructure migration via feature flags more thoroughly than
      `02-release-strategies.adoc:119-157` (Feature flags — decouple
      deployment from release; gradual rollouts) and
      `04-rollback.adoc:17-20` (a dual-write-then-switch-readers schema
      migration) — specifically, the reference frames flags as the
      mechanism for *infrastructure* rollout (replacing a database/backend
      service, not just user-facing feature toggling); prescribes a
      multi-flag migration sequence (ramp writes to the new service in
      parallel with the old, a separate flag to read from the new service
      without using data in responses — shadow reads, a flag for
      comparison/verification checks, a final flag to ramp real reads);
      states that multiple versions of infrastructure and data is the norm;
      and supports per-user migration cohorts. TS-10 establishes flags and
      gradual rollout and sketches a one-shot dual-write migration, but
      never frames flags as infrastructure-rollout tooling, never describes
      the staged parallel-write / shadow-read / comparison-check sequence,
      never treats multi-version infrastructure as a norm, and never
      addresses per-user migration. Recommend a new "Infrastructure
      migrations via feature flags" subsection in `02-release-strategies.adoc`
      (after the Feature flags section) covering the staged parallel-run /
      shadow-read pattern. Note: this overlaps TS-45 (Data Migrations); the
      user may decide to split.

- [ ] https://programmingisterrible.com/post/139222674273/write-code-that-is-easy-to-delete-not-easy-to
      (Step 7: feature flags as release/branch decoupling and runtime
      control) covers the branch-merging and operability angles beyond
      `02-release-strategies.adoc:119-130` (flags decouple deployment from
      release; runtime enable/disable without redeploy) and `:134-136`
      (trunk-based: flags let incomplete features merge to main) —
      specifically: flags *decouple feature releases from merging branches*
      (the Google Chrome example — the hardest part of a regular release
      cycle was merging long-lived feature branches; by toggling new code
      on/off without recompiling, larger changes break into smaller merges
      without impacting existing code, and long-running feature development
      becomes visible early so cross-cutting impact surfaces sooner); and
      the *SRE runtime-operability* angle — being able to change your mind
      at runtime becomes increasingly important as rollout duration grows
      (hours/days/weeks), and "any system that can wake you up at night is
      one worth being able to control at runtime." TS-10 frames runtime
      toggling as a risk-management/gradual-rollout convenience, not as the
      operability argument tied to rollout duration and on-call. This is
      distinct from the existing "feature flags are how infrastructure is
      rolled out" Partial above (infrastructure migration). Recommend
      expanding the trunk-based bullet (`02-release-strategies.adoc:134-136`)
      with the Chrome long-lived-branch rationale, and adding an
      operability/runtime-control note tying runtime control to rollout
      duration and on-call. Note: the branch-merging angle overlaps TS-9
      (Version Control) trunk-based/branching guidance.

## Out-of-scope

(None identified in this run.)

- [ ] https://www.gov.uk/guidance/government-design-principles (Principle 5,
      "Iterate. Then iterate again") covers starting small with MVPs,
      releasing early, progressing alpha → beta → live, iterating based on
      user feedback, deleting what doesn't work, and scrapping prototypes.
      This sits outside this standard because the repository's top-level
      `src/README.adoc` declares that "Methods and tools that help us to
      achieve our design goals – things like iterative and incremental
      development driven by feedback loops – are out-of-scope," and TS-10
      is scoped to production-release mechanics (`README.adoc:13-14`
      excludes pre-release environments). The fragments that touch
      feedback-driven refinement (A/B testing `02-release-strategies.adoc:138`,
      kill switches `02-release-strategies.adoc:141-146`) are operational
      enablers, not the iterate-to-learn process itself. Flagged for the
      user to confirm or overrule.

## Unresolved

(None.)
