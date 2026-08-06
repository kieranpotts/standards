# GAPS — TS-2 Software Design Qualities

Coverage gaps identified by comparing external sources against this standard.

---

## Trade-offs and conflicts between quality attributes

- **Source**: https://stackoverflow.blog/2022/01/17/plan-for-tradeoffs-you-cant-optimize-all-software-quality-attributes/
- **What the source says**: Increasing one quality attribute often unavoidably decreases another (e.g. MFA improves security but reduces usability; performance optimization can reduce portability). Designers must make explicit trade-off decisions.
- **Coverage check**: TS-2 covers synergy between qualities and notes relative importance differs by domain, but does not address conflicts or trade-offs between qualities.
- **Gap**: No guidance on the inevitable conflicts/trade-offs between quality attributes or how to reason about and document the compromises accepted.
- **Cross-references**: TS-1 (Software Requirements Specification)

---

## The three symptoms of complexity as a diagnostic taxonomy

- **Source**: https://web.archive.org/web/20250315132607/https://www.16elt.com/2024/09/25/first-book-of-byte-sized-tech/
- **What the source says**: Ousterhout defines complexity through three symptoms: change amplification (a simple change requires changes in many places), cognitive load (developers must learn a lot to complete a task), and unknown unknowns (it is not obvious which code must change). He advocates a "zero-tolerance" philosophy.
- **Coverage check**: TS-2's Simplicity section discusses complexity, quotes Ousterhout, and invokes Lehman's law, but never enumerates the three specific symptoms as a named diagnostic framework.
- **Gap**: The three-symptom taxonomy (change amplification, cognitive load, unknown unknowns) is not presented as an explicit diagnostic tool.
- **Cross-references**: TS-7 (Code Design)

---

## Defining tangible, measurable complexity criteria

- **Source**: https://nocomplexity.com/documents/0complexity/0cxdesignprinciples.html
- **What the source says**: Define context-specific, tangible, measurable criteria to check that a system is not getting too complex — e.g. number of components, number of interfaces, change cost, change time, repair time (MTTR), disaster recovery time.
- **Coverage check**: TS-2's Simplicity section argues simplicity is "not a perfectly measurable property" and "requires careful, qualitative judgment rather than metrics alone." Its Coupling subsection defines measurable coupling dimensions but as a diagnostic, not as prescribed complexity criteria for steering design.
- **Gap**: No standard prescribes defining tangible, context-specific complexity criteria as a design-steering mechanism. TS-2's stance that simplicity resists measurement partially conflicts with this approach.
- **Cross-references**: TS-12 (Quality Assurance)

---

## Conway's law and organizational structure

- **Source**: https://nocomplexity.com/documents/0complexity/0cxdesignprinciples.html
- **What the source says**: Organizational overhead leads to Conway's law effects — the more people involved in a design phase, the harder it is to deliver a simple system. Keep organizations and processes simple to avoid injecting complexity into the software.
- **Coverage check**: TS-2 discusses modularity, decomposition, and coupling at the software level but does not address how organizational structure shapes the resulting architecture.
- **Gap**: The relationship between organizational structure/process simplicity and software complexity (Conway's law) is not covered.
- **Cross-references**: TS-5 (Application Architecture)

---

## Optimization as a source of over-engineering

- **Source**: https://nocomplexity.com/documents/0complexity/0cxdesignprinciples.html
- **What the source says**: Over-engineering often occurs during optimization; optimization should be considered harmful because it introduces complexity and tighter coupling between components, layers, and business processes. Stop engineering when it works, but keep simplifying.
- **Coverage check**: TS-2's Simplicity/Coupling sections cover over-engineering via excessive modularity and abstraction, but a search for "optimization" returns no matches. The specific warning that optimization itself tends to introduce complexity and tighter coupling is not addressed.
- **Gap**: The caution that optimization is a common source of over-engineering (introducing complexity and tighter coupling) is not covered.
- **Cross-references**: TS-7 (Code Design)