# {{Aggregate}} — aggregate root

<!--
  Copy this file to `<aggregate>.md` (lowercase filename → capitalised display
  name, e.g. order.md → "Order"). Files starting with "_" are ignored by
  validate.py, so keep this template around for adding more aggregates later.
  The Mermaid entity name MUST be the display name in UPPERCASE (e.g. ORDER).
-->

One-line description of what this aggregate is. See the [full ERD](./README.md)
and [spec §3](../spec/README.md#3-domain-concepts).

```mermaid
erDiagram
    {{AGGREGATE}} {
        string id PK
        string slug UK
        string title
        datetime createdAt
        datetime updatedAt
    }
```

## Attributes

| Field | Type | Optional | Notes |
|---|---|---|---|
| `id` | string | — | PK |
| `slug` | string | — | Unique, URL-safe |
| `title` | string | — | {{...}} |

## Relations

- TODO(agent): list relations to other aggregates + cardinality.

## Invariants & rules

- TODO(agent): the non-negotiable rules (cite [spec §5](../spec/policies.md)).
