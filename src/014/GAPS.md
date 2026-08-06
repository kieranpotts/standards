# TS-14 gap analysis

Gaps found comparing TS-14: *Performance Testing* against the following
reference resource:

- https://blog.nelhage.com/post/reflections-on-performance/ (Nelson Elhage,
  "Reflections on software performance", 2020)

**Assessment.** Of the article's points, one was routed to TS-14:
"Performance isn't just about hot spots" (E). TS-14 is written entirely at
the level of system-level performance testing — load, soak, spike, capacity,
and scalability tests measuring end-to-end response time, throughput, and
resource utilization against thresholds, with regression detection via
baselines and CI/CD automation. It never descends to the code-profiling
level where the hot-spot-vs-diffuse-profile distinction lives: there is no
discussion of profilers, flame graphs, hot functions, or the fact that some
systems have no dominant hot spot and so cannot be sped up by localized
optimization — nor the corresponding remedy (whole-codebase techniques like
cache-optimized data structures or a lower-level implementation language that
make every line faster). The point is Missing.

**Status:** First run, 2026-08-06. One Missing gap open.

## Missing

- [ ] https://blog.nelhage.com/post/reflections-on-performance/ ("Performance
      isn't just about hot spots") is not addressed anywhere in the standard.
      The reference argues that some systems (compilers/typecheckers like
      Sorbet) have very few hot spots — time is diffuse, spread evenly across
      major passes — so you can't make a slow typechecker fast by optimizing
      hot spots since there aren't any; instead, techniques like cache-optimized
      data structures or writing in C++ make *every* line faster in a way that
      adds up across the whole application, and SQLite 3.8.7 got 50% faster via
      many stacked improvements each under 1%. TS-14 covers system-level
      metrics (response time p50/p95/p99, throughput, utilization at
      `02-performance-testing.adoc:14-28`), drift/baseline regression
      detection (`:30-40,69-74`), and "monitor all layers … to identify where
      bottlenecks occur" (`:79-80`), but never discusses profiling, hot-spot
      vs diffuse/flat profiles, the limits of profile-and-optimize-hotspots,
      or whole-codebase techniques (data structures, implementation language)
      that make every line faster. The "bottlenecks" framing (`:79-80`,
      `01-shift-left.adoc:13-19`, `03-capacity-testing.adoc`) is load-driven,
      not profile-driven. Recommend a new "Profiling and hot spots" subsection
      in `02-performance-testing.adoc` covering profilers/flame graphs, the
      hot-spot-vs-diffuse-profile distinction, and the limits of hot-spot
      optimization. Note: the whole-codebase techniques (data structures,
      language choice) border on TS-7 (Code Design) and TS-2 (Software Design
      Qualities).

## Partial

(None identified in this run.)

## Out-of-scope

(None identified in this run.)

## Unresolved

(None.)