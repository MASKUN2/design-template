# api/

The HTTP **API contract**: [`openapi.yaml`](./openapi.yaml), an **OpenAPI 3.1**
description of the surface (paths, schemas, auth, errors).

Rule: one component schema per aggregate root (named like the
[`../domain/`](../domain/) file). It describes the contract only — keep it in
sync with the real API. See the `/items` example.
