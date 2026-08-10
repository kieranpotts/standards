# TS-33: Java

This is a compact version of technical standard TS-33 for AI agents.

Use this when writing or reviewing Java code — source file organization, naming
conventions, code style (indentation, braces, whitespace), programming
constructs (imports, variables, classes, enums, modifiers, annotations,
exceptions, switch statements), types (numeric literals, arrays), comments and
Javadoc, and JPA usage. Based on
[Google's Java Style Guide](https://google.github.io/styleguide/javaguide.html).

For general code design principles (abstraction, decomposition, comments,
error handling, OOP, concurrency) see
[TS-7: Code Design](../007/AGENTS.md). For technical writing style see
[TS-26: Technical Writing Style Guide](../026/AGENTS.md).

## Rules

### Source files

- **Each source file SHOULD contain exactly one class-like construct; the
  top-level public class MUST be first.**

  In special circumstances, a file MAY have one top-level public class plus
  additional tightly-coupled class-like constructs shared with no other classes.
  File names MUST match exactly (including case) the name of the main class-like
  construct. Files use the `.java` extension; bytecode files use `.class`.

- **File contents MUST be laid out in this order: license/copyright → package
  statement → internal imports (alphabetical) → third-party imports
  (alphabetical) → main top-level class → other class-like constructs.**

  Each section separated by a single blank line. Class-like constructs,
  block-like constructs, and members MUST also be separated by a single blank
  line. Javadocs MUST be preceded by a single blank line, except the first
  file-level Javadoc, which MAY start on line 1.

- **Source files MUST be encoded using UTF-8 with Unix-style line endings (LF).**

  MUST NOT use Windows-style (CRLF). Whitespace is limited to the line
  termination sequence and the horizontal space character. Tab characters MUST
  NOT be used for indentation. Other whitespace characters MAY appear only in
  string/character literals and MUST be represented by escape sequences. For
  non-ASCII printable characters, either the actual Unicode character or its
  escape sequence MAY be used (choice determined by readability). For all
  escape sequences except widely-recognized ones (`\t`, `\n`, etc.), a comment
  SHOULD explain the meaning.

### Naming conventions

- **All file names, code, comments, and Javadocs MUST be written in English,
  with American English preferred for spelling.**

- **Identifiers MUST be composed only of ASCII letters and digits and, in a
  small number of cases, underscores (`\w+`).**

  Special prefixes or suffixes SHOULD NOT be used (eg. don't prefix variables
  with `s_` for static, or suffix interfaces with `I`).

- **Package names MUST use all lowercase letters and digits, no underscores,
  no hyphens. Consecutive words are concatenated with no delimiter.**

  Reverse domain name convention (eg. `com.example`) is long-established for
  global uniqueness. For internal application code, a project codename is
  preferred over a brand name (decouples code from marketing). Plural form for
  packages with homogeneous contents (`controllers`, `entities`, `services`);
  singular for heterogeneous contents (`gui`, `lib`, `util`, `config`).
  Abbreviations like `dto` or `dao` SHOULD NOT be pluralized.

- **Classes and interfaces: UpperCamelCase. Methods, fields, variables, and
  parameters: lowerCamelCase. Constants: UPPER_SNAKE_CASE.**

  Class names are typically nouns/noun phrases, descriptive and not overly long.
  Instantiable classes SHOULD use singular nouns (`UserService`); static-only
  containers MAY use plural (`DataAccessUtilities`). Interfaces follow class
  naming but SHOULD NOT be prefixed/suffixed with `I` or `Interface`. If an
  interface can't be better named, it MAY take the class name plus "Contract".
  Interfaces SHOULD NOT mirror exactly the implementing class's name (code
  smell suggesting tight coupling). Test classes MUST end with `Test`. Methods
  SHOULD be verbs/verb phrases; JUnit test methods MAY use underscores
  (`transferMoney_deductsFromSource`). Fields/variables/parameters SHOULD be
  nouns/noun phrases; one-character parameter names in public methods SHOULD be
  avoided.

- **A "constant" is a static final field whose contents are deeply immutable
  with no detectable side effects. Constants MUST use UPPER_SNAKE_CASE.**

  Local variables are NOT constants even if final and immutable. Examples of
  constants: primitives, strings, immutable value classes, `null`. Examples of
  non-constants: non-final fields, non-static fields, mutable collections,
  `Logger` instances, non-empty arrays.

- **Type variables SHOULD be either a single capital letter (optionally + a
  numeral, eg. `T`, `E`, `T2`) or the derived class/interface name + `T` (eg.
  `RequestT`).**

- **Annotation types SHOULD use UpperCamelCase (RECOMMENDED for consistency with
  the prevailing convention); MAY be verbs or nouns.**

### Code style

- **Indentation: 2 spaces per block level; continuation lines: 4 spaces.**

  Tab characters MUST NOT be used. IDEs SHOULD auto-replace tabs with spaces.
  Comments and Javadocs MUST align with the code they relate to.

- **One statement per line. Lines SHOULD be under 80 characters; SHOULD NOT
  exceed 100.**

  Package and import statements MAY exceed limits and MUST NOT be line-wrapped.
  Other code MAY exceed limits only where line-wrapping reduces readability or
  is impossible (eg. long URLs in comments).

- **Line-wrapping: refactor before wrapping; break at a higher syntactic level.**

  Break _before_ non-assignment operators and operator-like symbols (`.` and
  `::`). Break _after_ assignment operators. Break _after_ the lambda arrow if
  the body is a single un-braced statement. Commas stay attached to the
  preceding token. Constructors/method names stay attached to their opening
  parenthesis. Continuation lines indented +4 spaces.

- **Braces: K&R style ("Egyptian brackets") MUST be used for non-empty blocks.**

  No line break before the opening brace; line break after opening; line break
  before closing; line break after closing only if it terminates a statement or
  the body of a method/constructor/named class (`else`, `catch`, `finally`,
  `while` go immediately after the closing brace). Braces MUST be used with
  `if`, `else`, `for`, `do`, `while` even when the body is empty or
  single-statement. Empty blocks SHOULD be `{}` on the same line
  (`void doNothing() {}`). Authors MAY deviate from K&R where readability
  improves (eg. opening brace on a new line after very long statements, or
  blocks used only to limit scope of locals).

- **Vertical whitespace: single blank line between consecutive members;
  multiple consecutive blank lines SHOULD NOT be used.**

  Logical field groupings MAY be created by omitting blank lines between
  consecutive fields. Single blank lines MAY be added wherever they improve
  readability. No trailing whitespace — strongly RECOMMENDED to configure IDEs
  and pipelines to strip it automatically.

- **Horizontal whitespace: a single space in specific contexts.**

  Separating reserved words (`if`, `for`, `catch`) from opening parenthesis;
  `else`/`catch` from preceding closing brace; before most opening braces
  (exceptions: `@SomeAnnotation({a, b})`, `String[][] x = {{"foo"}};`); between
  type and variable (`List<String> list`); inside array initializer braces
  (`new int[] { 1, 2, 3 }`); after `,`, `;`, `:`; after cast closing parenthesis;
  on both sides of binary/ternary operators; around operator-like symbols
  (ampersand in conjunctive type bounds, pipe in multi-catch, colon in enhanced
  `for`, lambda arrow); before and after `//` that begins end-of-line comments.
  Additional spaces before end-of-line comments MAY be used for vertical
  alignment.

### Programming constructs

- **Wildcard imports (static or otherwise) SHOULD NOT be used.**

  Imports grouped by: static imports, then non-static imports, with exactly one
  blank line between groups. Within each group, sorted alphabetically. No
  other blank lines between imports. Import statements SHOULD NOT be
  line-wrapped (MAY exceed column limits). Static imports SHOULD NOT be used
  for static nested classes (use normal imports).

- **Each variable declaration MUST be on its own line; `int a, b;` MUST NOT be
  used (except in `for` loop headers).**

  Local variables SHOULD be declared close to first use (minimize scope), not
  habitually at the beginning of the containing block. SHOULD have initializers
  or be initialized immediately after declaration.

- **Class contents: a logical ordering is RECOMMENDED (class variables →
  instance variables → constructors → methods).**

  Better to order/group methods logically than by visibility, type, or name.
  However, it is REQUIRED that methods sharing the same name (overloads) be
  grouped together; this also applies to variadic constructors. Constructor and
  method declarations MUST be separated by a blank line; constants and fields
  MAY be.

- **Enums: singular form for the enum name; no blank lines within enum bodies
  (except around comments).**

  An enum with no methods and no constant documentation MAY be formatted on a
  single line (`private enum Suit { CLUBS, HEARTS, SPADES, DIAMONDS }`).
  Otherwise, constants on separate lines with trailing commas and opening brace
  on the same line as the enum name.

- **Modifiers SHOULD appear in JLS-recommended order:**

  `public protected private abstract default static final sealed non-sealed
  transient volatile synchronized native strictfp`

  `public` MUST be added only if the class is intended for use outside its
  package. Access modifiers SHOULD be added in most cases (be explicit). Most
  instance variables SHOULD be `private` (data hiding). Package-scoped members
  SHOULD generally be avoided, though useful in libraries and aggregate root
  pattern implementations.

- **Annotations: field annotations on the same line; class/method annotations
  each on separate lines before the declaration and after any preceding
  Javadoc.**

  Type-use annotations MUST appear immediately before the type they annotate.
  No specific formatting rules for parameter or local variable annotations.
  `@Override` MUST be used on all methods intended to override a superclass or
  interface method (exception: MAY be omitted when the parent is `@Deprecated`).

- **Static members MUST be qualified with the class name, not with a reference
  or expression of that class's type.**

  `Foo.doSomething()` not `myFoo.doSomething()` or
  `somethingThatReturnsFoo().doSomething()`.

- **Exceptions: it is very rarely correct to do nothing in response to a caught
  exception; if you do, the reason MUST be documented in a comment within the
  `catch` block.**

  In tests, the `try { emptyStack.pop(); fail(); } catch
  (NoSuchElementException expected) {}` idiom does not need a comment.

- **Switch statements: line break after each label; `// fall through` SHOULD be
  included where execution might continue into the next group (not required for
  the last group or empty groups).**

  Each switch statement MUST include a `default` group, even if empty. Only an
  `enum` switch MAY omit `default`, and only if it covers all possible values
  (enables static analysis warnings for missed cases).

### Types

- **Numeric literals: uppercase `L` suffix MUST be used for long literals
  (`3000000000L`, not `3000000000l`).**

- **Arrays: brackets SHOULD form part of the _type_, not the _variable_
  (`String[] args`, not `String args[]`).**

  C-style array declarations SHOULD NOT be used. Array initializers MAY be
  formatted as block-like constructs (single line, wrapped, or one element per
  line).

### Comments

- **Implementation comments (`//` and `/* ... */`) are for code explanation;
  Javadoc (`/** ... */`) is for API documentation.**

  `//` for commenting-out code and short end-of-line comments. `/* ... */` SHOULD
  be used for both single-line and multi-line implementation comments (opening
  and closing on the same line for short comments; on their own lines when
  wrapped). Exactly one space after `/*` and before `*/` for single-line
  `/* ... */` comments; exactly one space after `//`. Block-level comments MUST
  be indented to the same level as the related code. Multi-line block comments
  SHOULD have a blank line before and after; single-line SHOULD have a blank
  line before. All text within `/* ... */` MUST be full sentences starting with
  a capital and ending with a period. Implementation comments SHOULD only
  communicate information not readily available from the code; SHOULD NOT
  specify API/behavior (Javadoc's purpose) or explain build/test procedures
  (READMEs/out-of-band docs' purpose).

- **Javadoc SHOULD document all `public` classes and every `public` and
  `protected` member.**

  MAY be skipped for methods overriding an already-documented supertype method
  (documentation is inherited). Javadoc MUST NOT be used to document
  implementation details (use standard comments for that). Javadoc SHOULD NOT
  duplicate information encoded in method names or signatures. Single-line form
  (`/** An especially short bit of Javadoc. */`) SHOULD be used for short
  comments with no block tags. In multi-line form, the first paragraph SHOULD be
  a brief summary fragment (a complete sentence, not a detailed description);
  subsequent paragraphs MUST be prefixed with `<p>` (or other block-level tags
  like `<ul>`) immediately before the first word with no space. Block tags
  (`@param`, `@return`, `@throws`, `@deprecated`) MUST be on separate lines in
  that order, followed by a space and a text description (continuation lines
  indented +4 spaces from the `@`). Block tags MUST NOT be used in single-line
  Javadoc (`/** @return the customer ID */` is invalid; use `/** Returns the
  customer ID. */`).

### Java API specifications

- **JPA is RECOMMENDED for simple interactions with relational databases.**

  JPA (Jakarta Persistence, formerly Java Persistence API) provides ORM
  interoperability between compliant libraries (Hibernate, Spring Data JPA).
  For more complex interactions (deep joins, performance-critical queries), a
  lower-level abstraction or no abstraction may be more appropriate.

## References

- [TS-33 source](../../pages/033-java.adoc)
- [TS-7: Code Design](../007/AGENTS.md)
- [TS-26: Technical Writing Style Guide](../026/AGENTS.md)
- [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html)
- [Oracle Code Conventions](https://www.oracle.com/java/technologies/javase/codeconventions-introduction.html)
