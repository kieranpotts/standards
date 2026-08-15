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
but at the time of the original analysis it almost entirely omitted the
JSON Schema vocabulary itself — the validation, applicator, annotation,
content, and unevaluated keywords that make up the language a designer
actually uses. Most of the reference material fell inside the standard's
scope, and the bulk of it was **missing**: the core schema keywords,
composition, conditionals, annotations, `format`, and design best practices
were not addressed at all. A few areas (`$ref`/cross-references, JTD) were
treated **partially**. CloudEvents and storage-platform concerns are
**out-of-scope**. All Missing items are now resolved; see Status below.

**Status:** All 25 Missing items and all 4 Partial items resolved
(2026-08-14, across four batches, plus a follow-up decision pass). The
first batch closed the eight
core-vocabulary items (Validation, Applicator, Boolean composition,
if/then/else, dependentRequired/dependentSchemas, Meta-Data/Annotations,
both `format` items, and Content) via new `03`–`08` partials. The second
batch closed Unevaluated keywords, Core keywords (`$id`/`$comment`/`$defs`/
`$anchor`/`$dynamicAnchor`/`$dynamicRef`/`$vocabulary`), the
validator-tooling item, and JSON Patch (4 Missing), plus the composition and
schema-boilerplate Partial items, both closed by the same new "Schema
identification" section. The third batch closed Schema versioning and the
six LinkedIn best-practices items (7 Missing) via two new sections, plus the
JTD Partial item by extending the existing JTD partial. This fourth batch
closed the four remaining PayPal-sourced Missing items (monetary values,
phone numbers, vendor-prefixed `format`, error/envelope schemas, and
file-organization) — the user chose a new prose "Modeling patterns" section
over an `examples/` subdirectory for the four not already tied to an
existing file — and, on the user's confirmation, closed all three
Out-of-scope items: CloudEvents and storage-platform concerns confirmed
excluded outright (storage platforms flagged as a candidate for the
relational-databases standard's own gap analysis, not actioned here), and
validation-code APIs confirmed excluded from normative coverage but given a
one-sentence mention in `21-useful-links.adoc` at the user's request. In a
follow-up decision pass the same day, the last open Partial item
(`tour.json-schema.org`) was dismissed on the user's identification of the
source as an interactive playground rather than fetchable reference
material — its topics are in any case already covered via
learnjsonschema.com and json-schema.org. 0 Missing, 0 Partial, 0
Out-of-scope, and 2 Unresolved items remain open — both YouTube reference
resources, which could not be retrieved (see Unresolved).

Partials have now been renumbered four times. As of this run: old
`03-cross-references.adoc` is `11-cross-references.adoc` (now also carrying
a "File organization" subsection), old `04-json-hyper-schema.adoc` is
`12-json-hyper-schema.adoc`, old `07-json-pointer.adoc` is
`15-json-pointer.adoc` (now also carrying a "JSON Patch" subsection), old
`08-json-type-definition.adoc` (originally `14-json-type-definition.adoc`)
is `16-json-type-definition.adoc` (now also carrying four new JTD
subsections), and old `09-useful-links.adoc` is `21-useful-links.adoc` (now
also carrying a "Validator libraries" subsection) — see the page's
`include::` list for the full mapping. No open item below cites a
now-stale filename as of this run — the one that did
(`03-cross-references.adoc:24-30`, the file-organization item) is resolved
above, with the renumbering noted in its own resolution note.
`02-versions.adoc:9` is unaffected.

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

- [x] [https://www.learnjsonschema.com/2020-12/#unevaluated] The Unevaluated
      vocabulary (`unevaluatedItems`, `unevaluatedProperties`) is not addressed
      anywhere in the standard. Recommend placing in a new "Unevaluated
      keywords" section.

      **Resolved.** Closed by a new `06-unevaluated-keywords.adoc`,
      "Unevaluated keywords" section. Explains why `unevaluatedProperties`
      and `unevaluatedItems` see across composed subschemas where
      `additionalProperties`/`items` do not, with a worked `allOf`-extension
      example, and recommends `unevaluatedProperties: false` over
      `additionalProperties: false` wherever a schema is composed. Source
      added to the page's `== References` section. New file inserted as
      `06-`, renumbering every subsequent partial by two — see this file's
      top-level note and the page's `include::` list for the full mapping.

- [x] [https://www.learnjsonschema.com/2020-12/#core] Core vocabulary keywords
      beyond `$ref` — `$id` (schema identifier), `$comment`, `$defs` (inline
      reusable schemas), `$anchor`, `$dynamicAnchor`/`$dynamicRef` (dynamic
      referencing), and `$vocabulary` — are not addressed. `$defs` in
      particular is a key design tool for inlining reusable schemas.
      Recommend placing in `03-cross-references.adoc` (expand it) or a new
      "Schema identification" section.

      **Resolved.** Closed by a new `05-schema-identification.adoc`,
      "Schema identification" section, covering the document-skeleton role
      of `$schema`/`$id`, `$comment`, `$defs` (with a shared-address worked
      example), `$anchor`/`$dynamicAnchor`/`$dynamicRef` (with guidance to
      prefer plain `$ref`/`$anchor` and reserve dynamic referencing for
      schemas meant to be extended by others), and `$vocabulary`. This also
      closes the composition and schema-boilerplate items below, under
      Partial. Sources added to the page's `== References` section. New
      file inserted as `05-`, renumbering every subsequent partial by two.

- [x] [https://www.devzery.com/post/your-ultimate-guide-to-schema-for-json#best-practices-for-using-json-schema]
      Schema versioning — maintaining and evolving schema versions over time
      as data models change — is not addressed. `02-versions.adoc` covers
      JSON Schema *draft* versions, not versioning of one's own schemas.
      Recommend placing in a new "Schema versioning" section.

      **Resolved.** Closed by a new `17-schema-versioning.adoc`, "Schema
      versioning" section, distinguishing this from the draft versioning in
      <<Versions>>, defining backward-compatible vs. breaking changes, and
      recommending a new `$id` per breaking version plus a data-level
      `schemaVersion` field for persisted/transmitted data. Source added to
      the page's `== References` section.

- [x] [https://romanglushach.medium.com/json-schema-the-secret-to-building-scalable-and-maintainable-data-models-2c456d90f73b]
      Validator / tooling ecosystem (e.g. `ajv`, Python `jsonschema`, `joi`,
      `zod`) for validating JSON against schemas is not addressed. The
      standard mentions a bundling tool (`03-cross-references.adoc:44`) and
      lists two online validators (`09-useful-links.adoc`) but no general
      tooling guidance. Recommend placing in a new "Tooling" section or
      expanding `09-useful-links.adoc`.

      **Resolved.** Closed by a new "Validator libraries" subsection of
      `18-useful-links.adoc` (renumbered from `09-` — see this file's
      top-level note), listing `ajv` (JavaScript/TypeScript), `jsonschema`
      (Python), and `santhosh-tekuri/jsonschema` (Go), and recommending
      against `joi`/`zod` as JSON Schema substitutes since both define their
      own incompatible validation DSL. `09-cross-references.adoc:44`'s
      bundling-tool mention is unaffected — this item was about validation,
      not bundling. Source added to the page's `== References` section.

- [x] [https://www.linkedin.com/advice/1/how-do-you-keep-your-json-data-models-consistent#use-a-schema-language]
      Maintaining a centralized schema repository for cross-team reuse is not
      addressed. Recommend placing in a new "Schema management" / "Best
      practices" section.

      **Resolved.** Closed by the "Centralize shared schemas" subsection of
      a new `18-best-practices.adoc`, "Best practices" section (see the
      other five LinkedIn items below, all closed by the same file).
      Recommends a central repository of shared subschemas referenced by
      `$ref`, warning that independently-duplicated copies drift. Source
      added to the page's `== References` section.

- [x] [https://www.linkedin.com/advice/1/how-do-you-keep-your-json-data-models-consistent#use-a-schema-language]
      Integrating schema validation into CI/CD pipelines is not addressed.
      Recommend placing in a new "Best practices" section.

      **Resolved.** Closed by the "Validate in CI/CD" subsection of
      `18-best-practices.adoc` (see above), recommending automated
      validation of both schema documents and example payloads as a
      pipeline step, cross-referencing <<Schema versioning>> and
      <<Validator libraries>>.

- [x] [https://www.linkedin.com/advice/1/how-do-you-keep-your-json-data-models-consistent#follow-naming-conventions]
      Naming conventions for JSON property names (camelCase vs snake_case vs
      kebab-case, singular vs plural) are not addressed. Recommend placing
      in a new "Best practices" section.

      **Resolved.** Closed by the "Naming conventions" subsection of
      `18-best-practices.adoc` (see above), recommending one
      consistently-applied casing convention matched to the consuming
      ecosystem, and plural names for array-valued properties.

- [x] [https://www.linkedin.com/advice/1/how-do-you-keep-your-json-data-models-consistent#use-consistent-data-types]
      Guidance on consistent data typing (e.g. keeping array items
      homogeneously typed, not mixing types) is not addressed. Recommend
      placing in a new "Best practices" section.

      **Resolved.** Closed by the "Consistent data typing" subsection of
      `18-best-practices.adoc` (see above), recommending `items` or
      `prefixItems` (cross-referencing <<Applicator keywords>>) to enforce
      homogeneous array element types.

- [x] [https://www.linkedin.com/advice/1/how-do-you-keep-your-json-data-models-consistent#avoid-unnecessary-nesting]
      Guidance on limiting nesting depth and preferring normalized/flat
      models with reference keys over deep nesting is not addressed. Recommend
      placing in a new "Best practices" section.

      **Resolved.** Closed by the "Limit nesting depth" subsection of
      `18-best-practices.adoc` (see above), recommending a flatter,
      `$ref`-linked model for independently-meaningful entities, reserving
      nesting for data with no identity of its own, and noting the
      JSON-Patch cost of deep nesting.

- [x] [https://www.linkedin.com/advice/1/how-do-you-keep-your-json-data-models-consistent#document-your-data-models]
      Guidance on documenting data models (beyond the `title`/`description`
      annotation keywords) is not addressed. Recommend placing in a new
      "Best practices" section.

      **Resolved.** Closed by the "Document data models" subsection of
      `18-best-practices.adoc` (see above), recommending prose documentation
      alongside the schema for model-level intent that per-keyword
      annotations and `$comment` cannot carry. New file inserted as `18-`
      alongside `17-schema-versioning.adoc`; `17-references.adoc` and
      `18-useful-links.adoc` renumbered to `19-` and `20-` to make room —
      see this file's top-level note and the page's `include::` list.

- [x] [https://github.com/levid-gc/paypal-api-standards/tree/master/v1/schema/json/draft-04#money.json]
      The pattern of modeling monetary values as strings (not numbers) to
      preserve precision across currency subdivisions is not addressed.
      Recommend placing in a new "Modeling patterns" section or an
      `examples/` subdirectory.

      **Resolved.** Closed by the "Monetary values" subsection of a new
      `19-modeling-patterns.adoc`, "Modeling patterns" section (see the
      other three PayPal-sourced items below, all closed by the same
      file — placement as a prose section confirmed with the user rather
      than an `examples/` subdirectory). Explains the floating-point
      precision risk and recommends a string value paired with an ISO 4217
      currency code. Source added to the page's `== References` section.

- [x] [https://github.com/levid-gc/paypal-api-standards/tree/master/v1/schema/json/draft-04#phone.json]
      The pattern of modeling phone numbers as structured objects
      (`country_code`, `national_number`, `extension_number`) per ITU E.164
      rather than a single string is not addressed. Recommend placing in a
      new "Modeling patterns" section or an `examples/` subdirectory.

      **Resolved.** Closed by the "Phone numbers" subsection of
      `19-modeling-patterns.adoc` (see above), following ITU-T E.164's
      structure and recommending a free-form string only where the number
      is opaque to consumers. ITU-T E.164 added to the page's
      `== References` section alongside the PayPal source.

- [x] [https://github.com/levid-gc/paypal-api-standards/tree/master/v1/schema/json/draft-04]
      The convention of custom vendor-prefixed `format` strings (e.g.
      `paypal_common_currency_code_v1`) to signal semantic validation beyond
      base JSON Schema is not addressed. Recommend placing in a new "Format"
      or "Modeling patterns" section.

      **Resolved.** Closed by the "Vendor-prefixed `format` values"
      subsection of `19-modeling-patterns.adoc` (see above) rather than
      `09-format.adoc` — this is a design convention for using `format`,
      not an explanation of the keyword itself, which `09-format.adoc`
      already covers and cross-references from here. Notes the
      annotation-only default carries over from <<Format>>.

- [x] [https://github.com/levid-gc/paypal-api-standards/tree/master/v1/schema/json/draft-04]
      The convention of one schema per file with `snake_case` filenames,
      composing via relative `$ref` to sibling files, is not addressed as an
      explicit structural pattern. The standard shows `$ref` to sibling
      files (`03-cross-references.adoc:24-30`) but gives no file-organization
      guidance. Recommend placing in `03-cross-references.adoc` or a new
      "Schema organization" section.

      **Resolved.** Closed by extending `11-cross-references.adoc`
      (renumbered from `03-` — see this file's top-level note) with a new
      "File organization" subsection, rather than a new section — it is a
      direct extension of the file's existing `$ref`-to-sibling-file
      example. Source added to the page's `== References` section.

- [x] [https://github.com/levid-gc/paypal-api-standards/tree/master/v1/schema/json/draft-04#error.json]
      Patterns for error/envelope schema design (standard error fields,
      `details` arrays, HATEOAS `links`) are not addressed. Recommend placing
      in a new "Modeling patterns" section or an `examples/` subdirectory.

      **Resolved.** Closed by the "Error and envelope schemas" subsection of
      `19-modeling-patterns.adoc` (see above), with a worked
      `code`/`message`/`details`/`links` example. New file inserted as
      `19-`; `19-references.adoc` and `20-useful-links.adoc` (from the
      prior batch) renumbered to `20-` and `21-` — see this file's
      top-level note and the page's `include::` list.

- [x] [https://github.com/levid-gc/paypal-api-standards/tree/master/v1/schema/json/draft-04#patch.json]
      JSON Patch (RFC 6902) — the operation model (`op`/`path`/`value`/`from`,
      the `add`/`remove`/`replace`/`move`/`copy`/`test` operations) — is not
      addressed. The standard mentions JSON Patch only in passing
      (`07-json-pointer.adoc:26`). Recommend placing in `07-json-pointer.adoc`
      (expand) or a new "JSON Patch" section.

      **Resolved.** Closed by a new "JSON Patch" subsection of
      `15-json-pointer.adoc` (renumbered from `07-` — see this file's
      top-level note), citing RFC 6902 directly rather than the PayPal
      example (which does not itself explain the operation model), covering
      all six operations, the `-` end-of-array path segment, and
      recommending JSON Patch over an ad-hoc partial-update format for
      `PATCH` APIs. The existing passing mention now cross-references this
      section. Source added to the page's `== References` section.

## Partial

- [x] [https://json-schema.org/understanding-json-schema/reference/composition]
      covers modular schema combination more thoroughly than
      `03-cross-references.adoc` — specifically, it covers `$defs` for inline
      reusable schemas, `$anchor`/`$dynamicAnchor`/`$dynamicRef` for advanced
      referencing, recursive (self-referential) schemas, and the distinction
      between modular combination and boolean combination, none of which the
      standard addresses. The standard covers only basic `$ref` to external
      files and bundling.

      **Resolved.** Closed by `05-schema-identification.adoc` (see the Core
      vocabulary keywords item above, under Missing) — `$defs`, `$anchor`,
      `$dynamicAnchor`/`$dynamicRef`, and the plain-`$ref` recursive-schema
      case are all covered there. The modular-vs-boolean-combination
      distinction is covered across two sections: modular combination
      (`$ref`/`$defs`) in "Schema identification" and boolean combination
      (`allOf`/`anyOf`/`oneOf`/`not`) in the existing "Boolean composition"
      subsection of `04-applicator-keywords.adoc`, cross-referenced from
      each other. Source added to the page's `== References` section.

- [x] [https://ajv.js.org/json-type-definition.html] covers JTD far more
      thoroughly than `08-json-type-definition.adoc` — specifically, the eight
      JTD schema forms (type, enum, elements, properties, discriminator,
      values, ref, empty), the `nullable` member, the `metadata` extension
      member, the `definitions` dictionary, the default-disallow behavior of
      the properties form, JTD's inability to reference non-root definitions
      or other files (unlike JSON Schema), and migration from JSON Schema to
      JTD. The standard gives only one basic example and a one-paragraph
      comparison.

      **Resolved.** Closed by extending `16-json-type-definition.adoc`
      (renumbered from `14-`/`08-` — see this file's top-level note) with
      four new subsections: "Schema forms" (the eight forms and the
      properties form's stricter default), "`nullable` and `metadata`",
      "`definitions` and referencing" (including the no-cross-file-`$ref`
      limitation), and "Migrating from JSON Schema" (which source keywords
      have no JTD equivalent). Source added to the page's `== References`
      section.

- [x] [https://tour.json-schema.org/] covers the standard's subject matter
      (primitive types, objects, arrays, conditional validation, combining
      subschemas, annotating schemas) as dedicated topics; the standard
      addresses only the cross-references and Hyper-Schema slices of this.
      (Only the tour's table of contents could be retrieved; the sub-pages
      are client-rendered and 404 on fetch. The topics overlap with
      learnjsonschema.com, already cited above.)

      Re-checked 2026-08-14: the table of contents still retrieves (same
      eight topics), and a direct fetch of a sub-page
      (`/content/01-Getting-Started/01-Introduction`) still returns HTTP
      404, including via an archive-snapshot attempt.

      **Dismissed** (2026-08-14). The user identified the source as an
      interactive online playground rather than written reference material
      — it teaches by letting a reader edit and run schemas in-browser, not
      through fetchable prose. That explains the persistent 404s (the
      content is client-rendered, not server-delivered text) and means
      there is no prose to compare against the standard even if retrieval
      succeeded. Its topic list (primitive types, objects, arrays,
      conditional validation, combining subschemas, annotating schemas) is
      in any case already covered by TS-29's Validation keywords, Applicator
      keywords, Conditional validation, and Annotations sections, sourced
      from learnjsonschema.com and json-schema.org — both written reference
      material. No further action against this item.

- [x] [https://www.devzery.com/post/your-ultimate-guide-to-schema-for-json#creating-a-json-schema]
      covers schema boilerplate (`$schema`, `$id`, `title`, `description`,
      `type`, `properties`) more concretely than the standard — specifically,
      it walks through the skeleton of a schema document and the role of each
      header keyword, which the standard never does. The standard mentions
      `$schema`/metaschema only in `02-versions.adoc:9` and never explains
      `$id` or the document skeleton.

      **Resolved.** Closed by the new "Document skeleton" subsection of
      `05-schema-identification.adoc` (see the Core vocabulary keywords item
      above, under Missing), which walks through a `$schema`/`$id`/`title`/
      `description`/`type` example and explains the REQUIRED/OPTIONAL status
      of `$schema` and `$id`, cross-referencing `02-versions.adoc` for
      draft-version guidance and <<Annotations>> for `title`/`description`.
      Source added to the page's `== References` section.

## Out-of-scope

- [x] [https://romanglushach.medium.com/json-schema-the-secret-to-building-scalable-and-maintainable-data-models-2c456d90f73b#cloudevents-specifications]
      covers CloudEvents (a CNCF specification for event data), but it
      plausibly sits outside this standard's stated purpose (JSON Schema
      design) because it is a separate specification built on top of JSON
      Schema. Flagged for the user to confirm or overrule.

      **Confirmed out-of-scope** (2026-08-14). No change made to TS-29.

- [x] [https://www.linkedin.com/advice/1/how-do-you-keep-your-json-data-models-consistent#heres-what-else-to-consider]
      covers how different storage platforms (PostgreSQL, MongoDB) handle
      JSON, but it plausibly sits outside this standard's stated purpose
      because it is about data storage behavior, not schema design. Flagged
      for the user to confirm or overrule.

      **Confirmed out-of-scope** for TS-29 (2026-08-14). The user noted it
      may be relevant to the relational-databases standard instead. No
      change made to TS-29; flagged here as a candidate item for a future
      gap analysis of the relational-databases / SQL standard (its own
      `GAPS.md`), not actioned against that standard from this run.

- [x] [https://www.devzery.com/post/your-ultimate-guide-to-schema-for-json#using-json-schema-for-validation]
      covers language-specific validation code (e.g. Python `jsonschema`
      `validate()` API, `ValidationError` exceptions), but it plausibly sits
      outside this standard's stated purpose because it is implementation
      detail rather than schema design. Flagged for the user to confirm or
      overrule.

      **Confirmed out-of-scope** (2026-08-14), but the user asked for a
      short mention. Added one sentence to the "Validator libraries"
      subsection of `21-useful-links.adoc` (renumbered from `09-` — see
      this file's top-level note), naming Python `jsonschema`'s
      `validate()`/`ValidationError` as an example and pointing to each
      library's own documentation for the rest, without documenting any
      API in detail.

## Unresolved

- [x] [https://www.youtube.com/watch?v=QiAXxaLrt7E] could not be retrieved:
      the YouTube page returned only generic site chrome/footer with no video
      title, description, or transcript. Not included in the comparison
      above.

      **Dismissed.** 2026-08-15. Re-attempted via WebFetch; still returns
      only YouTube's footer/navigation chrome and the bare page title ("A
      Few JSON Schema Tips & Tricks: Getting Started"), no transcript or
      description text. Persistent, not transient. No claims extractable.

- [x] [https://www.youtube.com/watch?v=GjJpRsVffg0] could not be retrieved:
      the YouTube page returned only generic site chrome/footer with no video
      title, description, or transcript. Not included in the comparison
      above.

      **Dismissed.** 2026-08-15. Re-attempted via WebFetch; still returns
      only YouTube's footer/navigation chrome and the bare page title
      ("Maintaining JSON Schemas at Scale - Jason Desrosiers"), no transcript
      or description text. Persistent, not transient. No claims extractable.