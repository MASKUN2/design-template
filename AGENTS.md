# AGENTS.md — instantiating this design template

**You are an AI agent. This file tells you how to turn this template into a real
design surface for a specific project.** Follow it top to bottom. When you
finish, `python3 validate.py` must exit 0 with no `{{PLACEHOLDER}}` or
`TODO(agent:)` left outside `_TEMPLATE.*` files.

## What this is

A durable, human-readable description of *what* a product is and *how* it
behaves, versioned alongside the code but independent of it:

- `spec/` — the **intent** (purpose, actors, domain, functional requirements,
  policies, non-functional requirements, UI design system).
- `glossary.csv` — canonical domain vocabulary.
- `domain-model/` — Mermaid ER diagrams (overview + one file per aggregate root).
- `openapi.yaml` — the HTTP contract (OpenAPI 3.1).
- `wireframes/` — one self-contained bare-wireframe HTML per screen.
- `validate.py` — a stdlib, dependency-free linter that keeps the artifacts
  mutually consistent (no config needed; it auto-derives from the files).

## Golden rules

1. **Spec is intent, not implementation.** No framework names, file paths, or
   code inside `spec/`. Those belong in the repo's own README.
2. **Derived artifacts cite their source.** `domain-model/`, `openapi.yaml`, and
   `wireframes/` describe the real system — keep them in sync with it.
3. **Keep `validate.py` green.** It is the acceptance gate. Run it often.
4. **`_`-prefixed files are templates** (`_TEMPLATE.md`, `_TEMPLATE.html`) —
   `validate.py` ignores them. Keep them; copy them to add aggregates/screens.

## Instantiation protocol

Work in this order (each step feeds the next):

1. **Place it.** Copy these files into a `design/` directory at the target repo's
   root (this `AGENTS.md` and the top `README.md` are about *using* the template
   and need not be copied). Commands below assume you run them from that
   directory.
2. **Name it.** Replace every `{{PROJECT_NAME}}` with the real project name.
3. **Spec first (`spec/`).** Fill §1 Purpose, §2 Actors, §3 Domain Concepts (in
   `spec/README.md`), §4 (`functional.md`), §5–6 (`policies.md`), §7
   (`ui-design.md`). Replace every remaining `{{PLACEHOLDER}}` and resolve every
   `TODO(agent:)`. Number policies so other docs can cite them.
4. **Glossary (`glossary.csv`).** One row per term. Every **aggregate root** gets
   a `Domain` row; the set of `Domain` terms MUST equal your aggregate files
   (validate.py enforces this).
5. **Domain model (`domain-model/`).** For each aggregate root, copy
   `_TEMPLATE.md` → `<aggregate>.md` (lowercase filename → capitalised display
   name; the Mermaid entity name is the display name UPPERCASED). Add every
   aggregate as an entity in `README.md`'s overview ERD and draw the
   relationships with crow's-foot cardinality.
6. **API (`openapi.yaml`).** Keep it OpenAPI **3.1**. Define one component schema
   per aggregate root (same name), unique `operationId`s, no dangling `$ref`s.
7. **Wireframes (`wireframes/`).** For each screen, copy `_TEMPLATE.html` →
   `NN-<name>.html` (two-digit prefix). Follow the conventions (below). Link
   every screen from `index.html`.
8. **Version.** Set `VERSION` (start `1.0.0` for the first real cut).
9. **Delete the worked example**: `domain-model/item.md`, the `Item`
   rows/schema/paths in `glossary.csv` + `openapi.yaml`, and
   `wireframes/01-example.html` (and its `index.html` link) — once real content
   replaces them. Keep the `_TEMPLATE.*` files.
10. **Prove it.** Run `python3 validate.py` until it PASSES, then do the
    acceptance sweep below.

## Wireframe conventions (`wireframes/*.html`)

Bare wireframes — structure and copy over styling, so a mockup is never mistaken
for final visual design:

- **Self-contained**: inline `<style>` only; no external assets/fonts/CDN.
- **Minimal CSS**: one hairline `1px solid gray` border for all frames/dividers,
  system font, one `foreground`/`background` pair, auto light/dark via
  `@media (prefers-color-scheme: dark)`. No colour, hover, shadow, or radius.
- **Annotation**: a blue `<aside class="note">` at the top (never a `<footer>` —
  the real app may use that) describing the screen + its route, linking back to
  `index.html`.

## Acceptance criteria

- `python3 validate.py` → exit 0, `PASS`.
- `grep -rn "{{" . | grep -v _TEMPLATE` → nothing (no placeholders left, except
  inside the kept templates).
- `grep -rni "TODO(agent" . | grep -v _TEMPLATE` → nothing.
- No `EXAMPLE`/`Item` worked-example content remains (unless Item is a real
  aggregate).
- Every aggregate: has a `domain-model/*.md`, a `Domain` glossary row, and an
  OpenAPI component schema. Every screen: linked from `index.html`.

## Scope note

This template does **not** ship a source↔design *conformance* checker (does the
code match the spec?) — that is framework-specific. If the project wants one,
adapt the inhology project's `design/conformance.py` (NestJS + Next.js
reference: parses controllers vs `openapi.yaml`, guards vs `security`, and
documented screens vs real routes).
