# TODO

Outstanding work across the technical standards in this repository: standards
that are still stubs (no substantive content written), and standards whose
`GAPS.md` gap analysis still has open items.

This file is a manually-maintained index, regenerated from the tree. The
counts below were last regenerated on **2026-08-13**. Re-derive them with the
script in [Regenerating this file](#regenerating-this-file) before trusting
them after any content work.

## Stub standards

These pages have no substantive content yet — just a heading, `// TODO`
placeholder(s), and no `include::partial$NNN/...[]` includes.

| TS | Title | Notes |
| --- | --- | --- |
| [TS-24](src/modules/ROOT/pages/024.adoc) | User manuals | Has a short outline but is flagged to be split into separate Technical Documentation / User Documentation standards. |
| [TS-35](src/modules/ROOT/pages/035.adoc) | Python | Pure stub (`// Introduction.` placeholder only). |
| [TS-37](src/modules/ROOT/pages/037.adoc) | Web platform APIs | Pure stub aside from "See also" cross-references. Has a `GAPS.md` with 18 actionable items. |
| [TS-38](src/modules/ROOT/pages/038.adoc) | Node.js applications | Pure stub. `GAPS.md` explicitly notes this. |
| [TS-42](src/modules/ROOT/pages/042.adoc) | Vue | Pure stub (`// TODO: Introductory text…`). |
| [TS-44](src/modules/ROOT/pages/044.adoc) | Non-relational (NoSQL) databases | Pure stub. `GAPS.md` explicitly notes this. |
| [TS-55](src/modules/ROOT/pages/055.adoc) | Authentication and authorization | Pure stub (`// TODO` only). |

No open gap in any other standard's `GAPS.md` cross-references a stub, so the
stubs and the gap-closing work are independent. Writing a stub will not close
gaps recorded elsewhere — unlike TS-6, whose authoring closed six of TS-5's.

## Open gap analyses

Forty-one standards have a `GAPS.md`. One — TS-6 — is fully resolved and is
omitted from the table below; see
[partials/006/GAPS.md](src/modules/ROOT/partials/006/GAPS.md). The other forty
have open items.

### The two GAPS.md formats

The files are in two formats, and the columns mean different things in each.

- **Template format** (18 files). Follows the `gap-analysis` skill's bundled
  template: flat `- [ ]` checklists under `## Missing`, `## Partial`,
  `## Out-of-scope`, and `## Unresolved` headings.

- **Legacy format** (22 files). One `## <gap title>` subsection per gap, with
  `**Source**` / `**What the source says**` / `**Coverage check**` /
  `**Gap**` bullets, closed by appending a `**RESOLVED**` bullet. Some also
  carry a `**Cross-references**` field naming other standards the gap touches;
  the template format has no equivalent.

Legacy-format files are converted to the template format as they are worked,
not in a separate sweep.

### What the columns mean

- **Actionable** — `## Missing` plus `## Partial` items. Content that needs
  writing. This is the number to plan against. For legacy-format files it is
  every unresolved `## <gap title>` subsection, which mixes both kinds.

- **Scope** — `## Out-of-scope` items. Not authoring work: each is flagged
  for a human to confirm the exclusion or overrule it. Template format only.

- **Unresolved** — `## Unresolved` items. Reference resources that could not
  be retrieved when the analysis ran. Each needs re-fetching before it can
  become a gap or be dismissed. Template format only.

### Standards, ordered by actionable count

| TS | Title | Actionable | Scope | Unresolved | Format |
| --- | --- | ---: | ---: | ---: | --- |
| [TS-13](src/modules/ROOT/partials/013/GAPS.md) | Functional testing | 1 | — | — | Legacy |
| [TS-20](src/modules/ROOT/partials/020/GAPS.md) | Network APIs | 1 | — | — | Legacy |
| [TS-25](src/modules/ROOT/partials/025/GAPS.md) | Technical documentation | 1 | — | — | Legacy |
| [TS-36](src/modules/ROOT/partials/036/GAPS.md) | ECMAScript (JavaScript/TypeScript) | 1 | — | — | Legacy |
| [TS-38](src/modules/ROOT/partials/038/GAPS.md) | Node.js applications | 1 | — | — | Legacy — also a stub |
| [TS-41](src/modules/ROOT/partials/041/GAPS.md) | React | 1 | — | — | Legacy |
| [TS-46](src/modules/ROOT/partials/046/GAPS.md) | Distributed data and caching | 1 | 0 | 0 | Template |
| [TS-50](src/modules/ROOT/partials/050/GAPS.md) | Cloud economics | 1 | — | — | Legacy |
| [TS-52](src/modules/ROOT/partials/052/GAPS.md) | Security and secrets management | 1 | — | — | Legacy |
| [TS-54](src/modules/ROOT/partials/054/GAPS.md) | Threat modeling | 1 | — | — | Legacy |
| [TS-61](src/modules/ROOT/partials/061/GAPS.md) | AI tools | 1 | — | — | Legacy |
| [TS-3](src/modules/ROOT/partials/003/GAPS.md) | Design docs | 2 | — | — | Legacy |
| [TS-9](src/modules/ROOT/partials/009/GAPS.md) | Version control | 2 | — | — | Legacy |
| [TS-10](src/modules/ROOT/partials/010/GAPS.md) | Releasing | 2 | — | — | Legacy |
| [TS-11](src/modules/ROOT/partials/011/GAPS.md) | Versioning | 2 | 8 | 1 | Template |
| [TS-14](src/modules/ROOT/partials/014/GAPS.md) | Performance testing | 2 | — | — | Legacy |
| [TS-44](src/modules/ROOT/partials/044/GAPS.md) | Non-relational (NoSQL) databases | 2 | — | — | Legacy — also a stub |
| [TS-49](src/modules/ROOT/partials/049/GAPS.md) | Cloud platform engineering | 2 | — | — | Legacy |
| [TS-8](src/modules/ROOT/partials/008/GAPS.md) | Issue tracking | 3 | — | — | Legacy |
| [TS-23](src/modules/ROOT/partials/023/GAPS.md) | Messages and events | 3 | 2 | 0 | Template |
| [TS-2](src/modules/ROOT/partials/002/GAPS.md) | Software design qualities | 4 | — | — | Legacy — 1 of 5 resolved |
| [TS-4](src/modules/ROOT/partials/004/GAPS.md) | Modeling | 4 | 1 | 1 | Template |
| [TS-48](src/modules/ROOT/partials/048/GAPS.md) | Environment variables | 4 | 0 | 0 | Template |
| [TS-57](src/modules/ROOT/partials/057/GAPS.md) | Logging, monitoring, observability | 4 | — | — | Legacy |
| [TS-12](src/modules/ROOT/partials/012/GAPS.md) | Quality assurance | 6 | — | — | Legacy |
| [TS-31](src/modules/ROOT/partials/031/GAPS.md) | Unix shells and POSIX standards | 6 | 0 | 0 | Template |
| [TS-5](src/modules/ROOT/partials/005/GAPS.md) | Application architecture | 7 | — | — | Legacy — 6 of 13 resolved |
| [TS-7](src/modules/ROOT/partials/007/GAPS.md) | Code design | 13 | — | — | Legacy |
| [TS-27](src/modules/ROOT/partials/027/GAPS.md) | Markdown | 15 | 6 | 1 | Template |
| [TS-40](src/modules/ROOT/partials/040/GAPS.md) | CSS | 17 | 12 | 1 | Template |
| [TS-37](src/modules/ROOT/partials/037/GAPS.md) | Web platform APIs | 18 | 4 | 1 | Template — also a stub |
| [TS-26](src/modules/ROOT/partials/026/GAPS.md) | Technical writing style guide | 29 | 10 | 2 | Template |
| [TS-29](src/modules/ROOT/partials/029/GAPS.md) | JSON Schema | 29 | 3 | 2 | Template |
| [TS-21](src/modules/ROOT/partials/021/GAPS.md) | HTTP APIs | 49 | 13 | 4 | Template |
| [TS-15](src/modules/ROOT/partials/015/GAPS.md) | User interfaces | 50 | 7 | 12 | Template |
| [TS-33](src/modules/ROOT/partials/033/GAPS.md) | Java | 55 | 3 | 4 | Template |
| [TS-18](src/modules/ROOT/partials/018/GAPS.md) | Web GUIs | 56 | 26 | 5 | Template |
| [TS-16](src/modules/ROOT/partials/016/GAPS.md) | Command line interfaces (CLIs) | 59 | 9 | 1 | Template |
| [TS-43](src/modules/ROOT/partials/043/GAPS.md) | Relational databases and SQL | 61 | 6 | 4 | Template |
| [TS-39](src/modules/ROOT/partials/039/GAPS.md) | HTML | 136 | 5 | 4 | Template |
| | **Total** | **653** | **115** | **43** | |

Twenty-seven of the forty standards hold six or fewer actionable items each.
Seven standards — TS-39, TS-43, TS-16, TS-18, TS-33, TS-15, TS-21 — hold 466
of the 653 between them, and each needs several passes rather than one.

## Standards with neither a stub nor a GAPS.md

TS-1, TS-17, TS-19, TS-22, TS-28, TS-30, TS-32, TS-34, TS-45, TS-47, TS-51,
TS-53, TS-56, TS-58, TS-59, TS-60, TS-62, and TS-63 all have substantive
content and no recorded gap analysis. A gap analysis (`/gap-analysis`) could
be run against any of them; none is known to be missing content today.

## Known inconsistencies

Surfaced on 2026-08-13 while writing the `close-gaps` skill. These are
repo-level decisions and defects, not gap-closing work, but the first two
govern how all new content should be written.

- **RESOLVED — a dropped `include::` on the TS-27 page.**
  `pages/027.adoc` carried two `include::` directives on one source line, so
  `08-code.adoc` was absent from the built page and the second directive
  rendered as literal text. Split onto separate lines on 2026-08-13.

- **RESOLVED — cross-reference bold markup.** The style guide required
  `xref:NNN.adoc[*TS-N: Title*]` while all 237 cross-references in the corpus
  used `*xref:NNN.adoc[TS-N: Title]*`, the form it names as wrong. Settled on
  2026-08-13 in favor of the style guide: all 237 were converted, `AGENTS.md`
  was corrected to match, and three cross-references that were split across
  source lines were joined.

- **Self-referencing cross-references.** Twenty-nine `xref:` macros point at
  the page that contains them — 28 within TS-9, 1 within TS-49. They render
  as a link to the page the reader is already on. They predate the move to
  one merged page per standard, when each partial was its own page. The style
  guide (lines 96–102) requires `<<Section title>>` for a reference to
  another section of the same standard.

- **Link text that does not match the target's title.** Some cross-references
  label the target in title case (`TS-43: Relational Databases and SQL`)
  where the page's own title is sentence case (`TS-43: Relational databases
  and SQL`). Not audited in full.

- **Reference lists in a trailing partial.** `docs/style-guide.md` (lines
  150–153) says a reference list MUST NOT be split into a separate partial.
  Eight standards do exactly that: TS-17, TS-18, TS-21, TS-23, TS-29, TS-31,
  TS-32, and TS-33. Twenty-three pages carry a `== References` section.

- **A broken sentence in the `deep-dive` skill.**
  `.agents/skills/deep-dive/SKILL.md:55` reads "The mechanical verification in
  MUST have run" — a step reference has gone missing.

## Regenerating this file

Run from `src/modules/ROOT/partials/`:

```sh
for d in $(ls -d [0-9][0-9][0-9]/ | sort); do
  n="${d%/}"; g="$n/GAPS.md"; [ -f "$g" ] || continue
  if grep -q '^## Missing' "$g"; then
    awk -v n="$n" '
      /^## /   { s = substr($0, 4) }
      /^- \[ \]/ { c[s]++ }
      END { printf "%s template actionable=%d scope=%d unresolved=%d\n",
              n, c["Missing"] + c["Partial"], c["Out-of-scope"],
              c["Unresolved"] }' "$g"
  else
    awk -v n="$n" '
      /^## /            { total++; resolved_here = 0 }
      /\*\*RESOLVED\*\*/ { if (!resolved_here) { done++; resolved_here = 1 } }
      END { printf "%s legacy actionable=%d\n", n, total - done }' "$g"
  fi
done
```

Stub standards are those whose page has no `include::partial$` directive:

```sh
grep -L 'include::partial\$' src/modules/ROOT/pages/[0-9][0-9][0-9].adoc
```
