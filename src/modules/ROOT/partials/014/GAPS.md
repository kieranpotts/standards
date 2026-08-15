# TS-14 gap analysis

Gaps found comparing TS-14: Performance testing against the following
reference resources:

- https://blog.nelhage.com/post/computers-can-be-understood/
- https://newsletter.posthog.com/p/how-we-choose-technologies

**Assessment.** Both sources identify practices adjacent to, rather than
inside, TS-14's stated scope of testing quality attributes: reasoning across
stack layers to diagnose performance, and benchmarking candidate technologies
before adoption. Converted from the legacy format on 2026-08-13.

**Status:** 2 of 2 original actionable gaps closed (2026-08-13). Added a
"Diagnosing across abstraction layers" subsection to
`02-performance-testing.adoc`. Resolved the second gap by cross-reference:
the content already exists in TS-3 (Design docs). On 2026-08-15 one new
Missing item was routed in from TS-39's Out-of-scope review (CI/Axe
accessibility-testing tooling configuration), not yet closed.

## Missing

- [x] https://blog.nelhage.com/post/computers-can-be-understood/ says
      reasoning about performance often demands understanding multiple stack
      layers — you can't write efficient Python without some grasp of the
      CPython implementation, and cache-efficient C requires understanding
      generated code and the hardware. The gap: the standards cover
      performance as a quality to specify and test, but not the practice of
      understanding lower layers of the stack to diagnose and optimize
      performance. Coverage check: TS-14 is about testing performance and
      other NFRs. TS-2 (Software design qualities) frames performance as an
      architecturally-significant NFR. Neither addresses the engineering
      practice of digging through implementation layers to reason about and
      improve performance. Recommend a new section in
      `02-performance-testing.adoc`. Cross-references: TS-2 (Software design
      qualities).

      **Resolved.** Closed by a new "Diagnosing across abstraction layers"
      subsection in `02-performance-testing.adoc`, extending the existing
      "Performance testing" section rather than adding a section of its own.
      States that a performance test reports a symptom, not a cause, and
      that finding the cause requires reasoning about the layers below the
      one where the symptom appeared — runtime/interpreter, generated code,
      OS scheduling and I/O, hardware cache and memory. Gives four practices:
      profiling before hypothesizing, keeping one mental model per layer,
      reproducing the symptom at the smallest layer that shows it, and
      growing the capability deliberately through pairing rather than hiring
      for it. Source added to the page's `== References`.

- [ ] `__TODO__/039/html/_accessibility testing checklist.txt:7` (routed in
      from TS-39's Out-of-scope review, 2026-08-15) — CI/Axe automated
      accessibility-testing tooling configuration on the `dev` branch.
      TS-39 judged this HTML-authoring-adjacent but out of its own scope
      (process/tooling, not a markup rule); TS-18's `AGENTS.md` already
      states accessibility-testing process is covered by TS-14, so the
      user directed it here rather than dropping it. Recommend a new
      subsection in `06-accessibility-testing.adoc` covering
      CI-integrated automated accessibility scanning (Axe or equivalent)
      as a testing-pipeline practice. Not yet written into any partial.

- [ ] `__TODO__/018/web-clients/_todo/0300-accessibility.md:60` (Testing)
      (routed in from TS-18's Out-of-scope review, 2026-08-15) — the
      assistive-technology test matrix (JAWS, VoiceOver, NVDA, ZoomText,
      Dragon) and the manual/automated accessibility audit process. TS-18
      (Web GUIs)'s own `AGENTS.md` already states accessibility-testing
      process is covered by TS-14, matching the earlier CI/Axe item above.
      Recommend extending `06-accessibility-testing.adoc` with the AT
      test-matrix and audit-process content, alongside the CI/Axe
      subsection. Not yet written into any partial.

## Partial

- [x] https://newsletter.posthog.com/p/how-we-choose-technologies says teams
      evaluate technologies "as close to reality as possible" — building
      proof-of-concepts tested with real slow queries, mirroring live
      traffic to project costs/performance. The gap: no guidance on
      benchmarking candidate technologies against realistic production
      workloads as part of a technology-selection process. Coverage check:
      TS-14 is concerned with testing the quality attributes of your own
      system, not with benchmarking third-party candidate technologies
      before adoption. Recommend placing in TS-3 (Design docs), not TS-14.
      Cross-references: TS-3 (Design docs).

      **Resolved.** Closed by TS-3's `03-requests-for-comments.adoc`,
      "Evaluating candidate technologies" section — this content belongs to
      TS-3's RFC/technology-selection process, not to TS-14's testing scope,
      confirmed by re-reading both standards during this run. That section
      already covers testing candidates against realistic workloads,
      mirroring live traffic, bounding the evaluation, and recording the
      result, and it already cross-references TS-14 for the underlying
      testing methodology. No content written in TS-14; the gap was closed
      by prior work in the other standard, not by this run.
