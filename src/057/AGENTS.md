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

## References

- [TS-57: Logging, Monitoring, Observability (source)](README.adoc)
- [TS-6: Distributed System Design](../006/AGENTS.md)
- [TS-12: Quality Assurance](../012/AGENTS.md)
- [TS-14: Performance Testing](../014/AGENTS.md)
- [TS-18: Web GUIs](../018/AGENTS.md)
- [TS-21: HTTP APIs](../021/AGENTS.md)
- [TS-52: Security and Secrets Management](../052/AGENTS.md)
- [TS-53: Privacy and Data Protection](../053/AGENTS.md)