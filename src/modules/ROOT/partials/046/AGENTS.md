# TS-46: Distributed Data and Caching

Best practices for distributed data and caching in software systems.
General guidance, not specific to any particular technology or
application layer.

**Distributed data** is data spread across, or replicated between, multiple
locations (different services, databases, processes, machines) rather than
living in a single authoritative store. We distribute data to make systems
faster, more available, and more scalable — but once the same data exists
in more than one place we inherit consistency problems: keeping copies
consistent, deciding which copy is authoritative, and reconciling
concurrent changes.

**Caching** is one objective of distributed data: a deliberately placed
copy of data positioned closer to where it's needed so it can be read
faster or more cheaply than fetching from its source. Caching trades
single-source simplicity for performance and inherits the consistency
problems that come with it. Most caching bugs come from bad cache design,
not from the underlying technology.

Use this when designing, implementing, or reviewing distributed data
systems or caching layers.

Do NOT use this for database engine or schema specifics — see
[TS-43: Relational Databases and SQL](../043/AGENTS.md) and
[TS-44: Non-Relational (NoSQL) Databases](../044/AGENTS.md). For broader
distributed-system design concerns, see
[TS-6: Distributed System Design](../006/AGENTS.md). For application
architecture, see [TS-5: Application Architecture](../005/AGENTS.md).

## Rules

### Caching tradeoffs

- **Have clear, documented reasons for every caching layer.** Caching has
  real costs: harder debugging and code profiling; users see outdated
  information; increased memory footprint (caching moves resource
  utilization, it doesn't reduce it); increased system complexity. The
  reasons for implementing a caching layer MUST be clearly defined and
  documented.

### Factors for caching

- **Evaluate candidates against these factors before implementing a
  cache.** These factors decide whether a given piece of data is a good
  candidate for caching specifically (distributing it as a read-optimized
  copy):
  - **Data access frequency.** Rarely accessed data may not benefit;
    frequently hit data (by the same user or across many clients) may be
    worth caching.
  - **Cost of data access.** Not all reads are equal. Reads that hit
    external services, multiple databases, join several tables, or
    compute summaries are expensive and good cache candidates. A flat
    record lookup by primary key against a well-indexed table is already
    cheap and likely not worth caching.
  - **Data stability.** Stable data makes a great cache — it can sit for
    a long time without anyone noticing. Volatile data (data that gets
    stale quickly) requires particular attention to cache invalidation.
  - **Data size and complexity.** Big, messy data doesn't belong in fast
    memory: large payloads eat space, increase GC pressure, and slow
    serialization. Small, flat data is faster to work with and easier to
    evict. Caching is a fast-access shelf, not cold storage — store what
    fits, what you'll grab often and quickly. Caching is kept fast by
    storing simple shapes against small keys.
  - **Impact on user experience.** Not all latency matters; when it does,
    it tends to matter a lot. Anything on the critical path of a user
    interaction (loading a web page, rendering a component, hitting
    "submit") should feel instant — if caching makes that possible, use
    it. A 2 AM background sync task is probably not worth caching.
  - **Safeness.** Fast is good; leaky is not. Caching user-specific or
    sensitive data (PII, tokens, financials) without scoping or
    encryption is a security risk. Mitigations: use per-user or
    per-session cache keys; encrypt values where possible; set short
    TTLs for sensitive data. Heuristic: if it can't go in a log file, it
    probably shouldn't go in a cache either.
  - **Scalability.** Caching that works for 1,000 users can still
    collapse for 1 million. Unbounded keys, high churn, or poorly managed
    TTLs can overwhelm memory, reduce hit ratios, and cause eviction
    storms. Tactics: use eviction policies (LRU, LFU); set size limits;
    monitor hit/miss ratio and eviction churn.

### Evaluating a cache

- **Cache what is used frequently, expensive to fetch, stays valid long
  enough, and improves something a user can actually feel. Do NOT cache
  what you can't keep safe or what won't scale.**

- **Rough value calculation:**

  ```
  cache value = access frequency × retrieval cost × stability
  ```

  If any of access frequency, retrieval cost, or data stability are near
  zero, caching that data won't give much back. If all three are high,
  it's a high-leverage cache opportunity.

- **Every cache key MUST justify its existence.** If you can't explain
  why something is in a cache, it probably shouldn't be. Every cache key
  is a liability.

- **Design each cache with the same intent as a database schema or API
  contract.** Caches are a deliberate, visible part of the architecture,
  with trade-offs, constraints, and clear justification. Caching works
  best when it's boring, predictable, scoped, and justified.

### Cache freshness

- **Two main options for keeping cached data fresh:**
  - **Time-to-Live (TTL).** Expires the cache after a fixed time.
  - **Invalidation.** Explicitly remove or update the cache when the data
    changes.

- **Choose the freshness strategy based on data profile:**
  - Stable data + frequent reads → use TTL.
  - Stable data + infrequent reads → avoid TTL (wasteful).
  - Volatile data + frequent reads → use invalidation.
  - Volatile data + infrequent reads → avoid caching altogether.

### Distributed writes

- **Three ways databases handle concurrent writes to the same data.**
  Distributed writes mean several clients may try to update the same data
  at the same time. The three designs:

  1. **Write-ahead logging (WAL)** — used by PostgreSQL and MySQL. The
     change is written ahead to a log before being applied to the
     database. Safe and durable; non-blocking (no ongoing write blocks
     another). Does not properly handle concurrent write conflicts —
     updates are applied in the order the write logs are written. Down
     side: overhead of monitoring the logs.

  2. **Locking (pessimistic concurrency)** — used by traditional RDBMS.
     The writer acquires a lock on the record; other writers are blocked
     until the lock is released. Prevents conflicting updates; strong
     consistency; easy to reason about. Poor fit for high-throughput
     distributed systems due to blocking operations, risk of deadlocks,
     high latency, and poor scalability.

  3. **Versioning (optimistic concurrency)** — used by DynamoDB,
     Cassandra, and the Event Sourcing pattern. Locks are replaced with
     version checks: client reads version N, then writes with condition
     "version = N" (a **conditional write**). The write succeeds only if
     the version still matches. No blocking of new connections, so it
     scales well and supports high throughput. Clients assume no
     conflicts by default but handle them gracefully when they occur,
     preventing silent overwrites (only one writer succeeds per
     version, eliminating "last write wins" chaos). Main downsides are
     client-side: conflicts are made visible and clients require more
     logic to deal with them.

## References

- [TS-46: Distributed Data and Caching (source)](../../pages/046.adoc)
- [TS-5: Application Architecture](../005/AGENTS.md)
- [TS-6: Distributed System Design](../006/AGENTS.md)
- [TS-43: Relational Databases and SQL](../043/AGENTS.md)
- [TS-44: Non-Relational (NoSQL) Databases](../044/AGENTS.md)