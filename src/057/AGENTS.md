# TS-57: Logging, Monitoring, Observability

Principles and best practices for logging, monitoring, and
observability — collectively known as the *visibility* quality attribute.

Use this when designing or implementing logging, monitoring, alerting,
or metrics collection for applications and services.

Do NOT use this for security controls on log data (access control,
retention, audit-log protection) — see
[TS-52: Security and Secrets Management](../052/AGENTS.md). For PII
handling and data-retention policy, see
[TS-53: Privacy and Data Protection](../053/AGENTS.md). For QA and
testing practices, see [TS-12: Quality Assurance](../012/AGENTS.md). For
performance monitoring and load testing, see
[TS-14: Performance Testing](../014/AGENTS.md). For HTTP API metrics
(context of API response times), see [TS-21: HTTP APIs](../021/AGENTS.md).
For distributed system design concerns, see
[TS-6: Distributed System Design](../006/AGENTS.md).

## Rules

### Logging

- **PII MUST NOT be sent to log output.** (See also
  [TS-53: Privacy and Data Protection](../053/AGENTS.md).)

- **Runtime errors MUST be logged**, so that issues can be detected and
  investigated.

### Monitoring

- **Uptime monitoring MUST be implemented for software-as-a-service
  applications.**

- **Individual services within a distributed system MUST be monitored
  separately** to the user interface of the application as a whole.

### Alerting

- **Production alerting MUST be implemented in production
  environments.** Alerts — notifications of errors or other issues —
  SHOULD also be implemented in pre-production environments.

### Metrics

- **Metrics MUST be gathered** to inform and evaluate:
  - Success criteria for changes made.
  - Future development.
  - Stability and reliability monitoring.
  - Customer usage / activity patterns.

- **Key metrics MUST be tracked and monitored.** Examples: API response
  times, batch processing times, speed of transactions.

- **Customer-facing applications MUST have front-end analytics
  integrated**, to provide insights into how customers use the
  application. (See also [TS-18: Web GUIs](../018/AGENTS.md).)

### Observability strategy

- **Observability is the outcome, not the mechanism.** Logging,
  monitoring, alerting, and metrics are the mechanisms; observability is
  the ability to ask arbitrary questions of a running system without
  re-instrumenting it. A system with extensive telemetry but poor
  structure is not observable.

- **Treat observability as a product.** Observability tooling is used
  under pressure during incidents. It SHOULD be designed with the same
  care as a user-facing product: usable at a glance, consistent across
  systems, and owned by every team that owns a service — not just
  infrastructure specialists.

- **Structure dashboards as a drill-down hierarchy** (RECOMMENDED):
  1. *Overview dashboard* — a single bird's-eye view of every
     subsystem, acting as a traffic light that goes red when anything is
     wrong. The first stop when an alert fires. SHOULD be the default
     landing page and linked from team channels.
  2. *System dashboards* — one per subsystem, an exhaustive picture of
     that subsystem's health (rejections, bottlenecks, outcomes, load).
  3. *Logs* — individual events.
  4. *Traces* — the most zoomed-in view, for slow requests.
  Each level SHOULD link to the next so an engineer moves down the
  hierarchy without leaving the dashboard.

- **Optimize dashboards for a glance.** An engineer SHOULD be able to
  tell whether a dashboard is relevant in seconds. Avoid false negatives
  — an overview SHOULD go red when anything is wrong, no matter how
  minor. Use a consistent design system across all dashboards so
  familiarity transfers. Split metrics by outcome (eg. `success`,
  `rate_limited`, `error`).

- **Each significant unit of work SHOULD emit a single event log** on
  completion, regardless of outcome (success, error, or panic). Event
  logs record the event name, duration, outcome, and resource IDs — the
  high-cardinality data that metrics cannot capture. They bridge
  metrics to logs: a metric tells you *that* something is wrong; the
  event log gives a specific example of *what*. Emit the event log in a
  `defer` block so it is always written.

- **Exemplars MAY be attached to metrics** to let an engineer jump from
  a point on a chart directly to the trace for the request that
  produced it.

- **Trace third-party interactions and database queries.** Every call
  to an external API SHOULD be traced via a shared base client. Each
  database query SHOULD be traced with its duration and, where
  practical, the query itself. Time spent waiting for a connection
  SHOULD be tracked separately from execution time.

- **Exercise the setup with game days.** An observability setup that
  has never been used under pressure is unproven. Game days — scheduled
  exercises where the team deliberately breaks something and uses the
  dashboards to diagnose it — SHOULD be run regularly. Treat them like
  user testing: give participants minimal context, watch what they
  struggle with, and adjust the dashboards together afterward.

## References

- [TS-57: Logging, Monitoring, Observability (source)](README.adoc)
- [TS-6: Distributed System Design](../006/AGENTS.md)
- [TS-12: Quality Assurance](../012/AGENTS.md)
- [TS-14: Performance Testing](../014/AGENTS.md)
- [TS-18: Web GUIs](../018/AGENTS.md)
- [TS-21: HTTP APIs](../021/AGENTS.md)
- [TS-52: Security and Secrets Management](../052/AGENTS.md)
- [TS-53: Privacy and Data Protection](../053/AGENTS.md)
- [Building On-call: Our observability strategy — incident.io](https://incident.io/hubs/building-on-call/building-on-call-our-observability-strategy)
- [Anchor logs — Lisa](https://paprikati.github.io/2021/10/03/anchor-logs.html)
