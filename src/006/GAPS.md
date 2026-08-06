# TS-6 gap analysis

Gaps found comparing TS-6: *Distributed System Design* against the following
reference resource:

- https://12factor.net/concurrency (Factor VIII: Concurrency, "The Twelve-Factor
  App", Adam Wiggins, 2017)
- https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/
  (Jeff Hodges, "Notes on Distributed Systems for Young Bloods", 2013)

**Assessment.** TS-6 is currently an unwritten stub — its `README.adoc` contains
only a title, a `// TODO` marker, and a table-of-contents macro with no included
content files. There is nothing to compare the reference material against, so
every claim in the Concurrency factor is "missing" in the trivial sense that the
whole standard is missing. This is recorded as a single Unresolved item rather
than as a list of Missing gaps, since itemizing gaps against a blank page adds
no information beyond "write this standard."

The Concurrency factor's subject matter — scaling an application horizontally
via a process model, with distinct process types for distinct workloads — is
squarely inside TS-6's stated scope (distributed system design) and would be a
reasonable anchor for the standard's first content. Related material already
exists elsewhere: TS-5 (`../005/06-services.adoc`) covers microservices,
reactive/event-driven services, and CQRS, which are adjacent but distinct
concerns (service decomposition, not process-level concurrency within a single
deployable). TS-49 (`../049/`) covers platform-level environment lifecycle but
not the app-level process model.

**Status:** First run, 2026-08-05. All gaps open.

**Second run, 2026-08-06.** Re-run against Jeff Hodges' "Notes on Distributed
Systems for Young Bloods"
(https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/).
Eleven of its 18 points were routed to TS-6. TS-6 remains an unwritten stub,
so none are itemized as Missing/Partial; instead the routed topics are added
to the Writing backlog below for when the standard is authored.

## Missing

(Not itemized — see Unresolved.)

## Partial

(None — there is no existing content to be partial against.)

## Out-of-scope

(None identified in this run.)

## Writing backlog

Topics routed to TS-6 from assessed references, to be covered when the
standard is authored (then re-run this gap analysis for real Missing/Partial
findings):

- **Processes & concurrency** (12factor Concurrency): processes as
  first-class citizens; the Unix process model assigning distinct process
  *types* to distinct workloads; horizontal scaling by running more
  processes; processes MUST NOT daemonize or write PID files; lifecycle
  delegated to an external process manager; share-nothing, horizontally
  partitionable processes.
- **Design for failure / partial failure** (Hodges P1): networked systems
  fail more than single-machine systems; failures tend to be partial, not
  total; design for failure.
- **Cost of robustness** (Hodges P2): robust distributed systems cost more
  to build and test; some failures only occur with many machines; actual
  (not simulated) distribution is needed to flush out bugs.
- **Scarcity of robust open source distributed systems** (Hodges P3) —
  socio-economic observation (cost of running many machines burdens OSS
  communities; corporate-backed OSS priorities may misalign); borderline
  out-of-scope for a design standard.
- **Coordination is hard** (Hodges P4): avoid coordinating machines;
  horizontal scalability is really independence; minimise communication and
  consensus; Two Generals and Byzantine Generals problems; Paxos is hard.
- **In-memory is trivial** (Hodges P5): single-machine problems are easy;
  single-machine efficiency tricks don't transfer across the network.
- **Backpressure** (Hodges P7): signaling failure from serving to
  requesting system; bounding resource use; drop messages / ship errors
  back; timeouts and exponential backoff; prevents cascading failure and
  message loss.
- **Partial availability** (Hodges P8): return some results when parts
  fail; time-budgeted search; failure domains; "down for a few users" vs
  "missing data for many" trade-off.
- **ID space design** (Hodges P13): the chosen ID space shapes
  partitioning and consumption; encoding information in IDs;
  auto-increment crawl and de-anonymization hazards.
- **Data-locality** (Hodges P14): co-locate processing/caching with
  persistent storage; coalesce near-simultaneous requests in time and
  space. (Note: also relevant to TS-46.)
- **Single-machine capability** (Hodges P16): a single machine is far
  more capable than assumed; profile and optimise before prematurely
  distributing.
- **CAP as a critique tool** (Hodges P17): use the CAP theorem to
  critique/iterate a design and understand trade-offs, not as a first
  principle to build from; out of C, A, P you cannot choose CA.

## Unresolved

- [ ] TS-6 has no content to analyze. https://12factor.net/concurrency's core
      claims — processes as first-class citizens; the Unix process model
      assigning distinct process *types* to distinct workloads (eg. a web
      process type and a worker process type); horizontal scaling by running
      more processes, potentially across multiple physical machines; processes
      MUST NOT daemonize or write PID files; process lifecycle (starting,
      stopping, output capture, crash recovery, restarts) delegated to an
      external process manager (systemd, a cloud platform's process
      supervisor, or a tool like Foreman) rather than self-managed; and
      processes MUST be share-nothing and horizontally partitionable — would
      make a reasonable first section for this standard once it is authored.
      Recommend the user prioritize writing TS-6's baseline content (possibly
      starting from this reference), after which this gap analysis should be
      re-run to produce real Missing/Partial findings.
