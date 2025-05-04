# scripts/validate_loot_entries.py
import sys
import subprocess
import json
import argparse
from jsonschema import validate, ValidationError

entry_schema = {
    "type": "object",
    "properties": {
        "type": {"const": "minecraft:item"},
        "name": {"type": "string"},
        "weight": {"type": "integer", "minimum": 1},
        "functions": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "properties": {
                    "function": {"const": "minecraft:set_components"},
                    "components": {"type": "object"}
                },
                "required": ["function", "components"]
            }
        },
        "conditions": {
            "type": "array",
            "minItems": 1,
            "items": {"type": "object"}
        }
    },
    "required": ["type", "name", "weight", "functions", "conditions"]
}

def load_version(commit, path):
    content = subprocess.check_output(
        ["git", "show", f"{commit}:{path}"],
        universal_newlines=True
    )
    return json.loads(content)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", required=True)
    args = parser.parse_args()

    base = load_version(args.base, args.file)
    head = json.load(open(args.file))
    be = base["pools"][0]["entries"]
    he = head["pools"][0]["entries"]
    added = he[len(be):]

    count = len(added)
    if count != 6:
        print(f"::notice::found {count} new entries (expected 6); continuing with validation")

    for idx, entry in enumerate(added, start=1):
        try:
            validate(instance=entry, schema=entry_schema)
        except ValidationError as e:
            print(f"::error::Entry #{idx} schema error: {e.message}")
            sys.exit(1)
        funcs = entry["functions"][0]
        comps = funcs["components"]
        if ("minecraft:custom_name" not in comps
            or "minecraft:custom_data" not in comps
            or "minecraft:lore" not in comps):
            print(f"::error::Entry #{idx} missing required components")
            sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    main()
