# TS-9 gap analysis

Gaps found comparing TS-9: *Version Control* against the following reference
resource:

- https://12factor.net/codebase (Factor I: Codebase, "The Twelve-Factor App",
  Adam Wiggins, 2017)

**Assessment.** TS-9 already addresses most of Factor I's claims, generally more
thoroughly than the source: the single reference-repository model
(`03-repositories.adoc:9`), the requirement that repository boundaries reflect
component boundaries (`03-repositories.adoc:40-43`), and the promotion of
unmodified code through environments (`07-environments.adoc:158-174`) all cover
ground the factor asserts more tersely. The one substantive absence is the
factor's explicit prohibition on multiple applications sharing the same code
outside of a proper library dependency — TS-9 has no equivalent statement. Two
other claims are implicit in the mono-repo guidance but not stated as
principles in their own right.

**Status:** First run, 2026-08-05. All gaps open.

## Missing

- [ ] https://12factor.net/codebase ("Multiple apps sharing the same code is a
      violation of twelve-factor; the correct solution [...] is to factor the
      shared code into libraries which can be included through the dependency
      manager") is not addressed anywhere in TS-9. `03-repositories.adoc:38-55`
      (Repository scope) states that repository boundaries SHOULD reflect
      component boundaries, but never states the converse constraint — that
      code shared by two or more applications MUST NOT simply be copy-pasted or
      cross-referenced between their repositories, and MUST instead be
      extracted into a versioned, independently-consumed library. Recommend a
      new subsection in `03-repositories.adoc` after the "Repository scope"
      section (after line 55), or a short paragraph in the "Self-contained
      repositories" section given its adjacency to dependency management.

## Partial

- [ ] https://12factor.net/codebase ("One codebase maps to one app... if there
      are multiple codebases, it's not an app — it's a distributed system.
      Each component in a distributed system is an app, and each can
      individually comply with twelve-factor") is only implicit in TS-9.
      `03-repositories.adoc:38-43` states repository boundaries should reflect
      component boundaries, and the "Mono-repos" section
      (`03-repositories.adoc:97-126`) addresses when multiple *tightly-coupled*
      components should share a repository — but the standard never states the
      general principle that one codebase corresponds to one application, nor
      frames a multi-codebase system explicitly as a distributed system whose
      individual components are each subject to this standard in their own
      right. Recommend a short framing statement near
      `03-repositories.adoc:38-43`.

- [ ] https://12factor.net/codebase ("many apps [...] will have multiple
      copies of the app running at any given time... this fact does not change
      the fundamental notion that only one codebase exists per app") overlaps
      with `03-repositories.adoc:9-36` (Cloning workflows) and
      `07-environments.adoc:1-31` (Branch-to-environment mapping), which
      establish a single upstream reference repository and map branches to
      multiple concurrently-running deployment environments — but neither
      section states this converse framing (many running instances, still one
      codebase) as an explicit principle. This is a minor gap; the standard's
      existing structure already produces the correct outcome.

## Out-of-scope

(None identified in this run — Factor I's claims fall squarely within TS-9's
stated scope.)

## Unresolved

(None.)
