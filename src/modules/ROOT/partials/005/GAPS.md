# TS-5 gap analysis

Gaps found comparing TS-5: Application architecture against the following
reference resources:

- partials/002/06-habitability.adoc:75-107 (the "The rule of representation"
  section of TS-2's Habitability chapter)

**Assessment.** The reference excerpt is narrow — one section arguing that
data structures, not code structures, should be treated as the foundation of
a software design. It falls within TS-5's scope wherever it touches
distributed systems and service boundaries, but the standard is silent on
the core thesis, and its closest related material — bounded contexts and
per-service models — pulls in a different direction rather than reinforcing
it.

**Status:** 2 gaps open. Last run: 2026-09-02.

## Missing

- [ ] partials/002/06-habitability.adoc:77-102 (data structures, rather than
      code structures, as the foundation of a software design; folding
      complexity into data so that program logic can be "stupid and
      robust"; a data model that makes invalid states difficult to
      represent removing whole categories of defect by construction) is not
      addressed anywhere in TS-5. Related material exists —
      partials/005/01-horizontal-layers.adoc:65 distinguishes "data models"
      from "domain models" in passing, and
      partials/007/10-object-oriented-design.adoc:162-184 (value objects,
      avoiding primitive obsession) touches invalid-state prevention at the
      level of individual values — but neither states the broader thesis
      that the data model should be treated as the foundation of the
      design, or that complexity should be actively shifted from code into
      data. Recommend a new section in TS-5, near
      partials/005/01-horizontal-layers.adoc, or "new section".

## Partial

- [ ] partials/002/06-habitability.adoc:104-106 ("In distributed systems,
      shared data structures deserve particular care. Where several
      services exchange data, a well-designed common representation reduces
      the need for each team to write its own converters and mappers, and
      with it the risk of inconsistencies creeping in between services")
      covers this more thoroughly than
      partials/005/06-services.adoc:22-52 — specifically, TS-5's treatment
      of service boundaries argues for the opposite emphasis: each bounded
      context keeps its own model and translates at the boundary
      (partials/005/06-services.adoc:44-52), rather than reducing
      converter/mapper duplication through a well-designed shared
      representation. TS-5 does not address when a common representation is
      preferable to per-context translation, or the inconsistency risk that
      a shared representation mitigates. This may be a genuine tension
      between the two standards' guidance rather than a simple omission —
      worth the user's judgment on how (or whether) to reconcile them.

## Out-of-scope

(none)

## Unresolved

(none — the single reference resource is a local file and was read in full)
