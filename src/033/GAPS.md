# TS-33 gap analysis

Gaps found comparing TS-33: Java against the following reference resources:

- `src/033/__TODO__/README.adoc` (index only — links to the three files below)
- `src/033/__TODO__/naming.adoc`
- `src/033/__TODO__/nullability.adoc`
- `src/033/__TODO__/comments.adoc`

The three `SDCP-*.pdf` files in `src/033/__TODO__/` are binary PDFs and were
skipped silently per the skill's rules for non-text resources.

**Assessment.** The `naming.adoc` reference is far thinner than the standard's
own naming section and yielded no gaps. `comments.adoc` overlaps heavily with
the standard's comments section but adds substantive Javadoc content/semantic
guidance the standard omits — mostly partial gaps. `nullability.adoc` covers a
whole topic the standard does not address at all — entirely missing coverage,
and the largest single finding.

**Status:** Initial run, 2026-08-05. All gaps below remain open.

## Missing

- [ ] `src/033/__TODO__/nullability.adoc:1-110` — the standard addresses
      nullability nowhere. The reference covers the null-reference concept
      (Hoare's "billion-dollar mistake"), Java's lack of non-nullable types
      and null-safe operators, the verbose manual null-checking pattern, and
      the `NullPointerException` risk in method chains. Recommend a new
      section (e.g. a new `10-nullability.adoc`, or a subsection under
      `06-types.adoc`).

- [ ] `src/033/__TODO__/nullability.adoc:1-110` — the Java 8 `Optional` type
      as the recommended nullability mechanism: return type `X` when `X`
      cannot be null, `Optional<X>` when it can; `flatMap` chaining for
      null-safe traversal. Not addressed in the standard. Recommend the same
      new nullability section.

- [ ] `src/033/__TODO__/nullability.adoc:1-110` — caveats on `Optional`: it
      can itself be `null` (Java gives no guarantee), and it is not advised
      for method input parameters. Not addressed in the standard. Recommend
      the same new nullability section.

- [ ] `src/033/__TODO__/nullability.adoc:1-110` — nullability annotation
      libraries (JSR 305, Spring, JetBrains, Findbugs, Eclipse, Checker
      Framework, JSpecify, Lombok) with their `@NonNull`/`@Nullable`
      packages, and the caveat that none are bulletproof. Not addressed in
      the standard. Recommend the same new nullability section.

- [ ] `src/033/__TODO__/comments.adoc:122-162` — Javadoc MUST be used to
      help distinguish overloaded methods from each other, including
      constructors. The standard (`07-comments.adoc:87-121`) does not mention
      overloads. Recommend placing at `07-comments.adoc:87` (Javadoc
      section).

- [ ] `src/033/__TODO__/comments.adoc:122-162` — guidance on documenting
      private members: private methods SHOULD be documented if complex or
      called from multiple places; if called from one place, MAY be
      documented in the calling method instead. The standard says only that
      Javadoc is for `public`/`protected` members. Recommend placing at
      `07-comments.adoc:100` (after the public/protected member rule).

- [ ] `src/033/__TODO__/comments.adoc:163-227` — Javadoc description
      phrasing: method descriptions SHOULD start with a third-person
      descriptive verb ("Gets the label", not "Get the label");
      class/interface/field descriptions SHOULD state what the thing
      represents ("A button label"); avoid "This class…"/"This method…"
      phrasing. Not addressed in the standard. Recommend placing at
      `07-comments.adoc:141` (near the summary-fragment rule).

- [ ] `src/033/__TODO__/comments.adoc:228-271` — the `@since`, `@author`,
      and `@version` tags SHOULD NOT be included (the version control
      system tracks this; they are more useful in library than application
      development). The standard (`07-comments.adoc:149-159`) lists only
      `@param`/`@return`/`@throws`/`@deprecated` and is silent on these.
      Recommend placing at `07-comments.adoc:156`.

- [ ] `src/033/__TODO__/comments.adoc:272-301` — advanced Javadoc
      formatting: wrap Java keywords, package names, class names, method
      names, interface names, field names, argument names, and code
      examples in `<code> … </code>` blocks. Not addressed in the standard.
      Recommend a new subsection at `07-comments.adoc:170` (after block
      tags).

- [ ] `src/033/__TODO__/comments.adoc:289-301` — the `{@link}` inline tag
      for automatic links to other classes, methods, or fields, and the
      `@see` block tag as an alternative for cross-references. The standard
      does not mention either. Recommend placing at
      `07-comments.adoc:156` (block tags) and `07-comments.adoc:170`.

## Partial

- [ ] `src/033/__TODO__/comments.adoc:98-121` covers `//` more restrictively
      than `07-comments.adoc:14-19` — specifically, the reference says `//`
      SHOULD be avoided in production code and used only for temporary
      commented-out code and for noting expected return values/outputs,
      whereas the standard permits `//` for "short end-of-line comments"
      generally without that production caveat.

- [ ] `src/033/__TODO__/comments.adoc:98-121` adds guidance the standard
      omits at `07-comments.adoc:14-19` — specifically, that commented-out
      code SHOULD NOT be committed (version control tracks changes), and
      that `//` is preferred for temporary commented-out code precisely
      because static analysis pipelines can detect and reject it. The
      standard mentions `//` for "commenting-out code" without these
      caveats.

- [ ] `src/033/__TODO__/comments.adoc:122-162` covers Javadoc scope more
      thoroughly than `07-comments.adoc:100-108` — specifically, the
      reference requires Javadoc for all classes (not just `public` ones)
      and all public fields, and lists explicit exceptions (trivial
      getters/setters, trivial no-arg constructors that are not overridden,
      and methods that override without adding behavior). The standard
      says only that Javadoc SHOULD cover `public` classes and every
      `public`/`protected` member, and MAY be skipped for overriding
      methods.

- [ ] `src/033/__TODO__/comments.adoc:122-162` covers Javadoc content
      focus more thoroughly than `07-comments.adoc:97-99` — specifically,
      the reference states that long descriptions and usage examples
      SHOULD generally be excluded from Javadoc and placed in other
      documents (READMEs) referenced from the inline documentation. The
      standard says only that Javadoc MUST NOT document implementation
      details.

- [ ] `src/033/__TODO__/comments.adoc:228-271` covers block tags more
      thoroughly than `07-comments.adoc:149-159` — specifically, the
      reference adds: `@param` takes the parameter name (not data type)
      and MUST NOT wrap it in `<code>`, descriptions SHOULD be single
      sentences that are not capitalized or terminated with a period, and
      columns may be aligned; `@return` (not `@returns`) should state the
      type contained in returned collections; `@throws` should cover each
      declared and likely undeclared exception with the conditions under
      which each is thrown; `@deprecated` should include the date of
      deprecation and a reference to the replacement; `@see` for
      cross-references. The standard lists only the tag order and
      indentation.

## Out-of-scope

- [ ] `src/033/__TODO__/nullability.adoc:111-170` covers nullability in
      Kotlin, but this plausibly sits outside TS-33's stated purpose
      (Java coding guidelines) because it is a different language.
      Flagged for the user to confirm or overrule — a brief comparative
      note could be considered if the standard ever expands to
      JVM-ecosystem guidance.

## Unresolved

- [ ] `src/033/__TODO__/SDCP-1065287937-290722-0934.pdf`,
      `src/033/__TODO__/SDCP-1065287946-290722-0933.pdf`,
      `src/033/__TODO__/SDCP-2-Java-v1.0.0-290722-0931.pdf`, and
      `src/033/__TODO__/SDCP-BuildTools-v1.0.0-290722-0959.pdf` are binary
      PDFs and were not parsed. Not included in the comparison above.