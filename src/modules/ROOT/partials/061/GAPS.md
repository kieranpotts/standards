# GAPS — TS-61 AI Tools

Coverage gaps identified by comparing external sources against this standard.

---

## AI's negative impact on software delivery throughput and stability

- **Source**: https://refactoring.fm/p/code-quality-in-the-age-of-ai
- **What the source says**: The 2024 DORA report finds that AI adoption, while increasing individual productivity, is accompanied by an estimated 1.5% decrease in delivery throughput and a 7.2% reduction in delivery stability — the gains in pure coding throughput do not translate into delivery-performance improvements. The article frames this as "more code, faster, in exchange for it being less under our control."
- **Coverage check**: TS-61's benefits-and-costs section enumerates strategic costs of AI adoption (data privacy, dependence, skill erosion, no audit trail, copyright, socio-cultural bias) and states that "the gains show up per task, while several of the costs accrue only across a team and over time." However, it never names the specific empirically observed risk that AI adoption can reduce delivery throughput and stability.
- **Gap**: TS-61's costs section is missing the DORA-documented delivery-performance decline (reduced throughput and stability) as an explicit, named strategic cost of AI adoption. The "more code, less under control" tradeoff that drives it is also not articulated as a delivery risk.
- **Cross-references**: TS-12 (Quality Assurance)