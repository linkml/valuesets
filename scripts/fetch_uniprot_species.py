#!/usr/bin/env python3
"""
Fetch UniProt species codes and proteome IDs to generate a LinkML enum.
"""
import json
import re
import requests
from typing import Dict, List
import yaml


def clean_enum_name(name: str) -> str:
    """Convert species mnemonic to valid enum name."""
    # Already uppercase mnemonics, just ensure they're valid Python identifiers
    name = re.sub(r'[^A-Z0-9_]', '_', name.upper())
    # Ensure doesn't start with number
    if name and name[0].isdigit():
        name = 'SP_' + name
    return name


def fetch_uniprot_species(limit: int = None) -> List[Dict]:
    """Fetch species codes from UniProt proteomes API."""
    url = "https://rest.uniprot.org/proteomes/stream"
    params = {
        'format': 'tsv',
        'fields': 'upid,organism,organism_id,mnemonic',
        'query': 'proteome_type:1'  # Reference proteomes only
    }

    if limit:
        params['size'] = str(limit)

    response = requests.get(url, params=params)
    response.raise_for_status()

    lines = response.text.strip().split('\n')
    headers = lines[0].split('\t')

    species_data = []
    seen_mnemonics = set()

    for line in lines[1:]:
        if not line.strip():
            continue

        parts = line.split('\t')
        if len(parts) >= 4:
            proteome_id = parts[0]
            organism_name = parts[1]
            tax_id = parts[2]
            mnemonic = parts[3]

            # Skip if no mnemonic or already seen
            if not mnemonic or mnemonic in seen_mnemonics:
                continue

            seen_mnemonics.add(mnemonic)
            species_data.append({
                'mnemonic': mnemonic,
                'organism': organism_name,
                'tax_id': tax_id,
                'proteome_id': proteome_id
            })

    return species_data


def generate_linkml_schema(species_data: List[Dict]) -> Dict:
    """Generate LinkML schema for UniProt species codes."""

    permissible_values = {}

    for species in sorted(species_data, key=lambda x: x['mnemonic']):
        mnemonic = species['mnemonic']
        enum_key = clean_enum_name(mnemonic)

        # Extract common name if present in parentheses
        organism = species['organism']
        common_name = ""
        if '(' in organism and ')' in organism:
            # Extract content in last parentheses as common name
            parts = organism.rsplit('(', 1)
            if len(parts) == 2:
                common_name = parts[1].rstrip(')')
                organism = parts[0].strip()

        description = organism
        if common_name:
            description += f" ({common_name})"
        description += f" - Proteome: {species['proteome_id']}"

        permissible_values[enum_key] = {
            'description': description,
            'meaning': f"NCBITaxon:{species['tax_id']}",
            'title': mnemonic,
            'annotations': {
                'proteome_id': species['proteome_id'],
                'organism_name': organism,
                'tax_id': species['tax_id']
            }
        }

    schema = {
        'id': 'https://w3id.org/common-value-sets/uniprot_species',
        'name': 'uniprot_species',
        'title': 'UniProt Species Codes Value Sets',
        'description': 'Value sets for UniProt species mnemonic codes with associated proteome IDs',
        'imports': ['linkml:types'],
        'prefixes': {
            'CVS': 'https://w3id.org/common-value-sets/',
            'linkml': 'https://w3id.org/linkml/',
            'NCBITaxon': 'http://purl.obolibrary.org/obo/NCBITaxon_',
            'UniProt': 'http://purl.uniprot.org/proteomes/'
        },
        'default_prefix': 'CVS',
        'default_range': 'string',
        'enums': {
            'UniProtSpeciesCode': {
                'description': 'UniProt species mnemonic codes for reference proteomes with associated metadata',
                'permissible_values': permissible_values
            }
        }
    }

    return schema


def main():
    """Main function to fetch and generate schema."""
    print("Fetching UniProt reference proteomes...")

    # Fetch all reference proteomes
    species_data = fetch_uniprot_species()

    print(f"Found {len(species_data)} species with mnemonics")

    # Generate LinkML schema
    schema = generate_linkml_schema(species_data)

    # Save to file
    output_path = 'src/valuesets/schema/bio/uniprot_species.yaml'
    with open(output_path, 'w') as f:
        yaml.dump(schema, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    print(f"Generated schema saved to {output_path}")

    # Print some statistics
    print(f"\nStatistics:")
    print(f"Total species codes: {len(species_data)}")
    print(f"Sample species codes:")
    for species in species_data[:10]:
        print(f"  {species['mnemonic']}: {species['organism']} (Tax ID: {species['tax_id']}, Proteome: {species['proteome_id']})")


if __name__ == "__main__":
    main()