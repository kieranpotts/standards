# GAPS — TS-13 Functional testing

Coverage gaps identified by comparing external sources against this standard.

---

## Don't test the framework

- **Source**: https://zarar.dev/good-software-development-habits/
- **What the source says**: Know when you're testing the framework's own capability rather than your code; if so, don't — the framework is already tested by its maintainers. Keeping components small reduces the need for many tests.
- **Coverage check**: TS-13 covers test strategies, test types/levels, coverage, test doubles, TDD, and test design, but a search finds no guidance on avoiding tests that merely exercise framework/library capabilities, nor on trusting third-party code instead of re-testing it.
- **Gap**: No explicit guidance against testing framework-provided behavior, nor the related design advice that smaller components reduce the surface that needs custom tests.