#!/usr/bin/env python3
"""Generate a CSV report of all enums in the valuesets schema."""

import csv
import re
import sys
from collections import Counter
from pathlib import Path

import yaml


def extract_prefix(curie: str) -> str | None:
    """Extract prefix from a CURIE like ENVO:00000001."""
    if not curie:
        return None
    if ":" in curie:
        return curie.split(":")[0]
    return None


def calculate_heterogeneity(prefixes: list[str]) -> float:
    """
    Calculate heterogeneity score based on prefix diversity.
    Score ranges from 0 (all same) to 1 (all different).
    Uses normalized entropy.
    """
    if not prefixes:
        return 0.0
    if len(prefixes) == 1:
        return 0.0

    counts = Counter(prefixes)
    total = len(prefixes)
    unique = len(counts)

    if unique == 1:
        return 0.0

    # Normalized count of unique prefixes relative to total
    # More unique prefixes = higher heterogeneity
    return round(unique / total, 3)


def analyze_enum(enum_name: str, enum_def: dict) -> dict:
    """Analyze a single enum definition."""
    pvs = enum_def.get("permissible_values", {})
    if not pvs:
        return None

    # Convert all keys to strings (handles YAML booleans like True/False)
    pv_names = [str(k) for k in pvs.keys()]
    num_pvs = len(pv_names)

    # Collect meanings and other mappings
    meanings = []
    pvs_with_meaning = []
    pvs_without_meaning = []
    all_prefixes = []

    for pv_key, pv_def in pvs.items():
        pv_name = str(pv_key)
        if pv_def is None:
            pv_def = {}

        has_mapping = False

        # Check meaning field
        meaning = pv_def.get("meaning")
        if meaning:
            has_mapping = True
            prefix = extract_prefix(meaning)
            if prefix:
                meanings.append(meaning)
                all_prefixes.append(prefix)

        # Check exact_mappings
        for m in pv_def.get("exact_mappings", []) or []:
            prefix = extract_prefix(m)
            if prefix:
                has_mapping = True
                all_prefixes.append(prefix)

        # Check related_mappings
        for m in pv_def.get("related_mappings", []) or []:
            prefix = extract_prefix(m)
            if prefix:
                has_mapping = True
                all_prefixes.append(prefix)

        # Check close_mappings
        for m in pv_def.get("close_mappings", []) or []:
            prefix = extract_prefix(m)
            if prefix:
                has_mapping = True
                all_prefixes.append(prefix)

        if has_mapping:
            pvs_with_meaning.append(pv_name)
        else:
            pvs_without_meaning.append(pv_name)

    # Calculate stats
    pct_with_meaning = round(100 * len(pvs_with_meaning) / num_pvs, 1) if num_pvs > 0 else 0

    unique_prefixes = sorted(set(all_prefixes))
    heterogeneity = calculate_heterogeneity(all_prefixes)

    # Get status and other metadata
    status = enum_def.get("status", "")
    title = enum_def.get("title", "")
    description = enum_def.get("description", "")
    has_description = bool(description and len(description) > 10)

    return {
        "enum": enum_name,
        "title": title,
        "num_pvs": num_pvs,
        "num_with_mapping": len(pvs_with_meaning),
        "pct_with_meaning": pct_with_meaning,
        "heterogeneity": heterogeneity,
        "num_vocabs": len(unique_prefixes),
        "vocabs": "|".join(unique_prefixes),
        "all_pvs": "|".join(pv_names),
        "pvs_without_mapping": "|".join(pvs_without_meaning),
        "status": status,
        "has_description": has_description,
    }


def process_schema_file(filepath: Path, base_path: Path) -> list[dict]:
    """Process a single schema file and return enum analyses."""
    results = []

    rel_path = filepath.relative_to(base_path)
    parts = list(rel_path.parts)

    # Extract category (folder path) and module (filename without .yaml)
    module = filepath.stem
    if len(parts) > 1:
        category = "/".join(parts[:-1])
    else:
        category = ""

    with open(filepath) as f:
        try:
            schema = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(f"Error parsing {filepath}: {e}", file=sys.stderr)
            return results

    if not schema:
        return results

    enums = schema.get("enums", {})
    for enum_name, enum_def in enums.items():
        if not enum_def:
            continue

        analysis = analyze_enum(enum_name, enum_def)
        if analysis:
            analysis["category"] = category
            analysis["module"] = module
            results.append(analysis)

    return results


def main():
    base_path = Path("src/valuesets/schema")
    output_path = Path("enum_report.csv")

    if not base_path.exists():
        print(f"Schema path not found: {base_path}", file=sys.stderr)
        sys.exit(1)

    all_results = []

    # Find all YAML files
    yaml_files = sorted(base_path.rglob("*.yaml"))

    for filepath in yaml_files:
        results = process_schema_file(filepath, base_path)
        all_results.extend(results)

    # Sort by category, module, enum
    all_results.sort(key=lambda x: (x["category"], x["module"], x["enum"]))

    # Write CSV
    fieldnames = [
        "category",
        "module",
        "enum",
        "title",
        "num_pvs",
        "num_with_mapping",
        "pct_with_meaning",
        "heterogeneity",
        "num_vocabs",
        "vocabs",
        "status",
        "has_description",
        "all_pvs",
        "pvs_without_mapping",
    ]

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_results)

    # Print summary
    total_enums = len(all_results)
    total_pvs = sum(r["num_pvs"] for r in all_results)
    total_mapped = sum(r["num_with_mapping"] for r in all_results)
    avg_pct = round(100 * total_mapped / total_pvs, 1) if total_pvs > 0 else 0

    all_vocabs = set()
    for r in all_results:
        if r["vocabs"]:
            all_vocabs.update(r["vocabs"].split("|"))

    print(f"Generated: {output_path}")
    print(f"Total enums: {total_enums}")
    print(f"Total permissible values: {total_pvs}")
    print(f"Total with mappings: {total_mapped} ({avg_pct}%)")
    print(f"Unique vocabularies used: {len(all_vocabs)}")
    print(f"Vocabularies: {', '.join(sorted(all_vocabs))}")


if __name__ == "__main__":
    main()
