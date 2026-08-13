# TS-49 gap analysis

Gaps found comparing TS-49: Cloud platform engineering against the following
reference resources:

- https://blog.allegro.tech/2024/04/ten-years-microservices.html
- https://nocomplexity.com/documents/0complexity/0cxdesignprinciples.html

**Assessment.** Both sources identified topics missing from the standard
entirely rather than partially covered: the cloud service model progression
(IaaS to PaaS to container orchestration, the no-SSH operating model,
internal developer platforms, and autoscaling), and the principle that
management capacity must scale with the system, with automation as the only
solution at scale. Converted from the legacy format on 2026-08-13.

**Status:** 2 of 2 actionable gaps closed (2026-08-13). Both gaps closed in
this run. Nothing remains open in this file: 0 missing, 0 partial,
0 out-of-scope, 0 unresolved.

## Missing

- [x] https://blog.allegro.tech/2024/04/ten-years-microservices.html says
      Allegro moved from OpenStack VMs with Puppet (IaaS), to Mesos/Marathon
      (PaaS, no SSH — a culture shock), to Kubernetes, with a custom "App
      Console" (à la Backstage) abstracting the underlying platform;
      autoscaling now handles most services without developer involvement.
      The gap: TS-49 does not cover the IaaS to PaaS to container-
      orchestrator progression, internal developer platforms (IDPs), the
      no-SSH operating model, or autoscaling. Coverage check: TS-49 covers
      self-service platforms and paved roads but does not address the
      IaaS/PaaS/CaaS distinction, internal developer platforms
      (Backstage-style), the no-SSH/immutable-infrastructure operating
      model, or autoscaling. Recommend a new section in `partials/049/`.
      Cross-references: TS-58 (Docker).

      **Resolved.** Closed by a new partial,
      `03-cloud-platform-evolution.adoc`, included at the
      end of the page (before `== References`). Covers the three-stage
      IaaS/PaaS/container-orchestration progression under "IaaS, PaaS, and
      container orchestration"; the no-SSH, immutable-infrastructure
      operating model and its observability precondition under "The no-SSH,
      immutable-infrastructure operating model"; internal developer
      platforms as both the paved-road principle in practice and an
      orchestrator abstraction boundary under "Internal developer
      platforms"; and autoscaling, including its dependency on disposable,
      stateless instances, under "Autoscaling". No explicit
      cross-reference to TS-58 (Docker) was added — the new section does
      not discuss container images or registries specifically, so a link
      there would be incidental rather than load-bearing; noted here rather
      than added silently. Source added to the page's `== References`.

- [x] https://nocomplexity.com/documents/0complexity/0cxdesignprinciples.html
      says management capacity must be able to manage the systems that must
      be controlled. As the number of objects one person must manage grows,
      automation becomes the only solution; management/CI-CD software must
      be scalable, error-free, and able to work in parallel. The gap: the
      "management capacity must scale with the system; automation is the
      only answer at scale" principle is not treated as a design principle.
      Coverage check: TS-49 covers self-service platforms and aligned
      autonomy at the organizational level, but does not frame the core
      principle that management capacity must scale with the number of
      managed objects and that automation is the scaling mechanism.
      Recommend placing at `00-guiding-principles.adoc`.
      Cross-references: TS-2 (Software design qualities).

      **Resolved.** Closed by a new "Management capacity must scale with the
      system" section in `00-guiding-principles.adoc`, inserted between
      "Aligned autonomy" and "Two failure modes". States that human
      management capacity is bounded and that automation is the only
      mechanism that scales past that bound, then requires the platform's
      own management and CI/CD tooling to be scalable, reliable, and able to
      act in parallel — carrying over the source's three requirements —
      and notes that automation raises the ceiling on what a team can manage
      rather than removing the need for people. Source added to the page's
      `== References`.

## Partial

(No partial-coverage items — the original analysis recorded no items of
this kind.)

## Out-of-scope

(No out-of-scope items — the file was converted from the legacy format,
which recorded no such items.)

## Unresolved

(No unresolved items — the file was converted from the legacy format,
which recorded no such items.)
