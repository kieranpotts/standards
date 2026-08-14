# GAPS — TS-38 Node.js applications

**Status:** 1 of 1 gap resolved (2026-08-14). TS-38 has been authored from
scratch — six new content partials plus an introductory paragraph and a
`== References` section on the page — and its one recorded gap closed
against the new content.

---

## Stateless Node.js services for horizontal scaling

- **Source**: https://newsletter.pragmaticengineer.com/p/bluesky-engineering-culture
- **What the source says**: Bluesky runs its TypeScript backend on Node.js and worked around Node's single-threaded model by building stateless services that scale horizontally — running ~192 Node processes behind HAProxy at ~1% CPU each.
- **Coverage check**: TS-38 is a stub with no content.
- **Gap**: No guidance on the stateless-service / horizontal-scaling pattern for Node.js applications.

**RESOLVED.** Closed by `06-stateless-scaling.adoc`, "Stateless scaling"
section. Explains why Node's single-threaded event loop rules out
in-process multi-threading as a scaling strategy, states the horizontal
scaling pattern (many identical stateless processes behind a load
balancer) and the statelessness requirement it depends on, cites the
Bluesky/Pragmatic Engineer example (~192 processes behind HAProxy at ~1%
CPU each) as the source, and covers the `cluster` module's narrower role
versus letting a process orchestrator own multi-process scheduling.
Cross-references TS-6 (Distributed system design) for the underlying
statelessness/idempotency principles and TS-49 (Cloud platform
engineering) for the orchestration platform's role. Source added to the
page's `== References`.
