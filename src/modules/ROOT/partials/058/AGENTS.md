# TS-58: Docker

Guidance on working with Docker: building images, tagging, labeling,
security, monitoring, and running containers.

Use this when designing Dockerfiles, building Docker images, or running
Docker containers.

Do NOT use this for general secrets management (encryption, rotation,
storage of secrets) — see
[TS-52: Security and Secrets Management](../052/AGENTS.md). For privacy
and PII handling, see [TS-53: Privacy and Data Protection](../053/AGENTS.md).
For infrastructure-as-code and environment management, see
[TS-49: Cloud Platform Engineering](../049/AGENTS.md). For versioning
practices (image versioning follows the same principles), see
[TS-11: Versioning](../011/AGENTS.md). For general code design, see
[TS-7: Code Design](../007/AGENTS.md).

## Rules

### Base images

- **Use a standard library of organization-approved base images.** Within
  an organization, all containers SHOULD be built from a standard library
  of organization-approved base images. This ensures all containers are
  built with the same security and compliance standards.

- **Use lightweight Linux distributions for base images** (RECOMMENDED),
  such as [Alpine Linux](https://alpinelinux.org/), to benefit from small
  size and fast boot-up times.

### Build process

- **Keep image size to a minimum.** Container builds SHOULD be designed
  to keep the image size to a minimum.

- **Clean up artifacts in the same layer.** Each instruction in a
  Dockerfile adds a layer to the image. You SHOULD `RUN` commands to
  clean up any artifacts you don't need before moving on to building the
  next layer.

- **Order Dockerfile instructions to maximize layer caching.** In
  development environments using volume mounts for source code, order
  instructions so that slow-changing dependencies are copied and
  installed before the frequently-changing application code. This allows
  Docker to cache the dependency layer and only rebuild from the
  application-copy layer onward.

  ```dockerfile
  FROM node:20

  RUN apt install imagemagick

  WORKDIR /app

  COPY package*.json .

  RUN npm install

  COPY . .
  ```

  With this ordering, `npm install` is re-run only when `package.json` or
  `package-lock.json` changes — not on every application file change.

- **Use multi-stage builds** (RECOMMENDED). Multi-stage builds are
  especially useful when configuring containers differently for different
  environments (dev, test, prod). They help keep layers as small as
  possible and reduce security attack vectors in production. See the
  [Docker multi-stage build docs](https://docs.docker.com/build/building/multi-stage/).

### Image tags

- **Version images and treat each version as immutable.** When creating
  images, it is RECOMMENDED to version them and treat each version as
  immutable. Rather than deleting images and replacing them with new
  ones, prefer to bump to a new version.

- **Use specific version tags rather than `:latest`.** Using a specific
  version is best practice in most use cases. This locks the container to
  a particular version of an image, preventing unexpected breaking
  changes.

  ```dockerfile
  FROM nginx:1.23
  ```

  Be explicit if you always want the latest version, even though
  `:latest` is the default tag:

  ```dockerfile
  FROM alpine:latest
  ```

### Image labels

- **Follow the [Label Schema](http://label-schema.org/) convention**
  (SHOULD). It is the most popular Docker labeling convention.
  Variables may need to be passed at runtime so that labels are
  up-to-date.

- **All labels are OPTIONAL**, although `org.label-schema.schema-version`
  is RECOMMENDED for all containers.

- **Recommended labels:**

  | Name | Description |
  |---|---|
  | `org.label-schema.build-date` | Date/time the image was built, formatted per RFC 3339. |
  | `org.label-schema.name` | A human-friendly name for the image. |
  | `org.label-schema.description` | Text description for the image, max 300 characters. |
  | `org.label-schema.vcs-url` | URL for the code repository from which the image was built. |
  | `org.label-schema.vcs-ref` | Identifier for the version from which the image was built (eg. Git commit SHA). |
  | `org.label-schema.version` | Release identifier for the contents of the image (eg. Git branch or version tag). |
  | `org.label-schema.schema-version` | The version of Label Schema in use, usually `1.0`. |
  | `org.label-schema.docker.cmd` | How to run a container based on the image (eg. `docker run -d -p 80:80 example`). |

### Security

- **Do not store access keys or other secrets within Docker containers.**
  Secrets stored in containers allow anyone with access to an image to
  inspect the layers and view the credentials.

- **Mount credentials at runtime.** If the containerized application
  requires credentials such as database passwords, these SHOULD be
  mounted at runtime.

  See [TS-52: Security and Secrets Management](../052/AGENTS.md).

### Monitoring

- **Application containers SHOULD contain a health check.** A basic
  implementation is a simple `curl` request against localhost to check
  that the server has started. Other health checks may confirm that SSL
  certificates are valid and current, and that database ports are open
  and responding. The appropriate checks vary by service.

  ```dockerfile
  HEALTHCHECK --interval=5m --timeout=3s \
    CMD curl -f http://localhost/ || exit 1
  ```

- **Health checks SHOULD NOT monitor the health of dependent services**
  such as databases. Health checks should report only on the status of
  the container and its application.

- **Health checks SHOULD be run frequently in production.**

### Running multiple processes

- **One service or application per container.** In general, there should
  be one service or application per container. Multiple containers can be
  started and connected using user-defined networks and shared volumes.
  It is best practice to separate areas of concern (databases, services
  in distributed systems) into separate containers.

- **A container has a single main process**, defined in `ENTRYPOINT`
  and/or `CMD` at the end of the Dockerfile. That service MAY fork into
  multiple processes (eg. a web server may spawn multiple worker
  processes). The container's main process is responsible for managing
  all the processes it starts.

- **Use `--init` if the main process does not gracefully stop child
  processes.** If the main process isn't well designed to gracefully stop
  child processes when the container exits, pass the `--init` option when
  running the container. This inserts a tiny init process as the main
  process, which handles "reaping" of all processes when the container
  exits.

- **If more than one service is genuinely needed in a container**, there
  are two main approaches:
  - Use a wrapper script as the main `CMD` process.
  - Use a process manager like `supervisord`.

  See the [Docker multi-service container docs](https://docs.docker.com/engine/containers/multi-service_container/).

## References

- [TS-58: Docker (source)](../../pages/058.adoc)
- [TS-7: Code Design](../007/AGENTS.md)
- [TS-11: Versioning](../011/AGENTS.md)
- [TS-49: Cloud Platform Engineering](../049/AGENTS.md)
- [TS-52: Security and Secrets Management](../052/AGENTS.md)
- [TS-53: Privacy and Data Protection](../053/AGENTS.md)
- [Docker multi-stage build docs](https://docs.docker.com/build/building/multi-stage/)
- [Docker multi-service container docs](https://docs.docker.com/engine/containers/multi-service_container/)
- [Label Schema convention](http://label-schema.org/)
- [Alpine Linux](https://alpinelinux.org/)