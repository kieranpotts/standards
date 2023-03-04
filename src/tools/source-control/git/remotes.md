# Remotes

It is strongly RECOMMENDED to use SSH to connect to all remote Git repositories. Both SSH and HTTPS are secure protocols for communication between client and server Git hosts, but public/private key authentication tends to be more convenient and a better user experience. It makes scripting easier as you do not need to rely on Git's built-in [credentials manager](https://help.github.com/articles/caching-your-github-password-in-git) to have your password cached. And, if a private key has been compromised, you can simply revoke the public key without needing to change your password.
