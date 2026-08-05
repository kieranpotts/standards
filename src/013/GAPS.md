# TS-13 gap analysis

Gaps found comparing TS-13: *Functional Testing* against the following reference
resources (expanded from GitHub issue kieranpotts/standards#59 "Testing"):

- https://abseil.io/resources/swe-book/html/ch13.html#test_doubles (Google SWE Book, Ch. 13: Test Doubles)
- https://abseil.io/resources/swe-book/html/ch12.html#preventing_brittle_tests (Google SWE Book, Ch. 12: Unit Testing)
- https://blog.appsignal.com/2024/10/16/best-testing-practices-in-nodejs.html (AppSignal: Best Testing Practices in Node.js)
- https://www.youtube.com/watch?v=YAZr3LsCzn0 (YouTube: "When Behaviour Driven Development Goes WRONG!" — Dave Farley; compared against creator description only)
- https://www.youtube.com/watch?v=QFCHSEHgqFE (YouTube: "Don't Do E2E Testing!" — Dave Farley; compared against creator description only)
- https://en.wikipedia.org/wiki/Behavior-driven_development (Wikipedia: Behavior-driven development)
- https://newsletter.fractionalarchitect.io/p/36-verify-before-deploy-load-testing (Fractional Architect: Verify Before Deploy — Load Testing)

**Assessment.** The two Google SWE Book chapters overlap heavily with TS-13's
stated scope (test doubles, test design, brittleness) and surface several
specific techniques the standard does not name outright. The Wikipedia BDD
article adds canonical BDD vocabulary and structure that TS-13's BDD section
alludes to but does not spell out. The AppSignal blog and the Fractional
Architect newsletter are largely either already covered, tooling-specific, or
out of scope (performance testing). The two YouTube videos could only be
compared against their descriptions, so any claims made only in the spoken
audio could not be verified.

**Status:** First run, 2026-08-05. All gaps below are newly identified and open.

## Missing

- [ ] [SWE Book Ch. 12, "Write Clear Failure Messages"](https://abseil.io/resources/swe-book/html/ch12.html)
      — guidance that assertion failure messages should distinguish expected
      from actual state and include relevant parameters, and that good
      assertion libraries (eg. Truth) produce richer messages than bare
      boolean asserts — is not addressed anywhere in the standard. Recommend
      placing at `src/013/07-test-design.adoc` (new subsection under
      Readability, after the one-assertion guideline).

- [ ] [SWE Book Ch. 12, "Tests and Code Sharing: DAMP, Not DRY"](https://abseil.io/resources/swe-book/html/ch12.html)
      — the principle that test code should favour DAMP (Descriptive And
      Meaningful Phrases) over DRY, tolerating duplication when it makes tests
      clearer — is not addressed anywhere in the standard. Recommend placing
      at `src/013/07-test-design.adoc` (new subsection).

- [ ] [SWE Book Ch. 12, "Shared Values / Shared Setup / Shared Helpers / Test Infrastructure"](https://abseil.io/resources/swe-book/html/ch12.html)
      — concrete patterns for sharing code across tests (builder/factory
      helpers with defaults, when `@Before` setup helps vs. hides state,
      focused single-concept validation helpers, and treating cross-suite
      test infrastructure as its own product with its own tests) — is not
      addressed anywhere in the standard. Recommend placing at
      `src/013/07-test-design.adoc` or a new `09-test-organization.adoc`.

- [ ] [Wikipedia: Behavior-driven development — "Behavioral specifications"](https://en.wikipedia.org/wiki/Behavior-driven_development#Behavioral_specifications)
      — the canonical user-story structure (Title, Narrative with "As a / I
      want / so that", Acceptance criteria with Given/When/Then) — is not
      shown anywhere in the standard, even though BDD is the RECOMMENDED
      approach to acceptance tests. Recommend placing at
      `src/013/03-test-levels.adoc:229` (the BDD subsection).

- [ ] [Wikipedia: Behavior-driven development — "The three amigos"](https://en.wikipedia.org/wiki/Behavior-driven_development#The_three_amigos)
      — the "three amigos" / specification workshop practice (business,
      development, and testing roles collaborating to define the requirement
      and identify missing specifications before implementation) — is not
      addressed anywhere in the standard. Recommend placing at
      `src/013/03-test-levels.adoc:229` (the BDD subsection).

- [ ] [Wikipedia: Behavior-driven development — "Story versus specification"](https://en.wikipedia.org/wiki/Behavior-driven_development#Story_versus_specification)
      — the distinction between story-based BDD (business-facing) and
      specification-based BDD (lower-level, component-facing, often a
      replacement for free-form unit testing) — is not addressed anywhere in
      the standard. Recommend placing at `src/013/03-test-levels.adoc:229`
      (the BDD subsection) or `src/013/08-test-architecture.adoc`.

- [ ] [AppSignal blog, "9. Use Property-Based Testing"](https://blog.appsignal.com/2024/10/16/best-testing-practices-in-nodejs.html)
      — property-based testing (automatically generating large numbers of
      input combinations to find edge cases a hand-picked set would miss) —
      is not addressed anywhere in the standard. Recommend placing at
      `src/013/02-test-types.adoc` (new subsection) or
      `src/013/04-test-coverage.adoc`.

- [ ] [AppSignal blog, "6. Use a Dedicated Database in Each Test" + "7. Define an Effective Data Clean Strategy"](https://blog.appsignal.com/2024/10/16/best-testing-practices-in-nodejs.html)
      — test data isolation (a dedicated database/state per test to prevent
      cross-test contamination) and deliberate data-cleaning strategy (and
      the rule not to clean up after a failing test, to aid debugging) — is
      not addressed anywhere in the standard. Recommend placing at
      `src/013/07-test-design.adoc` (new subsection, under the
      Independence/Repeatable guidance) or `src/013/08-test-architecture.adoc`.

## Partial

- [ ] [SWE Book Ch. 13, "Seams" + "Mocking Frameworks"](https://abseil.io/resources/swe-book/html/ch13.html#test_doubles)
      covers this more thoroughly than `src/013/05-test-doubles.adoc:1` —
      specifically, it names "seams" and dependency injection as the
      structural mechanism that makes code testable, and discusses mocking
      frameworks (Mockito, etc.) as a tool category with specific overuse
      risks. TS-13 discusses testability only indirectly (a Feathers quote in
      `06-test-driven-development.adoc`) and mentions mocking frameworks only
      in passing.

- [ ] [SWE Book Ch. 13, "Prefer State Testing Over Interaction Testing" + "When Is Interaction Testing Appropriate?"](https://abseil.io/resources/swe-book/html/ch13.html#test_doubles)
      covers this more thoroughly than `src/013/05-test-doubles.adoc:105` —
      specifically, it articulates a state-testing-vs-interaction-testing
      distinction with explicit guidance to prefer state testing, and to
      restrict interaction testing to state-changing functions while avoiding
      overspecification. TS-13 discusses over-mocking and brittleness but
      does not frame the choice as state vs. interaction testing or give the
      state-changing-function rule.

- [ ] [SWE Book Ch. 13, "Fakes Should Be Tested"](https://abseil.io/resources/swe-book/html/ch13.html#test_doubles)
      covers this more thoroughly than `src/013/05-test-doubles.adoc:172` —
      specifically, it describes contract tests: running the same tests
      against both the real implementation and the fake to keep them in sync.
      TS-13 states "fakes should have their own tests!" but does not describe
      the contract-test mechanism.

- [ ] [SWE Book Ch. 13, "Real Implementations" (classical vs. mockist testing)](https://abseil.io/resources/swe-book/html/ch13.html#test_doubles)
      covers this more thoroughly than `src/013/05-test-doubles.adoc:148` —
      specifically, it names the two schools (classical testing vs. mockist
      testing) and explains why mockist testing is hard to scale. TS-13
      recommends high-fidelity/minimal-mocking without naming or contrasting
      the two schools.

- [ ] [SWE Book Ch. 12, "Strive for Unchanging Tests"](https://abseil.io/resources/swe-book/html/ch12.html#preventing_brittle_tests)
      covers this more thoroughly than `src/013/05-test-doubles.adoc:129` and
      `src/013/07-test-design.adoc:1` — specifically, it gives the framework
      of four kinds of production-code change (pure refactoring, new feature,
      bug fix, behavior change) and which of them should require a test
      change. TS-13 discusses brittle tests but does not articulate this
      "when is a test allowed to change?" framing.

- [ ] [SWE Book Ch. 12, "Test via Public APIs"](https://abseil.io/resources/swe-book/html/ch12.html#preventing_brittle_tests)
      covers this more thoroughly than `src/013/02-test-types.adoc:46`
      (behavioral testing) — specifically, it makes "test via the public API,
      not implementation details" an explicit brittleness-prevention rule with
      rules of thumb for what counts as a unit's public API. TS-13 frames
      black-box testing as a test type but does not connect it to
      brittleness-prevention or define "public API" for a unit.

- [ ] [SWE Book Ch. 12, "Test Behaviors, Not Methods"](https://abseil.io/resources/swe-book/html/ch12.html#preventing_brittle_tests)
      covers this more thoroughly than `src/013/07-test-design.adoc:109` (one
      assertion per test) — specifically, it explains the many-to-many
      mapping between methods and behaviors as the reason to organize tests
      around behaviors. TS-13's one-assertion guideline reaches a similar
      outcome but does not articulate the behaviors-not-methods principle.

- [ ] [Wikipedia: Behavior-driven development — "Specification as a ubiquitous language"](https://en.wikipedia.org/wiki/Behavior-driven_development#Specification_as_a_ubiquitous_language)
      covers this more thoroughly than `src/013/03-test-levels.adoc:229` —
      specifically, it grounds BDD's shared language in domain-driven design's
      "ubiquitous language" and explains BDD's origin as a combination of TDD
      with DDD and object-oriented analysis/design. TS-13 speaks of "the
      language of the business domain" but does not name ubiquitous language
      or the DDD/OOAD lineage.

- [ ] [Wikipedia: Behavior-driven development — overview / "executable specification" → "Living Documentation"](https://en.wikipedia.org/wiki/Behavior-driven_development#Overview)
      covers this more thoroughly than `src/013/03-test-levels.adoc:237` —
      specifically, it uses the term "living documentation" for the
      always-up-to-date requirements that executable specifications produce.
      TS-13 describes the dual verify/document purpose but does not use the
      established term.

- [ ] [YouTube: "Don't Do E2E Testing!" (description)](https://www.youtube.com/watch?v=QFCHSEHgqFE)
      covers this more thoroughly than `src/013/03-test-levels.adoc:135`
      (system tests) — specifically, the description argues E2E tests should
      be rejected because they prevent you from controlling variables and
      synthesising inputs/collecting outputs, which ATDD/TDD/BDD rely on.
      TS-13 acknowledges that system tests are slow, expensive, and
      environmentally sensitive, and recommends keeping their number
      manageable, but does not present the "control the variables / reject
      broad-brush E2E in favour of finer-grained tests" argument. (Comparison
      is against the video description only; the spoken argument may go
      further.)

- [ ] [YouTube: "When Behaviour Driven Development Goes WRONG!" (description)](https://www.youtube.com/watch?v=YAZr3LsCzn0)
      covers this more thoroughly than `src/013/03-test-levels.adoc:229` —
      specifically, the description warns of common BDD adoption mistakes /
      antipatterns and stresses that BDD is more than writing specs in
      SpecFlow or Cucumber. TS-13 recommends BDD and gives best practices but
      does not catalog BDD antipatterns. (Comparison is against the video
      description only; the "5 mistakes" are detailed in the spoken audio,
      which could not be verified.)

## Out-of-scope

- [ ] [Fractional Architect: "Verify Before Deploy — Load Testing"](https://newsletter.fractionalarchitect.io/p/36-verify-before-deploy-load-testing)
      covers load testing, stress testing, concurrent-user modelling, and
      scheduling load tests in the deployment pipeline. This plausibly sits
      outside TS-13's stated purpose because TS-13 explicitly scopes itself to
      *functional* testing and redirects non-functional test types
      (performance) to TS-14. Flagged for the user to confirm or overrule.

- [ ] [AppSignal blog, "14. Run Performance and Stress Tests"](https://blog.appsignal.com/2024/10/16/best-testing-practices-in-nodejs.html)
      covers performance and stress testing. This plausibly sits outside
      TS-13's stated purpose because TS-13 redirects non-functional test types
      to TS-14. Flagged for the user to confirm or overrule.

- [ ] [AppSignal blog, "12. Don't Forget to Test Middleware Functions"](https://blog.appsignal.com/2024/10/16/best-testing-practices-in-nodejs.html)
      covers testing Node.js/Express middleware specifically. This
      plausibly sits outside TS-13's stated purpose because it is a
      language/framework-specific technique rather than a general functional
      testing standard. Flagged for the user to confirm or overrule.

- [ ] [AppSignal blog, "3. Include Tags with Your Test Titles"](https://blog.appsignal.com/2024/10/16/best-testing-practices-in-nodejs.html)
      covers tagging test titles (eg. `#api`, `#authentication`) for
      selective runs and search. This plausibly sits outside TS-13's stated
      purpose because it is a tooling/workflow convention rather than a
      testing principle. Flagged for the user to confirm or overrule.

- [ ] [AppSignal blog, "11. Avoid Catching Expected Errors"](https://blog.appsignal.com/2024/10/16/best-testing-practices-in-nodejs.html)
      covers a specific assertion idiom (prefer
      `expect(fn).to.throw(...)` over `try/catch`). This plausibly sits
      outside TS-13's stated purpose because it is a language-level assertion
      idiom rather than a general standard. Flagged for the user to confirm
      or overrule.

- [ ] [SWE Book Ch. 13, "@DoNotMock" case study](https://abseil.io/resources/swe-book/html/ch13.html#test_doubles)
      covers a Java-specific ErrorProne annotation. This plausibly sits
      outside TS-13's stated purpose because it is a language/tooling
      artifact. Flagged for the user to confirm or overrule.

- [ ] [SWE Book Ch. 13, hermetic servers / larger-scope testing](https://abseil.io/resources/swe-book/html/ch13.html#test_doubles)
      covers hermetic server instances and larger-scope testing that
      exercises real dependencies regardless of suitability for unit tests.
      This plausibly sits outside TS-13's stated purpose because the SWE book
      itself defers this to its next chapter ("Testing at Google Scale" /
      larger-scope testing), and TS-13's integration/system-test sections
      cover the same ground at a higher level. Flagged for the user to
      confirm or overrule.

## Unresolved

- [ ] [YouTube: "When Behaviour Driven Development Goes WRONG!"](https://www.youtube.com/watch?v=YAZr3LsCzn0)
      — the video's spoken audio could not be retrieved; comparison was made
      against the creator's description only, which lists "5 mistakes" teams
      make when adopting BDD without detailing them. Any antipatterns
      discussed only in the audio could not be verified.

- [ ] [YouTube: "Don't Do E2E Testing!"](https://www.youtube.com/watch?v=QFCHSEHgqFE)
      — the video's spoken audio could not be retrieved; comparison was made
      against the creator's description only. The full argument against E2E
      testing (and the proposed alternative approach) may go further than the
      description and could not be verified.