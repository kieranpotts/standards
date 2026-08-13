# TS-13 gap analysis

Gaps found comparing TS-13: Functional testing against the following reference
resources:

- https://zarar.dev/good-software-development-habits/

**Assessment.** The single reference resource is Zarar Siddiqi's "Good
Software Development Habits", a short list of practice-level habits of which
only the testing entries bear on TS-13. It yielded one gap: the standard has
no guidance on declining to test a framework's own capability. This file was
converted from the legacy format on 2026-08-13; the original analysis
recorded no assessment paragraph, so this one is written from the converted
item rather than carried over.

**Status:** 1 of 1 actionable gaps closed (2026-08-13). Converted from the
legacy format in the same run, and the single gap — testing the framework's
own capability — closed by a new "What not to test" section. 0 missing, 0
partial, 0 out-of-scope, 0 unresolved. The file is fully worked.

## Missing

- [x] https://zarar.dev/good-software-development-habits/ says to know when
      you are testing the framework's own capability, and if you are, not to
      do it — the framework is already tested by people who know it better,
      and you have to trust that it does what it says; and that keeping
      components small reduces the need for a lot of tests, because the
      framework does most of the heavy lifting, whereas a big component
      introduces complexity that then needs a lot of tests. The gap: no
      explicit guidance against testing framework-provided behavior, nor the
      related design advice that smaller components reduce the surface that
      needs custom tests. Coverage check: TS-13 covers test strategies, test
      types/levels, coverage, test doubles, TDD, and test design, but a
      search finds no guidance on avoiding tests that merely exercise
      framework/library capabilities, nor on trusting third-party code
      instead of re-testing it.

      **Resolved.** Closed by a new "What not to test" section in
      `04-test-coverage.adoc`, extending the coverage section rather than
      adding a partial of its own, because the decision of what deserves a
      test is what that section already governs. States as a MUST NOT that
      tests are not written for behavior supplied wholly by a framework,
      library, or language runtime, and gives the discriminator — would the
      assertion still hold if your own code were deleted? — with three
      worked instances (an ORM's own `save`, a state hook's re-render, a
      validation library's built-in rule). Carves out what remains the
      author's to cover: their configuration of the dependency, their
      integration with it (handing off to `<<Integration tests>>`), and
      their own logic. Names one exception, the regression test that pins an
      upstream behavior you have specific reason to distrust, which must
      cite the assumption and the upstream issue. A "Small components need
      fewer tests" subsection carries the source's design point: a component
      demanding many tests is a design signal first, because size is what
      determines whether framework behavior and your own can be exercised
      separately. Cross-references TS-7 (Code design) for component sizing.
      Source added to a new `== References` section on the page, which had
      none before.

## Partial

(None. This file was converted from the legacy format, and the original
analysis recorded no partial-coverage items.)

## Out-of-scope

(None. This file was converted from the legacy format, and the original
analysis recorded no out-of-scope items.)

## Unresolved

(None. This file was converted from the legacy format, and the original
analysis recorded no unresolved reference resources.)
