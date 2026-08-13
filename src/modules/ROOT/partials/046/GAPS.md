# TS-46 gap analysis

Gaps found comparing TS-46: *Distributed data and caching* against the
following reference resource:

- https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/
  (Jeff Hodges, "Notes on Distributed Systems for Young Bloods")

**Assessment.** Of the 18 points in the reference, one was routed to TS-46:
#15 ("Writing cached data back to persistent storage is bad"). TS-46
consistently models the cache as a read-through / read-optimised copy whose
source-of-truth lives elsewhere (`04-cache-freshness.adoc:1-20`), and treats
write conflicts as something that happens at the authoritative store between
legitimate writers (`05-distributed-writes.adoc:1-36`). It does not address
the distinct anti-pattern the reference names: a system where the cached
copy is itself written back to persistent storage, so a stale cache value
silently overwrites a newer authoritative value. It is missing.

**Status:** 1 of 1 gap resolved (2026-08-13).

## Missing

- [x] https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/
      ("Writing cached data back to persistent storage is bad") is not
      addressed anywhere in the standard. The reference identifies writing
      cached data back to persistent storage as a flaw (especially in systems
      designed by people less experienced in distributed systems), names
      "Russian-doll caching" as a hazard, and gives the canonical symptom of
      user attributes (screennames, emails, hashed passwords) mysteriously
      reverting to a previous value. TS-46 models the cache strictly as a
      read-optimised copy (`04-cache-freshness.adoc:1-20`) and frames write
      conflicts as multi-writer concurrency at the authoritative store
      (`05-distributed-writes.adoc:1-36`) — it never contemplates the cache
      as a source of writes, never identifies the write-back-from-cache
      anti-pattern, never discusses multi-layer ("Russian-doll") caching
      hazards, and never connects the data-reverting symptom to cache
      write-back. Recommend a new "Cache write-back anti-pattern" subsection
      in `04-cache-freshness.adoc` (or `05-distributed-writes.adoc`) stating
      that caches MUST NOT be a source of writes to the persistent store, and
      warning against nested/multi-layer caching that feeds writes back.

      **Resolved.** Closed by a new "Cache write-back anti-pattern" section
      appended to `04-cache-freshness.adoc`. States that a cache MUST NOT be
      a source of writes to the persistent store, explains the mechanism by
      which a stale cached value silently overwrites newer authoritative
      data (the reference's screenname/email/password-reverting symptom),
      names the "Russian-doll" multi-layer caching hazard, and gives three
      normative practices: treat the cache as read-only from the
      application's point of view, never read-modify-write through a cache,
      and keep the write path separate from every read-side cache layer.
      Cross-references the existing "Distributed writes" section for how
      writes to the authoritative store should propagate to the cache.

## Partial

(None identified in this run.)

## Out-of-scope

(None identified in this run.)

## Unresolved

(None.)