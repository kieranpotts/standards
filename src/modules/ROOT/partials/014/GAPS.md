# GAPS — TS-14 Performance testing

Coverage gaps identified by comparing external sources against this standard.

---

## Performance engineering requires multi-layer understanding

- **Source**: https://blog.nelhage.com/post/computers-can-be-understood/
- **What the source says**: Reasoning about performance often demands understanding multiple stack layers — you can't write efficient Python without some grasp of the CPython implementation, and cache-efficient C requires understanding generated code and the hardware.
- **Coverage check**: TS-14 is about testing performance and other NFRs. TS-2 frames performance as an architecturally-significant NFR. Neither addresses the engineering practice of digging through implementation layers to reason about and improve performance.
- **Gap**: The standards cover performance as a quality to specify and test, but not the practice of understanding lower layers of the stack to diagnose and optimize performance.
- **Cross-references**: TS-2 (Software design qualities)

---

## Evaluating candidate technologies against real-world conditions

- **Source**: https://newsletter.posthog.com/p/how-we-choose-technologies
- **What the source says**: Teams evaluate technologies "as close to reality as possible" — building proof-of-concepts tested with real slow queries, mirroring live traffic to project costs/performance.
- **Coverage check**: TS-14 is concerned with testing the quality attributes of your own system, not with benchmarking third-party candidate technologies before adoption.
- **Gap**: No guidance on benchmarking candidate technologies against realistic production workloads as part of a technology-selection process.
- **Cross-references**: TS-3 (Design docs)