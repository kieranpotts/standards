# Types

## Dates

When dealing with date and time values, APIs SHOULD use ISO 8601-formatted strings.

```json
{
  "published_at": "2022-03-03T21:59:08Z"
}
```

Rendering of timezone-specific times is a concern that SHOULD be delegated to client applications.
