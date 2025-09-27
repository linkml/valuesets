#!/usr/bin/env python3
"""Fix UniProt species codes by moving organism_name to title and code to annotations."""

import yaml
from pathlib import Path

def fix_uniprot_titles():
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

                # Get the organism name from annotations
                if 'annotations' in value and 'organism_name' in value['annotations']:
                    organism_name = value['annotations']['organism_name']

                    # Set title to organism name
                    value['title'] = organism_name

                    # Add code to annotations and remove organism_name
                    value['annotations']['code'] = code
                    del value['annotations']['organism_name']

                    # Remove the aliases field if it exists
                    if 'aliases' in value:
                        del value['aliases']

    # Write back with proper formatting
    with open(file_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"Fixed titles for {len(enum_def['permissible_values'])} UniProt species codes")

if __name__ == "__main__":
    fix_uniprot_titles()