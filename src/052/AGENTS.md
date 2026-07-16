# TS-52: Security and Secrets Management

Security requirements for applications and best practices for secrets
management.

A **secret** is any value that grants access or trust when revealed:
passwords and passphrases, API access keys and PATs, encryption keys
(symmetric keys and private keys of asymmetric pairs), JWTs, session
cookies, signed URLs, and configuration strings that embed credentials
(eg. database connection strings).

Use this when designing, implementing, or reviewing application security,
authentication, authorization, secrets handling, or network/web
application hardening.

Do NOT use this for threat modeling methodologies and artifacts — see
[TS-54: Threat Modeling](../054/AGENTS.md). For privacy and data
protection (data classification, lawful basis, regulated data), see
[TS-53: Privacy and Data Protection](../053/AGENTS.md). For
authentication and authorization patterns in more depth, see
[TS-55: Authentication and Authorization](../055/AGENTS.md). For JWTs
specifically, see [TS-56: JSON Web Tokens (JWTs)](../056/AGENTS.md). For
AWS-specific secrets management (Secrets Manager, KMS, IAM), see
[TS-51: Amazon Web Services (AWS)](../051/AGENTS.md). For release
mechanics, see [TS-10: Releasing](../010/AGENTS.md). For logging and
monitoring of security events, see
[TS-57: Logging, Monitoring, Observability](../057/AGENTS.md).

## Rules

### Third-party code

- **Third-party code MUST be reviewed before it is executed.** This
  applies regardless of the apparent legitimacy of the source, and
  covers open-source packages and libraries, code samples from
  documentation or tutorials, AI-generated code, contractor deliverables,
  and recruitment coding challenges. Sophisticated supply-chain attacks
  are specifically designed to exploit the trust developers place in
  professional-looking projects, repositories, and individuals.
  Developers are high-value targets.

- **Third-party code MUST NOT be executed directly on a developer's
  primary machine** without first being reviewed. All unknown or
  untrusted codebases MUST be run in an isolated environment such as a
  Docker container or (better still) a virtual machine.

- **Review for malicious patterns.** The review SHOULD include, but is
  not limited to, checking for:
  - Obfuscated code (byte arrays, encoded strings, `eval`-style dynamic
    execution).
  - Outbound network calls to unexpected or dynamic URLs, especially
    those that fetch and execute remote payloads.
  - Access to the file system, environment variables, or credential
    stores beyond what the code's stated purpose requires.
  - Self-destructing infrastructure patterns (short-lived URLs, recently
    registered domains).

- **Use security scanning tools on third-party code.** DAST and SAST
  tools MUST be used to audit third-party code. AI coding assistants MAY
  be used to assist with the review — prompting an AI to scan an
  unfamiliar codebase for suspicious patterns before execution is a
  RECOMMENDED practice.

- **Check declared dependencies against known vulnerability databases.**
  Dependencies declared in package manifests (eg. `package.json`,
  `requirements.txt`) MUST be checked against known vulnerability
  databases. Dependency versions MUST be pinned to reduce the risk of a
  malicious update being silently pulled in.

- **Stay vigilant against social engineering.** Malicious codebases are
  often delivered through highly convincing social engineering.
  Professional-looking LinkedIn profiles, company pages, and
  communication do not guarantee legitimacy. A red flag is being rushed
  into an action that would execute unknown code.

### Encryption

- **Personal data and business-sensitive information MUST be encrypted
  at rest.**

- **All data MUST be encrypted in transit** (eg. TLS), sensitive or
  otherwise.

### Secrets

- **Secrets MUST NOT be hard-coded in source code.**

- **Secrets MUST NOT be committed to code repositories or package
  registries.**

- **Secrets MUST NOT be sent to log output.**

- **Use dedicated secrets management systems for primary secrets.**
  Systems like HashiCorp Vault or AWS Secrets Manager MUST be used to
  store primary secrets. Deployment strategies MUST be implemented to
  fetch and inject secrets from these stores into applications at
  compile time or runtime as appropriate.

- **Secondary secrets (for dev/ops) are typically stored in devops
  toolchain secrets systems** (eg. GitHub Secrets for GitHub Actions).
  The lifetime of secondary secrets SHOULD be rotated in line with PAT
  cadence — typically less than 90 days.

#### Secret rotation

- **Rotate secrets at regular intervals.** It is RECOMMENDED that
  secrets be rotated at regular intervals. Rotation intervals MAY vary
  based on the risk profile of individual secrets, but SHOULD NOT
  exceed one week in most cases. Rotation SHOULD be automated.

- **Secrets MUST be narrowly-scoped.** A secret SHOULD have only a
  single use case, and therefore only one reason to be changed. Do not
  reuse the same secrets for different things. For example, for message
  encryption keys, generate asymmetric keys per user rather than
  distributing the same public key to all users. Narrowly-scoped secrets
  are inherently more secure and easier to rotate.

#### Handling compromised secrets

- **Secrets MUST be considered compromised if they are ever leaked** —
  including into code repositories (even private ones) and into logs
  (even if the logs are not publicly accessible).

- **Compromised secrets MUST be rotated immediately.** It is NOT
  sufficient to simply remove the secret from the environment into which
  it has leaked. Removing a secret from a code repository (even by
  rewriting history) is not sufficient — the secret has already been
  compromised and must be rotated.

- **Document the lifecycle of every secret.** For every secret, there
  SHOULD be a document that answers:
  - What is the secret's purpose?
  - How is it used?
  - Who has access to it?
  - How is it rotated, and how often?
  - How will it be invalidated in the event of the secret being leaked?

### Vulnerability scanning

- **Source code MUST be scanned for vulnerabilities prior to release.**

- **Use a combination of SAST and DAST.** It is RECOMMENDED to use a
  combination of Static Application Security Testing (SAST, eg.
  [Checkmarx](https://checkmarx.com/)) and Dynamic Application Security
  Testing (DAST, eg. [ZAP](https://www.zaproxy.org/)).

- **Third-party components MUST be checked for security vulnerabilities
  and license changes**, using a software composition analysis (SCA)
  tool such as [Mend](https://www.mend.io/).

- **Triage findings by severity.** High-level issues identified by
  vulnerability scanning tools SHOULD be prioritized similarly to
  incidents. Low-level issues SHOULD be prioritized with high priority.

### Threat modeling

- **Threat modeling SHOULD begin during the design phase** of a new
  software product, or of a major new feature within an existing
  product. Thereafter, threat models SHOULD be treated as living
  documents that are regularly revised as the system evolves, new
  threats emerge, or business requirements change.

- **Threat modeling requires cross-functional participation.**
  Architecture and security, product and business stakeholders, and
  development, testing, and operations teams should all participate to
  capture diverse perspectives.

For methodology and artifacts, see
[TS-54: Threat Modeling](../054/AGENTS.md).

### Authentication

- **Prefer token- or certificate-based authentication** over
  password-based authentication for user authentication.

- **Initial login requires strict requirements for user IDs and
  passwords, and two-factor authentication is strongly RECOMMENDED.**
  See constraints on inputs below.

- **Authentication operations MUST happen over a secure, encrypted
  channel** (eg. TLS). Session data from a prior non-encrypted
  connection MUST NOT be reused to authenticate a user.

- **Re-authentication MUST be required prior to destructive operations**
  such as deleting data, or performing any operation considered
  sensitive (eg. changing a password or email address).

- **Failed authentication attempts MUST be logged, and the logs MUST be
  monitored** for suspicious activity.

- **Restrict failed authentication attempts.** There SHOULD be sensible
  restrictions on the number of failed attempts permitted within a time
  window, to prevent brute-force attacks. For example, an account MAY
  be locked after three failed attempts in a 24-hour period.

- **Do not reveal why an authentication attempt failed.** A user MUST
  NOT be informed exactly why their attempt failed. The application
  MUST NOT indicate whether the user ID or password was incorrect, or
  whether a CAPTCHA code was input correctly.

#### User IDs

- User IDs MUST be at least four characters long and SHOULD be at least
  7 characters long.
- User IDs MUST be unique.

#### User passwords

- **Force password change on first login and after administrative
  password reset.** Users MUST be required to change their passwords on
  first login and after an administrative password reset. It is
  RECOMMENDED that users be _prompted_ (but not necessarily _required_)
  to change their passwords at regular intervals, such as every 90 days.

- **New passwords SHOULD NOT match any of the user's previous 12
  passwords.**

- **Validate password strength.** Passwords MUST be validated for their
  strength. A strong password is defined as:
  - At least 8 characters long.
  - Contains at least one uppercase ASCII letter, one lowercase ASCII
    letter, one number, and one special ASCII character (punctuation or
    symbol), or at least one Unicode character outside the ASCII range.
  - Does not contain dictionary words, common phrases, or common
    patterns (eg. "12345678", "password", "qwerty").
  - Does not contain the user's user ID, first name, last name, or any
    other personal information that could be easily guessed.

- **Provide password generation tools and strength meters.**
  Applications SHOULD include both password generation tools and
  password strength meters to help users choose strong passwords.

- **Mask password input fields.** In graphical user interfaces, input
  fields for passwords (and other secrets) MUST be masked to prevent
  display.

- **Hash and salt stored passwords.** Stored passwords MUST be hashed
  and salted using a strong hashing algorithm. The following steps MUST
  be followed:
  - Concatenate a salt with the user's password.
  - Perform a hash on the result using the SHA-3 algorithm, if
    supported, else SHA-2 (minimum 256-bit hash output in either case).

#### Reset password operations

- **Limit reset password frequency.** There SHOULD be sensible
  restrictions on the number of times a user can trigger a reset password
  operation within a time window. For example, no more than three times
  in any 24-hour period, without an administrative override.

- **Allow users to further secure their accounts.** It MUST be possible
  for users to disable the reset password functionality, or to require
  additional verification steps (such as mobile authentication) for
  reset password operations.

- **Use short-lived one-time tokens for reset.** Reset password
  operations should generate a short-lived one-time token sent via
  out-of-band communication (email or SMS), scoped to a change password
  operation. It is RECOMMENDED that this token be valid for no more than
  30 minutes.

- **Reset password operations MUST be logged, and the logs MUST be
  monitored** for suspicious activity.

- **Notify users of reset requests.** Users MUST be notified — via both
  out-of-band communication (email or SMS) and via the application's
  interface — when a reset password operation is triggered on their
  account. There MUST be a mechanism for users to report suspicious
  reset password requests and to immediately "lock" their account in
  the event of a suspected compromise.

#### CAPTCHA

- reCAPTCHA v2 or v3 MAY be implemented for user authentication
  operations, for additional security.

- **Display a CAPTCHA after a first failed authentication attempt**
  (RECOMMENDED). It is also RECOMMENDED to display a CAPTCHA for
  transactions that require elevated permissions, such as changing a
  password or performing a destructive operation.

### Authorization and access controls

- **Apply the principle of least privilege.** Access MUST be based on
  the principle of least privilege: clients (users and other systems)
  MUST only be granted the minimum permissions necessary to perform
  their tasks.

- **Use logical security roles.** Access MUST be based on logical
  security roles such as user, super user, administrator, and so on.
  This applies for both human and non-human access.

- **Always verify access on the server.** Web applications MUST NOT
  rely on hidden fields, URL parameters, cookie values, HTTP headers, or
  other obscurity techniques as the basis of authorization decisions,
  unless such values are corroborated with server-side information.
  Access MUST always be verified. It is not sufficient to simply "hide"
  operations from clients (eg. by not displaying a button in a UI or by
  not documenting an API endpoint).

- **Verify access before any operation is performed.** Access
  verification MUST take place prior to any operation (reading, writing,
  deleting) being performed.

### Network security

- **Limit inbound access from the public internet** to what is required
  by the application (ports, protocols, services).

- **Limit outbound traffic to what is required by the application.** It
  is RECOMMENDED that all outbound traffic be blocked by default and
  enabled only for specific IP addresses, IP ranges, or specific domain
  names. An outbound proxy MAY be used to enforce this.

### Web application security

#### Security headers

- **`Strict-Transport-Security` MUST be sent on each HTTP transaction.**
  The `max-age` directive MUST be set to at least 86400 (1 day).

- **`Content-Security-Policy` MUST be returned.** The RECOMMENDED
  baseline:
  - `default-src 'self'`
  - `object-src 'none'`
  - `frame-ancestors 'deny'`
  - `frame-src 'none'`
  - `base-url 'self'`
  - `form-action 'self'`

- **`X-XSS-Protection` SHOULD be sent** with each HTTP transaction in
  cases where `Content-Security-Policy` is not supported (legacy
  browsers). The value MUST be set to `1; mode=block`.

- **`X-Frame-Options` MUST be sent** with each HTTP transaction. Either
  the `deny` or `sameorigin` directive SHOULD be used.

- **`X-Content-Type-Options` MUST be sent** on each HTTP transaction.
  The `no-sniff` directive MUST be set.

#### Caching control

- **`Cache-Control` MUST be sent with each HTTP transaction.** The
  `max-age` directive MUST be sent unless `no-cache` is used. The
  `max-age` value must be set according to the sensitivity of the data
  being sent — higher sensitivity means lower `max-age`. The `max-age`
  MUST NOT be longer than 1 year.

- **`Expires` MUST be sent with each HTTP transaction**, with a value
  consistent with the `max-age` directive in `Cache-Control`.

#### Other data controls

- **Do not leave confidential data on the client after session
  termination** without explicit acknowledgement by the client/user.
  Examples of restricted storage: browser caches, browser URL
  histories, persistent memory objects, form autocomplete histories,
  client-side JARs, Active-X controls, Flash shared objects.

- **Disable browser and proxy caching when sending confidential or
  restricted information.** A combination of all three of the following
  headers is RECOMMENDED, to satisfy different browsers:
  - `Pragma=nocache`
  - `Expires="01 Jan 1971 01:01:01 GMT"`
  - `Cache-Control="no-store"`

- **Disable autocomplete on forms that input confidential or restricted
  information.**

- **Interpreted client-side code MUST NOT contain hard-coded passwords,
  usernames, or database connection strings.**

- **Non-sensitive client-side data storage rules.** If non-sensitive
  data needs to be stored on the client:
  - Data that is not intended for public access MUST be encrypted.
  - Data MUST NOT be stored in world-readable/writable locations.
  - Data MUST be purged when it is no longer required.

- **One-time-viewable file content.** Web applications that generate
  file-based content intended for one-time viewing MUST remove access to
  the file immediately after it is retrieved by the user. The request to
  access the file MUST be validated to prevent unauthorized access.

- **Confidential data MUST NOT be sent via SMS, email, or push
  notifications.**

## References

- [TS-52: Security and Secrets Management (source)](README.adoc)
- [TS-10: Releasing](../010/AGENTS.md)
- [TS-51: Amazon Web Services (AWS)](../051/AGENTS.md)
- [TS-53: Privacy and Data Protection](../053/AGENTS.md)
- [TS-54: Threat Modeling](../054/AGENTS.md)
- [TS-55: Authentication and Authorization](../055/AGENTS.md)
- [TS-56: JSON Web Tokens (JWTs)](../056/AGENTS.md)
- [TS-57: Logging, Monitoring, Observability](../057/AGENTS.md)
- [HashiCorp Vault](https://vaultproject.io)
- [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)
- [Checkmarx (SAST)](https://checkmarx.com/)
- [ZAP (DAST)](https://www.zaproxy.org/)
- [Mend (SCA)](https://www.mend.io/)