# GAPS — TS-52 Security and secrets management

Coverage gaps identified by comparing external sources against this standard.

---

## Low-level / systems security (undefined behavior, memory safety, ASLR/DEP)

- **Source**: https://blog.nelhage.com/post/computers-can-be-understood/
- **What the source says**: Security reasoning often requires working across multiple abstraction layers — the C spec calls a buffer overflow "undefined behavior," but turning one into RCE, or reasoning about mitigations like ASLR and DEP, requires understanding the compiler, libc, and hardware implementation.
- **Coverage check**: TS-52 and TS-54 are application-security focused (third-party code review, encryption, secrets, auth, network/web-app security, STRIDE/OWASP). A search for "undefined behavior," "buffer overflow," "ASLR," "DEP," and "memory safety" returns no matches anywhere in `src/`.
- **Gap**: No standard covers systems-level security — undefined behavior, memory-safety vulnerabilities, or hardware/OS exploit mitigations (ASLR, DEP) — and the multi-layer reasoning required to understand them.
- **Cross-references**: TS-54 (Threat modeling)