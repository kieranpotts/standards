# TS-19: Search Engine Optimization (SEO)

This is a compact version of technical standard TS-19 for AI agents.

Use this when creating or optimizing content for search engine ranking — SEO
best practices, defensive SEO, targeting strategies, web vitals, and SEO tools.
The focus is on disciplined content habits over technical tricks.

Do NOT use this for web GUI performance optimization mechanics (server-rendering,
pre-fetching, caching, fonts) — those are covered by
[TS-18: Web GUIs](../018/AGENTS.md). Web vitals metrics are referenced here for
SEO context only. For URL design, see [TS-63: URL Design](../063/AGENTS.md).

## Rules

### Best practices for SEO

- **SEO is more about good habits than strategies; good outcomes depend on
  discipline.**

  This means: updating content frequently to keep it fresh; manually adding
  internal links to every new thing you publish; sweating the detail of
  everything you write; doing thorough research and backing up content with
  evidence from reliable sources; crafting headlines that stand out in search;
  constantly searching for new content opportunities.

- **Write content that is genuinely useful to your target users.**

  Write content that helps solve real problems your users have. Do not spend
  much effort on optimizing content for particular search keywords or
  particular crawlers. Content MUST be easily parsable by machines, but beyond
  this you should focus on writing high-quality content that people will find
  useful and want to share.

- **"Quality" content means independent, authoritative, and trustworthy
  content.**

  Avoid producing content that is overly promotional or self-serving, or overly
  technical or jargon-heavy (unless appropriate for the target audience). Don't
  oversell your products — focus on how your product is _different_, not why
  it's _better_ ("better" is subjective and people will see right through such
  claims). Instead, incentivize people to try your product for themselves and
  let them figure out if it's better or not.

### Defensive SEO

- **Defensive SEO aims to rank highly for certain search terms so your
  competitors don't.**

  Particularly effective for: comparisons between your product and your
  competitors; and "the best options in your product category" searches.

### Targeting strategies

- **It's easier to rank for 100 low-volume searches than a handful of lucrative,
  popular ones — especially early on, when you do not yet have a long-established
  web presence.**

  A niche tutorial with an estimated 30 relevant searches per month (and an
  Ahrefs difficulty score of zero) can result in ~5 unique visits/day, scaling
  to ~1,850 unique users per year. 100 similar pages scale to ~185,000 unique
  visitors per year, each with a very specific problem you are offering to
  solve. Getting good at ranking for low-competition keywords will make it
  easier to rank for high-competition ones in the long run, too.

### Web vitals

- **Google publishes [Core Web Vitals](https://support.google.com/webmasters/answer/9205520)
  — three UX metrics: Largest Contentful Paint (LCP), Interaction to Next Paint
  (INP), and Cumulative Layout Shift (CLS).**

  These are useful metrics for measuring user experience, but they are
  surprisingly unimportant when it comes to search engine ranking (at least in
  Google). Per a 2023 statement from a Google dev advocate: "Google Search
  always seeks to show the most relevant content, even if the page experience
  is not the best. So page loading performance and also core web vitals aren't
  as important as some people might think they are. They are not irrelevant,
  but do not over focus on these things." This has been reiterated by John
  Mueller (Google's search relations team lead): "A perfect score is a fun
  technical challenge, and you'll learn something along the way... but it's not
  going to make your site's rankings jump up."

### SEO tools

- **SEO tools are just _tools_ — they won't magically generate growth.**

  An easy way to fail is to spend too much time learning or researching SEO
  tools, and not enough doing the important bit — the content. Use a small
  number of good quality tools, rather than attempt to use lots of different
  ones.

- **Choose an all-in-one SEO tool (eg. Ahrefs or SEMrush).**

  These cover most bases — rank tracking, keyword research, and competitor
  research. Google Search Console is useful for finding problems and
  opportunities, including technical issues like website performance; it is
  free to use. [Keywords Everywhere](https://keywordseverywhere.com/) is an
  inexpensive browser extension that augments Google Search, Trends, and Search
  Console with keyword data.

## References

- [TS-19 source](../../pages/019.adoc)
- [TS-18: Web GUIs](../018/AGENTS.md)
- [TS-63: URL Design](../063/AGENTS.md)
- [Core Web Vitals](https://support.google.com/webmasters/answer/9205520)
