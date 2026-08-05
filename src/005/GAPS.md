# TS-5 gap analysis

Gaps found comparing TS-5: *Application Architecture* against the following
reference resources (all in the standard's `__TODO__/` draft directory):

- `src/005/__TODO__/automation.md`
- `src/005/__TODO__/configuration.adoc`
- `src/005/__TODO__/configuration.md`
- `src/005/__TODO__/CREDITS.adoc`
- `src/005/__TODO__/evolutionary.md`
- `src/005/__TODO__/feature-flags.adoc`
- `src/005/__TODO__/zero-configuration-philosophy.txt`
- `src/005/__TODO__/principles/` (README.md, state.md, infrastructure.md,
  administraion.md, services.md, configuration.md, logging.md)
- `src/005/__TODO__/principles2/` (README.md, defensive-programming.md,
  crash-only.md, simplicity.md)

**Assessment.** The reference material is a mix of 12-Factor-App-style
design principles (statelessness, port binding, config, logs, backing
services), a much deeper feature-flags treatment, and some delivery/ops
material. Roughly half falls inside TS-5's stated scope (application
architecture) and is currently unaddressed — chiefly configuration
management, statelessness, and the backing-service/port-binding model. The
feature-flags reference is substantially deeper than the standard's current
section, producing the largest cluster of partial/missing gaps. The other
half (CI/CD automation, build/release/run separation, env-var file
mechanics, admin processes, product UX defaults) plausibly belongs to other
standards (TS-9, TS-10, TS-45, TS-48, TS-49) and is flagged out-of-scope.

**Status:** First run, 2026-08-05. All gaps open.

## Missing

- [ ] `__TODO__/configuration.adoc:3` (also `configuration.md:9`,
      `principles/configuration.md:12`) — Environment-specific configuration
      MUST be driven by environment variables. Not addressed anywhere in the
      standard. Recommend a new "Configuration" section after
      `01-horizontal-layers.adoc:96` (System layer discussion) or as a new
      `07-configuration.adoc`.

- [ ] `__TODO__/configuration.adoc:5` — All application configuration MUST be
      centralized; environment variables imported into a single
      configuration object; application code accesses the object and MUST NOT
      read environment variables directly. Not addressed. Recommend new
      "Configuration" section.

- [ ] `__TODO__/configuration.md:5` (also `principles/configuration.md:3-10`) —
      Static and dynamic configuration MUST be kept strictly separate; static
      config (routing rules, memory limits, dependency resolution config)
      defined in code and committed to source control, dynamic config (DB
      credentials, file paths, feature flags, release version numbers) kept
      out of source code. Not addressed. Recommend new "Configuration"
      section.

- [ ] `__TODO__/principles/configuration.md:12` (also `configuration.md:7-11`)
      — Dynamic configuration provided at runtime by the host environment
      (e.g. environment variables set at the infrastructure level) or
      injected at compile time based on the build's target environment (e.g.
      CI/CD adding an appropriate `.env`); environments also used to provide
      sensitive static data (private keys, hashing salts) that cannot be
      committed. Not addressed. Recommend new "Configuration" section.

- [ ] `__TODO__/principles/state.md:3` — Applications MUST be treated as
      stateless processes (or multiple stateless processes if horizontally
      distributed); MUST NOT rely on storing state locally (file system or
      other local caching). Not addressed — the standard discusses service
      state machines (`06-services.adoc:87-119`) and Kernel UI state
      (`01-horizontal-layers.adoc:78-80`) but never states the
      stateless-process principle. Recommend new section, or extend
      `01-horizontal-layers.adoc` near the System layer discussion
      (`01-horizontal-layers.adoc:91`).

- [ ] `__TODO__/principles/state.md:5` — All state MUST be offloaded to
      backing services, treated as attached, network-accessible resources
      (local or remote). Not addressed. Recommend new section alongside the
      statelessness gap above.

- [ ] `__TODO__/principles/state.md:7` — Stateless applications enable
      concurrent processing through horizontal scaling of the process model,
      without adjusting application code or tooling/deployment process. Not
      addressed. Recommend new section.

- [ ] `__TODO__/principles/state.md:9` — Stateless applications allow fast
      startup and shutdown, making runtime environments easily replicable
      and disposable; graceful shutdown without side effects makes the
      overall system more robust. Not addressed. Recommend new section.

- [ ] `__TODO__/principles/infrastructure.md:3` — There MUST always be a
      clean contract with the underlying operating system, to give maximum
      portability between execution environments. Not addressed. Recommend
      new section (portability as an architectural concern), or extend the
      System layer discussion at `01-horizontal-layers.adoc:91`.

- [ ] `__TODO__/principles/services.md:7` — Network services SHOULD be
      exported using port binding; the application natively binds to a port
      and listens for connections, while routing and request forwarding are
      handled externally (system software configured at the infrastructure
      level). Not addressed. Recommend new section, or extend
      `01-horizontal-layers.adoc` I/O layer discussion
      (`01-horizontal-layers.adoc:60-69`).

- [ ] `__TODO__/feature-flags.adoc:17` — Ops toggles: controlled by
      operations teams (not developers), used to quickly disable or throttle
      resource-intensive features and as "kill switches" for whole services
      or subsystems; recommended for new features with unclear performance
      implications. Not addressed — `03-feature-flags.adoc:31` mentions
      canary/staged rollouts/A/B testing but no toggle taxonomy or ops
      toggles. Recommend extending `03-feature-flags.adoc` after line 32.

- [ ] `__TODO__/feature-flags.adoc:21` — Permissions toggles: change features
      and experiences on a per-user basis (premium features for paying
      customers, alpha features for internal users, beta features for opt-in
      external users via canary channels); the longest-lived toggle category.
      Not addressed. Recommend extending `03-feature-flags.adoc`.

- [ ] `__TODO__/feature-flags.adoc:23` — Release, ops, experiment, and
      permissions toggles are distinct concerns with different change
      requirements and stakeholders; best practice is for each category to
      use different toggle mechanisms. Not addressed. Recommend extending
      `03-feature-flags.adoc`.

- [ ] `__TODO__/feature-flags.adoc:25` — A toggle can move between categories
      over a feature's lifecycle (e.g. experiment → feature → permissions
      toggle), and the toggle mechanism/format may change accordingly (admin
      UI → source-controlled YAML/config → JWT token). Not addressed.
      Recommend extending `03-feature-flags.adoc`.

- [ ] `__TODO__/feature-flags.adoc:27-31` — Feature flags carry costs and
      risks: widespread release flags make codebases hard to maintain;
      testing complexity grows with combinations of code paths; release flags
      permit dead code and configuration to endure; Martin Fowler's guidance
      that release flags should be the last choice for putting features into
      production. Not addressed — `03-feature-flags.adoc` presents only
      benefits. Recommend extending `03-feature-flags.adoc` with a "Costs and
      risks" subsection after line 32.

- [ ] `__TODO__/feature-flags.adoc:38` — Code and configuration for
      deprecated features MUST be removed as early as possible; dead code has
      maintenance/security costs; release flags are cheap to create but
      accumulate cost; Knight Capital's US$460 million loss is cited as a
      cautionary tale on mismanaged feature flags. Not addressed. Recommend
      extending `03-feature-flags.adoc` with flag-retirement/dead-code-removal
      guidance.

- [ ] `__TODO__/feature-flags.adoc:40-48` — Flag management practices: clear
      stakeholder roles and policies; log a tracker ticket to remove a new
      release flag later; put expiration dates ("time bombs") on release
      flags that make tests fail when expired flags remain; cap the total
      number of release flags in an environment (old flags removed before new
      ones added). Not addressed. Recommend extending `03-feature-flags.adoc`.

- [ ] `__TODO__/feature-flags.adoc:52` — All feature flags should be fully
      documented, with code cross-referencing out-of-band documentation;
      documentation is essential for new developers to understand flag
      context. Not addressed. Recommend extending `03-feature-flags.adoc`.

- [ ] `__TODO__/feature-flags.adoc:54` — There should be a standard for
      annotating "dead" code that never executes because it is not yet
      released via its toggle; developers should be able to instantly
      distinguish "live" from "hidden" code without reverse-engineering
      execution paths. Not addressed. Recommend extending
      `03-feature-flags.adoc`.

- [ ] `__TODO__/feature-flags.adoc:56` — Avoid code whose execution is
      controlled by more than one toggle; multiple toggles create exponential
      testing complexity. Not addressed. Recommend extending
      `03-feature-flags.adoc`.

## Partial

- [ ] `__TODO__/principles/services.md:3-5` covers the "backing services as
      attached network resources" model more explicitly than
      `01-horizontal-layers.adoc:91-96` — specifically, the standard's System
      layer lists example components (databases, message queues, services)
      but does not articulate that local and remote services should both be
      abstracted as attached, network-accessible resources with connection
      details set in the environment configuration.

- [ ] `__TODO__/principles/logging.md:3` covers logging more thoroughly than
      `01-horizontal-layers.adoc:36-38` — specifically, the standard only
      lists "logging tools and monitoring services" as candidates for the
      System layer, while the reference states the principle that logs should
      be treated as event streams, applications should stream logs to
      standard output, and external services should handle those streams.

- [ ] `__TODO__/feature-flags.adoc:3` frames the simple feature flag pattern
      more precisely than `03-feature-flags.adoc:34-42` — specifically, the
      reference defines a flag as returning a value set independently of the
      code at the infrastructure level (usually an environment variable),
      whereas the standard only shows the conditional-check code shape without
      the environment-driven-value framing.

- [ ] `__TODO__/feature-flags.adoc:13` covers the "release flag" use case
      more directly than `03-feature-flags.adoc:5-21` — specifically, the
      standard explains decoupling deployment from release in general terms
      but does not articulate that feature flags are most commonly used to
      ship incomplete, untested code to production, nor names the "release
      flag" category.

- [ ] `__TODO__/feature-flags.adoc:19` covers experiment toggles more
      thoroughly than `03-feature-flags.adoc:32` — specifically, the standard
      mentions A/B testing in a single phrase, while the reference explains
      experiment toggles serve different experiences to different users for
      journey optimization based on usage analysis and may be managed by
      non-developer stakeholders (UX designers, content authors).

## Out-of-scope

- [ ] `__TODO__/automation.md:3-9` covers CI/CD automation, build/release/run
      stage separation, environment parity, and version-control-driven
      deployment, which plausibly sits outside this standard's stated purpose
      because TS-5 explicitly excludes "the means of getting there" (delivery
      process). These belong to TS-9 (Version Control) and TS-10 (Releasing).
      Flagged for the user to confirm or overrule.

- [ ] `__TODO__/configuration.adoc:7` requires an `.env.example` file listing
      all environment variables, kept up-to-date, which plausibly sits outside
      this standard because it is the specific mechanics of environment
      variables covered by TS-48 (Environment Variables). Flagged for the
      user to confirm or overrule.

- [ ] `__TODO__/configuration.adoc:11-13` requires the central config object
      to define production-appropriate defaults (and no defaults for sensitive
      values), which plausibly sits outside this standard because
      environment-variable defaults are covered by TS-48 (Environment
      Variables). Flagged for the user to confirm or overrule.

- [ ] `__TODO__/CREDITS.adoc:3-11` records external influences (12 Factor
      App, 12 Factor CLI Apps), which is repository meta-information, not a
      technical-standard claim. Flagged for the user to confirm or overrule.

- [ ] `__TODO__/zero-configuration-philosophy.txt:1-8` describes a "Zero
      Configuration Philosophy" product UX principle (sensible defaults, only
      subjective settings require user configuration), which plausibly sits
      outside this standard because it concerns end-user product design
      rather than application architecture. Flagged for the user to confirm or
      overrule.

- [ ] `__TODO__/principles/infrastructure.md:3` (cloud-platform-deployment
      portion) recommends applications be suitable for deployment to modern
      cloud platforms to reduce reliance on physical servers and
      administrators, which plausibly sits outside this standard because
      cloud platform engineering is covered by TS-49. The
      OS-portability/clean-contract portion of the same line is captured as a
      missing gap above. Flagged for the user to confirm or overrule.

- [ ] `__TODO__/principles/administraion.md:3-5` recommends administrative
      tasks (e.g. DB migration scripts) be run as one-off processes against
      specific releases with automation scripts shipped with the application,
      which plausibly sits outside this standard because it is an operational
      concern covered by TS-10 (Releasing) and TS-45 (Data Migrations).
      Flagged for the user to confirm or overrule.

## Unresolved

- [ ] `__TODO__/principles2/defensive-programming.md`,
      `__TODO__/principles2/crash-only.md`, and
      `__TODO__/principles2/simplicity.md` are unwritten stubs (heading plus a
      TODO note only). No substantive claims could be extracted, so no gaps
      were derived from them. If these are fleshed out, re-run this analysis
      against them.