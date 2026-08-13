# TS-41 gap analysis

Gaps found comparing TS-41: React against the following reference resources:

- https://newsletter.pragmaticengineer.com/p/bluesky-engineering-culture

**Assessment.** The single reference is The Pragmatic Engineer's write-up of
Bluesky's engineering culture, which yielded one gap — missing coverage of
React beyond the DOM, specifically React Native, Expo, and the trade-offs of
sharing one codebase across web and native mobile targets. This file was
converted from the legacy format on 2026-08-13.

**Status:** 1 of 1 actionable gaps closed (2026-08-13). This run converted
the file from the legacy format and closed the React Native and Expo gap
with a new `05-cross-platform.adoc` section. Nothing remains open: 0 missing,
0 partial, 0 out-of-scope awaiting the user, 0 unresolved.

## Missing

- [x] https://newsletter.pragmaticengineer.com/p/bluesky-engineering-culture
      says a single engineer built the Bluesky website, iOS app, and Android
      app using React Native and Expo, sharing code across all platforms, and
      that the team argues two separate codebases mean "two separate
      products." The gap: TS-41 does not cover React Native or Expo, nor the
      trade-offs of cross-platform (web + native mobile) code sharing. This
      may be intentionally out of scope if TS-41 is web-only, but given the
      standard's broad "React" title, the absence is worth flagging.
      Coverage check: TS-41 is scoped to "composing graphical web user
      interfaces" with no mention of React Native, Expo, mobile platforms, or
      cross-platform code sharing. Recommend a new section, appended after
      `04-filesystem.adoc`.

      **Resolved.** Closed by a new `05-cross-platform.adoc`, "Cross-platform
      React" section, wired into `src/modules/ROOT/pages/041.adoc` after the
      existing four partials. The section states that React is not tied to
      the DOM and that the component, hooks, and state conventions in the
      rest of the standard hold under React Native; it makes one shared
      codebase the SHOULD for a product shipping both a web UI and native
      mobile apps, on the grounds that two codebases for one product are two
      products that drift apart, citing Bluesky's one-engineer,
      three-platform client as the evidence; it makes React Native with Expo
      the RECOMMENDED basis for such a codebase; it carries a NOTE that
      sharing a codebase does not make the platforms free, so per-platform
      defects and release processes still have to be budgeted for; it
      requires platform differences to be isolated behind platform-suffixed
      modules rather than spread through shared code as `Platform.OS`
      branches, with a worked file tree and a `Platform.select` example, and
      requires every variant of such a module to export the same API; and it
      carves out the exception, that a web-only product MUST NOT adopt React
      Native speculatively, because React Native's primitives are not
      semantic HTML and reconstructing document semantics on top of them
      costs more than it saves. Cross-references TS-39 (HTML) and TS-19
      (Search engine optimization) for what the non-semantic primitives put
      at risk, and TS-18 (Web GUIs) for the web-only alternative. The
      page's introduction was widened from "graphical web user interfaces"
      to "graphical user interfaces", with a sentence saying the standard is
      written for the web and pointing at the new section — which is the part
      of the item that flagged the mismatch between the standard's scope
      statement and its broad "React" title. Source added to the page's new
      `== References` section.

## Partial

(Converted from the legacy format. The original analysis recorded no items
of this kind — its single gap was classed as missing.)

## Out-of-scope

(Converted from the legacy format. The original analysis recorded no items
of this kind — the legacy format has no concept of them.)

## Unresolved

(Converted from the legacy format. The original analysis recorded no items
of this kind — the legacy format has no concept of them.)
