# TS-7 gap analysis

Gaps found comparing TS-7: Code design against the following reference
resources:

- https://blog.nelhage.com/post/computers-can-be-understood/
- https://web.archive.org/web/20250315132607/https://www.16elt.com/2024/09/25/first-book-of-byte-sized-tech/
- https://stackoverflow.blog/2021/11/01/why-solid-principles-are-still-the-foundation-for-modern-software-architecture/
- https://www.simplethread.com/20-things-ive-learned-in-my-20-years-as-a-software-engineer/
- https://zarar.dev/good-software-development-habits/
- https://nocomplexity.com/documents/0complexity/0cxdesignprinciples.html

**Assessment.** The sources found two clusters of gaps: the SOLID principles
(LSP, ISP, OCP, DIP, and the framework as a whole) are largely unnamed even
where TS-7 covers adjacent mechanisms, and several habit-level heuristics
from engineering-practice retrospectives (reading dependency source,
Not-Invented-Here caution, the Rule of Three, optimization-driven
over-engineering, orphan modules, and Kent Beck's two-step refactor
discipline) are absent or only partially covered. This file was converted
from the legacy format on 2026-08-13.

**Status:** 14 of 14 actionable gaps closed (2026-08-15). All items resolved
across three runs. First run: the refactor-discipline gap (new "Make the change
easy, then make the easy change" section in `01-bike-shedding.adoc`), LSP,
ISP, and the SOLID-as-a-framework restatement (new "SOLID" section in
`09-object-oriented-design.adoc`, plus OCP and DIP named at their existing
coverage), and reading dependency source plus Not-Invented-Here syndrome (two
new sections in `05-dependency-management.adoc`). Second run: mental models
(new `11-mental-models.adoc` partial), exception aggregation (new "Aggregate
exception handling" section in `07-error-handling.adoc`), and orphan modules,
the Rule of Three, and optimization as a source of over-engineering (three
new sections in `03-decomposition.adoc`). Third run (2026-08-15): thread-safe
class design, routed in from TS-33's Out-of-scope review (new "Designing
thread-safe classes" section in `10-concurrency.adoc`). 0 out-of-scope, 0
unresolved. This file is now fully resolved.

## Missing

- [x] https://blog.nelhage.com/post/computers-can-be-understood/ says: rather
      than memorizing rules and edge cases, build a smaller model of a
      system's core primitives and the principles that generate its behavior
      (e.g. learning bash's expansion phases rather than memorizing quoting
      rules). The gap: no standard addresses the engineer-facing practice of
      constructing mental models of underlying systems as a way to
      understand behavior and debug. Coverage check: "mental model" appears
      in TS-2 (architectural mental model), TS-5 (framework mental model),
      and TS-14 (users' mental models), but none address modeling the
      underlying implementation layers of a language/library/OS. Recommend a
      new section in TS-7. Cross-references: TS-5 (Application architecture).

      **Resolved.** Closed by a new `11-mental-models.adoc` partial,
      appended after "Concurrency." States the case for building a small,
      generative mental model of a system's core primitives over memorizing
      rules and edge cases (using the bash-expansion-phases example from the
      source), covers what a useful model captures, cross-references
      "Reading dependency source" as one of the most effective ways to build
      an accurate model, and notes where investing in a model pays off and
      how it changes debugging. Source added to the page's `== References`.

- [x] https://stackoverflow.blog/2021/11/01/why-solid-principles-are-still-the-foundation-for-modern-software-architecture/
      says: subtypes must be substitutable for their base types without
      breaking expected behavior; in dynamic/FP contexts this becomes "keep
      the promises your function or interface declares." The gap: no
      statement of the substitutability contract, no guidance on
      precondition/postcondition strengthening/weakening, and no treatment
      of how the principle translates to duck-typed or FP code. Coverage
      check: TS-7 does not address LSP anywhere; its OO design section
      covers composition-over-inheritance, polymorphism, and Law of Demeter,
      but never mentions substitutability contracts. TS-36 names LSP in a
      single sentence for JS/TS classes, but the language-agnostic
      code-design standard is silent. Recommend placing at
      `09-object-oriented-design.adoc`.

      **Resolved.** Closed by a new "Liskov Substitution Principle"
      subsection under the new "SOLID" section in
      `09-object-oriented-design.adoc`. States the substitutability
      contract (no strengthened preconditions, no weakened postconditions),
      extends it to duck-typed/FP code as "keep the promises the interface
      declares," and names the type-check-before-calling code smell as the
      symptom of a violation. Source added to the page's `== References`.

- [x] https://stackoverflow.blog/2021/11/01/why-solid-principles-are-still-the-foundation-for-modern-software-architecture/
      says: clients should not be forced to depend on more than they use;
      split fat interfaces into role-specific ones. Modern restatement:
      "don't show your clients more than they need to see." The gap: TS-7
      lacks ISP entirely — no role-interface guidance, no "minimize the
      surface clients must depend on" as a named principle. Coverage check:
      the abstraction and OO-design sections discuss encapsulation and
      minimal interfaces in spirit but never frame role-interface
      segregation. Recommend placing at `09-object-oriented-design.adoc`.
      Cross-references: TS-5 (Application architecture) — service variant
      (separate external/internal interfaces) also missing.

      **Resolved.** Closed by a new "Interface Segregation Principle"
      subsection under the new "SOLID" section in
      `09-object-oriented-design.adoc`. States the role-specific-interface
      guidance and the coupling/testability rationale. The TS-5
      service-level variant (separate external/internal interfaces) remains
      open in TS-5's own GAPS.md — out of scope for this run. Source added
      to the page's `== References`.

- [x] https://stackoverflow.blog/2021/11/01/why-solid-principles-are-still-the-foundation-for-modern-software-architecture/
      says: SOLID was conceived for OO but applies beyond it; each principle
      is restated in terms of generic "modules" (files, exported objects,
      functions) with FP examples (higher-order functions, hook callbacks,
      duck-typed contracts). The gap: TS-7 does not present SOLID as a
      unified framework, nor does it translate the principles to non-OO
      paradigms. Coverage check: TS-7 is language-agnostic and uses general
      terms, but never references SOLID as a set, never bridges the
      OO-specific origins to FP/dynamic paradigms, and offers no FP
      equivalents. Recommend placing at `09-object-oriented-design.adoc`.

      **Resolved.** Closed by a new "SOLID" section opening
      `09-object-oriented-design.adoc`, naming all five principles and
      cross-referencing where each is already covered under a different
      name — Single Responsibility to "Keep methods and classes focused,"
      Open-Closed to "Polymorphism over conditionals" (now also naming OCP
      explicitly and covering the FP hook-point/callback equivalent),
      Dependency Inversion to "Dependency injection" in
      `05-dependency-management.adoc` (now also naming DIP explicitly, the
      high-level-owns-the-abstraction rule, the adapter pattern, and the
      message-bus application at service level) — and stating LSP and ISP
      in full as new subsections. Source added to the page's
      `== References`.

- [x] `https://www.infoworld.com/article/2165633/design-for-thread-safety.html`
      (routed in from TS-33's Out-of-scope review, 2026-08-15) —
      design-level thread-safety guidance: synchronizing critical
      sections, immutable objects, thread-safe wrappers, when to make a
      class thread-safe, and the associated performance trade-offs.
      TS-33 (Java)'s `AGENTS.md` already defers concurrency to TS-7, and
      this article's content fits `10-concurrency.adoc`, but has not yet
      been checked against that partial's current coverage or written in.

      **Resolved.** Closed by a new "Designing thread-safe classes" section
      in `10-concurrency.adoc`, directly before "Testing concurrent code."
      States the usage-driven criterion for deciding whether a class needs
      to be thread-safe, the private-field-plus-critical-section technique
      for synchronization (including the JVM's non-atomic `long`/`double`
      caveat), the trade-off of immutability (allocation/GC pressure vs.
      safety), the thread-safe-wrapper pattern for third-party or dual-mode
      classes, and the performance cost of synchronization (both
      unnecessary use and the cost of skipping it where genuinely needed).
      Cross-references "Optimization as a source of over-engineering" in
      the Decomposition section. Source added to the page's
      `== References`.

## Partial

- [x] https://blog.nelhage.com/post/computers-can-be-understood/ says: keep a
      checkout of your dependencies' source and read it when docs are
      lacking or behavior is strange; reading the source of frameworks/
      languages you use builds understanding and confidence. Coverage
      check: TS-7's dependency management discusses dependency opacity and
      "loss of control," framing understanding dependencies as a risk
      arguing for fewer dependencies. It never advises keeping a source
      checkout or reading dependency internals. The gap: TS-7 treats
      dependencies as black boxes to be isolated and minimized; it does not
      encourage reading dependency source as a normal, valuable engineering
      habit. Recommend placing at `05-dependency-management.adoc`.

      **Resolved.** Closed by a new "Reading dependency source" section in
      `05-dependency-management.adoc`, directly after "Dependency
      injection." States that isolating dependencies behind abstractions is
      not a reason to treat them as opaque, recommends keeping a local
      source checkout and reading it when docs are thin or behavior is
      strange, and extends the habit to languages and runtimes, not just
      libraries. Source added to the page's `== References`.

- [x] https://web.archive.org/web/20250315132607/https://www.16elt.com/2024/09/25/first-book-of-byte-sized-tech/
      says: Ousterhout recommends exception aggregation — handling many
      exceptions with a single piece of code rather than writing distinct
      handlers for each — as one of three ways to reduce exception-handling
      complexity. Coverage check: TS-7's error handling is aligned with
      Ousterhout's philosophy in spirit — "define errors out of existence"
      and "mask exceptions" are substantially covered — but exception
      aggregation is not addressed; "Minimize exception types" concerns
      reducing the number of types thrown, not consolidating where
      exceptions are handled. The gap: TS-7 does not address exception
      aggregation as a technique for reducing handling complexity. Recommend
      placing at `07-error-handling.adoc`.

      **Resolved.** Closed by a new "Aggregate exception handling" section
      in `07-error-handling.adoc`, directly before "Minimize exception
      types." Distinguishes aggregating handling (fewer places that contain
      recovery logic) from minimizing exception types (a smaller caller-facing
      surface), and recommends consolidating handling at a shared boundary
      when several call sites respond to failure the same way. Source added
      to the page's `== References`.

- [x] https://stackoverflow.blog/2021/11/01/why-solid-principles-are-still-the-foundation-for-modern-software-architecture/
      says: software entities should be open for extension but closed for
      modification; modern restatement is "use and add to a module without
      rewriting it," achieved in FP via explicit hook points/overridable
      callbacks. Coverage check: TS-7 covers the mechanism (polymorphism
      over conditionals, adding new variants by implementing an interface)
      but never names OCP, never frames extension-without-modification as a
      principle, and gives no guidance on the FP/dynamic-language
      equivalent. The gap: OCP is not named or framed as a principle, and
      the non-OO realization (hook functions, overridable callbacks,
      plugin-style extension) is not covered. Recommend placing at
      `09-object-oriented-design.adoc`.

      **Resolved.** Closed by extending "Polymorphism over conditionals" in
      `09-object-oriented-design.adoc` with a new paragraph naming the
      Open-Closed Principle, cross-referencing the new "SOLID" section, and
      covering the FP/dynamic-language equivalent (hook points, overridable
      callbacks accepted as parameters) as the same principle applied
      without a class hierarchy. Source added to the page's `== References`.

- [x] https://stackoverflow.blog/2021/11/01/why-solid-principles-are-still-the-foundation-for-modern-software-architecture/
      says: depend on abstractions, not concretions; in microservice terms,
      replace direct service-to-service calls with an abstraction such as a
      message bus. Coverage check: TS-7's dependency management describes
      dependency injection and notes it is "an application of the inversion
      of control principle," but does not name DIP, omits the nuance that
      abstractions should be owned by the high-level/policy layer, and does
      not discuss the adapter pattern or the message-bus application at the
      service level. The gap: DIP is partially covered via DI but is not
      named as a principle; the high-level-owns-the-abstraction rule, the
      adapter pattern, and the message-bus application at the service level
      are missing. Recommend placing at `05-dependency-management.adoc`.

      **Resolved.** Closed by extending "Dependency injection" in
      `05-dependency-management.adoc`. Names the Dependency Inversion
      Principle, states the high-level-owns-the-abstraction rule with a
      `PaymentGateway` example, and covers the adapter pattern and the
      message-bus application at the service level as DIP applied at an
      integration boundary. Cross-references the new "SOLID" section.
      Source added to the page's `== References`.

- [x] https://www.simplethread.com/20-things-ive-learned-in-my-20-years-as-a-software-engineer/
      says: engineers default to writing code; teams reinvent wheels when
      good wheels already exist; reusing existing, maintained-by-others code
      is often the better choice; "beware of toxic Not Invented Here
      syndrome." Coverage check: TS-7's dependency management presents the
      build-vs-reuse trade-off but tilts toward dependency caution and the
      upside of building yourself; it never names or cautions against the
      NIH anti-pattern. The gap: no explicit caution against NIH syndrome /
      the tendency to reinvent wheels, balancing TS-7's current pro-build-
      yourself treatment of the reuse trade-off. Recommend placing at
      `05-dependency-management.adoc`.

      **Resolved.** Closed by a new "Not-Invented-Here syndrome" section in
      `05-dependency-management.adoc`, directly after "Reading dependency
      source." Names the anti-pattern, states its costs (unmatched edge-case
      coverage, transferred maintenance burden), and balances it explicitly
      against the standard's existing learning-opportunity argument for
      building things yourself. Source added to the page's `== References`.

- [x] https://zarar.dev/good-software-development-habits/ says: Kent Beck's
      maxim — for each desired change, first make the change easy (which may
      be hard), then make the easy change; the author aims for at least half
      of all commits to be refactorings. Coverage check: TS-7's "boy scout
      rule" covers small, incremental, in-flight refactoring and warns
      against big refactors, but does not state Beck's explicit two-step
      sequencing as a deliberate technique, nor the heuristic of targeting a
      high proportion of refactor commits. The gap: the "make the change
      easy, then make the easy change" discipline and the practice of
      tracking a high refactor-to-feature commit ratio are not captured.
      Recommend placing at `01-bike-shedding.adoc` ("The boy scout rule").
      Cross-references: TS-8 (Issue tracking), TS-9 (Version control).

      **Resolved.** Closed by a new "Make the change easy, then make the
      easy change" section in `01-bike-shedding.adoc`, directly after "The
      boy scout rule." States Beck's two-step discipline as the boy scout
      rule applied deliberately at the point of greatest leverage —
      reshaping code before making the behavioral change, as two visibly
      distinct pieces of work — and states that a healthy proportion of a
      project's changes should be pure refactorings, with a low proportion
      as a warning signal. Cross-references TS-9 (Version control) for the
      commit-level mechanics of keeping the two kinds of change separate.
      This is TS-7's own angle on the maxim — the code-design technique of
      splitting a change into "make it easy" and "make the easy change" —
      distinct from TS-9's "Refactor commit discipline" subsection in
      `04-commits.adoc`, which independently closed the same source's
      version-control-practice angle: labeling and sequencing `refactor`
      commits, and targeting roughly half of a project's commits as
      refactors. TS-9's closure cross-references this item and TS-8's; TS-8
      recorded the same gap and deferred to this closure rather than
      actioning it itself (see TS-8's GAPS.md, "Not actioned — recommend
      TS-7 instead"). TS-8's own item remains open pending that
      cross-reference being completed on its side. Source added to the
      page's `== References`.

- [x] https://zarar.dev/good-software-development-habits/ says: when a
      function has no natural home, create a new independent construct
      (module/class/component) rather than jamming it into an existing
      module where it doesn't belong; an orphan module is an acceptable
      outcome. Coverage check: TS-7's decomposition section discusses DRY,
      locality of reference, and warns against over-decomposition and
      premature abstraction, but does not give the converse heuristic — when
      a unit has no existing home, prefer creating a new independent module
      over forcing it into an unrelated one. The gap: the specific "create a
      new module for an orphan function rather than shoehorning it in"
      heuristic is absent. Recommend placing at `03-decomposition.adoc`.

      **Resolved.** Closed by a new "Orphan modules" section in
      `03-decomposition.adoc`, directly after "The Rule of Three." States
      that a small standalone module with no obvious existing home is an
      acceptable outcome, and is preferable to forcing unrelated logic into
      an existing module and eroding its cohesion. Source added to the
      page's `== References`.

- [x] https://zarar.dev/good-software-development-habits/ says: copy-paste is
      acceptable once; the second time (three copies) is duplication that
      should be consolidated, because by then you have enough data points to
      form a good abstraction. Coverage check: TS-7's decomposition section
      advocates "write everything twice (WET) before abstracting" and
      extracting only when components are semantically related — this is
      conceptually adjacent but does not state the concrete Rule-of-Three
      trigger or its risk-based rationale. The gap: the explicit
      Rule-of-Three heuristic and its risk-based rationale (diverging
      implementations of near-identical logic) are not stated. Recommend
      placing at `03-decomposition.adoc`.

      **Resolved.** Closed by a new "The Rule of Three" section in
      `03-decomposition.adoc`, directly after "Don't repeat yourself."
      States the third-occurrence trigger explicitly, and the risk-based
      rationale that consolidating too early risks building an abstraction
      around an accidental resemblance before enough data points exist to
      distinguish it from a genuine shared pattern. Source added to the
      page's `== References`.

- [x] https://nocomplexity.com/documents/0complexity/0cxdesignprinciples.html
      says: over-engineering often occurs during optimization; optimization
      introduces complexity and tighter coupling between components, layers,
      and business processes; stop engineering when it works, but keep
      simplifying. Coverage check: TS-7's decomposition warns against
      over-decomposition and premature abstraction, but the specific warning
      that optimization itself tends to introduce complexity and tighter
      coupling is not addressed. The gap: the caution that optimization is a
      common source of over-engineering is not covered. Recommend placing at
      `03-decomposition.adoc`. Cross-references: TS-2 (Software design
      qualities).

      **Resolved.** Closed by a new "Optimization as a source of
      over-engineering" section in `03-decomposition.adoc`, closing the
      file. States that optimization introduces complexity and tighter
      coupling, recommends optimizing only with profiling/load-testing/
      production-metrics evidence, cross-references TS-2 (Software design
      qualities) for the broader performance trade-off, and restates the
      "stop when it works, keep simplifying" guidance. Source added to the
      page's `== References`.

## Out-of-scope

(None — the file was converted from the legacy format, which recorded no
out-of-scope items.)

## Unresolved

(None — the file was converted from the legacy format, which recorded no
unresolved items.)
