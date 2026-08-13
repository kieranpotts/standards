# Gap analysis

Checks a single technical standard for coverage gaps against external
reference resources — web pages, files, or a whole directory of them — and
records what it finds in a `GAPS.md` beside the standard.

The agent reads the standard in full — its page, every `include::`d partial,
and any subdirectories — then ingests every reference
resource, breaks it down into individual claims, rules, and topics, and checks
each one against the standard. Every point is classified as one of:

- **Missing.** Not addressed at all, and within the standard's own scope.
- **Partial.** Touched on, but more shallowly than the reference.
- **Out-of-scope.** Covered by the reference, but plausibly outside what this
  standard is meant to address.

Only missing and partial items count as gaps. Out-of-scope items are recorded
anyway, so the user can overrule the agent's scope call.

A `kieranpotts/*` GitHub issue URL is treated as an index rather than a resource.
The agent is instructed to use `gh` to pull its description, comments, and
sub-issues, and expands it into whatever is actually linked from there,
recursing into sub-issues under the same account.

For large reference material, the reading is fanned out to sub-agents, one per
resource or per batch of files. Sub-agents only ever return citation-tagged
claims. The orchestrating agent does all of the classification, since that
needs the whole standard in context.

## Interactivity

The agent is instructed to prompt for the target standard or the reference
resources when either is unclear. It also asks before analyzing a standard that
is still a stub.

## How to invoke

> Do a gap analysis between TS-42 and [url].

> Analyze TS-42 for gaps with [file].

> Gap-check TS-42 against the directory of vendor docs in [path].

Both the target standard and the reference resources are required. The agent
will not proceed until it can identify a single specific standard.

## Recommended models

It is recommended to use a premium frontier reasoning model for this task.
