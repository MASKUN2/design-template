# {{PROJECT_NAME}} — Product Specification

The **what** and the **why** of {{PROJECT_NAME}}: its purpose, the features it
must provide, and the rules that govern them. Intentionally free of
implementation detail — no frameworks, file paths, or code. When behaviour and
this document disagree, treat it as a bug in one of them and reconcile — this is
the source of truth for **intent**.

## Contents

| File | Covers |
|---|---|
| **this file** | §1 Purpose & Vision, §2 Actors, §3 Domain Concepts, §8 Out of Scope, §9 Glossary |
| [`functional.md`](./functional.md) | §4 Functional Requirements |
| [`policies.md`](./policies.md) | §5 Policies & Business Rules, §6 Non-Functional Requirements |
| [`ui-design.md`](./ui-design.md) | §7 UI & Visual Design |

Related artifacts: [`../glossary.csv`](../glossary.csv),
[`../domain/`](../domain/), [`../api/openapi.yaml`](../api/openapi.yaml),
[`../wireframe/`](../wireframe/).

---

## 1. Purpose & Vision

> TODO(agent): what is {{PROJECT_NAME}}, for whom, and why does it exist?

### Goals
- TODO(agent)

### Non-Goals
- TODO(agent)

---

## 2. Actors

| Actor | Description | How they're identified |
|---|---|---|
| **{{Actor}}** | TODO(agent) | TODO(agent) |

---

## 3. Domain Concepts

Define each core concept in one or two sentences. Every **aggregate root** here
must have a file in [`../domain/`](../domain/) and a `Domain` row in
[`../glossary.csv`](../glossary.csv).

- **Item** — *EXAMPLE* — the central unit of content/data. Replace/delete.

---

## 8. Out of Scope (this version)

- TODO(agent): explicitly list what is NOT being built, to bound the work.

---

## 9. Glossary

The canonical, machine-readable glossary is [`../glossary.csv`](../glossary.csv).
Keep the `Domain` rows in sync with the aggregate roots.
