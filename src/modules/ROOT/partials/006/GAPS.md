# GAPS — TS-6 Distributed System Design

> **Note**: This standard is currently a stub (`// TODO` only). All points below are gaps because the standard has no written content. Several gaps that also belong here are recorded in the GAPS.md files of their primary standards (see cross-references below).

---

## When systems defy understanding — switch to empirical/observability methods

- **Source**: https://blog.nelhage.com/post/computers-can-be-understood/
- **What the source says**: For distributed systems, "big balls of mud," heterogeneous client-side JavaScript, and deep learning, in-depth understanding is impractical; the right strategy is empiricism — observe the running system, treat behavior statistically, and invest in fault-tolerance rather than root-causing every component failure.
- **Coverage check**: TS-6 is a stub. TS-57 covers observability mechanics but not the meta-principle of when to abandon deductive understanding for empirical methods.
- **Gap**: No standard frames the decision of when a system is too complex to reason about deductively and must be probed empirically, nor the distributed-systems guidance to prioritize system-level resilience over root-causing individual failures.
- **Cross-references**: TS-57 (Logging, Monitoring, Observability)

---

## Service mesh, microservice contracts, and shared library upgrades at scale

- **Source**: https://blog.allegro.tech/2024/04/ten-years-microservices.html
- **What the source says**: Migrating to a service mesh let Allegro control cross-cutting behavior (mTLS, service discovery) centrally; a written "Microservice Contract" defines required behaviors; updating a shared library across 1000+ services is slow, motivating automated upgrades.
- **Coverage check**: TS-6 is a stub. No matches for "service mesh" or "microservice contract" anywhere in `src/`.
- **Gap**: No standard covers service mesh, microservice contracts, or the common-library-vs-infrastructure tradeoff and library-upgrade-at-scale problem.
- **Cross-references**: TS-49 (Cloud Platform Engineering)

---

> Additional gaps that belong in TS-6 (when written) are recorded in: `src/modules/ROOT/partials/005/GAPS.md` (microservices prerequisites, service sizing, monolith-to-microservices migration execution, SOLID at service level, continuous technology re-evaluation).