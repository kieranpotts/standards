# Fix cross-references

Scans the technical standards for broken internal cross-references and repairs
them, so that every reference from one standard to another carries the right
number, the right title, and a path that actually resolves.

The agent builds an index of TS numbers, titles, and directories from
`src/README.adoc`, then sweeps the `.adoc` and `.md` files in scope — either a
single standard or the whole of `src/` — for anything that looks like a
reference to another standard.

Each candidate is checked on three axes: does the number exist, does the stated
title match the index, and does the relative path resolve from where the
referring file actually sits. Only the ones that fail a check are touched; the
link syntax around them is left alone.

Anything ambiguous is deliberately not repaired. A reference with more than one
plausible target keeps its original text and is reported as unresolved, on the
grounds that a wrong guess is worse than a flagged uncertainty because it looks
fixed.

## Interactivity

Interactive, but only barely. The agent prompts when the scope is unclear —
one standard, or the whole repository — and otherwise runs to completion,
reporting fixes and unresolved references at the end rather than asking about
them along the way.

## How to invoke

> Fix references in TS-10.

> Fix all broken cross-references.

> The links out of TS-31 are pointing at the wrong standard.

## Recommended models

A small, fast model is sufficient. The work is mechanical validation against a
known index, and the skill is written to escalate anything ambiguous to the
report rather than to reason about it.

## Related skills

- [**agentify**](../agentify/) \
  That skill validates cross-references only within the one file it writes.
  This one sweeps every standard in scope.

- [**deep-dive**](../deep-dive/) \
  Broken cross-references are a conventions-tier finding in a deep dive. Run
  this skill to clear them in one pass, rather than one at a time.
