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

**Status:** All 5 gaps open. Last run: 2026-09-02.

## Missing

- [ ] partials/002/06-habitability.adoc:63-65 ("Avoid using too much magic —
      behavior that happens implicitly, through convention, reflection, or
      framework machinery that the reader cannot see at the point of use")
      is not addressed anywhere in TS-7. The standard's only near-miss is
      "magic numbers" in partials/007/04-expressiveness.adoc:65-68, which is
      a distinct, narrower concept (unexplained literals, not implicit
      framework/convention-driven behavior). Recommend a new subsection in
      partials/007/04-expressiveness.adoc, after "Syntax and control
      structures", or a new section entirely if the topic warrants its own
      TL;DR bullet.

- [ ] partials/002/06-habitability.adoc:50 ("the number of distinct design
      patterns observed throughout the codebase should be small") is not
      addressed anywhere in TS-7. The closest material —
      partials/007/02-abstraction.adoc and
      partials/007/09-object-oriented-design.adoc — covers choosing the right
      pattern for a given problem, but not the cross-cutting discipline of
      keeping the total vocabulary of patterns small so a reader doesn't
      have to relearn a new idiom in each part of the codebase. Recommend
      placing at partials/007/03-decomposition.adoc or "new section".

## Partial

- [ ] partials/002/06-habitability.adoc:54-56 ("Respect established
      precedent in the domain and in the surrounding ecosystem, rather than
      optimizing terminology for newcomers at the expense of the people who
      will work in the codebase daily") covers this more thoroughly than
      partials/007/04-expressiveness.adoc:59 — specifically, TS-7 only says
      "avoid jargon and acronyms unless they are universally understood in
      your domain," which doesn't state the newcomer-vs-daily-maintainer
      trade-off, or the instruction to defer to domain/ecosystem precedent
      even when it's less approachable to newcomers.

- [ ] partials/002/06-habitability.adoc:57-59 ("Once a term is chosen for a
      domain concept, use it everywhere that concept appears – in code,
      comments, tests, and documentation alike – rather than letting
      synonyms accumulate") covers this more thoroughly than
      partials/007/04-expressiveness.adoc:61-63 — specifically, TS-7's
      consistency guidance ("Naming conventions should be consistent
      throughout a program") is scoped to naming identifiers in code, and
      doesn't extend the same discipline to comments, tests, and
      out-of-band documentation.

- [ ] partials/002/06-habitability.adoc:57 ("Include every word needed to
      remove ambiguity, and omit every word that carries no information")
      covers this more thoroughly than
      partials/007/04-expressiveness.adoc:26-39 — specifically, TS-7 argues
      for clarity over brevity and against unnecessary abbreviation, but
      doesn't state the complementary half of the rule: that words carrying
      no information should be omitted, not just that words shouldn't be cut
      for brevity's sake.

## Out-of-scope

(none)

## Unresolved

(none — the single reference resource is a local file and was read in full)
