# TS-57 gap analysis

Gaps found comparing TS-57: Logging, Monitoring, Observability against the
following reference resources:

- https://source.android.com/docs/setup/contribute/code-style (AOSP, Java
  code style for contributors, "Log sparingly" section)

**Assessment.** The items below come from TS-33 (Java)'s gap analysis of
2026-09-19. The user confirmed them as out of scope for TS-33 and asked for
them to be recorded here. The source is Android-specific in its mechanics,
but its logging practices are general. TS-57's "Logging" chapter is two
sentences long, so the findings are mostly missing coverage: log levels,
rate-limiting, and the cost of disabled log statements. There is one partial
gap in its rule on private data. AOSP's point that `System.out` and
`System.err` must not be used was written into TS-33 instead, since it is
Java-specific.

**Status:** 3 missing, 1 partial, all open. Recorded: 2026-09-19.

## Missing

- [ ] https://source.android.com/docs/setup/contribute/code-style#log-sparingly
      (defines five log levels by the consequence of the event: ERROR for
      something fatal and unrecoverable without drastic action, WARNING for
      something serious and unexpected but recoverable, INFO for something
      interesting with likely widespread impact, DEBUG for detail relevant to
      investigating unexpected behavior, and VERBOSE for everything else,
      logged only in debug builds) is not addressed anywhere in the standard.
      Recommend a new "Log levels" section in 01-logging.adoc, defining the
      levels in language-neutral terms.

- [ ] https://source.android.com/docs/setup/contribute/code-style#log-sparingly
      (rate-limit log statements that can repeat, so that many duplicate
      copies of the same message do not flood the log) is not addressed
      anywhere in the standard. Recommend placing in 01-logging.adoc.

- [ ] https://source.android.com/docs/setup/contribute/code-style#log-sparingly
      (a log statement below the enabled level still costs the work of
      building its message, eg. string concatenation, on production builds,
      so guard expensive messages or use a logging API that defers
      formatting) is not addressed anywhere in the standard. Recommend
      placing in 01-logging.adoc, with language-specific idioms left to the
      language standards (eg. TS-33 for Java).

## Partial

- [ ] https://source.android.com/docs/setup/contribute/code-style#log-sparingly
      covers this more thoroughly than 01-logging.adoc:4 — specifically, it
      extends the exclusion beyond personally identifiable information to any
      private information and protected content. TS-57 names PII only.

## Out-of-scope

(None.)

## Unresolved

(None. The one resource was retrieved and read in full.)
