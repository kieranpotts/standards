# TS-25: Technical Documentation

This is a compact version of technical standard TS-25 for AI agents.

Use this when deciding what documentation a project needs, where it
should live, who it's for, or whether it's still trustworthy. This
standard covers the *informational architecture and lifecycle* of
documentation.

For sentence-level writing rules (voice, headings, formatting, citations)
see [TS-26](../026/AGENTS.md).

## Rules

The capitalized words REQUIRED, MUST, MUST NOT, RECOMMENDED, SHOULD, SHOULD NOT,
OPTIONAL, and MAY are to be interpreted as described in
[IETF RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

-   **Prefer code-adjacent documentation.**

    Inline comments, generated API references, and READMEs kept next to the
    code they describe stay accurate because they're updated alongside the code.
    Out-of-band documentation drifts. Where practical, generate documentation
    from the source (eg. OpenAPI specs from route/type definitions) rather
    than hand-maintaining it separately.

-   **Distinguish documentation types and write for a specific audience.**

    Reference docs (READMEs, API docs), architecture/design docs, process docs
    (ADRs, RFCs), operational docs (runbooks), onboarding docs, and changelogs
    each have a different audience and update trigger. Don't mix audiences
    (maintainers, consumers, operators, newcomers) in one document — each
    SHOULD find their section without reading the rest.

-   **A README orients, it doesn't exhaustively document.**

    Cover: purpose, status, setup, common usage with runnable examples, and
    links to deeper docs. Do NOT duplicate full API references or changelogs
    into the README — link out instead.

-   **Documentation MUST describe the current state, not future intent.**

    Documentation follows implementation, not the other way round, since docs
    written before implementation drift as plans change. Exceptions:
    requirements specs and proposals, which are explicitly forward-looking.

-   **Process documentation (ADRs, RFCs, design docs) is a historical artifact.**

    Process documentation is a historical record — it captures point-in-time
    rationale — not a source-of-truth for current processes. Only the source
    code is authoritative for how the system currently works. Don't treat a
    design doc as still accurate just because it's linked from the README.

-   **Changelogs are the one exception to "descriptive, not historical."**

    A changelog explicitly documents past state transitions.
    Follow [Keep a Changelog](https://keepachangelog.com/) conventions
    where practical: entries grouped by release, categorized as
    Added/Changed/Deprecated/Removed/Fixed/Security, written for the consumer
    (user-visible effect), not the contributor (implementation detail).

-   **Documentation MUST have an owner, tied to the code it describes.**

    A PR that changes behavior without updating its documentation is incomplete,
    the same way an untested behavior change is incomplete. Where docs can't be
    kept current, mark them explicitly as historical rather than leaving
    staleness silent.

-   **Not everything needs a standalone document.**

    Before creating one, consider whether self-documenting code, a code comment,
    a type/schema, or a test would serve better. Create a document when the
    information is broader than one piece of code, needs reading before the
    code, or must persist independently of the current implementation.
