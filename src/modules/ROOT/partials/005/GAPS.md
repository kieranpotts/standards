# TS-5 gap analysis

Gaps found comparing TS-5: Application architecture against the following
reference resources:

- https://www.simplethread.com/20-things-ive-learned-in-my-20-years-as-a-software-engineer/
- https://blog.allegro.tech/2024/04/ten-years-microservices.html
- https://stackoverflow.blog/2021/11/01/why-solid-principles-are-still-the-foundation-for-modern-software-architecture/
- https://newsletter.posthog.com/p/how-we-choose-technologies
- https://nocomplexity.com/documents/0complexity/0cxdesignprinciples.html

**Assessment.** The analysis found a mix of missing and partial coverage
across microservices practice (sizing, migration execution, antipattern
tolerance, decommissioning), technology-selection process (adoption triggers,
evaluation criteria, build-vs-buy), and SOLID applied at the service level.
Six of the thirteen items belonged to distributed-systems concerns rather
than single-application architecture and were closed by TS-6 (Distributed
system design) once that standard gained substantive content. This file was
converted from the legacy format to the template format on 2026-08-13.

**Status:** 13 of 13 actionable gaps closed (2026-08-13). Six were closed by
TS-6 (Distributed system design) in a prior run. This run closed the
remaining seven: proven-technology heuristic, pragmatic antipattern
acceptance, service decommissioning, technology-adoption triggers, technology
selection criteria, the pilot-first adoption process, and the open-standards
preference. 0 missing, 0 partial, 0 out-of-scope, 0 unresolved.

## Missing

- [x] https://www.simplethread.com/20-things-ive-learned-in-my-20-years-as-a-software-engineer/
      says old technologies that have survived are "sharks, not dinosaurs" —
      they solve problems so well they've outlasted change, and should not be
      replaced without a very good reason. The gap: no general,
      technology-agnostic articulation of the "favor proven, long-surviving
      technologies; replace only with strong justification" heuristic across
      all technology choices (databases, languages, protocols, runtimes,
      message brokers). Coverage check: TS-5's dependencies and frameworks
      content states this narrowly for frameworks only ("prefer frameworks
      with a proven track record of stability and longevity"). Recommend a
      new section in `04-dependencies.adoc`.

      **Resolved.** Closed by `04-dependencies.adoc`, "Favor proven
      technology" section. States the heuristic generally, across every
      technology choice an application makes, not only frameworks; quotes
      the "sharks, not dinosaurs" framing; and requires a newer alternative
      to clear a higher bar of justification — a concrete scaling, cost, or
      capability gap — before displacing an established technology. Source
      added to the page's `== References`.

- [x] https://blog.allegro.tech/2024/04/ten-years-microservices.html says the
      author witnessed the full lifecycle of a service, including its 2022
      shutdown when replaced by a newer solution. The gap: no standard covers
      the decommissioning/sunset phase of a service's lifecycle (replacement,
      data retention, client migration, shutdown). Coverage check: TS-10
      covers release cadence, strategies, rollback, and change freezes but
      not service sunset/decommissioning — that standard's scope is a live
      service's own release cycle, not the end of a service's life. TS-5 had
      no end-of-life content. Recommend a new section in TS-5, since
      decommissioning is a phase of a service's lifecycle, which is TS-5's
      concern, not a release-engineering concern.

      **Resolved.** Closed by a new partial, `07-decommissioning.adoc`,
      "Decommissioning" section, wired into the page after `06-services.adoc`.
      Requires a deliberate decommissioning plan covering replacement, data
      retention, client migration, and shutdown, in that order, and requires
      confirming zero consumer traffic before the final shutdown. Distinguishes
      decommissioning from TS-10's release-cadence scope: TS-10 governs how a
      *live* service ships new versions of itself, this section governs how a
      service's life ends. Cross-references TS-10 (Releasing) for that
      distinction. Source added to the page's `== References`.

- [x] https://newsletter.posthog.com/p/how-we-choose-technologies says new
      technology should only be adopted to solve "hair-on-fire" problems —
      excessive costs, scaling limits, or new customer needs — and each such
      problem raises an explicit build-vs-buy question. The gap: no standard
      addresses the decision of when to seek a new technology (cost/scaling/
      customer-need triggers) or the build-vs-buy trade-off. Coverage check:
      TS-5's dependencies and frameworks content discusses minimizing and
      justifying dependencies but never discusses what triggers adopting a
      new technology or when to build versus buy. Recommend a new section in
      `04-dependencies.adoc`.

      **Resolved.** Closed by `04-dependencies.adoc`, "Triggers for adopting
      new technology" section. Names the three triggers (cost, scale, new
      requirements) as the bar a new technology adoption must clear, and
      requires each trigger to raise an explicit build-versus-buy question
      weighing in-house build against adopting a new technology or vendor
      service. Source added to the page's `== References`.

- [x] https://newsletter.posthog.com/p/how-we-choose-technologies says every
      technology decision is weighed against criteria that deliberately mixes
      technical and business factors: performance/scalability, cost,
      reliability/uptime, support (open source with active community), and
      flexibility/interoperability. The gap: no standard frames technology
      selection as a multi-criteria evaluation balancing technical qualities
      against business factors. Coverage check: TS-2 defines design qualities
      as attributes of a finished design, not as selection criteria for
      choosing between technologies, and omits cost, community/support
      maturity, and interoperability. TS-5's framework guidance touches
      "proven track record" but does not enumerate a balanced criteria set.
      Recommend a new section in `04-dependencies.adoc`.
      Cross-references: TS-2 (Software design qualities).

      **Resolved.** Closed by `04-dependencies.adoc`, "Technology selection
      criteria" section. Enumerates the five criteria (performance and
      scalability, cost, reliability, support and maturity, flexibility and
      interoperability) as the balanced set a technology choice should be
      weighed against, and states the purpose of naming them explicitly:
      making the trade-off visible rather than implicit. Source added to the
      page's `== References`.

- [x] https://nocomplexity.com/documents/0complexity/0cxdesignprinciples.html
      says adopt new technologies only when you fully understand the why,
      what, and how; pilot new technology on a small scale with real
      customers before committing; and develop a structural organizational
      process for introducing innovations. The gap: no guidance on the
      process for evaluating and adopting new technologies (pilot-first
      validation, staged introduction). Coverage check: TS-5's frameworks
      content advises choosing a framework you "understand well" but does not
      address the adoption/evaluation process itself. Recommend a new section
      in `04-dependencies.adoc`. Cross-references: TS-2 (Software design
      qualities).

      **Resolved.** Closed by `04-dependencies.adoc`, "Adoption process"
      section. Requires full understanding of a technology before adopting
      it, requires piloting new technology at a small scale against a narrow
      slice of real production traffic before committing broadly, and
      recommends larger organizations establish a structural review process
      to keep adoption decisions consistent across teams. Source added to
      the page's `== References`.

- [x] https://nocomplexity.com/documents/0complexity/0cxdesignprinciples.html
      says that, as part of designing for change, applications should make
      use of open standards supported by FOSS implementations to avoid
      unwanted vendor lock-in. The gap: the explicit "prefer open standards
      and FOSS implementations to avoid vendor lock-in" principle is missing.
      Coverage check: TS-5's dependencies and frameworks content mitigates
      vendor lock-in mechanically (minimize dependencies, vendor facades,
      application-defined interfaces) but does not state a preference for
      open standards or FOSS implementations as a design-for-change
      principle. Recommend a new section in `04-dependencies.adoc`.
      Cross-references: TS-2 (Software design qualities).

      **Resolved.** Closed by `04-dependencies.adoc`, "Design for change:
      prefer open standards" section. States the preference for open
      standards and FOSS implementations over proprietary alternatives,
      frames it as a complement to the existing vendor-facades guidance
      (facades contain lock-in mechanically; open standards keep a migration
      path open even where no facade was written), and notes the preference
      is not absolute. Source added to the page's `== References`.

## Partial

_(No items — the original legacy analysis recorded no partial-coverage
items still open after the TS-6 closures; all seven open items were Missing.)_

## Out-of-scope

_(No items — the file was converted from the legacy format, which has no
concept of an out-of-scope item, and recorded none.)_

## Unresolved

_(No items — the file was converted from the legacy format, which has no
concept of an unresolved reference resource, and recorded none.)_

---

## Resolved before this run (closed by TS-6)

The following six gaps were identified against TS-5 but, on inspection, their
content plainly belonged in TS-6 (Distributed system design) — a stub at the
time of the original analysis. The user agreed to that split. TS-6 has since
been written, and each of these was closed there. Kept here, in full, as the
permanent record of the decision and its resolution.

- [x] https://blog.allegro.tech/2024/04/ten-years-microservices.html says
      microservices require heavy, ongoing investment in infrastructure and
      tooling; the "glue" between services is not simple; much
      anti-microservice sentiment comes from treating them as a silver
      bullet or ignoring the "you must be this tall" prerequisites. The gap:
      no guidance on prerequisites, total cost of ownership, or the
      "right scale required" framing for adopting microservices. Coverage
      check: TS-5's services content notes microservices are "harder to
      implement well than many teams realize" but does not address
      infrastructure/tooling investment, scale thresholds, or total-cost
      framing. Recommend a new section in TS-6 (Distributed system design) —
      stub at the time of analysis. Cross-references: TS-6 (Distributed
      system design).

      **Resolved.** Closed by TS-6's `08-microservices-at-scale.adoc`,
      "Prerequisites and total cost of ownership" section. States the
      required infrastructure investment (deployment pipeline, cross-service
      observability, team structure aligned to boundaries) as a precondition
      for adopting microservices, and requires weighing the cumulative total
      cost of ownership of many services against the coordination cost of
      the monolith they would replace.

- [x] https://blog.allegro.tech/2024/04/ten-years-microservices.html says
      microservices let teams safely experiment with new languages (Kotlin,
      Scala, Go, Elixir) in production by limiting the blast radius of
      failures. The gap: no coverage of using service boundaries as a
      deliberate experimentation / blast-radius-isolation mechanism.
      Coverage check: TS-49 covers "aligned autonomy" and TS-5 covers
      independent deployability and bounded contexts, but neither covers
      using service isolation to trial new languages/stacks in production
      with contained failure radius. Recommend a new section in TS-6
      (Distributed system design) — stub at the time of analysis.
      Cross-references: TS-6 (Distributed system design), TS-49 (Cloud
      platform engineering).

      **Resolved.** Closed by TS-6's `07-resilience-and-blast-radius.adoc`,
      "Blast radius and failure domains" section. States that service
      boundaries double as failure-domain boundaries, making them a
      practical place to trial a new language, framework, or runtime under
      real production traffic with the resulting risk contained to one
      service.

- [x] https://blog.allegro.tech/2024/04/ten-years-microservices.html says
      going too small ("nanoservices") causes debugging and
      distribution-overhead pain; going too big recreates monolith problems;
      1000+ services carry cumulative overprovisioning cost. The gap: only
      one end of the sizing spectrum (premature/too-early decomposition) is
      addressed. The too-small, too-many, and overgrown-service cases are
      unaddressed. Coverage check: TS-5 covers the too-early extraction
      problem ("premature decomposition") but says nothing about the
      too-small end, service-sizing heuristics, splitting overgrown
      services, or the cumulative overhead cost of many services. Recommend
      a new section in TS-6 (Distributed system design) — stub at the time
      of analysis. Cross-references: TS-6 (Distributed system design).

      **Resolved.** Closed by TS-6's `08-microservices-at-scale.adoc`,
      "Service sizing" section. Names both failure modes (nanoservices split
      along a technical rather than business seam; overgrown services
      accreting unrelated responsibilities), requires revisiting boundaries
      periodically, and covers the cumulative infrastructure-overhead cost
      of running many services.

- [x] https://blog.allegro.tech/2024/04/ten-years-microservices.html says
      Rubicon was a multi-year, prioritized extraction with parallel running
      of old and new systems, and a business-granted grace period for
      technical work. The gap: the "how to execute a large
      monolith-to-microservices migration" half (prioritization, parallel
      running, sequencing) is unaddressed. Coverage check: TS-5 covers the
      principle of not extracting too early and using the modular monolith
      as a stepping stone, but not the execution of a large-scale migration
      (extraction prioritization, strangler-fig/parallel-run patterns,
      multi-year sequencing). Recommend a new section in TS-6 (Distributed
      system design) — stub at the time of analysis. Cross-references: TS-6
      (Distributed system design), TS-45 (Data migrations).

      **Resolved.** Closed by TS-6's `09-migration-execution.adoc`. Covers
      the strangler fig pattern, extraction prioritization by boundary
      stability and isolation, parallel running for correctness-critical
      paths, and multi-year sequencing. Cross-references TS-45 for the
      expand-and-contract data-migration discipline that accompanies each
      extraction.

- [x] https://stackoverflow.blog/2021/11/01/why-solid-principles-are-still-the-foundation-for-modern-software-architecture/
      says SOLID scales to services — SRP means a service shouldn't handle
      unrelated business functions; DIP means replacing direct service calls
      with a message bus; ISP means separate external/internal service
      interfaces. The gap: no coverage of applying SOLID at the
      service/system level. Coverage check: TS-5's services content covers
      microservice decomposition via bounded contexts and Conway's Law but
      does not frame service boundaries in terms of SOLID principles.
      Recommend a new section in TS-6 (Distributed system design) — stub at
      the time of analysis. Cross-references: TS-6 (Distributed system
      design), TS-7 (Code design).

      **Resolved.** Closed by TS-6's `08-microservices-at-scale.adoc`,
      "SOLID at the service level" section. Restates all five principles at
      the service boundary — single responsibility (one business
      capability), open/closed (extend via versioned APIs/flags), Liskov
      substitution (interchangeable implementations behind a stable
      contract), interface segregation (distinct external/internal APIs),
      dependency inversion (depend on message contracts, eg. route via a
      broker, not concrete services).

- [x] https://newsletter.posthog.com/p/how-we-choose-technologies says
      choosing a technology is not the end — teams continuously evaluate
      even cherished technologies, maintain long-term plans for core
      capabilities, and align the stack with multi-year strategy. The gap:
      no standard addresses the ongoing, long-term evaluation of an
      organization's technology stack. Coverage check: TS-5 covers
      single-application architecture but contains nothing on ongoing
      re-evaluation of adopted technologies or maintaining a forward-looking
      technology-stack roadmap. Recommend a new section in TS-6 (Distributed
      system design) — stub at the time of analysis. Cross-references: TS-6
      (Distributed system design).

      **Resolved.** Closed by TS-6's `10-continuous-technology-evaluation.adoc`.
      Requires periodically re-evaluating even long-standing technology
      choices against the same criteria that justified adopting them, and
      maintaining a living, system-wide technology-strategy view so
      individual service teams' choices accumulate toward a coherent
      direction.
