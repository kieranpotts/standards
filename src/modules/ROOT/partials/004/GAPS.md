# TS-4 gap analysis

Gaps found comparing TS-4: *Modeling* against the following reference
resources (the contents of `__TODO__/004/`):

- `__TODO__/004/modeling-examples/README.txt`
- `__TODO__/004/modeling-examples/uml/` — a collection of Umlet (`.uxf`)
  example diagrams and rendered `.png` images, organized by UML concept.

**Assessment.** The reference material is a library of worked UML example
diagrams (plus a one-line `README.txt` noting they are drawn with Umlet). It
does not introduce any new modeling *views* or *levels* beyond what TS-4 already
covers in `01-modeling-levels.adoc`. The substantive overlap is with the UML
notation section (`03-notations.adoc`): the standard names class, use case, and
sequence diagrams as the most useful UML diagram types, but stops short of
describing the notation elements of any of them. The reference examples
demonstrate exactly those notation elements for class diagrams (relationships,
multiplicity, members, interfaces) and use case diagrams. The image-only
directories `47710241/`, `164352/`, and `47874101/` contain only binary `.png`
files (skipped silently per the skill) plus one duplicate `.uxf`, so they add
no extractable claims beyond the `modeling-examples/` tree.

**Status:** 4 of 4 actionable gaps closed (2026-08-13). Both Partial items
extended into one new "Class diagram notation" subsection (relationships,
multiplicity, member notation) and one new "Use case diagram notation"
subsection in `03-notations.adoc`. The out-of-scope item was confirmed
excluded (2026-08-13). 1 unresolved resource re-checked: the reference
directory no longer exists on disk, so the re-fetch failed again.

## Missing

(None recorded by the original analysis — all four actionable items were
classified as Partial.)

## Partial

- [x] `__TODO__/004/modeling-examples/uml/associations/` (`composition`,
      `aggregation`, `dependency`, `composition-aggregation` `.uxf` examples)
      and `__TODO__/004/modeling-examples/uml/diagrams/class/relationships/`
      (`generalization/`, `association/` with dependency, aggregation,
      composition, reflexive examples) demonstrate and directly compare the
      core class-diagram relationship types and their semantics (association,
      aggregation, composition, generalization/inheritance, dependency,
      reflexive). `03-notations.adoc:22-23` names class diagrams as one of the
      three most useful UML diagram types, but the standard does not cover the
      relationship notation or the semantic distinctions between them (notably
      composition vs aggregation, the most commonly confused). Recommend a new
      subsection under "Unified Modeling Language (UML)" in
      `03-notations.adoc` (after line 30).

      **Resolved.** Closed by a new "Class diagram notation" section in
      `03-notations.adoc`, immediately after the UML introduction. Covers all
      five relationship types — association, aggregation, composition,
      generalization, and dependency — each with its line notation and, for
      the diamond-ended pair, the lifecycle question that distinguishes
      composition from aggregation. Also documents reflexive relationships.
      No stable, citable source (author/title/URL) exists for a local Umlet
      example directory, so no entry was added to a `== References` section.

- [x] `__TODO__/004/modeling-examples/uml/diagrams/class/multiplicity/`
      (`association/one-to-one/`, `association/one-to-many/`, `attributes/`
      examples) demonstrates multiplicity notation (`1`, `*`, `0..1`, `1..*`).
      `03-notations.adoc:22-23` names class diagrams as a key notation but does
      not cover multiplicity. Recommend the same new subsection in
      `03-notations.adoc` (after line 30), alongside the relationships guidance.

      **Resolved.** Closed by the same "Class diagram notation" section,
      final paragraph: documents `1`, `0..1`, `*`/`0..*`, and `1..*`
      multiplicity markers with a worked `Person`-to-`Address` example.

- [x] `__TODO__/004/modeling-examples/uml/diagrams/class/entities/person.umlet.uxf`
      (a class with name/attribute/operation compartments and `+`/`-` visibility
      markers), `.../class/members/abstract/` and `.../class/members/static/`
      (abstract and static member notation), and `.../class/interfaces/animal`
      (interface notation) demonstrate class-diagram member notation.
      `03-notations.adoc:22-23` names class diagrams as a key notation but does
      not cover class compartments, visibility, abstract/static members, or
      interfaces. Recommend the same new subsection in `03-notations.adoc`
      (after line 30).

      **Resolved.** Closed by the same "Class diagram notation" section,
      opening paragraph: documents the three-compartment rectangle
      (name/attributes/operations), the `+`/`-`/`#`/`~` visibility markers,
      the `<<interface>>` stereotype, and the italic/underline conventions for
      abstract and static members.

- [x] `__TODO__/004/modeling-examples/uml/diagrams/use-case/basic.umlet.umlet.uxf`
      demonstrates use case diagram notation. `03-notations.adoc:27-30` names
      use case diagrams as useful for requirements analysis and cross-references
      TS-1, but neither TS-4 nor TS-1 covers the use case *diagram notation*
      (actors, use cases, `<<include>>`/`<<extend>>`, generalization). TS-1
      covers use case *analysis* (the textual structure), not the diagram
      notation, so the notation gap falls to TS-4. Recommend a brief note in
      `03-notations.adoc` (after line 30) or an explicit cross-reference stating
      where the diagram notation is covered.

      **Resolved.** Closed by a new "Use case diagram notation" section in
      `03-notations.adoc`, directly after "Class diagram notation". Documents
      the actor (stick figure) and use case (labeled oval) symbols, the
      `<<include>>`/`<<extend>>` dashed-arrow relationships, and
      generalization between actors or use cases. Distinguishes the notation
      from TS-1's use case *analysis* technique with an explicit
      cross-reference.

## Out-of-scope

- [x] `__TODO__/004/modeling-examples/README.txt` states "Diagrams are
      created with Umlet." Umlet is a graphical UML editor.
      `02-text-to-diagram-modeling-tools.adoc:18-21` deliberately recommends
      text-to-diagram tools (PlantUML, Mermaid, Graphviz) over graphical drawing
      tools, so a graphical editor like Umlet plausibly sits outside this
      standard's recommended approach. Flagged for the user to confirm or
      overrule. Recommendation: confirm the exclusion. The standard's stance
      in `02-text-to-diagram-modeling-tools.adoc` is a deliberate,
      already-argued preference for text-based tooling; Umlet's role here was
      only as a convenient source of worked notation examples, not as a
      tool recommendation, and the new "Class diagram notation" / "Use case
      diagram notation" sections describe the *notation* independent of any
      particular drawing tool. Nothing in the reference material argues that
      graphical editors deserve standard-level coverage.

      **Confirmed out-of-scope (2026-08-13).** Umlet was only the source of
      worked examples; the standard's existing preference for text-to-diagram
      tooling over graphical editors stands unchanged.

## Unresolved

- [ ] The directories `__TODO__/004/47710241/`, `__TODO__/004/164352/`,
      and `__TODO__/004/47874101/` contain only binary `.png` images (skipped
      silently per the skill — binary files are not plain-text reference
      resources) plus one `.uxf` that is a duplicate of the `Person` class
      example already counted under `modeling-examples/`. No additional claims
      could be extracted from them; they appear to be ad-hoc downloaded
      screenshots. Not included in the comparison beyond noting their presence.
      Re-fetch failed again on 2026-08-13: no `__TODO__` directory exists
      anywhere under the repository root any longer (`find` from the repo
      root returned nothing under that name). The failure is persistent, not
      fresh — the whole reference tree behind this analysis, not only these
      three directories, is currently unavailable.

      Re-fetch attempted again on 2026-08-13: searched the entire local
      workspace (`~/dev/personal`, all sibling repositories) and the full
      filesystem for `__TODO__` and for the three directory names
      (`47710241`, `164352`, `47874101`) by name — no match anywhere.
      Checked this repository's Git history (`git log --all --diff-filter=A`
      and full-history search for the three directory names) — the
      `__TODO__` tree was never committed, confirming it was always local,
      ephemeral scratch input to the gap-analysis skill and not a versioned
      or remotely-hosted resource. No URL, README, or other provenance note
      accompanies these three directories anywhere in this file (unlike
      `modeling-examples/`, which has its own `README.txt`), so there is no
      remote resource to fetch — re-fetching would require either the
      original local source restoring these files or a citable URL that
      does not currently exist in any recoverable record. Remains
      unresolved; no further automated re-fetch is possible without new
      information about the original source.