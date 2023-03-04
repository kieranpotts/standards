# Remotes

## Connections

It is strongly RECOMMENDED to use SSH to connect to all remote Git repositories. Both SSH and HTTPS are secure protocols for communication between client and server Git hosts, but public/private key authentication tends to be more convenient and a better user experience. It makes scripting easier as you do not need to rely on Git's built-in [credentials manager](https://help.github.com/articles/caching-your-github-password-in-git) to have your password cached. And, if a private key has been compromised, you can simply revoke the public key without needing to change your password.

It is RECOMMENDED that, for the purpose of authenticated with Git servers, you use a private key that is NOT protected by a passphrase. That's because many automation tools, including VS Code's built-in Git client, do not work well with passphrase-protected private SSH keys. This means, however, that it is especially important that private keys are kept securely on client devices. Private keys MUST NOT be backed up on public cloud services. If possible, expiry times of up to 12 months SHOULD be applied to public keys when they are enabled in remote Git hosting services like GitLab.

## Credentials management

Git has a built-in [credentials manager](https://help.github.com/articles/caching-your-github-password-in-git) that will remember the usernames and passwords needed to access remote repositories over HTTPS. The credentials manager runs a daemon process that caches your credentials in memory and hands them out on demand.

It is RECOMMENDED to disable the Git credentials manager. Doing so will encourage authentication with private repositories to happen over SSH instead of HTTPS.

To disable the credentials manager globally:

```sh
git config --global --unset credential.helper
```

For some versions of Git For Windows, you will need to issue a different command, and with the console running under administrator privileges:

```sh
git config --system --unset credential.helper
```

Alternatively, you can fully delete the credential manager program:

```sh
git credential-manager uninstall
```

To disable credentials caching on a per-repository basis, override the global settings like this:

```sh
git config credential.helper ""
```

To check, run `git config --list` and verify there is no entry called "credential.helper".
