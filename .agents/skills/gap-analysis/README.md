# Gap analysis

This skill instructs agents to check a single technical standard for coverage
gaps against one or more external reference resources — web pages, files, or
a whole directory of them — and record every gap found in a `GAPS.md` artifact.

The agent is instructed to read the target standard in full — its
`README.adoc`, every `include::`d file, any subdirectories, and its
`AGENTS.md`.

Next, the agent ingests every reference resource — fetching URLs, reading local
files, or recursing through a directory's Markdown, AsciiDoc, and plain-text
files.

It breaks the reference material down into individual claims, rules, or
topics. Then it check each one against the standard, classifying it as one of:

- **Missing.** Not addressed at all, and within the standard's own scope.
- **Partial.** Touched on, but more shallowly than the reference.
- **Out-of-scope.** Covered by the reference, but plausibly outside what
  this standard is meant to address.

For a large reference resource — a directory of many files, or several
sizeable URLs — the agent fans the reading-and-extraction step out to
sub-agents, one per resource or per batch of files. Sub-agents only ever
extract citation-tagged claims, while the orchestrating agent does the gap
analysis.

Findings are written to `GAPS.md` as a flat checklist, each citing where the
gap comes from and where in the standard it would best fit.

Re-running the skill against an existing `GAPS.md` re-verifies old findings and
adds new ones, rather than starting over. The agent is explicitly instructed to
not change any other files on disk — only `GAPS.md`.

## Interactivity

The agent prompts for the target standard or the reference resources if
either is unclear, and stops after presenting the report — it does not go on
to fix anything it finds.

## How to invoke

> Do a gap analysis between TS-42 and [url].

> Analyze TS-42 for gaps with [file].

> Gap-check TS-42 against the directory of vendor docs in [path].

You MUST define a specific technical standard. The agent will not proceed unless
the target standard is clear.

## Recommended models

A strong reasoning model will work best here.
