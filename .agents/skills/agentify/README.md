# Agentify

This skill instructs agents to bring a single technical standard into context,
and compact it into a token-efficient `AGENTS.md`.

If the `AGENTS.md` already exists, the agent is instructed to review it for
inconsistencies against the source standard, and update it to bring it into
line.

## What it does

Reads the `README.adoc` and all included `.adoc` files for a given technical
standard, then produces (or updates) a single `AGENTS.md` in the same directory.

When `AGENTS.md` already exists, the skill does a gap analysis. Missing rules
are added, stale rules are updated, invalid TS cross-references are corrected,
and any typos or grammar errors found along the way are fixed.

The agent is instructed to:

- Preserve all normative rules (RFC 2119 keywords) faithfully.

- Strip extended prose, rationale, and introductory content that adds no
  actionable guidance.

- Keep useful ✅/❌ code examples.

- Add an inheritance statement when the standard extends another (eg. TS-32
  Bash extends TS-31 Unix Shells).

- Validate all cross-references against the TS index in `src/README.adoc`.

## How to invoke

> Agentify TS-10
