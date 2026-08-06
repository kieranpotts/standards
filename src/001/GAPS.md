# TS-1 gap analysis

Gaps found comparing TS-1: *Software Requirements Specification* against the
following reference resources:

- `src/001/__TODO__/index.md`
- `src/001/__TODO__/0100-openapi.md`
- `src/001/__TODO__/_rdf.md`
- `src/001/__TODO__/_200-owl.md`
- `src/001/__TODO__/_todo/User story - Wikipedia.URL` → https://en.wikipedia.org/wiki/User_story
- `src/001/__TODO__/_todo/User Story And Use Case Comparison.URL` → http://wiki.c2.com/?UserStoryAndUseCaseComparison
- https://github.com/kieranpotts/standards/issues/67 (issue titled "Requirements"),
  which expands to the following discovered resources:
  - https://sobolevn.me/2019/02/engineering-guide-to-user-stories
  - https://www.youtube.com/watch?v=_gteHp-ZR9k
  - https://www.youtube.com/watch?v=vSuJqMRG1WM
  - https://www.youtube.com/watch?v=4aHKsolzCv4
  - https://www.youtube.com/watch?v=XxxJZ_oduqo
  - https://www.youtube.com/watch?v=JDD5EEJgpHU
- https://www.gov.uk/guidance/government-design-principles (UK Government
  Design Principles)

**Assessment.** Most of the reference material falls outside TS-1's stated
scope. The OpenAPI cheat sheet, and the RDF/OWL semantic-web material, describe
implementation-level notations (HTTP API definitions, ontology languages) that
TS-1 deliberately excludes — the standard keeps the Interfaces contract
behavioural and protocol-agnostic (`07-behaviors.adoc:160-169`) and defers
modelling techniques to TS-4 (`06-context.adoc:83`). The Wikipedia *User story*
article is the only resource from the first batch with meaningful in-scope
overlap, and most of what it covers (story mapping, INVEST, acceptance criteria,
Given-When-Then, the limitations of card-based stories) TS-1 already addresses by
a different route. The second batch (issue #67) added the sobolevn.me blog post
on writing correct user stories; its atomic points (consistent language via a
glossary, separating user goals from implementation details, clarifying roles,
making stories verifiable via BDD/Gherkin, covering unhappy paths, MoSCoW
prioritization, and linking requirements to code/tests) are all already covered
by TS-1 — ubiquitous language (`06-context.adoc:105-124`), actor hierarchy
(`06-context.adoc:85-103`), executable specifications
(`09-executable-specifications.adoc`), unhappy paths (`07-behaviors.adoc:93`),
MoSCoW (`11-proposal-lifecycle.adoc:77-92`), and requirements traceability
(`11-proposal-lifecycle.adoc:201-206`). It produced no new gaps. The five unique
YouTube videos linked from issue #67 (one URL was duplicated in the issue body)
were ingested via their creator-supplied descriptions and keywords, extracted
from the page metadata via YouTube's oEmbed endpoint and the embedded
`ytInitialPlayerResponse`; one (Bridging the Gap) also published a full transcript,
which was fetched. Their theses — user stories shouldn't be too big, technical
stories don't work, "non-functional requirements" is a bad name for cross-cutting
concerns, use case thinking avoids missing requirements, and acceptance tests
as executable specifications — are mostly already covered by TS-1 (INVEST "Small"
and story splitting at `10-requirements-elicitation.adoc:160-177`; qualities
terminology and architectural significance at `08-qualities.adoc:3-56`; use case
extensions surfacing unhappy paths at `10-requirements-elicitation.adoc:83-86`;
executable specifications and enforcement at `09-executable-specifications.adoc`).
The one genuine new finding is the "technical stories" anti-pattern (see
Partial). The genuine findings otherwise remain the small number of missing and
partial items from the first batch, plus the c2.com fetch failure.

**Status:** Re-run against issue #67 resources. sobolevn.me blog produced no new
gaps. Five unique YouTube videos ingested via metadata/transcript; produced one
new Partial gap (technical stories) and one new Out-of-scope note (industry
document-format taxonomy). All prior gaps remain open and were re-verified. Last
run 2026-08-05.

**Fourth run, 2026-08-06.** Re-run against the UK Government Design
Principles (https://www.gov.uk/guidance/government-design-principles). Of its
11 principles, only #1 ("Start with user needs") was routed to TS-1; the
rest were routed to other standards. Principle #1 is partially covered —
TS-1 grounds the specification in identified actors and their goals and
expects engineers to push back on requirements that would not achieve the
underlying outcome, but is silent on the means the principle prescribes
(user research, talking to users, behavioural-data analysis, empathy, and
the explicit "asked-for ≠ needed" distinction). One new Partial gap added;
all prior gaps remain open.

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

- [ ] https://www.youtube.com/watch?v=vSuJqMRG1WM (Dave Farley, "TECHNICAL
      STORIES DON'T WORK") argues that "technical stories" / "technical user
      stories" — stories written for technical or enabling work (infrastructure,
      refactoring, tooling) alongside user stories — are a planning anti-pattern
      that decouples work from user value and degrades prioritization and
      quality. TS-1's principles imply technical work does not belong in the
      specification as stories — INVEST "Valuable: delivers value to an actor,
      not merely a technical task" (`10-requirements-elicitation.adoc:158`),
      the warning against splitting by architectural layer
      (`10-requirements-elicitation.adoc:175-177`), and "implementation details
      MUST NOT appear in the specification" (`11-proposal-lifecycle.adoc:178-180`)
      — but the standard never names the "technical story" practice or explains
      why it is problematic, so a team currently using technical stories would
      find no explicit guidance to stop. Recommend a short note at
      `10-requirements-elicitation.adoc` after the splitting discussion (around
      line 177), or in `07-behaviors.adoc` Features. Note: this borders on
      work/backlog management, which may sit outside a requirements
      *specification* standard; the user may decide it is out-of-scope.

- [ ] https://www.gov.uk/guidance/government-design-principles (Principle 1,
      "Start with user needs") covers the means of discovering user needs
      more thoroughly than `06-context.adoc:85-103` (Actors) and
      `03-responsibility.adoc:1-34` (Responsibility) — specifically, the
      principle prescribes doing user research, analysing data, and talking
      to users rather than making assumptions; having empathy for users;
      and the distinction that what users ask for isn't always what they
      need. TS-1 derives actors and features from the domain model and
      expects engineers to push back on stated requirements that would not
      achieve the underlying outcome, but it never mentions user research,
      talking to users, behavioural-data analysis, empathy, or the
      asked-for ≠ needed distinction as a discovery practice, and it
      locates user/problem framing in the upstream PRD
      (`01-scope.adoc:57-101`) rather than the SRS workflow. Recommend a
      short "User research and need discovery" note in
      `03-responsibility.adoc` or `06-context.adoc` (Actors),
      cross-referencing the PRD. Note: TS-1 may legitimately defer the
      *means* of user research to a UX/product standard (eg. TS-15); the
      user may decide it is out-of-scope here.

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

- [ ] https://www.bridging-the-gap.com/functional-specification/ (transcript of
      https://www.youtube.com/watch?v=XxxJZ_oduqo, "Functional Requirements and
      Specifications: A Quick Tutorial") surveys industry document formats for
      functional specifications — Functional Requirements Documents (FRDs),
      System Requirements Specifications (SRSs), Business Requirements Documents
      (BRDs), tabular "system shall" statements — and gives the pros and cons of
      each versus use cases and user stories. TS-1 takes a definitive position
      (its own structure, with Gherkin scenarios and use cases for discovery)
      rather than surveying alternative industry formats, so a reader arriving
      from an FRD/BRD/"system shall" background gets no explicit bridge to the
      standard's approach. This is plausibly outside TS-1's purpose as an
      opinionated standard rather than a tutorial. Flagged for the user to
      confirm or overrule.

## Unresolved

- [ ] http://wiki.c2.com/?UserStoryAndUseCaseComparison could not be retrieved:
      the c2.com wiki requires JavaScript and the fetch returned only a
      "javascript required to view this site" notice. Not included in the
      comparison above. (The Wikipedia article's "Comparing with use cases"
      section covers the same topic at a high level and was used instead.)

- [ ] The five YouTube videos from issue #67 were ingested only via their
      creator-supplied descriptions and keywords (extracted from page
      metadata), not full video transcripts. Four of the five have no public
      transcript, so atomic claims beyond the description's thesis could not be
      verified. The descriptions were treated as the author's own summary of
      each video's argument and compared on that basis. If full transcripts
      become available, a follow-up run could surface additional gaps.