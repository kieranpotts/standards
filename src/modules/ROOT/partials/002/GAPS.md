# TS-2 gap analysis

Gaps found comparing TS-2: Software design qualities against the following
reference resources:

- https://stackoverflow.blog/2022/01/17/plan-for-tradeoffs-you-cant-optimize-all-software-quality-attributes/
- https://web.archive.org/web/20250315132607/https://www.16elt.com/2024/09/25/first-book-of-byte-sized-tech/
- https://nocomplexity.com/documents/0complexity/0cxdesignprinciples.html

**Assessment.** The three `nocomplexity.com` design-principles items and the
Ousterhout complexity-taxonomy item found gaps mostly in the Simplicity
section: specific diagnostic framings and prescriptions the section's general
treatment of complexity does not state explicitly. The Stack Overflow item,
already resolved, found a gap in trade-off guidance across the whole standard.
Converted from the legacy format on 2026-08-13.

Two further items below originated from a `close-gaps` run against TS-12
(Quality assurance) the same day, working the same `nocomplexity.com` source
alongside three other sources of its own. That run's agent judged both items
belonged to TS-2's design-qualities scope rather than TS-12's
quality-assurance scope, recorded them as open items in TS-12's `GAPS.md`
with a recommendation to redirect them here, and left them there for the
user to decide — the item's content was never written into TS-12. The user
confirmed the redirect; this run adds them here as new items and works them
in the same pass, following the precedent set in
`src/modules/ROOT/partials/005/GAPS.md` for gaps closed on TS-10's behalf.
See `src/modules/ROOT/partials/012/GAPS.md` for the original items, their
sources, and TS-12's re-verification notes.

**Status:** 7 of 7 actionable gaps closed (2026-08-13). The original five are
unchanged from the prior run. Of the two items redirected from TS-12: the
people-first framing (bus factor, knowledge transfer, safety before
optimization) was newly written into Habitability; the tangible
complexity-criteria item required no change, since the prior run's tangible-
complexity-metrics gap (immediately above) already closed it in substance. 0
missing, 0 partial, 0 out-of-scope, 0 unresolved.

## Missing

- [x] https://stackoverflow.blog/2022/01/17/plan-for-tradeoffs-you-cant-optimize-all-software-quality-attributes/
      says increasing one quality attribute often unavoidably decreases
      another (e.g. MFA improves security but reduces usability; performance
      optimization can reduce portability), and that designers must make
      explicit trade-off decisions. The gap: no guidance on the inevitable
      conflicts/trade-offs between quality attributes or how to reason about
      and document the compromises accepted. Coverage check: TS-2 covers
      synergy between qualities and notes relative importance differs by
      domain, but did not address conflicts or trade-offs between qualities.
      Recommend a new section in `README.adoc`.
      Cross-references: TS-1 (Software requirements specification).

      **Resolved.** Closed by a new closing section, `10-trade-offs.adoc`,
      included from `README.adoc`. Names the five recurring conflicts
      (security/experience, performance/simplicity, performance/portability,
      correctness/performance, completeness/simplicity) and gives three rules
      for resolving one: try to dissolve it before accepting it, defer to the
      priority order set by the requirements and escalate rather than
      silently override it, and record what was given up and why in a design
      doc. The README's existing synergy claim is now qualified as the
      general rather than universal case. Summarized in `AGENTS.md`; source
      added to a new `== References` section in `README.adoc`. The
      requirements-side counterpart is TS-1's new `== Prioritizing qualities`
      section.

- [x] https://web.archive.org/web/20250315132607/https://www.16elt.com/2024/09/25/first-book-of-byte-sized-tech/
      says Ousterhout defines complexity through three symptoms: change
      amplification (a simple change requires changes in many places),
      cognitive load (developers must learn a lot to complete a task), and
      unknown unknowns (it is not obvious which code must change), and
      advocates a "zero-tolerance" philosophy toward all three. The gap: the
      three-symptom taxonomy is not presented as an explicit diagnostic tool.
      Coverage check: TS-2's Simplicity section discusses complexity, quotes
      Ousterhout, and invokes Lehman's law, but never enumerated the three
      specific symptoms as a named diagnostic framework.
      Recommend placing at `09-simplicity.adoc`.
      Cross-references: TS-7 (Code design).

      **Resolved.** Closed by a new "Symptoms of complexity" subsection in
      `09-simplicity.adoc`, inserted after the introductory complexity
      discussion and before "Coupling". Names Ousterhout's three symptoms —
      change amplification, cognitive load, and unknown unknowns — with one
      diagnostic question per symptom, and states the zero-tolerance
      position: each symptom is worth reacting to at first appearance rather
      than once it accumulates. Cross-references TS-7 (Code design) for the
      code-level tactics that address change amplification specifically.
      Source added to the page's `== References`.

- [x] https://nocomplexity.com/documents/0complexity/0cxdesignprinciples.html
      says to define context-specific, tangible, measurable criteria to check
      that a system is not getting too complex — e.g. number of components,
      number of interfaces, change cost, change time, repair time (MTTR),
      disaster recovery time. The gap: no standard prescribes defining
      tangible, context-specific complexity criteria as a design-steering
      mechanism; TS-2's stance that simplicity resists measurement partially
      conflicts with this approach. Coverage check: TS-2's Simplicity section
      argues simplicity is "not a perfectly measurable property" and
      "requires careful, qualitative judgment rather than metrics alone." Its
      Coupling subsection defines measurable coupling dimensions but as a
      diagnostic, not as prescribed complexity criteria for steering design.
      Recommend placing at `09-simplicity.adoc`.
      Cross-references: TS-12 (Quality assurance).

      **Resolved.** Closed by a new paragraph at the end of the "Interpreting
      the measurements" subsection of `09-simplicity.adoc`. Reconciles the
      standard's existing qualitative stance with the source's prescription:
      simplicity as a whole resists direct measurement, but a team should
      still pick a small set of context-specific, tangible proxies —
      component count, interface count, change lead time, MTTR — and track
      their trend, not their absolute value, as an early-warning signal.
      Frames this as a complement to coupling, not a replacement for
      judgment. Source added to the page's `== References`.

- [x] https://nocomplexity.com/documents/0complexity/0cxdesignprinciples.html
      says organizational overhead leads to Conway's law effects — the more
      people involved in a design phase, the harder it is to deliver a simple
      system — and that organizations and processes should be kept simple to
      avoid injecting complexity into the software. The gap: the relationship
      between organizational structure/process simplicity and software
      complexity (Conway's law) is not covered. Coverage check: TS-2
      discusses modularity, decomposition, and coupling at the software
      level but did not address how organizational structure shapes the
      resulting architecture.
      Recommend placing at `09-simplicity.adoc`.
      Cross-references: TS-5 (Application architecture).

      **Resolved.** TS-5 (Application architecture) already covers Conway's
      law directly, quoting Conway (1967) in its "Bounded contexts and
      service interfaces" section and drawing the same practical
      implication: service boundaries drift toward team boundaries unless
      deliberately aligned. Rather than duplicate that treatment, TS-2 adds
      one paragraph to the "Coupling and the other qualities" subsection of
      `09-simplicity.adoc` naming organizational and process overhead as a
      source of complexity distinct from Conway's team-to-architecture
      effect — the source's point that more people in a design phase makes a
      simple result harder to reach regardless of team-to-service alignment —
      and cross-references TS-5 for the fuller treatment. Source added to
      the page's `== References`.

- [x] Redirected from `src/modules/ROOT/partials/012/GAPS.md`
      (TS-12: Quality assurance), where it was found against
      https://nocomplexity.com/documents/0complexity/0cxdesignprinciples.html.
      That source says systems exist to serve humans and are maintained by
      humans; organizational culture should prioritize people over profits,
      the business must not rely on a small group of people, knowledge
      transfer must be seamless, and safety should come before optimization.
      The gap: no standard treats prioritizing people (culture, safety,
      knowledge transfer, avoiding bus factor) as an architectural/design
      principle. Coverage check (from TS-12's re-verification): TS-2 had no
      bus-factor, knowledge-transfer, or "people first" framing anywhere in
      its nine design-quality sections; TS-12's Quality Culture covers the
      adjacent but narrower "shared ownership" and "blameless post-mortems"
      ground. TS-12's agent judged this a *design* principle (safety,
      organizational resilience, human-centric design), which is TS-2's
      territory, and recommended placing it here rather than in TS-12.
      Cross-references: TS-3 (Design docs).

      **Resolved.** Re-verified against TS-2's current state before writing:
      confirmed no bus-factor, knowledge-transfer, or "people first" content
      exists anywhere in the standard. Closed by a new "People first"
      subsection at the end of `06-habitability.adoc`, extending Habitability
      rather than adding a new top-level quality, since the source's concern
      is habitability applied at the scale of the team rather than the file.
      States three principles: design against bus factor (treat
      single-person knowledge of a critical part of the system as a known
      risk, not a fact to live with), design for knowledge transfer (extends
      the section's existing documentation discussion, and cross-references
      TS-3 (Design docs) for the design-rationale half of that transfer), and
      design safety before optimization (linked back to
      the existing over-engineering caution in "Interpreting the
      measurements"). Source annotation extended in the page's
      `== References` (same NoComplexity entry used by the two items closed
      in the prior run, now naming all three sections it fed).

- [x] Redirected from `src/modules/ROOT/partials/012/GAPS.md`
      (TS-12: Quality assurance), where it was found against
      https://nocomplexity.com/documents/0complexity/0cxdesignprinciples.html.
      That source says to define context-specific, tangible, measurable
      criteria to check that a system is not getting too complex — e.g.
      component counts, interface counts, change cost, MTTR, disaster
      recovery time. The gap: no standard prescribes defining tangible,
      context-specific complexity criteria as a design-steering mechanism.
      Coverage check (from TS-12's re-verification): TS-12 defines MTTR,
      MTTD, lead time, and cycle time as quality/process metrics, but not as
      complexity-design criteria; TS-2's Simplicity section discusses
      coupling as a measurable proxy for complexity at length. TS-12's agent
      recommended placing this in TS-2 rather than TS-12, noting it may
      already be partially covered there and asking this run to re-verify
      before writing. Cross-references: TS-12 (Quality assurance).

      **No change needed.** Re-verified against TS-2's current state: this
      item is fully superseded by the tangible-complexity-metrics gap this
      standard's own analysis found against the same source (see the
      "Resolved" item immediately above this one), closed in the prior run
      today as a new paragraph at the end of "Interpreting the measurements"
      in `09-simplicity.adoc`. That paragraph already states the exact
      prescription this item describes — a small set of context-specific,
      tangible proxies (component count, interface count, change lead time,
      MTTR), tracked as a trend rather than an absolute value, as a
      design-steering early-warning signal. TS-12's agent's "may already be
      partially covered" caveat undersold the prior run's coverage: it is
      fully covered, not partially. No further content needed; no source
      annotation change beyond what the prior run already made.

## Partial

(None. The original legacy-format analysis recorded no partial-coverage
items.)

## Out-of-scope

(None. The legacy format has no concept of an out-of-scope item, so the file
converted from it recorded none.)

## Unresolved

(None. The legacy format has no concept of an unresolved item, so the file
converted from it recorded none.)
