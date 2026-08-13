# GAPS — TS-10 Releasing

Coverage gaps identified by comparing external sources against this standard.

---

## Service end-of-life and decommissioning

- **Source**: https://blog.allegro.tech/2024/04/ten-years-microservices.html
- **What the source says**: The author witnessed the full lifecycle of a service, including its 2022 shutdown when replaced by a newer solution.
- **Coverage check**: TS-10 covers release cadence, strategies, rollback, and change freezes but not service sunset/decommissioning. No matches for "decommission" in `src/`.
- **Gap**: No standard covers the decommissioning/sunset phase of a service's lifecycle (replacement, data retention, client migration, shutdown).
- **Cross-references**: TS-5 (Application architecture)

---

## Healthy oncall as a priority

- **Source**: https://blog.pragmaticengineer.com/pragmatic-engineer-test/
- **What the source says**: For oncall teams, oncall health and its impact on developers should be measured, and fixing an unhealthy oncall should take priority over product work.
- **Coverage check**: TS-10 mentions the "on-call engineer" only as a release-approval role. No standard addresses oncall rotations, load, or health.
- **Gap**: Neither TS-10 nor TS-57 covers oncall health measurement or the prioritization of oncall remediation over product work.
- **Cross-references**: TS-57 (Logging, monitoring, observability)