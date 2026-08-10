# GAPS — TS-20 Network APIs

Coverage gaps identified by comparing external sources against this standard.

---

## Schema-driven contracts for decentralized microservices

- **Source**: https://newsletter.pragmaticengineer.com/p/bluesky-engineering-culture
- **What the source says**: Bluesky uses a custom "Lexicon" schema to describe HTTP endpoints and all record types, enforcing strongly-typed contracts between backend and client across a decentralized microservices network.
- **Coverage check**: TS-20's inter-service communication patterns file covers commands, messages, and events but makes no mention of schema languages, interface definition, or strongly-typed contracts as a mechanism for governing inter-service communication.
- **Gap**: TS-20 does not address using a schema/IDL to define and enforce contracts across services in a (decentralized) microservices network.
- **Cross-references**: TS-29 (JSON Schema)