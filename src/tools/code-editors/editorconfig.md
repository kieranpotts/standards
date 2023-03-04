# EditorConfig

[EditorConfig](https://editorconfig.org/) is a standard for defining a baseline configuration for code editing environments that can be shared via code repositories and automatically plugged in to each developer's preferred programming application.

The project consists of a file format and a suite of plugins for the most popular IDEs and text editors.

It is RECOMMENDED that every Git repository has an `.editorconfig` file in the root directory, with contents based on the following configuration:

```ini
; ------------------------------------------------------------------------------
; This file helps to enforce a consistent coding style across different editors.
; https://editorconfig.org/
; ------------------------------------------------------------------------------

root = true                           # Place this file in the project root.

[*]                                   # Defaults:
charset = utf-8                       # - Files are UTF-8 encoded.
end_of_line = lf                      # - Files use Unix line endings.
indent_style = space                  # - Use spaces for indentation.
indent_size = 2                       # - Each indent should contain two spaces.
insert_final_newline = true           # - For VCS, end files with an empty line.
max_line_length = 120                 # - Lines should not exceed this length.
trim_trailing_whitespace = true       # - No whitespace on the end of lines.

[*.bat]                               # Windows Batch files:
end_of_line = crlf                    # - Require \r\n line endings.

[{Makefile,*.mk}]                     # Makefiles:
indent_style = tab                    # - Require tabs for indentation.

[*.md]                                # Markdown files:
trim_trailing_whitespace = false      # - Leave trailing whitespace.

[*.php]                               # PHP files:
indent_size = 4                       # - 4-space indents are conventional.

[*.py]                                # Python files:
indent_size = 4                       # - 4-space indents are conventional.
```
