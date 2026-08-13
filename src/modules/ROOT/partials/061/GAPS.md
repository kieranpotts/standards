# TS-61 gap analysis

Gaps found comparing TS-61: *AI tools* against the following reference
resource:

- https://refactoring.fm/p/code-quality-in-the-age-of-ai

**Assessment.** The one gap identified is a missing strategic cost: DORA's
2024 finding that AI adoption is accompanied by reduced delivery throughput
and stability. Converted from the legacy format on 2026-08-13.

**Status:** 1 of 1 gap resolved (2026-08-13).

## Missing

- [x] https://refactoring.fm/p/code-quality-in-the-age-of-ai — The 2024 DORA
      report finds that AI adoption, while increasing individual
      productivity, is accompanied by an estimated 1.5% decrease in delivery
      throughput and a 7.2% reduction in delivery stability — the gains in
      pure coding throughput do not translate into delivery-performance
      improvements. The article frames this as "more code, faster, in
      exchange for it being less under our control." TS-61's costs section
      (`06-benefits-and-costs.adoc`) enumerates strategic costs of AI
      adoption (data privacy, dependence, skill erosion, no audit trail,
      copyright, socio-cultural bias) but never named the specific,
      empirically observed risk that AI adoption can reduce delivery
      throughput and stability. Recommend placing at
      `06-benefits-and-costs.adoc`, in the "Costs and risks" bulleted list.
      Cross-references: TS-12 (Quality assurance).

      **Resolved.** Closed by a new "Delivery throughput and stability
      decline" bullet added to the "Costs and risks" list in
      `06-benefits-and-costs.adoc`. States DORA's 1.5% throughput decrease
      and 7.2% stability reduction, explains the "more code, less control"
      mechanism (larger batch size, downstream maintenance cost), and
      directs readers to measure throughput and stability rather than
      lines-of-code or task-completion speed, cross-referencing TS-12
      (Quality assurance) for how delivery stability is measured. Source
      added to the page's `== References`.

## Partial

(The original analysis recorded no partial-coverage items.)

## Out-of-scope

(None. The file was converted from the legacy format on 2026-08-13, which has
no concept of out-of-scope items.)

## Unresolved

(None. The file was converted from the legacy format on 2026-08-13, which has
no concept of unresolved items.)
