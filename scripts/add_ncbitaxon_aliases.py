#!/usr/bin/env python3
"""Add NCBITaxon label aliases for mismatched UniProt entries."""

import yaml
import subprocess
from pathlib import Path

def get_mismatches():
    """Get all validation mismatches with their expected NCBITaxon labels."""
    result = subprocess.run(
        ["uv", "run", "python", "-m", "src.valuesets.validators.enum_evaluator",
         "src/valuesets/schema", "--no-cache"],
        stdout=subprocess.PIPE, text=True, stderr=subprocess.DEVNULL
    )

    mismatches = {}
    for line in result.stdout.splitlines():
        if "uniprot_species.yaml" in line and "Ontology label mismatch" in line:
            # Parse the line to extract the key and the NCBITaxon label
            if "UniProtSpeciesCode." in line:
                # Extract the key (e.g., SP_9GAMM or AADNV)
                key_start = line.find("UniProtSpeciesCode.") + len("UniProtSpeciesCode.")
                key_end = line.find(" [", key_start)
                key = line[key_start:key_end]

                # Extract the NCBITaxon label (what it got from the ontology)
                got_start = line.find("got '") + len("got '")
                got_end = line.find("'", got_start)
                ncbi_label = line[got_start:got_end]

                mismatches[key] = ncbi_label

    return mismatches

def add_aliases():
    file_path = Path("/Users/cjm/repos/common-value-sets/src/valuesets/schema/bio/uniprot_species.yaml")

    # Get all mismatches
    print("Getting mismatches from validator...")
    mismatches = get_mismatches()
    print(f"Found {len(mismatches)} entries with label mismatches")

    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)

    # Process each permissible value in the UniProtSpeciesCode enum
    updated = 0
    if 'enums' in data and 'UniProtSpeciesCode' in data['enums']:
        enum_def = data['enums']['UniProtSpeciesCode']
        if 'permissible_values' in enum_def:
            for key, value in enum_def['permissible_values'].items():
                if key in mismatches:
                    ncbi_label = mismatches[key]
                    # Only add alias if it's different from the current title
                    if 'title' in value:
                        # Add the NCBITaxon label as an alias
                        # Note: Even if title == ncbi_label, the yaml dump might have created an empty aliases field
                        value['aliases'] = [ncbi_label]
                        updated += 1
                        print(f"Added alias for {key}: {ncbi_label}")

    # Write back with proper formatting
    with open(file_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"\nAdded aliases to {updated} entries")

if __name__ == "__main__":
    add_aliases()