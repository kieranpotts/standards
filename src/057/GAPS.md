# TS-57 gap analysis

Gaps found comparing TS-57: *Logging, Monitoring, Observability* against the
following reference resource:

- https://12factor.net/logs (Factor XI: Logs, "The Twelve-Factor App", Adam
  Wiggins, 2017)

**Assessment.** TS-57's `01-logging.adoc` is currently three lines long,
stating only that PII MUST NOT be logged and that runtime errors MUST be
logged. The reference's entire subject — how an application should emit logs
in the first place (as an unbuffered stdout event stream, with no application-
level concern for routing, storage, or format beyond one-event-per-line text)
— is completely absent. This is the largest gap found across this batch of
reference material relative to the size of the affected content: a
three-line section against an eight-point reference model. `02-monitoring.adoc`
through `05-observability-strategy.adoc` were not read in this pass and may
independently cover collection/aggregation concerns; if so, some items below
may turn out to be Partial rather than Missing on a fuller read.

**Status:** First run, 2026-08-05. All gaps open. `02-monitoring.adoc`,
`03-alerting.adoc`, `04-metrics.adoc`, and `05-observability-strategy.adoc`
were not read in this pass — see Unresolved.

**Second run, 2026-08-06.** Re-run against the UK Government Design
Principles (https://www.gov.uk/guidance/government-design-principles). Of
its 11 principles, only #3 ("Design with data") was routed to TS-57. The
four files not read in the first pass (`02-monitoring.adoc`,
`03-alerting.adoc`, `04-metrics.adoc`, `05-observability-strategy.adoc`)
were read for this run. TS-57 covers the operational/telemetry side
(built-in front-end analytics, easy-to-read dashboards, metrics informing
decisions) but not the product-decision framing the principle is really
about — data over hunches, prototyping/testing with users, iterating in
response, analytics as an always-on product tool. One new Partial gap
added; all prior gaps remain open.

**Third run, 2026-08-06.** Re-run against Jeff Hodges' "Notes on
Distributed Systems for Young Bloods"
(https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/).
Three points were routed to TS-57: P6 ("'It's slow' is the hardest problem
you'll ever debug"), P9 ("Metrics are the only way to get your job done"),
and P10 ("Use percentiles, not averages"). P10 is a clean Missing gap (no
aggregation-statistic guidance at all). P6 and P9 are Partial — TS-57
covers the *solutions* (tracing, exemplars, metrics-mandated, "that vs
what") but not the problem framing, the proactive-instrument rationale,
metric types, baseline comparison, or the "logs lie" cautions. One new
Missing and two new Partial gaps added; all prior gaps remain open.

## Missing

- [ ] https://12factor.net/logs ("Treat logs as event streams... A
      twelve-factor app never concerns itself with routing or storage of its
      output stream") is not addressed. `01-logging.adoc` says what MUST/MUST
      NOT be logged but nothing about how the application should treat its own
      log output. Recommend a new opening principle in `01-logging.adoc`
      before the PII/errors requirements.

- [ ] https://12factor.net/logs ("each running process writes its event
      stream, unbuffered, to `stdout`... In staging or production deploys,
      each process' stream will be captured by the execution environment,
      collated together with all other streams from the app, and routed to
      one or more final destinations [...] completely managed by the
      execution environment") is not addressed. TS-57 does not state that
      applications should write to stdout at all, nor that collection/routing
      is the execution environment's responsibility rather than the
      application's. Recommend adding to the new section proposed above; this
      is the reference's central mechanism and arguably belongs first.

- [ ] https://12factor.net/logs ("During local development [...] the
      developer will view this stream in the foreground of their terminal to
      observe the app's behavior") is not addressed — no distinction is drawn
      between local and deployed log handling. Recommend a brief note in the
      new section.

- [ ] https://12factor.net/logs ("the log format is text, one event per line
      [though] backtraces [...] may span multiple lines") is not addressed —
      TS-57 has no format guidance at all (structured/JSON vs plain text,
      one-event-per-line convention). This also borders TS-57's own scope
      question of whether it should recommend structured (eg. JSON) logging
      for machine parsing, which the reference does not itself require but
      which is common practice this standard could reasonably take a position
      on. Recommend a new "Log format" subsection.

- [ ] https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/
      ("Use percentiles, not averages") is not addressed anywhere in the
      standard. `04-metrics.adoc:10-11` requires latency-like metrics (API
      response times, batch processing times, transaction speed) to be
      tracked but never specifies how to aggregate them — no mention of
      percentiles (50th/99th/99.9th/99.99th), no statement that averages
      should be avoided, no warning that a mean assumes a bell curve, and
      no claim that distributed-system latency does not follow a bell
      curve. The standard could be read as permitting "average latency"
      reporting, which is exactly what the reference argues against.
      Recommend a one-paragraph addition to `04-metrics.adoc` mandating
      percentile aggregation over averages for latency distributions.

## Partial

(None identified against `01-logging.adoc` — everything in scope was Missing.
Re-running against `02-monitoring.adoc` and `05-observability-strategy.adoc`
may surface Partial items for the collection/routing claims.)

- [ ] https://www.gov.uk/guidance/government-design-principles (Principle 3,
      "Design with data") covers data-driven product decision-making more
      directly than `04-metrics.adoc:3-14` (metrics inform success criteria,
      future development, and "customer usage / activity patterns";
      customer-facing apps MUST have front-end analytics) and
      `05-observability-strategy.adoc:19-21,58-60` (dashboards easy to find,
      read, navigate, optimised for a glance) — specifically, the principle
      prescribes letting data (not hunches or guesswork) drive
      decision-making; prototyping and testing with users then iterating
      in response after launch; and treating analytics as "built-in,
      always on and easy to read" — an essential product tool. TS-57 covers
      the visibility/operational plumbing that can feed a "design with
      data" practice (it even requires front-end analytics for
      customer-facing apps) and its "treat observability as a product"
      framing applies to tooling for engineers, but it never frames
      analytics as a product/decision tool for shaping the service, never
      states data-over-hunches, and never addresses prototype/test/iterate
      in response to data. Recommend a new "Product analytics and
      data-driven decisions" subsection in `04-metrics.adoc` (or
      `05-observability-strategy.adoc`), distinguishing operational
      observability from product analytics. Note: the product-analytics/
      iterate-from-data framing may border on TS-15 (User Interfaces) or a
      product standard; the user may decide to split.

- [ ] https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/
      ("'It's slow' is the hardest problem you'll ever debug") covers the
      problem framing more directly than
      `05-observability-strategy.adoc:101-115` (Tracing — "the tool of last
      resort for investigating slow requests") and `:94-99` (Exemplars —
      collapsing the metric-to-trace step) — specifically, the reference
      frames "it's slow" as uniquely hard because the symptom gives few
      clues to the flaw's location, partial failures lurk that don't show
      on the graphs you usually look at, and you won't get resources to
      investigate until degradation is already obvious (so instrument
      proactively). TS-57 strongly covers the *solution* (distributed
      tracing, exemplars, attributing latency to upstream dependencies, the
      "go red on anything" false-negative rule at `:62-64`) but never
      states the *problem framing* or the proactive-instrument-before-it-
      hurts rationale tied to latency debugging. Recommend a short framing
      paragraph in the Tracing section (`05-observability-strategy.adoc:101`)
      stating why latency debugging demands tracing and proactive
      instrumentation.

- [ ] https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/
      ("Metrics are the only way to get your job done") covers metric types
      and baseline reasoning more thoroughly than `04-metrics.adoc:3-11`
      (metrics MUST inform success criteria, future development, stability,
      customer usage; key metrics tracked) and
      `05-observability-strategy.adoc:83-86` ("a metric tells you *that*
      something is wrong; the event log gives you a specific example of
      *what*") — specifically, the reference names the metric types (latency
      percentiles, monotonically increasing counters on actions, rates of
      change), frames baseline comparison (day-20 vs day-15) as "the
      difference between engineering and shamanism," and warns that log
      files tend to lie (rare error classes dominate log volume) and that
      odd log lines shouldn't be over-emphasised without checking against
      metrics. TS-57 mandates metrics and captures the "necessary but not
      sufficient" framing but doesn't specify counter/gauge/histogram metric
      types, doesn't frame baseline-comparison reasoning, and doesn't warn
      that logs lie or that log anomalies should be cross-checked against
      metrics. The "log as if someone who hasn't seen the code will read
      them" guidance is partially captured by the dashboard-usability
      principle (`05-observability-strategy.adoc:19-21`) but not for log
      content specifically. Recommend expanding `04-metrics.adoc` to name
      metric types and baseline comparison, and adding a log-reliability
      caution to `01-logging.adoc` or the event-log pattern in
      `05-observability-strategy.adoc`.

## Out-of-scope

(None identified in this run.)

## Unresolved

- [ ] `02-monitoring.adoc`, `03-alerting.adoc`, `04-metrics.adoc`, and
      `05-observability-strategy.adoc` were not read in this pass. The Logs
      factor is narrowly about `01-logging.adoc`'s subject matter, but the
      "execution environment captures and routes streams" claim may already be
      implicit in the monitoring/observability-strategy content. Recommend a
      follow-up pass reading those four files before treating the Missing
      items above as final.
