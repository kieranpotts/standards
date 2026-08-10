# TS-34: PHP

PHP coding standards for projects that use PHP. The
[PER Coding Style v2.0](https://www.php-fig.org/per/coding-style/) is the
definitive standard for PHP coding style; this standard summarizes and extends
it, but where it is silent, PER Coding Style is authoritative.

Use this when writing, reviewing, or refactoring PHP code.

Do NOT use this for non-PHP languages. See
[TS-33: Java](../033/AGENTS.md), [TS-35: Python](../035/AGENTS.md), or
[TS-36: ECMAScript](../036/AGENTS.md) for other languages. For general code
design principles applicable to any language, see
[TS-7: Code Design](../007/AGENTS.md). For QA and linting policy, see
[TS-12: Quality Assurance](../012/AGENTS.md).

## Rules

### Linting

- **Use automated static analysis.** It is RECOMMENDED to use automated static
  analysis tools, with automatic code fixing enabled where available, to
  enforce consistent coding standards.

### Type hinting

- **Type everything you can.** Class properties, method parameters, and
  method return types SHOULD be typed. Type hinting is optional in PHP but
  strongly RECOMMENDED.

```php
function sum(int $a, int $b): int {
  return $a + $b;
}
```

- **Enable strict mode.** It is strongly RECOMMENDED to opt-in to strict type
  checking by adding the following to the beginning of every PHP file:

```php
declare(strict_types=1);
```

- **Nullable types.** Use `?Type` to indicate a value MAY be `null` in
  addition to the declared type (PHP 7.1+).

- **Use the `void` return type.** Although PHP does not require it, it is
  RECOMMENDED to declare `void` return types wherever a function does not
  return a value.

- **Do not repeat native types in docblocks.** Where extended type hints are
  provided via phpdoc, the docblocks MUST NOT repeat native type declarations —
  this is redundant.

- **Use static analysis tools to fill type-system gaps.** PHP cannot express
  the types held in arrays or iterables, nor the parameters and return types
  of `callable`s. It is RECOMMENDED to use static analysis tools (eg. phpstan)
  that understand phpdoc annotations like `array<int, MyObject>` to enforce
  stricter type checking for these cases.

- **Prefer custom typed array classes.** For non-trivial list-like
  structures, the optimal solution is to define custom array-like value
  objects (extending `ArrayObject` / `ArrayIterator`, or implementing
  `ArrayAccess` and `IteratorAggregate`) that enforce their element type
  via constructor variadic params or `offsetSet` checks.

```php
class Users extends ArrayIterator
{
    public function __construct(User ...$users)
    {
        parent::__construct($users);
    }

    public function current(): User
    {
        return parent::current();
    }
}
```

- **Document complex callables in phpdoc.** PHP cannot express the parameter
  or return types of a `callable`; for complex callable signatures, the
  signature SHOULD be documented in phpdoc.

- **Avoid union types.** Union types (PHP 8+) SHOULD be avoided. Ideally all
  variables SHOULD encapsulate a single discrete data type, OPTIONALLY
  `null`.

### Magic methods

- **Avoid magic methods in application code.** Application code SHOULD avoid
  using magic methods wherever possible. They make code less explicit and
  harder to understand. Prefer more direct execution of framework-level logic
  and define class methods explicitly. (Some framework internals rely on
  magic methods; this rule concerns application code, not framework code.)

### Exceptions

- **Catch and rethrow to make exceptions meaningful.** Catch-and-rethrow
  patterns SHOULD be used to make exceptions more meaningful. Exceptions
  SHOULD be allowed to bubble up, perhaps unmodified, until they are relevant
  to the current level of abstraction. This also avoids unnecessary
  disclosure of information about modules underlying the abstraction.

```php
/**
 * @throws UserNotFoundException
 */
public function getUser($username)
{
    try {
        $user = $db->query('SELECT ...', $username);
    } catch (DatabaseException $e) {
        throw new UserNotFoundException();
    }
    return $user;
}
```

### phpDoc

- **Document explicitly thrown exceptions with `@throws`.** Where a method
  _explicitly_ throws something, the thrown type MUST be documented with an
  `@throws` annotation.

- **Do not propagate `@throws` from callees.** Authors MUST NOT use `@throws`
  annotations on caller functions to document exception types that may be
  thrown by callee functions, unless the caller catches and rethrows those
  exceptions. Only exception types that are _relevant to the current
  abstraction level_ are documented.

## References

- [TS-34: PHP (source)](../../pages/034-php.adoc)
- [TS-7: Code Design](../007/AGENTS.md)
- [TS-12: Quality Assurance](../012/AGENTS.md)
- [TS-33: Java](../033/AGENTS.md)
- [TS-35: Python](../035/AGENTS.md)
- [TS-36: ECMAScript](../036/AGENTS.md)
- [PER Coding Style v2.0](https://www.php-fig.org/per/coding-style/)
- [phpstan phpdoc types](https://phpstan.org/writing-php-code/phpdoc-types)
