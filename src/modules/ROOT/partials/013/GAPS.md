# TS-13 gap analysis

Gaps found comparing TS-13: Functional Testing against the following reference
resources:

- https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md
  (Twitter Commons, Java Style Guide, "Writing testable code" and "Testing
  antipatterns" sections)

**Assessment.** The items below come from TS-33 (Java)'s gap analysis of
2026-09-19. The user confirmed them as out of scope for TS-33 and asked for
them to be recorded here. The source is Java-specific, but these points of
test design are language-neutral. Its preference for mocks over fakes is
already covered by "Trade-offs" (05-test-doubles.adoc:83), which reaches a
compatible conclusion, so it is not recorded. Its time-dependence point was
recorded against TS-47 (Dates and Times) instead. What remains is mostly
missing coverage of design for testability and of testing concurrent code,
plus two partial gaps in the FIRST principles.

**Status:** 3 missing, 2 partial, all open. Recorded: 2026-09-19.

## Missing

- [ ] https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md#writing-testable-code
      and #let-your-callers-construct-support-objects (design classes for
      testability: have callers pass in support objects such as an
      `InputStream`, rather than the class constructing them from, say, a file
      name, so a test can supply an in-memory one) are not addressed anywhere
      in the standard. "FIRST principles" (07-test-design.adoc:34, "Timely")
      notes that late tests meet code "not designed with testability in
      mind", but gives no guidance on what testable design is. Recommend a
      new section in 07-test-design.adoc, or in 08-test-architecture.adoc.
      Cross-references: TS-7 (Code Design), whose dependency-management
      chapter covers dependency injection.

- [ ] https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md#testing-multithreaded-code
      (test concurrent code without real waits: trigger scheduled tasks
      directly rather than scheduling them, inject the executor and supply a
      single-threaded one in tests, and use synchronizers such as a blocking
      queue or a countdown latch for lock-step execution where several
      threads are unavoidable) is not addressed anywhere in the standard. The
      only mention is 01-test-strategies.adoc:93, which lists concurrency
      issues as a target of negative testing. Recommend a new section in
      07-test-design.adoc. Cross-references: TS-7 (Code Design), "Testing
      concurrent code" in its concurrency chapter.

- [ ] https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md#the-hidden-stress-test
      (unit tests should not assert on performance; performance testing
      belongs in a separate, controlled environment) is not addressed
      anywhere in the standard. Recommend a short addition to "FIRST
      principles" (07-test-design.adoc:14, "Fast"), or to "What not to test"
      (04-test-coverage.adoc:72), noting that performance is a
      non-functional concern outside this standard.

## Partial

- [ ] https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md#threadsleep
      covers this more thoroughly than 07-test-design.adoc:24
      ("Repeatable") — specifically, it rules out sleeping in tests: a sleep
      encodes an assumption that something else happens meanwhile, so the
      test turns brittle when that thread is not scheduled in time, and it
      sets a fixed lower bound on the test's duration however fast the
      machine is. TS-13 says only to eliminate non-determinism from timing.

- [ ] https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md#avoid-randomness-in-tests
      covers this more thoroughly than 07-test-design.adoc:24
      ("Repeatable") — specifically, it prefers fixed input data that
      exercises known edge cases over random input, even seeded random input,
      which rarely improves coverage in practice and makes a failure hard to
      reproduce. TS-13 only says to seed randomness. The rule should be
      reconciled with property-based testing, if TS-13 covers or intends to
      cover it.

## Out-of-scope

(None.)

## Unresolved

(None. The one resource was retrieved and read in full.)
