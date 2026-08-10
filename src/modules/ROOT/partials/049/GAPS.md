# GAPS — TS-49 Cloud Platform Engineering

Coverage gaps identified by comparing external sources against this standard.

---

## Cloud progression IaaS → PaaS → Kubernetes; internal developer platforms; no-SSH; autoscaling

- **Source**: https://blog.allegro.tech/2024/04/ten-years-microservices.html
- **What the source says**: Allegro moved from OpenStack VMs with Puppet (IaaS), to Mesos/Marathon (PaaS, no SSH — a culture shock), to Kubernetes, with a custom "App Console" (à la Backstage) abstracting the underlying platform; autoscaling now handles most services without developer involvement.
- **Coverage check**: TS-49 covers self-service platforms and paved roads but does not address the IaaS/PaaS/CaaS distinction, internal developer platforms (Backstage-style), the no-SSH/immutable-infrastructure operating model, or autoscaling.
- **Gap**: TS-49 does not cover the IaaS→PaaS→container-orchestrator progression, internal developer platforms (IDPs), the no-SSH operating model, or autoscaling.
- **Cross-references**: TS-58 (Docker)

---

## Management capacity must scale with the system; automation is the only answer at scale

- **Source**: https://nocomplexity.com/documents/0complexity/0cxdesignprinciples.html
- **What the source says**: Management capacity must be able to manage the systems that must be controlled. As the number of objects one person must manage grows, automation becomes the only solution; management/CI-CD software must be scalable, error-free, and able to work in parallel.
- **Coverage check**: TS-49 covers self-service platforms and aligned autonomy at the organizational level, but does not frame the core principle that management capacity must scale with the number of managed objects and that automation is the scaling mechanism.
- **Gap**: The "management capacity must scale with the system; automation is the only answer at scale" principle is not treated as a design principle.
- **Cross-references**: TS-2 (Software Design Qualities)