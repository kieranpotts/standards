# TS-48: Environment Variables

Use of environment variables in applications.

Use this when designing or implementing application configuration that
uses environment variables.

Do NOT use this for general configuration management or release
mechanics — see [TS-10: Releasing](../010/AGENTS.md). For handling of
security credentials referenced by environment variables, see
[TS-52: Security and Secrets Management](../052/AGENTS.md). For general
code design, see [TS-7: Code Design](../007/AGENTS.md).

## Rules

- **Store environment-specific configuration in environment variables.**
  Environment-specific configuration MUST be stored in environment
  variables.

- **Provide sensible defaults, except for secrets.** Applications SHOULD
  provide sensible defaults for environment configuration options, except
  for options that store security credentials — these MUST be empty by
  default. The purpose is to simplify environment configuration.

- **Optimize defaults for production.** Configuration defaults SHOULD be
  set and optimized for the production environment, to reduce risks
  associated with missing configuration in production.

- **Treat environment configuration as external input.** Environment
  configuration MUST be treated as external input to an application.
  Values MUST be validated and sanitized before use. Tools such as
  [Pkl](https://pkl-lang.org/) can help define configuration schemas and
  validate environment configurations against them.

## References

- [TS-48: Environment Variables (source)](README.adoc)
- [TS-7: Code Design](../007/AGENTS.md)
- [TS-10: Releasing](../010/AGENTS.md)
- [TS-52: Security and Secrets Management](../052/AGENTS.md)
- [Pkl](https://pkl-lang.org/)