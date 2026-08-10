# GAPS — TS-8 Issue Tracking

Coverage gaps identified by comparing external sources against this standard.

---

## Engineers contributing to the team roadmap/backlog

- **Source**: https://blog.pragmaticengineer.com/pragmatic-engineer-test/
- **What the source says**: Teams should have a roadmap/backlog, and engineers should regularly contribute to the one for their team — i.e. engineers shape planned work, not just receive it.
- **Coverage check**: TS-8 explicitly excludes roadmap/long-term-backlog management from the issue tracker's scope, deferring it to "separate project-management tools." It covers issue lifecycle, ownership, and assignment, but says nothing about whether/how engineers contribute to planning the backlog.
- **Gap**: No standard addresses engineer participation in roadmap/backlog planning. TS-8 treats roadmaps as out-of-scope.

---

## Technical debt classification and prioritization

- **Source**: https://zarar.dev/good-software-development-habits/
- **What the source says**: Technical debt falls into three types: (1) things preventing you from doing work now, (2) things that will prevent you later, (3) things that might prevent you later. Minimize #1, focus on #2, and ignore #3.
- **Coverage check**: TS-8's refactoring issue type introduces the technical-debt metaphor and asks authors to weigh short-term cost vs. long-term benefit, but does not categorize debt into types or give a prioritization rule.
- **Gap**: No classification of technical debt into types (blocking-now / will-block-later / might-block-later) and no prioritization guidance for triaging debt items.
- **Cross-references**: TS-12 (Quality Assurance)

---

## "Make the change easy" refactoring discipline

- **Source**: https://zarar.dev/good-software-development-habits/
- **What the source says**: Kent Beck's maxim — first make the change easy, then make the easy change. Target a high proportion of refactor commits.
- **Coverage check**: TS-8's refactoring issue type covers refactoring as scoped in-flight work plus standalone refactoring tickets, but does not state the two-step sequencing or the commit-ratio heuristic.
- **Gap**: The "make the change easy, then make the easy change" discipline is not captured as a refactoring technique.
- **Cross-references**: TS-7 (Code Design), TS-9 (Version Control)