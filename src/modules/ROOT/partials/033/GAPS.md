# TS-33 gap analysis

Gaps found comparing TS-33: Java against the following reference resources.

## Run 1 — `__TODO__/033/` (2026-08-05)

- `__TODO__/033/README.adoc` (index only — links to the three files below)
- `__TODO__/033/naming.adoc`
- `__TODO__/033/nullability.adoc`
- `__TODO__/033/comments.adoc`

The three `SDCP-*.pdf` files in `__TODO__/033/` are binary PDFs and were
skipped silently per the skill's rules for non-text resources.

**Assessment.** The `naming.adoc` reference is far thinner than the standard's
own naming section and yielded no gaps. `comments.adoc` overlaps heavily with
the standard's comments section but adds substantive Javadoc content/semantic
guidance the standard omits — mostly partial gaps. `nullability.adoc` covers a
whole topic the standard does not address at all — entirely missing coverage,
and the largest single finding.

## Run 2 — GitHub issue #66 (2026-08-05)

Issue [#66](https://github.com/kieranpotts/standards/issues/66) ("Java") is an
index of eight URLs (one duplicated), each treated as a reference resource:

- https://www.infoworld.com/article/2165633/design-for-thread-safety.html
- https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html
- https://source.android.com/docs/setup/contribute/code-style#use-javadoc-standard-comments
- https://www.oracle.com/java/technologies/javase/codeconventions-comments.html#385
- https://www.theserverside.com/feature/Java-naming-conventions-explained
- https://google.github.io/styleguide/javaguide.html#s3.4.1-one-top-level-class
- https://www.quora.com/What-is-the-difference-between-string-args-and-string-args-in-Java
- https://www.oracle.com/java/technologies/javase/codeconventions-introduction.html

**Assessment.** The Oracle "How to Write Doc Comments for the Javadoc Tool"
article and the Oracle Code Conventions comments page together produce the
bulk of the new findings — they are detailed Javadoc authoring guides, and
TS-33's comments section is comparatively thin on Javadoc _content_ rules
(tag semantics, description phrasing, spec vs. guide distinction, package-level
docs). The Google Java Style Guide (already TS-33's primary basis) surfaces
several modern-Java features the standard does not mention at all: records,
text blocks, arrow-style switch and switch expressions, the `_` unnamed
variable syntax, and `package-info`/`module-info` file structures. The InfoWorld
thread-safety article is design-level concurrency material that TS-33
explicitly defers to TS-7, so it is out-of-scope here. The TheServerSide naming
article overlaps almost entirely with TS-33's naming section and adds only the
observation that records are a reference type absent from TS-33's terminology.
The Oracle Code Conventions introduction is rationale/meta material (and is
itself an archived, unmaintained document last revised 1999) — no coverage
gaps. The Quora URL could not be fetched (see Unresolved).

**Status:** Re-run, 2026-08-05. All Run 1 gaps remain open (the standard has
not been modified). Run 2 gaps added below.

## Missing

### From Run 1 (`__TODO__/`)

- [ ] `__TODO__/033/nullability.adoc:1-110` — the standard addresses
      nullability nowhere. The reference covers the null-reference concept
      (Hoare's "billion-dollar mistake"), Java's lack of non-nullable types
      and null-safe operators, the verbose manual null-checking pattern, and
      the `NullPointerException` risk in method chains. Recommend a new
      section (e.g. a new `10-nullability.adoc`, or a subsection under
      `06-types.adoc`).

- [ ] `__TODO__/033/nullability.adoc:1-110` — the Java 8 `Optional` type
      as the recommended nullability mechanism: return type `X` when `X`
      cannot be null, `Optional<X>` when it can; `flatMap` chaining for
      null-safe traversal. Not addressed in the standard. Recommend the same
      new nullability section.

- [ ] `__TODO__/033/nullability.adoc:1-110` — caveats on `Optional`: it
      can itself be `null` (Java gives no guarantee), and it is not advised
      for method input parameters. Not addressed in the standard. Recommend
      the same new nullability section.

- [ ] `__TODO__/033/nullability.adoc:1-110` — nullability annotation
      libraries (JSR 305, Spring, JetBrains, Findbugs, Eclipse, Checker
      Framework, JSpecify, Lombok) with their `@NonNull`/`@Nullable`
      packages, and the caveat that none are bulletproof. Not addressed in
      the standard. Recommend the same new nullability section.

- [ ] `__TODO__/033/comments.adoc:122-162` — Javadoc MUST be used to
      help distinguish overloaded methods from each other, including
      constructors. The standard (`07-comments.adoc:87-121`) does not mention
      overloads. Recommend placing at `07-comments.adoc:87` (Javadoc
      section).

- [ ] `__TODO__/033/comments.adoc:122-162` — guidance on documenting
      private members: private methods SHOULD be documented if complex or
      called from multiple places; if called from one place, MAY be
      documented in the calling method instead. The standard says only that
      Javadoc is for `public`/`protected` members. Recommend placing at
      `07-comments.adoc:100` (after the public/protected member rule).

- [ ] `__TODO__/033/comments.adoc:163-227` — Javadoc description
      phrasing: method descriptions SHOULD start with a third-person
      descriptive verb ("Gets the label", not "Get the label");
      class/interface/field descriptions SHOULD state what the thing
      represents ("A button label"); avoid "This class…"/"This method…"
      phrasing. Not addressed in the standard. Recommend placing at
      `07-comments.adoc:141` (near the summary-fragment rule).

- [ ] `__TODO__/033/comments.adoc:228-271` — the `@since`, `@author`,
      and `@version` tags SHOULD NOT be included (the version control
      system tracks this; they are more useful in library than application
      development). The standard (`07-comments.adoc:149-159`) lists only
      `@param`/`@return`/`@throws`/`@deprecated` and is silent on these.
      Recommend placing at `07-comments.adoc:156`.

- [ ] `__TODO__/033/comments.adoc:272-301` — advanced Javadoc
      formatting: wrap Java keywords, package names, class names, method
      names, interface names, field names, argument names, and code
      examples in `<code> … </code>` blocks. Not addressed in the standard.
      Recommend a new subsection at `07-comments.adoc:170` (after block
      tags).

- [ ] `__TODO__/033/comments.adoc:289-301` — the `{@link}` inline tag
      for automatic links to other classes, methods, or fields, and the
      `@see` block tag as an alternative for cross-references. The standard
      does not mention either. Recommend placing at
      `07-comments.adoc:156` (block tags) and `07-comments.adoc:170`.

### From Run 2 (issue #66)

- [ ] `https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html#Introduction`
      — Javadoc should textually document the thread-safety guarantees of an
      object; absent explicit indication, all objects are assumed
      thread-safe. TS-33's comments section does not mention documenting
      thread-safety. Recommend placing at `07-comments.adoc:97` (Javadoc
      content rules). (The design of thread-safe classes themselves is
      TS-7's domain, but the documentation obligation is a Javadoc concern.)

- [ ] `https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html#Introduction`
      — The distinction between an API specification (a contract describing
      behavior callers can rely on, implementation-independent) and a
      programming guide (examples, term definitions, conceptual overviews,
      bug/workaround notes). TS-33 says Javadoc is for "API documentation"
      but does not draw this distinction or warn against mixing the two.
      Recommend placing at `07-comments.adoc:87`.

- [ ] `https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html#Descriptions`
      — The spec should be complete enough for conforming implementors,
      including boundary conditions, parameter ranges, and corner cases,
      and should state what is left unspecified. TS-33 does not address
      Javadoc spec completeness. Recommend placing at `07-comments.adoc:97`.

- [ ] `https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html#Descriptions`
      — Implementation-specific behavior should be documented in a separate
      paragraph with a lead-in such as "On <platform>" or
      "Implementation-Specific:". Not addressed in the standard. Recommend
      placing at `07-comments.adoc:97`.

- [ ] `https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html#Tag-Conventions`
      — The canonical block-tag order is `@author`, `@version`, `@param`,
      `@return`, `@throws`, `@see`, `@since`, `@serial`/`@serialField`/`@serialData`,
      `@deprecated`; multiple `@param` in argument-declaration order; multiple
      `@throws` alphabetically by exception name; multiple `@see` by access
      proximity (nearest to farthest). TS-33 (`07-comments.adoc:149-159`)
      lists only `@param`/`@return`/`@throws`/`@deprecated` in order and gives
      no multi-tag ordering rules. Recommend placing at `07-comments.adoc:156`.

- [ ] `https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html#Required-Tags`
      — `@param` is required for every parameter (even when obvious), and
      `@return` is required for every non-void method (even if seemingly
      redundant). TS-33 lists these tags but does not state they are
      required. Recommend placing at `07-comments.adoc:151` and
      `07-comments.adoc:152`.

- [ ] `https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html#Documenting-Exceptions-with-throws-Tag`
      — `@throws` should cover all checked exceptions and any unchecked
      exception the caller might reasonably want to catch (except
      `NullPointerException`); errors should not be documented; an unchecked
      exception tied to the current implementation should not be documented
      (use `IndexOutOfBoundsException`, not `ArrayIndexOutOfBoundsException`);
      `@throws` is distinct from the `throws` clause, and including
      unchecked exceptions in the `throws` clause is poor practice. TS-33
      (`07-comments.adoc:153` and `05-programming-constructs.adoc:196-224`)
      does not address any of this. Recommend placing at `07-comments.adoc:153`.

- [ ] `https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html#Tag-Comments`
      — `@deprecated`'s first sentence should state when the API was
      deprecated and what to use as a replacement, using `{@link}` (or
      `@see`) to point to the replacement; if no replacement, state "No
      replacement". TS-33 lists `@deprecated` but gives no content guidance
      for it. Recommend placing at `07-comments.adoc:154`.

- [ ] `https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html#Custom-Tags-and-Annotations`
      — Use both the `@Deprecated` annotation (compiler warning) and the
      `@deprecated` Javadoc tag (documentation) together. TS-33 mentions
      `@Deprecated` only in a formatting example
      (`05-programming-constructs.adoc:153`) and `@deprecated` only as a
      Javadoc tag, without linking the two. Recommend placing at
      `07-comments.adoc:154` or `05-programming-constructs.adoc:129`.

- [ ] `https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html#Documenting-Default-Constructors`
      — All constructors in public and protected classes should be explicit
      (no implicit default constructors in public APIs), because an
      explicit declaration forces a decision about access and prevents
      inadvertent public instantiability. TS-33 does not address default
      constructors. Recommend placing at `05-programming-constructs.adoc:36`
      (classes and interfaces section) or a new subsection.

- [ ] `https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html#Package-Level-Comments`
      — Package-level Javadoc via `package-info.java` (or `package.html`),
      including its recommended structure: a summary sentence, a "Package
      Specification" section, and a "Related Documentation" section. TS-33
      does not mention package-level documentation. Recommend a new
      subsection at `07-comments.adoc:170` or `02-source-files.adoc`.

- [ ] `https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html#Documenting-Anonymous-Inner-Classes`
      — The Javadoc tool does not document anonymous inner classes; they
      should be documented in the doc comment of their outer class. TS-33
      does not mention this. Recommend placing at `07-comments.adoc:100`.

- [ ] `https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html#Including-Images`
      — Including images in Javadoc via a per-package `doc-files` directory,
      with images named `<class>-<n>.gif`. TS-33 does not address Javadoc
      images. Recommend a new subsection at `07-comments.adoc:170`.

- [ ] `https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html#Troubleshooting-Curly-Quotes`
      — Avoid curly/smart quotes (from word processors) in Javadoc; use
      straight quotes. TS-33 does not mention this. Recommend placing at
      `07-comments.adoc:21` (near the whitespace/comment-format rules) or
      `07-comments.adoc:87`.

- [ ] `https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html#A-Style-Guide`
      — Use "this" rather than "the" when referring to the current object
      ("Gets the toolkit for this component"); omit parentheses when
      referring to the general form of a method ("the `add` method") and
      use them with argument types only for a specific overload ("the
      `add(int, Object)` method"). TS-33 does not address either. Recommend
      placing at `07-comments.adoc:141`.

- [ ] `https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html#A-Style-Guide`
      — Avoid Latin abbreviations in Javadoc: use "also known as" not "aka",
      "that is" not "i.e.", "for example" not "e.g.", "in other words"/"namely"
      not "viz.". TS-33 does not address this. Recommend placing at
      `07-comments.adoc:87`. (Borderline — also a technical-writing concern
      covered by TS-26 — but applied here to Javadoc content.)

- [ ] `https://www.oracle.com/java/technologies/javase/codeconventions-comments.html#385`
      — Avoid redundant comments that are likely to get out of date as the
      code evolves. TS-33 (`07-comments.adoc:75-85`) says comments should
      communicate info not readily available from the code but does not
      warn against staleness. Recommend placing at `07-comments.adoc:75`.

- [ ] `https://www.oracle.com/java/technologies/javase/codeconventions-comments.html#385`
      — The frequency of comments sometimes reflects poor code quality;
      when you feel compelled to add a comment, consider rewriting the
      code to make it clearer. TS-33 does not make this point. Recommend
      placing at `07-comments.adoc:75`.

- [ ] `https://www.oracle.com/java/technologies/javase/codeconventions-comments.html#385`
      — Comments should not be enclosed in boxes drawn with asterisks or
      other characters. TS-33 does not prohibit this. Recommend placing at
      `07-comments.adoc:21`.

- [ ] `https://www.oracle.com/java/technologies/javase/codeconventions-comments.html#385`
      — Multi-line block comment format: `/*` on its own line, subsequent
      lines beginning with ` * ` aligned to the first `*`, closing ` */` on
      its own line. TS-33 (`07-comments.adoc:21-27`) describes when to use
      `/* … */` but does not specify the asterisk-alignment convention for
      wrapped comments. Recommend placing at `07-comments.adoc:26`.

- [ ] `https://www.oracle.com/java/technologies/javase/codeconventions-comments.html#385`
      — Doc comments must not be positioned inside a method or constructor
      body (Java associates a doc comment with the first declaration after
      it). TS-33 does not state this. Recommend placing at `07-comments.adoc:87`.

- [ ] `https://www.oracle.com/java/technologies/javase/codeconventions-comments.html#385`
      — Javadoc indentation rules: for top-level classes/interfaces the
      first `/**` line is not indented and subsequent lines have 1 space to
      align asterisks; for members the first line is indented 4 spaces and
      subsequent lines 5. TS-33 (`07-comments.adoc` and
      `04-code-style.adoc:11-23`) gives general indentation rules but no
      Javadoc-specific asterisk-alignment rules. Recommend a new subsection
      at `07-comments.adoc:122` (near the multi-line form).

- [ ] `https://www.oracle.com/java/technologies/javase/codeconventions-comments.html#385`
      — Information about a class/interface/variable/method that is not
      appropriate for documentation should go in an implementation block
      comment or single-line comment immediately after the declaration,
      not in the doc comment. TS-33 (`07-comments.adoc:97-98`) says Javadoc
      must not document implementation details but does not say where such
      detail should go. Recommend placing at `07-comments.adoc:98`.

- [ ] `https://www.theserverside.com/feature/Java-naming-conventions-explained#PascalCase-for-Java-reference-types`
      and `https://google.github.io/styleguide/javaguide.html#s1.1` —
      Records are a Java reference type (alongside classes, interfaces,
      annotations, and enums). TS-33's "class-like constructs" definition
      (`01-terminology.adoc:5-6`) and naming section
      (`03-naming-conventions.adoc:88`) do not mention records at all — no
      naming, formatting, or terminology guidance for record classes.
      Recommend updating `01-terminology.adoc:5` and
      `03-naming-conventions.adoc:88`.

- [ ] `https://google.github.io/styleguide/javaguide.html#s3` — Special
      source-file structures for `package-info.java` (package-level
      declarations/doc comments) and `module-info.java` (module
      declaration, no package declaration). TS-33
      (`02-source-files.adoc:1-35`) covers only ordinary `.java` files.
      Recommend a new subsection at `02-source-files.adoc:35`.

- [ ] `https://google.github.io/styleguide/javaguide.html#s3.5.1` — Module
      directive ordering: `requires`, `exports`, `opens`, `uses`,
      `provides`, each in a single block separated by a blank line. TS-33
      does not address the Java Platform Module System at all. Recommend a
      new subsection at `02-source-files.adoc` or
      `05-programming-constructs.adoc`. (Niche — may be considered
      out-of-scope if modules are deemed beyond this standard's purpose.)

- [ ] `https://google.github.io/styleguide/javaguide.html#s4.8.4` —
      New-style (arrow) switch syntax and switch expressions. TS-33
      (`05-programming-constructs.adoc:226-256`) covers only the old-style
      (`case … :`/`break`) switch and does not mention arrow-style labels,
      switch expressions, or the rule that switch expressions must use
      new-style syntax. Recommend updating `05-programming-constructs.adoc:226`.

- [ ] `https://google.github.io/styleguide/javaguide.html#s4.8.9` — Text
      blocks (`""" … """`): the opening `"""` on a new line, the closing
      `"""` on a new line with the same indentation, each text line indented
      at least as much as the delimiters, and that text-block contents may
      exceed the column limit. TS-33 does not mention text blocks anywhere.
      Recommend a new subsection at `06-types.adoc:8` (after numeric
      literals) or `04-code-style.adoc`.

- [ ] `https://google.github.io/styleguide/javaguide.html#s5.2.9` — The `_`
      syntax for unnamed variables and parameters, allowed wherever it is
      applicable. TS-33 (`03-naming-conventions.adoc:17-19`) restricts
      identifiers to `\w+` but does not mention the unnamed-variable
      pattern. Recommend placing at `03-naming-conventions.adoc:19` or
      `05-programming-constructs.adoc:23`.

- [ ] `https://google.github.io/styleguide/javaguide.html#s4.7` — Optional
      grouping parentheses should be omitted only when author and reviewer
      agree there is no reasonable chance of misinterpretation; it is not
      reasonable to assume readers have the Java operator precedence table
      memorized. TS-33 does not address grouping parentheses. Recommend a
      new subsection at `04-code-style.adoc` (after horizontal whitespace).

- [ ] `https://google.github.io/styleguide/javaguide.html#s6.4` — Do not
      override `Object.finalize`; finalization support is scheduled for
      removal. TS-33 (`05-programming-constructs.adoc:196-224`) discusses
      exception handling but does not mention `finalize`. Recommend placing
      at `05-programming-constructs.adoc:224` or a new subsection.

- [ ] `https://google.github.io/styleguide/javaguide.html#s7.2` — The
      `{@return}` inline tag as an alternative to a `@return` block tag for
      the summary fragment. TS-33 does not mention `{@return}`. Recommend
      placing at `07-comments.adoc:152`.

- [ ] `https://google.github.io/styleguide/javaguide.html#s7.1.3` — Block
      tags must never appear with an empty description. TS-33
      (`07-comments.adoc:156-159`) says block tags are followed by a space
      and a text description but does not explicitly prohibit empty
      descriptions. Recommend placing at `07-comments.adoc:157`.

- [ ] `https://google.github.io/styleguide/javaguide.html#s7.1.2` — A
      blank line (containing only the aligned `*`) should appear before the
      group of block tags in multi-line Javadoc. TS-33
      (`07-comments.adoc:137-139`) mentions blank lines between paragraphs
      but not before block tags. Recommend placing at `07-comments.adoc:148`.

- [ ] `https://google.github.io/styleguide/javaguide.html#s7.3.4` —
      Non-required Javadoc (i.e. Javadoc added beyond the minimum) is not
      strictly required to follow the formatting rules of sections 7.1.1–7.3,
      though it is recommended. TS-33 applies its Javadoc rules uniformly
      with no such relaxation. Recommend placing at `07-comments.adoc:170`.

## Partial

### From Run 1 (`__TODO__/`)

- [ ] `__TODO__/033/comments.adoc:98-121` covers `//` more restrictively
      than `07-comments.adoc:14-19` — specifically, the reference says `//`
      SHOULD be avoided in production code and used only for temporary
      commented-out code and for noting expected return values/outputs,
      whereas the standard permits `//` for "short end-of-line comments"
      generally without that production caveat.

- [ ] `__TODO__/033/comments.adoc:98-121` adds guidance the standard
      omits at `07-comments.adoc:14-19` — specifically, that commented-out
      code SHOULD NOT be committed (version control tracks changes), and
      that `//` is preferred for temporary commented-out code precisely
      because static analysis pipelines can detect and reject it. The
      standard mentions `//` for "commenting-out code" without these
      caveats.

- [ ] `__TODO__/033/comments.adoc:122-162` covers Javadoc scope more
      thoroughly than `07-comments.adoc:100-108` — specifically, the
      reference requires Javadoc for all classes (not just `public` ones)
      and all public fields, and lists explicit exceptions (trivial
      getters/setters, trivial no-arg constructors that are not overridden,
      and methods that override without adding behavior). The standard
      says only that Javadoc SHOULD cover `public` classes and every
      `public`/`protected` member, and MAY be skipped for overriding
      methods.

- [ ] `__TODO__/033/comments.adoc:122-162` covers Javadoc content
      focus more thoroughly than `07-comments.adoc:97-99` — specifically,
      the reference states that long descriptions and usage examples
      SHOULD generally be excluded from Javadoc and placed in other
      documents (READMEs) referenced from the inline documentation. The
      standard says only that Javadoc MUST NOT document implementation
      details.

- [ ] `__TODO__/033/comments.adoc:228-271` covers block tags more
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

### From Run 2 (issue #66)

- [ ] `https://google.github.io/styleguide/javaguide.html#s7.2` — Google
      defines the Javadoc summary fragment as a noun phrase or verb phrase
      that is _not_ a complete sentence, but capitalized and punctuated _as
      if_ it were one. TS-33 (`07-comments.adoc:141-142`) states the summary
      "MUST be written as a complete sentence" — this directly contradicts
      Google's guidance. Recommend reconciling at `07-comments.adoc:141`;
      the standard's wording should be corrected to match its own primary
      source.

- [ ] `https://google.github.io/styleguide/javaguide.html#s7.3` and
      `#s7.3.1` — At minimum Javadoc is present for every _visible_ class
      and member (visibility defined for top-level classes, members, and
      record components), and is optional for "simple, obvious" members
      (such as `getFoo()`) only if there is truly nothing else worthwhile
      to say. TS-33 (`07-comments.adoc:100-103`) scopes Javadoc to
      `public` classes and `public`/`protected` members with an override
      exception, but does not frame the rule around visibility generally,
      does not mention record components, and does not articulate the
      "simple, obvious" exception. Reinforces the Run 1 Javadoc-scope gap.

- [ ] `https://source.android.com/docs/setup/contribute/code-style#use-javadoc-standard-comments`
      — Every file should have a copyright statement at the top. TS-33
      (`02-source-files.adoc:21-24`) lists license/copyright as the first
      file section but makes it conditional ("if required"). The Android
      guide treats it as always-present. Partial — a project-licensing
      policy question the standard leaves open.

- [ ] `https://google.github.io/styleguide/javaguide.html#s4.6.3` —
      Horizontal alignment (adding variable spaces so tokens appear
      directly below previous tokens) is permitted but never required and
      does not need to be maintained; reformatting otherwise-unaffected
      lines just to realign is discouraged. TS-33
      (`04-code-style.adoc:299-306`) allows extra spaces before end-of-line
      comments for vertical alignment but does not address horizontal
      alignment maintenance or the discouragement of realignment-only
      diffs. Recommend placing at `04-code-style.adoc:300`.

- [ ] `https://google.github.io/styleguide/javaguide.html#s5.3` — Camel
      case conversion proceeds by a specific algorithm (convert to plain
      ASCII, remove apostrophes, split on spaces/punctuation, lowercase
      all, then uppercase first character of each word or each word except
      the first). TS-33 (`03-naming-conventions.adoc`) mandates camel-case
      forms but does not define the conversion algorithm. Recommend
      placing at `03-naming-conventions.adoc:19` (identifiers section).

## Out-of-scope

### From Run 1 (`__TODO__/`)

- [ ] `__TODO__/033/nullability.adoc:111-170` covers nullability in
      Kotlin, but this plausibly sits outside TS-33's stated purpose
      (Java coding guidelines) because it is a different language.
      Flagged for the user to confirm or overrule — a brief comparative
      note could be considered if the standard ever expands to
      JVM-ecosystem guidance.

### From Run 2 (issue #66)

- [ ] `https://www.infoworld.com/article/2165633/design-for-thread-safety.html`
      (entire article) — design-level thread-safety guidance (synchronizing
      critical sections, immutable objects, thread-safe wrappers, when to
      make classes thread-safe, performance trade-offs). TS-33's
      `AGENTS.md` explicitly defers concurrency to TS-7 (Code design), and
      TS-33 itself is a formatting/naming/style standard. The only
      thread-safety-adjacent point kept in-scope is the Javadoc
      _documentation_ obligation (see Missing, Oracle javadoc-tool
      Introduction). Flagged for the user to confirm.

- [ ] `https://www.oracle.com/java/technologies/javase/codeconventions-introduction.html`
      (entire page) — rationale for having code conventions (80% of
      lifetime cost is maintenance; software is rarely maintained by its
      original author) and attribution/history of the Oracle Code
      Conventions document. This is contextual material, not a coding
      rule, so it does not represent a coverage gap. Additionally, the
      page states the document is archived and no longer maintained (last
      revised 1999); the user may wish to reconsider citing it as a
      reference from `09-references.adoc`.

## Unresolved

- [ ] `__TODO__/033/SDCP-1065287937-290722-0934.pdf`,
      `__TODO__/033/SDCP-1065287946-290722-0933.pdf`,
      `__TODO__/033/SDCP-2-Java-v1.0.0-290722-0931.pdf`, and
      `__TODO__/033/SDCP-BuildTools-v1.0.0-290722-0959.pdf` are binary
      PDFs and were not parsed. Not included in the comparison above.

- [ ] `https://www.quora.com/What-is-the-difference-between-string-args-and-string-args-in-Java`
      — fetch returned HTTP 403 (Cloudflare bot challenge). The page
      content could not be retrieved without authenticated access. No
      claims extracted. Not included in the comparison above.

- [ ] Scope call: the Javadoc-content rules derived from the Oracle
  javadoc-tool article (documenting thread-safety, spec completeness,
  implementation-specific behavior) overlap with TS-7 (Code design) and
  TS-26 (Technical Writing). They are classified here as missing because
  they concern what Javadoc _should contain_, which is TS-33's comments
  section — but the user may prefer to defer some to TS-7 or TS-26.

- [ ] Scope call: the module-directives gap
  (`https://google.github.io/styleguide/javaguide.html#s3.5.1`) is marked
  missing but is niche. The user may consider the Java Platform Module
  System out-of-scope for this standard.