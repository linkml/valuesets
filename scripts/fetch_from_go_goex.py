#!/usr/bin/env python3
"""
Fetch UniProt species from GO goex.yaml metadata file.
This ensures we have all organisms used in Gene Ontology annotations.

Usage:
    python scripts/fetch_from_go_goex.py [--output FILE]
"""

import yaml
import requests
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Optional
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

GOEX_URL = "https://raw.githubusercontent.com/geneontology/go-site/master/metadata/goex.yaml"


def fetch_goex_yaml() -> List:
    """Fetch the goex.yaml file from GO site repository."""
    logger.info(f"Fetching goex.yaml from {GOEX_URL}...")
    response = requests.get(GOEX_URL, timeout=30)
    response.raise_for_status()
    data = yaml.safe_load(response.text)

    # goex.yaml has structure: {organisms: [...]}
    if isinstance(data, dict) and 'organisms' in data:
        return data['organisms']
    elif isinstance(data, list):
        return data
    else:
        logger.error(f"Unexpected goex.yaml structure: {type(data)}")
        return []


def fetch_proteome_id(tax_id: str) -> Optional[str]:
    """Fetch the reference proteome ID for a given taxonomy ID from UniProt."""
    base_url = "https://rest.uniprot.org/proteomes/search"

    try:
        params = {
            'query': f'taxonomy_id:{tax_id} AND proteome_type:1',
            'format': 'json',
            'size': 1
        }

        response = requests.get(base_url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('results'):
                return data['results'][0].get('id', '')
    except Exception as e:
        logger.warning(f"Failed to fetch proteome for tax_id {tax_id}: {e}")

    return None


def extract_organisms_from_goex(goex_data: Dict) -> List[Dict]:
    """Extract organism information from goex.yaml structure."""
    organisms = []

    # The goex.yaml structure has organisms under various keys
    # Look for 'genomes' or similar structures
    for key, value in goex_data.items():
        if isinstance(value, dict):
            # Check if this is an organism entry
            if 'taxon_id' in value or 'code_uniprot' in value:
                organisms.append(value)
            # Recursively check nested structures
            elif any(isinstance(v, dict) and ('taxon_id' in v or 'code_uniprot' in v)
                    for v in value.values() if isinstance(v, dict)):
                for sub_key, sub_value in value.items():
                    if isinstance(sub_value, dict) and ('taxon_id' in sub_value or 'code_uniprot' in sub_value):
                        organisms.append(sub_value)

    return organisms


def parse_goex_organisms(goex_data: List) -> List[Dict]:
    """
    Parse organisms from goex.yaml and enrich with UniProt proteome IDs.

    Returns list of dicts with:
        - code: UniProt mnemonic code
        - tax_id: NCBI Taxonomy ID
        - name: Scientific name
        - common_name: Common name (if available)
        - proteome_id: UniProt proteome ID (from goex or fetched)
    """
    organisms_list = []

    # goex.yaml is a list of organism entries like:
    # - taxon_id: NCBITaxon:9606
    #   full_name: Homo sapiens
    #   common_name_uniprot: Human
    #   code_uniprot: HUMAN
    #   uniprot_proteome_id: uniprot.proteome:UP000005640
    #   ...

    if not isinstance(goex_data, list):
        logger.error("Expected goex.yaml to be a list of organisms")
        return []

    for entry in goex_data:
        if not isinstance(entry, dict):
            continue

        # Extract fields
        taxon_id = entry.get('taxon_id', '')
        if not taxon_id:
            continue

        # Handle both NCBITaxon:9606 and 9606 formats
        tax_id = str(taxon_id)
        if tax_id.startswith('NCBITaxon:'):
            tax_id = tax_id.replace('NCBITaxon:', '')
        elif not tax_id.isdigit():
            continue

        code = entry.get('code_uniprot', '')
        if not code:
            continue

        name = entry.get('full_name', '')
        common_name = entry.get('common_name_uniprot', '') or entry.get('common_name_panther', '')

        # Extract proteome ID if present in goex
        proteome_id = entry.get('uniprot_proteome_id', '')
        if proteome_id.startswith('uniprot.proteome:'):
            proteome_id = proteome_id.replace('uniprot.proteome:', '')
        else:
            proteome_id = None

        organisms_list.append({
            'code': code,
            'tax_id': tax_id,
            'name': name,
            'common_name': common_name,
            'proteome_id': proteome_id
        })

    logger.info(f"Found {len(organisms_list)} organisms in goex.yaml")

    # Fetch missing proteome IDs
    missing_proteome = [org for org in organisms_list if not org.get('proteome_id')]
    if missing_proteome:
        logger.info(f"Fetching {len(missing_proteome)} missing proteome IDs...")
        for idx, org in enumerate(missing_proteome, 1):
            logger.info(f"[{idx}/{len(missing_proteome)}] Fetching proteome for {org['code']} ({org['name']})...")
            proteome_id = fetch_proteome_id(org['tax_id'])
            org['proteome_id'] = proteome_id

            if proteome_id:
                logger.info(f"  ✓ Found proteome {proteome_id}")
            else:
                logger.warning(f"  ✗ No proteome found")

    return organisms_list


def save_organisms_json(organisms: List[Dict], output_path: Path):
    """Save organisms data as JSON for later merging."""
    import json

    with open(output_path, 'w') as f:
        json.dump(organisms, f, indent=2)

    logger.info(f"Saved {len(organisms)} organisms to {output_path}")


def main():
    """Main function to fetch GO organisms."""
    parser = argparse.ArgumentParser(
        description='Fetch UniProt species from GO goex.yaml metadata'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='cache/go_organisms.json',
        help='Output JSON file path (default: cache/go_organisms.json)'
    )

    args = parser.parse_args()

    logger.info("=== Fetching GO Organisms from goex.yaml ===")

    # Fetch goex.yaml
    goex_data = fetch_goex_yaml()

    # Parse organisms
    organisms = parse_goex_organisms(goex_data)

    if not organisms:
        logger.error("No organisms found in goex.yaml")
        return 1

    # Save to JSON
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    save_organisms_json(organisms, output_path)

    # Report statistics
    logger.info(f"\n=== Summary ===")
    logger.info(f"Total organisms: {len(organisms)}")
    with_proteomes = sum(1 for org in organisms if org.get('proteome_id'))
    logger.info(f"With proteome IDs: {with_proteomes}")
    logger.info(f"Missing proteomes: {len(organisms) - with_proteomes}")

    # Show some examples
    logger.info(f"\nSample organisms:")
    for org in organisms[:5]:
        proteome = org.get('proteome_id', 'N/A')
        logger.info(f"  {org['code']}: {org['name']} (Tax: {org['tax_id']}, Proteome: {proteome})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
