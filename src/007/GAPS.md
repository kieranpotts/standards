# GAPS — TS-7 Code Design

Coverage gaps identified by comparing external sources against this standard.

---

## Building mental models of underlying systems and layers

- **Source**: https://blog.nelhage.com/post/computers-can-be-understood/
- **What the source says**: Rather than memorizing rules and edge cases, build a smaller model of a system's core primitives and the principles that generate its behavior (e.g. learning bash's expansion phases rather than memorizing quoting rules).
- **Coverage check**: "Mental model" appears in TS-2 (architectural mental model), TS-5 (framework mental model), and TS-14 (users' mental models), but none address the practice of modeling the underlying implementation layers of a language/library/OS to understand and debug it.
- **Gap**: No standard addresses the engineer-facing practice of constructing mental models of underlying systems as a way to understand behavior and debug.
- **Cross-references**: TS-5 (Application Architecture)

---

## Reading the source code of your dependencies

- **Source**: https://blog.nelhage.com/post/computers-can-be-understood/
- **What the source says**: Keep a checkout of your dependencies' source and read it when docs are lacking or behavior is strange; reading the source of frameworks/languages you use builds understanding and confidence.
- **Coverage check**: TS-7's dependency management discusses dependency opacity and "loss of control," framing understanding dependencies as a risk arguing for fewer dependencies. It never advises keeping a source checkout or reading dependency internals.
- **Gap**: TS-7 treats dependencies as black boxes to be isolated and minimized; it does not encourage reading dependency source as a normal, valuable engineering habit.

---

## Exception aggregation as a distinct error-handling technique

- **Source**: https://web.archive.org/web/20250315132607/https://www.16elt.com/2024/09/25/first-book-of-byte-sized-tech/
- **What the source says**: Ousterhout recommends exception aggregation — handling many exceptions with a single piece of code rather than writing distinct handlers for each — as one of three ways to reduce exception-handling complexity.
- **Coverage check**: TS-7's error handling is aligned with Ousterhout's philosophy in spirit. "Define errors out of existence" and "mask exceptions" are substantially covered. However, exception aggregation — centralizing the handling of many exception types into one place — is not addressed. The "Minimize exception types" guidance concerns reducing the number of types you throw, not consolidating where exceptions are handled.
- **Gap**: TS-7 does not address exception aggregation as a technique for reducing handling complexity.

---

## Liskov Substitution Principle (LSP)

- **Source**: https://stackoverflow.blog/2021/11/01/why-solid-principles-are-still-the-foundation-for-modern-software-architecture/
- **What the source says**: Subtypes must be substitutable for their base types without breaking expected behavior; in dynamic/FP contexts this becomes "keep the promises your function or interface declares."
- **Coverage check**: TS-7 does not address LSP anywhere. Its OO design section covers composition-over-inheritance, polymorphism, and Law of Demeter, but never mentions substitutability contracts or pre/postcondition rules. TS-36 names LSP in a single sentence for JS/TS classes, but the language-agnostic code-design standard is silent.
- **Gap**: No coverage of LSP: no statement of the substitutability contract, no guidance on precondition/postcondition strengthening/weakening, and no treatment of how the principle translates to duck-typed or FP code.

---

## Interface Segregation Principle (ISP)

- **Source**: https://stackoverflow.blog/2021/11/01/why-solid-principles-are-still-the-foundation-for-modern-software-architecture/
- **What the source says**: Clients should not be forced to depend on more than they use; split fat interfaces into role-specific ones. Modern restatement: "don't show your clients more than they need to see."
- **Coverage check**: TS-7 has no mention of ISP. The abstraction and OO-design sections discuss encapsulation and minimal interfaces in spirit but never frame role-interface segregation.
- **Gap**: TS-7 lacks ISP entirely (no role-interface guidance, no "minimize the surface clients must depend on" as a named principle).
- **Cross-references**: TS-5 (Application Architecture) — service variant (separate external/internal interfaces) also missing

---

## Open-Closed Principle (OCP)

- **Source**: https://stackoverflow.blog/2021/11/01/why-solid-principles-are-still-the-foundation-for-modern-software-architecture/
- **What the source says**: Software entities should be open for extension but closed for modification; modern restatement is "use and add to a module without rewriting it," achieved in FP via explicit hook points/overridable callbacks.
- **Coverage check**: TS-7 covers the mechanism (polymorphism over conditionals, adding new variants by implementing an interface) but never names OCP, never frames extension-without-modification as a principle, and gives no guidance on the FP/dynamic-language equivalent.
- **Gap**: OCP is not named or framed as a principle in TS-7, and the non-OO realization (hook functions, overridable callbacks, plugin-style extension) is not covered.

---

## Dependency Inversion Principle (DIP)

- **Source**: https://stackoverflow.blog/2021/11/01/why-solid-principles-are-still-the-foundation-for-modern-software-architecture/
- **What the source says**: Depend on abstractions, not concretions; in microservice terms, replace direct service-to-service calls with an abstraction such as a message bus.
- **Coverage check**: TS-7's dependency management describes dependency injection and notes it is "an application of the inversion of control principle," but does not name DIP, omits the nuance that abstractions should be owned by the high-level/policy layer, and does not discuss the adapter pattern or the message-bus application at the service level.
- **Gap**: DIP is partially covered via DI but is not named as a principle; the high-level-owns-the-abstraction rule, the adapter pattern, and the message-bus application at the service level are missing.

---

## SOLID restated for multi-paradigm / dynamic / FP languages

- **Source**: https://stackoverflow.blog/2021/11/01/why-solid-principles-are-still-the-foundation-for-modern-software-architecture/
- **What the source says**: SOLID was conceived for OO but applies beyond it; each principle is restated in terms of generic "modules" (files, exported objects, functions) with FP examples (higher-order functions, hook callbacks, duck-typed contracts).
- **Coverage check**: TS-7 is language-agnostic and uses general terms, but never references SOLID as a set, never bridges the OO-specific origins to FP/dynamic paradigms, and offers no FP equivalents.
- **Gap**: TS-7 does not present SOLID as a unified framework, nor does it translate the principles to non-OO paradigms.

---

## Not-Invented-Here (NIH) syndrome

- **Source**: https://www.simplethread.com/20-things-ive-learned-in-my-20-years-as-a-software-engineer/
- **What the source says**: Engineers default to writing code; teams reinvent wheels when good wheels already exist. Reusing existing, maintained-by-others code is often the better choice. "Beware of toxic Not Invented Here syndrome."
- **Coverage check**: TS-7's dependency management presents the build-vs-reuse trade-off but tilts toward dependency caution and the upside of building yourself. It never names or cautions against the NIH anti-pattern.
- **Gap**: No explicit caution against NIH syndrome / the tendency to reinvent wheels, balancing TS-7's current pro-build-yourself treatment of the reuse trade-off.

---

## "Make the change easy, then make the easy change" — refactoring as a two-step discipline

- **Source**: https://zarar.dev/good-software-development-habits/
- **What the source says**: Kent Beck's maxim — for each desired change, first make the change easy (which may be hard), then make the easy change. The author aims for at least half of all commits to be refactorings.
- **Coverage check**: TS-7's "boy scout rule" covers small, incremental, in-flight refactoring and warns against big refactors. However, it does not state Beck's explicit two-step sequencing as a deliberate technique, nor the heuristic of targeting a high proportion of refactor commits.
- **Gap**: The specific "make the change easy, then make the easy change" discipline and the practice of tracking a high refactor-to-feature commit ratio are not captured.
- **Cross-references**: TS-8 (Issue Tracking), TS-9 (Version Control)

---

## Creating a new module for an orphan function

- **Source**: https://zarar.dev/good-software-development-habits/
- **What the source says**: When a function has no natural home, create a new independent construct (module/class/component) rather than jamming it into an existing module where it doesn't belong; an orphan module is an acceptable outcome.
- **Coverage check**: TS-7's decomposition section discusses DRY, locality of reference, and warns against over-decomposition and premature abstraction. It does not give the converse heuristic: when a unit has no existing home, prefer creating a new independent module over forcing it into an unrelated one.
- **Gap**: The specific "create a new module for an orphan function rather than shoehorning it in" heuristic is absent.

---

## Rule of Three — copy-paste is OK once, consolidate on the third copy

- **Source**: https://zarar.dev/good-software-development-habits/
- **What the source says**: Copy-paste is acceptable once; the second time (three copies) is duplication that should be consolidated, because by then you have enough data points to form a good abstraction.
- **Coverage check**: TS-7's decomposition section advocates "write everything twice (WET) before abstracting" and extracting only when components are semantically related. This is conceptually adjacent but does not state the concrete Rule-of-Three trigger or its risk-based rationale.
- **Gap**: The explicit Rule-of-Three heuristic and its risk-based rationale (diverging implementations of near-identical logic) are not stated.

---

## Optimization as a source of over-engineering

- **Source**: https://nocomplexity.com/documents/0complexity/0cxdesignprinciples.html
- **What the source says**: Over-engineering often occurs during optimization; optimization introduces complexity and tighter coupling between components, layers, and business processes. Stop engineering when it works, but keep simplifying.
- **Coverage check**: TS-7's decomposition warns against over-decomposition and premature abstraction, but the specific warning that optimization itself tends to introduce complexity and tighter coupling is not addressed.
- **Gap**: The caution that optimization is a common source of over-engineering is not covered.
- **Cross-references**: TS-2 (Software Design Qualities)