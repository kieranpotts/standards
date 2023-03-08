# Loops

## Tips and tricks

### Labelled loops

It's rarely used, but you can use [labeled statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label) to identify loops. This is useful in nested loops as it allows you to specify which loop to `continue` or `break` out from.

```js
function loop () {
  dance:
  for (let i = 0; i < 4; i++) {
    for (let j = 0; j < 4; j++) {
      if (j === 2) {
        break dance;
      }
    }
  }
}
```
