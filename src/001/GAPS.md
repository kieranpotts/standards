# TS-1 gap analysis

Gaps found comparing TS-1: *Software Requirements Specification* against the
following reference resources:

- `src/001/__TODO__/index.md`
- `src/001/__TODO__/0100-openapi.md`
- `src/001/__TODO__/_rdf.md`
- `src/001/__TODO__/_200-owl.md`
- `src/001/__TODO__/_todo/User story - Wikipedia.URL` → https://en.wikipedia.org/wiki/User_story
- `src/001/__TODO__/_todo/User Story And Use Case Comparison.URL` → http://wiki.c2.com/?UserStoryAndUseCaseComparison

**Assessment.** Most of the reference material falls outside TS-1's stated
scope. The OpenAPI cheat sheet, and the RDF/OWL semantic-web material, describe
implementation-level notations (HTTP API definitions, ontology languages) that
TS-1 deliberately excludes — the standard keeps the Interfaces contract
behavioural and protocol-agnostic (`07-behaviors.adoc:160-169`) and defers
modelling techniques to TS-4 (`06-context.adoc:83`). The Wikipedia *User story*
article is the only resource with meaningful in-scope overlap, and most of what
it covers (story mapping, INVEST, acceptance criteria, Given-When-Then, the
limitations of card-based stories) TS-1 already addresses by a different route.
The genuine findings are a small number of missing and partial items, plus one
fetch failure.

**Status:** Initial run. All gaps open. Last run 2026-08-05.

## Missing

- [ ] https://en.wikipedia.org/wiki/User_story#Common_templates ("Evil User
      Story" / "Abuse User Story" template — stories written from an attacker's
      perspective to surface security scenarios) is not addressed anywhere in
      the standard. The elicitation techniques in `10-requirements-elicitation.adoc`
      cover discovery of functional behaviours but none target security/abuse
      cases. Recommend placing at `10-requirements-elicitation.adoc` as a new
      subsection after line 208, or at `08-qualities.adoc:34` (Security) with a
      cross-reference. Note: this borders on TS-54 (Threat Modeling) and TS-52
      (Security); the user may decide it belongs there rather than here.

## Partial

- [ ] https://en.wikipedia.org/wiki/User_story#Comparing_with_use_cases compares
      user stories and use cases (formality, scale, goal/sequence focus vs
      conversation-placeholder). `10-requirements-elicitation.adoc:92-96` notes
      only that use cases and Gherkin overlap and a project need not use both —
      it does not articulate the structural differences that would help a team
      choose between them. Recommend expanding the note at
      `10-requirements-elicitation.adoc:92-96`, or a short "Choosing a technique"
      subsection.

- [ ] https://en.wikipedia.org/wiki/User_story#Relationship_to_epics,_themes_and_initiatives/programs
      defines *epic* as a grouping of user stories. `11-proposal-lifecycle.adoc:157`
      uses the term "epic" (as a container for grouping dependent proposals)
      without defining it. Recommend a one-line definition at
      `11-proposal-lifecycle.adoc:157`. (The reference's *theme* and *initiative*
      hierarchy levels are not used by the standard and are treated as
      out-of-scope below.)

## Out-of-scope

- [ ] `src/001/__TODO__/index.md` notes that "some modelling notations such as
      UML are also used as specification." TS-1 explicitly defers modelling
      techniques to TS-4 (`06-context.adoc:83`), so UML and other modelling
      notations plausibly sit outside this standard's stated purpose. Flagged
      for the user to confirm or overrule.

- [ ] `src/001/__TODO__/_rdf.md` and `src/001/__TODO__/_200-owl.md` cover RDF
      (triples, resources/properties/classes, serialisation formats) and OWL
      (ontology classes, property types such as functional/symmetric/transitive,
      editors like Protégé). These are modelling/ontology notations; TS-1's
      Model section (`06-context.adoc:64-83`) covers the domain model and ERDs
      and defers modelling techniques to TS-4. Flagged for the user to confirm
      or overrule.

- [ ] `src/001/__TODO__/0100-openapi.md` is an OpenAPI 3.0.1 cheat sheet
      (info, servers, paths, components, security, types, extensions,
      examples). TS-1's Interfaces section (`07-behaviors.adoc:160-169`)
      deliberately keeps the external contract behavioural and
      protocol-agnostic — "Protocol, transport, payload formats, and endpoint
      naming are technical design decisions, not requirements." HTTP API
      specification is covered by TS-20 (Network APIs) / TS-21 (HTTP APIs).
      Flagged for the user to confirm or overrule.

- [ ] https://en.wikipedia.org/wiki/User_story#History (Beck 1997, Cockburn,
      Jeffries' "Three Cs", Cohn 2004, Patton 2014) is historical background.
      TS-1 already cites Cohn and Patton as references; the origin history of
      the practice is not a technical standard's purpose. Flagged for the user
      to confirm or overrule.

- [ ] https://en.wikipedia.org/wiki/User_story#User_journey_map describes a UX
      research artifact that maps a single user category's chronology of
      phases, including emotions and points of friction. TS-1's Journeys
      section (`07-behaviors.adoc:171-188`) is a specification artifact — how
      features combine into end-to-end flows — not a UX research map. The
      emotional/friction journey map plausibly belongs to TS-15 (User
      Interfaces) or a UX research standard rather than TS-1. Flagged for the
      user to confirm or overrule.

- [ ] https://en.wikipedia.org/wiki/User_story#Relationship_to_epics,_themes_and_initiatives/programs
      defines *theme* and *initiative* as backlog-hierarchy levels above the
      epic. TS-1 uses only "epic" (as a proposal grouping); the broader
      epic/theme/initiative backlog hierarchy is a product/backlog-management
      concern, not requirements specification. Flagged for the user to confirm
      or overrule.

## Unresolved

- [ ] http://wiki.c2.com/?UserStoryAndUseCaseComparison could not be retrieved:
      the c2.com wiki requires JavaScript and the fetch returned only a
      "javascript required to view this site" notice. Not included in the
      comparison above. (The Wikipedia article's "Comparing with use cases"
      section covers the same topic at a high level and was used instead.)