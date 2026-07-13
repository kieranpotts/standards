# Agentify

Takes a technical standard and compacts it into a token-efficient `AGENTS.md`
suitable for AI agent consumption. If the `AGENTS.md` already exists, the skill
instead reviews it for inconsistencies against the source standard and updates
it.

## What it does

Reads the `README.adoc` and all included `.adoc` files for a given technical
standard, then produces (or updates) a single `AGENTS.md` in the same directory.
The output:

- Preserves all normative rules (RFC 2119 keywords) faithfully.

- Strips extended prose, rationale, and introductory content that adds no
  actionable guidance.

- Keeps useful ✅/❌ code examples.

- Adds an inheritance statement when the standard extends another (eg. TS-32
  Bash extends TS-31 Unix Shells).

- Validates all cross-references against the TS index in `src/README.adoc`.

When `AGENTS.md` already exists, the skill does a gap analysis: missing rules
are added, stale rules are updated, stale TS cross-references are corrected, and
any typos or grammar errors found along the way are fixed.

## How to invoke

```
agentify TS-N
```

Where `TS-N` is the identifier of the target technical standard, eg:

```
agentify TS-31
agentify TS-31: Unix Shells
```

## Examples

**Creating a new AGENTS.md:**

```
agentify TS-47
```

Reads `src/047/README.adoc` and all its included files, then writes
`src/047/AGENTS.md`.

**Updating an existing AGENTS.md:**

```
agentify TS-31
```

Reads `src/031/README.adoc` and all its included files, then compares the
content against the existing `src/031/AGENTS.md` and applies any necessary
updates.
