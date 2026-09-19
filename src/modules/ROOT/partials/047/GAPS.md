# TS-47 gap analysis

Gaps found comparing TS-47: Dates and Times against the following reference
resources:

- https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md
  (Twitter Commons, Java Style Guide, "Testing antipatterns" section)

**Assessment.** The item below comes from TS-33 (Java)'s gap analysis of
2026-09-19. The user confirmed it as out of scope for TS-33 and asked for it
to be recorded here. It is a single missing topic. TS-47 is still a draft,
and covers date and time formats and timestamp width, but not how code
obtains the current time.

**Status:** 1 missing, open. Recorded: 2026-09-19.

## Missing

- [ ] https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md#time-dependence
      (code that reads the wall clock directly, eg. through `new Date()`,
      `System.currentTimeMillis()`, or `System.nanoTime()`, is hard to test
      repeatably; inject a clock abstraction instead, backed by the system
      clock in production and a controllable fake clock in tests) is not
      addressed anywhere in the standard. Recommend a new section in
      pages/047.adoc. Java's own abstraction for this is `java.time.Clock`,
      which TS-33 (Java) could reference once TS-47 covers the principle.
      Cross-references: TS-13 (Functional Testing), whose "Repeatable"
      principle (partials/013/07-test-design.adoc:24) says to control time
      in tests.

## Partial

(The analysis recorded no partial-coverage items.)

## Out-of-scope

(None.)

## Unresolved

(None. The one resource was retrieved and read in full.)
