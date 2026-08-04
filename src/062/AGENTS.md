# TS-62: Make

This is a compact version of technical standard TS-62 for AI agents.

Use this skill when authoring or modifying `Makefile`s, including project task
runners built on GNU Make.

For the shell scripts and recipes invoked from within Makefile targets, see
[POSIX standards](../031/AGENTS.md) and [Bash standards](../032/AGENTS.md) -
those rules apply to `Makefile` recipe bodies too. For guidance on the
targets themselves as a user-facing interface, see
[CLI standards](../016/AGENTS.md).

## Rules

- **Make the Makefile self-documenting.**

  Add a `##` comment on the same line as any user-facing target, describing
  what it does in a short sentence:

  ```makefile
  install: ## Install project dependencies
  	npm install

  test: ## Run the test suite
  	npm test
  ```

  Do not add a `##` comment to internal/implementation-detail targets not
  meant to be invoked directly - this keeps generated help output focused.

- **Add a `help` target that parses the `##` comments.**

  ```makefile
  help: ## Show this help message
  	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
  ```

  Always use `$(MAKEFILE_LIST)`, not a hardcoded filename - it expands to all
  Makefiles actually read for the invocation, including `include`d files.

- **Set `help` as the default goal.**

  ```makefile
  .DEFAULT_GOAL := help
  ```

  This makes plain `make` (no arguments) show the command list, instead of
  running whichever target happens to be declared first in the file.

- **Declare phony targets explicitly.**

  Any target that does not produce a file matching its own name MUST be
  listed under `.PHONY`, to avoid Make skipping it if a file of that name ever
  exists in the working directory:

  ```makefile
  .PHONY: install test help
  ```

## Examples

```makefile
.DEFAULT_GOAL := help

install: ## Install project dependencies
	npm install

test: ## Run the test suite
	npm test

build: ## Build the production bundle
	npm run build

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: install test build help
```
