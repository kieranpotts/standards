# Fix cross-references

Scans the technical standards for broken internal cross-references and repairs
them, so that every reference from one standard to another carries the right
number, the right title, and a target that actually resolves.

The agent builds an index of TS numbers, titles, and page slugs from
`src/modules/ROOT/pages/index.adoc`, then sweeps the `.adoc` and `.md` files
in scope — either a single standard or the whole of `src/modules/ROOT/` —
for anything that looks like a reference to another standard. `.adoc` files
use Antora `xref:`/`include::` resource IDs; `AGENTS.md`/`GAPS.md` files keep
the older relative-Markdown-link convention.

Each candidate is checked on the axes that apply to its mechanism: does the
number exist, does the stated title match the index, and does the `xref:`
slug or the `AGENTS.md` relative path actually resolve. Only the ones that
fail a check are touched; the link syntax around them is left alone.

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
