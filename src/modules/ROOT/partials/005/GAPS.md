# GAPS — TS-5 Application architecture

Coverage gaps identified by comparing external sources against this standard.

**Status: 6 of 13 gaps resolved (2026-08-11).** The six gaps cross-referenced
to TS-6 (Distributed system design) were closed by that standard now that it
has substantive content. The remaining seven, which belong to TS-5 itself or
to other standards, are still open.

---

## Favor proven, battle-tested technology ("technological sharks")

- **Source**: https://www.simplethread.com/20-things-ive-learned-in-my-20-years-as-a-software-engineer/
- **What the source says**: Old technologies that have survived are "sharks, not dinosaurs" — they solve problems so well they've outlasted change. Don't bet against them; replace them only with a very good reason.
- **Coverage check**: TS-5's dependencies and frameworks content states this narrowly for frameworks ("prefer frameworks with a proven track record of stability and longevity"). There is no general, technology-agnostic articulation of the principle.
- **Gap**: No general statement of the "favor proven, long-surviving technologies; replace only with strong justification" heuristic across all technology choices (databases, languages, protocols, runtimes, message brokers).

---

## Microservices prerequisites, scale thresholds, and total cost of ownership

- **Source**: https://blog.allegro.tech/2024/04/ten-years-microservices.html
- **What the source says**: Microservices require heavy, ongoing investment in infrastructure and tooling; the "glue" between services is not simple. Much anti-microservice sentiment comes from treating them as a silver bullet or ignoring the "you must be this tall" prerequisites.
- **Coverage check**: TS-5's services content notes microservices are "harder to implement well than many teams realize" but does not address infrastructure/tooling investment, scale thresholds, or total-cost framing.
- **Gap**: No guidance on prerequisites, total cost of ownership, or the "right scale required" framing for adopting microservices.
- **Cross-references**: TS-6 (Distributed system design) — stub
- **RESOLVED**: Closed by TS-6's `08-microservices-at-scale.adoc`, "Prerequisites and total cost of ownership" section. States the required infrastructure investment (deployment pipeline, cross-service observability, team structure aligned to boundaries) as a precondition for adopting microservices, and requires weighing the cumulative total cost of ownership of many services against the coordination cost of the monolith they would replace.

---

## Microservice boundaries for safe technology experimentation

- **Source**: https://blog.allegro.tech/2024/04/ten-years-microservices.html
- **What the source says**: Microservices let teams safely experiment with new languages (Kotlin, Scala, Go, Elixir) in production by limiting the blast radius of failures.
- **Coverage check**: TS-49 covers "aligned autonomy" and TS-5 covers independent deployability and bounded contexts, but neither covers using service isolation to trial new languages/stacks in production with contained failure radius.
- **Gap**: No coverage of using service boundaries as a deliberate experimentation / blast-radius-isolation mechanism.
- **Cross-references**: TS-6 (Distributed system design), TS-49 (Cloud platform engineering)
- **RESOLVED**: Closed by TS-6's `07-resilience-and-blast-radius.adoc`, "Blast radius and failure domains" section. States that service boundaries double as failure-domain boundaries, making them a practical place to trial a new language, framework, or runtime under real production traffic with the resulting risk contained to one service.

---

## Service sizing — the nanoservice trap and overgrown services

- **Source**: https://blog.allegro.tech/2024/04/ten-years-microservices.html
- **What the source says**: Going too small ("nanoservices") causes debugging and distribution-overhead pain; going too big recreates monolith problems; 1000+ services carry cumulative overprovisioning cost.
- **Coverage check**: TS-5 covers the too-early extraction problem ("premature decomposition") but says nothing about the too-small end, service-sizing heuristics, splitting overgrown services, or the cumulative overhead cost of many services.
- **Gap**: Only one end of the sizing spectrum (premature/too-early decomposition) is addressed. The too-small, too-many, and overgrown-service cases are unaddressed.
- **Cross-references**: TS-6 (Distributed system design) — stub
- **RESOLVED**: Closed by TS-6's `08-microservices-at-scale.adoc`, "Service sizing" section. Names both failure modes (nanoservices split along a technical rather than business seam; overgrown services accreting unrelated responsibilities), requires revisiting boundaries periodically, and covers the cumulative infrastructure-overhead cost of running many services.

---

## Pragmatic acceptance of antipatterns

- **Source**: https://blog.allegro.tech/2024/04/ten-years-microservices.html
- **What the source says**: Good practices are heuristics; the team deliberately applied an antipattern (splitting read/write services sharing an Elasticsearch cluster) to solve a bursty-write problem, and it worked well for 3+ years. "Know when to use patterns, know when to use antipatterns."
- **Coverage check**: TS-5 has a CQRS section but nothing on the meta-pragmatism of knowingly accepting a coupling antipattern when a clean solution doesn't exist.
- **Gap**: No guidance on the pragmatic, evidence-driven acceptance of antipatterns at the architecture level, or how to bound and evaluate the resulting risk.
- **Cross-references**: TS-7 (Code design)

---

## Service end-of-life and decommissioning

- **Source**: https://blog.allegro.tech/2024/04/ten-years-microservices.html
- **What the source says**: The author witnessed the full lifecycle of a service, including its 2022 shutdown when replaced by a newer solution.
- **Coverage check**: TS-10 covers release cadence, strategies, rollback, and change freezes but not service sunset/decommissioning. TS-5 has no end-of-life content.
- **Gap**: No standard covers the decommissioning/sunset phase of a service's lifecycle (replacement, data retention, client migration, shutdown).
- **Cross-references**: TS-10 (Releasing)

---

## Monolith-to-microservices migration execution

- **Source**: https://blog.allegro.tech/2024/04/ten-years-microservices.html
- **What the source says**: Rubicon was a multi-year, prioritized extraction with parallel running of old and new systems, and a business-granted grace period for technical work.
- **Coverage check**: TS-5 covers the principle of not extracting too early and using the modular monolith as a stepping stone, but not the execution of a large-scale migration (extraction prioritization, strangler-fig/parallel-run patterns, multi-year sequencing).
- **Gap**: The "how to execute a large monolith-to-microservices migration" half (prioritization, parallel running, sequencing) is unaddressed.
- **Cross-references**: TS-6 (Distributed system design) — stub, TS-45 (Data migrations)
- **RESOLVED**: Closed by TS-6's `09-migration-execution.adoc`. Covers the strangler fig pattern, extraction prioritization by boundary stability and isolation, parallel running for correctness-critical paths, and multi-year sequencing. Cross-references TS-45 for the expand-and-contract data-migration discipline that accompanies each extraction.

---

## SOLID applied at the microservice/system level

- **Source**: https://stackoverflow.blog/2021/11/01/why-solid-principles-are-still-the-foundation-for-modern-software-architecture/
- **What the source says**: SOLID scales to services — SRP means a service shouldn't handle unrelated business functions; DIP means replacing direct service calls with a message bus; ISP means separate external/internal service interfaces.
- **Coverage check**: TS-5's services content covers microservice decomposition via bounded contexts and Conway's Law but does not frame service boundaries in terms of SOLID principles.
- **Gap**: No coverage of applying SOLID at the service/system level.
- **Cross-references**: TS-6 (Distributed system design) — stub, TS-7 (Code design)
- **RESOLVED**: Closed by TS-6's `08-microservices-at-scale.adoc`, "SOLID at the service level" section. Restates all five principles at the service boundary — single responsibility (one business capability), open/closed (extend via versioned APIs/flags), Liskov substitution (interchangeable implementations behind a stable contract), interface segregation (distinct external/internal APIs), dependency inversion (depend on message contracts, eg. route via a broker, not concrete services).

---

## Triggers for adopting new technology and the build-vs-buy decision

- **Source**: https://newsletter.posthog.com/p/how-we-choose-technologies
- **What the source says**: New technology should only be adopted to solve "hair-on-fire" problems — excessive costs, scaling limits, or new customer needs. Each such problem raises an explicit build-vs-buy question.
- **Coverage check**: TS-5's dependencies and frameworks content discusses minimizing and justifying dependencies but never discusses what triggers adopting a new technology or when to build versus buy.
- **Gap**: No standard addresses the decision of when to seek a new technology (cost/scaling/customer-need triggers) or the build-vs-buy trade-off.
- **Cross-references**: TS-50 (Cloud economics)

---

## Combined technical-and-business evaluation criteria for technology selection

- **Source**: https://newsletter.posthog.com/p/how-we-choose-technologies
- **What the source says**: Every technology decision is weighed against criteria that deliberately mixes technical and business factors: performance/scalability, cost, reliability/uptime, support (open source with active community), and flexibility/interoperability.
- **Coverage check**: TS-2 defines design qualities as attributes of a finished design, not as selection criteria for choosing between technologies, and omits cost, community/support maturity, and interoperability. TS-5's framework guidance touches "proven track record" but does not enumerate a balanced criteria set.
- **Gap**: No standard frames technology selection as a multi-criteria evaluation balancing technical qualities against business factors.
- **Cross-references**: TS-2 (Software design qualities)

---

## Continuously re-evaluating technology choices and long-term stack strategy

- **Source**: https://newsletter.posthog.com/p/how-we-choose-technologies
- **What the source says**: Choosing a technology is not the end — teams continuously evaluate even cherished technologies, maintain long-term plans for core capabilities, and align the stack with multi-year strategy.
- **Coverage check**: TS-5 covers single-application architecture but contains nothing on ongoing re-evaluation of adopted technologies or maintaining a forward-looking technology-stack roadmap.
- **Gap**: No standard addresses the ongoing, long-term evaluation of an organization's technology stack.
- **Cross-references**: TS-6 (Distributed system design) — stub
- **RESOLVED**: Closed by TS-6's `10-continuous-technology-evaluation.adoc`. Requires periodically re-evaluating even long-standing technology choices against the same criteria that justified adopting them, and maintaining a living, system-wide technology-strategy view so individual service teams' choices accumulate toward a coherent direction.

---

## Technology adoption process — "only use what you understand"

- **Source**: https://nocomplexity.com/documents/0complexity/0cxdesignprinciples.html
- **What the source says**: Adopt new technologies only when you fully understand the why, what, and how; pilot new technology on a small scale with real customers before committing; develop a structural organizational process for introducing innovations.
- **Coverage check**: TS-5's frameworks content advises choosing a framework you "understand well" but does not address the adoption/evaluation process itself — small-scale piloting, staged introduction, or organizational risk capacity.
- **Gap**: No guidance on the process for evaluating and adopting new technologies (pilot-first validation, staged introduction).
- **Cross-references**: TS-2 (Software design qualities)

---

## Design for change — prefer open standards and FOSS

- **Source**: https://nocomplexity.com/documents/0complexity/0cxdesignprinciples.html
- **What the source says**: As part of designing for change, make use of open standards supported by FOSS implementations to avoid unwanted vendor lock-in.
- **Coverage check**: TS-5's dependencies and frameworks content mitigates vendor lock-in mechanically (minimize dependencies, vendor facades, application-defined interfaces) but does not state a preference for open standards or FOSS implementations as a design-for-change principle.
- **Gap**: The explicit "prefer open standards and FOSS implementations to avoid vendor lock-in" principle is missing.
- **Cross-references**: TS-2 (Software design qualities)