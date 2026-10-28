#!/usr/bin/env python3
"""Fail if the vendored FedRAMP schemas drift from what fedramp.gov publishes,
or if FedRAMP's official rules JSON references a newer CPO schema version."""
import json
import re
import sys
import urllib.request
from pathlib import Path

SCHEMA_DIR = Path(__file__).resolve().parent.parent / "schema"
RULES_JSON = "https://raw.githubusercontent.com/FedRAMP/rules/main/fedramp-consolidated-rules.json"
CPO_URL = re.compile(r"https://fedramp\.gov/schemas/fedramp-certification-package-overview-schema-[\d-]+\.json")


def fetch(url: str) -> str:
    with urllib.request.urlopen(url, timeout=30) as r:  # noqa: S310 - fixed https URLs
        return r.read().decode()


def canon(o) -> str:
    return json.dumps(o, sort_keys=True)


def main() -> None:
    problems = []

    pinned = set()
    for p in sorted(SCHEMA_DIR.glob("*.json")):
        local = json.loads(p.read_text())
        if not local["$id"].endswith("/" + p.name):
            problems.append(f"{p.name}: filename does not match $id {local['$id']}")
        live = json.loads(fetch(local["$id"]))
        if canon(live) != canon(local):
            problems.append(f"{p.name}: differs from the version published at {local['$id']}")
        if "certification-package-overview" in p.name:
            pinned.add(local["$id"])

    referenced = set(CPO_URL.findall(fetch(RULES_JSON)))
    if referenced != pinned:
        problems.append(
            f"official rules reference CPO schema(s) {sorted(referenced)}, vendored {sorted(pinned)}"
        )

    if problems:
        print("Schema check failed:", *problems, sep="\n  - ", file=sys.stderr)
        sys.exit(1)
    print(f"schemas match fedramp.gov; CPO schema in use: {sorted(pinned)[0]}")


if __name__ == "__main__":
    main()
