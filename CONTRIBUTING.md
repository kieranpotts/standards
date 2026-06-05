# Contributing

These technical standards are living documents. To make changes to a technical standard, or to create a new one, use the normal pull request workflow via GitHub.

Technical standards documents are written in the AsciiDoc format, as specified in the [AsciiDoctor docs](https://docs.asciidoctor.org/asciidoc/latest/). Long technical standards documents – with two or more sections – MUST include a table of contents, generated automatically by the AsciiDoc processor. Use the [TOC macro](https://docs.asciidoctor.org/asciidoc/latest/toc/position/) to control the position of the TOC in each document, after the introductory text and before the first section.

```adoc
= TS-1: Technical Standard #1
:toc: macro
:toc-title: Contents

Introductory text…

toc::[]

== Section 1

// Text content...

```

Any books, blogs, or other third-party media that influenced the content of a technical standard MUST be listed in a "References" section at the end of the document.

```adoc
// Main content ...

''''

== References

* https://example.com[Link 1]

* https://example.com[Link 2]

* https://example.com[Link 3]
```
