# TS-30: YAML

This is a compact version of technical standard TS-30 for AI agents.

Use this when writing or reviewing YAML — application config, CI/CD pipeline
definitions, infrastructure-as-code manifests, or any other structured data
file.

Do NOT use this for GitHub Actions-specific behavior (expressions, workflow
design, GITHUB_TOKEN permissions) — see
[TS-60: GitHub Actions](../060/AGENTS.md), which builds on this standard. For
designing a JSON Schema to validate YAML documents, see
[TS-29: JSON Schema](../029/AGENTS.md).

## Rules

- **Target YAML 1.2 semantics, but write as if the parser might still be
  1.1.** YAML 1.2 restricts implicit booleans to `true`/`True`/`TRUE` and
  `false`/`False`/`FALSE`; YAML 1.1 also treats `yes`, `no`, `on`, `off`,
  `y`, `n`, and case variants as booleans (22 literals total — the "Norway
  problem," where a country code `NO` parses as `false`). Many libraries
  (eg. PyYAML's default loader) still default to 1.1 semantics regardless of
  what the document targets. Always quote a string value that coincides with
  a YAML 1.1 boolean literal.

- **Quote any numeric-looking string that is semantically a string.**
  Version numbers (`"1.10"`, not `1.10` — the float `1.1` loses the trailing
  zero), postal/zip codes, and any value with a leading zero (parsed as
  octal by a 1.1 parser) MUST be quoted if they are not meant to be numbers.

- **Use `.yaml`, not `.yml`, for new files.** `.yaml` is the officially
  recommended extension (since 2006). Stay consistent with whichever
  extension a project already uses; don't mix both.

- **Indentation MUST use spaces, never tabs.** Tabs are illegal in YAML
  indentation and produce a parse error. Two spaces per level is
  RECOMMENDED. Indent block-sequence items one level under their parent key
  for clarity, though the spec also permits them at the same level as the
  key.

- **Prefer block style over flow style for anything that changes over
  time.** Block style (indentation-based) produces clean, line-based Git
  diffs; flow style (`[a, b]`, `{k: v}`) rewrites the whole line on every
  change. Use flow style only for short, stable, single-line collections.
  Do not mix block and flow style within one collection.

- **Prefer single-quoted strings; use double quotes only when an escape
  sequence is needed.** Single quotes support one escape (`''` for a
  literal `'`); double quotes support full C-style escapes (`\n`, `\uXXXX`).

- **Use literal (`|`) or folded (`>`) block scalars for multi-line text**
  instead of a quoted string with embedded `\n` escapes. `|` preserves line
  breaks; `>` folds them into spaces (except around blank/indented lines).

- **A document start marker (`---`) SHOULD be present even for a single
  document**, and is REQUIRED when a stream holds more than one document.
  The end marker (`...`) is rarely needed outside multi-document streams.

- **Use anchors/aliases (`&name`/`*name`) and the merge key (`<<`) only for
  low-risk, shallow duplication.** Avoid them for security-sensitive values
  (permissions, secrets) — write those explicitly at each use site so a
  reviewer sees the effective value directly. The merge key does not
  recurse into nested mappings. Anchors/aliases are scoped to one document;
  they cannot be shared across files.

- **MUST parse untrusted YAML with a safe/restricted loader**
  (`yaml.safe_load()` in PyYAML, or the equivalent in other libraries),
  never an "unsafe"/"full" loader. An unsafe loader can construct arbitrary
  objects or execute code via language-specific tags (eg.
  `!!python/object/apply`).

- **Pair a safe loader with a resource limit when parsing untrusted YAML.**
  Nested anchor/alias expansion can exhaust memory/CPU (YAML's "billion
  laughs" analogue) even under a safe loader; cap document size, nesting
  depth, or alias expansion where the library supports it.

- **Delegate structural validation to JSON Schema.** YAML's data model is a
  JSON superset, so a parsed YAML document validates against the same JSON
  Schema tooling used elsewhere. Use a `# yaml-language-server: $schema=...`
  modeline, or an editor-level schema mapping, for real-time IDE validation.

- **Comments start with `#`, preceded by whitespace or line-start.** Use
  them for anything not obvious from the key/value/structure — the "why,"
  not the "what." Comments are stripped by parsers and not preserved on
  round-trip unless the library specifically supports it.

- **Lint with [yamllint](https://yamllint.readthedocs.io/).** Its `truthy`
  rule catches the Norway problem at lint time by restricting implicit
  booleans to `true`/`false`. Keep lines under 80 columns, avoid nesting
  deeper than four or five levels, and keep one document self-consistent
  (one indent width, one quoting style, one sequence-indent convention).

## References

- [TS-30 source](../../pages/030.adoc): \
  Read this for the full standard, rationale, and worked examples.

- [YAML 1.2.2 Specification](https://yaml.org/spec/1.2.2/): \
  Read this for the authoritative grammar and core-schema type-resolution
  rules.

- [TS-29: JSON Schema](../029/AGENTS.md): \
  Read this when designing a schema to validate a YAML document's structure.

- [TS-60: GitHub Actions](../060/AGENTS.md): \
  Read this for GitHub Actions-specific workflow/action conventions that
  build on this standard.

- [TS-52: Security and Secrets Management](../052/AGENTS.md): \
  Read this before committing any secret-adjacent value to a YAML file.
