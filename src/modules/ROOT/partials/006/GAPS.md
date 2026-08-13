# GAPS — TS-6 Distributed system design

**Status: 2 of 2 gaps resolved (2026-08-11).** TS-6 now has substantive
content. Several gaps that belong here were tracked in other standards'
GAPS.md files instead — see the cross-references below; those have also been
resolved as part of this pass (see `src/modules/ROOT/partials/005/GAPS.md`).

---

## When systems defy understanding — switch to empirical/observability methods

- **Source**: https://blog.nelhage.com/post/computers-can-be-understood/
- **What the source says**: For distributed systems, "big balls of mud," heterogeneous client-side JavaScript, and deep learning, in-depth understanding is impractical; the right strategy is empiricism — observe the running system, treat behavior statistically, and invest in fault-tolerance rather than root-causing every component failure.
- **Coverage check**: TS-6 is a stub. TS-57 covers observability mechanics but not the meta-principle of when to abandon deductive understanding for empirical methods.
- **Gap**: No standard frames the decision of when a system is too complex to reason about deductively and must be probed empirically, nor the distributed-systems guidance to prioritize system-level resilience over root-causing individual failures.
- **Cross-references**: TS-57 (Logging, monitoring, observability)
- **RESOLVED**: Closed by `01-fundamentals.adoc`'s "Reasoning about systems that defy understanding" section. States the switch from deductive to empirical reasoning as a three-part response — invest in empiricism over deduction, treat behavior statistically rather than individually, and prioritize system-level resilience over root-causing every failure — and frames the rest of the standard's resilience patterns (timeouts, retries, circuit breakers, bulkheads, graceful degradation) as what makes that prioritization the default outcome. Cross-references TS-57 for the observability mechanics. Source added to the page's `== References` section.

---

## Service mesh, microservice contracts, and shared library upgrades at scale

- **Source**: https://blog.allegro.tech/2024/04/ten-years-microservices.html
- **What the source says**: Migrating to a service mesh let Allegro control cross-cutting behavior (mTLS, service discovery) centrally; a written "Microservice Contract" defines required behaviors; updating a shared library across 1000+ services is slow, motivating automated upgrades.
- **Coverage check**: TS-6 is a stub. No matches for "service mesh" or "microservice contract" anywhere in `src/`.
- **Gap**: No standard covers service mesh, microservice contracts, or the common-library-vs-infrastructure tradeoff and library-upgrade-at-scale problem.
- **Cross-references**: TS-49 (Cloud platform engineering)
- **RESOLVED**: Closed by `06-service-topology.adoc`. Covers service discovery, API gateways, service mesh (sidecar pattern, mTLS as the canonical centralization example), a RECOMMENDED microservice contract (health/readiness, observability output, auth expectations, graceful shutdown), and the shared-library-at-scale problem (move the concern into infrastructure, or automate the upgrade). Cross-references TS-49 for the surrounding platform and TS-20/TS-57 for the individual cross-cutting concerns a mesh centralizes. Source added to the page's `== References` section.

---

> The additional gaps that belonged in TS-6 (microservices prerequisites, service sizing, monolith-to-microservices migration execution, SOLID at service level, continuous technology re-evaluation) were tracked in `src/modules/ROOT/partials/005/GAPS.md` and are now resolved there, closed by TS-6's `08-microservices-at-scale.adoc`, `09-migration-execution.adoc`, and `10-continuous-technology-evaluation.adoc`.
