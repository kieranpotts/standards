# TS-41: React

Best practices for working with React, the JavaScript library for composing
graphical web user interfaces from reusable components.

Use this when writing, reviewing, or refactoring React component code.

Do NOT use this for non-React web frameworks. See
[TS-42: Vue](../042/AGENTS.md) for Vue. For the underlying language, see
[TS-36: ECMAScript (JavaScript/TypeScript)](../036/AGENTS.md). For general web GUI principles, see
[TS-18: Web GUIs](../018/AGENTS.md). For general code design, see
[TS-7: Code Design](../007/AGENTS.md).

## Rules

### Importing React

- **Import the entire `react` package.** Although React v17+ no longer
  requires an explicit `import React from "react"`, it is RECOMMENDED to
  import the entire package and use the `React` namespace for all
  React-related imports. This makes React-related code easier to identify.

```jsx
import React from "react"

const [things, setThings] = React.useState([])
```

### Wrapping native elements

- **Spread props to wrapped native elements.** It is RECOMMENDED to use the
  spread operator to pass all props from React components to the underlying
  native elements they wrap. This lets consumers set any native HTML
  attribute; HTML ignores invalid attributes so there is no runtime risk.

```jsx
export default function Button({children, className, size, ...rest}) {
  let sizeClass
  if (size === "sm") sizeClass = "button-small"
  if (size === "lg") sizeClass = "button-large"
  return (
    <button className={`${sizeClass} ${className}`} {...rest}>
      {children}
    </button>
  )
}
```

- **Do not spread props for composite custom components.** The spread
  pattern is restricted to wrappers for single native HTML elements. It is
  NOT RECOMMENDED for custom components composed of multiple native
  elements or other components. In that case, props are part of the
  component's declarative API and SHOULD be explicitly defined.

### State

- **Use the callback API for state setters.** State setters SHOULD NOT
  directly pass new state values. They SHOULD use the callback API, which
  receives the current state value as its argument and returns the new
  value. This ensures the new state is based on the most recent state.

```jsx
const [count, setCount] = React.useState(0)

/* No: */
setCount(count++)

/* Yes: */
setCount(prevCount => prevCount - 1)
```

- **Name the callback argument `prev<Variable>`.** By convention, the name
  of the state setter callback's argument SHOULD be `prev` followed by the
  name of the state variable (eg. `prevCount`).

### Filesystem

- **Organize components to reflect hierarchy.** Components SHOULD be placed
  in directories that correspond to the component hierarchy. The following
  structure is RECOMMENDED as a starting point:

```
src/
├── assets/
├── elements/       # smallest building blocks (buttons, fields, icons)
│   └── calendar/
│       ├── components/
│       ├── types/
│       └── utils/
├── features/       # domain-oriented components (payments, auth)
│   ├── payments/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── mutations/
│   │   ├── queries/
│   │   ├── services/
│   │   ├── types/
│   │   ├── utils/
│   │   └── index.ts
│   └── auth/
├── views/          # top-level screens (no domain logic, may have UI logic)
└── tests/
```

- **Layer responsibilities:**
  - **Elements** are the smallest reusable building blocks (buttons, form
    fields, icons) plus larger composite but generic elements (calendar,
    data table, modal dialog).
  - **Features** are libraries of domain-specific components (payments,
    transactions, auth). They contain state management, data fetching, and
    business logic, composed of multiple elements.
  - **Views** are top-level components representing screens. They compose
    multiple features and elements and render the overall layout. Views
    SHOULD NOT contain domain-specific logic (that belongs in features) but
    MAY contain UI logic such as routing and navigation.

- **Colocate tests for large projects.** Tests MAY be colocated with the
  components they test, or placed in a separate top-level `tests/`
  directory. Colocation is RECOMMENDED for large, complex projects; a
  dedicated `tests/` directory works well only for smaller projects.

- **Follow the folder naming conventions:**

| Category   | Naming      | Examples                                            |
|------------|-------------|-----------------------------------------------------|
| API        | camelCase   | `registerAlert.ts`, `getAlerts.ts`                  |
| Queries    | camelCase   | `treeReasonByParentIdQuery.ts`                      |
| Components | PascalCase  | `Ticket.tsx`, `TicketList.tsx`, `TicketForm.tsx`   |
| Constants  | kebab-case  | `query-keys.ts`, `alert.constants.ts`               |
| Contexts   | PascalCase  | `AlertsContext.tsx`                                  |
| Hooks      | camelCase   | `useAlertMutation.ts`, `useAlertsQuery.ts`         |
| Views      | PascalCase  | `AlertScreen.tsx`                                   |
| Utils      | kebab-case  | `alert.utils.ts`                                     |
| Types      | kebab-case  | `alert.types.ts`                                     |

## References

- [TS-41: React (source)](../../pages/041.adoc)
- [TS-7: Code Design](../007/AGENTS.md)
- [TS-18: Web GUIs](../018/AGENTS.md)
- [TS-36: ECMAScript (JavaScript/TypeScript)](../036/AGENTS.md)
- [TS-42: Vue](../042/AGENTS.md)