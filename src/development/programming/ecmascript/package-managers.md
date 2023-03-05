# Package managers for ECMAScript applications

[Yarn](https://yarnpkg.com/) is my preferred package manager for ECMAScript applications, libraries and development toolchains that run in runtime environments like Node. Although Yarn and NPM – the built-in Node Package Manager – pretty much have feature parity now, I tend to find Yarn the easiest of the two to use.

All contributors to an ECMAScript project SHOULD use the same package manager. That's because Yarn and NPM resolve dependencies differently, and so can produce different dependency trees within the `node_modules` directory.
