# TS-10 gap analysis

Gaps found comparing TS-10: Releasing against the following reference
resources:

- https://blog.allegro.tech/2024/04/ten-years-microservices.html
- https://blog.pragmaticengineer.com/pragmatic-engineer-test/

**Assessment.** Both sources point at content that belongs to other
standards rather than to TS-10 itself — service decommissioning is a
lifecycle concern of TS-5 (Application architecture), and oncall health is a
developer-wellbeing concern of TS-57 (Logging, monitoring, observability).
Converted from the legacy format on 2026-08-13.

**Status:** 0 of 2 actionable gaps closed (2026-08-13). Both items were
re-verified against the standard and found to plainly belong to other
standards' directories (TS-5 and TS-57 respectively, which each already
record the same gap in their own `GAPS.md`), so neither was written into
TS-10 without the user's decision. 2 missing, 0 partial, 0 out-of-scope,
0 unresolved.

## Missing

- [ ] https://blog.allegro.tech/2024/04/ten-years-microservices.html says the
      author witnessed the full lifecycle of a service, including its 2022
      shutdown when replaced by a newer solution. The gap: no standard
      covers the decommissioning/sunset phase of a service's lifecycle
      (replacement, data retention, client migration, shutdown). Coverage
      check: TS-10 covers release cadence, strategies, rollback, and change
      freezes but not service sunset/decommissioning; no matches for
      "decommission" anywhere in `src/`. Recommend a new section in TS-5
      (Application architecture), not TS-10 — decommissioning is a service
      lifecycle concern, and TS-10 is scoped to production releases of
      still-live software. TS-5's own `GAPS.md` already records this same
      gap, sourced from the same article, still open. Cross-references:
      TS-5 (Application architecture).

- [ ] https://blog.pragmaticengineer.com/pragmatic-engineer-test/ says that
      for oncall teams, oncall health and its impact on developers should be
      measured, and fixing an unhealthy oncall should take priority over
      product work. The gap: neither TS-10 nor TS-57 covers oncall health
      measurement or the prioritization of oncall remediation over product
      work. Coverage check: TS-10 mentions the "on-call engineer" only as a
      release-approval role (`03-release-approval-and-governance.adoc`) and
      a factor in change-freeze timing (`05-change-freezes.adoc`); neither
      file addresses oncall load, rotations, or health. Recommend a new
      section in TS-57 (Logging, monitoring, observability), not TS-10 —
      oncall health is a developer-wellbeing and observability-practice
      concern, not a release mechanic. TS-57's own `GAPS.md` already records
      this same gap, sourced from the same article, still open.
      Cross-references: TS-57 (Logging, monitoring, observability).

## Partial

(The original analysis recorded no partial-coverage items.)

## Out-of-scope

(Converted from the legacy format, which recorded no out-of-scope items.)

## Unresolved

(Converted from the legacy format, which recorded no unresolved items.)
