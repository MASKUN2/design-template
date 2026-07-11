# {{PROJECT_NAME}} — Product Specification

The **what** and the **why** of {{PROJECT_NAME}}: its purpose, the features it
must provide, and the rules that govern them. Free of implementation detail — no
frameworks, file paths, or code. The source of truth for **intent**.

## Contents

| File | Covers |
|---|---|
| **this file** | §1 Purpose & Vision, §2 Actors, §3 Domain Concepts, §8 Out of Scope, §9 Glossary |
| [`functional.md`](./functional.md) | §4 Functional Requirements |
| [`policies.md`](./policies.md) | §5 Policies & Business Rules, §6 Non-Functional Requirements |
| [`ui-design.md`](./ui-design.md) | §7 UI & Visual Design |

Related: [`../glossary.csv`](../glossary.csv), [`../domain/`](../domain/),
[`../api/openapi.yaml`](../api/openapi.yaml), [`../wireframe/`](../wireframe/).

---

## 1. Purpose & Vision

{{PROJECT_NAME}} is a small content-publishing site for a single author. The
author writes **Posts**, keeps them private as drafts, and publishes them when
ready; anyone on the web can read what's published. It optimises for a
frictionless write-and-publish loop and a fast, clean reading experience.

### Goals
- A low-friction authoring loop: draft, preview, publish.
- A fast, readable public site.
- Simple enough for one person to run and maintain.

### Non-Goals
- Multiple authors or roles beyond *author* vs *reader*.
- Social features, feeds, or recommendations.
- A rich WYSIWYG editor (content is plain text / Markdown).

---

## 2. Actors

| Actor | Description | How they're identified |
|---|---|---|
| **Author** | The single privileged user. Creates, edits, publishes, and deletes posts. | Authenticated (a single admin credential). |
| **Reader** | Anyone on the public web. Reads published posts. | Anonymous — no account. |

---

## 3. Domain Concepts

- **Post** — the central unit of content: a titled article with a URL slug and a
  publication state (draft or published). The only aggregate root.

---

## 8. Out of Scope (this version)

- Comments or any reader-generated content.
- Multiple authors, accounts, or permissions.
- Full-text search, tags, or categories.
- Scheduled publishing and feeds (RSS/Atom).

---

## 9. Glossary

Canonical vocabulary: [`../glossary.csv`](../glossary.csv). The `Domain` rows are
the aggregate roots.
