# Deep dive

This skill instructs agents to review a single technical standard in depth,
record every finding in a `TODO.md` alongside it, and then work through the
todos one item at a time.

The review and the remediation are separate. The findings are produced first,
for human review before being acted on.

## What it does

Reads a standard in full — `README.adoc` and every `include::`d file, any
subdirectories, and its `AGENTS.md` — along with the yardsticks it will be
measured against: the repository style guide and template, TS-26 (technical
writing), TS-27 (Markdown), and TS-28 (AsciiDoc).

It then collects findings in seven categories: contradictions, factual errors,
structural problems, coverage gaps, convention conformance, `AGENTS.md` drift,
and prose defects.

Findings are written to `TODO.md` as a flat checklist, each citing a file and
line. The findings are sorted into four tiers, worked in order:

1. **Correctness.** A standard that contradicts itself cannot be followed.
2. **Coherence.** Structure settles before content is added to it.
3. **Completeness.** Gaps filled into a structure that has stopped moving.
4. **Conventions.** Last, so cosmetic fixes are not invalidated by content
   edits.

The agent stops after each tier so the user can review the changes in the Git
working tree.

## How to invoke

Start a new review:

> Deep dive TS-1

Continue an existing one — the agent reads `TODO.md` and reports what remains:

> What's next on the plan?

Work the next tier:

> Let's finish tier 3
