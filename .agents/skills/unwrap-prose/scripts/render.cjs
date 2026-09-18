#!/usr/bin/env node
// Render AsciiDoc documents to HTML with Asciidoctor.js, for comparing a file
// before and after unwrapping.
//
// Usage: node render.cjs <path-to-@asciidoctor/core>
// Stdin: JSON object {id: asciidocText, ...}
// Stdout: JSON object {id: html, ...}

const corePath = process.argv[2];
if (!corePath) {
  console.error('usage: render.cjs <path-to-@asciidoctor/core>');
  process.exit(2);
}

const asciidoctor = require(corePath)();
// Silence warnings (eg. unresolvable `partial$` includes); they are identical
// before and after, and are not what this comparison is checking.
asciidoctor.LoggerManager.getLogger().setLevel(4);

let input = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', (chunk) => (input += chunk));
process.stdin.on('end', () => {
  const docs = JSON.parse(input);
  const out = {};
  for (const [id, text] of Object.entries(docs)) {
    out[id] = asciidoctor.convert(text, {
      safe: 'safe',
      attributes: { 'attribute-missing': 'skip' },
    });
  }
  process.stdout.write(JSON.stringify(out));
});
