# TS-20 gap analysis

Gaps found comparing TS-20: Network APIs against the following reference
resources:

- https://newsletter.pragmaticengineer.com/p/bluesky-engineering-culture

**Assessment.** One source — The Pragmatic Engineer's account of Bluesky's
engineering culture — was compared against TS-20, and it found a single gap,
missing rather than partial: the standard describes how services talk to each
other but never how the contract between them is defined and enforced. This
file was converted from the legacy format on 2026-08-13.

**Status:** 1 of 1 actionable gaps closed (2026-08-13). This run converted the
file from the legacy format and closed the schema-driven contracts gap. Nothing
remains open: 0 missing, 0 partial, 0 out-of-scope awaiting the user, 0
unresolved.

## Missing

- [x] https://newsletter.pragmaticengineer.com/p/bluesky-engineering-culture
      says Bluesky uses a custom "Lexicon" schema to describe HTTP endpoints
      and all record types, enforcing strongly-typed contracts between backend
      and client across a decentralized microservices network. The gap: TS-20
      does not address using a schema/IDL to define and enforce contracts
      across services in a (decentralized) microservices network. Coverage
      check: TS-20's inter-service communication patterns file covers commands,
      messages, and events but makes no mention of schema languages, interface
      definition, or strongly-typed contracts as a mechanism for governing
      inter-service communication. Recommend placing at
      `01-inter-service-communication-patterns.adoc`, as a new section
      following the three pattern sections it already carries.
      Cross-references: TS-29 (JSON Schema).

      **Resolved.** Closed by a new "Schema-driven contracts" section in
      `01-inter-service-communication-patterns.adoc`, extending the existing
      patterns file rather than adding a partial of its own, because the
      contract is a property of all three patterns it already describes.
      Requires the contract — operations, message types, and payload shapes —
      to be defined in a machine-readable schema that is the single source of
      truth for producer and consumer, and names the failure mode it guards
      against: a network boundary has no compiler, so nothing but convention
      stops the two sides disagreeing. Maps IDLs to transports (Protocol
      Buffers and OpenAPI for RPC-style; JSON Schema, Avro, or Protocol
      Buffers with AsyncAPI for message- and event-driven), and admits a
      bespoke schema language where no standard one fits the domain, citing
      the AT Protocol's Lexicon as the example. Requires schemas to be
      authored before the implementation with both sides generated from them,
      versioned and published where consumers resolve them at build time, and
      checked for backward compatibility in CI against the last published
      version. Carves out the asymmetry in validation: consumers validate
      inbound payloads and ignore unrecognized fields (tolerant reader), while
      producers MAY skip outbound validation in production where generated
      code already guarantees the shape. Cross-references TS-29 (JSON Schema)
      for the schema language itself and TS-23 (Messages and events) for
      payload design, and links internally to the standard's existing
      "Version management" section for the compatibility rules. Source added
      to the page's new `== References` section.

## Partial

(Converted from the legacy format; the original analysis recorded no
partial-coverage items.)

## Out-of-scope

(Converted from the legacy format, which has no concept of out-of-scope items;
the original analysis recorded none.)

## Unresolved

(Converted from the legacy format, which has no concept of unresolved
resources; the original analysis recorded none. The one source cited above
re-fetched successfully on 2026-08-13.)
