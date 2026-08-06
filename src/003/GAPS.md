# TS-3 gap analysis

Gaps found comparing TS-3: *Design Docs* against the following reference
resource:

- https://blog.pragmaticengineer.com/the-product-minded-engineer/ (Gergely
  Orosz, "The Product-Minded Software Engineer", 2019)

**Assessment.** Of the article's traits, one was routed to TS-3: trait 5
(offering product/engineering tradeoffs upfront). TS-3 has strong normative
machinery for recording alternatives and tradeoffs in RFCs — it requires
"alternatives considered" that "would reasonably have achieved similar
outcomes" (`03-requests-for-comments.adoc:224-243`) and makes the trade-off
"an RFC's reason for existing" (`06-best-practices.adoc:12-13`). But it frames
tradeoffs throughout as *technical/design* tradeoffs: the alternatives are
alternative *designs*, the goals are engineering goals, and the cross-cutting
concerns are technical. It never asks authors to weigh *engineering effort
against product impact/value* or to propose a *different feature* (as opposed
to a different implementation) that achieves similar product value at lower
engineering cost. The point is Partial — the documentary scaffolding exists
but the product/engineering framing does not.

**Status:** First run, 2026-08-06. One Partial gap open.

## Missing

(None identified in this run.)

## Partial

- [ ] https://blog.pragmaticengineer.com/the-product-minded-engineer/
      (Trait 5: "Offering product/engineering tradeoffs upfront") covers
      product/engineering tradeoff evaluation more directly than
      `03-requests-for-comments.adoc:224-243` (alternatives considered —
      "alternative designs that would reasonably have achieved similar
      outcomes," with trade-offs for each) and
      `06-best-practices.adoc:12-13,58-59` ("lead with the trade-offs"; "don't
      omit alternatives") — specifically, the reference argues for weighing
      *engineering effort against product impact/value* and proposing a
      *different feature* (not just a different implementation) that
      achieves similar product value at vastly smaller engineering effort,
      and for making *product* tradeoffs and assessing their *engineering*
      impact. TS-3's RFC machinery could capture such tradeoffs if an author
      chose to, but the standard frames alternatives as alternative *designs*
      and tradeoffs as technical/design tradeoffs (the cross-cutting concerns
      enumerated in `03-requests-for-comments.adoc` are security, privacy,
      observability, compatibility, operability — all technical), and never
      calls for the product-value-per-unit-engineering-effort framing.
      Recommend adding guidance to `03-requests-for-comments.adoc`
      (alternatives / trade-offs) to explicitly include product/engineering
      tradeoffs — alternative *features* achieving similar product value at
      different engineering cost, and product tradeoffs assessed for
      engineering impact. Note: this overlaps TS-2 (Software Design
      Qualities), which treats the same tradeoff as an engineering-internal
      quality concern — see `../002/GAPS.md`.

## Out-of-scope

(None identified in this run.)

## Unresolved

(None.)