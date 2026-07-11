# design-template

A reusable, project-agnostic **design surface** — a durable, human-readable
description of a product (spec, glossary, domain model, API contract, UI
wireframes) plus a stdlib linter that keeps those artifacts mutually consistent.

Extracted from the [inhology](https://github.com/MASKUN2/inhology) project so it
can be dropped into any new repo. Designed to be filled in by a **human or an AI
agent** — the agent protocol is in **[`AGENTS.md`](./AGENTS.md)**.

## Quick start

```bash
# 1. Copy the artifacts into a design/ folder in your repo
#    (everything here except README.md and AGENTS.md)
mkdir -p /path/to/your-repo/design
cp -R spec domain-model wireframes glossary.csv openapi.yaml validate.py VERSION \
      /path/to/your-repo/design/

# 2. Point an AI agent at it (or do it yourself) — follow AGENTS.md.

# 3. Validate (stdlib Python 3 only — no install, no config)
cd /path/to/your-repo/design && python3 validate.py
```

Out of the box it validates green against a tiny worked example (`Item`), so you
start from a passing state and edit down.

## Layout

```
design-template/
├── README.md          # this file (human)
├── AGENTS.md          # the AI-agent instantiation protocol
├── VERSION            # 0.1.0
├── validate.py        # stdlib consistency linter (auto-derive, no config)
├── glossary.csv       # term,category,definition
├── openapi.yaml       # OpenAPI 3.1 skeleton (+ /items example)
├── spec/              # README · functional · policies · ui-design
├── domain-model/      # README (overview ERD) · _TEMPLATE.md · item.md (example)
└── wireframes/        # index.html · _TEMPLATE.html · 01-example.html
```

## Artifacts

| Artifact | What it is |
|---|---|
| [`spec/`](./spec/) | **Product specification** — purpose, actors, functional requirements, policies, non-functional requirements, and the visual-design system. Source of truth for **intent**. |
| [`glossary.csv`](./glossary.csv) | **Glossary** — machine-readable domain terms. |
| [`domain-model/`](./domain-model/) | **Domain model** — Mermaid ER diagrams: overview + one file per aggregate root. |
| [`openapi.yaml`](./openapi.yaml) | **API contract** — OpenAPI 3.1. |
| [`wireframes/`](./wireframes/) | **UI mockups** — one self-contained bare-wireframe HTML per screen + `index.html`. |
| [`validate.py`](./validate.py) | **Consistency linter** (stdlib only). |

## Validation

```bash
python3 validate.py        # full report
python3 validate.py -q     # failures + summary only
```

Layer by layer: the glossary parses and its `Domain` terms match the aggregate
roots; every aggregate is diagrammed in `domain-model/` (overview + own file);
the OpenAPI spec is 3.1, has unique operationIds, no dangling `$ref`s, and a
component schema per aggregate; and the wireframes are self-contained, carry an
`<aside class="note">`, avoid `<footer>`, and are all linked from `index.html`.
Non-zero exit on any error, so it drops into CI.

## Design decisions

- **Stack-agnostic, zero-config.** `validate.py` checks the artifacts against
  *each other* only; it assumes no framework and needs no config file.
  Aggregates are derived from `domain-model/*.md`, screens from
  `wireframes/NN-*.html`; `_`-prefixed files are ignored.
- **No source↔design conformance checker** (that's framework-bound). See
  inhology's `design/conformance.py` for a NestJS + Next.js reference.

## Requirements

Python 3.8+ (standard library only). No dependencies to install.
