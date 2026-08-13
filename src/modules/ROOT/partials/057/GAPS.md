# GAPS — TS-57 Logging, monitoring, observability

Coverage gaps identified by comparing external sources against this standard.

---

## Debugging as a discipline

- **Source**: https://blog.nelhage.com/post/computers-can-be-understood/
- **What the source says**: The trickiest bugs span multiple abstraction layers and require moving between layers to root-cause. With strong mental models, engineers can sometimes "single-shot" a bug from a single observation by reasoning through system state.
- **Coverage check**: TS-57 covers observing a running system (dashboards, event logs, traces) but not the diagnostic reasoning that turns observations into root causes.
- **Gap**: No guidance on debugging methodology — how to systematically investigate bugs using observations (logs, traces, dumps) to form and test hypotheses.
- **Cross-references**: TS-12 (Quality assurance)

---

## When systems defy understanding — switch to empirical/observability methods

- **Source**: https://blog.nelhage.com/post/computers-can-be-understood/
- **What the source says**: For distributed systems, "big balls of mud," and heterogeneous client-side JavaScript, in-depth understanding is impractical; the right strategy is empiricism — observe the running system, treat behavior statistically, and invest in fault-tolerance rather than root-causing every component failure.
- **Coverage check**: TS-57 covers observability mechanics but does not articulate the meta-principle of when to abandon deductive understanding for empirical methods, nor the distributed-systems tradeoff of fixing the fault-tolerance layer instead of root-causing component failures.
- **Gap**: No standard frames the decision of when a system is too complex to reason about deductively and must be probed empirically.
- **Cross-references**: TS-6 (Distributed system design) — stub

---

## Team-owned, self-service observability configuration

- **Source**: https://blog.allegro.tech/2024/04/ten-years-microservices.html
- **What the source says**: Monitoring was initially a centralized team reached via JIRA tickets (~1-week turnaround); a major early win was pushing observability configuration (custom charts, alerts) directly to development teams.
- **Coverage check**: TS-57's monitoring section is a single paragraph requiring uptime monitoring and per-service monitoring. It does not address who owns observability configuration or the centralized-vs-decentralized ownership model.
- **Gap**: TS-57 does not address ownership of observability configuration by development teams (vs. a centralized ops/monitoring team), nor the self-service observability workflow.
- **Cross-references**: TS-49 (Cloud platform engineering)

---

## Healthy oncall as a priority

- **Source**: https://blog.pragmaticengineer.com/pragmatic-engineer-test/
- **What the source says**: For oncall teams, oncall health and its impact on developers should be measured, and fixing an unhealthy oncall should take priority over product work.
- **Coverage check**: TS-57's alerting content is about production error notification; it does not address oncall health as a developer-wellbeing concern (alert fatigue, page volume, toil, burnout), nor the practice of measuring oncall load and prioritizing its remediation over feature work.
- **Gap**: No standard covers oncall health measurement or the prioritization of oncall remediation over product work.
- **Cross-references**: TS-10 (Releasing)