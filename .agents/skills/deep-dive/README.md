# Deep dive

Reviews a single technical standard in depth, records every finding in a
`TODO.md` beside it, and organizes the findings into tiers. When prompted,
the agent will work through the findings, resolving them one tier at a time.

The review and the remediation are separate steps. The findings are produced
first, for a human to read and judge before any of them are acted on.

The tiers are:

1. **Correctness.** Contradictions within the standard.
2. **Coherence.** Structure, rather than content.
3. **Completeness.** Gaps in the content.
4. **Conventions.** Cosmetic fixes.

## Interactivity

The agent is instructed to prompt for the target standard when the context does
not make it obvious, presents the plan for approval before starting any
remediation, and pauses for the user to review and commit the resolution to
each tier.

## How to invoke

Start a new review:

> Deep dive TS-1.

Continue an existing one — the agent reads `TODO.md` and reports what remains:

> What's next on the plan?

Work the next tier:

> Let's finish tier 3.

## Recommended models

You should definitely use a premium frontier reasoning model for this. Weaker
models will only surface lots of plausible-sounding, but ultimately invalid,
findings — wasting review time.
