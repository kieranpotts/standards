# TS-25: Technical Documentation

This is a compact version of technical standard TS-25 for AI agents.

Use this when deciding what documentation a project needs, where it should live,
who it's for, or whether it's still trustworthy. This standard covers the
_informational architecture and lifecycle_ of documentation.

For sentence-level writing rules (voice, headings, formatting, citations) see
[TS-26](../026/AGENTS.md).

## Rules

- **Prefer code-adjacent documentation.**

  Inline comments, generated API references, and READMEs kept next to the code
  they describe stay accurate because they're updated alongside the code.
  Out-of-band documentation drifts. Where practical, generate documentation from
  the source (eg. OpenAPI specs from route/type definitions) rather than
  hand-maintaining it separately.

- **Distinguish documentation types and write for a specific audience.**

  Reference docs (READMEs, API docs), architecture/design docs, process docs
  (ADRs, RFCs), operational docs (runbooks), onboarding docs, and changelogs
  each have a different audience and update trigger. Don't mix audiences
  (maintainers, consumers, operators, newcomers) in one document — each SHOULD
  find their section without reading the rest.

- **A README orients, it doesn't exhaustively document.**

  Cover: purpose, status, setup, common usage with runnable examples, and links
  to deeper docs. Do NOT duplicate full API references or changelogs into the
  README — link out instead. Duplication creates two places that can drift out
  of sync, and a README that grows too long stops serving its purpose as a
  quick orientation point.

- **Documentation MUST describe the current state, not future intent.**

  Documentation follows implementation, not the other way round, since docs
  written before implementation drift as plans change. Exceptions: requirements
  specs and proposals, which are explicitly forward-looking.

- **Process documentation (ADRs, RFCs, design docs) is a historical artifact.**

  Process documentation is a historical record — it captures point-in-time
  rationale — not a source-of-truth for current processes. Only the source code
  is authoritative for how the system currently works. Don't treat a design doc
  as still accurate just because it's linked from the README.

- **Changelogs are the one exception to "descriptive, not historical."**

  A changelog explicitly documents past state transitions. Follow
  [Keep a Changelog](https://keepachangelog.com/) conventions where practical:
  entries grouped by release in reverse-chronological order, categorized as
  Added/Changed/Deprecated/Removed/Fixed/Security, written for the consumer
  (user-visible effect, eg. "the API now returns 429 on rate-limit" not "add
  rate limiting middleware"), not the contributor (implementation detail).
  Where commit history and PR titles are already structured and user-legible
  (eg. via Conventional Commits), a changelog MAY be generated automatically
  rather than hand-maintained.

- **Documentation MUST have an owner, tied to the code it describes.**

  A PR that changes behavior without updating its documentation is incomplete,
  the same way an untested behavior change is incomplete. Where docs can't be
  kept current, mark them explicitly as historical rather than leaving staleness
  silent. Prefer documentation whose staleness is self-evident (generated from
  code, or dated and clearly historical) over documentation whose staleness is
  silent (hand-maintained prose with no indication of when it was last true).

- **API documentation SHOULD be generated from the code where practical; at
  minimum specify per operation inputs, outputs, errors, and non-obvious side
  effects.**

  An OpenAPI spec generated from route and type definitions, or reference docs
  generated from typed function signatures and docstrings, cannot drift from
  the source because it _is_ the source, rendered. Where generation isn't
  practical (third-party APIs, protocols), hand-written API docs SHOULD still
  describe the interface as it currently behaves, not as it was designed to
  behave. At minimum, per operation: inputs (including required versus optional
  and types), outputs, error conditions, and any side effects that aren't
  obvious from the operation's name.

- **Use diagrams when a structure or flow is easier to understand visually;
  prefer diagrams-as-code over opaque images.**

  Warranted for component boundaries, data flow, state machines, sequence of
  calls across systems. Not warranted merely to break up a wall of text, and
  should not be the only place a piece of information is recorded — accompany
  with prose for readers who need to search the text or who consume the document
  with assistive technology. Prefer diagrams defined as code (Mermaid,
  PlantUML) over opaque image files (PNG, JPEG): they live alongside the code,
  are versioned in the same commits, can be reviewed as a diff, and don't
  require proprietary software to edit. Where an opaque image is unavoidable
  (eg. a screenshot), keep the source file that generated it so the image can
  be regenerated after a UI change rather than manually re-captured.

- **Each document MUST be focused on a single, narrow, specific topic.**

  A document covering multiple topics becomes harder to navigate, harder to
  keep accurate, and harder to link to. Readers arriving via search or a
  cross-reference want the answer to one question, not a document they must skim
  in full. Narrow documents can be read in one sitting, updated in isolation,
  and referenced precisely (a link to a specific file rather than a heading
  buried partway down a long page). Signs a document has outgrown its scope:
  the title includes "and" or "or"; you need a list in the introduction to
  describe what it covers; sections could each stand alone as a useful search
  result; updating one part regularly requires re-reading unrelated parts;
  contributors are unsure which section to update. When a document grows to
  cover more than one topic, split it — extract each topic into its own file and
  link between them. A narrow document is not the same as a short one; the
  constraint is on breadth of subject matter, not word count.

- **Not everything needs a standalone document.**

  Before creating one, consider whether self-documenting code, a code comment, a
  type/schema, or a test would serve better. Create a document when the
  information is broader than one piece of code, needs reading before the code,
  or must persist independently of the current implementation.

## References

- [TS-25 source](../../pages/025-technical-documentation.adoc)
- [TS-7: Code Design](../007/AGENTS.md)
- [TS-26: Technical Writing Style Guide](../026/AGENTS.md)
- [Keep a Changelog](https://keepachangelog.com/)
