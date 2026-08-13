# GAPS — TS-9 Version control

Coverage gaps identified by comparing external sources against this standard.

---

## Internal open source collaboration model

- **Source**: https://blog.pragmaticengineer.com/pragmatic-engineer-test/
- **What the source says**: Any engineer can access and contribute to most other codebases, with appropriate code ownership in place — an "internal open source" collaboration model across an organization's repositories.
- **Coverage check**: TS-9 has the building blocks (repository boundaries, CODEOWNERS, PR-based review, fork-and-pull workflows) but frames them around repository ownership and branch mechanics, not as an organization-wide access-and-contribution model. It does not discuss cross-repository contribution rights or the tradeoffs of an internal-open-source topology.
- **Gap**: TS-9 does not frame or recommend an internal-open-source collaboration model. The organizational access/contribution pattern and its governance implications are unaddressed.

---

## "Make the change easy" refactoring discipline

- **Source**: https://zarar.dev/good-software-development-habits/
- **What the source says**: Kent Beck's maxim — first make the change easy, then make the easy change. Target a high proportion of refactor commits.
- **Coverage check**: TS-9 defines a `Refactor` revision type but does not state the two-step sequencing or the commit-ratio heuristic.
- **Gap**: The "make the change easy, then make the easy change" discipline is not captured.
- **Cross-references**: TS-7 (Code design), TS-8 (Issue tracking)