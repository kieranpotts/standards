# TS-50 gap analysis

Gaps found comparing TS-50: *Cloud Economics* against the following reference
resource:

- https://www.gov.uk/guidance/government-design-principles (UK Government
  Design Principles)

**Assessment.** Of the 11 UK Government Design Principles, only #11 ("Minimise
environmental impact") was routed to TS-50. TS-50 is a financial-decision-
making standard (cost structures, surge-cost avoidance, cloud-native-vs-
dedicated-server economics); it never frames any guidance in sustainability
terms, and none of its content addresses energy, water, materials, carbon,
climate, biodiversity, or pollution. Several of its cost-efficiency
recommendations (caching, compression, avoiding excessive logging,
right-sizing workloads, preferring fewer/larger servers — eg.
`01-auto-scaling-surge-costs.adoc:53-62`, `02-dedicated-servers-vs-cloud-native.adoc:24-43`)
would *incidentally* reduce resource consumption, but the standard never
makes the connection to environmental impact. The principle's environmental
content plausibly sits outside TS-50's stated purpose (economics), and likely
warrants a dedicated sustainability standard; recorded as out-of-scope,
flagged for the user.

**Status:** First run, 2026-08-06. One Out-of-scope item flagged for the
user; no in-scope gaps recorded.

**Second run, 2026-08-06.** Re-run against Jeff Hodges' "Notes on
Distributed Systems for Young Bloods"
(https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/).
One point was routed to TS-50: P11 ("Learn to estimate your capacity").
Partial — TS-50 touches the outcome (a 10k-QPS single-server rule of thumb)
but not the estimation methodology (back-of-envelope sizing, Jeff Dean's
hardware numbers, machine-count derivation). One new Partial gap added; the
prior out-of-scope item remains.

## Missing

(None identified in this run.)

## Partial

- [ ] https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/
      ("Learn to estimate your capacity") covers capacity-estimation
      methodology more thoroughly than
      `02-dedicated-servers-vs-cloud-native.adoc:28-33` (a single rule of
      thumb: a single large server suffices for most web services under
      ~10,000 QPS) — specifically, the reference teaches back-of-the-
      envelope sizing (how many tweet ids fit in 24GB minus OS/request
      overhead given 8-byte ids), machine-count derivation from a workload
      (QPS, data volume, request rate), "seconds in a day" throughput
      reasoning, and Jeff Dean's "Numbers Everyone Should Know" as a
      hardware-performance baseline (latency, memory bandwidth, disk seek,
      round-trip). TS-50 touches the *outcome* (the 10k-QPS rule, a
      5%-utilization cost threshold at
      `02-dedicated-servers-vs-cloud-native.adoc:24-26`, a storage-cost
      arithmetic example at `01-auto-scaling-surge-costs.adoc:30-38`) but
      never teaches the *skill* of estimating capacity, gives no hardware
      performance baselines, and never derives machine count from a
      workload. Recommend a new "Capacity estimation" subsection in
      `02-dedicated-servers-vs-cloud-native.adoc` (or a new file) covering
      back-of-envelope sizing and hardware characteristic baselines. Note:
      this sits at the TS-50 (economics) / TS-14 (Performance Testing)
      boundary — capacity-estimation methodology may better fit TS-14; the
      user may decide to split.

## Out-of-scope

- [ ] https://www.gov.uk/guidance/government-design-principles (Principle 11,
      "Minimise environmental impact") covers the real-world consumption of
      energy, water, and materials to build and run digital services; the
      impacts of climate change, biodiversity loss, and pollution; and
      applying sustainability best practice across a service's lifespan. This
      plausibly sits outside this standard because TS-50's stated purpose is
      cloud *economics* (cost), not environmental sustainability — it never
      discusses energy consumption, water usage (datacenter cooling),
      materials/embodied carbon/e-waste, carbon accounting, climate,
      biodiversity, or pollution. Its cost-efficiency recommendations
      (`01-auto-scaling-surge-costs.adoc:53-62`,
      `02-dedicated-servers-vs-cloud-native.adoc:24-43`) would incidentally
      reduce resource use but are framed purely financially. The
      environmental dimension has no current home in the standards corpus and
      likely warrants a dedicated sustainability standard. Flagged for the
      user to confirm or overrule, or to route to a future sustainability
      standard.

## Unresolved

(None.)