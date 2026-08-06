# TS-7 gap analysis

Gaps found comparing TS-7: *Code Design* against the following reference
resources (the standard's `__TODO__` directory):

- `__TODO__/programming/*.md` (local drafts: index, comments, logging, patterns, principles)
- `__TODO__/programming2/*.md` (local drafts: functions, state-management, type-systems, principles/*)
- `__TODO__/programming/_todo/patterns/*.URL` (13 web references)
- `__TODO__/programming/_todo/principles/*.URL` (32 web references)

**Assessment.** The local drafts are mostly stubs; the substantive ones
(logging, functions, state-management, type-systems, crash-only,
defensive-programming, zero-one-infinity) surface a handful of topics the
standard does not address directly. The web references are dominated by
named design principles (SOLID, GRASP, CQS, etc.) and by architectural
material (SOA, ROA, monolith, package principles) that sits outside a
low-level code-design standard. Where the standard already covers a
principle's mechanism (e.g. polymorphism-for-extension, DI, LoD) the gap is
usually that the principle is not named or that a specific nuance/heuristic is
omitted. The clearest outright gaps are CQS, ISP, and LSP — none of which the
standard addresses in any form.

**Status:** First run (2026-08-05). All gaps below remain open.

**Second run, 2026-08-06.** Re-run against Joel Spolsky's "The Law of Leaky
Abstractions" (https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/).
Three points were routed to TS-7: the Law of Leaky Abstractions (P1), the
learning-burden / working-vs-learning implication (P2), and code-generation
tools (P3). P1 and P2 are Partial — TS-7 has a "Leaky abstractions"
subsection but uses "leaky" in an interface-design sense, not Spolsky's
runtime/operational sense, and doesn't state the law that all non-trivial
abstractions leak; it acknowledges deep abstractions are hard to understand
but not the working-vs-learning/hiring argument. P3 (code-gen tools) is
Missing. One new Missing and two new Partial gaps added; all prior gaps
remain open.

**Third run, 2026-08-06.** Re-run against tef's "Write code that is easy to
delete, not easy to extend" (https://programmingisterrible.com/post/139222674273/write-code-that-is-easy-to-delete-not-easy-to).
Three themes were routed to TS-7: copy-paste/DRY trade-offs (A),
big-ball-of-mud/decomposition/loose-coupling/uniform-interfaces (B), and
error handling (C). All three Partial — TS-7 covers WET-before-DRY and
premature-abstraction avoidance, and fail-fast-at-bugs, but not the
observed-behaviour/deleteability/util-directory points (A), the
mess-first/decompose-by-what's-not-shared/uniform-interfaces points (B), or
the end-to-end principle (C). Three new Partial gaps added; all prior gaps
remain open.

**Fourth run, 2026-08-06.** Re-run against tef's "Repeat yourself, do more
than one thing, and rewrite everything" (https://programmingisterrible.com/post/176657481103/repeat-yourself-do-more-than-one-thing-and).
Two points were routed to TS-7: "repeat yourself to find abstractions" (P1)
and "gather responsibilities / modularity as limiting options for growth"
(P2). Both Partial — TS-7 covers WET/extract-don't-invent and
over-decomposition/SRP-too-rigidly as a complexity trade-off, but not the
wrong-abstraction cost asymmetry, abstraction-as-coupling-for-change,
gathering-as-simplifying-interactions, or module-defined-by-what-it-excludes.
Two new Partial gaps added; all prior gaps remain open.

**Fifth run, 2026-08-06.** Re-run against Sandi Metz's "The Wrong Abstraction"
(https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction). This is the
primary source of the "duplication is far cheaper than the wrong abstraction"
cost-asymmetry thesis already recorded above (the tef "Repeat yourself" Partial
entry). One new Missing gap added capturing what that entry doesn't: the decay
mechanism (parameter/conditional accumulation), the sunk-cost fallacy, and the
inlining remedy ("the fastest way forward is back"). All prior gaps remain
open.

## Missing

- [ ] [Command–query separation — https://en.wikipedia.org/wiki/Command%E2%80%93query_separation#lead]
      is not addressed anywhere in the standard. CQS (a method should be a
      command OR a query, never both; asking a question should not change the
      answer) is a low-level method-design rule with no coverage. Recommend a
      new subsection in `09-object-oriented-design.adoc` after "Objects and
      data structures" (~L124) or in `04-expressiveness.adoc`.

- [ ] [Interface segregation principle — https://en.wikipedia.org/wiki/Interface_segregation_principle]
      is not addressed anywhere in the standard. ISP (no code should be forced
      to depend on methods it does not use; split fat interfaces into role
      interfaces) is unaddressed despite the standard's OOP design section.
      Recommend a new subsection in `09-object-oriented-design.adoc` near the
      polymorphism / static-methods guidance (~L42-195).

- [ ] [Liskov substitution principle — https://en.wikipedia.org/wiki/Liskov_substitution_principle]
      is not addressed anywhere in the standard. LSP (subtypes must be
      substitutable for base types; preconditions cannot be strengthened,
      postconditions/invariants cannot be weakened; the history rule;
      Square/Rectangle violation) has no coverage. Recommend a new subsection
      in `09-object-oriented-design.adoc` near "Composition over inheritance"
      (~L24-40).

- [ ] [GRASP responsibility-assignment patterns — https://en.wikipedia.org/wiki/GRASP_(object-oriented_design)]
      are not addressed as a set. The standard covers one GRASP pattern
      (Polymorphism) and an adjacent idea (Law of Demeter ≈ Low Coupling), but
      the other patterns — Controller, Creator, Indirection, Information
      Expert, Pure Fabrication, Protected Variations, High Cohesion, and Low
      Coupling as a named evaluative pattern — are not addressed. Recommend a
      new subsection in `09-object-oriented-design.adoc`.

- [ ] [`__TODO__/programming/logging.md`] (log format as structured objects,
      providing context in log lines, unique error codes in
      `<AppCode>-<ErrorCode>` format, error-code documentation tables,
      per-feature error-code ranges) is not addressed anywhere in the
      standard. The standard has no logging guidance and no error-code
      convention. Recommend a new section, or placement in
      `07-error-handling.adoc` (~L106-119, "Minimize exception types"). Note:
      logging may plausibly belong in TS-57 (observability) rather than TS-7;
      flagged for the user to confirm the scope call.

- [ ] [`__TODO__/programming/principles.md` §Zero one infinity rule] is not
      addressed. The standard's "do not impose arbitrary limits on
      abstractions" (`02-abstraction.adoc`:~L115-119) concerns abstraction
      size, not the zero-one-infinity rule (forbid arbitrary limits on the
      *number of instances* of any entity). Recommend a new subsection in
      `02-abstraction.adoc` or `03-decomposition.adoc`.

- [ ] [`__TODO__/programming2/functions.md` §Output arguments] (do not use
      output arguments; all output should come from return values; mutating
      input parameters violates the principle of least surprise) is not
      addressed anywhere in the standard. Recommend placement in
      `04-expressiveness.adoc` "Syntax and control structures" (~L88-110) or a
      new subsection on function signatures.

- [ ] https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/
      ("The Law of Leaky Abstractions" — code-generation tools) is not
      addressed anywhere in the standard. The reference argues that
      code-generation / "wizzy" tools (scaffolding, GUI builders, ORMs,
      ASP.NET's abstracting hyperlink-vs-button clicks via generated
      JavaScript) promise to abstract away a layer of work, but their
      abstractions leak (eg. ASP.NET breaks if the user has JavaScript
      disabled), and the only competent response is to learn what the tool
      abstracts — hence the advice "learn how to do it manually first, then
      use the tool to save time." TS-7 has no discussion of code-generation
      tools, scaffolding, ORMs, or GUI builders and their leak trade-offs
      (a grep for `generat`, `scaffold`, `wizard`, `ORM` found nothing).
      Recommend a new "Code generation and scaffolding tools" subsection in
      `02-abstraction.adoc` (or `05-dependency-management.adoc`) covering the
      leak trade-off and the "learn it manually first" heuristic. Note: this
      may border on TS-61 (AI Tools) for AI-assisted code generation.

- [ ] https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction ("The Wrong
      Abstraction") covers the mechanism, sunk-cost pressure, and remedy for
      a wrong abstraction — beyond the cost-asymmetry thesis already recorded
      above (the tef "Repeat yourself" Partial entry) — specifically: (a) the
      *decay mechanism*: a correctly-extracted shared abstraction degrades as
      new near-fit requirements arrive and subsequent programmers add
      parameters and conditional paths to serve each case, turning a
      universal abstraction into a "condition-laden procedure interleaving
      vaguely-associated ideas" — with the diagnostic signal "if you find
      yourself passing parameters and adding conditional paths through
      shared code, the abstraction is incorrect" (TS-7 only frames
      *premature initial* extraction at `02-abstraction.adoc:144-150` and
      `03-decomposition.adoc:74-97`, never subsequent decay); (b) the
      *sunk-cost fallacy* — existing code exerts pressure to retain it, and
      the more complicated/incomprehensible (the deeper the investment), the
      more pressure to keep it; resist being driven by sunk costs and
      reframe to "this code made sense for a while, but perhaps we've learned
      all we can from it" (TS-7's posture is the opposite — it prescribes
      retaining abstractions via backwards-compatible evolution or parallel
      new versions at `02-abstraction.adoc:152-156`); and (c) the *remedy* —
      "the fastest way forward is back": re-introduce duplication by inlining
      the abstracted code back into every caller, use the parameters to
      determine each caller's subset, delete the unneeded bits, then re-
      isolate duplication and re-extract abstractions; abandon the wrong
      abstraction sooner rather than later (TS-7 has the preventive
      WET-before-abstracting at `03-decomposition.adoc:91-97` but not this
      remedial inline-then-re-extract direction). Recommend a new "When
      abstractions go wrong" subsection in `02-abstraction.adoc` covering
      the decay mechanism, the sunk-cost fallacy, and the inlining remedy.

## Partial

- [ ] [Abstraction principle — https://en.wikipedia.org/wiki/Abstraction_principle_(computer_programming)#Implications]
      covers the **rule of three** (Fowler: abstract once code is copied more
      than twice) more concretely than `03-decomposition.adoc`:~L91-97, which
      says "write everything twice (WET) before abstracting" without naming
      the rule of three or its three-copy threshold.

- [ ] [`__TODO__/programming2/functions.md` §Setters and getters] makes the
      abstraction-stability argument for separate mutation functions
      (`startLoading()`/`stopLoading()` over `setLoading(bool)`) — the two
      functions keep the interface stable when the implementation changes.
      `09-object-oriented-design.adoc`:~L95-124 discusses getters/setters only
      in the "hybrid" objects-vs-data-structures context and omits this
      abstraction-stability pattern.

- [ ] [`__TODO__/programming2/principles/defensive-programming.md` +
      https://en.wikipedia.org/wiki/Defensive_programming] cover defensive
      programming more specifically than `07-error-handling.adoc`:~L54-77 —
      validate all user input and bail out early; differentiate user errors
      from internal logic errors; treat defensive checks as an "early warning
      system" for API users; and "offensive programming" (trust internal data,
      `assert` unreachable branches rather than returning fallbacks). The
      standard states the robustness principle but omits these concrete
      practices. (Security-specific items — canonicalization, buffer
      overflow, "three rules of data security" — are out-of-scope; see below.)

- [ ] [Don't repeat yourself — https://en.wikipedia.org/wiki/Don%27t_repeat_yourself#Alternatives]
      names **AHA (Avoid Hasty Abstractions)** and the **single choice
      principle** (Meyer), which `02-abstraction.adoc`/`03-decomposition.adoc`
      cover in spirit (premature-abstraction avoidance) but do not name.

- [ ] [Composition over inheritance — https://en.wikipedia.org/wiki/Composition_over_inheritance]
      covers the diamond problem of multiple inheritance, virtual
      inheritance, and language-specific composition mechanisms (traits,
      mixins, type embedding, protocol extensions) that
      `09-object-oriented-design.adoc`:~L24-40 omits — the standard states the
      principle but not these mechanisms or the multiple-inheritance failure
      mode.

- [ ] [Coupling — https://en.wikipedia.org/wiki/Coupling_(computer_programming)]
      catalogs coupling types (data, stamp, control, content, common,
      external, temporal) and the **connascence** framework (Page-Jones: name,
      type, position, meaning; static vs dynamic), which the standard touches
      only via the Law of Demeter and "vertical consistency"
      (`09-object-oriented-design.adoc`:~L71-93, `02-abstraction.adoc`:~L166-181)
      without naming coupling types or connascence. Integration/distributed
      coupling forms are out-of-scope (see below).

- [ ] [Inversion of control — https://en.wikipedia.org/wiki/Inversion_of_control]
      covers IoC broadly (framework controls flow vs. procedural code; the
      Hollywood Principle; callbacks, event loops, template method as IoC
      patterns; event-driven dispatch). `05-dependency-management.adoc`:~L108-110
      mentions IoC only as the principle behind DI and does not explain the
      broader mechanism.

- [ ] [KISS principle — https://en.wikipedia.org/wiki/KISS_principle] names
      "keep it simple, stupid" as a design goal. The standard advocates
      avoiding over-abstraction/over-decomposition and arbitrary limits
      (`02-abstraction.adoc`, `03-decomposition.adoc`) but does not name KISS
      or frame simplicity as a primary objective.

- [ ] [Law of Demeter — https://en.wikipedia.org/wiki/Law_of_Demeter] adds the
      **"use only one dot" heuristic**, the wrapper-method proliferation cost,
      and the layered-architecture implementation that
      `09-object-oriented-design.adoc`:~L71-93 omits — the standard states the
      rule and the delegating-method fix but not the heuristic or the cost
      trade-off.

- [ ] [Open–closed principle — https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle]
      names OCP (open for extension, closed for modification). The standard
      covers the *mechanism* — polymorphism lets new variants be added without
      editing existing chains (`09-object-oriented-design.adoc`:~L62-69) — but
      does not name OCP or frame it as a principle.

- [ ] [Principle of least astonishment — https://en.wikipedia.org/wiki/Principle_of_least_astonishment]
      covers POLA for API behavior, function/method names matching behavior,
      and sensible defaults. `04-expressiveness.adoc`:~L29-87 covers
      expressive naming but does not frame least-astonishment as a principle or
      address behavior/defaults surprise.

- [ ] [Separation of concerns — https://en.wikipedia.org/wiki/Separation_of_concerns]
      names SoC and discusses cross-cutting concerns / aspect-oriented
      programming. The standard covers decomposition and single responsibility
      (`03-decomposition.adoc`) in spirit but does not name SoC or address
      cross-cutting concerns / AOP.

- [ ] [Separation of mechanism and policy — https://en.wikipedia.org/wiki/Separation_of_mechanism_and_policy]
      states the principle behind keeping configurable values out of
      implementation logic. `05-dependency-management.adoc`:~L112-125 covers
      the practice (lift configurable values high in the call stack) but not
      the underlying mechanism/policy-separation principle.

- [ ] [Single-responsibility principle — https://en.wikipedia.org/wiki/Single-responsibility_principle]
      frames SRP as "a module should be responsible to one, and only one,
      *actor*" (a stakeholder group) and "gather together the things that
      change for the same reasons." The standard uses the "one reason to
      change" formulation (`09-object-oriented-design.adoc`:~L199-202,
      `03-decomposition.adoc`) but omits the actor framing.

- [ ] [SOLID — https://en.wikipedia.org/wiki/SOLID] presents the five
      principles as a unified framework. The standard covers SRP (partial),
      OCP (via polymorphism, partial), and DIP (partial), but never references
      SOLID as a set; LSP and ISP are entirely missing (see Missing above).

- [ ] [You aren't gonna need it — https://en.wikipedia.org/wiki/You_aren%27t_gonna_need_it]
      applies YAGNI at the feature level (do not add functionality until
      necessary; DTSTCPW; depends on continuous refactoring/TDD/CI). The
      standard covers premature *abstraction* (`02-abstraction.adoc`) but not
      YAGNI for features/capabilities.

- [ ] [Overengineering — https://en.wikipedia.org/wiki/Overengineering +
      Famous laws of Software development (Knuth's "premature optimization")]
      cover feature creep and premature optimization as overengineering modes.
      The standard covers over-abstraction and over-decomposition but does not
      address feature creep or premature optimization explicitly.

- [ ] [Information hiding — https://en.wikipedia.org/wiki/Information_hiding]
      names the principle (segregate design decisions most likely to change;
      Parnas 1972) and distinguishes information hiding (principle) from
      encapsulation (technique). `02-abstraction.adoc` covers the concept
      (hide complexity behind stable interfaces, evolve backwards-compatibly)
      but does not name "information hiding" or cite Parnas.

- [ ] [`__TODO__/programming2/state-management.md`] (manage state deliberately;
      Out of the Tar Pit: state is a leading cause of complexity) is covered
      only in the concurrency context (`10-concurrency.adoc`:~L36-55, shared
      mutable state). State management as a general code-design concern is
      not addressed.

- [ ] [`__TODO__/programming2/type-systems.md`] (a good type system adds value
      with low overhead; inference/flow analysis can give dynamic-language
      feel) is touched only via value objects (`09-object-oriented-design.adoc`:~L126-156).
      General guidance on leveraging type systems is not addressed.

- [ ] [Uniform access principle — https://en.wikipedia.org/wiki/Uniform_access_principle]
      (uniform notation for stored vs computed values; attribute↔method
      conversion without changing call sites) relates to the standard's
      stable-interface guidance (`02-abstraction.adoc`) but is not named or
      addressed.

- [ ] [Dependency inversion principle — https://en.wikipedia.org/wiki/Dependency_inversion_principle]
      adds implementation nuances the standard omits: abstractions owned by
      the high-level/policy layer; the adapter pattern mediating closed
      low-level components; and the drawback that generalizing interfaces
      everywhere yields plumbing/mocks-only noise. `05-dependency-management.adoc`:~L94-110
      states the DI pattern without these nuances.

- [ ] [Loose coupling — https://en.wikipedia.org/wiki/Loose_coupling] covers
      code-level loose coupling (interface-based dependency, the four
      autonomies, measuring coupling by data-element changes). The standard
      addresses this via DI and LoD but does not name "loose coupling" or its
      forms. (Distributed/integration coupling forms are out-of-scope; see
      below.)

- [ ] https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/
      ("The Law of Leaky Abstractions") covers the runtime/operational sense
      of leakiness more directly than `02-abstraction.adoc:125` ("Leaky
      abstractions" subsection) — specifically, TS-7 uses "leaky" to mean an
      *interface-design* leak (implementation details seep into the public
      interface, forcing call-site changes), whereas Spolsky's law is that
      *all non-trivial abstractions, to some degree, are leaky* in a
      *runtime/operational* sense: the underlying system breaks through under
      real-world conditions. The reference's canonical examples are absent —
      TCP providing reliable transport over unreliable IP but leaking when
      the network is down/overloaded; 2D-array iteration hitting
      virtual-memory page faults; logically-equivalent SQL queries differing
      thousands-fold in speed (forcing the query-plan analyzer); NFS/SMB
      remote files ceasing to act local when the connection drops; C++
      `"foo" + "bar"` failing because string literals are `char*`. TS-7's
      deep-abstraction examples (`02-abstraction.adoc:86-97`) are cited as
      *good* because their complexity is fully hidden — the opposite of
      Spolsky's thesis that such hiding is never complete. Recommend
      expanding the "Leaky abstractions" subsection to state the law (all
      non-trivial abstractions leak to some degree) in the runtime/
      operational sense, with canonical examples (TCP/IP, page faults, SQL
      plans, NFS).

- [ ] https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/
      (Implications: abstractions don't simplify as much as hoped; learning
      burden) covers the working-vs-learning consequence more directly than
      `02-abstraction.adoc:7,99-106` (deep abstractions are hard to
      understand; prefer shallow ones) — specifically, the reference argues
      that *because* abstractions leak, they don't really simplify life: to
      use one competently you must still learn the underlying system, so
      abstractions save time *working* but not time *learning*; paradoxically,
      even as higher-level tools improve, becoming a proficient programmer
      gets harder (you must know the layers beneath the abstractions you
      use); and when hiring, knowing the high-level tool is insufficient
      without understanding the underlying layers. TS-7 frames
      understandability as a design heuristic for the *author* of an
      abstraction (prefer shallow abstractions), not as Spolsky's
      competence/hiring argument for the *user* of any non-trivial
      abstraction. Recommend adding the working-vs-learning distinction and
      the "users of abstractions must understand what they abstract" point to
      `02-abstraction.adoc`.

- [ ] https://programmingisterrible.com/post/139222674273/write-code-that-is-easy-to-delete-not-easy-to
      (Steps 1-2: copy-paste before abstracting; DRY trade-offs) covers
      abstraction-trade-off specifics beyond `03-decomposition.adoc:61-97`
      (tolerate duplication; "write everything twice (WET) before
      abstracting") and `02-abstraction.adoc:144-150` (avoid premature
      abstraction) — specifically: callers rely on the *observed*
      (intentional and unintentional) behaviour of an implementation, not
      what's documented (a Hyrum's-law point); "it's simpler to delete the
      code inside a function than to delete a function" (the deleteability
      framing of abstraction cost, vs TS-7's refactoring-snowball framing at
      `02-abstraction.adoc:132-137`); put utilities in a `util` *directory*
      of separate files, not a single `util` file that grows too big to
      split (TS-7 only warns the *name* `utils` is uncommunicative at
      `04-expressiveness.adoc:42`); and keep less-specific/library code
      (logging, collections — things that don't grow in scope) separate
      from app-specific code, keeping the hard-to-delete parts away from
      the easy-to-delete parts. Recommend adding these to
      `03-decomposition.adoc` / `02-abstraction.adoc`.

- [ ] https://programmingisterrible.com/post/139222674273/write-code-that-is-easy-to-delete-not-easy-to
      (Steps 5-6: big ball of mud; decomposition by what's NOT shared; loose
      coupling; uniform interfaces) covers decomposition-for-changeability
      beyond `03-decomposition.adoc:11-60,79-89` and
      `02-abstraction.adoc:144-164` — specifically: sometimes write a big
      lump of trashy code to hold the rest together (business logic is edge
      cases and quick hacks; easier to delete one big mistake than 18
      interleaved ones; "everything should be built top-down, except the
      first time" — Perlis) — TS-7's posture is the opposite (it calls
      "stream of consciousness" code a smell at `02-abstraction.adoc:176-178`);
      break code apart by what it does NOT share (isolate the
      frustrating/likely-to-change parts from each other), not by common
      functionality (TS-7 decomposes *by commonality* at
      `03-decomposition.adoc:79-85`, the inverse); each module hides a
      difficult or likely-to-change design decision (Parnas — TS-7 covers
      information hiding in concept but doesn't frame decomposition around
      *likelihood of change*); "each hard problem is only handled by one
      module — sometimes one awful component with a simple interface beats
      two requiring careful coordination"; loose coupling as
      delete/replace-ability (even hardcoding a variable once, or a CLI
      flag, can be loose coupling — TS-7's `05-dependency-management.adoc:112-125`
      pushes configurable values *up* the stack, the opposite lean); and
      uniform interfaces as loose coupling (HTTP cache/CDN, HTTP error
      codes, file systems, SQL, middleware/pipelines/filters, UNIX pipes).
      Recommend a "Decompose by what's not shared / changeability" addition
      to `03-decomposition.adoc` and a uniform-interfaces-as-loose-coupling
      note. Note: the big-ball-of-mud/mess-first angle borders on the
      exploratory/iterative methods the repo README excludes — the user may
      decide it is out-of-scope.

- [ ] https://programmingisterrible.com/post/139222674273/write-code-that-is-easy-to-delete-not-easy-to
      (Step 6: error handling — end-to-end principle, outer layers) covers
      error-handling placement beyond `07-error-handling.adoc:54-86` (fail-
      fast at bug level; UI layer catches/normalizes errors) — specifically,
      the *end-to-end principle*: error handling and recovery are best done
      at the *outer layers* of the codebase — "easier to handle failure at
      the far ends of a connection than in the middle; if every layer atop
      must handle errors anyway, why bother handling them on the inside?"
      TS-7 routes some handling to the UI layer (`07-error-handling.adoc:79-86`)
      but justifies it by preventing internal-leakage to users, not by the
      end-to-end argument, and elsewhere prescribes the *opposite* — catch
      abstraction exceptions "on immediate return… don't let the exception
      propagate up the call stack" (`07-error-handling.adoc:45-47`), i.e.
      middle-of-stack handling. Recommend articulating the end-to-end
      principle in `07-error-handling.adoc`. Note: the Erlang/OTP
      supervision-tree / fail-fast-and-restart model the article also
      describes is architectural (overlaps TS-6, Distributed System
      Design) and is already routed out-of-scope for TS-7 via the existing
      crash-only entry — flagged for the user.

- [ ] https://programmingisterrible.com/post/176657481103/repeat-yourself-do-more-than-one-thing-and
      ("Repeat yourself to find abstractions") covers the wrong-abstraction
      angle beyond `02-abstraction.adoc:144-150` (avoid premature abstraction;
      abstractions emerge piecemeal from actual usage) and
      `03-decomposition.adoc:74-97` (DRY-as-don't-copy-paste leads to
      premature abstraction and tight coupling; WET before abstracting;
      coincidental duplication shouldn't be extracted) — specifically: the
      *wrong-abstraction cost asymmetry* ("duplication is far cheaper than the
      wrong abstraction" — Sandi Metz; TS-7 warns premature abstraction
      *causes* coupling but never states a wrong abstraction is more expensive
      than the duplication it replaced); the reframing that *abstractions are
      for coupling things for change, not for code reuse* (TS-7 states the
      opposite — it defines abstraction's purpose as "code reuse" and
      "compression" at `02-abstraction.adoc:50-52`); *writing reusable code
      inside your project is preemptive optimization* (most successful
      libraries/frameworks are *extracted* from a working system, not created
      from scratch — TS-7 says libraries are extracted at
      `05-dependency-management.adoc:20-21` but doesn't frame intra-project
      reusable code as premature optimization); and the *reuse-others'-work /
      duplicate-your-own* heuristic (reuse the OS/DB/etc.; duplicate within
      your own project to find the right abstraction, then deduplicate to
      implement it; use abstractions only when sure about coupling, not for
      opportunistic reuse). Recommend adding the wrong-abstraction cost
      asymmetry and the coupling-for-change thesis to `02-abstraction.adoc`.

- [ ] https://programmingisterrible.com/post/176657481103/repeat-yourself-do-more-than-one-thing-and
      ("Gather responsibilities to simplify interactions" / "Modularity is
      about limiting the options for growth") covers the gathering and
      module-boundary angles beyond `03-decomposition.adoc:19-24,38-41`
      (over-decomposition / SRP-too-rigidly as a complexity trade-off) and
      `09-object-oriented-design.adoc:197-223` (a single cohesive method/class
      can beat several fragments that must be read together) — specifically:
      *gathering responsibilities can simplify interactions* — the only
      difference between pushing together and pulling apart is which changes
      become easier (TS-7 frames over-decomposition only as a
      complexity/understandability cost, never as gathering-for-changeability);
      the *hard-to-use / composability* angle of over-decomposition (the UNIX
      command line / "obscenely expensive watches, or bash" — many small
      interlocking pieces with no shared features create a need for a layer
      above, eg. bash aliases/scripts/spreadsheets; even with it the UI can be
      a mess — git's `checkout` does six things but shares internal
      operations, showing components can be used in very different ways;
      TS-7's over-decomposition discussion is about *reading* code, never
      *using* or *composing* it); *a module is defined by what it will never
      be responsible for, not what it's currently responsible for* — without
      exclusion rules a module grows to contain more and more of the system
      (the `util` problem; everything ends up in the MVC controller — TS-7's
      only `util` mention is that the *name* is uncommunicative at
      `04-expressiveness.adoc:42`, and the existing `util`-directory GAPS
      note is about file organization, not module-bounded-by-exclusion); and
      *modularity as keeping things apart / limiting coordination across the
      codebase* (overlaps the existing "decompose by what's NOT shared" entry
      but states the limiting-coordination framing). Recommend a
      "Gathering responsibilities" and a "Modules bounded by exclusion"
      addition to `03-decomposition.adoc`.

## Out-of-scope

- [ ] [Create, read, update and delete — https://en.wikipedia.org/wiki/Create,_read,_update_and_delete]
      covers data-persistence operations and their SQL/REST/UI mappings;
      plausibly belongs in data/API/UI standards rather than low-level code
      design. Flagged for the user to confirm.

- [ ] [In Defence of the Monolith, Parts 1 & 2 — https://www.infoq.com/articles/monolith-defense-part-1/]
      cover modular-monolith architecture, module boundaries, acyclic/stable
      dependencies principles, data ownership, and transactionality —
      architecturally-significant decisions the standard explicitly defers to
      TS-5 / TS-6.

- [ ] [Resource-oriented architecture — https://en.wikipedia.org/wiki/Resource-oriented_architecture]
      and [Resource-oriented computing — https://en.wikipedia.org/wiki/Resource-oriented_computing]
      are architectural/API styles, outside this standard's stated purpose.

- [ ] [Service-oriented architecture — https://en.wikipedia.org/wiki/Service-oriented_architecture]
      and [Web-oriented architecture — https://en.wikipedia.org/wiki/Web-oriented_architecture]
      are architectural styles, outside this standard's stated purpose.

- [ ] [Package principles — https://en.wikipedia.org/wiki/Package_principles]
      (package cohesion/coupling, organizing classes into packages) concern
      module/package structure, which the standard defers to TS-5 / TS-6.

- [ ] [design-patterns-for-humans — https://github.com/kamranahmedse/design-patterns-for-humans]
      is a catalog of GoF design patterns (Factory, Builder, Prototype,
      Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy,
      Chain of Responsibility, Command, Iterator, Mediator, Memento, Observer,
      Visitor, Strategy, State, Template Method). The standard deliberately
      sets out principles rather than a pattern catalog; only Facade is
      referenced (in dependency management). A pattern catalog plausibly sits
      outside this standard's scope.

- [ ] [`__TODO__/programming2/principles/crash-only.md`] (crash-only software,
      crash-recovery as a system design model) is an availability/architecture
      concern, outside low-level code design.

- [ ] [The Rise Of The State Machines — https://www.smashingmagazine.com/2018/01/rise-state-machines/]
      covers finite-state machines for UI state management (Redux/Stent);
      plausibly belongs in UI standards (TS-15/TS-18). The general "think in
      states not transitions" idea is borderline; flagged for the user.

- [ ] [50 Ideas That Changed My Life — https://perell.com/essay/50-ideas-that-changed-my-life/]
      is a general life/business-philosophy essay; most ideas (mimetic desire,
      Overton window, etc.) are not code design. Items already covered by the
      standard (bike-shed effect, Parkinson's law, robustness principle) are
      addressed; the remainder is out-of-scope.

- [ ] [Famous laws of Software development — https://www.timsommer.be/famous-laws-of-software-development/]
      is a collection of project-management and general laws (Brook's,
      Conway's, Hofstadter's, Pareto, Peter, Moore's, Wirth's,
      ninety-ninety). These are organizational/management concerns, not
      low-level code design. (Knuth's premature-optimization principle is
      captured under Partial above.)

- [ ] [Worse is better — https://en.wikipedia.org/wiki/Worse_is_better]
      is a software-acceptance philosophy; the standard's pragmatic stance
      aligns in spirit but "worse is better" is not a low-level code-design
      rule.

- [ ] [Zen of Python — https://en.wikipedia.org/wiki/Zen_of_Python] is a
      Python-specific idiom list; the standard is deliberately language-agnostic
      and already covers the universal ideas it overlaps (readability,
      expressiveness).

- [ ] [Syntactic sugar — https://en.wikipedia.org/wiki/Syntactic_sugar] is a
      programming-language-design concept (desugaring, expressive power) rather
      than a code-design decision; plausibly outside this standard's purpose.

- [ ] Defensive-programming security material — [https://en.wikipedia.org/wiki/Defensive_programming#Secure_programming]
      (the "three rules of data security," canonicalization, buffer-overflow
      handling, "never trust the client") is security-specific and plausibly
      belongs in TS-52 (Security) rather than TS-7.

- [ ] [Category:Software development philosophies — https://en.wikipedia.org/wiki/Category:Software_development_philosophies]
      is a Wikipedia category listing page with no substantive content of its
      own; not a comparable reference.

## Unresolved

- [ ] [oop - Worker design pattern — https://stackoverflow.com/questions/4945509/worker-design-pattern]
      could not be retrieved: Cloudflare bot challenge (HTTP 403) blocked
      automated access; the Google webcache fallback returned HTTP 429 with a
      CAPTCHA. Not included in the comparison above.

- [ ] [What State Machines Are and Why We Use Them — https://blog.smartive.ch/what-state-machines-are-and-why-we-use-them-5ea55183be09]
      could not be retrieved: the host appears unreachable or the post has
      been removed (request failed on two attempts). Not included in the
      comparison above.

- [ ] [You Are Not Google — https://blog.bradfieldcs.com/you-are-not-google-84912cf44afb]
      could not be retrieved: error sending request (host unreachable /
      blocked). Not included in the comparison above.

- [ ] [Fail-fast — https://en.wikipedia.org/wiki/Fail_fast] resolved to a
      Wikipedia disambiguation page with no substantive content; nothing to
      extract. (The fail-fast concept is partially covered by the standard's
      "bugs surface early and close to their source" in
      `07-error-handling.adoc`:~L74-77.)