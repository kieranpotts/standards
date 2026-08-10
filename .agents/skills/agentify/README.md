# Agentify

Compacts one technical standard into a token-efficient `AGENTS.md`, saved
beside the standard's own source files.

The agent reads the standard in full — `README.adoc`, every `include::`d file,
and any subdirectories — and writes out only what an agent can act on.
Normative rules keep their RFC 2119 strength, worked ✅/❌ examples are kept,
and prose introductions, rationale, and glossaries are dropped.
Cross-references point at other standards' `AGENTS.md` files, so an agent
following a chain of them stays in compact context throughout.

Where an `AGENTS.md` already exists, the skill reconciles it against the source
instead of rewriting it: missing rules are added, drifted rules corrected, stale
cross-references repaired, and non-actionable content removed. Rules already in
the file are left alone unless they contradict the source.

## Interactivity

Interactive. The agent prompts for the target standard when the context does
not make it obvious, and asks before compacting a standard that is still a
stub. Everything else runs to completion without stopping.

## How to invoke

> Agentify TS-10.

> Update the AGENTS.md for TS-31.

> Refresh the agent version of the Markdown standard.

## Recommended models

A mid-tier model is usually sufficient. The task is a structured
transformation with clear rules, but judging which prose is load-bearing and
which is decoration benefits from a stronger model on the larger standards.

## Related skills

- [**deep-dive**](../deep-dive/) \
  A deep dive audits an existing `AGENTS.md` for drift against its source as
  one of its seven finding categories. Run this skill to fix that drift.

- [**fix-cross-references**](../fix-cross-references/) \
  This skill validates cross-references only within the file it writes. Run
  that one to sweep the whole of `src/` for broken references.

## References

- [AGENTS.md specification](https://agents.md) — the format this skill writes.

- [TS-27: Markdown](../../../src/modules/ROOT/pages/027-markdown.adoc) — the
  formatting conventions every generated `AGENTS.md` follows.
