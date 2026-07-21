# Threat modeling workshop 2026-01-16

- **System/application name:** PixelVault Image Storage Service
- **Workshop facilitator:** Sarah Chen (Security Architect)
- **Participants:**
  - **Business stakeholder:** Marcus Rodriguez (Product Manager)
  - **Technical architect:** Jennifer Park (Principal Engineer)
  - **Development lead:** Ahmed Hassan (Engineering Lead)
  - **Security analyst:** David Kim (Security Engineer)
  - **Privacy officer (eg. data controller):** Lisa Thompson (Data Protection Officer)
  - **Other stakeholders:** Tom Wilson (DevOps Lead), Rachel Green (Compliance Manager)

## Business context

PixelVault is a cloud-based image storage and sharing service that allows users
to upload, store, organize, and share photographs and images. The service
provides both free and premium tiers, with revenue generated through
subscription fees and enterprise licensing.

The critical business functions include secure image upload and storage, image
retrieval and download, user authentication and authorization, image
organization (albums, tags), sharing capabilities (private links, public
galleries), and integration with third-party applications via an HTTP API.

Key stakeholders include end users (photographers, content creators, families),
enterprise customers (marketing agencies, media companies), partners (camera
manufacturers, photo editing software vendors), and regulatory bodies (GDPR,
CCPA compliance authorities).

Business impact of security/privacy failures:

- **Financial.** Loss of customer trust leading to churn, potential regulatory
fines under GDPR, litigation costs from data breaches, loss of enterprise
contracts.

- **Reputational.** Brand damage as a trusted platform for personal memories,
negative press coverage, loss of competitive advantage.

- **Regulatory.** Non-compliance with GDPR, CCPA, SOC 2 requirements leading to
sanctions and inability to operate in certain markets.

- **Operational.** Service disruption affecting millions of users, emergency
incident response costs, mandatory breach notifications.

## Technical scope

The threat model covers the core PixelVault platform including the web
application, mobile applications (iOS/Android), API gateway, authentication
service, image processing pipeline, storage layer, and content delivery network.

**System boundaries:** The scope includes all components from user-facing
interfaces through to persistent storage. Out-of-scope are third-party payment
processing (Stripe integration), email delivery service (SendGrid), and
monitoring/analytics platforms (DataDog).

**Technology stack:**

- **Front-end:** React web app, Swift (iOS), Kotlin (Android).
- **API layer:** Node.js with Express, GraphQL.
- **Authentication:** Auth0 with custom user database.
- **Image processing:** Python microservices using Pillow and ImageMagick.
- **Storage:** AWS S3 for objects, PostgreSQL for metadata, Redis for caching.
- **CDN:** CloudFront for content delivery.
- **Infrastructure:** Kubernetes on AWS EKS, Terraform for IaC.

**Deployment environments:** Production (multi-region AWS deployment in us-east-1
and eu-west-1), staging (single region), development (local and shared dev/test
environment).

**Integration points:** Auth0 authentication service, AWS S3 storage, CloudFront
CDN, Stripe payment API, SendGrid email API.

## System decomposition

### Key components

| Component                    | Description                                                          | Trust level                 | Data handled                                                                                 |
|------------------------------|----------------------------------------------------------------------|-----------------------------|----------------------------------------------------------------------------------------------|
| **Web application**          | React SPA hosted on CloudFront, handles user interactions            | UNTRUSTED (public internet) | User credentials (transit only), session tokens, image metadata, UI state                    |
| **Mobile apps**              | Native iOS/Android applications                                      | UNTRUSTED (user devices)    | User credentials (transit only), session tokens, cached image thumbnails, user preferences   |
| **API gateway**              | Kong Gateway handling routing, rate limiting, authentication         | SEMI-TRUSTED (DMZ)          | JWT tokens, API keys, request/response data, rate limiting metadata                          |
| **Authentication service**   | Auth0-based service with custom user database integration            | TRUSTED (internal)          | User credentials (hashed), session tokens, MFA secrets, authentication logs                  |
| **Image upload service**     | Node.js microservice handling multipart uploads                      | TRUSTED (internal)          | Raw image files, upload metadata, temporary presigned URLs                                   |
| **Image processing service** | Python workers for thumbnail gen, format conversion, meta extraction | TRUSTED (internal)          | Original images, generated thumbnails, EXIF metadata, processing queue messages              |
| **Metadata service**         | Node.js API for image metadata, albums, tags, sharing settings       | TRUSTED (internal)          | Image metadata, user-created tags, album structures, sharing permissions, user relationships |
| **Storage layer**            | AWS S3 buckets for image storage                                     | TRUSTED (internal)          | Original images, thumbnails, encrypted backups                                               |
| **Metadata database**        | PostgreSQL cluster                                                   | TRUSTED (internal)          | User profiles, image metadata, sharing permissions, album data, audit logs                   |
| **CDN**                      | CloudFront distribution for image delivery                           | SEMI-TRUSTED (public edge)  | Cached images, signed URLs, access logs                                                      |
| **Background jobs**          | Celery workers for async tasks                                       | TRUSTED (internal)          | Image processing tasks, cleanup jobs, notification data                                      |

### Data flows

| Source                       | Destination              | Data type                              | Protocol                 | Authentication                       |
|------------------------------|--------------------------|----------------------------------------|--------------------------|--------------------------------------|
| **Web/mobile clients**       | API gateway              | Login credentials                      | HTTPS (TLS 1.3)          | HTTP Basic auth                      |
| **API gateway**              | Authentication service   | Authentication request                 | HTTPS (mTLS)             | Service certificate                  |
| **Authentication service**   | Client                   | JWT access token, refresh token        | HTTPS (TLS 1.3)          | N/A (response)                       |
| **Client**                   | API gateway              | Image upload request with JWT          | HTTPS (TLS 1.3)          | JWT Bearer token                     |
| **API gateway**              | Image upload service     | Validated upload request               | HTTPS (mTLS)             | Service certificate + JWT validation |
| **Image upload service**     | S3                       | Image file data                        | HTTPS (AWS Signature V4) | IAM role credentials                 |
| **Image upload service**     | Image processing service | Processing job via message queue       | TLS over AMQP            | Service credentials                  |
| **Image processing service** | S3                       | Read original, write thumbnails        | HTTPS (AWS Signature V4) | IAM role credentials                 |
| **Metadata service**         | PostgreSQL               | Image metadata, permissions            | TLS (certificate auth)   | Database credentials (rotated)       |
| **Client**                   | CDN                      | Image download request with signed URL | HTTPS (TLS 1.3)          | Signed URL (time-limited)            |
| **CDN**                      | S3                       | Origin fetch                           | HTTPS (AWS Signature V4) | CloudFront OAI                       |
| **Background jobs**          | Metadata database        | Cleanup operations, analytics          | TLS (certificate auth)   | Database credentials (rotated)       |

### Sensitive assets

| Asset                                       | Sensitivity | Integrity requirements                                     | Availability requirements                   | Privacy concern                                               |
|---------------------------------------------|-------------|------------------------------------------------------------|---------------------------------------------|---------------------------------------------------------------|
| **User images (original files)**            | HIGH        | CRITICAL (must not be modified or corrupted)               | HIGH (users expect reliable access)         | YES (GDPR personal data, potentially intimate/private images) |
| **User credentials and password hashes**    | CRITICAL    | CRITICAL (compromise enables account takeover)             | HIGH (required for authentication)          | YES (authentication secrets)                                  |
| **JWT signing keys**                        | CRITICAL    | CRITICAL (compromise allows token forgery)                 | CRITICAL (service cannot function without)  | NO (infrastructure secret)                                    |
| **S3 encryption keys (KMS)**                | CRITICAL    | Critical (compromise exposes all stored images)            | CRITICAL (required for data access)         | NO (infrastructure secret)                                    |
| **Image metadata (titles, EXIF)**           | MEDIUM-HIGH | HIGH (must accurately reflect user intent)                 | HIGH (core functionality)                   | YES (may contain location data, personal information)         |
| **Sharing permissions and access controls** | HIGH        | Critical (incorrect permissions cause unauthorized access) | HIGH (required for sharing features)        | YES (defines privacy boundaries)                              |
| **User profile data**                       | MEDIUM      | HIGH (must be accurate)                                    | MEDIUM (degraded experience if unavailable) | YES (PII - name, email, preferences)                          |
| **API keys and OAuth tokens**               | HIGH        | CRITICAL (compromise enables impersonation)                | HIGH (required for partner integrations)    | NO (authorization credentials)                                |
| **Database connection strings**             | CRITICAL    | CRITICAL (compromise exposes all data)                     | CRITICAL (service depends on database)      | NO (infrastructure secret)                                    |
| **Audit logs**                              | MEDIUM      | CRITICAL (must be tamper-proof for compliance)             | MEDIUM (needed for investigations)          | YES (contains user activity data)                             |

### Entry points

1. **Web application.** Public-facing React SPA.
2. **Mobile applications.** iOS App Store and Google Play Store downloads.
3. **Public API.** RESTful and GraphQL endpoints for partners.
4. **OAuth 2.0 endpoints.** Third-party application integration.
5. **Admin console.** Internal administration interface.
6. **CDN endpoints.** Image delivery URLs.
7. **Webhook receivers.** Callbacks from Auth0, Stripe, partner services.

### Trust boundaries

1.  **Internet → API gateway.**
    Transition from untrusted public internet to semi-trusted DMZ.

2.  **API gateway → internal services.**
    Transition from DMZ to trusted internal network.

3.  **Application layer → data layer.**
    Transition from application services to data persistence.

4.  **Internal network → AWS services.**
    Transition from self-managed infrastructure to AWS-managed services.

5.  **Internal network → third-party services.**
    Boundary with integrated services (Auth0, Stripe).

## Threat assessment

### TA1: API gateway

Attacker spoofs authentication tokens to impersonate legitimate users and access
their images.

Counter-measures: JWT signature verification with RS256, short token expiry
(15min access, 7day refresh), token rotation, Auth0 integration with MFA support,
IP-based anomaly detection.

- Type: SPOOFING
- Likelihood: MEDIUM
- Impact: HIGH
- Overall Risk Rating: **HIGH**

### TA2: S3 storage

Attacker gains unauthorized access to S3 bucket and downloads all user images
directly.

Counter-measures: S3 bucket policies with explicit deny for public access, IAM
roles with least privilege, VPC endpoints for S3 access, bucket versioning
enabled, MFA delete enabled, CloudTrail logging of all access.

- Type: ELEVATION OF PRIVILEGE
- Likelihood: LOW
- Impact: HIGH
- Overall Risk Rating: **MEDIUM**

### TA3: Image upload service

Attacker uploads malicious files (malware, XSS payloads embedded in images)
that exploit other users.

Counter-measures: File type validation using magic bytes, antivirus scanning
(ClamAV integration), content security policy headers, image re-encoding to
strip malicious payloads, size limits (50MB max), upload rate limiting.

- Type: TAMPERING
- Likelihood: HIGH
- Impact: HIGH
- Overall Risk Rating: **HIGH**

### TA4: CDN/download flow

Attacker intercepts or enumerates signed URLs to access private images they
shouldn't have permission to view.

Counter-measures: Short-lived signed URLs (1 hour expiry), URL signing with
cryptographically secure keys, permission verification before URL generation,
no predictable URL patterns, HTTPS-only delivery, CloudFront geo-restrictions
for sensitive content.

- Type: INFORMATION DISCLOSURE
- Likelihood: MEDIUM
- Impact: HIGH
- Overall Risk Rating: **MEDIUM**

### TA5: API gateway

Attacker performs denial of service attack overwhelming the API with requests.

Counter-measures: Kong rate limiting (100 req/min per user, 1000 req/min per
IP), WAF rules (AWS WAF), auto-scaling based on load, CDN caching to reduce
origin load, request size limits, connection limits, DDoS protection (AWS
Shield).

- Type: DENIAL OF SERVICE
- Likelihood: HIGH
- Impact: MEDIUM
- Overall Risk Rating: **MEDIUM**

### TA6: Metadata database

SQL injection vulnerability allows attacker to extract sensitive user data or
sharing permissions.

Counter-measures: Parameterized queries exclusively (no string concatenation),
ORM usage (Sequelize), input validation, least privilege database user,
database activity monitoring, regular security scanning (SAST/DAST).

- Type: TAMPERING + INFORMATION DISCLOSURE
- Likelihood: LOW
- Impact: HIGH
- Overall Risk Rating: **MEDIUM**

### TA7: Image processing service

Attacker uploads specially crafted image that exploits ImageMagick
vulnerability causing remote code execution.

Counter-measures: Sandboxed processing environment (separate K8s namespace),
ImageMagick policy.xml restrictions, input validation, regular patching,
resource limits on workers, network segmentation preventing internet access
from workers.

- Type: ELEVATION OF PRIVILEGE
- Likelihood: MEDIUM
- Impact: HIGH
- Overall Risk Rating: **HIGH**

### TA8: User session

Attacker performs session fixation or session hijacking to take over user
accounts.

Counter-measures: Secure session cookies (httpOnly, secure, sameSite), session
regeneration on privilege change, session timeout (24h idle, 7d absolute),
binding sessions to IP/user-agent, logout on multiple failed attempts.

- Type: SPOOFING
- Likelihood: MEDIUM
- Impact: HIGH
- Overall Risk Rating: **MEDIUM**

### TA9: API endpoints

Insecure direct object references allow users to access images belonging to
other users by manipulating IDs.

Counter-measures: Permission verification on every request, UUIDs instead of
sequential IDs, authorization middleware enforced globally, separation of
resource ownership from resource ID, audit logging of access attempts.

- Type: AUTHORIZATION BYPASS
- Likelihood: MEDIUM
- Impact: HIGH
- Overall Risk Rating: **HIGH**

### TA10: Data at rest

Unencrypted database backups expose user data if stolen from backup storage.

Counter-measures: AES-256 encryption for all S3 objects using KMS, encrypted
EBS volumes, encrypted RDS snapshots, encrypted database connections, key
rotation every 90 days, separate encryption keys per environment.

- Type: INFORMATION DISCLOSURE
- Likelihood: LOW
- Impact: HIGH
- Overall Risk Rating: **MEDIUM**

### TA11: Mobile apps

Reverse engineering of mobile apps exposes API keys or encryption secrets
hardcoded in the application.

Counter-measures: API keys stored in secure enclave (iOS Keychain, Android
KeyStore), certificate pinning, code obfuscation, no hardcoded secrets in
source, secrets retrieved from backend after authentication, tamper detection.

- Type: INFORMATION DISCLOSURE
- Likelihood: HIGH
- Impact: MEDIUM
- Overall Risk Rating: **MEDIUM**

### TA12: Audit logging

Attacker deletes or modifies logs to hide malicious activity from detection.

Counter-measures: Write-only log permissions, centralized logging to immutable
storage (S3 with object lock), log integrity verification, separate IAM role
for log access, CloudTrail enabled and protected, SIEM integration for
real-time monitoring.

- Type: REPUDIATION
- Likelihood: LOW
- Impact: MEDIUM
- Overall Risk Rating: **LOW**

### TA13: Third-party integrations

Compromised OAuth tokens for partner applications grant unauthorized access to
user images.

Counter-measures: OAuth 2.0 with authorization code flow, granular scope
permissions, token expiration and refresh, user consent for each permission,
ability to revoke tokens, audit logging of third-party access, partner
application vetting.

- Type: ELEVATION OF PRIVILEGE
- Likelihood: MEDIUM
- Impact: HIGH
- Overall Risk Rating: **MEDIUM**

### TA14: EXIF metadata

Images retain geolocation and timestamp metadata exposing user privacy (home
addresses, travel patterns).

Counter-measures: Optional metadata stripping feature (enabled by default),
user controls for metadata retention, privacy education in UI, separate
processing pipeline for shared vs. private images, EXIF data not exposed in
API responses without explicit permission.

- Type: INFORMATION DISCLOSURE
- Likelihood: HIGH
- Impact: MEDIUM
- Overall Risk Rating: **MEDIUM**

### TA15: Shared links

Publicly shared image links are indexed by search engines exposing supposedly
private images.

Counter-measures: Robots.txt directives, noindex meta tags on shared link
pages, separate domain for user-generated content, signed URLs with
authentication even for "public" shares, user warnings about public sharing
implications.

- Type: INFORMATION DISCLOSURE
- Likelihood: MEDIUM
- Impact: HIGH
- Overall Risk Rating: **MEDIUM**

### TA16: Data retention

User data retained indefinitely after account deletion violates GDPR right to
erasure.

Counter-measures: Automated deletion workflow triggered 30 days after deletion
request, hard delete from all systems including backups, deletion verification
audit, user confirmation of deletion, retention policy documentation,
compliance monitoring.

- Type: NON-COMPLIANCE
- Likelihood: LOW
- Impact: HIGH
- Overall Risk Rating: **MEDIUM**

### TA17: Cross-tenant data leakage

Shared infrastructure allows one user's processing job to access another
user's images in memory/temp storage.

Counter-measures: Namespace isolation in Kubernetes, separate temp directories
per job with unique IDs, cleanup after processing, no shared memory between
workers, container security contexts, resource quotas per tenant.

- Type: INFORMATION DISCLOSURE
- Likelihood: LOW
- Impact: HIGH
- Overall Risk Rating: **MEDIUM**

### TA18: Admin console

Compromised admin credentials provide unrestricted access to all user data and
system configuration.

Counter-measures: Mandatory MFA for admin access, admin actions require
approval workflow for sensitive operations, separate VPN access required, IP
allowlisting, privileged access management (PAM) system, session recording,
just-in-time access provisioning.

- Type: ELEVATION OF PRIVILEGE
- Likelihood: LOW
- Impact: HIGH
- Overall Risk Rating: **MEDIUM**

### TA19: Man-in-the-middle

Network traffic interception between client and server exposes images and
authentication tokens.

Counter-measures: TLS 1.3 exclusively, HSTS headers with preloading,
certificate pinning in mobile apps, no mixed content, monitoring for
certificate transparency, regular TLS configuration audits.

- Type: INFORMATION DISCLOSURE
- Likelihood: LOW
- Impact: HIGH
- Overall Risk Rating: **LOW**

### TA20: Credential stuffing

Attackers use leaked credentials from other breaches to compromise PixelVault
accounts.

Counter-measures: Integration with HaveIBeenPwned API, password complexity
requirements, mandatory password reset for compromised credentials, rate
limiting on login attempts, account lockout after 5 failed attempts, CAPTCHA
after 3 failures, login anomaly detection.

- Type: SPOOFING
- Likelihood: HIGH
- Impact: HIGH
- Overall Risk Rating: **HIGH**
