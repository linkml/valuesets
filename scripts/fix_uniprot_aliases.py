#!/usr/bin/env python3
"""Add aliases to UniProt species codes to fix validation."""

import yaml
from pathlib import Path

def add_aliases_to_uniprot():
    file_path = Path("/Users/cjm/repos/common-value-sets/src/valuesets/schema/bio/uniprot_species.yaml")

    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)

    # Process each permissible value in the UniProtSpeciesCode enum
    if 'enums' in data and 'UniProtSpeciesCode' in data['enums']:
        enum_def = data['enums']['UniProtSpeciesCode']
        if 'permissible_values' in enum_def:
            for key, value in enum_def['permissible_values'].items():
                # Extract the code without SP_ prefix
                if key.startswith('SP_'):
                    code = key[3:]  # Remove 'SP_' prefix
                else:
                    code = key

                # Add aliases for both the code and SP_ prefixed version
                value['aliases'] = [code, f'SP_{code}']

    # Write back with proper formatting
    with open(file_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"Added aliases to {len(enum_def['permissible_values'])} UniProt species codes")

if __name__ == "__main__":
    add_aliases_to_uniprot()