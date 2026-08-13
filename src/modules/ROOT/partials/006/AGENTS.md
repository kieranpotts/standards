# TS-6: Distributed System Design

This is a compact version of technical standard TS-6 for AI agents.

Use this when designing or reviewing a system composed of multiple
independently deployable components that communicate over a network:
consistency/availability trade-offs, consensus, delivery semantics,
distributed transactions, service topology, system-level resilience, and
running a large service fleet.

Do NOT use this for a single application's internal architecture — use
[TS-5: Application Architecture](../005/AGENTS.md) for that. For the
mechanics of keeping distributed *data* consistent (WAL, locking,
versioning), see [TS-46](../046/AGENTS.md). For individual network-call and
message design, see [TS-20](../020/AGENTS.md) and [TS-23](../023/AGENTS.md).
For the surrounding platform, see [TS-49](../049/AGENTS.md). For
observability mechanics, see [TS-57](../057/AGENTS.md). For the data-move
half of a service extraction, see [TS-45](../045/AGENTS.md).

## Rules

### Fundamentals

- **Treat every call to another component as one that can fail slowly,
  fail silently, fail partially, or succeed after the caller has given
  up.** Partial failure — one component fails while others keep running,
  and the survivors cannot always tell a crash from a slow response from a
  lost message — is the central problem of distributed systems.

- **Design against the eight fallacies of distributed computing** (Deutsch
  and Gosling): the network is reliable; latency is zero; bandwidth is
  infinite; the network is secure; topology doesn't change; there is one
  administrator; transport cost is zero; the network is homogeneous. A
  component not reviewed against all eight has not been reviewed for
  production readiness.

- **Once a system is too complex to reason about deductively, switch
  strategy rather than push harder on the same one:** invest in empiricism
  (observe the running system) over deduction; treat behavior
  statistically (track failure rates, not every individual failure); and
  prioritize system-level resilience (tolerate the next failure mode) over
  root-causing every past one.

### Consistency and availability

- **Every distributed data set MUST have an explicit, documented CAP
  choice**, made per data set, not implicitly by whichever database was
  picked: CP (refuse requests during a partition rather than risk
  inconsistency) or AP (keep serving, accept staleness). A single system
  commonly needs both — CP for a ledger, AP for a catalog.

- **PACELC governs the trade-off outside of a partition too**: else,
  choose between latency and consistency. Strong cross-replica consistency
  requires coordinating before acknowledging a write, which adds latency
  proportional to replica count and distance.

- **Choose the weakest consistency model the use case can tolerate, no
  weaker**, in descending strength: linearizable, sequential, causal,
  eventual. Consistency model and delivery guarantee (at-least-once, etc.)
  are independent axes — evaluate them separately.

### Consensus and coordination

- **Reserve consensus for the small amount of state where getting it
  wrong is unacceptable** (leader election, distributed locks, mesh-wide
  config) — not as the default coordination mechanism. Most application
  state SHOULD be owned by exactly one service/datastore, avoiding the
  need for consensus about it.

- **Size consensus clusters as `2f + 1` nodes to tolerate `f` failures**
  (hence odd-numbered clusters: 3, 5, 7). A cluster that loses its
  majority MUST stop accepting writes.

- **Do not implement Raft or Paxos from scratch.** Use a proven system
  (etcd, ZooKeeper, Consul) or a database with consensus built in.

- **A distributed lock MUST have a lease with an expiry, never an
  indefinite hold.** Where the guarded action isn't idempotent/safe to
  run twice, pair the lock with a monotonically increasing **fencing
  token** that the protected resource checks — the lock alone does not
  guarantee mutual exclusion under process pauses.

- **Prefer optimistic concurrency, idempotent operations, or
  single-writer ownership over consensus** wherever they suffice — reach
  for consensus only after ruling these out.

### Idempotency and delivery semantics

- **Default to at-least-once delivery plus idempotent processing.** True
  exactly-once delivery is not achievable in an asynchronous distributed
  system; what "exactly-once" systems actually provide is at-least-once
  delivery + idempotent processing, giving an exactly-once *effect*.

- **Every retryable operation MUST be made idempotent, or wrapped in a
  mechanism that makes retrying it safe.** Standard mechanism: an
  idempotency key (UUID) sent with every attempt; the receiver returns the
  stored result of the first attempt for a repeated key rather than
  re-executing. Retain keys for a bounded window (eg. 24h), not
  indefinitely.

- **Do not assume ordered delivery unless the transport explicitly
  guarantees it** and the component depends on only that one ordered
  source. Where order matters otherwise, include a sequence number/
  timestamp and handle out-of-order/duplicate delivery explicitly.

### Distributed transactions and sagas

- **Do not use two-phase commit (2PC) as the default cross-service
  consistency mechanism.** It holds locks across every participant for
  the duration and can block indefinitely if the coordinator fails
  mid-decision. Reserve it for a small, tightly controlled participant set.

- **Use the saga pattern for cross-service business operations**: a
  sequence of local transactions, one per service; on failure, run
  compensating transactions for every already-committed step, in reverse
  order. Compensating transactions MUST be idempotent and retryable.
  Choreography (event-driven, decentralized) SHOULD be preferred for
  short sagas (2-3 steps); orchestration (explicit coordinator, centrally
  observable) SHOULD be preferred as length/branching grows.

- **Use the transactional outbox pattern to avoid the dual-write
  problem.** Write the event to an outbox table in the same local
  transaction as the business data; a separate process publishes from the
  outbox with retries, giving at-least-once delivery without a
  distributed transaction between the database and the broker.

### Service topology

- **Use service discovery, not hard-coded addresses** — client-side
  (caller queries a registry and balances itself) or server-side (caller
  hits a fixed address that queries the registry). Default to a
  platform's built-in server-side discovery where available.

- **Use an API gateway at the boundary between external callers and
  internal services** to centralize auth, rate limiting, routing, and TLS
  termination — not between every pair of internal services.

- **Adopt a service mesh once the number of services and the pain of
  keeping cross-cutting behavior (mTLS, retries, circuit breaking)
  consistent across them outweighs its operational cost** (extra proxy
  hop, a control plane that becomes a critical dependency) — not as a
  default starting point for a handful of services.

- **Define an explicit, organization-wide microservice contract**: health
  and readiness endpoints, standard observability output, auth
  expectations, graceful shutdown behavior. Specify required behavior,
  not required implementation — a service MAY satisfy it via a shared
  library or independently.

- **When a shared library's update burden grows faster than it can be
  worked down, move the concern into infrastructure (eg. a service mesh)
  or automate the upgrade across every consuming repo** — don't rely on
  every team to notice and act on a new release.

### Resilience and blast radius

- **Use bulkheads to isolate shared resources (connection/thread pools)
  per dependency**, so one slow dependency cannot exhaust a resource
  shared with healthy dependencies.

- **Apply backpressure explicitly**: bounded queues that reject/shed load
  once full, consumers that pull at their own sustainable rate, and
  producer rate limits informed by observed consumer capacity. An
  unbounded queue is not a safety mechanism.

- **Implement liveness and readiness checks as distinct signals.** A
  failed liveness check SHOULD trigger a restart (process can't recover
  on its own); a failed readiness check SHOULD remove the instance from
  rotation without restarting (may self-recover). Don't conflate them.

- **Choose failure-domain boundaries deliberately** so one failure
  degrades the smallest reasonable portion of the system. Service
  boundaries double as blast-radius boundaries — a good place to trial a
  new language/runtime under real traffic, since a bad outcome is
  contained to one service.

- **Practice chaos engineering regularly**, not only after an incident
  reveals a gap — it verifies the *system* recovers without operator
  intervention, complementing observability game days
  ([TS-57](../057/AGENTS.md)), which verify operators can *diagnose* an
  injected failure.

### Microservices at scale

- **Do not adopt microservices without the infrastructure to run
  them**: a deployment pipeline that makes shipping one more service a
  marginal cost, observability capable of following a request across
  service boundaries, and a team structure that maps to the intended
  boundaries (Conway's law). Weigh the cumulative total cost of ownership
  of many services against the coordination cost of the monolith they'd
  replace.

- **Avoid both sizing failure modes.** Nanoservices: split along a
  technical seam rather than a business capability, so one logical
  operation needs several service calls. Overgrown services: accrete
  unrelated responsibilities until multiple teams are needed to operate
  them safely. Revisit service boundaries periodically as the domain and
  organization change.

- **Apply SOLID at the service level**: single responsibility (one
  business capability per service); open/closed (extensible via
  versioned APIs/flags, not internal modification); Liskov substitution
  (interchangeable implementations behind a stable contract);
  interface segregation (distinct external vs. internal APIs);
  dependency inversion (depend on message contracts/versioned APIs, not
  concrete services — eg. route via a broker).

### Migration execution

- **Use the strangler fig pattern for monolith-to-microservices
  migration**: route an increasing share of traffic through new services
  via a routing layer while the monolith serves the rest; each step is
  small, independently reversible, and delivers value as it lands. Pair
  service extraction's data half with [TS-45](../045/AGENTS.md)'s
  expand-and-contract discipline.

- **Prioritize extraction by boundary stability and isolation**: extract
  stabilized interfaces before ones still under active redesign, and
  components with fewer dependencies before deeply entangled ones. Write
  the sequencing plan down.

- **Run new and old code paths in parallel before cutover where
  correctness matters** (pricing, billing) — compare outputs on real
  traffic silently before switching.

- **Plan a large migration as a multi-year program**: re-prioritize the
  extraction backlog periodically, secure an explicit standing capacity
  allocation from leadership, and keep operating the monolith with full
  care for as long as it still serves live traffic.

### Continuous technology evaluation

- **Adopt new technology only in response to a concrete, current
  problem** — cost, scaling limits, or a genuine new requirement — not
  because an alternative is marginally better.

- **Validate build-vs-buy with a short, real-world proof-of-concept**
  against production-representative data/load rather than a paper
  evaluation or vendor-stated figures alone.

- **Evaluate technology choices against combined technical + business
  criteria**: performance/scalability, cost (including operational cost),
  reliability, support/community maturity, flexibility/interoperability
  with the existing stack.

- **Re-evaluate standing technology choices periodically against the same
  criteria that justified adopting them**, even ones that have worked well
  for years — this is distinct from routine dependency-version
  maintenance ([TS-5](../005/AGENTS.md)). Maintain a living, system-wide
  technology-strategy view so individual service teams' choices
  accumulate toward a coherent direction.

## References

- [TS-6 (source)](../../pages/006.adoc): \
  Read this for the full standard, rationale, and worked examples.

- [Fallacies of Distributed Computing](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing): \
  Read this when reviewing a design against the eight fallacies in detail.

- [Raft paper — Ongaro & Ousterhout](https://raft.github.io/raft.pdf): \
  Read this when implementing or evaluating a consensus system.

- [Pattern: Saga — microservices.io](https://microservices.io/patterns/data/saga.html): \
  Read this when designing a cross-service business transaction.
