# design-template

A reusable, stack-agnostic **design surface**: a durable, human-readable
description of a product — spec, glossary, domain model, API contract, and UI
wireframes — plus a dependency-free linter that keeps those artifacts mutually
consistent. Built to be filled in by a human or an **AI agent**.

## Quick start

```bash
mkdir -p /path/to/your-repo/design && cp -R ./* /path/to/your-repo/design/
cd /path/to/your-repo/design && python3 validate.py   # stdlib only, no config
```

It validates green against a small worked example (`Item`), so you start passing
and edit down.

## Layout

```
├── README.md          # this file (overview + the agent protocol)
├── VERSION
├── validate.py        # consistency linter (auto-derive, no config)
├── glossary.csv       # term,category,definition
├── api/               # OpenAPI 3.1 contract
├── spec/              # the product spec (intent)
├── domain/            # Mermaid ER diagrams, one file per aggregate root
└── wireframe/         # one bare-wireframe HTML per screen + shared wireframe.css
```

Every directory carries its own short `README.md`.

## Validation

```bash
python3 validate.py        # full report      (-q for failures only)
```

Checks that the glossary's `Domain` terms match the aggregate roots, every
aggregate is diagrammed, the OpenAPI spec is 3.1 with unique operationIds and no
dangling `$ref`s, and the wireframes share `wireframe.css`, carry an annotation
note, use no remote assets, and are all linked from `index.html`. Non-zero exit
on any error — CI-friendly.

---

# For AI agents

You are turning this template into a real design surface. **Learn the shape from
the worked example** (`domain/item.md`, `wireframe/01-example.html`, the `/items`
paths and `Item` schema, the `Item` glossary row) — there are no separate
template files. Finish when `python3 validate.py` is green with no
`{{PLACEHOLDER}}` or `TODO(agent:)` left.

**Rules**

1. Spec is *intent*, not implementation — no frameworks, paths, or code in `spec/`.
2. `domain/`, `api/`, and `wireframe/` describe the real system — keep them in sync.
3. Keep `validate.py` green; run it often.

**Protocol**

1. Copy these files into a `design/` directory at your repo root; replace every
   `{{PROJECT_NAME}}`.
2. Write `spec/` (purpose, actors, domain, functional, policies, non-functional,
   UI). Resolve every `TODO(agent:)`.
3. Fill `glossary.csv` — one `Domain` row per aggregate root (the set must equal
   your `domain/*.md` files).
4. Model the domain: one `domain/<name>.md` per aggregate (Mermaid entity =
   filename UPPERCASED) plus the overview ERD in `domain/README.md`.
5. Write `api/openapi.yaml` (OpenAPI 3.1): one component schema per aggregate.
6. Draw one `wireframe/NN-<name>.html` per screen and link each from
   `index.html`.
7. Set `VERSION`; delete the `Item` example once real content replaces it.

**Wireframe conventions** — bare wireframes: link the shared `wireframe.css`
(no remote assets), one hairline gray border, system font, auto light/dark, no
colour/hover/shadow; a blue `<aside class="note">` at the top describing the
screen + route and linking back to `index.html`.

## Requirements

Python 3.8+ (standard library only).
