# Close gaps

Works through the open coverage gaps recorded in one standard's `GAPS.md`,
writing the content that closes them into the standard, and recording against
each gap what was written and where.

This is the other half of [gap-analysis](../gap-analysis/README.md). That
skill finds gaps and records them; this one closes them. Neither does the
other's job.

Work is taken in bounded batches — at most eight actionable items per run
unless the user says otherwise. Forty standards have open gaps, 653 actionable
items between them, and the largest single file holds 136. A run that tried to
empty a file like that would produce thin content and a diff nobody can
review.

The four headings in a `GAPS.md` are not equivalent work, and the skill treats
them differently:

- **Missing** and **Partial** need content written. These are the only items
  that count as the batch's work.
- **Out-of-scope** items are scope calls awaiting a human. The agent
  recommends, the user decides, and nothing is actioned unilaterally.
- **Unresolved** items are reference resources that failed to fetch. They get
  re-fetched, and then either become gaps or are dismissed.

An agent cannot report a batch closed on the strength of the last two.

## The two file formats

Eighteen `GAPS.md` files follow the `gap-analysis` template — flat checklists
under the four headings. Twenty-two are in an older format, one `##`
subsection per gap, closed by appending a `**RESOLVED**` bullet.

A legacy file is converted to the template format by the same run that works
it, as that run's first edit, never as a separate sweep. The conversion loses
nothing: gaps already resolved keep their resolution notes verbatim, and the
legacy `**Cross-references**` field — which the template format has no slot
for — is preserved as the closing sentence of the item it belongs to.

## Interactivity

The agent is instructed to prompt for the target standard when the context
does not make it obvious, and to name the batch it has selected before
starting. It does not wait for approval on the batch itself. It stops and asks
in three cases: an out-of-scope item needing a scope decision, a gap whose
content plainly belongs in a _different_ standard (a unit of work stays within
one standard, so splitting it is the user's call), and a standard that is
still a stub, where there is no structure to extend.

Every run ends with a dirty working tree. The agent never stages or commits.

## How to invoke

Start on a standard's backlog:

> Close the gaps in TS-31.

Continue — the agent reads `GAPS.md` and reports what remains:

> Close the next batch of gaps in TS-31.

Scope the batch explicitly:

> Work the three partial items in TS-23's GAPS.md.

## Recommended models

Use a premium frontier reasoning model. Closing a gap means writing standards
prose to the depth of the surrounding material, from a source the analysis
only summarized. Weaker models paraphrase the gap note back into a section
heading and tick the box.
