# GAPS — TS-12 Quality Assurance

Coverage gaps identified by comparing external sources against this standard.

---

## Debugging as a discipline

- **Source**: https://blog.nelhage.com/post/computers-can-be-understood/
- **What the source says**: The trickiest bugs span multiple abstraction layers and require moving between layers to root-cause. With strong mental models, engineers can sometimes "single-shot" a bug from a single observation by reasoning forward and backward through system state.
- **Coverage check**: A search for "debug" across all standards finds only incidental mentions (debuggers listed as a tool, `--debug` flags, "difficult to debug" asides). No standard covers debugging methodology: forming/refining hypotheses, cross-layer investigation, reading core dumps, or reasoning backward from observations.
- **Gap**: No guidance on debugging practice — how to systematically investigate bugs, especially cross-layer bugs, or how to use observations to form and test hypotheses.
- **Cross-references**: TS-57 (Logging, Monitoring, Observability)

---

## "Do the easy thing first" before deep investigation

- **Source**: https://blog.nelhage.com/post/computers-can-be-understood/
- **What the source says**: Try the trivial fix first (upgrade the pinned dependency, reproduce against a debug build, use the debugger) before investing in deep source spelunking.
- **Coverage check**: TS-12 has no debugging-triage guidance. TS-9 covers version pinning but not as a debugging heuristic.
- **Gap**: No standard captures the practical heuristic of escalating from cheap fixes to expensive deep investigation.
- **Cross-references**: TS-9 (Version Control)

---

## AI's negative impact on delivery throughput and stability

- **Source**: https://refactoring.fm/p/code-quality-in-the-age-of-ai
- **What the source says**: The 2024 DORA report finds that AI adoption, while increasing individual productivity, is accompanied by an estimated 1.5% decrease in delivery throughput and a 7.2% reduction in delivery stability — the gains in coding throughput do not translate into delivery-performance improvements.
- **Coverage check**: TS-12's quality-culture and quality-metrics sections do not reference AI's effect on delivery metrics. TS-61's costs section covers strategic costs conceptually but does not name the DORA-documented delivery-performance decline.
- **Gap**: No standard names the empirically observed risk that AI adoption can reduce delivery throughput and stability as an explicit cost.
- **Cross-references**: TS-61 (AI Tools)

---

## Technical debt classification and prioritization

- **Source**: https://zarar.dev/good-software-development-habits/
- **What the source says**: Technical debt falls into three types: (1) blocking now, (2) will block later, (3) might block later. Minimize #1, focus on #2, ignore #3.
- **Coverage check**: TS-12's definition-of-done mentions debt accumulating silently when "done" is ambiguous, but does not categorize debt into types or give a prioritization rule.
- **Gap**: No classification of technical debt into types and no prioritization guidance.
- **Cross-references**: TS-8 (Issue Tracking)

---

## "Put people first" as a design principle

- **Source**: https://nocomplexity.com/documents/0complexity/0cxdesignprinciples.html
- **What the source says**: Systems exist to serve humans and are maintained by humans; organizational culture should prioritize people over profits, the business must not rely on a small group of people, knowledge transfer must be seamless, and safety should come before optimization.
- **Coverage check**: TS-12's Quality Culture covers shared ownership, blameless post-mortems, and developer education, but does not frame "people first" as a first-class design principle spanning safety, organizational resilience, and human-centric design.
- **Gap**: No standard treats prioritizing people (culture, safety, knowledge transfer, avoiding bus-factor) as an architectural/design principle.
- **Cross-references**: TS-2 (Software Design Qualities), TS-3 (Design Docs)

---

## Defining tangible, measurable complexity criteria

- **Source**: https://nocomplexity.com/documents/0complexity/0cxdesignprinciples.html
- **What the source says**: Define context-specific, tangible, measurable criteria to check that a system is not getting too complex — e.g. component counts, interface counts, change cost, MTTR, disaster recovery time.
- **Coverage check**: TS-12 defines MTTR, MTTD, lead time, cycle time as quality/process metrics, but not as complexity-design criteria.
- **Gap**: No standard prescribes defining tangible, context-specific complexity criteria as a design-steering mechanism.
- **Cross-references**: TS-2 (Software Design Qualities)