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

## Out-of-scope

(None identified in this run.)

## Unresolved

(None.)
