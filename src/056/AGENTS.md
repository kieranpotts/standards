# TS-56: JSON Web Tokens (JWTs)

Best practices for designing the schema for JSON Web Tokens (JWTs), used
for stateless authentication and authorization. The goal is tokens that
are secure, contain sufficient information for authorization decisions,
and remain lightweight without exposing sensitive data unnecessarily.

Use this when designing, implementing, or reviewing JWT-based
authentication or authorization systems.

Do NOT use this for stateful authentication (session tracking, complex
state management) — JWTs are probably not the appropriate solution in
those cases. For general security and secrets management, see
[TS-52: Security and Secrets Management](../052/AGENTS.md). For
authentication and authorization patterns more broadly, see
[TS-55: Authentication and Authorization](../055/AGENTS.md). For privacy
and PII handling, see
[TS-53: Privacy and Data Protection](../053/AGENTS.md). For HTTP API
design (where JWTs are commonly transported), see
[TS-21: HTTP APIs](../021/AGENTS.md). For general code design, see
[TS-7: Code Design](../007/AGENTS.md).

## Rules

### Statelessness

- **JWTs MUST be designed to contain all necessary claims for
  authentication and authorization**, such that no external database
  lookups — or requests to external auth services — are required for
  authentication and validation of users. JWTs are specifically intended
  for stateless authentication and authorization.

### Secrets and PII

- **Secrets (API keys, passwords) and personally identifiable
  information (PII) MUST NOT be included in JWT payloads.** JWTs are
  base64-encoded, not encrypted, and can be easily decoded by anyone
  with access to a compromised token.

- **JWTs MUST be transmitted over secure channels** (eg. HTTPS) to
  prevent interception during transmission. This applies to private
  networks as much as public networks like the internet.

### Token size

- **JWTs MUST be kept as small as possible** to reduce bandwidth usage,
  since they are sent with every request in stateless authentication
  scenarios. Smaller tokens are also inherently less risky because they
  expose less information if intercepted.

- **Encode only what is absolutely necessary.** The information encoded
  in a JWT MUST be limited to what is necessary for effective
  authentication and authorization — no more. There MUST NOT be any
  excessive or redundant data included in a token, even if the data is
  not sensitive or is encrypted.

### Claims

- **Repurpose standard claims where possible** (RECOMMENDED). Using
  standard JWT schema means higher interoperability with existing and
  future libraries and services. Standardized claims:
  - `iss` (issuer): Identifies the entity that issued the token.
  - `sub` (subject): Typically the user ID or unique identifier for the
    subject of the token.
  - `aud` (audience): Specifies the intended recipients or services for
    which the token is valid.
  - `exp` (expiration): Sets the expiration time, after which the token
    is no longer valid.
  - `iat` (issued at): Indicates the time at which the token was issued.
  - `nbf` (not before): Indicates the time before which the token must
    not be accepted for processing.
  - `jti` (JWT ID): A unique identifier for the token, useful for
    preventing replay attacks and managing token revocation.

### Roles and permissions

- **Encode fine-grained _scopes_ rather than broad roles.** Scopes are
  specific permissions (eg. `read:posts`, `write:comments`). This allows
  more granular control over what actions a user can perform with a
  token, and tokens can be tailored to specific actions or resources
  rather than relying on broad roles like "admin" or "user".

- **Consider how to represent hierarchical permissions**, where a user
  might inherit permissions from a parent role or group.

### Token lifetime

- **Tokens MUST have a defined expiration time** (using the `exp` claim)
  to restrict their validity period. This is crucial for security, as it
  reduces the window of opportunity for an attacker to use a compromised
  token.

- **Balance security and user experience.** A balance must be found
  between security (shorter expiration times) and user experience (less
  frequent re-authentication). The optimum balance depends on the
  application domain and its security requirements.

### Refresh strategy

- **Refresh tokens are used in conjunction with access tokens** to
  allow users to maintain a session after token expiry without needing
  to re-authenticate frequently. A refresh token obtains a new access
  token when the current one expires.

- **Refresh tokens are longer lived than access tokens.** Their lifetime
  SHOULD be carefully considered, again balancing security and user
  experience.

- **Other refresh considerations:** which claims need to persist across
  token refreshes, and how to handle revocation of refresh tokens.

### Other considerations

- **JWTs MUST be signed** to ensure integrity and authenticity. Use a
  strong signing algorithm such as RS256 or ES256, rather than weaker
  algorithms like HS256.

- **JWTs MAY be encrypted** to protect sensitive information, but this is
  not a requirement for all use cases. If encryption is used, ensure
  encryption keys are managed securely. Normally, transmitting JWTs over
  secure channels (HTTPS) is adequate. Encrypting JWTs themselves adds
  an additional layer of security but is likely only necessary where
  tokens are persisted at rest in insecure environments (which could
  include the client's own device and file system).

- **For multi-tenancy scenarios, consider including tenant or
  organization identifiers in the JWT claims** to scope tokens to the
  correct tenant. Important in SaaS applications where users from
  different organizations share the same application instance.

- **Consider including device fingerprints or session identifiers in the
  JWT claims** to provide additional context for a token. This can
  improve security by scoping tokens to a particular client device.

## References

- [TS-56: JSON Web Tokens (JWTs) (source)](README.adoc)
- [TS-7: Code Design](../007/AGENTS.md)
- [TS-21: HTTP APIs](../021/AGENTS.md)
- [TS-52: Security and Secrets Management](../052/AGENTS.md)
- [TS-53: Privacy and Data Protection](../053/AGENTS.md)
- [TS-55: Authentication and Authorization](../055/AGENTS.md)
- [RFC 7519: JSON Web Token (JWT)](https://datatracker.ietf.org/doc/html/rfc7519)