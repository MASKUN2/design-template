#!/usr/bin/env python3
"""
Validate the design artifacts for internal consistency.

Project-agnostic and dependency-free: this script checks that the artifacts in
this directory agree WITH EACH OTHER. It makes no assumption about your tech
stack, and needs no configuration.

Layers, in dependency order:

    glossary.csv  ->  domain/  ->  api/openapi.yaml + wireframe/

Aggregates are auto-derived from domain/*.md and screens from
wireframe/NN-*.html. Files whose name starts with "_" (e.g. _TEMPLATE.md) are
ignored everywhere.

Stdlib only. Run:
    python3 validate.py            # full report
    python3 validate.py -q         # failures + summary only

Exit code: 0 = consistent (warnings allowed), 1 = at least one error.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

QUIET = "-q" in sys.argv or "--quiet" in sys.argv


# --------------------------------------------------------------------------- #
# Reporting
# --------------------------------------------------------------------------- #
class Report:
    def __init__(self):
        self.errors = 0
        self.warnings = 0
        self.checks = 0

    def layer(self, title):
        print(f"\n\033[1m{title}\033[0m")

    def ok(self, msg):
        self.checks += 1
        if not QUIET:
            print(f"  \033[32m✓\033[0m {msg}")

    def warn(self, msg):
        self.checks += 1
        self.warnings += 1
        print(f"  \033[33m⚠\033[0m {msg}")

    def fail(self, msg):
        self.checks += 1
        self.errors += 1
        print(f"  \033[31m✗\033[0m {msg}")

    def check(self, cond, ok_msg, fail_msg, warn=False):
        if cond:
            self.ok(ok_msg)
        elif warn:
            self.warn(fail_msg)
        else:
            self.fail(fail_msg)
        return bool(cond)


def read(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return None


# --------------------------------------------------------------------------- #
# Derivation (ignore "_"-prefixed template files)
# --------------------------------------------------------------------------- #
def derive_aggregates() -> list[str]:
    names = []
    for f in sorted((ROOT / "domain").glob("*.md")):
        if f.name == "README.md" or f.name.startswith("_"):
            continue
        names.append(f.stem[:1].upper() + f.stem[1:])
    return names


def screen_files() -> list[Path]:
    # NN-*.html — the leading digits already exclude index.html and _TEMPLATE.html
    return sorted((ROOT / "wireframe").glob("[0-9][0-9]-*.html"))


def mermaid_entities(text: str) -> set[str]:
    return set(re.findall(r"(?m)^\s*([A-Z][A-Z0-9_]+)\s*\{", text))


# --------------------------------------------------------------------------- #
# OpenAPI (regex-based; no YAML dependency)
# --------------------------------------------------------------------------- #
def block_children(text: str, header: str) -> list[str]:
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if re.match(rf"^  {header}:\s*$", line):
            start = i + 1
            break
    if start is None:
        return []
    keys = []
    for line in lines[start:]:
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip())
        if indent <= 2:
            break
        m = re.match(r"\s{4}(\w+):", line)
        if m and indent == 4:
            keys.append(m.group(1))
    return keys


def parse_openapi(text: str) -> dict:
    ver = re.search(r"openapi:\s*([\d.]+)", text)
    return {
        "version": ver.group(1) if ver else None,
        "operation_ids": re.findall(r"operationId:\s*(\w+)", text),
        "schemas": block_children(text, "schemas"),
        "responses": block_children(text, "responses"),
        "schema_refs": set(re.findall(r"#/components/schemas/(\w+)", text)),
        "response_refs": set(re.findall(r"#/components/responses/(\w+)", text)),
    }


# --------------------------------------------------------------------------- #
# Layers
# --------------------------------------------------------------------------- #
def check_glossary(r: Report, aggregates):
    r.layer("1. Glossary  (glossary.csv)")
    text = read(ROOT / "glossary.csv")
    if text is None:
        r.fail("glossary.csv not found")
        return
    rows = list(csv.DictReader(text.splitlines()))
    cols = list(rows[0].keys()) if rows else []
    expected = ["term", "category", "definition"]
    r.check(all(c in cols for c in expected),
            f"columns include {expected} (got {cols})",
            f"columns must include {expected}, got {cols}")

    terms, domain, dupes, empties = set(), set(), [], 0
    for row in rows:
        t = (row.get("term") or "").strip()
        if not t:
            empties += 1
            continue
        if t in terms:
            dupes.append(t)
        terms.add(t)
        if any(not (row.get(c) or "").strip() for c in ("category", "definition")):
            empties += 1
        if (row.get("category") or "").strip().lower() == "domain":
            domain.add(t)
    r.check(not dupes, f"{len(terms)} unique terms, no duplicates",
            f"duplicate terms: {dupes}")
    r.check(empties == 0, "no empty cells",
            f"{empties} row(s) have empty cells")
    r.check(domain == set(aggregates),
            f"glossary 'Domain' terms == aggregate roots {sorted(aggregates)}",
            f"glossary Domain terms {sorted(domain)} != aggregates {sorted(aggregates)}")


def check_domain_model(r: Report, aggregates):
    r.layer("2. Domain model  (domain/)")
    if not aggregates:
        r.warn("no aggregate files found in domain/ (add one per aggregate root)")
        return
    readme = read(ROOT / "domain" / "README.md") or ""
    ents = mermaid_entities(readme)
    for name in aggregates:
        r.check(name.upper() in ents,
                f"overview ERD includes entity {name}",
                f"domain/README.md ERD missing entity {name}")
        txt = read(ROOT / "domain" / f"{name.lower()}.md") or ""
        r.check(name.upper() in mermaid_entities(txt),
                f"{name.lower()}.md diagrams {name}",
                f"{name.lower()}.md missing a {name} entity block")


def check_api_spec(r: Report, aggregates):
    r.layer("3. API spec  (api/openapi.yaml)")
    text = read(ROOT / "api" / "openapi.yaml")
    if text is None:
        r.fail("openapi.yaml not found")
        return
    api = parse_openapi(text)
    r.check(api["version"] and api["version"].startswith("3.1"),
            f"OpenAPI version is {api['version']}",
            f"expected OpenAPI 3.1, got {api['version']}")

    ids = api["operation_ids"]
    dupes = sorted({i for i in ids if ids.count(i) > 1})
    r.check(not dupes, f"{len(ids)} operationIds, all unique",
            f"duplicate operationIds: {dupes}")

    undef_s = sorted(api["schema_refs"] - set(api["schemas"]))
    r.check(not undef_s, "all schema $refs resolve",
            f"undefined schema $refs: {undef_s}")
    undef_r = sorted(api["response_refs"] - set(api["responses"]))
    r.check(not undef_r, "all response $refs resolve",
            f"undefined response $refs: {undef_r}")

    for name in aggregates:
        r.check(name in api["schemas"],
                f"schema '{name}' defined",
                f"aggregate {name} has no component schema")


def check_ui(r: Report):
    r.layer("4. Wireframes  (wireframe/)")
    ui = ROOT / "wireframe"
    index = read(ui / "index.html")
    r.check(index is not None, "index.html exists", "index.html missing")
    r.check((ui / "wireframe.css").exists(),
            "shared wireframe.css exists",
            "wireframe/wireframe.css missing (screens share it)")

    screens = screen_files()
    r.check(bool(screens), f"{len(screens)} screen file(s) found",
            "no NN-*.html screens found in wireframe/", warn=True)

    # A "remote" asset is a src/href to http(s) or a CSS @import — the shared,
    # relative wireframe.css is allowed and expected.
    for f in screens:
        txt = read(f) or ""
        problems = []
        if 'href="index.html"' not in txt:
            problems.append("no link to index.html")
        if 'wireframe.css' not in txt:
            problems.append("does not link the shared wireframe.css")
        if "<footer" in txt:
            problems.append("uses <footer> for the note")
        if '<aside class="note"' not in txt:
            problems.append("no <aside class=note> annotation")
        if re.search(r'(src|href)\s*=\s*"https?:', txt) or "@import" in txt:
            problems.append("references a remote asset")
        r.check(not problems, f"{f.name} ok", f"{f.name}: {'; '.join(problems)}")

    if index is not None:
        r.check("wireframe.css" in index, "index.html links wireframe.css",
                "index.html does not link the shared wireframe.css")
    if index is not None and screens:
        missing = [f.name for f in screens if f.name not in index]
        r.check(not missing, "index.html links every screen",
                f"index.html missing links: {missing}")


def main():
    r = Report()
    print("Validating design artifacts "
          "(glossary → domain → api + wireframe)")
    aggregates = derive_aggregates()

    check_glossary(r, aggregates)
    check_domain_model(r, aggregates)
    check_api_spec(r, aggregates)
    check_ui(r)

    print("\n" + "─" * 60)
    status = "\033[31mFAIL\033[0m" if r.errors else "\033[32mPASS\033[0m"
    print(f"{status}  {r.checks} checks · {r.errors} error(s) · {r.warnings} warning(s)")
    return 1 if r.errors else 0


if __name__ == "__main__":
    sys.exit(main())
