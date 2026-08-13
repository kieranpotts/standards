# TS-50 gap analysis

Gaps found comparing TS-50: Cloud economics against the following reference
resources:

- https://newsletter.posthog.com/p/how-we-choose-technologies

**Assessment.** A single-source analysis against PostHog's account of how it
selects technologies, which found one gap: the standard bounds and compares
cloud costs but never establishes the standing review that turns a cost into
a detectable trigger for change. Converted from the legacy format on
2026-08-13.

**Status:** 1 of 1 actionable gaps closed (2026-08-13). This run converted
the file from the legacy format and closed the cost-as-a-trigger gap with a
new `03-cost-review.adoc` section. Nothing remains open: 0 missing, 0
partial, 0 out-of-scope, 0 unresolved.

## Missing

- [x] https://newsletter.posthog.com/p/how-we-choose-technologies says new
      technology should only be adopted to solve "hair-on-fire" problems —
      including excessive costs, which its infrastructure team surfaces
      through a quarterly review of AWS spend measured against benchmarks —
      and that each such problem raises an explicit build-vs-buy question.
      The gap: no standard addresses cost as a trigger for re-evaluating
      technology, or the build-vs-buy trade-off as a general
      technology-selection concern. Coverage check: TS-50 covers cloud cost
      structure and a narrow cloud-native-vs-dedicated-server choice, but
      not cost-as-a-trigger for re-evaluating a technology stack, nor a
      general build-vs-buy framework. Recommend placing in a new section.
      Cross-references: TS-5 (Application architecture).

      **Resolved.** Closed by a new `03-cost-review.adoc`, "Cost review"
      section, appended to the page after the cloud-native comparison.
      Requires a scheduled review of cloud spend — quarterly by default,
      monthly where spend is outgrowing the business — rather than review
      triggered by bill shock, and fixes the three things each review has to
      establish: where the money goes (which requires cost allocation to be
      designed in, since spend cannot be attributed retrospectively), how
      unit cost is moving as distinct from total spend, and how spend
      compares against three benchmarks (the previous period, the budget,
      and the same workload under an alternative deployment model). It then
      separates the trigger from the response: a benchmark breach obliges
      investigation, not a technology change, and the configuration-level
      responses in "Auto-scaling surge costs" are to be exhausted before
      cost is escalated into a technology-selection question. Where the
      response is build-versus-buy, the comparison is required to be a total
      cost of ownership rather than vendor price against infrastructure
      price. A final subsection requires projected costs to be validated
      against a production-representative workload before commitment, using
      the source's own EFS case — roughly US$300 per month projected against
      roughly US$600 per day measured, sixty times the projection — and
      names the usual cause, a per-operation or per-request charging
      dimension that the estimate priced per gigabyte.

      The general technology-selection half of this gap — the adoption
      triggers, the build-versus-buy evaluation, and the ongoing
      re-evaluation of a stack — was closed while this item was open, by
      TS-6's `10-continuous-technology-evaluation.adoc` (see the
      correspondingly worded item in
      `src/modules/ROOT/partials/005/GAPS.md`). The new TS-50 section
      therefore supplies only the cloud-economics half — the review
      discipline that makes cost detectable as a trigger, and the validation
      of cost estimates — and cross-references
      TS-6 (Distributed system design) for the selection framework rather
      than restating it, with TS-5 (Application architecture) for the
      single-application dependency case. Source added to a new
      `== References` section on the page.

## Partial

(None. This file was converted from the legacy format, and the original
analysis recorded no items of this kind.)

## Out-of-scope

(None. This file was converted from the legacy format, whose schema had no
concept of an out-of-scope item, and the original analysis recorded none.)

## Unresolved

(None. This file was converted from the legacy format, whose schema had no
concept of an unresolved resource, and the original analysis recorded none.)
