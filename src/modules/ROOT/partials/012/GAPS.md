# TS-12 gap analysis

Gaps found comparing TS-12: Quality assurance against the following reference
resources:

- https://blog.nelhage.com/post/computers-can-be-understood/
- https://refactoring.fm/p/code-quality-in-the-age-of-ai
- https://zarar.dev/good-software-development-habits/
- https://nocomplexity.com/documents/0complexity/0cxdesignprinciples.html

**Assessment.** The sources found six gaps, five of them missing coverage
outright (debugging methodology, a debugging triage heuristic, AI's effect on
delivery metrics, technical debt classification, and two design-principle
framings borrowed from a complexity-engineering source) and none partial. File
converted from the legacy format on 2026-08-13.

**Status:** 6 of 6 actionable gaps closed (2026-08-13). Closed: debugging
methodology and the cheap-to-expensive triage heuristic (new "Debugging"
section), technical debt classification (new subsection in "Definition of
Done"), and the AI-delivery-metrics gap (already closed in TS-61, no TS-12
change needed). The two remaining gaps — "people first" as a design
principle and complexity criteria as a design-steering mechanism — were
redirected to TS-2 (Software design qualities) and closed there in a
follow-up run: the first by a new "People first" section, the second found
already covered by TS-2's own earlier work today. 0 Partial, 0 Out-of-scope,
0 Unresolved.

## Missing

- [x] https://blog.nelhage.com/post/computers-can-be-understood/ says the
      trickiest bugs span multiple abstraction layers and require moving
      between layers to root-cause; with strong mental models, engineers can
      sometimes "single-shot" a bug from a single observation by reasoning
      forward and backward through system state. The gap: no guidance on
      debugging practice — how to systematically investigate bugs, especially
      cross-layer bugs, or how to use observations to form and test
      hypotheses. Coverage check: a search for "debug" across all standards
      finds only incidental mentions (debuggers listed as a tool, `--debug`
      flags, "difficult to debug" asides); no standard covers debugging
      methodology. Recommend a new section in `partials/012/`.
      Cross-references: TS-57 (Logging, monitoring, observability).

      **Resolved.** Closed by new `07-debugging.adoc`, "Debugging" section,
      wired into `012.adoc` after "Quality metrics". Its "Cross-layer
      investigation" subsection documents the hypothesis-and-observation
      cycle: state a falsifiable hypothesis, move between layers deliberately
      rather than staying in one, reason both forward and backward, and
      refine the hypothesis on each new observation rather than discarding it.
      It also names "single-shotting" a bug as what that cycle looks like once
      internalized, and recommends capturing a successful single-shot
      diagnosis rather than treating it as luck. Cross-references TS-57
      (Logging, monitoring, observability) for the telemetry that shortens
      cross-layer investigation, and TS-9 (Version control) via the sibling
      item below. Source added to the page's `== References`.

- [x] https://blog.nelhage.com/post/computers-can-be-understood/ says to try
      the trivial fix first (upgrade the pinned dependency, reproduce against
      a debug build, use the debugger) before investing in deep source
      spelunking. The gap: no standard captures the practical heuristic of
      escalating from cheap fixes to expensive deep investigation. Coverage
      check: TS-12 has no debugging-triage guidance; TS-9 covers version
      pinning but not as a debugging heuristic. Recommend a new section in
      `partials/012/`. Cross-references: TS-9 (Version control).

      **Resolved.** Closed by the same new `07-debugging.adoc`, in its
      "Escalate from cheap to expensive" subsection, sharing the destination
      with the item above since both concern debugging practice. States a
      five-step, increasing-cost sequence — reproduce the failure, check for
      a known cause, check dependency versions, reproduce against a debug
      build, attach a debugger — and frames skipping straight to cross-layer
      investigation as itself a quality-process failure. Cross-references
      TS-9 (Version control) for dependency pinning practice. Source added to
      the page's `== References`.

- [x] https://refactoring.fm/p/code-quality-in-the-age-of-ai says the 2024
      DORA report finds that AI adoption, while increasing individual
      productivity, is accompanied by an estimated 1.5% decrease in delivery
      throughput and a 7.2% reduction in delivery stability — the gains in
      coding throughput do not translate into delivery-performance
      improvements. The gap: no standard names the empirically observed risk
      that AI adoption can reduce delivery throughput and stability as an
      explicit cost. Coverage check: TS-12's quality-culture and
      quality-metrics sections do not reference AI's effect on delivery
      metrics; TS-61's costs section covers strategic costs conceptually but
      does not name the DORA-documented delivery-performance decline.
      Recommend placing at `partials/061/`. Cross-references: TS-61 (AI
      tools).

      **Resolved.** Closed by `partials/061/06-benefits-and-costs.adoc`,
      "Delivery throughput and stability decline" bullet — not by this run.
      The standard already cites the DORA 2024 figures (1.5% throughput
      decrease, 7.2% stability reduction) verbatim and already
      cross-references TS-12 ("see TS-12: Quality assurance for how delivery
      stability is measured"). The premise that no standard names this risk
      was already false when this batch ran; TS-12 needs no reciprocal
      cross-reference because TS-61 already links out to it, and TS-12's
      MTTR/MTTD/lead-time metrics require no AI-specific caveat to remain
      correct. See `src/modules/ROOT/partials/061/GAPS.md` for whether this
      gap is also tracked there.

- [x] https://zarar.dev/good-software-development-habits/ says technical
      debt falls into three types: (1) blocking now, (2) will block later,
      (3) might block later — minimize #1, focus on #2, ignore #3. The gap:
      no classification of technical debt into types and no prioritization
      rule. Coverage check: TS-12's definition-of-done mentions debt
      accumulating silently when "done" is ambiguous, but does not categorize
      debt into types or give a prioritization rule. Recommend placing at
      `partials/012/02-definition-of-done.adoc`. Cross-references: TS-8
      (Issue tracking).

      **Resolved.** Closed by a new "Classifying technical debt" subsection
      in `02-definition-of-done.adoc`, extending the existing Definition of
      Done partial rather than adding a section of its own. States the
      three-way classification (blocking now / will block later / might block
      later), the minimize/focus/ignore prioritization rule, and recommends
      tagging tracked debt in the issue tracker with its classification.
      Cross-references TS-8 (Issue tracking). Source added to the page's
      `== References`.

- [x] https://nocomplexity.com/documents/0complexity/0cxdesignprinciples.html
      says systems exist to serve humans and are maintained by humans;
      organizational culture should prioritize people over profits, the
      business must not rely on a small group of people, knowledge transfer
      must be seamless, and safety should come before optimization. The gap:
      no standard treats prioritizing people (culture, safety, knowledge
      transfer, avoiding bus-factor) as an architectural/design principle.
      Coverage check: TS-12's Quality Culture covers shared ownership,
      blameless post-mortems, and developer education, but does not frame
      "people first" as a first-class design principle spanning safety,
      organizational resilience, and human-centric design. Recommend a new
      section, most plausibly in TS-2 rather than TS-12. Cross-references:
      TS-2 (Software design qualities), TS-3 (Design docs).

      **Resolved.** Closed by `src/modules/ROOT/partials/002/06-habitability.adoc`,
      new "People first" section, written in a TS-2 close-gaps follow-up run
      on 2026-08-13. States three principles: design against bus factor,
      design for knowledge transfer (cross-referencing TS-3), and design
      safety before optimization. TS-12's quality-culture content (shared
      ownership, blameless post-mortems) is left untouched, as this gap's
      design-principle framing belonged to TS-2's territory, not TS-12's.

- [x] https://nocomplexity.com/documents/0complexity/0cxdesignprinciples.html
      says to define context-specific, tangible, measurable criteria to check
      that a system is not getting too complex — e.g. component counts,
      interface counts, change cost, MTTR, disaster recovery time. The gap:
      no standard prescribes defining tangible, context-specific complexity
      criteria as a design-steering mechanism. Coverage check: TS-12 defines
      MTTR, MTTD, lead time, cycle time as quality/process metrics, but not
      as complexity-design criteria. Recommend a new section, most plausibly
      in TS-2 rather than TS-12. Cross-references: TS-2 (Software design
      qualities).

      **Resolved.** Closed already, as it turned out — TS-2's own earlier
      close-gaps run on 2026-08-13 had independently added exactly this
      content to `09-simplicity.adoc`'s "Interpreting the measurements"
      paragraph, prescribing component count, interface count, change lead
      time, and MTTR as tracked-trend, context-specific complexity proxies.
      Re-verified in a TS-2 follow-up run on 2026-08-13, which recorded it
      there as `**No change needed.**` No TS-12 change was needed either.

## Partial

(The original analysis recorded no partial-coverage items.)

## Out-of-scope

(Converted from the legacy format, which has no concept of out-of-scope
items; the format recorded none.)

## Unresolved

(Converted from the legacy format, which has no concept of unresolved
items; the format recorded none.)
