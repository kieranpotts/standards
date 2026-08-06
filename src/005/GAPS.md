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

**Second run, 2026-08-05.** Re-run against
https://12factor.net/[The Twelve-Factor App] (Adam Wiggins, 2017), fetched
directly rather than via the `__TODO__/` drafts (which were themselves derived
from this source — see the Assessment above). This corroborates most of the
first run's Missing items on configuration, statelessness, backing services,
and port binding almost claim-for-claim, and adds detail the `__TODO__/` drafts
did not capture: explicit dependency-declaration/isolation tooling (Factor II),
the Unix process-model detail behind concurrency (Factor VIII), and specific
SIGTERM/shutdown-protocol detail behind disposability (Factor IX). New items
below are additive to, not replacements for, the first-run items on the same
themes. All new gaps open.

**Third run, 2026-08-06.** Re-run against the *Architecture Playbook* (AR
Playbook) by Maikel Mardjan / nocomplexity.com
(https://nocomplexity.com/documents/arplaybook/introduction.html), traversing
its Business, Data, Applications, and Technology Infrastructure sections plus the
Software Architecture, Software Development, Quality, NFR Capabilities, and
Architecture References pages. The AR Playbook is a broad Enterprise
Architecture reference — tool/template/checklist/NFR heavy and deliberately
method-agnostic — so the large majority of its content sits outside TS-5's
stated purpose (the architecture of standalone applications) and is flagged
out-of-scope below. Only a handful of prescriptive points fall inside TS-5's
scope and are unaddressed, chiefly: domain analysis before microservices, the
Self-Contained Systems (SCS) pattern, and the abstraction-layer-as-dependency
trade-off for vendor facades. All new gaps open.

**Fourth run, 2026-08-06.** Re-run against the UK Government Design
Principles (https://www.gov.uk/guidance/government-design-principles). Of
its 11 principles, only #8 ("Build digital services, not websites") was
routed to TS-5. The principle is a user-facing service-design thesis
(services help people do things; uncover user needs; the digital world
connects to the real world; think about all aspects of a service
end-to-end) that sits outside TS-5's stated purpose (the internal
architecture of standalone applications) — TS-5's `06-services.adoc`
covers SOA/microservices as a code-decomposition strategy, a different
sense of "service." Recorded as out-of-scope, flagged for the user. No
in-scope gaps added; all prior gaps remain open.

**Fifth run, 2026-08-06.** Re-run against Jeff Hodges' "Notes on
Distributed Systems for Young Bloods"
(https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/).
One point was routed to TS-5: P18 ("Extract services"). Partial — TS-5
covers independent deployability and incremental extraction but not the
services-vs-shared-libraries trade-off (deployment and social coordination
costs, strict boundary preventing shortcuts) or the storage-migration-
hiding use case. One new Partial gap added; all prior gaps remain open.

**Sixth run, 2026-08-06.** Re-run against Nelson Elhage's "Reflections on
software performance" (https://blog.nelhage.com/post/reflections-on-performance/).
Two points were routed to TS-5: "architecture strongly impacts performance"
(D) and "performant foundations simplify architecture" (F). Both Missing —
TS-5 mentions performance only incidentally (as a framework-selection factor
at `05-frameworks.adoc:79-84` and a multi-process motivation at
`README.adoc:11-12`), with no thesis that architecture determines
performance or that a fast core simplifies architecture. Two new Missing
gaps added; all prior gaps remain open.

**Seventh run, 2026-08-06.** Re-run against tef's "Write code that is easy
to delete, not easy to extend" (https://programmingisterrible.com/post/139222674273/write-code-that-is-easy-to-delete-not-easy-to).
One point was routed to TS-5: layering (boilerplate, simple-on-simple,
protocol vs policy, wrap third-party libraries). Partial — TS-5 strongly
covers wrapping third-party libraries behind facades but not
boilerplate-as-dependency-avoidance, simple-on-simple API stacking, the
protocol/policy split, or the pleasant-vs-extensible API tension. One new
Partial gap added; all prior gaps remain open.

**Eighth run, 2026-08-06.** Re-run against Dan McKinley's "Choose Boring
Technology" (https://mcfunley.com/choose-boring-technology). Three points
were routed to TS-5: optimize globally (P1), deliberate adoption process
(P2), and polyglot operational toil (P3). All Partial — TS-5 has
"frameworks as platforms" (org-wide TCO) and "frameworks as destinations"
(build-without-framework) and dependency-minimization, but no
global-optimization/least-worst thesis, no operational/cognitive cost
items, no deliberate org-visible adoption process, no migration-timeline
governance, and no polyglot-toil thesis (and `05-frameworks.adoc:69-72`
contradicts McKinley by recommending per-app "best tool for the job"). Two
new Partial gaps added; all prior gaps remain open.

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

- [ ] https://12factor.net/dependencies ("A twelve-factor app never relies on
      implicit existence of system-wide packages. It declares all dependencies,
      completely and exactly, via a dependency declaration manifest... uses a
      dependency isolation tool during execution to ensure that no implicit
      dependencies 'leak in' from the surrounding system... applied uniformly
      to both production and development") is not addressed. `04-dependencies.adoc`
      covers minimizing, vetting, and updating dependencies, but never states
      the more basic requirement that all dependencies MUST be declared in a
      manifest and installed via an isolation mechanism (eg. a lockfile plus a
      per-project virtual environment or `node_modules`), applied identically
      in development and production. Recommend a new "Dependency declaration"
      subsection at the top of `04-dependencies.adoc`, before the current
      opening paragraph.

- [ ] https://12factor.net/dependencies ("If the app needs to shell out to a
      system tool, that tool should be vendored into the app") is not
      addressed. `04-dependencies.adoc` does not mention shell-out dependencies
      on system tools (eg. ImageMagick, curl) at all. Recommend adding to the
      new subsection proposed above.

- [ ] https://12factor.net/concurrency ("twelve-factor app processes should
      never daemonize or write PID files. Instead, rely on the operating
      system's process manager [...] to manage output streams, respond to
      crashed processes, and handle user-initiated restarts and shutdowns")
      is not addressed anywhere in TS-5. `06-services.adoc` covers service
      decomposition, reactive state machines, and CQRS, but says nothing about
      how an individual process's lifecycle (start, crash recovery, restart,
      shutdown) should be managed, nor that this responsibility belongs to an
      external process manager rather than the application itself. This
      borders TS-6 (Distributed System Design), which is currently an
      unwritten stub — see `../006/GAPS.md`. Recommend either a new
      subsection here or, once TS-6 is authored, there instead.

- [ ] https://12factor.net/disposability ("Processes shut down gracefully when
      they receive a SIGTERM signal. For a web process, graceful shutdown is
      achieved by ceasing to listen [...] then finishing any current requests
      [...] Worker processes [...] return the current job to the work queue")
      is more specific than the existing disposability gap
      (`__TODO__/principles/state.md:9`, first run above), which captures only
      the general "fast startup/shutdown" claim. The signal-handling mechanism
      and the distinct web-process vs worker-process shutdown protocols are
      new detail. Recommend folding into whichever new section addresses the
      first-run disposability gap.

- [ ] https://12factor.net/disposability ("all jobs [must be] reentrant [...]
      typically [...] wrapping the job in a transaction, or making the
      operation idempotent") is not addressed. Neither `04-dependencies.adoc`'s
      graceful-degradation section nor `06-services.adoc`'s reactive-systems
      section states that queued/background jobs MUST be safely re-runnable.
      Recommend adding to the disposability material proposed above, or to
      `06-services.adoc`'s reactive-systems section given its existing
      messaging-durability discussion (`06-services.adoc:100-113`).

- [ ] https://nocomplexity.com/documents/arplaybook/architecture-references.html#microservices
      (AR Playbook, Architecture References → Microservices) — "Before
      designing/building/running a microservices architecture, perform domain
      analysis first." Not addressed — `06-services.adoc:16-28` discusses the
      challenge of microservice interfaces and `06-services.adoc:30-67` covers
      bounded contexts, but the standard never states that domain analysis must
      precede microservices design. Recommend extending `06-services.adoc`'s
      Microservices section (after `06-services.adoc:28`) or the premature-
      decomposition section (`06-services.adoc:69-83`).

- [ ] https://nocomplexity.com/documents/arplaybook/architecture-references.html#architecture-methods
      (AR Playbook, Architecture References → Architecture Methods) —
      Self-Contained Systems (SCS): an architectural approach that separates a
      larger system's functionality into many independent, collaborating
      (self-contained) systems. Not addressed — `02-vertical-slices.adoc` and
      `06-services.adoc` cover the modular monolith → microservices extraction
      path, but the standard does not name or characterize the SCS pattern.
      Recommend a new subsection in `06-services.adoc` (or `02-vertical-slices.adoc`),
      noting SCS overlaps with the modular-monolith-to-services progression.

## Partial

- [ ] https://12factor.net/backing-services ("Resources can be attached to and
      detached from deploys at will [...] a resource may be spun up or torn
      down by the deploy's administrator") extends the first-run gap on
      `__TODO__/principles/services.md:3-5` above — beyond "backing services
      are attached, network-accessible resources," the reference adds that
      resources should be attachable/detachable by an administrator, without
      code changes, independent of application deploys. `06-services.adoc`
      does not cover this operational dimension.

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

- [ ] https://nocomplexity.com/documents/arplaybook/ti-architecture.html#abstraction-tools
      (AR Playbook, Technology Infrastructure → Abstraction Tools) — abstraction
      layers ease implementation and portability, but the trade-off is that the
      extra layer adds another dependency. Partial — `04-dependencies.adoc:74-89`
      and `05-frameworks.adoc:21-54` advocate vendor facades to decouple
      application code from frameworks/vendors, but never state the trade-off
      that an abstraction layer/facade is itself an additional dependency with
      its own maintenance cost. Recommend adding this caution to the "Vendor
      facades" section of `04-dependencies.adoc` (after `04-dependencies.adoc:89`).

- [ ] https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/
      ("Extract services") covers the services-vs-shared-libraries
      trade-off more thoroughly than `06-services.adoc:16-28` (independent
      deployability as the defining microservice characteristic) and
      `06-services.adoc:69-83` (incremental extraction from a modular
      monolith) — specifically, the reference compares extracting a service
      to distributing a shared library and argues the service wins on
      deployment coordination: upgrading a library requires coordinating a
      deploy of every client system (harder when out-of-order deploys risk
      data corruption, and a higher *social* coordination cost when clients
      have different maintainers), whereas a service deploys independently;
      the service boundary is *strict* in a way a library boundary is not,
      preventing the "shortcuts" (direct access to internals, shared
      in-memory state) that libraries permit; and the canonical use case is
      hiding a storage layer undergoing changes/migration behind a
      reduced-surface-area service API. TS-5 names independent
      deployability and endorses incremental extraction but never compares
      a service to a shared library, never makes the deployment/social-
      coordination-cost argument, never states the strict-boundary-
      prevents-shortcuts benefit, and never names the storage-migration-
      hiding use case (its vendor-facade pattern at `04-dependencies.adoc:74-89`
      is an in-process abstraction, not a deployed service). Recommend a
      new "Services vs shared libraries" subsection in `06-services.adoc`
      covering the trade-off and the storage-migration-hiding use case.

- [ ] https://blog.nelhage.com/post/reflections-on-performance/ ("Architecture
      strongly impacts performance") is not addressed anywhere in the
      standard. The reference argues that a system's basic architecture —
      high-level structure, dataflow, and organization — has profound
      performance implications; that early architectural decisions (eg.
      Sorbet's local-only type inference, which made it simpler, faster,
      and easier to parallelize/incrementalize) are cheap to make up front
      but extraordinarily costly to change later (the Flow team's
      multi-year refactor); and that to build truly performant software you
      must keep performance in mind while making early design/architectural
      decisions, lest you paint yourself into a corner. TS-5 mentions
      performance only incidentally — as one factor in framework choice
      (`05-frameworks.adoc:79-84`) and a reason for multi-process designs
      (`README.adoc:11-12`) — and never states that architecture determines
      performance or warns of architectural lock-in on performance.
      Recommend a new "Performance as an architectural concern" subsection
      (eg. in `README.adoc` or a new `07-performance.adoc`) stating that
      high-level structure and dataflow profoundly impact performance and
      that early architectural decisions are cheap up front but costly to
      reverse. Note: this borders on TS-2 (Software Design Qualities),
      which covers performance as a design quality — but the architectural-
      decision angle is TS-5's scope.

- [ ] https://blog.nelhage.com/post/reflections-on-performance/ ("Performant
      foundations simplify architecture") is not addressed anywhere in the
      standard. The reference argues that starting with a performant core
      can drastically *simplify* architecture for a given level of
      functionality: attempts to add performance to a slow system often add
      complexity (complex caching, distributed systems, fine-grained
      incremental-recomputation bookkeeping) that introduces bugs,
      overhead, and worse straight-line performance; when a tool is fast in
      the first place those layers may be unnecessary, yielding a net
      simpler system (Sorbet outperformed a slower Ruby tool *without*
      caching; its cache format has no forward/backward compatibility
      because cold-start is fast enough, avoiding the cache-invalidation
      complexity MyPy faced). TS-5 has adjacent instincts (cautions against
      premature decomposition and unnecessary dependencies/abstractions)
      but never connects them to *performance* as the driver, never states
      that a fast foundation can make caching/distribution/incremental
      layers unnecessary, and never warns that bolting performance onto a
      slow core is a complexity trap (it even defers caching to TS-46).
      Recommend a new "Performant foundations simplify architecture"
      subsection in `README.adoc` (or `07-performance.adoc`) covering the
      performance-simplicity trade-off. Note: the caching/distributed-
      systems layers it references border on TS-46 (Distributed Data and
      Caching) and TS-6 (Distributed System Design).

- [ ] https://programmingisterrible.com/post/139222674273/write-code-that-is-easy-to-delete-not-easy-to
      (Steps 3-4: layering — boilerplate, simple-on-simple, protocol vs
      policy, wrap third-party libraries) covers API layering beyond
      `01-horizontal-layers.adoc:43-46,98-123` (architectural layers;
      Vendors layer facades) and `04-dependencies.adoc:74-89` /
      `05-frameworks.adoc:21-54` (vendor/framework facades to avoid lock-in)
      — specifically: *boilerplate as a deliberate dependency-avoidance
      trade-off* (duplicate code to *use* a library, accepting verbosity to
      avoid introducing a dependency and retain flexibility — TS-5's
      dependency guidance is about minimizing/vetting deps, not accepting
      verbosity as a substitute for one); *simple-on-simple API stacking*
      (build a simple-to-use API on top of a simpler-to-implement but
      clumsy-to-use one — the `requests`-on-`urllib3` pattern; TS-5's
      layers are concern-separation layers, not API-stacking layers);
      *protocol vs policy* as a named distinction (wire formats, network
      protocols, parsing kits are the hard-to-delete code where business
      logic must be kept out — TS-5 keeps business logic in the Model layer
      but frames it as domain isolation, not protocol/policy contamination
      risk); the *pleasant-to-use vs extensible API tension* (wrapping
      resolves it by layering an opinionated API over a flexible one);
      empathy for the programmers who will use the API; and keeping `util`
      free of business logic. Recommend a new "Layering APIs: simple on
      simple" subsection in `04-dependencies.adoc` (or
      `01-horizontal-layers.adoc`) covering boilerplate-as-dependency-
      avoidance, simple-on-simple stacking, the protocol/policy split, and
      the pleasant-vs-extensible tension.

- [ ] https://mcfunley.com/choose-boring-technology ("Optimize globally" /
      "Just ship") covers global technology-selection optimization and
      polyglot-toil beyond `05-frameworks.adoc:8-19` ("frameworks as
      platforms" — org-wide standardization reduces total cost of ownership
      across a portfolio) and `04-dependencies.adoc:3-5` (minimize
      dependencies; each adds complexity/maintenance overhead) —
      specifically: technology choices should be optimized *globally across
      the org and the emerging system*, not per-problem ("best tool for the
      job" is myopic — the "best" tool is the "least worst" for as many of
      your problems as possible); adding tech carries *operations* and
      *cognitive overhead* (monitoring, unit tests, initial knowledge to
      hack on it, init scripts) that adds up fast; long-term costs of
      keeping a system working reliably vastly exceed build-time
      inconveniences; and polyglot freedom generates day-to-day operational
      toil that crushes teams ("technology for its own sake is snake oil";
      mindful choice frees minds for bigger questions). TS-5 argues
      standardization from the *benefits* side but never from the
      *cost-of-polyglot* side, never names polyglot proliferation as a
      risk, and `05-frameworks.adoc:69-72` actively recommends per-
      application "best tool for the job" selection — the myopia McKinley
      warns against. Recommend a "Global technology optimization" addition
      to `04-dependencies.adoc` (or a new `07-technology-selection.adoc`)
      covering least-worst-for-many-problems, the operational/cognitive
      cost items, and the polyglot-toil thesis.

- [ ] https://mcfunley.com/choose-boring-technology ("Choose new technology,
      sometimes") covers a deliberate adoption-governance process beyond
      `04-dependencies.adoc:41-44` (each dependency MUST be carefully
      considered/justified — vetting provenance/security) and
      `05-frameworks.adoc:56-72` ("frameworks as destinations" — the
      build-without-the-framework thought experiment) — specifically:
      adding tech requires *company-wide visibility/conversation* (set
      cultural expectations that "this is something we all talk about");
      exercise (a) consider how to solve the immediate problem *without
      adding anything new* (this detects the case where the "problem" is
      that someone just wants to use the technology — abort if so — TS-5's
      build-without-framework check is a design-fit test, not this
      tech-for-tech's-sake guard); exercise (b) write down exactly what
      about the current stack makes the problem prohibitively expensive;
      and exercise (c) when new tech overlaps/replaces existing tech, set
      clear *migration expectations with a proposed timeline* (policy
      typically "we're committed to migrating") to keep wreckage
      manageable and avoid proliferating locally-optimal solutions. TS-5's
      facades address making future migration *cheaper* but not the
      *governance* (migration-timeline policy, anti-proliferation
      rationale). Recommend a "Deliberate technology adoption" addition to
      `04-dependencies.adoc` covering the org-wide conversation, the
      solve-without-adding-new check, the write-down-prohibitive-cost
      exercise, and migration-timeline governance. Note: the migration-
      timeline angle overlaps TS-10 (Releasing) and TS-45 (Data Migrations).

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

- [ ] https://nocomplexity.com/documents/arplaybook/application-architecture.html#tools-for-creating-an-application-architecture
      (AR Playbook, Applications → Tools) — "Creating good interfaces (APIs) is
      a MUST for every good architecture; APIs form the connecting glue between
      modern applications," plus API design-first tooling (API Blueprint,
      Swagger/OpenAPI, RAML). API/interface design as a discipline plausibly
      sits outside this standard because it is covered by TS-20 (Network APIs)
      and TS-21 (HTTP APIs); TS-5 only addresses service interfaces at the
      architectural-boundary level (`06-services.adoc:55-67`). Flagged for the
      user to confirm or overrule.

- [ ] https://nocomplexity.com/documents/arplaybook/software-architecture.html
      (AR Playbook, Software Architecture) — architecture documentation and
      visualization methods/tools: the C4 model, arc42, Structurizr, Mermaid, the
      Bounded Context Canvas, Systemizer, and standardized templates
      (ISO/IEC/IEEE 42010:2011, SAD, SEI Architecture template). These are
      architecture-documentation concerns that plausibly sit outside this
      standard because they belong to TS-3 (Design Docs). Flagged for the user
      to confirm or overrule.

- [ ] https://nocomplexity.com/documents/arplaybook/architecture-references.html#architecture-methods,
      `arplaybook-template-architecturedecisions.html`, and `ADR-template.html`
      (AR Playbook) — Architectural Decision Records (ADRs) and structured
      architecture-decision logging. This plausibly sits outside this standard
      because recording design decisions is a documentation concern covered by
      TS-3 (Design Docs). Flagged for the user to confirm or overrule.

- [ ] https://nocomplexity.com/documents/arplaybook/software-development.html
      (AR Playbook, Software Development) — version control from day one,
      branching-model choice (GitHub flow), coding-style guides, code-quality
      analysis services, release-early/release-often, and semantic versioning.
      These plausibly sit outside this standard because they are delivery and
      code-level concerns covered by TS-9 (Version Control), TS-11 (Versioning),
      and TS-7 (Code Design). Flagged for the user to confirm or overrule.

- [ ] https://nocomplexity.com/documents/arplaybook/quality.html and
      `capabilities.html` (AR Playbook, Quality & NFR Capabilities) — the
      architecture must address quality attributes (performance, availability,
      maintainability, modifiability, security, privacy, testability,
      operability, flexibility), the ISO/IEC 25010 quality model, and NFR
      capabilities (high availability, disaster recovery, manageability,
      footprint, supportability, service levels). These plausibly sit outside
      this standard because software design qualities are covered by TS-2
      (Software Design Qualities), and HA/DR/deployment-topology concerns belong
      to TS-6 (Distributed System Design) and TS-49 (Cloud Platform Engineering).
      Flagged for the user to confirm or overrule.

- [ ] https://nocomplexity.com/documents/arplaybook/businessprinciples.html
      (AR Playbook, Business Principles) — start simple, MVP within one month,
      make-it-easy-then-fast, reuse-before-buy-buy-before-build, business
      continuity, ease-of-use, open data/standards/source, strategic focus.
      These are enterprise/product-ownership and delivery principles that
      plausibly sit outside this standard because TS-5 explicitly excludes "the
      means of getting there" and these concern business rather than application
      architecture. Flagged for the user to confirm or overrule.

- [ ] https://nocomplexity.com/documents/arplaybook/data-architecture.html and
      `data-principles.html` (AR Playbook, Data) — data modelling vs database
      design, conceptual/logical/physical data models, and data principles
      (timely, machine-processable, primary data). These plausibly sit outside
      this standard because data and database concerns are covered by TS-43
      (Relational Databases and SQL) and TS-44 (Non-Relational Databases).
      Flagged for the user to confirm or overrule.

- [ ] https://nocomplexity.com/documents/arplaybook/ti-architecture.html
      (AR Playbook, Technology Infrastructure, non-abstraction portion) —
      network-usage sizing (per-user IOPS/bandwidth peaks) and cloud-provider
      abstraction libraries (Apache Libcloud). These plausibly sit outside this
      standard because technology-infrastructure and cloud-platform concerns are
      covered by TS-49 (Cloud Platform Engineering) and TS-51 (AWS). The
      abstraction-layer-as-dependency trade-off from the same page is captured
      as a partial gap above. Flagged for the user to confirm or overrule.

- [ ] https://nocomplexity.com/documents/arplaybook/architecture-references.html
      (AR Playbook, Architecture References, catalog entries) — external
      reference architectures and pattern catalogs: BIAN, OASIS SOA Reference
      Architecture, Open Group SOA Reference Architecture, Microsoft Cloud
      Design Patterns, Cloud Computing Patterns, and the Red Hat Microservice
      Architecture Reference Architecture. These are external reference catalogs
      rather than prescriptive rules for this standard, and pattern catalogs for
      cloud/distributed systems plausibly belong to TS-6 (Distributed System
      Design). Flagged for the user to confirm or overrule.

- [ ] https://nocomplexity.com/documents/arplaybook/capabilities.html (AR
      Playbook, NFR Capabilities → `requirements.csv`) — "sensitive data must
      not be logged in clear text; database connections/passwords/keys/secrets
      must not be stored in plain text." This plausibly sits outside this
      standard because secrets and security concerns are covered by TS-52
      (Security and Secrets Management). Flagged for the user to confirm or
      overrule.

- [ ] https://www.gov.uk/guidance/government-design-principles (Principle 8,
      "Build digital services, not websites") covers service-as-something-
      that-helps-people, uncovering user needs, the explicit "not a website"
      framing, end-to-end consideration of all aspects of a service, the
      connection between the digital and real world, and service mapping.
      This plausibly sits outside this standard because TS-5's stated
      purpose is the internal architecture of standalone applications
      (`README.adoc:5-14`); its `06-services.adoc` addresses
      SOA/microservices as a code-decomposition strategy, a different sense
      of "service." Holistic user-facing service design is more a
      product/service-design concern with no current home in the standards
      corpus. Flagged for the user to confirm or overrule, or to route to a
      future service-design standard.

## Unresolved

- [ ] `__TODO__/principles2/defensive-programming.md`,
      `__TODO__/principles2/crash-only.md`, and
      `__TODO__/principles2/simplicity.md` are unwritten stubs (heading plus a
      TODO note only). No substantive claims could be extracted, so no gaps
      were derived from them. If these are fleshed out, re-run this analysis
      against them.