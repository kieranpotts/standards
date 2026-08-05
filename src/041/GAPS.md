# TS-41 gap analysis

Gaps found comparing TS-41: React against the following reference
resources (sourced from GitHub issue
[#56](https://github.com/kieranpotts/standards/issues/56)):

- https://thetshaped.dev/p/the-styling-dilemma-in-react
- https://www.twilio.com/en-us/blog/react-choose-functional-components
- https://overreacted.io/how-are-function-components-different-from-classes/
- https://overreacted.io/writing-resilient-components/
- https://overreacted.io/before-you-memo/
- https://overreacted.io/the-wet-codebase/
- https://overreacted.io/goodbye-clean-code/
- https://overreacted.io/the-two-reacts/
- https://petarivanovv9.gumroad.com/l/jqcuh

**Assessment.** The standard is narrow — it covers only four topics
(imports, prop spreading, the state-setter callback API, and filesystem
layout) and is silent on most of what the references discuss. The bulk of
the reference material falls inside the standard's stated scope (React
component best practices) and is missing entirely: styling, functional
vs class components, effects/refs/reducers, the "resilient components"
design principles, and performance optimization. Two overreacted posts
are general software-design philosophy (WET codebase, clean code) and
sit outside scope; the Server Components mental model is a closer call
but flagged out-of-scope given the standard's component-implementation
focus.

**Status:** First run (2026-08-05). All gaps below are open.

## Missing

- [ ] [thetshaped.dev/p/the-styling-dilemma-in-react](https://thetshaped.dev/p/the-styling-dilemma-in-react)
      surveys CSS styling strategies for React (vanilla CSS, SASS/SCSS,
      Tailwind, CSS Modules, CSS-in-JS runtime vs compile-time) with
      pros/cons and a recommendation toward classless, locality-of-
      behavior approaches. The standard has no styling guidance at all.
      Recommend a new section.

- [ ] [twilio.com/.../react-choose-functional-components](https://www.twilio.com/en-us/blog/react-choose-functional-components)
      argues for preferring functional components over class components
      (shorter, simpler, easier to test, avoids `this` confusion) while
      noting no need to rewrite existing class components. The standard
      uses function components in examples but never states a preference
      or rationale. Recommend a new section (near
      `01-importing-react.adoc:1`).

- [ ] [twilio.com/.../react-choose-functional-components#lifecycle-methods](https://www.twilio.com/en-us/blog/react-choose-functional-components)
      maps class lifecycle methods to `useEffect` (`componentDidMount` →
      `useEffect` with `[]`; `componentWillUnmount` → effect cleanup
      return) and notes `componentWillMount` is legacy. The standard does
      not cover effects or lifecycle equivalents. Recommend a new
      section.

- [ ] [overreacted.io/how-are-function-components-different-from-classes](https://overreacted.io/how-are-function-components-different-from-classes/)
      explains that function components capture rendered values via
      closures (props/state per render), in contrast to classes reading
      mutable `this`. The standard's state section (`03-state.adoc:1`)
      covers the setter callback API but omits the capture/closure
      semantics that motivate it. Recommend extending
      `03-state.adoc` or a new section.

- [ ] [overreacted.io/how-are-function-components-different-from-classes](https://overreacted.io/how-are-function-components-different-from-classes/)
      introduces `useRef` as the escape hatch for mutable values that
      mirror class instance fields (`this.something` ↔
      `something.current`), including the guidance to avoid reading/
      setting refs during render and to update them in effects. The
      standard never mentions refs. Recommend a new section.

- [ ] [overreacted.io/how-are-function-components-different-from-classes](https://overreacted.io/how-are-function-components-different-from-classes/)
      and [writing-resilient-components#don-t-stop-the-data-flow-in-side-effects](https://overreacted.io/writing-resilient-components/)
      cover `useEffect` dependency arrays: functions/props/state must not
      be omitted from the dependency array, stale-closure bugs arise
      from that mistake, and the `exhaustive-deps` lint rule
      (`eslint-plugin-react-hooks`) validates consistency. The standard
      has nothing on effect dependencies. Recommend a new section.

- [ ] [overreacted.io/how-are-function-components-different-from-classes](https://overreacted.io/how-are-function-components-different-from-classes/)
      recommends `useReducer` as often a better solution than the
      `useRef`-to-track-latest pattern for state logic that gets complex.
      The standard does not cover reducers. Recommend a new section
      (near `03-state.adoc`).

- [ ] [writing-resilient-components#don-t-stop-the-data-flow-in-rendering](https://overreacted.io/writing-resilient-components/)
      warns against copying props into state (which ignores updates) and
      says to name the prop `initialColor`/`defaultColor` when ignoring
      updates is intentional. The standard has no guidance on this. New
      section.

- [ ] [writing-resilient-components#don-t-stop-the-data-flow-in-rendering](https://overreacted.io/writing-resilient-components/)
      recommends `useMemo` for expensive computations derived from props
      rather than copying computed values into state. The standard does
      not cover memoization of computations. New section.

- [ ] [writing-resilient-components#don-t-stop-the-data-flow-in-optimizations](https://overreacted.io/writing-resilient-components/)
      recommends `React.memo` with default shallow comparison over
      manual `shouldComponentUpdate`/custom comparators, and warns that
      custom comparators must not skip function props. The standard does
      not cover render optimization via memo. New section.

- [ ] [writing-resilient-components#don-t-stop-the-data-flow-in-optimizations](https://overreacted.io/writing-resilient-components/)
      recommends `useCallback`/`useContext` to avoid passing functions
      deep through the tree (stable identity without manual memoization).
      The standard does not cover these hooks. New section.

- [ ] [writing-resilient-components#principle-2-always-be-ready-to-render](https://overreacted.io/writing-resilient-components/)
      says components must be resilient to re-rendering more or less
      often: avoid `componentWillReceiveProps`, avoid derived state, and
      prefer either fully controlled components or fully uncontrolled
      components reset via the `key` prop. The standard has no guidance
      here. New section.

- [ ] [writing-resilient-components#principle-3-no-component-is-a-singleton](https://overreacted.io/writing-resilient-components/)
      says not to assume a component renders once (test by rendering the
      app twice) and not to reset global state on mount/unmount, since
      showing/hiding a tree shouldn't break components outside it. The
      standard does not address this. New section.

- [ ] [writing-resilient-components#principle-4-keep-the-local-state-isolated](https://overreacted.io/writing-resilient-components/)
      gives the test "if this component were rendered twice, should this
      interaction reflect in the other copy?" to decide what is truly
      local state, and says not to hoist local state higher than
      necessary. The standard's state section (`03-state.adoc:1`) does
      not address state placement/locality. New section (near
      `03-state.adoc`).

- [ ] [before-you-memo#solution-1-move-state-down](https://overreacted.io/before-you-memo/)
      shows moving state down into a child component so an expensive
      sibling subtree doesn't re-render on state changes. The standard
      has no performance-optimization guidance. New section.

- [ ] [before-you-memo#solution-2-lift-content-up](https://overreacted.io/before-you-memo/)
      shows passing an expensive subtree as the `children` prop from a
      parent so a stateful wrapper's re-renders skip it. The standard
      does not cover this composition-for-performance pattern. New
      section.

- [ ] [before-you-memo](https://overreacted.io/before-you-memo/)
      recommends, before reaching for `memo`/`useMemo`, verifying a
      production build, checking state isn't hoisted too high, and using
      the React DevTools Profiler. The standard has no performance-
      investigation guidance. New section.

## Partial

- [ ] [twilio.com/.../react-choose-functional-components#handling-state](https://www.twilio.com/en-us/blog/react-choose-functional-components)
      covers `useState` more thoroughly than `03-state.adoc:1` —
      specifically, it shows basic `useState` usage and initial-state
      typing, and contrasts with the class `this.state`/`setState` model,
      which the standard omits entirely (it only covers the setter
      callback convention).

- [ ] [thetshaped.dev/p/the-styling-dilemma-in-react](https://thetshaped.dev/p/the-styling-dilemma-in-react)
      covers dynamic/prop-driven styling (CSS-in-JS enables styling from
      component props; vanilla CSS and CSS Modules have limited support
      for it). The standard's prop-spreading pattern
      (`02-wrapping-native-elements.adoc:1`) passes props to native
      elements but never connects props to styling, so the
      props-to-styles relationship is only partially implied.

## Out-of-scope

- [ ] [overreacted.io/the-wet-codebase](https://overreacted.io/the-wet-codebase/)
      is a conference talk on how strict DRY adherence produces
      incomprehensible software — general software-design philosophy,
      not React-specific. Sits under TS-7 (Code Design). Flagged for the
      user to confirm.

- [ ] [overreacted.io/goodbye-clean-code](https://overreacted.io/goodbye-clean-code/)
      is a personal essay on over-abstraction and clean-code zealotry —
      general software-engineering philosophy, not React-specific. Sits
      under TS-7 (Code Design). Flagged for the user to confirm.

- [ ] [twilio.com/.../react-choose-functional-components](https://www.twilio.com/en-us/blog/react-choose-functional-components)
      covers basic JSX rendering syntax and how to pass props
      (`<Component name="Shiori" />`, destructuring). This is
      introductory/tutorial material; per the project AGENTS.md the
      standards are "reference material, not tutorials." Flagged for the
      user to confirm.

- [ ] [writing-resilient-components#don-t-get-distracted-by-imaginary-problems](https://overreacted.io/writing-resilient-components/)
      discusses general lint-config hygiene (remove rules that never
      caught a bug) and using Prettier for formatting rather than lint —
      general tooling guidance, not React-specific. The React-specific
      `exhaustive-deps` rule is captured under the effects gap above.
      Flagged for the user to confirm.

- [ ] [overreacted.io/the-two-reacts](https://overreacted.io/the-two-reacts/)
      lays out the React Server Components mental model
      (`UI = f(data, state)`, client vs server component environments,
      the `"use client"` boundary). The standard's stated scope is
      "composing graphical web user interfaces from reusable components"
      and its current content is component-implementation patterns with
      no treatment of rendering environments or architecture. Likely
      belongs in a separate standard. Flagged for the user to confirm or
      overrule.

## Unresolved

- [ ] [petarivanovv9.gumroad.com/l/jqcuh](https://petarivanovv9.gumroad.com/l/jqcuh)
      could not be retrieved — the Gumroad product page is JavaScript-
      rendered and the fetch returned no textual content. The product
      appears to be a paid ebook/resource by Petar Ivanov (author of the
      T-Shaped Dev styling article above), but its contents could not be
      verified and were not included in the comparison.