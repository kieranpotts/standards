# TODO

Outstanding work across the technical standards in this repository: standards
that are still stubs (no substantive content written), and standards with a
`GAPS.md` gap analysis that has open, unresolved gaps.

This file is a manually-maintained index. Regenerate it by re-checking each
page and its `GAPS.md` before trusting it fully out of date.

## Stub standards

These pages have no substantive content yet — just a heading, `// TODO`
placeholder(s), and (in most cases) no `include::partial$NNN/...[]` includes.

| TS | Title | Notes |
| --- | --- | --- |
| [TS-24](src/modules/ROOT/pages/024.adoc) | User Manuals | Has a short outline but is flagged to be split into separate Technical Documentation / User Documentation standards. |
| [TS-35](src/modules/ROOT/pages/035.adoc) | Python | Pure stub (`// Introduction.` placeholder only). |
| [TS-37](src/modules/ROOT/pages/037.adoc) | Web Platform APIs | Pure stub aside from "See also" cross-references; has a GAPS.md with open gaps. |
| [TS-38](src/modules/ROOT/pages/038.adoc) | Node.js Applications | Pure stub. GAPS.md explicitly notes this. |
| [TS-42](src/modules/ROOT/pages/042.adoc) | Vue | Pure stub (`// TODO: Introductory text…`). |
| [TS-44](src/modules/ROOT/pages/044.adoc) | Non-Relational (NoSQL) Databases | Pure stub. GAPS.md explicitly notes this. |
| [TS-55](src/modules/ROOT/pages/055.adoc) | Authentication and Authorization | Pure stub (`// TODO` only). |

## Standards with open GAPS.md analysis

Every standard below has a `GAPS.md` file recording coverage gaps found by
comparing it against external reference sources, and at least one of those
gaps is still unresolved (no `**RESOLVED**` entry). TS-2 (1 of 5) and TS-5
(6 of 13) are the only standards with any gaps closed so far. TS-6's GAPS.md
has been fully resolved (2 of 2) and so no longer appears in this table — see
[partials/006/GAPS.md](src/modules/ROOT/partials/006/GAPS.md).

| TS | Title | GAPS.md |
| --- | --- | --- |
| TS-2 | Software Design Qualities | [partials/002/GAPS.md](src/modules/ROOT/partials/002/GAPS.md) — 1 of 5 resolved, 4 open |
| TS-3 | Design Docs | [partials/003/GAPS.md](src/modules/ROOT/partials/003/GAPS.md) |
| TS-4 | Modeling | [partials/004/GAPS.md](src/modules/ROOT/partials/004/GAPS.md) |
| TS-5 | Application Architecture | [partials/005/GAPS.md](src/modules/ROOT/partials/005/GAPS.md) — 6 of 13 resolved, 7 open |
| TS-7 | Code Design | [partials/007/GAPS.md](src/modules/ROOT/partials/007/GAPS.md) |
| TS-8 | Issue Tracking | [partials/008/GAPS.md](src/modules/ROOT/partials/008/GAPS.md) |
| TS-9 | Version Control | [partials/009/GAPS.md](src/modules/ROOT/partials/009/GAPS.md) |
| TS-10 | Releasing | [partials/010/GAPS.md](src/modules/ROOT/partials/010/GAPS.md) |
| TS-11 | Versioning | [partials/011/GAPS.md](src/modules/ROOT/partials/011/GAPS.md) |
| TS-12 | Quality Assurance | [partials/012/GAPS.md](src/modules/ROOT/partials/012/GAPS.md) |
| TS-13 | Functional Testing | [partials/013/GAPS.md](src/modules/ROOT/partials/013/GAPS.md) |
| TS-14 | Performance Testing | [partials/014/GAPS.md](src/modules/ROOT/partials/014/GAPS.md) |
| TS-15 | User Interfaces | [partials/015/GAPS.md](src/modules/ROOT/partials/015/GAPS.md) |
| TS-16 | Command Line Interfaces (CLIs) | [partials/016/GAPS.md](src/modules/ROOT/partials/016/GAPS.md) |
| TS-18 | Web GUIs | [partials/018/GAPS.md](src/modules/ROOT/partials/018/GAPS.md) |
| TS-20 | Network APIs | [partials/020/GAPS.md](src/modules/ROOT/partials/020/GAPS.md) |
| TS-21 | HTTP APIs | [partials/021/GAPS.md](src/modules/ROOT/partials/021/GAPS.md) |
| TS-23 | Messages and Events | [partials/023/GAPS.md](src/modules/ROOT/partials/023/GAPS.md) |
| TS-25 | Technical Documentation | [partials/025/GAPS.md](src/modules/ROOT/partials/025/GAPS.md) |
| TS-26 | Technical Writing Style Guide | [partials/026/GAPS.md](src/modules/ROOT/partials/026/GAPS.md) |
| TS-27 | Markdown | [partials/027/GAPS.md](src/modules/ROOT/partials/027/GAPS.md) |
| TS-29 | JSON Schema | [partials/029/GAPS.md](src/modules/ROOT/partials/029/GAPS.md) |
| TS-31 | Unix Shells and POSIX Standards | [partials/031/GAPS.md](src/modules/ROOT/partials/031/GAPS.md) |
| TS-33 | Java | [partials/033/GAPS.md](src/modules/ROOT/partials/033/GAPS.md) |
| TS-36 | ECMAScript (JavaScript/TypeScript) | [partials/036/GAPS.md](src/modules/ROOT/partials/036/GAPS.md) |
| TS-37 | Web Platform APIs | [partials/037/GAPS.md](src/modules/ROOT/partials/037/GAPS.md) — also a stub, see above |
| TS-38 | Node.js Applications | [partials/038/GAPS.md](src/modules/ROOT/partials/038/GAPS.md) — also a stub, see above |
| TS-39 | HTML | [partials/039/GAPS.md](src/modules/ROOT/partials/039/GAPS.md) |
| TS-40 | CSS | [partials/040/GAPS.md](src/modules/ROOT/partials/040/GAPS.md) |
| TS-41 | React | [partials/041/GAPS.md](src/modules/ROOT/partials/041/GAPS.md) |
| TS-43 | Relational Databases and SQL | [partials/043/GAPS.md](src/modules/ROOT/partials/043/GAPS.md) |
| TS-44 | Non-Relational (NoSQL) Databases | [partials/044/GAPS.md](src/modules/ROOT/partials/044/GAPS.md) — also a stub, see above |
| TS-46 | Distributed Data and Caching | [partials/046/GAPS.md](src/modules/ROOT/partials/046/GAPS.md) |
| TS-48 | Environment Variables | [partials/048/GAPS.md](src/modules/ROOT/partials/048/GAPS.md) |
| TS-49 | Cloud Platform Engineering | [partials/049/GAPS.md](src/modules/ROOT/partials/049/GAPS.md) |
| TS-50 | Cloud Economics | [partials/050/GAPS.md](src/modules/ROOT/partials/050/GAPS.md) |
| TS-52 | Security and Secrets Management | [partials/052/GAPS.md](src/modules/ROOT/partials/052/GAPS.md) |
| TS-54 | Threat Modeling | [partials/054/GAPS.md](src/modules/ROOT/partials/054/GAPS.md) |
| TS-57 | Logging, Monitoring, Observability | [partials/057/GAPS.md](src/modules/ROOT/partials/057/GAPS.md) |
| TS-61 | AI Tools | [partials/061/GAPS.md](src/modules/ROOT/partials/061/GAPS.md) |

## Standards with neither a stub nor a GAPS.md

Every other standard (TS-1, TS-17, TS-19, TS-22, TS-28, TS-30, TS-32, TS-34,
TS-45, TS-47, TS-51, TS-53, TS-56, TS-58, TS-59, TS-60, TS-62, TS-63) has
substantive content and no recorded gap analysis yet. A gap analysis
(`/gap-analysis`) could still be run against any of these; none is known to
be missing today.
