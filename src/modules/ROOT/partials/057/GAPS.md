# TS-57 gap analysis

Gaps found comparing TS-57: Logging, monitoring, observability against the
following reference resources:

- https://blog.nelhage.com/post/computers-can-be-understood/
- https://blog.allegro.tech/2024/04/ten-years-microservices.html
- https://blog.pragmaticengineer.com/pragmatic-engineer-test/

**Assessment.** All three sources point at coverage the standard was
entirely missing rather than treating thinly: debugging methodology and the
deductive/empirical split, self-service ownership of observability
configuration, and oncall health as a measured, prioritized concern.
Converted from the legacy format on 2026-08-13.

**Status:** 4 of 4 actionable gaps closed (2026-08-13). All four items were
written up: two new sections in `05-observability-strategy.adoc`
("Debugging as a discipline" and "When to stop deducing and start
observing"), an extension to that file's "Treat observability as a product"
section on self-service configuration ownership, and a new "Oncall health"
section in `03-alerting.adoc`. 0 missing, 0 partial, 0 out-of-scope,
0 unresolved.

## Missing

- [x] https://blog.nelhage.com/post/computers-can-be-understood/ says the
      trickiest bugs span multiple abstraction layers and require moving
      between layers to root-cause. With strong mental models, engineers can
      sometimes "single-shot" a bug from a single observation by reasoning
      through system state. The gap: no guidance on debugging methodology —
      how to systematically investigate bugs using observations (logs,
      traces, dumps) to form and test hypotheses. Coverage check: TS-57
      covers observing a running system (dashboards, event logs, traces) but
      not the diagnostic reasoning that turns observations into root causes.
      Recommend a new section in `05-observability-strategy.adoc`.
      Cross-references: TS-12 (Quality assurance).

      **Resolved.** Closed by a new "Debugging as a discipline" section in
      `05-observability-strategy.adoc`. States that debugging is a
      practicable skill, not an innate ability, covering cross-layer
      reasoning, forming a hypothesis before gathering more data, and
      preferring the observation that eliminates the most hypotheses.
      Source added to the page's `== References`.

- [x] https://blog.nelhage.com/post/computers-can-be-understood/ says that
      for distributed systems, "big balls of mud," and heterogeneous
      client-side JavaScript, in-depth understanding is impractical; the
      right strategy is empiricism — observe the running system, treat
      behavior statistically, and invest in fault-tolerance rather than
      root-causing every component failure. The gap: no standard frames the
      decision of when a system is too complex to reason about deductively
      and must be probed empirically. Coverage check: TS-57 covers
      observability mechanics but does not articulate the meta-principle of
      when to abandon deductive understanding for empirical methods, nor the
      distributed-systems tradeoff of fixing the fault-tolerance layer
      instead of root-causing component failures. Recommend a new section in
      `05-observability-strategy.adoc`. Cross-references: TS-6 (Distributed
      system design).

      **Resolved.** Closed by a new "When to stop deducing and start
      observing" section in `05-observability-strategy.adoc`, directly
      following "Debugging as a discipline". States when deductive
      root-causing does not scale (distributed systems, undocumented
      accretion, heterogeneous client-side code), and directs the reader to
      treat behavior statistically and invest in fault tolerance over
      root-causing every failure, cross-referencing TS-6 (Distributed system
      design) for the resilience patterns this relies on. Note: the item's
      original cross-reference described TS-6 as a stub; TS-6 is now fully
      written (10 partials, no `// TODO` placeholder), so the xref links
      directly rather than needing a redirect. Source added to the page's
      `== References`.

- [x] https://blog.allegro.tech/2024/04/ten-years-microservices.html says
      monitoring was initially a centralized team reached via JIRA tickets
      (~1-week turnaround); a major early win was pushing observability
      configuration (custom charts, alerts) directly to development teams.
      The gap: TS-57 does not address ownership of observability
      configuration by development teams (vs. a centralized ops/monitoring
      team), nor the self-service observability workflow. Coverage check:
      TS-57's monitoring section is a single paragraph requiring uptime
      monitoring and per-service monitoring. It does not address who owns
      observability configuration or the centralized-vs-decentralized
      ownership model. Recommend extending the existing "Ownership" bullet
      under "Treat observability as a product" in
      `05-observability-strategy.adoc`. Cross-references: TS-49 (Cloud
      platform engineering).

      **Resolved.** Closed by a new paragraph extending "Treat observability
      as a product" in `05-observability-strategy.adoc`, directly below the
      existing "Ownership" bullet. Requires development teams to be able to
      configure their own dashboards, alerts, and metrics directly, without
      routing through a centralized team's ticket queue; permits a
      centralized team to own the underlying platform (provisioning,
      retention, cost) but not to be the sole route for a development team's
      own configuration changes. Source added to the page's `== References`.

- [x] https://blog.pragmaticengineer.com/pragmatic-engineer-test/ says that
      for oncall teams, oncall health and its impact on developers should be
      measured, and fixing an unhealthy oncall should take priority over
      product work. The gap: no standard covers oncall health measurement or
      the prioritization of oncall remediation over product work. Coverage
      check: TS-57's alerting content is about production error
      notification; it does not address oncall health as a
      developer-wellbeing concern (alert fatigue, page volume, toil,
      burnout), nor the practice of measuring oncall load and prioritizing
      its remediation over feature work. Recommend a new section in
      `03-alerting.adoc`. Cross-references: TS-10 (Releasing).

      **Resolved.** Closed by a new "Oncall health" section in
      `03-alerting.adoc`. Requires oncall health to be measured (page volume
      per rotation/engineer, actionable-vs-non-actionable split, time-of-day
      distribution, time to resolution) and requires prioritizing
      remediation of an unhealthy rotation over product work, naming
      threshold tuning, fixing recurring-page causes, and adjusting rotation
      size as remediation options. Note: TS-10 (Releasing)'s own `GAPS.md`
      already recorded this same gap, sourced from the same article, and
      recommended TS-57 — not TS-10 — as the correct home; that
      recommendation is what this item follows, so no cross-standard split
      was needed. Source added to the page's `== References`.

## Partial

(The original analysis recorded no partial-coverage items.)

## Out-of-scope

(Converted from the legacy format, which recorded no out-of-scope items.)

## Unresolved

(Converted from the legacy format, which recorded no unresolved items.)
