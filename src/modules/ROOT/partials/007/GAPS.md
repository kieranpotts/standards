# TS-7 gap analysis

Gaps found comparing TS-7: Code design against the following reference
resources:

- partials/002/06-habitability.adoc:47-73 (the "Code design" section of
  TS-2's Habitability chapter)

**Assessment.** The reference excerpt is narrow — 27 lines on naming,
terminology, magic, and documentation — and almost entirely within TS-7's
stated scope (naming conventions, expressiveness, comments). Most of it is
already covered, in some cases nearly verbatim. What remains is one clearly
missing topic (avoiding implicit "magic" behavior) and several places where
TS-2 states a sharper or broader rule than TS-7's existing treatment.

**Status:** All 5 gaps closed. Last run: 2026-09-05.

## Missing

- [x] partials/002/06-habitability.adoc:63-65 ("Avoid using too much magic —
      behavior that happens implicitly, through convention, reflection, or
      framework machinery that the reader cannot see at the point of use")
      is not addressed anywhere in TS-7. The standard's only near-miss is
      "magic numbers" in partials/007/04-expressiveness.adoc:65-68, which is
      a distinct, narrower concept (unexplained literals, not implicit
      framework/convention-driven behavior). Recommend a new subsection in
      partials/007/04-expressiveness.adoc, after "Syntax and control
      structures", or a new section entirely if the topic warrants its own
      TL;DR bullet.

      **Resolved.** Added a new "Avoiding magic" section to
      `05-expressiveness.adoc`, after "Syntax and control structures" and
      before "Programming paradigms". Defines magic as implicit behavior
      driven by naming convention, reflection, decorators, dependency
      injection, or other framework machinery; gives concrete examples (a
      test runner's name-based discovery, an ORM's schema reflection, a DI
      container's constructor inspection); states the trade-off against
      narrative-readable code; and recommends preferring explicit
      alternatives, treating widely-known ecosystem conventions as a more
      reasonable trade than bespoke, codebase-specific magic. Added a
      corresponding TL;DR bullet.

- [x] partials/002/06-habitability.adoc:50 ("the number of distinct design
      patterns observed throughout the codebase should be small") is not
      addressed anywhere in TS-7. The closest material —
      partials/007/02-abstraction.adoc and
      partials/007/09-object-oriented-design.adoc — covers choosing the right
      pattern for a given problem, but not the cross-cutting discipline of
      keeping the total vocabulary of patterns small so a reader doesn't
      have to relearn a new idiom in each part of the codebase. Recommend
      placing at partials/007/03-decomposition.adoc or "new section".

      **Resolved.** Added a new "A small vocabulary of patterns" section to
      `03-decomposition.adoc`, at the end of the file. States that this is a
      cross-cutting discipline distinct from choosing the right pattern for
      one problem, that a codebase of individually well-reasoned decisions
      can still be hard to work in if each module solves the same kind of
      problem a different way, and recommends favoring the codebase's
      existing pattern for a given kind of problem over a marginally better
      new one, reserving new patterns for genuinely new kinds of problems.
      Added a corresponding TL;DR bullet.

## Partial

- [x] partials/002/06-habitability.adoc:54-56 ("Respect established
      precedent in the domain and in the surrounding ecosystem, rather than
      optimizing terminology for newcomers at the expense of the people who
      will work in the codebase daily") covers this more thoroughly than
      partials/007/04-expressiveness.adoc:59 — specifically, TS-7 only says
      "avoid jargon and acronyms unless they are universally understood in
      your domain," which doesn't state the newcomer-vs-daily-maintainer
      trade-off, or the instruction to defer to domain/ecosystem precedent
      even when it's less approachable to newcomers.

      **Resolved.** Extended the "Naming things" section of
      `05-expressiveness.adoc`, directly after the existing jargon/acronym
      sentence. Added guidance to favor precise, specialized terminology
      over generic words that could be misunderstood, and to respect
      established domain/ecosystem precedent even where it is less
      approachable to newcomers, on the grounds that daily maintainers pay
      the relearning cost far more often than an occasional reader pays the
      lookup cost.

- [x] partials/002/06-habitability.adoc:57-59 ("Once a term is chosen for a
      domain concept, use it everywhere that concept appears – in code,
      comments, tests, and documentation alike – rather than letting
      synonyms accumulate") covers this more thoroughly than
      partials/007/04-expressiveness.adoc:61-63 — specifically, TS-7's
      consistency guidance ("Naming conventions should be consistent
      throughout a program") is scoped to naming identifiers in code, and
      doesn't extend the same discipline to comments, tests, and
      out-of-band documentation.

      **Resolved.** Extended the "Naming things" section of
      `05-expressiveness.adoc`, immediately after the existing "vocabulary
      of the codebase" paragraph. Added a paragraph stating that this
      consistency extends beyond code identifiers to comments, tests, and
      documentation, with a worked example (`order` vs. "purchase" vs.
      "transaction" for one concept) showing the cost of letting synonyms
      accumulate across artifacts.

- [x] partials/002/06-habitability.adoc:57 ("Include every word needed to
      remove ambiguity, and omit every word that carries no information")
      covers this more thoroughly than
      partials/007/04-expressiveness.adoc:26-39 — specifically, TS-7 argues
      for clarity over brevity and against unnecessary abbreviation, but
      doesn't state the complementary half of the rule: that words carrying
      no information should be omitted, not just that words shouldn't be cut
      for brevity's sake.

      **Resolved.** Extended the "Naming things" section of
      `05-expressiveness.adoc`, directly after the newcomer-precedent
      addition above. Added a paragraph stating the complementary half of
      the clarity-over-brevity rule — omit words that carry no information —
      with a worked example (`userAccountData` vs. `userAccount`) showing
      that favoring clarity is not license to pad names with empty words.

## Out-of-scope

(none)

## Unresolved

(none — the single reference resource is a local file and was read in full)
