# Agentify

Compacts one technical standard into a token-efficient `AGENTS.md`.

Where an `AGENTS.md` already exists, the skill reconciles it against the source.
Missing rules are added, drifted rules are corrected, and stale cross-references
are repaired.

## Interactivity

The agent is instructed to prompt for the target standard when the context does
not make it obvious.

## How to invoke

> Agentify TS-10.

> Update the AGENTS.md for TS-31.

> Refresh the agent version of the Markdown standard.

## Recommended models

A mid-tier model is usually sufficient. The task is a structured transformation
with clear rules. But judging which prose is load-bearing and which is decoration
benefits from a stronger model on the larger standards.
