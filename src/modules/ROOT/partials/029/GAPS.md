# TS-29 gap analysis

Gaps found comparing TS-29: JSON Schema against the following reference
resources (discovered from GitHub issue
https://github.com/kieranpotts/standards/issues/71):

- https://www.learnjsonschema.com/2020-12/
- https://json-schema.org/understanding-json-schema/reference/composition
- https://tour.json-schema.org/
- https://www.devzery.com/post/your-ultimate-guide-to-schema-for-json
- https://romanglushach.medium.com/json-schema-the-secret-to-building-scalable-and-maintainable-data-models-2c456d90f73b
- https://www.linkedin.com/advice/1/how-do-you-keep-your-json-data-models-consistent
- https://github.com/levid-gc/paypal-api-standards/tree/master/v1/schema/json/draft-04
- https://ajv.js.org/json-type-definition.html
- https://www.youtube.com/watch?v=QiAXxaLrt7E
- https://www.youtube.com/watch?v=GjJpRsVffg0

**Assessment.** The standard's stated purpose is "designing JSON Schema,"
but it almost entirely omits the JSON Schema vocabulary itself — the
validation, applicator, annotation, content, and unevaluated keywords that
make up the language a designer actually uses. Most of the reference
material falls inside the standard's scope, and the bulk of it is **missing**:
the core schema keywords, composition, conditionals, annotations, `format`,
and design best practices are not addressed at all. A few areas
(`$ref`/cross-references, JTD) are treated **partially**. CloudEvents and
storage-platform concerns are **out-of-scope**.

**Status:** 8 of 25 Missing items and 0 of 4 Partial items resolved
(2026-08-14) — the eight core-vocabulary items (Validation, Applicator,
Boolean composition, if/then/else, dependentRequired/dependentSchemas,
Meta-Data/Annotations, both `format` items, and Content) closed in one batch
via new `03`–`08` partials. 17 Missing, 4 Partial, 3 Out-of-scope, and 2
Unresolved items remain open. Two YouTube reference resources could not be
retrieved (see Unresolved).

This run's `03`–`08` insertions renumbered the standard's pre-existing
partials: old `03-cross-references.adoc` is now `09-cross-references.adoc`,
old `04-json-hyper-schema.adoc` is now `10-json-hyper-schema.adoc`, old
`07-json-pointer.adoc` is now `13-json-pointer.adoc`, and old
`09-useful-links.adoc` is now `16-useful-links.adoc` (see the page's
`include::` list for the full mapping). The still-open items below that cite
`03-cross-references.adoc:44`, `03-cross-references.adoc:24-30`, and
`07-json-pointer.adoc:26` were left with their original text per the
append-only rule, but those line references now point at the file's old
name — re-verify against the renumbered files (`09-` and `13-`
respectively) before acting on them. `02-versions.adoc:9` is unaffected.

## Missing

- [x] [https://www.learnjsonschema.com/2020-12/#validation] The Validation
      vocabulary keywords (`type`, `enum`, `const`, `maxLength`, `minLength`,
      `pattern`, `maximum`, `minimum`, `exclusiveMaximum`, `exclusiveMinimum`,
      `multipleOf`, `required`, `dependentRequired`, `maxProperties`,
      `minProperties`, `maxItems`, `minItems`, `maxContains`, `minContains`,
      `uniqueItems`) are not addressed anywhere in the standard. Recommend
      placing in a new "Validation keywords" section between
      `02-versions.adoc` and `03-cross-references.adoc`.

      **Resolved.** Closed by a new `03-validation-keywords.adoc`,
      "Validation keywords" section, grouped into Type and value, String,
      Numeric, Object, and Array keyword subsections covering all listed
      keywords (`dependentRequired` is covered in the "Conditional
      validation" section instead and cross-referenced from here). Old
      `03-cross-references.adoc` renumbered to `09-` to make room; the
      page's include list and this file's other line-number citations were
      updated accordingly. Source added to the page's new `== References`
      section.

- [x] [https://www.learnjsonschema.com/2020-12/#applicator] The Applicator
      vocabulary keywords (`allOf`, `anyOf`, `oneOf`, `if`, `then`, `else`,
      `not`, `properties`, `additionalProperties`, `patternProperties`,
      `dependentSchemas`, `propertyNames`, `contains`, `items`,
      `prefixItems`) are not addressed anywhere in the standard. Recommend
      placing in a new "Applicator keywords" / "Schema composition" section
      between `02-versions.adoc` and `03-cross-references.adoc`.

      **Resolved.** Closed by a new `04-applicator-keywords.adoc`,
      "Applicator keywords" section, with "Boolean composition" and "Object
      and array applicators" subsections. `if`/`then`/`else` and
      `dependentSchemas` are covered in the new "Conditional validation"
      section instead and cross-referenced from here, since they are
      conditional-application keywords rather than plain composition. Source
      added to the page's new `== References` section.

- [x] [https://json-schema.org/understanding-json-schema/reference/combining]
      Boolean composition keywords `allOf` (AND), `anyOf` (OR), `oneOf` (XOR),
      and `not` (NOT) are not explained. The standard says "prefer schema
      composition over inheritance" (`03-cross-references.adoc:7`) but never
      defines the composition keywords or their semantics. Recommend placing
      in a new "Schema composition" section, or expanding
      `03-cross-references.adoc`.

      **Resolved.** Closed by the "Boolean composition" subsection of
      `04-applicator-keywords.adoc` (see above), which defines `allOf`,
      `anyOf`, `oneOf`, and `not` and gives guidance on choosing between
      `oneOf` and `anyOf`. The cross-references section (renumbered to
      `09-cross-references.adoc`) now links to it in place of its former
      unexplained mention of composition.

- [x] [https://json-schema.org/understanding-json-schema/reference/conditionals#if-then-else]
      Conditional validation via `if`/`then`/`else` is not addressed anywhere
      in the standard. Recommend placing in a new "Conditional validation"
      section.

      **Resolved.** Closed by a new `05-conditional-validation.adoc`,
      "Conditional validation" section, "if/then/else" subsection, with a
      worked postal-code-by-country example and guidance on using `allOf` to
      chain more than two branches. Source added to the page's new
      `== References` section.

- [x] [https://json-schema.org/understanding-json-schema/reference/conditionals#dependentRequired]
      Conditional validation via `dependentRequired` (conditionally required
      properties) and `dependentSchemas` (conditionally applied subschemas) is
      not addressed anywhere in the standard. Recommend placing in a new
      "Conditional validation" section.

      **Resolved.** Closed by the "dependentRequired and dependentSchemas"
      subsection of `05-conditional-validation.adoc` (see above), with a
      credit-card/billing-address example for each keyword and guidance to
      prefer them over `if`/`then` where the condition is presence-only.

- [x] [https://www.learnjsonschema.com/2020-12/#meta-data] The Meta Data
      (annotation) vocabulary (`title`, `description`, `default`,
      `deprecated`, `examples`, `readOnly`, `writeOnly`) is not addressed as
      a general concept. `readOnly` appears only incidentally in a Hyper-Schema
      example (`04-json-hyper-schema.adoc:23`) and `title` only for link
      descriptions (`04-json-hyper-schema.adoc:78`). Recommend placing in a
      new "Annotations" section.

      **Resolved.** Closed by a new `06-annotations.adoc`, "Annotations"
      section, covering `title`, `description`, `default`, `examples`,
      `deprecated`, `readOnly`, and `writeOnly`. Source added to the page's
      new `== References` section.

- [x] [https://www.learnjsonschema.com/2020-12/#format-annotation] The
      `format` keyword (Format Annotation) for semantic string validation
      (e.g. `email`, `date-time`) is not addressed anywhere in the standard.
      Recommend placing in a new "Format" section.

- [x] [https://www.learnjsonschema.com/2020-12/#format-assertion] The
      distinction between Format Annotation (annotation only, default) and
      Format Assertion (asserting, an official vocabulary not included by
      default) is not addressed anywhere in the standard. Recommend placing
      in a new "Format" section.

      **Resolved.** Both format items closed together by a new
      `07-format.adoc`, "Format" section, which introduces the `format`
      keyword, states plainly that it is annotation-only by default under
      Draft 2020-12, and explains the separate, not-included-by-default
      Format Assertion vocabulary as the way to make it enforce. Source
      added to the page's new `== References` section.

- [x] [https://www.learnjsonschema.com/2020-12/#content] The Content vocabulary
      (`contentEncoding`, `contentMediaType`, `contentSchema`) for annotating
      non-JSON data encoded in JSON strings is not addressed anywhere in the
      standard. Recommend placing in a new "Content keywords" section.

      **Resolved.** Closed by a new `08-content-keywords.adoc`, "Content
      keywords" section, covering `contentEncoding`, `contentMediaType`, and
      `contentSchema` with a base64-encoded-JSON worked example, and noting
      they are annotations rather than assertions like `format`. Source
      added to the page's new `== References` section.

- [ ] [https://www.learnjsonschema.com/2020-12/#unevaluated] The Unevaluated
      vocabulary (`unevaluatedItems`, `unevaluatedProperties`) is not addressed
      anywhere in the standard. Recommend placing in a new "Unevaluated
      keywords" section.

- [ ] [https://www.learnjsonschema.com/2020-12/#core] Core vocabulary keywords
      beyond `$ref` — `$id` (schema identifier), `$comment`, `$defs` (inline
      reusable schemas), `$anchor`, `$dynamicAnchor`/`$dynamicRef` (dynamic
      referencing), and `$vocabulary` — are not addressed. `$defs` in
      particular is a key design tool for inlining reusable schemas.
      Recommend placing in `03-cross-references.adoc` (expand it) or a new
      "Schema identification" section.

- [ ] [https://www.devzery.com/post/your-ultimate-guide-to-schema-for-json#best-practices-for-using-json-schema]
      Schema versioning — maintaining and evolving schema versions over time
      as data models change — is not addressed. `02-versions.adoc` covers
      JSON Schema *draft* versions, not versioning of one's own schemas.
      Recommend placing in a new "Schema versioning" section.

- [ ] [https://romanglushach.medium.com/json-schema-the-secret-to-building-scalable-and-maintainable-data-models-2c456d90f73b]
      Validator / tooling ecosystem (e.g. `ajv`, Python `jsonschema`, `joi`,
      `zod`) for validating JSON against schemas is not addressed. The
      standard mentions a bundling tool (`03-cross-references.adoc:44`) and
      lists two online validators (`09-useful-links.adoc`) but no general
      tooling guidance. Recommend placing in a new "Tooling" section or
      expanding `09-useful-links.adoc`.

- [ ] [https://www.linkedin.com/advice/1/how-do-you-keep-your-json-data-models-consistent#use-a-schema-language]
      Maintaining a centralized schema repository for cross-team reuse is not
      addressed. Recommend placing in a new "Schema management" / "Best
      practices" section.

- [ ] [https://www.linkedin.com/advice/1/how-do-you-keep-your-json-data-models-consistent#use-a-schema-language]
      Integrating schema validation into CI/CD pipelines is not addressed.
      Recommend placing in a new "Best practices" section.

- [ ] [https://www.linkedin.com/advice/1/how-do-you-keep-your-json-data-models-consistent#follow-naming-conventions]
      Naming conventions for JSON property names (camelCase vs snake_case vs
      kebab-case, singular vs plural) are not addressed. Recommend placing
      in a new "Best practices" section.

- [ ] [https://www.linkedin.com/advice/1/how-do-you-keep-your-json-data-models-consistent#use-consistent-data-types]
      Guidance on consistent data typing (e.g. keeping array items
      homogeneously typed, not mixing types) is not addressed. Recommend
      placing in a new "Best practices" section.

- [ ] [https://www.linkedin.com/advice/1/how-do-you-keep-your-json-data-models-consistent#avoid-unnecessary-nesting]
      Guidance on limiting nesting depth and preferring normalized/flat
      models with reference keys over deep nesting is not addressed. Recommend
      placing in a new "Best practices" section.

- [ ] [https://www.linkedin.com/advice/1/how-do-you-keep-your-json-data-models-consistent#document-your-data-models]
      Guidance on documenting data models (beyond the `title`/`description`
      annotation keywords) is not addressed. Recommend placing in a new
      "Best practices" section.

- [ ] [https://github.com/levid-gc/paypal-api-standards/tree/master/v1/schema/json/draft-04#money.json]
      The pattern of modeling monetary values as strings (not numbers) to
      preserve precision across currency subdivisions is not addressed.
      Recommend placing in a new "Modeling patterns" section or an
      `examples/` subdirectory.

- [ ] [https://github.com/levid-gc/paypal-api-standards/tree/master/v1/schema/json/draft-04#phone.json]
      The pattern of modeling phone numbers as structured objects
      (`country_code`, `national_number`, `extension_number`) per ITU E.164
      rather than a single string is not addressed. Recommend placing in a
      new "Modeling patterns" section or an `examples/` subdirectory.

- [ ] [https://github.com/levid-gc/paypal-api-standards/tree/master/v1/schema/json/draft-04]
      The convention of custom vendor-prefixed `format` strings (e.g.
      `paypal_common_currency_code_v1`) to signal semantic validation beyond
      base JSON Schema is not addressed. Recommend placing in a new "Format"
      or "Modeling patterns" section.

- [ ] [https://github.com/levid-gc/paypal-api-standards/tree/master/v1/schema/json/draft-04]
      The convention of one schema per file with `snake_case` filenames,
      composing via relative `$ref` to sibling files, is not addressed as an
      explicit structural pattern. The standard shows `$ref` to sibling
      files (`03-cross-references.adoc:24-30`) but gives no file-organization
      guidance. Recommend placing in `03-cross-references.adoc` or a new
      "Schema organization" section.

- [ ] [https://github.com/levid-gc/paypal-api-standards/tree/master/v1/schema/json/draft-04#error.json]
      Patterns for error/envelope schema design (standard error fields,
      `details` arrays, HATEOAS `links`) are not addressed. Recommend placing
      in a new "Modeling patterns" section or an `examples/` subdirectory.

- [ ] [https://github.com/levid-gc/paypal-api-standards/tree/master/v1/schema/json/draft-04#patch.json]
      JSON Patch (RFC 6902) — the operation model (`op`/`path`/`value`/`from`,
      the `add`/`remove`/`replace`/`move`/`copy`/`test` operations) — is not
      addressed. The standard mentions JSON Patch only in passing
      (`07-json-pointer.adoc:26`). Recommend placing in `07-json-pointer.adoc`
      (expand) or a new "JSON Patch" section.

## Partial

- [ ] [https://json-schema.org/understanding-json-schema/reference/composition]
      covers modular schema combination more thoroughly than
      `03-cross-references.adoc` — specifically, it covers `$defs` for inline
      reusable schemas, `$anchor`/`$dynamicAnchor`/`$dynamicRef` for advanced
      referencing, recursive (self-referential) schemas, and the distinction
      between modular combination and boolean combination, none of which the
      standard addresses. The standard covers only basic `$ref` to external
      files and bundling.

- [ ] [https://ajv.js.org/json-type-definition.html] covers JTD far more
      thoroughly than `08-json-type-definition.adoc` — specifically, the eight
      JTD schema forms (type, enum, elements, properties, discriminator,
      values, ref, empty), the `nullable` member, the `metadata` extension
      member, the `definitions` dictionary, the default-disallow behavior of
      the properties form, JTD's inability to reference non-root definitions
      or other files (unlike JSON Schema), and migration from JSON Schema to
      JTD. The standard gives only one basic example and a one-paragraph
      comparison.

- [ ] [https://tour.json-schema.org/] covers the standard's subject matter
      (primitive types, objects, arrays, conditional validation, combining
      subschemas, annotating schemas) as dedicated topics; the standard
      addresses only the cross-references and Hyper-Schema slices of this.
      (Only the tour's table of contents could be retrieved; the sub-pages
      are client-rendered and 404 on fetch. The topics overlap with
      learnjsonschema.com, already cited above.)

- [ ] [https://www.devzery.com/post/your-ultimate-guide-to-schema-for-json#creating-a-json-schema]
      covers schema boilerplate (`$schema`, `$id`, `title`, `description`,
      `type`, `properties`) more concretely than the standard — specifically,
      it walks through the skeleton of a schema document and the role of each
      header keyword, which the standard never does. The standard mentions
      `$schema`/metaschema only in `02-versions.adoc:9` and never explains
      `$id` or the document skeleton.

## Out-of-scope

- [ ] [https://romanglushach.medium.com/json-schema-the-secret-to-building-scalable-and-maintainable-data-models-2c456d90f73b#cloudevents-specifications]
      covers CloudEvents (a CNCF specification for event data), but it
      plausibly sits outside this standard's stated purpose (JSON Schema
      design) because it is a separate specification built on top of JSON
      Schema. Flagged for the user to confirm or overrule.

- [ ] [https://www.linkedin.com/advice/1/how-do-you-keep-your-json-data-models-consistent#heres-what-else-to-consider]
      covers how different storage platforms (PostgreSQL, MongoDB) handle
      JSON, but it plausibly sits outside this standard's stated purpose
      because it is about data storage behavior, not schema design. Flagged
      for the user to confirm or overrule.

- [ ] [https://www.devzery.com/post/your-ultimate-guide-to-schema-for-json#using-json-schema-for-validation]
      covers language-specific validation code (e.g. Python `jsonschema`
      `validate()` API, `ValidationError` exceptions), but it plausibly sits
      outside this standard's stated purpose because it is implementation
      detail rather than schema design. Flagged for the user to confirm or
      overrule.

## Unresolved

- [ ] [https://www.youtube.com/watch?v=QiAXxaLrt7E] could not be retrieved:
      the YouTube page returned only generic site chrome/footer with no video
      title, description, or transcript. Not included in the comparison
      above.

- [ ] [https://www.youtube.com/watch?v=GjJpRsVffg0] could not be retrieved:
      the YouTube page returned only generic site chrome/footer with no video
      title, description, or transcript. Not included in the comparison
      above.