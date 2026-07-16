# TS-10: Releasing

This is a compact version of technical standard TS-10 for AI agents.

Use this when choosing release cadence or rollout strategy, designing release
approval/governance, planning rollback, declaring change freezes, or writing
release notes/changelogs/migration guides/deprecation notices/security
advisories. Applicable to both intermittently-released software-as-a-product and
continuously-released software-as-a-service. Concerned with production releases
specifically (not deployments to test/staging).

Do NOT use this for the version-control mechanics that underpin releases
(branching, integration, release-trunk/release-branch workflows) — those are
covered by [TS-9: Version Control](../009/AGENTS.md). For version numbering
see [TS-11: Versioning](../011/AGENTS.md).

## Rules

### Release cadence

The first and most consequential decision is _cadence_ — how frequently
versions are delivered and how much change each release contains. Cadence
shapes which strategies are viable, the automation required, the testing
investment, and incident response. Three cadences on a spectrum:

- **Big bang** — infrequent releases bundling a large volume of accumulated
  change; planned/scheduled with formal release windows and stakeholder
  sign-off. Common for shrink-wrapped products, software with strong
  backward-compatibility commitments, and strict-governance orgs. Principal
  disadvantage: isolating the cause of a post-release problem is hard and the
  blast radius is large — compensate with extensive pre-release testing,
  formal rehearsals, and detailed rollback plans.

- **Release trains** — versions delivered at a regular, predictable interval
  (every two weeks, month, quarter). Changes merged and verified before
  cut-off board the train; misses wait for the next. Balances predictability
  and throughput; gives consumers a known upgrade rhythm. A feature missing
  cut-off may be delayed a full cycle. Widely used for libraries, frameworks,
  mobile apps, and platforms with external consumers.

- **Continuous deployment** — every change passing automated verification is
  released to production automatically, often within minutes of merge; no
  scheduled release event. Requires high-confidence automated testing, robust
  observability, and operational maturity to respond to incidents quickly.
  Typically combined with feature flags and progressive rollout so that
  _deploying_ code is decoupled from _releasing_ a feature. Suited to web
  services/SaaS where all users run the same version; generally inappropriate
  for software distributed to consumer devices or installed on-premises.

- **Cadence has direct implications for versioning.**

  Big-bang and release-train cadences pair naturally with semantic versioning
  (each release is a discrete event with a meaningful number). Continuous
  deployment releases too frequently for human-meaningful numbers; build tags,
  commit SHAs, or date-based versioning (CalVer) are often more useful. See
  [TS-11: Versioning](../011/AGENTS.md).

### Release strategies

Strategy determines _how_ a new version is rolled out to users/instances. The
simplest is a big-bang deployment (all users at once) — appropriate for
low-risk changes, low-traffic systems, or scheduled-downtime windows. For
systems with availability requirements, larger user populations, or
higher-stakes changes, one of the strategies below SHOULD be used. Strategy is
constrained by cadence: big bang typically pairs with scheduled-downtime
cutovers or blue-green; release trains often pair with canary or staged
rollouts; continuous deployment usually combines with rolling or canary plus
feature flags.

- **Rolling deployment** — gradually replaces old-version instances with new;
  both versions serve traffic throughout; system stays available. Works well
  for horizontally scaled, stateless services on orchestrators (Kubernetes,
  ECS, Nomad) or autoscaling groups. Key parameters: rollout rate (faster =
  larger blast radius), health-check criteria, and failure policy (halt +
  MAY auto-rollback). Requires less infrastructure than blue-green but offers
  no instant rollback — reverting is another rolling deployment in reverse.
  Requires that old and new versions can coexist without conflict; not
  appropriate where schema migrations aren't backwards-compatible without
  additional design work.

- **Canary testing** — initially roll out the change to a small subset of
  users (eg. route a small percentage of traffic via a load balancer, or
  deploy to a single node). Useful for services difficult to test in
  isolation or where the potential impact of failure is high. _Staged
  rollouts_ extend this: ramp the percentage up between stages, monitoring
  health and setting criteria for continuation.

- **Blue-green deployment** — two identical production environments
  ("blue"/"green") maintained side by side; only one serves live traffic.
  Deploy the new version to the idle environment, validate, switch traffic
  (via load balancer or DNS). Chief advantage: near-instantaneous rollback
  (redirect traffic back without redeploying). Well-suited to stateless
  services; for persistent state (especially databases) require schema
  changes in two phases (backwards-compatible migration first, cleanup
  migration after full release). Differs from canary in shifting all traffic
  at once; the two MAY be combined (canary to green before full cutover).

- **Feature flags** — conditional statements controlling whether a feature is
  active, state typically controlled at runtime via a configuration service.
  Decouple _deployment_ of code from _release_ of features: deploy disabled,
  later enable for all/cohorts/gradually without redeploying. Common uses:
  trunk-based development (merge incomplete features without exposing them
  — see [TS-9](../009/AGENTS.md)), A/B testing, kill switches (quickly
  disable a problem feature without rollback/redeployment), and gradual
  rollouts at the feature level.

  Flags introduce complexity — each is a branch and the combinatorial
  explosion of flag states is hard to test exhaustively. Flags SHOULD be
  used sparingly; applications SHOULD have a defined maximum number of flags
  at any one time. Flags SHOULD have a defined lifecycle — once a feature is
  fully rolled out and stable, the flag and the dead code path SHOULD be
  removed (via a deployment). Long-lived flags are a common source of
  technical debt and occasionally of incidents (eg. accidental toggling of
  an obsolete flag).

### Release approval and governance

- **Where governance requires a manual gate, put it at the `ready` → `release`
  boundary — not earlier.**

  Earlier gates (on commits to `dev`, or on promotion to `ready`) interfere
  with continuous integration and the principle that `ready`'s tip is always
  shippable. Gate at release to preserve a continuously-deliverable codebase
  while controlling _when_ changes reach production.

- **Choose an approval mechanism appropriate to the regulatory environment and
  cadence.**

  Common patterns: pull-request approval (PR/tag-promotion PR reviewed by
  named approvers — immediate version-controlled audit trail),
  change-management tickets (eg. ServiceNow, Jira Service Management;
  pipeline checks ticket state before promoting), change-advisory-board (CAB)
  sign-off (scheduled board review; common in larger/regulatory orgs but
  introduces latency and is poorly suited to high-cadence releases), and
  automated policy gates (rules-based checks — test coverage thresholds,
  security-scan results, absence of critical open incidents — that block
  release if violated; complement rather than replace human approval where
  governance demands it; essential where cadence is too high for
  human-in-the-loop review).

- **Tie approvals to roles, not individuals.**

  Approvals SHOULD be tied to _roles_ (on-call engineer, release manager,
  product owner, security/compliance officer, executive sponsor for
  high-impact changes) so the workflow doesn't break when a person is
  unavailable. For each role, document the scope of changes it can approve,
  any required sequencing (eg. security review MUST precede production
  approval), and delegation rules.

- **Capture an auditable, traceable approval record for each release.**

  At minimum: the version being released (with reference to the source-control
  tag/commit), identity of each approver and the role under which they
  approved, timestamp, the artifacts being deployed (with references to the
  artifact repository — see [TS-9](../009/AGENTS.md)), and any exceptions or
  deviations with justification. Retain per regulatory/organizational policy.

- **MUST include a documented break-glass procedure for emergency releases.**

  A formal approval process MUST NOT prevent rapid response to production
  incidents. The break-glass procedure SHOULD: reduce approval to a minimum
  (eg. a single on-call engineer, or two-person review with a senior
  reviewer), require post-hoc review and full audit-trail backfill once the
  incident is resolved, and be tested periodically (like other DR procedures)
  so the team is fluent under pressure. Its existence is not a license to
  bypass normal governance — track invocations; frequent invocations SHOULD
  prompt review of whether the standard process is too restrictive.

### Rollback

- **Have a rollback strategy; document and periodically rehearse it.**

  An untested rollback plan is not a rollback plan.

- **Simplest rollback is redeploying the previous version, which requires the
  previous artifacts remain available and deployment is fast enough to be
  useful during an incident.**

  See [TS-9](../009/AGENTS.md) for artifact storage and the
  version-tag-to-artifact binding that makes rollback reproducible.

- **For services with persistent state, design schema/data migrations to be
  reversible.**

  Schema migrations SHOULD be backwards-compatible across at least one
  release (eg. column rename: one release adds the new column and dual-writes,
  next release switches readers, later release removes the old column). Data
  migrations SHOULD be idempotent so they can be safely re-run if interrupted
  or if a partial rollback occurs.

- **Consider roll-forward where rollback is risky.**

  When database state has diverged, or a targeted hotfix can be prepared
  quickly, preparing a new release that fixes the problem is often preferable
  to reverting.

### Change freezes

- **A change freeze (code freeze / release freeze) is a defined period during
  which no non-critical changes are released to production.**

  Common around: high-traffic commercial events (Black Friday), holiday
  periods with reduced on-call coverage, major customer events/product
  launches/marketing campaigns, and external audit or compliance windows.
  During a freeze, only critical bug fixes and security patches are released.
  Freezes SHOULD be communicated in advance, with clear criteria for what
  constitutes a "critical" change, a documented exception process for
  unforeseen circumstances, and dates/scope visible to all affected teams.

### Release documentation

Two related but distinct artifacts document what has changed; a project may
produce one, the other, or both.

- **Every production release SHOULD be accompanied by release notes.**

  Audience and format vary by software type:

  - Libraries and APIs — aimed at consuming developers; highlight new
    features, deprecations, notable bug fixes with sufficient detail to
    understand impact. Breaking changes MUST be called out prominently and
    SHOULD be accompanied by a migration guide where possible.
  - End-user applications — aimed at users; describe new functionality and
    notable fixes in user-meaningful terms, avoiding implementation detail.
  - Internal services — aimed at other teams; note changes to interfaces,
    performance characteristics, or operational requirements.

  Release notes SHOULD be written as part of the normal development process,
  not separately at release time. A consistent commit-message convention is
  RECOMMENDED to support automatic generation (where appropriate). Release
  notes SHOULD reference the version number. A GitHub Release is RECOMMENDED
  only where GitHub is the primary distribution channel (binaries, CLIs,
  artifacts downloaded from the repo's releases page); where artifacts are
  distributed via a package registry (npm, PyPI, Maven Central, container
  registry) or deployed directly, tagging the release point in Git history is
  sufficient and notes MAY be published through whatever channel reaches the
  consumers.

- **Maintain a changelog for software where consumers may compare versions,
  plan upgrades, or trace when a change was introduced.**

  A changelog is a chronological, cumulative engineering reference spanning
  every release; release notes are a curated summary tied to a single release
  for a specific audience. The two SHOULD NOT be conflated: release notes
  answer "What does this release mean for me?" (selective, narrative, often
  non-technical); changelogs answer "What changed between version X and Y?"
  (exhaustive, structured, for engineers). For some developer-facing
  libraries they may be the same artifact; for end-user products and large
  platforms they are distinct, with notes typically derived by summarizing
  the relevant changelog section in audience-appropriate language.

  Maintain a changelog for libraries, APIs, CLIs, infrastructure components,
  and most internal services. Publish release notes for any software where a
  release is a discrete event communicated to an audience (end-user apps,
  paid products, major platform upgrades, and libraries/APIs with a wide
  consumer base where the changelog alone would be too dense).

  A widely-adopted convention is [Keep a Changelog](https://keepachangelog.com/)
  — structure organized by version, changes grouped under fixed headings:
  **Added**, **Changed**, **Deprecated**, **Removed**, **Fixed**, **Security**.
  A `CHANGELOG.md` file SHOULD be maintained in the source repository with
  entries added as part of the same change that introduces them (avoids the
  failure mode of reconstructing history at release time). Where commit
  messages follow a consistent convention, the changelog MAY be generated
  automatically from history, though human curation is often still needed.

- **Provide a migration guide for releases introducing breaking changes,
  significant behavioral differences, or non-trivial config updates.**

  Release notes describe _what_ changed; a migration guide describes _what
  consumers need to do_ in response. Release notes SHOULD link to the relevant
  migration guide for any breaking change. Migration guides SHOULD: be
  versioned to specific transitions (eg. "Migrating from v1 to v2"; a separate
  guide MAY be provided per major transition); enumerate every breaking
  change with before-and-after code/config examples where applicable;
  highlight required ordering of steps (especially where data migrations or
  downtime are involved); and note any tooling (codemods, migration scripts)
  that can automate parts of the upgrade. For libraries with a large consumer
  base, the cost of a poorly documented migration is borne many times over.

- **Issue deprecation notices well in advance of planned removal.**

  A deprecation notice is a forward-looking formal communication that a
  feature/API/endpoint/config option/behavior will be removed in a future
  release — the mechanism by which breaking changes can be introduced
  gradually. SHOULD include: what is being deprecated (unambiguously); the
  release in which the deprecation takes effect; the release or criteria that
  will trigger removal; the recommended replacement (if any) with a reference
  to a migration guide; and the reason. Projects SHOULD adopt and publish a
  deprecation policy defining the minimum notice period (a common convention:
  a feature deprecated in `vN.x` will not be removed before `vN+1.0`, or
  before a defined number of minor releases). Where the language/runtime
  supports it, deprecation SHOULD also be signaled in code — compiler
  warnings, runtime warnings, deprecation annotations, response headers — so
  consumers are alerted in their normal workflow, not only by reading docs.

- **Publish a security advisory for vulnerabilities identified and addressed
  in a release.**

  Distinct from regular release notes because of legal, compliance, and
  incident-response implications, and consumed by audiences (security teams,
  automated scanners, downstream maintainers) who may not otherwise track
  releases. SHOULD include: a unique identifier (ideally a
  [CVE](https://www.cve.org/) number for public-interest vulnerabilities, or
  a project-specific identifier like GHSA); a severity rating (typically
  [CVSS](https://www.first.org/cvss/)); a description including affected
  versions and exploitation conditions; the fixed version(s) and any
  mitigations/workarounds for consumers who cannot upgrade immediately; and
  acknowledgment of the reporter where appropriate. Publish through channels
  downstream consumers and automated tools can reliably discover (GitHub
  Advisory Database, ecosystem databases like RustSec/npm/PyPI, dedicated
  mailing lists). Disclosure SHOULD be coordinated with the release of the
  fix — premature disclosure exposes users to attack; delayed disclosure
  prevents users from understanding why an upgrade is urgent. Publish a
  documented security disclosure policy (how to report vulnerabilities and
  expected response times) in the repository, conventionally as
  `SECURITY.md`.

## References

- [TS-10 source](README.adoc)
- [TS-9: Version Control](../009/AGENTS.md)
- [TS-11: Versioning](../011/AGENTS.md)
- [Keep a Changelog](https://keepachangelog.com/)
