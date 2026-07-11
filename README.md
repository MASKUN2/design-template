# design-template

A reusable, project-agnostic **design surface** — a durable, human-readable
description of a product (spec, glossary, domain model, API contract, UI
wireframes) plus a stdlib linter that keeps those artifacts mutually consistent.

Extracted from the [inhology](https://github.com/MASKUN2/inhology) project so it
can be dropped into any new repo. Designed to be filled in by a **human or an AI
agent** — the agent protocol is [below](#for-ai-agents--instantiation-protocol).

## Quick start

```bash
# 1. Copy the artifacts into a design/ folder in your repo
#    (everything here except this README.md)
mkdir -p /path/to/your-repo/design
cp -R spec domain wireframe api glossary.csv validate.py VERSION \
      /path/to/your-repo/design/

# 2. Point an AI agent at it (or do it yourself) — follow the protocol below.

# 3. Validate (stdlib Python 3 only — no install, no config)
cd /path/to/your-repo/design && python3 validate.py
```

Out of the box it validates green against a tiny worked example (`Item`), so you
start from a passing state and edit down.

## Layout

```
design-template/
├── README.md          # this file: overview + the AI-agent protocol
├── VERSION            # 0.1.0
├── validate.py        # stdlib consistency linter (auto-derive, no config)
├── glossary.csv       # term,category,definition
├── api/               # README + openapi.yaml (OpenAPI 3.1, + /items example)
├── spec/              # README (§1-3,8,9) + functional + policies + ui-design
├── domain/            # README (overview ERD) + _TEMPLATE.md + item.md (example)
└── wireframe/         # README + index.html + _TEMPLATE.html + 01-example.html
```

Every child directory carries its own `README.md`.

## Artifacts

| Artifact | What it is |
|---|---|
| [`spec/`](./spec/) | **Product specification** — purpose, actors, functional requirements, policies, non-functional requirements, and the visual-design system. Source of truth for **intent**. |
| [`glossary.csv`](./glossary.csv) | **Glossary** — machine-readable domain terms. |
| [`domain/`](./domain/) | **Domain model** — Mermaid ER diagrams: overview + one file per aggregate root. |
| [`api/`](./api/) | **API contract** — OpenAPI 3.1 (`api/openapi.yaml`). |
| [`wireframe/`](./wireframe/) | **UI mockups** — one self-contained bare-wireframe HTML per screen + `index.html`. |
| [`validate.py`](./validate.py) | **Consistency linter** (stdlib only). |

## Validation

```bash
python3 validate.py        # full report
python3 validate.py -q     # failures + summary only
```

Layer by layer: the glossary parses and its `Domain` terms match the aggregate
roots; every aggregate is diagrammed in `domain/` (overview + own file); the
OpenAPI spec is 3.1, has unique operationIds, no dangling `$ref`s, and a
component schema per aggregate; and the wireframes are self-contained, carry an
`<aside class="note">`, avoid `<footer>`, and are all linked from `index.html`.
Non-zero exit on any error, so it drops into CI.

---

# For AI agents — instantiation protocol

**You are an AI agent turning this template into a real design surface for a
specific project.** Follow this top to bottom. When you finish, `python3
validate.py` must exit 0 with no `{{PLACEHOLDER}}` or `TODO(agent:)` left outside
`_TEMPLATE.*` files.

## Golden rules

1. **Spec is intent, not implementation.** No framework names, file paths, or
   code inside `spec/`. Those belong in the repo's own README.
2. **Derived artifacts cite their source.** `domain/`, `api/openapi.yaml`, and
   `wireframe/` describe the real system — keep them in sync with it.
3. **Keep `validate.py` green.** It is the acceptance gate. Run it often.
4. **`_`-prefixed files are templates** (`_TEMPLATE.md`, `_TEMPLATE.html`) —
   `validate.py` ignores them. Keep them; copy them to add aggregates/screens.

## Protocol

Work in this order (each step feeds the next):

1. **Place it.** Copy these artifacts into a `design/` directory at the target
   repo's root (this `README.md` is about *using* the template and need not be
   copied). Run the commands below from that directory.
2. **Name it.** Replace every `{{PROJECT_NAME}}` with the real project name.
3. **Spec first (`spec/`).** Fill §1 Purpose, §2 Actors, §3 Domain Concepts (in
   `spec/README.md`), §4 (`functional.md`), §5–6 (`policies.md`), §7
   (`ui-design.md`). Replace every remaining `{{PLACEHOLDER}}` and resolve every
   `TODO(agent:)`. Number policies so other docs can cite them.
4. **Glossary (`glossary.csv`).** One row per term. Every **aggregate root** gets
   a `Domain` row; the set of `Domain` terms MUST equal your aggregate files.
5. **Domain model (`domain/`).** For each aggregate root, copy `_TEMPLATE.md` →
   `<aggregate>.md` (lowercase filename → capitalised display name; the Mermaid
   entity name is the display name UPPERCASED). Add every aggregate as an entity
   in `README.md`'s overview ERD and draw the relationships (crow's-foot).
6. **API (`api/openapi.yaml`).** Keep it OpenAPI **3.1**. Define one component
   schema per aggregate root (same name), unique `operationId`s, no dangling
   `$ref`s.
7. **Wireframes (`wireframe/`).** For each screen, copy `_TEMPLATE.html` →
   `NN-<name>.html` (two-digit prefix). Follow the conventions below. Link every
   screen from `index.html`.
8. **Version.** Set `VERSION` (start `1.0.0` for the first real cut).
9. **Delete the worked example**: `domain/item.md`, the `Item`
   rows/schema/paths in `glossary.csv` + `api/openapi.yaml`, and
   `wireframe/01-example.html` (and its `index.html` link) — once real content
   replaces them. Keep the `_TEMPLATE.*` files.
10. **Prove it.** Run `python3 validate.py` until it PASSES, then do the
    acceptance sweep below.

## Wireframe conventions (`wireframe/*.html`)

- **Self-contained**: inline `<style>` only; no external assets/fonts/CDN.
- **Minimal CSS**: one hairline `1px solid gray` border for all frames/dividers,
  system font, one `foreground`/`background` pair, auto light/dark via
  `@media (prefers-color-scheme: dark)`. No colour, hover, shadow, or radius.
- **Annotation**: a blue `<aside class="note">` at the top (never a `<footer>` —
  the real app may use that) describing the screen + its route, linking back to
  `index.html`.

## Acceptance criteria

- `python3 validate.py` → exit 0, `PASS`.
- `grep -rn "{{" . | grep -v _TEMPLATE` → nothing.
- `grep -rni "TODO(agent" . | grep -v _TEMPLATE` → nothing.
- No `EXAMPLE`/`Item` worked-example content remains (unless Item is real).
- Every aggregate: a `domain/*.md`, a `Domain` glossary row, and an OpenAPI
  component schema. Every screen: linked from `index.html`.

## Scope note

This template does **not** ship a source↔design *conformance* checker (does the
code match the spec?) — that is framework-specific. If the project wants one,
adapt the inhology project's `design/conformance.py` (NestJS + Next.js reference:
parses controllers vs `openapi.yaml`, guards vs `security`, and documented
screens vs real routes).

---

## Design decisions

- **Stack-agnostic, zero-config.** `validate.py` checks the artifacts against
  *each other* only; it assumes no framework and needs no config file.
  Aggregates are derived from `domain/*.md`, screens from `wireframe/NN-*.html`;
  `_`-prefixed files are ignored.
- **No source↔design conformance checker** (that's framework-bound; see above).

## Requirements

Python 3.8+ (standard library only). No dependencies to install.
