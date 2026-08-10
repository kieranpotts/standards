# Deep dive

Reviews a single technical standard in depth, records every finding in a
`TODO.md` beside it, and then works through the findings one tier at a time.

The review and the remediation are separate steps. The findings are produced
first, for a human to read and judge before any of them are acted on.

The agent reads the standard in full — its page, every `include::`d partial,
any subdirectories, and its `AGENTS.md` — along with the yardsticks it will be
measured against: the repository style guide and template, TS-26 (technical
writing), TS-27 (Markdown), and TS-28 (AsciiDoc).

It then collects findings in seven categories: contradictions, factual errors,
structural problems, coverage gaps, convention conformance, `AGENTS.md` drift,
and prose defects. Each finding is a flat checklist item citing a file and a
line, sorted into one of four tiers, worked in order:

1. **Correctness.** A standard that contradicts itself cannot be followed.
2. **Coherence.** Structure settles before content is added to it.
3. **Completeness.** Gaps filled into a structure that has stopped moving.
4. **Conventions.** Last, so cosmetic fixes are not invalidated by content
   edits.

Every tier ends with a mechanical verification pass — character counts, xref
uniqueness, link resolution, diff size — and then a stop, so the user can
review and commit the changes from the Git working tree.

## Interactivity

Interactive. The agent prompts for the target standard when the context does
not make it obvious, presents the plan for approval before starting any
remediation, puts findings with two defensible resolutions to the user, and
pauses after every tier for the user to commit.

## How to invoke

Start a new review:

> Deep dive TS-1.

Continue an existing one — the agent reads `TODO.md` and reports what remains:

> What's next on the plan?

Work the next tier:

> Let's finish tier 3.

## Recommended models

A premium frontier reasoning model. Judging whether two rules genuinely
contradict each other, or whether a gap is real, is open-ended analysis over a
lot of context, and a weaker model produces plausible-sounding findings that
waste review time.

## Related skills

- [**agentify**](../agentify/) \
  A deep dive reports `AGENTS.md` drift as one of its finding categories; that
  skill is how the drift gets fixed.

- [**gap-analysis**](../gap-analysis/) \
  Both produce a flat checklist of findings beside the standard. A deep dive
  measures the standard against itself and the repository's own conventions;
  a gap analysis measures it against external reference material.

- [**fix-cross-references**](../fix-cross-references/) \
  Broken cross-references surface in a deep dive's conventions tier. That
  skill repairs them across the whole of `src/` in one pass.
