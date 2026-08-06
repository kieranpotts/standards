# GAPS — TS-41 React

Coverage gaps identified by comparing external sources against this standard.

---

## React Native + Expo for cross-platform code sharing

- **Source**: https://newsletter.pragmaticengineer.com/p/bluesky-engineering-culture
- **What the source says**: A single engineer built the Bluesky website, iOS app, and Android app using React Native and Expo, sharing code across all platforms. The team argues that two separate codebases mean "two separate products."
- **Coverage check**: TS-41 is scoped to "composing graphical web user interfaces" with no mention of React Native, Expo, mobile platforms, or cross-platform code sharing.
- **Gap**: TS-41 does not cover React Native or Expo, nor the trade-offs of cross-platform (web + native mobile) code sharing. This may be intentionally out of scope if TS-41 is web-only, but given the standard's broad "React" title, the absence is worth flagging.