# Gap analysis

Checks a single technical standard for coverage gaps against external
reference resources — web pages, files, or a whole directory of them — and
records what it finds in a `GAPS.md` beside the standard.

The agent reads the standard in full — its page, every `include::`d partial,
any subdirectories, and its `AGENTS.md` — then ingests every reference
resource, breaks it down into individual claims, rules, and topics, and checks
each one against the standard. Every point is classified as one of:

- **Missing.** Not addressed at all, and within the standard's own scope.
- **Partial.** Touched on, but more shallowly than the reference.
- **Out-of-scope.** Covered by the reference, but plausibly outside what this
  standard is meant to address.

Only missing and partial items count as gaps. Out-of-scope items are recorded
anyway, so the user can overrule the agent's scope call.

Two kinds of resource get special handling. A `kieranpotts/*` GitHub issue URL
is treated as an index rather than a resource: the agent uses `gh` to pull its
description, comments, and sub-issues, and expands it into whatever is actually
linked from there, recursing into sub-issues under the same account. A YouTube
URL cannot be fetched at all, so a small bundled script pulls the video's
title, author, keywords, and full creator-supplied description from YouTube's
public oEmbed endpoint and the embedded page metadata, with no API key needed.
The agent is then explicit in `GAPS.md` that it compared against the creator's
summary rather than a transcript.

For large reference material, the reading is fanned out to sub-agents, one per
resource or per batch of files. Sub-agents only ever return citation-tagged
claims; the orchestrating agent does all of the classification, since that
needs the whole standard in context.

Findings are a flat checklist, each citing where the gap comes from and where
in the standard it would best fit. Re-running against an existing `GAPS.md`
re-verifies the old findings and adds new ones, rather than starting over.

## Interactivity

Interactive. The agent prompts for the target standard or the reference
resources when either is unclear, and asks before analyzing a standard that is
still a stub. It stops at the report — it does not go on to close any of the
gaps it finds.

## How to invoke

> Do a gap analysis between TS-42 and [url].

> Analyze TS-42 for gaps with [file].

> Gap-check TS-42 against the directory of vendor docs in [path].

Both the target standard and the reference resources are required. The agent
will not proceed until it can identify a single specific standard.

## Recommended models

A premium frontier reasoning model. Deciding whether a point in the reference
material is genuinely absent from the standard, merely thinner there, or
outside its scope entirely is exactly the open-ended judgment that a weaker
model gets wrong in both directions.

## Related skills

- [**deep-dive**](../deep-dive/) \
  Both produce a flat checklist of findings beside the standard. A gap
  analysis measures the standard against external reference material; a deep
  dive measures it against itself and the repository's own conventions.
