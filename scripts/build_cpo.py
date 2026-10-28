#!/usr/bin/env python3
"""Build cpo/cpo.json from cpo/cpo.md and validate it against the FedRAMP CPO schema."""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml
from jsonschema import FormatChecker
from jsonschema.validators import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = ROOT / "schema"
CPO_SCHEMA = "fedramp-certification-package-overview-schema-2026-06-24.json"


def split_frontmatter(text: str) -> tuple[dict, str]:
    m = re.match(r"---\n(.*?)\n---[ \t]*(?:\n|$)(.*)", text, re.DOTALL)
    if not m:
        sys.exit("error: cpo markdown must start with a '---' YAML frontmatter block")
    return yaml.safe_load(m.group(1)) or {}, m.group(2).strip()


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.strip()


def prune_empty(o):
    """Drop empty strings/None so optional fields left blank in YAML are omitted."""
    if isinstance(o, dict):
        return {k: v for k, v in ((k, prune_empty(v)) for k, v in o.items()) if v not in ("", None)}
    if isinstance(o, list):
        return [prune_empty(i) for i in o]
    return o


def build(src: Path) -> dict:
    data, body = split_frontmatter(src.read_text())
    meta = data.pop("metadata", {}) or {}
    if body:
        data.setdefault("serviceIdentification", {})["serviceDescription"] = body

    rel = str(src.relative_to(ROOT)) if src.is_relative_to(ROOT) else src.name
    try:
        updated = git("log", "-1", "--format=%cI", "--", rel)
        sha = git("log", "-1", "--format=%H", "--", rel)
    except subprocess.CalledProcessError:
        updated, sha = "", ""
    # CPO-CSO-MTD: version, date/time of last update, source of update, responsible official
    schema_id = json.loads((SCHEMA_DIR / CPO_SCHEMA).read_text())["$id"]
    data["$schema"] = schema_id  # records which schema version this document was validated against
    data["metadata"] = {
        "version": meta.get("version"),
        "lastUpdated": updated,
        "updateSource": {"file": rel, "commit": sha},
        "responsibleOfficial": meta.get("responsibleOfficial"),
    }
    return prune_empty(json.loads(json.dumps(data, default=str)))


def validate(doc: dict) -> list[str]:
    resources = []
    for p in SCHEMA_DIR.glob("*.json"):
        s = json.loads(p.read_text())
        resources.append((s["$id"], Resource.from_contents(s)))
    registry = Registry().with_resources(resources)
    schema = json.loads((SCHEMA_DIR / CPO_SCHEMA).read_text())
    v = Draft202012Validator(schema, registry=registry, format_checker=FormatChecker())
    errs = [f"{'/'.join(map(str, e.absolute_path)) or '<root>'}: {e.message}" for e in v.iter_errors(doc)]
    # CPO-CSO-MTD fields the schema does not itself require
    m = doc.get("metadata", {})
    for k in ("version", "responsibleOfficial"):
        if not m.get(k):
            errs.append(f"metadata/{k}: required by CPO-CSO-MTD")
    return errs


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=ROOT / "cpo/cpo.md", type=Path, help="markdown source (default: cpo/cpo.md)")
    ap.add_argument("--out", default=ROOT / "cpo/cpo.json", type=Path)
    ap.add_argument("--check", action="store_true", help="validate only; do not write output")
    args = ap.parse_args()
    args.src, args.out = args.src.resolve(), args.out.resolve()

    doc = build(args.src)
    errs = validate(doc)
    if errs:
        print("CPO validation failed:", *errs, sep="\n  - ", file=sys.stderr)
        sys.exit(1)
    if args.check:
        print(f"{args.src.name} is valid")
        return
    args.out.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {args.out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
