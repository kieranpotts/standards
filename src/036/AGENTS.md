# TS-36: ECMAScript (JavaScript/TypeScript)

This is a compact version of technical standard TS-36 for AI agents.

Use this when writing or reviewing JavaScript or TypeScript source code:
language syntax and style, functions, objects and classes, modules, package
manifests, dependency management, TypeScript usage, asynchronous programming,
functional programming, runtime targeting (Node/web), architecture, and
testing/error handling.

Do NOT use this for framework-specific rules (React, Vue), CSS-in-JS, Node.js
application/deployment concerns beyond the language itself, or Markdown/JSON
formatting — see the cross-referenced standards below for those.

Follow [TS-27: Markdown](../027/AGENTS.md) formatting rules when writing
Markdown, including inside docblocks and this file.

## Rules

### Files and encoding

- **File naming and encoding.**

  JavaScript files MUST use the `.js` extension; TypeScript files MUST use
  `.ts` (never `.mjs`). File names MUST be all lower case, MAY include dashes
  but not underscores, and MUST NOT carry other punctuation. All files MUST be
  UTF-8, using only the line terminator and ASCII space (0x20) as whitespace;
  tabs MUST NOT be used for indentation.

- **Escape sequences.**

  Use standard escape sequences (`\'`, `\"`, `\\`, `\b`, `\f`, `\n`, `\r`,
  `\t`, `\v`), not numeric/Unicode escapes (`\x0a`, `\u000a`, or `\u{a}`) or
  legacy octal escapes. Printable non-ASCII characters SHOULD be written as
  literal Unicode characters (`'μs'`); where a hex/Unicode escape is
  necessary, document why in an adjacent comment and print the literal
  character in an end-of-line comment. Non-printable characters MUST have an
  inline comment explaining their purpose.

### Types and values

- **Type system.** TypeScript MUST be used to enforce strong typing across all
  JavaScript code (see [TypeScript](#typescript) below). Any standalone
  JavaScript package MUST export `*.d.ts` type definition files.

- **Numbers.** Binary floating point cannot exactly represent most decimal
  fractions (`0.1 + 0.2 !== 0.3`). Decimal values SHOULD be scaled to whole
  numbers (e.g. cents instead of dollars) so integer arithmetic is exact.
  Where scaling is impractical, use a dedicated decimal-arithmetic library
  (e.g. Decimal.js, bignumber.js).

- **BigInt.** `BigInt` MUST be used only in runtimes that support it natively
  — it cannot be reliably polyfilled. Use it for integers exceeding
  `Number.MAX_SAFE_INTEGER`.

- **Strings.** Prefer single quotes, switching to double quotes only to avoid
  escaping. Use template literals (backticks) for interpolation/multi-line
  strings. Use `String.prototype.includes` to test for a substring, not
  `indexOf`.

- **Primitives, not wrapper objects.** Always define booleans, numbers, and
  strings as primitives, never as `new Boolean()`/`new Number()`/`new
  String()` — a `Boolean` object is always truthy regardless of its internal
  value. To coerce a value, call `Boolean()`, `Number()`, `String()` without
  `new`.

- **Equality.** Always use `===`/`!==`. `==`/`!=` perform unintuitive implicit
  coercion (e.g. `'0' == ''` is `true`).

- **Nullish coalescing and optional chaining.** Use `??` to fall back only
  when the left operand is `null`/`undefined` (unlike `||`, which triggers on
  any falsy value). Use `?.` to short-circuit to `undefined` instead of
  throwing on a `null`/`undefined` base.

- **`typeof` vs `instanceof`.** `typeof` is safe on undeclared variables but
  `typeof null === 'object'` and it cannot distinguish object subtypes — use
  `instanceof` or `Array.isArray()` for that.

### Statements, control flow, arrays

- **One statement per line; semicolons.** Every statement MUST end with a
  semicolon except `for`, `function`, `if`, `switch`, `try`, `while`.
  Function expressions and `do...while` MUST end with a semicolon. Because of
  automatic semicolon insertion, a `return` expression MUST be on the same
  line as `return`, and opening braces MUST be on the same line as whatever
  they open:

  ```javascript
  // ✅ Correct — returns the object.
  return {
    result: false
  }

  // ❌ Wrong — returns undefined (semicolon inserted after `return`).
  return
  {
    result: false
  }
  ```

- **Literals over `new`.** Use `[]`/`{}` instead of `new Array()`/`new
  Object()`, and primitive types instead of `new String()`/`new Number()`/
  `new Boolean()`.

- **Control structures.** Always use curly braces even where optional; the
  opening brace MUST be on the keyword line. `else`/`else if` SHOULD begin on
  a new line, not `} else {`.

- **`switch`.** Prefer `if`/`else` chains where they read as well. A case
  MUST NOT intentionally fall through — every case SHOULD end with `break`
  (or `return`/`throw`). Where a `switch` dispatches on a value to call a
  function, prefer a dispatch-table object instead.

- **Loops.** Use `for`/`while`/`do...while` for counted loops, `for...of` for
  iterables, `for...in` only for object property enumeration (guard it with
  `Object.hasOwn()`, or prefer `Object.keys()`/`Object.entries()`).

- **Arrays.** Define with `[]`, never `new Array()`. Use
  `Array.prototype.includes` to test membership, not `indexOf(...) !== -1`.
  Use `some`/`every` (both short-circuit) to test conditions; `forEach` has
  no `break`. Prefer non-mutating `filter`/`map` over `splice`. Convert
  array-likes with `Array.from()` or spread, not the `Array.prototype.slice`
  hack.

- **Strict mode.** ES modules and class bodies are always strict. In classic
  scripts, scope `'use strict'` to a function or IIFE, never the global
  scope of a concatenated file.

- **Regular expressions.** Prefer a more expressive alternative where one
  achieves the same result. Complex patterns MUST be accompanied by an
  explanatory comment.

### Naming and code style

- **Low-level style via tooling.** Enforce indentation, spacing, and quote
  style with a formatter (e.g. Prettier) and correctness/best-practice rules
  with a linter (e.g. ESLint) in CI. Default: 2-space indentation, single
  quotes.

- **Naming conventions.**

  - Classes: `UpperCamelCase`. Capability protocols end in "able"/"ible"/"ing"
    (`Equitable`, `ProgressReporting`).
  - Functions/methods: `lowerCamelCase`. Side-effect-free methods read as
    noun phrases (`obj.distance(...)`); side-effecting methods read as
    imperative verbs (`sort()`, `append()`). Factories are prefixed `make`
    (`makeModel()`). Mutating/non-mutating pairs are distinguished by suffix
    (`sort()`/`sorted()`) or a `clone` prefix on the mutating form
    (`union()`/`cloneUnion()`). Boolean methods/properties read as
    assertions (`isEmpty()`).
  - Variables/properties: `lower_case`, named for role not type.
  - Prefer explicit names that encode units/intent: `sleepForSeconds(t)` over
    `sleep(t)`.
  - Most objects SHOULD be immutable after construction; prefer non-mutating
    methods and functions generally.
  - Place parameters with defaults toward the end of the parameter list.

### Variable declarations and scope

- **`const` over `let` over `var`.** Prefer `const` for any binding never
  reassigned. Use `let` only where reassignment is genuinely needed. Avoid
  `var` entirely — it is function-scoped, hoisted, and permits redeclaration;
  any remaining `var` is a code smell. `const`/`let` are block-scoped and
  throw `ReferenceError` if accessed before declaration (temporal dead
  zone).

- **`const` freezes the binding, not the value.** For true immutability of
  an object, combine `const` with `Object.freeze()`.

- **One declaration per line**, initialized at the point of declaration
  where practical. An identifier SHOULD represent one concept for its whole
  lifetime.

- **Avoid global variables.** Encapsulate state in modules, functions, and
  objects. A function MUST NOT read or mutate variables from an outer
  (non-module) scope — all variables used inside a function MUST be either
  passed as arguments or declared within it. Use `globalThis` (not
  `window`/`self`/`global`) to reference the global object portably.

- **`this` binding.** `this` is call-time bound, not definition-time bound.
  Arrow functions inherit `this` lexically and cannot be rebound by
  `call`/`apply`/`bind` — this is why arrow functions are preferred for
  functional-style code.

### Comments and inline API documentation (JSDoc/TSDoc)

- **Comment syntax and language.** Use `//` for unstructured inline notes,
  each on its own line (not trailing at end-of-line). All comments MUST be
  written in American English with proper grammar.

- **Docblocks document API surface.** Use the multi-line `/** ... */` form
  (never single-line `/** ... */` except for inline type casts — see below).
  Every docblock MUST be preceded by a blank line (except file-level
  docblocks, which start on line 1), and the line after it MUST start the
  documented code.

  ```javascript
  /**
   * @type {string}
   */
  let s
  ```

- **Descriptions** are optional, written on the docblock's first line, with
  one blank line before any tags. Markdown is permitted (backticks, `*bold*`,
  `_italic_`, `[text](url)`); inline HTML MUST NOT be used.

- **Tags used:** `@alpha`, `@author`, `@beta`, `@callback`, `@copyright`,
  `@deprecated`, `@example`, `@experimental`, `@extends`, `@license`,
  `@link`, `@param`, `@prop`, `@see`, `@returns`, `@template`, `@this`,
  `@throws`, `@type`, `@typedef`. All are block-level except `@link`
  (inline). Do NOT align tag columns — alignment increases line length and
  churns diffs on every edit.

- **Types.** Use curly-brace type syntax: `{string}`, `{number|boolean}`
  (space either side of `|` for union/nullable types), `{string[]}`,
  `{Promise<string>}`, `{(s: string) => number}`. Declare primitives in
  lower case (`string`, not `String`). For functions returning nothing,
  declare `{void}`. Non-specific `any` (JSDoc's `*`) SHOULD be avoided;
  document your reason wherever the type checker is disabled. Do not use `?`
  for "unknown" — use `*` for "any" instead.

  ```javascript
  /**
   * @type {{ a: string, b?: number }}
   */
  ```

- **Functions.** SHOULD be fully typed (`@param`, `@returns`, `@throws`, in
  that order, no blank lines between `@param`/`@returns`). A function's
  docblock MUST have exactly one `@returns` tag (even for `void` or `async`
  functions) with a comment. Declare the return type explicitly for
  functions that `return new Promise()` rather than use `async`. `@throws`
  tags MUST NOT wrap the thrown type in `{}`; use one tag per error type,
  each with a comment starting with the type name in backticks.

- **Anything exported from a module MUST have its types declared** via
  `@type`. Internal variables SHOULD also be typed for accuracy.

- **Classes.** SHOULD have a class-level docblock. Constructor parameters
  MUST be documented on the `constructor`. Prefer ECMAScript `#` private
  fields over TypeScript's `private` modifier (see
  [Private members](#objects-and-classes)) — `private` is compile-time only
  and leaks the field into build artifacts.

- **File-level docblocks.** Every file MUST have a single file-level
  docblock starting on line 1. `@file`/`@fileOverview` are not used — the
  leading prose is the module description. `@author` is required only when
  authorship differs from the copyright owner. Contact details (emails)
  MUST NOT appear in docblock tags. `@since` and `@version` MUST NOT be
  used — versioning belongs in `package.json` and changelogs.

- **Release-stage tags** (`@experimental`, `@alpha`, `@beta`, `@deprecated`)
  SHOULD sit near the top of a docblock, immediately after the description.

- **Examples** (`@example`) MUST be correct and executable in isolation.

- **VS Code integration.** Enable JS type-checking with `// @ts-check` per
  file, or repository-wide via `js/ts.implicitProjectConfig.checkJs` in
  `.vscode/settings.json` — RECOMMENDED to do both, since the repo-level
  setting is ignored when the folder opens inside a broader workspace.
  `// @ts-nocheck` disables per file; `@ts-ignore` suppresses the next line.

### Functions

- **Declarations vs. expressions.** Use a function declaration only where
  consumers need dynamic `this` rebinding or where the function is used as a
  constructor. In all other cases, use a function expression assigned to
  `const`. Arrow functions cannot be used as constructors and cannot be
  rebound with `bind()`.

- **Parameters.** Use rest parameters (`...args`) instead of the legacy
  `arguments` object. Prefer default and rest parameters over manual
  argument checks.

- **Return values.** Unless the return shape is obvious from the function
  name, return an object so callers can destructure by name:

  ```javascript
  return { template, id }
  ```

- **`call`/`apply`/`bind`.** `apply` takes arguments as an array; `call`
  takes them individually. Pass `null` as the context argument when no
  context is needed. Arrow functions cannot be rebound by any of the three.

### Objects and classes

- **Do not modify objects you do not own.** Never extend or change the APIs
  of native objects (`Array`, `Math`, `Object`, ...) or host objects (e.g.
  the DOM).

- **Definition vs. assignment.** `Object.defineProperty()` creates an own
  property with explicit attributes; `obj.prop = value` invokes an inherited
  setter or creates an own property with default attributes, and never
  mutates a prototype's properties.

- **Object equality is by reference**, not value. Implement a dedicated
  comparison function (or use a library) to compare by value.

- **`toString()`.** Custom types SHOULD override it for a meaningful debug
  representation.

- **Property access.** Use dot notation by default; use bracket notation
  only for computed names, non-identifier names, or names with special
  characters.

- **Classes are the preferred construct** for encapsulating related data and
  behavior (ES2015+), preferred over constructor functions. No commas
  separate class members. Class declarations/expressions are NOT hoisted —
  a class MUST be declared before use.

- **Private members.** Authors MUST NOT use TypeScript's `private` modifier.
  Use ECMAScript `#`-prefixed private fields instead — the compiler keeps
  these genuinely private in build output, whereas `private` is compile-time
  only:

  ```javascript
  class Person {
    #name

    constructor(name) {
      this.#name = name
    }
  }
  ```

- **Inheritance.** A superclass instance SHOULD be substitutable by a
  subclass instance (Liskov Substitution Principle). Prefer composition over
  inheritance where either could express the design; deep hierarchies are
  rarely needed given JavaScript's prototypal (delegation-based) model.

- **Class design.** Each class SHOULD have one responsibility and one reason
  to change. Code to an interface, not a concrete type. Prefer constructor
  injection against an interface over tight coupling.

### Modules

- **ES modules only.** Standard ECMAScript modules (`import`/`export`) MUST
  be used exclusively for all code. Authors MUST NOT write CommonJS
  (`require`/`module.exports`), AMD, or UMD modules. JavaScript files MUST
  use `.js` (not `.mjs`); rare CommonJS exceptions (e.g. tool config files)
  MUST use `.cjs` to distinguish them.

- **Import directories via `index.js` explicitly** — unlike CJS's `require()`,
  ESM's relative imports do not resolve a directory to its `index.js` file
  automatically:

  ```javascript
  import database from './database/index.js'
  ```

- **Internal absolute imports.** For in-house applications, use the `~`
  prefix for internal imports (resolving to `src/`), reserving `@` for
  external package imports (resolving to `node_modules/`). This convention
  MUST NOT be used in public libraries, where relative paths MUST be used
  instead.

  ```javascript
  import { forIn } from '~utils/array'
  ```

- **Importing JSON.** Use the `with { type: 'json' }` import attribute where
  supported; otherwise read and `JSON.parse()` the file with `fs`. Loading
  JSON via `require()` is CommonJS and MUST NOT be used. Module imports are
  cached — for content that must always be fresh (e.g. test fixtures), read
  and parse the file directly.

- **Named exports over default exports.** New libraries and applications
  SHOULD use named exports: they force refactors to use a stable identifier,
  enable tree-shaking, are more extensible, and are cross-referenced more
  reliably by tooling. Mixing default and named exports in one module is bad
  practice (though permitted) and complicates CJS interop.

  ```javascript
  // ❌ Do not do this.
  export default {
    propertyA: 'A',
    propertyB: 'B',
  }

  // ✅ Do this instead.
  export const propertyA = 'A'
  export const propertyB = 'B'
  ```

- **Aliasing named imports** SHOULD be done only to resolve identifier
  conflicts, keeping the canonical name visible.

- **Node's dual interpreter.** Set `"type": "module"` in `package.json`
  (root or per-directory) to make Node interpret `.js` files as ESM — this
  is the RECOMMENDED way to toggle the interpreter (over the `.mjs`
  extension, which is NOT RECOMMENDED since many tools, notably TypeScript,
  do not recognize it). Files that must stay CommonJS get the `.cjs`
  extension.

- **Importing CJS into ESM.** Import the whole module via default import
  (CJS has no concept of named exports), then destructure:

  ```javascript
  import _ from './lodash'
  const { shuffle } = _
  ```

  Node can sometimes detect CJS named exports automatically, but this is
  fragile — prefer whole-module default imports. Prefer ESM packages over
  competing CJS ones where a choice exists, for tree-shaking.

- **Importing ESM into CJS.** Use dynamic `import()` (CJS's synchronous
  `require()` cannot load async ESM). Wrap `await import()` in an `async`
  IIFE within CJS scripts, since CJS lacks top-level `await`.

- **Dynamic `import()`** (ES2020) is for runtime-driven loading — user
  locale, lazy loading, robustness against optional-module failure. Its
  specifier is evaluated at runtime and need not be a string literal.
  Static `import` remains the default for anything that can be
  statically analyzed, bundled, and tree-shaken.

### Package manifests and tooling

- **Package filesystem.** Every package MUST have a `package.json`, a
  Markdown README, and a plain-text LICENSE file, plus a `lib` directory
  (programmatic API) and/or a `bin` directory (CLI).

- **Separate package manifests from repository manifests.** A package
  manifest carries publish metadata and `dependencies`/`peerDependencies`
  only. A repository manifest carries `devDependencies`, `scripts`, and
  `workspaces`, with `private: true` set and `name`/`version` omitted so
  `npm publish` fails safely if attempted.

- **`type` field is REQUIRED in every manifest**, even when the value is
  `"commonjs"` — this future-proofs the package for tooling.

- **Package `exports`.** Prefer the `exports` field (an export map) over
  the legacy single-entry `main` field; `exports` overrides `main` and
  encapsulates the package, preventing consumers from importing undeclared
  entry points. Introducing `exports` on an existing package MUST declare
  all previously-implicit entry points explicitly, to avoid a breaking
  change. Disabling encapsulation entirely (`"./*": "./*"`) is NOT
  RECOMMENDED except as a pragmatic migration step.

- **Conditional exports** (`require`/`import` keys) support hybrid CJS/ESM
  packages. All exported modules of a hybrid package MUST be stateless,
  since ESM and CJS run through separate interpreters and could otherwise
  create two independent instances of the "same" module.

- **`bin` maps CLI command names to scripts.** Use `process.argv` to read
  CLI arguments; omit the `.js` extension from files referenced in `bin`.

- **Publishing.** Test extensively before publishing — verify the packed
  archive locally with `npm pack` and install it into an empty directory
  before running `npm publish`. Deprecate rather than fully remove a
  published version (`npm unpublish --force` breaks dependents).

- **Vendor packages MUST be audited before use.** Good test coverage is
  REQUIRED so upgrades don't introduce regressions; security auditing is
  REQUIRED on every new or updated dependency (see
  [TS-52: Security and Secrets Management](../052/AGENTS.md)).

- **Repository structure for libraries** — top-level `dist` (build output,
  excluded from source control), `docs`, `lib` (repo-level automation
  scripts), `run` (run-scripts referenced from `package.json`), `src`
  (source, mirroring the eventual `node_modules` install layout), `srv`
  (public website source, if any). Per-package source under `src` MUST
  encapsulate its library code in `lib` and any CLI in `bin`.

- **Package manager.** Yarn is RECOMMENDED. All contributors to a project
  SHOULD use the same package manager — Yarn and NPM can produce different
  dependency trees. Prefer `npx`/`yarn dlx` over global installs for
  one-off commands and generators.

- **Transpilation and bundling.** Transpile/bundle as little as possible;
  prefer native ES modules over transpiled, synchronously-loaded bundles
  wherever target runtimes support them. Babel is the standard transpiler.
  Use dynamic `import()` plus bundler code-splitting to lazy-load code
  rather than shipping one large bundle.

- **Package design.** Classes within a package SHOULD form one cohesive,
  reusable family. Prefer a dependency hierarchy where higher-order
  packages depend only on lower-order ones, avoiding circular references.
  Public APIs and behavior SHOULD be stable even while internals iterate.

### Dependency management

- **Major version updates.** Use static analysis to detect available major
  updates and raise issues automatically. Prefer LTS releases. For
  dependencies with an SLA, major versions MUST be updated before their EOL
  date.

- **Minor/patch updates.** SHOULD be applied regularly, ideally at the start
  of a release cycle (not close to release) via dedicated maintenance
  issues.

- **Minimize dependency count** while still favoring well-maintained vendor
  libraries over reinventing solved problems.

- **Prefer dependency injection** — a component receives its dependencies
  from an external source rather than constructing them itself, which
  simplifies testing and removes construction concerns from the component:

  ```javascript
  // ✅ Dependencies injected via constructor.
  class MyClass {
    constructor(database) {
      this.database = database.connect()
    }
    myFunction() {
      return this.database.query()
    }
  }
  ```

- **Version constraints.** Prefer the patch constraint (`~1.2.3`) over the
  minor constraint (`^1.2.3`) for production dependencies — manually upgrade
  minor/major versions only when new features are needed. Minor constraints
  (`^`) MAY be used for `devDependencies`. Publicly-distributed packages
  MUST NOT blindly accept any update, including patches, to their production
  dependencies — extensive manual end-to-end testing MUST be performed
  whenever a dependency lock file changes.

- **Commit production dependencies to source control** wherever practical,
  so the application can always be rebuilt to reproduce an identical
  artifact.

### TypeScript

- **Use a subset of TypeScript.** Apply TypeScript only where the
  application's scale/complexity benefits from it, and prefer standard
  ECMAScript syntax and APIs over TypeScript-specific notation where both
  exist (e.g. `#` private fields over `private`). Regularly upgrade to the
  latest TypeScript release; no specific minimum version is mandated.

- **Non-null assertion (`!` after an expression)** MUST be used sparingly —
  consider `any`/`unknown` instead. Wherever the type checker is disabled,
  it becomes the developer's responsibility to check types at runtime, and
  meaningful exceptions SHOULD be thrown when non-nullness assumptions turn
  out to be wrong.

- **Definite assignment assertion (`!` after a declaration)** SHOULD be
  preferred over the non-null assertion where *all* instances of a
  variable/property will be assigned.

- **Handling "possibly undefined" values** — prefer, in order of
  specificity: a type-narrowing conditional (`typeof token === 'string'`),
  the nullish coalescing operator (`token ?? 'default'`, stricter than
  `||`), an `as` type assertion, or the non-null assertion `!` as a last
  resort.

- **Declaration files (`.d.ts`).** Library authors SHOULD maintain type
  declarations in parallel with development — publicly-maintained
  third-party `.d.ts` files frequently mismatch the libraries they
  describe. TypeScript-authored libraries get declaration files generated
  automatically; JavaScript-authored libraries either hand-write `.d.ts` or
  generate it from JSDoc/TSDoc comments.

- **Decorators** are a higher-order-function pattern for wrapping behavior
  (`@decorator` syntax). Class member decorators receive `(target, name,
  descriptor)`; class decorators receive the constructor and decorate every
  instance, so are generally less useful than member decorators.

### Asynchronous programming

- **Avoid callbacks for new code** — use promises/`async`/`await` instead.
  Where a callback API must still be consumed, follow the Node.js
  error-first convention (`(err, result) => ...`) and never ignore the
  error argument.

- **Promise combinators.**

  - `Promise.all` — resolves with all results once every input fulfills, or
    rejects as soon as one rejects.
  - `Promise.allSettled` — resolves once every input has settled
    (`{status, value}` or `{status, reason}`); never rejects.
  - `Promise.race` — settles the same way as the first input to settle.
  - `Promise.any` — resolves with the first fulfillment, or rejects only if
    all reject.

- **`async`/`await` MUST NOT be used inside `forEach()`** or other
  higher-order functions that do not await their callback — the enclosing
  function returns before the async work completes:

  ```javascript
  // ❌ Wrong — printFiles returns before files are read.
  async function printFiles () {
    const files = await getFilePaths()
    files.forEach(async (file) => {
      const contents = await fs.readFile(file, 'utf8')
      console.log(contents)
    })
  }
  ```

  Use `for...of` to run iterations in sequence, or `Promise.all(files.map(...))`
  to run them in parallel.

- **Async iteration** over a collection of promises that resolve
  independently: use `for await...of` (`forEach` cannot be awaited).

- **`new Promise()` is an anti-pattern.** Almost always unnecessary and
  reintroduces the error-handling problems promises solve. Prefer
  `async`/`await` or chaining existing promises directly.

- **Constructors cannot be `async`.** If construction needs async work,
  store the promise from an IIFE and expose async methods that `await` it,
  rather than an `initialized` property callers must remember to check:

  ```javascript
  class ExampleClass {
    #dependency_promise

    constructor () {
      this.#dependency_promise = (async () => { /* ... */ })()
    }

    async otherMethod () {
      const dependency = await this.#dependency_promise
    }
  }
  ```

### Functional programming

- **Apply FP principles pragmatically**, particularly at the level of data
  structures and algorithms — not as a purist constraint on the whole
  codebase. JavaScript is multi-paradigm and more object-oriented than
  functional; use utility libraries (Ramda, Lodash FP, Immutable.js) where a
  strong FP style is genuinely warranted.

- **Prefer arrow functions for higher-order-function code** wherever the
  function does not need to internally reference `this` — arrow functions
  are lexically scoped and cannot be rebound, matching FP's no-surprises
  goal.

- **Function composition.** Prefer `pipe(...)` (left-to-right, argument
  order matches call order) over `compose(...)` (right-to-left) for
  readability.

- **Currying — design for it, don't bolt it on.** Curried function
  signatures SHOULD have: fixed arity (a function called with too few
  arguments MUST either throw or return a function awaiting the rest);
  data-last (the data being transformed is the final argument); and
  iterator-first (transform functions precede the data argument).

  ```javascript
  // ✅ Curried, data-last.
  const discount = (discountValue) => (price) => price + discountValue
  ```

- **Pure functions** must not depend on or mutate external state (random
  values, current time, globals, DOM, filesystem, DB, console/network I/O)
  and must not mutate their own input parameters — always return new
  values. This gives referential transparency: same input, same output,
  every time.

- **Immutability.** Primitives are immutable by default; objects and arrays
  are not. Shallow copies (`Object.assign({}, obj, patch)` or `{...obj,
  patch}`) are insufficient for nested structures — nested objects still
  share references and mutating them mutates the original:

  ```javascript
  const updated = { ...person, address: { ...person.address, city: 'X' } }
  ```

  For non-trivial immutable data structures, use a dedicated library (e.g.
  Immutable.js, Immer) rather than hand-rolling deep copies.

- **Recursion** is the FP-idiomatic alternative to loops for
  branching/traversal problems (sorting, tree traversal, fractal math).
  Test the terminal case before computing, so recursive calls exit early.

### Runtimes

- **Node version support.** Target only Node's active and maintenance LTS
  releases (even-numbered majors) — the `engines` field SHOULD pin the
  initial LTS patch release of each supported major:

  ```json
  {
    "engines": {
      "node": "^<maintenance-lts-1>.x.x || ^<maintenance-lts-2>.x.x || ^<active-lts>.x.x"
    }
  }
  ```

  Supporting the short-lived odd-numbered "current" release MUST be done
  only with specific business justification. Dropping support for a Node
  major MUST coincide with a major version bump of your own package —
  don't drop support just because Node's own maintenance for it ended.

- **Node built-in modules.** Import with the `node:` scheme to distinguish
  them from vendor/local modules (`import fs from 'node:fs/promises'`).
  Prefer the promise-based API over the callback API where both exist
  (`node:fs/promises` over `node:fs`, or `util.promisify` for legacy
  callback functions). Prefer streams over buffering whole files for large
  or streaming I/O. See
  [TS-38: Node.js Applications](../038/AGENTS.md) for application-level
  Node conventions.

- **Feature detection over UA sniffing.** Detect the specific feature you
  intend to use; do not infer one feature's presence from another, and do
  not branch on user-agent strings to target current/future browser
  versions. Avoid vendor-prefixed features except to target old, buggy
  browser versions, and always keep a default code path for
  unknown/current browsers. See
  [TS-37: Web Platform APIs](../037/AGENTS.md) for browser API guidance.

- **Universal (isomorphic) JavaScript.** Host-agnostic utility libraries
  SHOULD be written to run in any runtime, to maximize reuse between client
  and server — but avoid runtime-branching (`process.browser`) inside a
  single package, which ships unnecessary code to each environment.

- **Date validation.** `new Date()` always returns a `Date` instance, even
  for an invalid input string — check validity via the timestamp, not
  `instanceof`:

  ```javascript
  const date = new Date('an invalid date-time string')
  if (isNaN(date.getTime())) {
    // Date is invalid.
  }
  ```

  See [TS-47: Dates and Times](../047/AGENTS.md) for broader date/time
  handling conventions.

### Architecture and design

- **API consistency.** Keep parameter naming/ordering, return types, and
  getter/setter naming conventions consistent across an application or
  library's internal APIs.

- **Avoid function overloading** — radically different behavior based on
  argument shape (à la jQuery's `load()`/`toggle()`) is hard to test and
  increases external complexity.

- **Domain-Driven Design layers** for Node.js applications: *Interfaces*
  (interaction with other systems — validation, serialization), *Application*
  (interface-independent workflow orchestration, thin on domain logic),
  *Domain* (the core business logic — entities, value objects, domain
  events, repository interfaces, one package per aggregate, named per the
  ubiquitous language), *Infrastructure* (external libraries, database,
  messaging — should be fully stubbable in unit/scenario tests while still
  exercising the domain layer).

### Barrel files

- **Barrel files re-export a directory's modules through one entry point**
  (conventionally `index.ts`), so consumers import from the directory
  rather than each individual file:

  ```typescript
  // utils/index.ts
  export * from './formatDate'
  export * from './parseUrl'
  ```

  ```typescript
  import { formatDate, parseUrl } from './utils'
  ```

### Testing and quality assurance

- **Test framework.** Preference is Mocha + Chai + Sinon (alternatives:
  Jest, Ava, Jasmine); Nock for HTTP mocking, jsdom for a browser
  environment, Selenium/Cypress for web automation. Tests live in
  `./test/`; unit tests use the `.test.js` suffix, behavior-driven tests
  `.spec.js`. Write tests in standard ESM. See
  [TS-12: Quality Assurance](../012/AGENTS.md) and
  [TS-13: Functional Testing](../013/AGENTS.md) for broader testing
  strategy.

- **Test independence.** Isolate the unit under test; reset state between
  cases via framework hooks; stub/mock dependencies as needed. Test both
  passing and failing conditions.

- **Linting.** Use ESLint for static analysis; enforce low-level style
  through it rather than by hand. Prefer disabling ESLint line-by-line;
  where a whole file must be excluded, place `/* eslint-disable */` near
  the top, before any code.

- **Custom errors MUST extend `Error`** (or an `Error` subclass) — plain
  thrown objects lack stack traces and behave inconsistently with
  built-ins:

  ```javascript
  class StackOverflowError extends Error {
    constructor(message) {
      super(message)
      this.name = this.constructor.name
      if (typeof Error.captureStackTrace === 'function') {
        Error.captureStackTrace(this, this.constructor)
      } else {
        this.stack = (new Error(message)).stack
      }
    }
  }
  ```

- **Throw, don't return, for exceptional conditions** — throw whenever a
  component is used outside its designed contract (e.g. unexpected
  parameter type/range). Always throw an `Error` instance or subclass, not
  a bare value.

- **Exception handling.** Code that may throw MUST be wrapped in `try`,
  followed by `catch`, `finally`, or both. Discriminate error types with
  `instanceof` inside `catch`.

- **`eval()` MUST NOT be used** — slow, dangerous, and always better solved
  another way. **`with` MUST NOT be used** — it makes name resolution
  ambiguous and slows execution.

- **Memory leaks** stem mainly from circular references and closures that
  hide them. Explicitly null out object references when finished with
  them.

- **Don't over-optimize early.** Optimize only once a program is provably
  too slow, and only the slow parts.

- **Polyfills** SHOULD be used only where a modern feature is essential and
  there is no other implementation path, with a documented business
  justification — every polyfill adds weight.

- **Logging.** Avoid `console.*` in production code; use a structured
  logging library instead. Do not commit stray `console.log` calls.

## References

- [TS-36 (source)](README.adoc):
  Read this for the full standard, rationale, and background context.

- [TS-27: Markdown](../027/AGENTS.md):
  Read this when formatting Markdown, including docblock descriptions and
  this file itself.

- [TS-37: Web Platform APIs](../037/AGENTS.md):
  Read this when writing browser-targeted code — DOM/web API usage, feature
  detection specifics.

- [TS-38: Node.js Applications](../038/AGENTS.md):
  Read this when building a Node.js application (not just a library) —
  application-level runtime, deployment, and process conventions.

- [TS-47: Dates and Times](../047/AGENTS.md):
  Read this when handling dates, times, or timezones beyond basic `Date`
  validation.

- [TS-52: Security and Secrets Management](../052/AGENTS.md):
  Read this when auditing or adding third-party dependencies.

- [TS-12: Quality Assurance](../012/AGENTS.md) and
  [TS-13: Functional Testing](../013/AGENTS.md):
  Read these when designing a test strategy beyond unit-test mechanics.

- [JSDoc](https://jsdoc.app/) and [TSDoc](https://tsdoc.org/):
  Read these when the tag/type syntax needed for a docblock isn't covered
  above.
