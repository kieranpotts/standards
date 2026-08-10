# TS-47: Dates and Times

Best practices for working with, and storing, date and time values.

Date and time values are captured in string data types in most programming
languages and data storage systems. There are multiple formats that can
be used to represent them. Which formats to support is an important
design consideration with impacts on interoperability, maintainability,
and usability.

Use this when designing or implementing systems that store, transmit, or
display date and time values.

Do NOT use this for database engine or schema specifics — see
[TS-43: Relational Databases and SQL](../043/AGENTS.md) and
[TS-44: Non-Relational (NoSQL) Databases](../044/AGENTS.md). For general
code design, see [TS-7: Code Design](../007/AGENTS.md).

## Rules

- **Use RFC 3339.** Applications MUST use the
  [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339) standard (analogous
  to [ISO 8601](https://www.iso.org/standard/70907.html)) for representing
  dates and times in data storage and data exchange formats.

- **Use a small, interoperable subset of formats.** It is strongly
  RECOMMENDED that applications use a small subset of date and time
  encoding formats that are compliant with both RFC 3339 and ISO 8601 and
  have high interoperability with other standards (eg. the HTML Living
  Standard). The RECOMMENDED subset:

  | Description | Format | Example |
  |---|---|---|
  | Date only | `%Y-%M-%D` | `2025-12-31` |
  | Time in UTC | `%h:%m:%sZ` | `23:59:59Z` |
  | Time with UTC offset | `%h:%m:%s±00:00` | `23:59:59+00:00` |
  | Date and time in UTC | `%Y-%M-%DT%h:%m:%sZ` | `2025-12-31T23:59:59Z` |
  | Date and time with UTC offset | `%Y-%M-%DT%h:%m:%s±00:00` | `2025-12-31T23:59:59-00:00` |

  Use uppercase `T` and `Z` symbols, not lowercase.

- **Use split-second formats only when fine-grained precision is
  required.** Split second formats (eg. `2025-01-10T11:15:21.027652567Z`)
  SHOULD be used only when the precision is required for the use case —
  for example, high-frequency trading systems, scientific applications, or
  performance benchmarking.

- **Transmit and store in UTC.** Dates and times SHOULD be transmitted and
  stored in UTC, and converted to the local time zone only when required
  for application output or processing. Exception: when the local time zone
  is a critical part of the data and it is a requirement that the data be
  represented in the original time zone.

- **Accept alternative input formats, but normalize before persisting.**
  Applications MAY accept date and time values in a wider range of
  formats as input for a more convenient user experience, but alternative
  formats SHOULD be converted to the recommended subset before persisting
  or exchanging the data with other internal systems.

- **Render in human-readable locale-specific format for UIs.** Dates and
  times SHOULD be rendered in a human-readable locale-specific format for
  user interfaces.

### Timestamps and the Year 2038 problem

- **Use timestamp representations wide enough for dates beyond 2038.** A
  signed 32-bit integer overflows at 2038-01-19T03:14:07Z (the Year 2038
  problem, Y2038). Applications and data storage systems MUST use
  representations that accommodate dates beyond 2038 — a signed 64-bit
  integer is effectively immune to overflow. Verify rather than assume,
  particularly with legacy systems, C libraries, file formats, or binary
  protocols that may use 32-bit timestamps.

- **Avoid 32-bit timestamp types.** Common sources: `time_t` on legacy C/C++
  platforms (use a 64-bit type explicitly); `TIMESTAMP` in some SQL engines
  (prefer `DATETIME` or a 64-bit `TIMESTAMP` — see
  [TS-43](../043/AGENTS.md)); binary formats and wire protocols (use at
  least 64 bits when designing new formats; check specs when consuming
  existing ones).

- **Prefer string representations for storage and exchange.** The most
  robust defense against timestamp overflow is to store and exchange dates
  and times as RFC 3339 strings, which have no fixed width and are not
  subject to integer overflow. Where an integer timestamp is required (eg.
  a compact binary protocol), it MUST be at least 64 bits wide.

## References

- [TS-47: Dates and Times (source)](../../pages/047-dates-and-times.adoc)
- [TS-7: Code Design](../007/AGENTS.md)
- [TS-43: Relational Databases and SQL](../043/AGENTS.md)
- [TS-44: Non-Relational (NoSQL) Databases](../044/AGENTS.md)
- [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339)
- [ISO 8601](https://www.iso.org/standard/70907.html)
- [RFC 3339 vs ISO 8601](https://ijmacd.github.io/rfc3339-iso8601/) — Venn
  diagram showing where the two standards overlap
