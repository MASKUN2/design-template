# api/

The HTTP **API contract** for the project.

- [`openapi.yaml`](./openapi.yaml) — an **OpenAPI 3.1** description of every
  endpoint: paths, methods, request/response schemas, auth, and error shape.

## Conventions

- Keep the version at **3.1.x**.
- One **component schema per aggregate root** (same name as the
  [`../domain/`](../domain/) file), so `validate.py` can tie the contract to the
  domain model.
- Unique `operationId`s; no dangling `$ref`s (both enforced by `../validate.py`).
- This describes the contract only — it is derived from and must stay in sync
  with the real API.

> Ships with an example `/items` resource. Replace it with your own, then delete
> the `Item` schema/paths.
