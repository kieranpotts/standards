# TS-33 gap analysis

Gaps found comparing TS-33: Java against the following reference resources:

- https://google.github.io/styleguide/javaguide.html (Google Java Style
  Guide)
- https://openjdk.org/projects/amber/guides/lvti-style-guide (OpenJDK, Local
  Variable Type Inference: Style Guidelines)
- https://www.oracle.com/java/technologies/javase/codeconventions-contents.html
  (Oracle, Code Conventions for the Java Programming Language, all 11
  chapter pages; archived, last revised 1999)
- https://source.android.com/docs/setup/contribute/code-style (AOSP, Java
  code style for contributors)
- https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md
  (Twitter Commons, Java Style Guide)

**Assessment.** TS-33 already covers the Google guide's formatting and naming
rules closely, so most of Google's content is covered, and the rest turns up
as partial gaps in line-wrapping, whitespace, switch, and annotation detail.
The clearest missing topics come from the other four sources: local variable
type inference (`var`), which TS-33 uses in its examples without governing;
generics and collection typing; resource cleanup; and several Java-specific
exception and API practices. Much of the AOSP and Twitter material is general
code design, logging, or testing advice that belongs to TS-7, TS-57, or TS-13
instead, and is listed as out-of-scope. Several reference rules conflict with
deliberate TS-33 choices, and those are also listed as out-of-scope rather
than as gaps.

**Status:** 24 of 35 actionable gaps closed (all 18 missing, 6 partial); 11
partial and 9 out-of-scope remain open. First run: 2026-09-19. Last worked:
2026-09-19 (third batch).

## Missing

- [x] https://openjdk.org/projects/amber/guides/lvti-style-guide#P1 to
      #P4 and #G1 to #G4 (the reader-first principles for `var`: choose
      names that carry the information the type no longer shows, minimize
      the scope of `var` variables, use `var` where the initializer makes the
      type obvious, and use `var` to break long chains into intermediate
      variables) are not addressed anywhere in the standard, although its
      own examples use `var` (06-types.adoc:84, 06-types.adoc:111). Recommend
      a new "Local variable type inference" subsection in
      05-programming-constructs.adoc, after "Variable declarations"
      (05-programming-constructs.adoc:19).

      **Resolved.** Closed by `05-programming-constructs.adoc`, new "Local
      variable type inference" section after "Variable declarations". States
      that `var` MAY be used only where the reader loses nothing by it, then
      gives four numbered rules: name the variable for what the type no longer
      shows; keep `var` variables' scope small (cross-referencing "Variable
      declarations"); prefer `var` where the initializer states the type, and
      avoid it where a method's return type is not evident from its name; and
      use `var` locals to break up long chained expressions, with an example.
      Source added to `99-references.adoc`.

- [x] https://openjdk.org/projects/amber/guides/lvti-style-guide#G6 (`var`
      combined with diamond or a generic method with no informative
      arguments infers `Object`, eg. `var list = List.of()` is
      `List<Object>`) is not addressed anywhere in the standard. Recommend
      placing in the same new "Local variable type inference" subsection.

      **Resolved.** Closed by the same "Local variable type inference" section
      in `05-programming-constructs.adoc`. Rules that `var` MUST NOT be combined
      with the diamond operator or a generic method unless the arguments supply
      the type argument, and shows the `PriorityQueue<>()` and `List.of()` cases
      that infer `Object` beside the corrected forms.

- [x] https://openjdk.org/projects/amber/guides/lvti-style-guide#G7 (`var`
      with integer literals always infers `int`, and with a `float`
      initializer can silently change a former `double`) is not addressed
      anywhere in the standard. Recommend placing in the same new "Local
      variable type inference" subsection.

      **Resolved.** Closed by the same "Local variable type inference" section
      in `05-programming-constructs.adoc`. Rules that `var` SHOULD NOT be used
      with an integer literal where the intended type is not `int`, requires a
      `long` to be declared explicitly or with an `L`-suffixed literal
      (cross-referencing "Numeric literals", which gained an explicit anchor),
      explains how a `float` initializer that an explicit `double` would widen
      instead narrows under `var`, and lists the literals that are safe with
      `var`.

- [x] https://openjdk.org/projects/amber/guides/lvti-style-guide#G5 (`var`
      infers the concrete type, so programming to the interface still
      matters for fields, parameters, and return types) and
      https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md#use-general-types
      (declare fields and method signatures with the most general type,
      eg. `Iterable<User>`, not `ArrayList<User>`) are not addressed
      anywhere in the standard. Recommend a new "Generics and collections"
      section in 06-types.adoc.

      **Resolved.** Closed by `06-types.adoc`, new "Generics and collections"
      section after "Arrays". Its opening rule says fields, parameters, and
      return types SHOULD use the most general type that supports their use,
      with an `ArrayList<User>` versus `List<User>` example, and explains
      choosing between `Iterable`, `Collection`, and `List` by the promise
      callers need. A following paragraph carries G5's concession that local
      variables, including `var` locals, MAY use the concrete type. The `var`
      section in `05-programming-constructs.adoc` points here for non-local
      types. Twitter source added to `99-references.adoc`.

- [x] https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md#always-use-type-parameters
      (no raw types; use a wildcard or a wide type where the type argument is
      unknown) is not addressed anywhere in the standard. Recommend placing
      in the same new "Generics and collections" section in 06-types.adoc.

      **Resolved.** Closed by the same "Generics and collections" section in
      `06-types.adoc`. Rules that a parameterized type MUST NOT be used as a raw
      type, explains that raw types disable compile-time checks and defer the
      failure to a `ClassCastException`, and prescribes `List<?>` or a broad
      type argument where the element type is unknown, with an example of each.

- [x] https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md#favor-immutability
      (don't return mutable internal collections; return an immutable copy
      or an accessor instead) is not addressed anywhere in the standard.
      TS-7 covers immutability in general, but not the Java collection
      idioms. Recommend placing in the same new "Generics and collections"
      section in 06-types.adoc.

      **Resolved.** Closed by the same "Generics and collections" section in
      `06-types.adoc`. Rules that a method MUST NOT return a mutable collection
      that is part of its object's internal state, with a `Team.getMembers()`
      example returning `List.copyOf(members)`. Distinguishes `List.copyOf` and
      its siblings (unmodifiable copies, which reject `null`) from
      `Collections.unmodifiableList` (a live view), and adds the reverse case: a
      stored collection argument SHOULD be copied. Links TS-7 (Code Design) for
      immutability in general, using the JDK idioms rather than Twitter's Guava
      `ImmutableMap.copyOf`.

- [x] https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md#clean-up-with-finally
      (release resources deterministically, even without checked
      exceptions), https://source.android.com/docs/setup/contribute/code-style#dont-use-finalizers
      (give a resource an explicit `close()` method, and document when it
      must be called), and the try-with-resources example at
      https://openjdk.org/projects/amber/guides/lvti-style-guide#examples
      (declare each wrapped I/O object as its own resource so it is closed if
      a later wrapper fails) are not addressed anywhere in the standard.
      Recommend a new "Resource management" subsection in
      05-programming-constructs.adoc, beside the finalizer rule at
      05-programming-constructs.adoc:50. None of the references names
      try-with-resources as a rule, so the wording will need a primary
      source such as the JLS.

      **Resolved.** Closed by `05-programming-constructs.adoc`, new "Resource
      management" section after "Classes and interfaces", which the finalizer
      rule now points to. A resource-holding class SHOULD implement
      `AutoCloseable` and document who closes it; users MUST close
      deterministically, preferably with try-with-resources, whose JLS 14.20.3
      semantics (reverse-order close, null resources skipped, `addSuppressed`)
      are summarized. Each wrapped I/O layer SHOULD be its own resource, with
      the socket-reader example from the LVTI guide. Adds JDK 9 effectively
      final resources, and requires a `finally` block straight after acquiring a
      non-`AutoCloseable` resource such as a `Lock`, per Twitter. JLS (Java SE
      21) added to `99-references.adoc`.

- [x] https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md#when-interrupted-reset-thread-interrupted-state
      (a caught `InterruptedException` MUST restore the interrupt flag with
      `Thread.currentThread().interrupt()`) is not addressed anywhere in the
      standard. Recommend placing in the "Exceptions" section,
      05-programming-constructs.adoc:157.

      **Resolved.** Closed by a new paragraph and example at the end of the
      "Exceptions" section in `05-programming-constructs.adoc`. Rules that a
      caught `InterruptedException` MUST NOT be swallowed, explains that
      catching it clears the interrupted status that code higher up the stack
      (eg. a shutting-down thread pool) relies on, and requires either
      propagating it or calling `Thread.currentThread().interrupt()`, shown in a
      `queue.take()` example.

- [x] https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md#manage-threads-properly
      (manage the lifecycle of spawned threads, understand daemon versus
      non-daemon threads, and shut down an `ExecutorService` correctly) is
      not addressed anywhere in the standard. TS-7's "Concurrency" chapter
      covers the principles but not the Java APIs. Recommend a new
      "Concurrency" section in 05-programming-constructs.adoc.

      **Resolved.** Closed by `05-programming-constructs.adoc`, new
      "Concurrency" section after "Resource management", which links TS-7 (Code
      Design) for concurrency principles and covers only the Java APIs.
      Application code SHOULD use an `ExecutorService` rather than starting
      threads directly. The code that starts a thread or executor MUST stop it:
      the section explains how non-daemon threads keep the JVM alive, and why
      daemon threads are no fix. A block-scoped executor SHOULD be a
      try-with-resources resource (JDK 19+). A long-lived executor MUST be shut
      down in the two phases the `ExecutorService` Javadoc describes, with an
      example. Long tasks SHOULD respond to interruption. The `ExecutorService`
      Javadoc (Java SE 21) and the `Thread` Javadoc's daemon rules were read;
      the former was added to `99-references.adoc`.

- [x] https://source.android.com/docs/setup/contribute/code-style#use-standard-java-annotations
      (`@SuppressWarnings` only where a warning is impossible to eliminate,
      with a comment explaining why, and scoped as narrowly as possible) is
      not addressed anywhere in the standard. Recommend a new
      `@SuppressWarnings` subsection in the "Annotations" section,
      05-programming-constructs.adoc:96, beside `@Override`.

      **Resolved.** Closed by a new "@SuppressWarnings" subsection after
      "@Override" in the "Annotations" section of
      `05-programming-constructs.adoc`. Rules that it SHOULD be used only where
      a warning cannot be eliminated and that fixable warnings MUST be fixed,
      requires the narrowest scope (a local declaration or method, never a
      class, extracting code where needed), and requires a comment explaining
      why, with an unchecked-cast example. AOSP asks for a TODO-prefixed
      comment; the standard asks for an explanatory comment, leaving TODO format
      to TS-7 (Code Design).

- [x] https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md#avoid-assert
      (don't rely on `assert`, which can be disabled at run time) and
      https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md#preconditions
      (check arguments with precondition checks, and null-check the object
      parameters of public constructors and methods unless `null` is
      explicitly allowed) are not addressed anywhere in the standard.
      Recommend a new "Preconditions and assertions" section in
      05-programming-constructs.adoc. Twitter's examples use Guava's
      `checkNotNull`; the JDK equivalent is `Objects.requireNonNull`.

      **Resolved.** Closed by `05-programming-constructs.adoc`, new
      "Preconditions and assertions" section after "Exceptions". Public
      constructors and methods SHOULD check arguments on entry. Object
      parameters MUST be null-checked unless the Javadoc allows `null`, using
      `Objects.requireNonNull`, with `IllegalArgumentException` and
      `IllegalStateException` for other failures, shown in a `readLater` example
      adapted from Twitter's. Guava `Preconditions` MAY be used, but not mixed
      with the JDK style. `assert` SHOULD NOT be used and MUST NOT check
      arguments, because it is disabled unless the JVM runs with `-ea`.

- [x] https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md#visiblefortesting
      (members widened for test access are kept package-private and marked
      as such) is not addressed anywhere in the standard. Recommend placing
      in the "Modifiers" section, 05-programming-constructs.adoc:79, noting
      that `@VisibleForTesting` comes from Guava rather than the JDK.

      **Resolved.** Closed by a new paragraph and example at the end of the
      "Modifiers" section of `05-programming-constructs.adoc`. A member widened
      for tests SHOULD go no further than package-private and SHOULD be marked,
      with Guava's `@VisibleForTesting` named as the usual marker, a comment as
      the fallback without Guava, and a note that many such members suggest
      testing through the public interface instead. Uses Twitter's
      `ConfigReader` constant example.

- [x] https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md#stringbuilder-over-stringbuffer,
      #scheduledexecutorservice-over-timer, and #list-over-vector (prefer the
      modern API over the legacy synchronized or single-threaded one), plus
      https://source.android.com/docs/setup/contribute/code-style#java-library-rules
      (never use deprecated libraries in new code) are not addressed anywhere
      in the standard. Recommend a new "Legacy APIs" section in
      08-java-api-specifications.adoc.

      **Resolved.** Closed by `08-java-api-specifications.adoc`, new "Legacy
      APIs" section after "Jakarta Persistence (JPA)". New code MUST NOT use
      deprecated APIs, and existing code MAY keep them for consistency, per
      AOSP. A table maps superseded classes to replacements with reasons:
      `StringBuffer` to `StringBuilder`; `Vector`, `Stack`, and `Hashtable` to
      `ArrayList`, `ArrayDeque`, and `HashMap`, or a concurrent collection; and
      `Timer` to `ScheduledExecutorService`, using Twitter's failure-mode
      reasons. Beyond the sources, it adds `Date`, `Calendar`, and
      `SimpleDateFormat` to `java.time`, linking TS-47 (Dates and Times). The
      "Concurrency" section points here for `Timer`.

- [x] https://www.oracle.com/java/technologies/javase/codeconventions-declarations.html#16817
      (6.3: avoid local declarations that hide declarations at a higher
      level) is not addressed anywhere in the standard. Recommend placing in
      "Variable declarations", 05-programming-constructs.adoc:19.

      **Resolved.** Closed by a new paragraph and example at the end of
      "Variable declarations" in `05-programming-constructs.adoc`. Rules that a
      local variable or parameter SHOULD NOT hide a field or other higher-level
      declaration, explains that the compiler rejects a local hiding a local but
      accepts one hiding a field, and shows Oracle's `count` example. Allows the
      `this.name = name` constructor and setter idiom as the one exception. The
      Oracle Code Conventions were already in `99-references.adoc`; the page
      needed a direct fetch, as WebFetch returned 403.

- [x] https://google.github.io/styleguide/javaguide.html#s3.3.1.1-module-imports
      (module imports, `import module java.base;`, are not used) and
      https://google.github.io/styleguide/javaguide.html#s3.2-package-declaration
      (compact source files are not used, and every file except
      `module-info.java` has a package declaration) are not addressed
      anywhere in the standard. Recommend placing the module-import rule in
      "Import statements", 05-programming-constructs.adoc:4, and the
      package-declaration and compact-source-file rules in the file layout
      at 02-source-files.adoc:7.

      **Resolved.** Module imports: "Import statements" in
      `05-programming-constructs.adoc` now says module imports (JDK 25+) MUST
      NOT be used, because they share the wildcard import's drawbacks at a
      larger scale. Package declarations: a new paragraph after the file-layout
      list in `02-source-files.adoc` requires a `package` statement in every
      file except `module-info.java` and rules out compact source files (JDK
      25+). It explains they are meant for single-file programs, and that
      classes in the unnamed package cannot be imported. The statement MUST NOT
      be wrapped and MAY exceed the column limits, per Google 3.2. JEPs 511 and
      512 were read for the feature details and added to `99-references.adoc`.

- [x] https://google.github.io/styleguide/javaguide.html#s5.2.1-package-names
      (module names follow the same rules as package names) and
      https://google.github.io/styleguide/javaguide.html#s4.8.7-modifiers
      (`requires` directive modifiers are ordered `transitive static`) are
      not addressed anywhere in the standard. Recommend placing the naming
      rule in "Package names", 03-naming-conventions.adoc:83, and the
      modifier order with the `module-info.java` rules at
      02-source-files.adoc:30.

      **Resolved.** "Package names" in `03-naming-conventions.adoc` gained an
      explicit anchor and a sentence saying module names follow the same rules.
      The `module-info.java` paragraph in `02-source-files.adoc`, under "Special
      source files", now requires `requires` modifiers in the order `transitive
      static` and links to "Package names". Its example now shows `requires
      transitive` and `requires static` directives.

- [x] https://www.oracle.com/java/technologies/javase/codeconventions-fileorganization.html
      (3: files longer than 2000 lines are cumbersome and should be avoided)
      is not addressed anywhere in the standard. Recommend placing in
      "Source files", 02-source-files.adoc:3.

      **Resolved.** Closed by a new paragraph in the opening of "Source files"
      in `02-source-files.adoc`. A source file SHOULD NOT exceed about 2,000
      lines, because such a file usually means its class has more than one
      responsibility, so the class should be split rather than the file. The
      Oracle page was fetched directly and confirms the figure.

- [x] https://www.oracle.com/java/technologies/javase/codeconventions-statements.html#438
      (7.3: a `return` value is not parenthesized unless the parentheses
      make it clearer) is not addressed anywhere in the standard. Recommend
      placing in "Grouping parentheses", 04-code-style.adoc:251.

      **Resolved.** Closed by a new paragraph in "Grouping parentheses" in
      `04-code-style.adoc`. A `return` value SHOULD NOT be wrapped in
      parentheses. Parentheses MAY be kept around part of the value where they
      help, shown with the condition of a conditional expression, after Oracle
      7.3's example.

## Partial

- [ ] https://google.github.io/styleguide/javaguide.html#s4.5.1-line-wrapping-where-to-break
      and #s4.5.2-line-wrapping-indent cover this more thoroughly than
      04-code-style.adoc:24 — specifically, breaking before `&` in type
      bounds and `|` in multi-catch, treating the enhanced-`for` colon like
      an assignment, never breaking next to a switch-rule arrow, keeping a
      record name attached to its `(`, and giving continuation lines the
      same indentation only when they begin with parallel elements.
      https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md#chained-method-calls
      and #indent-style add one call per line in a wrapped method chain, and
      one parameter per line in a wrapped method declaration.
      https://www.oracle.com/java/technologies/javase/codeconventions-indentation.html
      (4.2) adds layouts for wrapped ternary expressions.

- [ ] https://google.github.io/styleguide/javaguide.html#s4.6.2-horizontal-whitespace
      covers this more thoroughly than 04-code-style.adoc:207 —
      specifically, it states that a single space appears _only_ in the
      listed places, that `::` and the dot separator take no spaces, and
      that a space separates a type annotation from a following `[]` or
      `...`.
      https://www.oracle.com/java/technologies/javase/codeconventions-whitespace.html#682
      (8.2) adds no space between a unary operator and its operand, and no
      space between a method name and its `(`.

- [ ] https://google.github.io/styleguide/javaguide.html#s4.8.4.1-switch-indentation
      and #s4.8.4.3-switch-default cover this more thoroughly than
      05-programming-constructs.adoc:208 — specifically, how arrow-style
      switch rules are indented and when one may sit on a single line, and
      that _every_ switch, not only a colon-style switch statement
      (05-programming-constructs.adoc:206), is exhaustive.

- [x] https://google.github.io/styleguide/javaguide.html#s4.8.5.3-method-annotation-style
      and #s4.8.5.2-class-annotation-style cover this more thoroughly than
      05-programming-constructs.adoc:96 — specifically, the exception that
      a single parameterless annotation may share the signature line (eg.
      `@Override public int hashCode()`), that package and module
      annotations follow the class rule, and that the line breaks between
      annotations are not line-wrapping.
      https://source.android.com/docs/setup/contribute/code-style#use-standard-java-annotations
      adds that annotations precede all other modifiers.

      **Resolved.** Closed by additions to the "Annotations" section of
      `05-programming-constructs.adoc`. A new opening rule says declaration
      annotations MUST precede all other modifiers (per AOSP), with type-use
      annotations excepted. The class rule now extends to `package-info.java`
      and `module-info.java`, and says the line breaks between annotations are
      not line-wrapping. After the method example, a single parameterless
      annotation MAY share the signature line, shown with `@Override public int
      hashCode()`.

- [x] https://google.github.io/styleguide/javaguide.html#s6.1-override-annotation
      covers this more thoroughly than 05-programming-constructs.adoc:140 —
      specifically, that `@Override` also applies to an explicitly declared
      record accessor, and to an interface method that respecifies a
      superinterface method.

      **Resolved.** Closed by rewriting the rule in the "@Override" subsection
      of `05-programming-constructs.adoc`. `@Override` MUST now be used wherever
      it is legal, listing the four cases from Google 6.1, including an
      interface method respecifying a superinterface method and an explicit
      record accessor, with a `record Team` example whose accessor returns a
      defensive copy. The `@Deprecated` exception is kept.

- [x] https://google.github.io/styleguide/javaguide.html#s6.2-caught-exceptions
      and https://source.android.com/docs/setup/contribute/code-style#dont-ignore-exceptions
      cover this more thoroughly than 05-programming-constructs.adoc:157 —
      specifically, what to do instead of swallowing an exception, in order
      of preference: propagate it, wrap it in an exception at the caller's
      level of abstraction (passing the original as the cause), substitute a
      documented default, or rethrow it unchecked. Google adds rethrowing an
      "impossible" exception as `AssertionError`.
      https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md#throw-appropriate-exception-types
      adds never declaring `throws Exception`, and hiding
      implementation-specific exception types behind a custom one.

      **Resolved.** Closed by new content in the "Exceptions" section of
      `05-programming-constructs.adoc`, after the existing empty-`catch`
      example. Frames the empty `catch` block as the last resort, then lists the
      alternatives in AOSP's order of preference: propagate, wrap at the
      caller's level of abstraction passing the cause, substitute a documented
      default, or rethrow unchecked, with a `ConfigurationException` example.
      Adds Google's `AssertionError` rule for a declared checked exception the
      arguments rule out, using `new String(bytes, "UTF-8")`. Adds Twitter's
      rules: a method MUST NOT declare `throws Exception`, and SHOULD NOT expose
      implementation-specific types such as `SQLException`. AOSP source added to
      `99-references.adoc`.

- [x] https://source.android.com/docs/setup/contribute/code-style#dont-catch-generic-exception
      covers this more thoroughly than 05-programming-constructs.adoc:183 —
      specifically, it also rules out `Throwable`, gives multi-catch as the
      alternative, and allows the one exception of top-level code and tests
      that must catch everything, with a comment explaining why.

      **Resolved.** Closed by additions to the end of the "Exceptions" section
      of `05-programming-constructs.adoc`. The broad-catch rule now names
      `Throwable`. New paragraphs prescribe multi-catch for exceptions sharing
      handling, with a `ClassNotFoundException | NoSuchMethodException` example,
      and smaller `try` blocks or propagation where handling differs. Top-level
      code (a batch loop, a request dispatcher, a test harness) MAY catch
      `Exception` or `Throwable`, but MUST say why in a comment and MUST record
      the failure.

- [x] https://google.github.io/styleguide/javaguide.html#s3.3.3-import-ordering-and-spacing
      covers this more thoroughly than 05-programming-constructs.adoc:13 —
      specifically, imported names are in ASCII sort order, which differs
      from sorting the import lines because `.` sorts before `;`.

      **Resolved.** "Import statements" in `05-programming-constructs.adoc` now
      sorts imports in ASCII order of the imported names, not alphabetically. A
      worked `com.example.Foo` / `com.example.Foo.Bar` example shows why that
      differs from sorting the lines, since `.` sorts before `;`.

- [x] https://google.github.io/styleguide/javaguide.html#s3.4.2-ordering-class-contents
      covers this more thoroughly than 05-programming-constructs.adoc:29 —
      specifically, new methods are not habitually appended to the end of a
      class, since the order they were added in is not a logical order.

      **Resolved.** The ordering paragraph in "Classes and interfaces" in
      `05-programming-constructs.adoc` now says a class's maintainer SHOULD be
      able to explain its order. It adds that new methods SHOULD NOT be
      habitually appended to the end, since that order is chronological rather
      than logical, and should sit beside related members.

- [ ] https://google.github.io/styleguide/javaguide.html#s5.3-camel-case
      covers this more thoroughly than 03-naming-conventions.adoc:16 —
      specifically, splitting words that already look camel-cased in common
      usage ("AdWords" becomes "ad words"), underscores between adjacent
      numbers (eg. `guava33_4_6`), and both forms being correct for
      ambiguously hyphenated words.

- [ ] https://www.oracle.com/java/technologies/javase/codeconventions-namingconventions.html#15429
      and https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md#extremely-short-variable-names-should-be-reserved-for-instances-like-loop-indices
      cover this more thoroughly than 03-naming-conventions.adoc:157 —
      specifically, one-character names are avoided for all variables, not
      only public-method parameters, except throwaway variables such as
      loop indices.

- [ ] https://google.github.io/styleguide/javaguide.html#s4.8.9-text-blocks
      covers this differently from 06-types.adoc:22 — Google puts the
      closing `"""` at the same indentation as the _opening_ line, allows
      the opening line to sit at the left margin, and allows code after the
      closing delimiter. TS-33 aligns the closing `"""` with the content.
      Needs a decision on which rule to keep.

- [ ] https://google.github.io/styleguide/javaguide.html#s7.1.3-javadoc-block-tags
      conflicts with 07b-javadoc.adoc:166 — for Markdown Javadoc, Google
      indents block-tag continuation lines by exactly _two_ spaces, because
      four can start a code block. TS-33 says four spaces for both
      notations.

- [ ] https://google.github.io/styleguide/javaguide.html#s7.1.2-javadoc-paragraphs
      covers this more thoroughly than 07b-javadoc.adoc:118 — specifically,
      block-level HTML elements such as `<ul>` and `<table>` are not
      preceded by `<p>` in classic Javadoc.

- [ ] https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md#nullable
      covers this more thoroughly than 06-types.adoc:123 — specifically,
      treating non-null as the default and annotating every nullable
      variable, parameter, and return value, even private ones.

- [ ] https://google.github.io/styleguide/javaguide.html#s4.4-column-limit
      covers this more thoroughly than 04-code-style.adoc:21 —
      specifically, very long identifiers are an allowed exception, and the
      limit counts Unicode code points, not display width.

- [ ] https://google.github.io/styleguide/javaguide.html#s4.6.1-vertical-whitespace
      covers this more thoroughly than 04-code-style.adoc:197 —
      specifically, a blank line before the first member or after the last
      is neither encouraged nor discouraged. TS-33 is silent on it.

## Out-of-scope

- [ ] https://www.oracle.com/java/technologies/javase/codeconventions-programmingpractices.html#1255
      (magic numbers) and #333 (return a boolean expression directly), and
      https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md#superfluous-temporary-variables,
      #unneeded-assignment, #extract-constants-whenever-it-makes-sense,
      #stay-out-of-texas, #obey-the-law-of-demeter-lod,
      #dont-repeat-yourself-dry, and
      #premature-optimization-is-the-root-of-all-evil, cover these, but they
      are general code design, which TS-7 owns (eg.
      partials/007/05-expressiveness.adoc:12 on magic numbers). Flagged for
      the user to confirm or overrule.

- [ ] https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md#include-units-in-variable-names
      and #dont-embed-metadata-in-variable-names (put units in names, and
      don't put the type or scope in names) cover this, but naming advice
      that applies to any language plausibly belongs in TS-7's "Naming
      things". Flagged for the user to confirm or overrule.

- [ ] https://google.github.io/styleguide/javaguide.html#s4.8.6.2-todo-comments,
      https://source.android.com/docs/setup/contribute/code-style#use-todo-comments,
      https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md#leave-no-todo-unassigned,
      and https://www.oracle.com/java/technologies/javase/codeconventions-programmingpractices.html#395
      (`XXX`/`FIXME`) cover TODO comment format, but TS-7 already has a "TODO
      comments" section (partials/007/07-comments.adoc:175). The references
      disagree: Google avoids naming a person, and Twitter requires an owner.
      Flagged for the user to confirm or overrule.

- [ ] https://source.android.com/docs/setup/contribute/code-style#log-sparingly
      and #log-sparingly-notes cover logging levels, rate-limiting, and
      avoiding private data in logs, but that belongs to TS-57: Logging,
      Monitoring, Observability. One Java-specific point, never using
      `System.out.println()` in production code, may still be worth a line in
      TS-33. Flagged for the user to confirm or overrule.

- [ ] https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md#writing-testable-code,
      #fakes-and-mocks, #let-your-callers-construct-support-objects,
      #testing-multithreaded-code, #the-hidden-stress-test, #threadsleep,
      and #avoid-randomness-in-tests cover test design, which belongs to
      TS-13: Functional Testing. #time-dependence (inject a clock rather than
      calling `System.currentTimeMillis()`) plausibly belongs to TS-47: Dates
      and Times. Flagged for the user to confirm or overrule.

- [ ] https://source.android.com/docs/setup/contribute/code-style#be-consistent
      (match the style of surrounding code) and #write-short-methods (about
      40 lines) cover these, but TS-7 owns consistency and function length.
      Flagged for the user to confirm or overrule.

- [ ] https://www.oracle.com/java/technologies/javase/codeconventions-fileorganization.html#3441
      (a beginning comment with version and date),
      https://www.oracle.com/java/technologies/javase/codeconventions-filenames.html#253
      (`GNUmakefile`, `README`), and
      https://source.android.com/docs/setup/contribute/code-style#use-javadoc-standard-comments
      (the AOSP copyright template) are project-specific or superseded by
      version control. Flagged for the user to confirm or overrule.

- [ ] Several reference rules conflict with positions TS-33 takes
      deliberately, so they are not gaps: Oracle's four-space indentation,
      declarations at the start of blocks, and two blank lines between
      sections
      (https://www.oracle.com/java/technologies/javase/codeconventions-indentation.html,
      codeconventions-declarations.html#16817,
      codeconventions-whitespace.html#487); AOSP's `m`/`s` field prefixes,
      eight-space continuation, braceless one-line `if`, and Android-first
      import grouping
      (https://source.android.com/docs/setup/contribute/code-style#follow-field-naming-conventions,
      #use-spaces-for-indentation, #use-standard-brace-style,
      #order-import-statements); Google's 100-column limit and ban on `{}` in
      multi-block statements
      (https://google.github.io/styleguide/javaguide.html#s4.4-column-limit,
      #s4.1.3-braces-empty-blocks). Flagged for the user to confirm or
      overrule.

- [ ] https://google.github.io/styleguide/javaguide.html#s5.2.2-class-names
      says there are "no specific rules or even well-established conventions
      for naming annotation types", while 03-naming-conventions.adoc:213 now
      states that UpperCamelCase is the established convention. Read in
      context, Google's remark concerns word choice rather than case, since
      its terminology treats annotation types as classes, which are
      UpperCamelCase. Not a gap, but the wording at
      03-naming-conventions.adoc:213 could be checked. Flagged for the user
      to confirm or overrule.

## Unresolved

None. All five resources were retrieved and read in full.
