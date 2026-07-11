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
├── README.md          # this file (overview)
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

To instantiate, fill in the artifacts by analysing the worked example (`Item`)
and `validate.py`; finish when the validator is green with no `{{PLACEHOLDER}}`
left.

## Requirements

Python 3.8+ (standard library only).
