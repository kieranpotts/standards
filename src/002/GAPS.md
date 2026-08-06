# TS-2 gap analysis

Gaps found comparing TS-2: *Software Design Qualities* against the following
reference resource:

- https://www.gov.uk/guidance/government-design-principles (UK Government
  Design Principles)

**Assessment.** Of the 11 UK Government Design Principles, two were routed to
TS-2: #2 ("Do less") and #4 ("Do the hard work to make it simple"). Principle
#4 is adequately covered by TS-2's Simplicity chapter
(`09-simplicity.adoc:66-93`, `01-completeness.adoc:11-20`) and produced no
gap. Principle #2 is partially covered: TS-2 addresses reuse-over-reinvention
and minimal initial scope (MVP / worse-is-better) but is silent on the
principle's outward-facing, ecosystem-level posture — building platforms,
registers, and APIs for others to build upon, sharing work outward, and the
"only do what only you can do" scope discipline.

**Status:** First run, 2026-08-06. One Partial gap open. Principle #4
assessed as covered (no gap recorded).

**Second run, 2026-08-06.** Re-run against Nelson Elhage's "Reflections on
software performance" (https://blog.nelhage.com/post/reflections-on-performance/).
Two points were routed to TS-2: "performance is a feature" (A) and
"performance needs effort throughout the lifecycle" (C). Both Partial —
TS-2 endorses the spirit (fast software changes user behaviour and confers
competitive advantage; performance is an architecturally significant,
design-it-in-from-the-start quality) but doesn't make the under-investment /
multiplicative-tooling-cost argument, and doesn't name or rebut the specific
maxims ("premature optimization", "make it work/right/fast", "CPU time
cheaper than engineer time", "Ruby/Python fast enough") or the language-
runtime trade-off. Two new Partial gaps added; the prior gap remains open.

**Third run, 2026-08-06.** Re-run against tef's "Write code that is easy to
delete, not easy to extend" (https://programmingisterrible.com/post/139222674273/write-code-that-is-easy-to-delete-not-easy-to).
One point was routed to TS-2: the "disposable, not reusable / easy-to-delete
not easy-to-extend" thesis. Partial — TS-2 shares the changeability telos
but leans the *opposite* direction on the central claim (endorses
reuse/extensibility as goals; "Evolve, don't rewrite" rebuts Brooks' "plan
to throw one away"; says simplicity is "not about the volume of code"). One
new Partial gap added; all prior gaps remain open.

**Fourth run, 2026-08-06.** Re-run against tef's "Repeat yourself, do more
than one thing, and rewrite everything" (https://programmingisterrible.com/post/176657481103/repeat-yourself-do-more-than-one-thing-and).
One point was routed to TS-2: the "Rewrite Everything" point (the "never
rewrite" maxim and its limits; how to rewrite safely). Partial — TS-2's
"Evolve, don't rewrite" shares the anti-rewrite premise and concedes narrow
necessity, but adds no rewrite-risks catalog, safe-rewrite/parallel-run
migration strategy, second-system effect, 3-month rule, or "never rewrite in
"hurry" refinement. One new Partial gap added; all prior gaps remain open.

**Fifth run, 2026-08-06.** Re-run against Gergely Orosz's "The Product-Minded
Software Engineer" (https://blog.pragmaticengineer.com/the-product-minded-engineer/),
trait 5. One point was routed to TS-2: product/engineering tradeoffs. Partial
— TS-2 treats over-engineering/focus/minimalism as engineering-internal
quality, never framing tradeoffs against product impact/value or proposing
lower-effort alternative features for similar product value. One new Partial
gap added; all prior gaps remain open.

**Sixth run, 2026-08-06.** Re-run against Dan McKinley's "Choose Boring
Technology" (https://mcfunley.com/choose-boring-technology). One point was
routed to TS-2: the "embrace boredom" thesis. TS-2 already covers it
adequately — the cohesiveness chapter's "Boring technology" subsection
(`07-cohesiveness.adoc:39-78`) cites McKinley's essay and reproduces its
known/unknown-unknowns examples — so the only residual gap is the "innovation
tokens" budget framing. One new Partial gap added; all prior gaps remain open.

## Missing

(None identified in this run.)

## Partial

- [ ] https://www.gov.uk/guidance/government-design-principles (Principle 2,
      "Do less") covers outward sharing and scope discipline more thoroughly
      than `07-cohesiveness.adoc:69-72` (choose proven technologies, reuse
      existing solutions) and `01-completeness.adoc:11-20` (minimal viable
      product / worse-is-better) — specifically, the principle's distinctive
      claims that an organisation should "only do what only [it] can do"
      (scope discipline — deciding what to leave to others), make its work
      "reusable and shareable" outward, build "platforms and registers
      others can build upon," provide "resources (like APIs) that others
      can use," and "link to the work of others," concentrating on the
      "irreducible core." TS-2's reuse is about *consuming* others' mature
      technology to keep one's own system cohesive; it never discusses
      *producing* shared platforms/registers/APIs for other teams or
      organisations to consume, nor scope-of-organisation discipline.
      Recommend a new subsection in `07-cohesiveness.adoc` (or
      `01-completeness.adoc`) on outward shareability and ecosystem-level
      scope discipline. Note: this borders on product/organisational
      strategy; the user may decide it is out-of-scope for a software design
      qualities standard.

- [ ] https://blog.nelhage.com/post/reflections-on-performance/ ("Performance
      is a feature") covers the industry's systematic under-investment in
      performance more directly than `05-experience.adoc:27-42` (fast
      software changes user behaviour, confers competitive advantage,
      signals quality) and `09-simplicity.adoc:105-113` (speed forces
      product-focus decisions) — specifically, the reference argues that
      performance is "often given lip service but rarely given real
      investment," that "fast software is still possible and very much
      worth it" against a prevailing fast-enough mindset, and that we
      "casually give up factors of two or ten (or more) with our choices of
      tools and libraries without asking if the benefits are worth it."
      TS-2 endorses the value of speed but never frames tool/library/runtime
      selection as a performance lever with multiplicative cost, nor the
      lip-service-vs-investment gap. Recommend a short addition to
      `03-performance.adoc` (or `05-experience.adoc`) on auditing
      multiplicative performance costs of technology choices.

- [ ] https://blog.nelhage.com/post/reflections-on-performance/ ("Performance
      needs effort throughout a project's lifecycle") covers the limits of
      the "performance last" model more directly than
      `03-performance.adoc:31-48,74-82` (performance is architecturally
      significant, cross-cutting, cannot be retrofitted or achieved
      incrementally; specify up-front) and `05-experience.adoc:59-67`
      (responsiveness/performance are first-class architectural concerns,
      not afterthoughts) — specifically, the reference names and rebuts the
      common maxims ("premature optimization is the root of all evil",
      "make it work, then make it right, then make it fast", "CPU time is
      always cheaper than an engineer's time", "Ruby/Python are fast
      enough"), argues the "write it expediently, then profile and optimize
      hot spots" model "will rarely if ever produce truly fast software,"
      and discusses the language/runtime-choice trade-off. TS-2 asserts the
      contrary prescription (design performance in from the start) but
      never engages the prevailing folk wisdom it argues against, never
      names those maxims, and never treats programming-language/runtime
      selection as a performance decision. Recommend a short "Common maxims
      and their limits" addition to `03-performance.adoc` that steelmans and
      rebuts the premature-optimization / make-it-fast-last maxims and
      addresses language-runtime trade-offs.

- [ ] https://programmingisterrible.com/post/139222674273/write-code-that-is-easy-to-delete-not-easy-to
      ("Write code that is easy to delete, not easy to extend") covers the
      disposable-not-reusable thesis more directly than
      `08-changeability.adoc:1-4,116-120` (changeability is the supreme
      quality; "cheap to change") — specifically, the reference argues that
      lines of code are "lines spent" not "lines produced" (magnitude
      matters: a million-line monolith is costlier to replace than a
      ten-thousand-line one), that we should build *disposable* not reusable
      software (optimize for deletability, not extensibility), that "writing
      extensible code is hoping you got everything right in three months;
      writing deletable code is the opposite assumption," and (citing
      Brooks) "plan to throw one away." TS-2 leans the opposite way: it
      lists extensibility as a *positive* sub-quality of changeability
      (`08-changeability.adoc:237-238`), prescribes "reuse existing
      solutions in preference to building new ones" (`07-cohesiveness.adoc:68-72`),
      argues "Evolve, don't rewrite" and quotes Spolsky against throwing
      code away (`08-changeability.adoc:172-230` — a direct rebuttal of the
      Brooks citation), and states simplicity is "not about the volume of
      code" (`09-simplicity.adoc:128-130`). It also never frames the
      reuse-vs-changeability tension as a trade-off *against* reuse (the
      more consumers of an API, the harder to change) — it notes afferent
      coupling makes change expensive (`09-simplicity.adoc:149-152`) but
      treats it as a solvable constraint, not a cost of reuse. Recommend a
      "Disposability and deletability" counterpoint in `08-changeability.adoc`
      (alongside "Evolve, don't rewrite") framing code as a cost to be
      minimized/deleted and the reuse-vs-changeability trade-off, and
      revisiting the "not about the volume of code" claim.

- [ ] https://programmingisterrible.com/post/176657481103/repeat-yourself-do-more-than-one-thing-and
      ("Rewrite Everything") covers how to rewrite safely beyond
      `08-changeability.adoc:172-230` ("Evolve, don't rewrite" — rewrites are
      risky because we undervalue accumulated knowledge; replacement reserved
      for cases with no incremental path at `:188-195`) — specifically, the
      reference adds: a *risks-of-rewrite catalog* (we rarely understand what
      the previous system did — many properties are accidental, documentation
      is scarce, tests are ornamental, interfaces are organic and stubbornly
      lock behaviors in place; rewrites are usually only considered at
      breaking point, which is too late); a *safe-rewrite strategy* — plan
      migration to AND from the old system, ease in the existing load,
      handle things being in one or both places at once, continuously
      maintain both systems until one can be decommissioned (a slow, careful
      migration is the only reliable option for larger systems); start with
      the hard problems first (often performance, or the biggest customer);
      the *3-month rule* (if a replacement isn't doing something useful after
      three months, it probably never will); the *second-system effect* (the
      canonical doomed rewrite plans numerous features, implements few, and
      rarely works reliably — like writing a game engine without a game, or a
      framework without a product); and the refinement "it's more important
      to *never rewrite in a hurry* than to never rewrite at all." TS-2 only
      does the first half (concedes necessity in narrow cases) and offers no
      safe-rewrite playbook, no second-system-effect warning, and no
      time-boxing heuristic. Recommend a "Rewriting safely" subsection in
      `08-changeability.adoc` (alongside "Evolve, don't rewrite") covering
      the risks catalog, the parallel-run migration strategy, the
      second-system effect, and the 3-month rule. Note: the parallel-run
      migration strategy overlaps TS-10 (Releasing) and TS-45 (Data
      Migrations), which already have migration entries.

- [ ] https://blog.pragmaticengineer.com/the-product-minded-engineer/
      (Trait 5: "Offering product/engineering tradeoffs upfront") covers
      product-vs-engineering tradeoff evaluation more directly than
      `01-completeness.adoc:104-176` (under-/over-engineering; "how good is
      good enough" — engineering-internal quality vs speed) and
      `09-simplicity.adoc:105-113` (resist speculative features; focus on
      what users need) — specifically, the reference argues for *juggling
      product and engineering tradeoffs together, each evaluated for its
      impact on the other*: looking for engineering tradeoffs (reduce
      effort) and evaluating their *product impact*, and making *product
      tradeoffs* and evaluating their *engineering impact* — eg. proposing a
      completely different feature to build that has similar product impact
      but vastly smaller engineering effort. TS-2's tradeoffs are
      engineering-internal (correctness vs performance, consistency vs
      availability, reuse vs changeability) and its product scope guidance
      ("what users genuinely need") is a simplicity discipline, not an
      explicit product-value-vs-engineering-effort tradeoff to weigh during
      scoping. Recommend a "Product/engineering tradeoff evaluation" addition
      to `01-completeness.adoc` (or `09-simplicity.adoc`) framing engineering
      effort against product impact and proposing lower-effort alternatives
      that preserve product value. Note: this overlaps TS-3 (Design Docs),
      which records alternatives/tradeoffs in RFCs but frames them as
      technical/design tradeoffs — see `../003/GAPS.md`.

- [ ] https://mcfunley.com/choose-boring-technology ("Choose Boring
      Technology" — innovation tokens) adds the *budget* framing beyond
      TS-2's "Boring technology" subsection (`07-cohesiveness.adoc:39-78`,
      which cites this essay as "The essay that named the principle" and
      reproduces its known/unknown-unknowns examples verbatim) —
      specifically, the reference frames adoption capacity as a *fixed
      supply* of about three "innovation tokens": spending one on shiny new
      tech (NodeJS, MongoDB, brand-new service discovery, writing your own
      database) is a zero-sum choice against the company's actual mission,
      and you tend to overestimate how many you have. TS-2 frames the cost
      of adding technology as real but *unbounded* ("carries a cost that is
      easy to overlook"); it never quantifies it as a fixed budget or frames
      adoption as a token-allocation decision, and gives no concrete roster
      of boring-and-good technologies (MySQL, Postgres, PHP, Python,
      Memcached, Squid, Cron) to anchor the boring-vs-bad distinction.
      Recommend adding the innovation-tokens budget framing to the "Boring
      technology" subsection in `07-cohesiveness.adoc`.

## Out-of-scope

(None identified in this run.)

## Unresolved

(None.)