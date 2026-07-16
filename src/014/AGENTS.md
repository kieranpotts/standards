# TS-14: Performance Testing

This is a compact version of technical standard TS-14 for AI agents.

Use this when testing the *quality attributes* (non-functional requirements /
cross-functional requirements) of a software system — speed, capacity,
scalability, security, accessibility, usability, compliance, and resilience.
Despite the standard's title, its scope is the qualities as a whole, not
performance alone. NFRs describe _how well_ the system performs its functions,
not _what_ functions it performs, and they are architecturally significant —
they cannot be tested as an afterthought or bolted on before release; they
influence design at every level from infrastructure and data storage through
application logic and user interfaces.

Do NOT use this for functional testing — see
[TS-13: Functional Testing](../013/AGENTS.md). For canary testing and other
release testing strategies see [TS-10: Releasing](../010/AGENTS.md).

## Rules

The capitalized words REQUIRED, MUST, MUST NOT, RECOMMENDED, SHOULD, SHOULD NOT,
OPTIONAL, and MAY are to be interpreted as described in
[IETF RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

### Shift left

- **Integrate non-functional testing early and continuously; do not treat it as
  a last-mile quality gate before release.**

  Performance problems discovered late — or only after production deployment —
  cost orders of magnitude more to remediate than if found earlier. The same
  shift-left principle applies to security, accessibility, and compliance:
  vulnerabilities, barriers, and gaps are all significantly cheaper to address
  during development than in production, via external audit, or via user
  complaint. Shifting left also changes team culture — when developers get
  immediate feedback on non-functional impact (automated performance tests in
  CI/CD, security scanning in pull requests, accessibility checks in the dev
  environment), non-functional quality becomes a shared responsibility, not a
  separate team's concern.

  Best practices: integrate performance, security, accessibility, and
  compliance tests into CI/CD so they run on every change (not just before
  releases); establish NFRs and acceptance criteria at project start alongside
  functional requirements (performance targets, security standards,
  accessibility conformance levels before implementation begins); provide
  developers tools to evaluate non-functional characteristics locally before
  commit (fast feedback loops are essential); treat non-functional test
  failures with the same urgency as functional failures (a performance
  regression or security vulnerability is as much a defect as a broken
  feature); do not wait for a dedicated "performance testing phase" or "security
  audit" — these activities should be continuous, not periodic; use
  lightweight representative performance benchmarks during development and
  reserve comprehensive testing (full production-like environments and data
  sets) for integration and pre-release stages.

### Performance testing

- **Non-functional requirements MUST have well-defined acceptance criteria,
  typically defined as metrics and thresholds.**

  Performance testing evaluates whether the system meets its NFRs under normal
  operational conditions. Key metrics:

  - **Response time** — how long to respond, measured at specific percentiles
    (p50, p95, p99) rather than averages, since averages hide tail latency.
  - **Throughput** — transactions/requests per unit time.
  - **Resource utilization** — CPU, memory, disk I/O, network bandwidth during
    operation. High utilization under normal load may indicate capacity risks.
  - **Error rate** — proportion of requests that result in errors under load. A
    system may appear fast while silently failing a percentage of requests.

  Performance tests serve a _verification_ role (confirm the system meets
  targets before release) and a _monitoring_ role (track trends over time,
  providing early warning of gradual degradation — _performance drift_ — that
  functional tests won't catch).

- **Establish baseline measurements; use soak and spike testing.**

  _Baseline testing_ establishes reference measurements under known conditions
  (a defined number of concurrent users, representative data, specific
  infrastructure config); all subsequent evaluations compare against the
  baseline — without baselines, you cannot determine whether performance is
  improving or degrading. _Soak testing_ (endurance testing) runs under
  sustained load for hours or days to expose problems that only emerge over
  time (memory leaks, connection-pool exhaustion, log file growth, gradual
  resource depletion). _Spike testing_ subjects the system to sudden dramatic
  load increases then equally sudden decreases, revealing behavior under
  unexpected surges and whether it recovers gracefully when the spike subsides.

- **Performance testing best practices.**

  Define requirements as specific, measurable targets (eg. "p95 response time
  under 200ms at 500 concurrent users") — not vague aspirations like "the
  system should be fast." Simulate realistic user behavior patterns and
  transaction volumes (synthetic benchmarks that don't reflect real usage give
  misleading results). Conduct testing in environments mirroring production
  infrastructure (differences in hardware, network topology, or data volume
  invalidate results). Establish baselines early and track over time to detect
  gradual degradation. Automate and integrate into CI/CD to catch regressions
  early. Use percentile-based metrics (p95, p99) — a system with an average of
  100ms may have a p99 of 5 seconds, a serious problem the average conceals.
  Include soak tests in the regular cadence, not just before major releases
  (resource leaks often take hours to manifest). Monitor all layers during
  tests — application, database, network, infrastructure — to identify where
  bottlenecks occur.

### Capacity testing

- **Capacity is a requirement like any other and MUST be specified and tested.**

  Also known as load testing — evaluates whether the system continues to meet
  performance requirements under increasing load, and determines the maximum
  workload it can handle while maintaining acceptable performance. Capacity
  encompasses not only concurrent requests/users but also batch record
  processing volumes, file upload/download sizes, message queue depths, and
  data storage limits. The purpose is to understand operational limits _before_
  users discover them in production. Variations:

  - **Volume testing** — performance when processing large datasets (bulk
    imports, large query results, high-volume event streams, significantly
    grown databases). Reveals whether data handling remains efficient at
    scale.
  - **Stress testing** — pushes the system beyond designed operational
    capacity. The purpose is not to verify that it works under overload (it is
    expected not to) but to understand _how_ it fails: does it degrade
    gracefully, shedding non-essential work while maintaining core
    functionality, or fail catastrophically (corrupting data, becoming
    unresponsive)? Reveals which components are most sensitive to load and
    should be prioritized for optimization.
  - **Rate-limit testing** — verifies correct enforcement of configured rate
    limits. For API providers, confirms that clients exceeding thresholds
    receive appropriate throttling responses (typically HTTP 429). For API
    consumers, understanding behavior when rate-limited by upstream services.
    Achieving consistent results at high request rates often requires
    distributed load generation (a single machine may not produce sufficient
    concurrency due to CPU-core and network-latency constraints).

- **Capacity testing best practices.**

  Establish baseline metrics under normal conditions before beginning (without
  baselines, results have no meaningful reference point). Increase load
  incrementally to identify the precise points where performance starts to
  degrade (sudden jumps from low to extreme load make it difficult to pinpoint
  the threshold). Design scenarios reflecting anticipated growth (test against
  projected load for six months or a year ahead, not just today's load).
  Monitor all system components during testing (application servers,
  databases, caches, message queues, network infrastructure — bottlenecks may
  appear in unexpected places). Test recovery behavior after overload (verify
  the system returns to normal performance when load reduces, without manual
  intervention). For rate-limit testing, verify both enforcement and behavior
  when limits are reached (error responses should be informative; the system
  should recover immediately once the rate drops below the threshold). Feed
  results directly into infrastructure planning and auto-scaling
  configuration.

### Scalability testing

- **Scalability testing evaluates the system's ability to accommodate
  increasing workloads by adding resources — and to release them when demand
  subsides.**

  Where capacity testing determines the limits of a fixed configuration,
  scalability testing determines how effectively the system can grow beyond
  those limits. Two fundamental approaches:

  - **Horizontal scaling** (scaling out) — adding more instances to distribute
    load. RECOMMENDED for web services and cloud-native applications (offers
    theoretically unlimited growth and avoids single points of failure).
  - **Vertical scaling** (scaling up) — increasing the resources (CPU, memory,
    storage) available to a single instance. Simpler to implement but has hard
    hardware-defined limits and provides no redundancy.

  Most modern systems are designed for horizontal scalability, but few are
  truly scalable in practice without deliberate architectural choices — state
  management, session affinity, database contention, and shared resource
  locking can all prevent horizontal scaling even when the infrastructure
  supports it.

- **Evaluate scalability across four dimensions.**

  - **Provisioning speed** — how quickly new instances come online when demand
    increases. With auto-scaling, the lag between a spike and the availability
    of new capacity. A system that takes ten minutes to scale while traffic
    doubles every two minutes will still suffer outages despite auto-scaling.
  - **Scaling efficiency** — whether adding resources produces a proportional
    capacity increase. If doubling instances increases throughput by only 30%,
    the system has a scaling bottleneck (often in shared infrastructure like
    databases, caches, or message brokers).
  - **Scale-down behavior** — whether the system can safely reduce capacity
    when demand drops. Poorly designed scale-down can interrupt in-flight
    requests, break active connections, or leave orphaned resources consuming
    budget.
  - **Data scalability** — whether the data layer scales alongside the
    application. Adding application instances is futile if all contend for the
    same database connection pool. Data partitioning, read replicas, and
    distributed caching are common solutions, but they MUST be tested under
    realistic conditions.

- **Scalability testing best practices.**

  Design tests around realistic growth scenarios (projected increases in
  users, transactions, data volume, geographic distribution). Test
  auto-scaling by generating load patterns that trigger scaling events and
  measure the time from trigger to new-capacity availability. Verify scaling
  efficiency by measuring throughput at increasing instance counts and
  plotting results to identify the point of diminishing returns. Test
  scale-down as rigorously as scale-up (verify active connections drain
  gracefully and no data is lost during instance removal). Include the data
  layer (the application tier and data tier must scale together; testing only
  the application tier gives a false picture). Test under conditions reflecting
  production topology — including network latency between zones/regions, load
  balancer configuration, and DNS propagation delays.

### Security testing

- **Security testing MUST be integrated throughout the development lifecycle,
  not reserved for a pre-release audit.**

  Security is not a feature that can be tested at the end and bolted on.
  Security requirements are architecturally significant, cross-cutting concerns
  influencing decisions at every layer — from infrastructure configuration and
  network topology through application logic and UI design. The goal is to
  identify weaknesses that could be exploited _before_ an attacker does. Scope:
  authentication, authorization, data protection, input validation, session
  management, vulnerability management.

- **Use multiple security testing categories.**

  - **Vulnerability scanning** — automated tools identifying known
    vulnerabilities in code, configuration, and dependencies. Includes SAST
    (static application security testing — analyzes source code without
    executing it) and DAST (dynamic application security testing — probes the
    running application for exploitable weaknesses). Neither alone is
    sufficient: SAST catches issues unreachable at runtime; DAST catches issues
    that only manifest during execution.
  - **Penetration testing** — simulates real-world attacks, applying creative
    adversarial thinking to discover vulnerabilities automated tools miss.
    Black-box (no knowledge of internals), white-box (full access to source and
    architecture), or gray-box (partial knowledge). RECOMMENDED that critical
    systems undergo regular penetration testing by qualified security
    professionals.
  - **Dependency scanning** — identifies known vulnerabilities in third-party
    libraries and components. Modern applications rely heavily on open-source
    dependencies and new vulnerabilities are disclosed regularly; automated
    dependency scanning integrated into CI/CD ensures prompt detection.
  - **Authentication and authorization testing** — verifies access control:
    users can only access resources they are entitled to, privilege escalation
    is not possible, authentication cannot be bypassed. Includes password
    policies, MFA, token management, session handling.
  - **Data protection testing** — verifies sensitive data is encrypted in
    transit (TLS) and at rest, encryption keys are managed securely, and data
    is not inadvertently exposed through logs, error messages, or API
    responses.

- **Security testing best practices.**

  Conduct security testing throughout the lifecycle (automated vulnerability
  scanning on every build). Use a combination of automated scanning and manual
  penetration testing (automated provides breadth; manual provides depth and
  creative adversarial thinking). Test all access control mechanisms
  (authentication, authorization, session management, API keys) — verify
  positive cases (authorized access works) and negative cases (unauthorized
  access is denied). Verify sensitive data is encrypted in transit and at rest,
  and that algorithms and key lengths meet current standards. Include
  dependency scanning in CI/CD and establish a policy for how quickly known
  vulnerabilities must be remediated based on severity. Follow established
  frameworks (the [OWASP Testing Guide](https://owasp.org/www-project-testing-guide/)
  and the [OWASP Top 10](https://owasp.org/www-project-top-ten/)) for
  structured, comprehensive coverage. Verify error messages and logs do not
  expose sensitive internals (stack traces, database schemas, internal paths,
  configuration details). Engage security specialists for critical systems and
  penetration testing — security testing requires a different mindset from
  functional testing.

### Accessibility testing

- **Accessibility testing verifies the system is usable by people with
  disabilities — a legal requirement in many jurisdictions and a fundamental
  quality attribute.**

  Evaluates compliance with standards such as the
  [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/WAI/standards-guidelines/wcag/),
  Section 508, and the European Accessibility Act. These define specific
  testable success criteria across conformance levels (A, AA, AAA), with Level
  AA the most widely adopted target. A system that excludes a significant
  portion of its potential users is not fit for purpose.

- **Automated tools are a first pass only; manual testing with assistive
  technology is essential.**

  Automated scanners detect many common issues (missing alt text, insufficient
  color contrast, missing form labels, incorrect heading hierarchy) but
  cannot evaluate the actual experience of using the system with assistive
  technology. A page may pass every automated check and still be unusable for a
  screen reader user if the reading order is illogical, interactive elements
  are poorly labeled, or focus management is broken. Address multiple
  categories of impairment:

  - **Visual impairments** — test with screen readers (NVDA, JAWS, VoiceOver),
    screen magnifiers, and high-contrast modes. Verify all content and
    functionality is available without visual perception.
  - **Motor impairments** — test all functionality using keyboard-only
    navigation. Verify logical focus order, that all interactive elements are
    reachable, and that there are no keyboard traps.
  - **Auditory impairments** — verify audio content has captions or
    transcripts, and that sound-conveyed information is also conveyed
    visually.
  - **Cognitive impairments** — evaluate clarity of language, consistency of
    navigation, predictability of interactions, and availability of error
    prevention and recovery mechanisms.

- **Accessibility testing best practices.**

  Test with real assistive technologies (screen readers, keyboard-only
  navigation, voice control, screen magnifiers) — not just automated
  scanners. Integrate automated scanners into CI/CD as a first pass, but
  manual testing with assistive devices is essential for evaluating the actual
  user experience. Include users with disabilities in usability testing where
  possible (no amount of expert evaluation substitutes for real user
  feedback). Address accessibility from the start of the design process
  (retrofitting is significantly more expensive than building it in). Establish
  a target conformance level (eg. WCAG 2.1 Level AA) and treat failures
  against that level as defects that block release. Test across multiple
  assistive-technology and browser combinations (screen reader behavior varies
  significantly across platforms). Document accessibility requirements and
  results as part of the standard QA process, not as a separate activity.

### Usability testing

- **Usability testing assesses ease of use, intuitiveness, and overall user
  experience — inherently human-centered and not fully automatable.**

  Evaluates whether users can accomplish their goals effectively, efficiently,
  and with satisfaction, without extensive training or assistance. Cannot be
  fully automated because it depends on observing real users interacting with
  the system and interpreting their behavior, frustrations, and mental models.
  Automated tools can measure proxies (page load times, click depths, error
  frequencies) but cannot evaluate whether a user feels confident, confused,
  or frustrated. Usability is often treated as subjective and untestable —
  this is a mistake; it can and should be measured with concrete metrics:

  - **Task completion rate** — can users accomplish what they set out to do?
  - **Time on task** — how long it takes (improving over time suggests the
    interface is learnable).
  - **Error rate** — how often users make mistakes and how easily they
    recover.
  - **Learnability** — how quickly new users become productive.
  - **User satisfaction** — measured through standardized questionnaires such
    as the System Usability Scale (SUS).

- **Usability testing is most effective when conducted early and iteratively.**

  Testing prototypes, wireframes, or partial implementations reveals design
  problems before they become entrenched in code — usability problems are far
  cheaper to fix in wireframes than in production code. Best practices:
  recruit participants representing actual target users (not developers or
  testers — internal team members have fundamentally different mental models);
  observe users completing realistic tasks without guidance or assistance
  (the tester's role is to observe and record, not to coach); measure both
  quantitative metrics and qualitative feedback (interviews, think-aloud
  protocols, satisfaction surveys); test early prototypes and wireframes;
  conduct iteratively (test, improve, test again — a single round is not
  sufficient); do not conflate usability with visual aesthetics (a visually
  appealing interface may still be difficult to use; a plain one may be highly
  effective).

### Compliance testing

- **Compliance testing verifies adherence to industry standards, regulatory
  requirements, organizational procedures, and contractual obligations.**

  Acceptance criteria are defined _externally_ — by regulators, standards
  bodies, or contractual agreements — not by the development team or product
  owners. Compliance is not negotiable, and partial compliance is often as
  unacceptable as non-compliance. Consequences of non-compliance can be severe
  (financial penalties, legal action, loss of operating licenses, reputational
  damage). Treat compliance requirements with the same rigor as the most
  critical functional requirements — failures SHOULD block releases, and
  evidence of compliance SHOULD be maintained systematically. Dimensions:

  - **Regulatory compliance** — laws and regulations applicable to the domain
    and jurisdiction (GDPR, HIPAA, PCI DSS for payment processing).
  - **Standards compliance** — industry standards (ISO 27001, SOC 2,
    domain-specific frameworks).
  - **Contractual compliance** — specific requirements in customer or partner
    agreements.
  - **Internal compliance** — organizational coding standards, architectural
    guidelines, operational procedures.

- **Compliance testing best practices.**

  Identify all relevant standards, regulations, and guidelines early in the
  project lifecycle (capture as part of initial requirements analysis, not
  discovered during pre-release audits). Create compliance checklists mapped
  to specific requirements and maintain traceability between those
  requirements and the test cases that verify them. Engage compliance experts
  or auditors when testing against complex regulations (development teams
  should not be solely responsible for interpreting regulatory requirements).
  Document compliance evidence thoroughly for audit purposes (automated test
  reports supplement manual documentation). Treat compliance requirements as
  first-class acceptance criteria — compliance failures MUST block releases,
  just as critical functional test failures do. Automate compliance checks
  where possible (particularly standards compliance and internal coding
  standards) and integrate them into CI/CD.

### Recovery testing

- **Recovery testing verifies the system's ability to recover from failures and
  resume normal operation with minimal data loss and downtime.**

  Covers hardware faults, software crashes, network outages, and data
  corruption; validates backup/restore procedures, failover mechanisms, and
  disaster recovery plans. Closely related to resilience and overlaps with
  chaos testing (see [TS-13](../013/AGENTS.md)) — where chaos testing
  proactively introduces failures to discover unknown weaknesses, recovery
  testing validates that _known_ recovery procedures work correctly and meet
  their defined objectives. Every system that matters will eventually fail;
  recovery testing turns the response from a hope into a verified capability.

- **RTO and RPO targets MUST be defined as explicit requirements and tested
  against.**

  - **Recovery Time Objective (RTO)** — the maximum acceptable time to restore
    service after a failure. A business-driven metric: how long can the
    organization tolerate the system being unavailable?
  - **Recovery Point Objective (RPO)** — the maximum acceptable amount of data
    loss, measured in time. An RPO of one hour means the organization can
    tolerate losing up to one hour of data.

  A backup strategy that produces backups every 24 hours cannot meet an RPO of
  one hour. Best practices: simulate realistic failure scenarios (power loss,
  network interruption, storage failures, process crashes, data corruption);
  verify data integrity is maintained during and after failures (partial
  writes and in-flight transactions handled atomically — the system should not
  silently lose or corrupt data); test backup and restore procedures
  regularly under various failure conditions, not just once during initial
  setup (backups that have never been tested are not backups — they are
  assumptions); measure actual RTO and RPO against defined targets and report
  deviations as defects; document recovery procedures clearly for operations
  teams (procedures should be executable by on-call staff under pressure, not
  just by the engineers who designed them); test failover mechanisms for
  high-availability systems (automatic, manual, and failback — verify
  seamless-to-users failover with no data loss); test recovery from partial
  failures, not just complete outages (a single failed DB replica, a lost
  inter-zone network link, a corrupted cache should not require full system
  recovery).

### Installation and compatibility testing

- **Installation testing validates that installation, upgrade, and
  uninstallation procedures work correctly across all supported
  configurations.**

  Verifies users can deploy and configure the system without errors that
  block adoption. Closely related are _compatibility testing_ (verifies
  correct behavior across different combinations of hardware, operating
  systems, browsers, network configurations, and other environmental
  variables — post-installation behavior across diverse environments) and
  _configuration testing_ (verifies correct behavior under different
  configuration options including minimal, recommended, and non-default
  settings; testing the effect of adding or modifying resources such as
  memory, disk space, CPU allocation). These three share a common focus: the
  system working correctly not just in the development team's environment, but
  in the varied environments where it will actually be deployed and operated.

- **Installation, compatibility, and configuration testing best practices.**

  Test installation on clean systems representing minimum, recommended, and
  various realistic deployment configurations. Verify prerequisites are
  clearly documented and validated during installation (where possible, the
  installer should check for prerequisites and provide clear feedback when not
  met). Test upgrade paths from previous versions including data migration and
  configuration preservation (users should not lose data or settings when
  upgrading). Validate that uninstallation leaves the system in a clean state
  (no orphaned files, services, or configuration entries). Document and test
  configuration options systematically (ensure installation and configuration
  logs provide sufficient detail for troubleshooting). For compatibility
  testing, define a support matrix of target environments and test each
  combination systematically (automate cross-browser and cross-platform
  testing where possible). For web applications, test across the full range of
  supported browsers, operating systems, and device form factors (rendering
  differences, JavaScript engine variations, and API availability can all
  cause compatibility issues).

## References

- [TS-14 source](README.adoc)
- [TS-10: Releasing](../010/AGENTS.md)
- [TS-13: Functional Testing](../013/AGENTS.md)
- [OWASP Testing Guide](https://owasp.org/www-project-testing-guide/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)