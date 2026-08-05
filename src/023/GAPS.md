# TS-23 gap analysis

Gaps found comparing TS-23: Messages and Events against the following reference
resources:

- `src/023/__TODO__/event-driven.md`

**Assessment.** The reference is a single short TODO note on event-driven
programming. Most of its content is general paradigm commentary that sits
outside TS-23's stated scope (design and implementation of messages and events
for intra-organization asynchronous communication). One point — the necessity of
logging, monitoring, and alerting for event-driven systems — is a genuine
operational gap not addressed anywhere in the standard, despite TS-23 already
covering delivery reliability, retries, and dead letters.

**Status:** First run (2026-08-05). No prior `GAPS.md` existed. One missing gap
(observability) and two out-of-scope items flagged for the user.

## Missing

- [ ] `src/023/__TODO__/event-driven.md:7` states that logging, monitoring, and
      alerting become necessary to stay on top of event-driven systems and
      ensure they are working as expected. TS-23 addresses delivery
      reliability, retries, circuit breakers, dead letters, and SLAs
      (`src/023/03-delivery-and-reliability.adoc:1-143`) but gives no guidance
      on observability — logging message flows, monitoring delivery health,
      or alerting on stuck/failed/dead-lettered messages. Recommend a new
      section in `src/023/03-delivery-and-reliability.adoc` after "Service
      level agreements" (around line 120) or a new top-level section on
      observability. (Scope call: arguably belongs in a dedicated
      observability standard, but since TS-23 already covers operational
      reliability concerns, observability is a natural fit here.)

## Partial

_(None identified.)_

## Out-of-scope

- [ ] `src/023/__TODO__/event-driven.md:5` observes that event-driven
      programming is more complex due to the lack of a clear flow of control.
      This is general commentary on the event-driven programming paradigm
      rather than a design/implementation rule for messages and events. It
      plausibly sits outside TS-23's stated purpose, which is best practices
      for designing and implementing messages and events in message-driven
      architectures — not a treatise on the paradigm's characteristics.
      Flagged for the user to confirm or overrule; if kept, it would fit as a
      motivating note in `src/023/README.adoc:5-17`.

- [ ] `src/023/__TODO__/event-driven.md:5` observes that event-driven
      programming is often unavoidable in web client application interfaces,
      distributed systems, and multi-threaded environments. TS-23's scope is
      explicitly narrowed to asynchronous communication within a single
      organization's internal network (`src/023/README.adoc:8-9`); web client
      UIs and multi-threaded environments are outside that focus, and the
      "distributed systems" mention is too generic to be actionable. Flagged
      for the user to confirm or overrule.

## Unresolved

_(None. The single reference file was read in full.)_