# GAPS — TS-36 ECMAScript (JavaScript/TypeScript)

Coverage gaps identified by comparing external sources against this standard.

---

## One language (TypeScript) shared across front and back end

- **Source**: https://newsletter.pragmaticengineer.com/p/bluesky-engineering-culture
- **What the source says**: Bluesky uses TypeScript for the backend, frontend, and mobile apps so engineers can work across the stack without switching languages, citing shared schema understanding, code-generation ergonomics, and rapid prototyping.
- **Coverage check**: TS-36 is a coding-conventions standard. A search of its architecture-and-design section for shared-language / full-stack / isomorphic concepts returned no matches. The standard addresses how to write ECMAScript, not the architectural decision to standardize on one language across the stack.
- **Gap**: TS-36 does not address the full-stack single-language strategy or its trade-offs. This may be out of scope for TS-36 (closer to TS-5/TS-7), but no standard in the index clearly owns it.
- **Cross-references**: TS-5 (Application architecture)