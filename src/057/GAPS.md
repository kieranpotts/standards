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

## Partial

(None identified against `01-logging.adoc` — everything in scope was Missing.
Re-running against `02-monitoring.adoc` and `05-observability-strategy.adoc`
may surface Partial items for the collection/routing claims.)

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
