# TS-4 gap analysis

Gaps found comparing TS-4: *Modeling* against the following reference
resources (the contents of `src/004/__TODO__/`):

- `src/004/__TODO__/modeling-examples/README.txt`
- `src/004/__TODO__/modeling-examples/uml/` — a collection of Umlet (`.uxf`)
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

**Status:** Initial run. All gaps open. Last run 2026-08-05.

## Missing

## Partial

- [ ] `src/004/__TODO__/modeling-examples/uml/associations/` (`composition`,
      `aggregation`, `dependency`, `composition-aggregation` `.uxf` examples)
      and `src/004/__TODO__/modeling-examples/uml/diagrams/class/relationships/`
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

- [ ] `src/004/__TODO__/modeling-examples/uml/diagrams/class/multiplicity/`
      (`association/one-to-one/`, `association/one-to-many/`, `attributes/`
      examples) demonstrates multiplicity notation (`1`, `*`, `0..1`, `1..*`).
      `03-notations.adoc:22-23` names class diagrams as a key notation but does
      not cover multiplicity. Recommend the same new subsection in
      `03-notations.adoc` (after line 30), alongside the relationships guidance.

- [ ] `src/004/__TODO__/modeling-examples/uml/diagrams/class/entities/person.umlet.uxf`
      (a class with name/attribute/operation compartments and `+`/`-` visibility
      markers), `.../class/members/abstract/` and `.../class/members/static/`
      (abstract and static member notation), and `.../class/interfaces/animal`
      (interface notation) demonstrate class-diagram member notation.
      `03-notations.adoc:22-23` names class diagrams as a key notation but does
      not cover class compartments, visibility, abstract/static members, or
      interfaces. Recommend the same new subsection in `03-notations.adoc`
      (after line 30).

- [ ] `src/004/__TODO__/modeling-examples/uml/diagrams/use-case/basic.umlet.umlet.uxf`
      demonstrates use case diagram notation. `03-notations.adoc:27-30` names
      use case diagrams as useful for requirements analysis and cross-references
      TS-1, but neither TS-4 nor TS-1 covers the use case *diagram notation*
      (actors, use cases, `<<include>>`/`<<extend>>`, generalization). TS-1
      covers use case *analysis* (the textual structure), not the diagram
      notation, so the notation gap falls to TS-4. Recommend a brief note in
      `03-notations.adoc` (after line 30) or an explicit cross-reference stating
      where the diagram notation is covered.

## Out-of-scope

- [ ] `src/004/__TODO__/modeling-examples/README.txt` states "Diagrams are
      created with Umlet." Umlet is a graphical UML editor.
      `02-text-to-diagram-modeling-tools.adoc:18-21` deliberately recommends
      text-to-diagram tools (PlantUML, Mermaid, Graphviz) over graphical drawing
      tools, so a graphical editor like Umlet plausibly sits outside this
      standard's recommended approach. Flagged for the user to confirm or
      overrule.

## Unresolved

- [ ] The directories `src/004/__TODO__/47710241/`, `src/004/__TODO__/164352/`,
      and `src/004/__TODO__/47874101/` contain only binary `.png` images (skipped
      silently per the skill — binary files are not plain-text reference
      resources) plus one `.uxf` that is a duplicate of the `Person` class
      example already counted under `modeling-examples/`. No additional claims
      could be extracted from them; they appear to be ad-hoc downloaded
      screenshots. Not included in the comparison beyond noting their presence.