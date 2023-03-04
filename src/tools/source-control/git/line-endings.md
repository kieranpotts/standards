# Line endings

In a distributed source control system such as Git, it is important to ensure consistent configuration of the source control system across different operating systems, particularly between Windows and Unix-based operating systems.

The main concern in cross-platform utilization of Git is how Git handles line endings. Windows uses both a carriage-return (CR) character and a linefeed (LF) character for newlines, whereas Mac and Linux systems use only the linefeed character. Many text editors on Windows silently replace existing LF-style line endings with CRLF, or insert both line-ending characters when the user hits the Enter key.

So, to maintain consistency in shared repositories, all text files checked-in to source control MUST use Unix line endings (`LF`), unless those files are intended to be compatible with the Windows operating system or a Windows-only application – eg `*.bat` files – in which case CRLF line endings MAY be present.

There is no good reason even to check out files with `CR+LF` endings on Windows, since all modern code editors support Unix line endings out-of-the-box. This feature can be disabled in Git with the following configuration:

```sh
git config --global core.autocrlf false
```

This configuration MUST be used in conjunction with the following setting, which enables conversion of line endings to the Unix format on all files that Git auto-detects as being text based:

```sh
git config --global core.eol lf
```

(Exclude the `--global` parameter to configure the current Git repository only.)

Since there is no guarantee that all contributors to a project will have this configuration in their local Git installation, we MUST enforce conversion of files at the point they are checked in. This can be done with the following `.gitatttributes` configuration. This file MUST be committed to source control and it MUST be placed in the top-level directory of all source control repositories.

```ini
* text=auto eol=lf
```

This configuration auto-detects all types of text files and normalizes line endings to the Unix format. It will apply normalization first to the local working directory and, in turn, to committed files that are ultimately pushed to the remote reference repository.

Alternatively, to constrain line ending conversions to specific file types, such as plain text files:

```ini
*.txt text eol=lf
```

If this rule is added to a project retrospectively, one contributor MUST run `git add --renormalize .` from the root directory of the repository, and commit and distribute the resulting changeset. This will apply the new line ending normalization rule to everything under source control. (The `--renormalize` option is available since Git v2.16.)

In addition, it is strongly RECOMMENDED that all projects have an `.editorconfig` file, which is recognized by most modern code editors and prompts them to automatically create new files with the desired line endings. See **[EditorConfig](//github.com/kieranpotts/standards/blob/dev/src/tools/code-editors/editorconfig.md)**.

## Related links

- [Configuring Git to handle line endings](https://docs.github.com/en/get-started/getting-started-with-git/configuring-git-to-handle-line-endings) – GitHub Docs
