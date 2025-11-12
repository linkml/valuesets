#!/usr/bin/env python3
"""
Merge UniProt species data from multiple sources into a best union.

This script combines:
1. GO goex.yaml organisms (authoritative for GO annotations)
2. Existing uniprot_species.yaml (manual curation)
3. UniProt common organisms (curated list)
4. Optional: Extended UniProt reference proteomes

The merge strategy:
- Prefer GO organisms (they're actively used in annotations)
- Preserve any manually curated entries
- Add common model organisms
- Optionally add extended set
- De-duplicate by UniProt mnemonic code

Usage:
    python scripts/merge_uniprot_sources.py [OPTIONS]
"""

import yaml
import json
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Set
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


def load_json_organisms(path: Path) -> List[Dict]:
    """Load organisms from JSON file."""
    if not path.exists():
        logger.warning(f"File not found: {path}")
        return []

    with open(path) as f:
        data = json.load(f)
    logger.info(f"Loaded {len(data)} organisms from {path}")
    return data


def load_existing_yaml(path: Path) -> Dict:
    """Load existing uniprot_species.yaml file."""
    if not path.exists():
        logger.warning(f"File not found: {path}")
        return {}

    with open(path) as f:
        data = yaml.safe_load(f)
    logger.info(f"Loaded existing YAML from {path}")
    return data


def extract_organisms_from_yaml(yaml_data: Dict) -> List[Dict]:
    """Extract organism data from existing YAML structure."""
    organisms = []

    pvs = yaml_data.get('enums', {}).get('UniProtSpeciesCode', {}).get('permissible_values', {})

    for key, value in pvs.items():
        # Key format is SP_CODE
        code = key.replace('SP_', '')

        # Extract tax_id from meaning
        meaning = value.get('meaning', '')
        tax_id = meaning.replace('NCBITaxon:', '') if meaning.startswith('NCBITaxon:') else ''

        # Extract proteome_id from exact_mappings
        proteome_id = None
        for mapping in value.get('exact_mappings', []):
            if mapping.startswith('uniprot.proteome:'):
                proteome_id = mapping.replace('uniprot.proteome:', '')
                break

        name = value.get('title', '')
        common_name = value.get('aliases', [None])[0] if value.get('aliases') else None

        organisms.append({
            'code': code,
            'tax_id': tax_id,
            'name': name,
            'common_name': common_name,
            'proteome_id': proteome_id,
            'source': 'existing'
        })

    logger.info(f"Extracted {len(organisms)} organisms from existing YAML")
    return organisms


def merge_organisms(*organism_lists: List[Dict]) -> List[Dict]:
    """
    Merge multiple organism lists into a single de-duplicated list.

    Merge strategy:
    - De-duplicate by UniProt mnemonic code
    - Prefer entries with more complete data
    - Prefer later sources (they're more recent/authoritative)
    - Preserve all unique codes
    """
    merged: Dict[str, Dict] = {}

    # Process each source in order
    for organisms in organism_lists:
        for org in organisms:
            code = org.get('code', '')
            if not code:
                continue

            if code not in merged:
                # New entry
                merged[code] = org.copy()
            else:
                # Merge with existing entry
                existing = merged[code]

                # Update fields if new data is more complete
                for field in ['tax_id', 'name', 'common_name', 'proteome_id']:
                    new_value = org.get(field)
                    existing_value = existing.get(field)

                    # Prefer non-empty values
                    if new_value and not existing_value:
                        existing[field] = new_value
                    # Prefer longer names (more descriptive)
                    elif field in ['name', 'common_name'] and new_value and existing_value:
                        if len(str(new_value)) > len(str(existing_value)):
                            existing[field] = new_value

                # Track sources
                existing_sources = existing.get('sources', [])
                new_source = org.get('source', 'unknown')
                if new_source not in existing_sources:
                    existing_sources.append(new_source)
                existing['sources'] = existing_sources

    result = list(merged.values())
    logger.info(f"Merged into {len(result)} unique organisms")
    return result


def generate_yaml_content(organisms: List[Dict]) -> Dict:
    """Generate the YAML content for the UniProt species file."""
    yaml_content = {
        'name': 'uniprot_species',
        'title': 'UniProt Species Codes Value Sets',
        'description': 'Value sets for UniProt species mnemonic codes with associated proteome IDs',
        'id': 'https://w3id.org/common-value-sets/uniprot_species',
        'imports': ['linkml:types'],
        'prefixes': {
            'CVS': 'https://w3id.org/common-value-sets/',
            'linkml': 'https://w3id.org/linkml/',
            'NCBITaxon': 'http://purl.obolibrary.org/obo/NCBITaxon_',
            'uniprot.proteome': 'http://purl.uniprot.org/proteomes/',
            'valuesets': 'https://w3id.org/valuesets/'
        },
        'default_prefix': 'valuesets',
        'slots': {
            'uni_prot_species': {
                'description': 'UniProt species mnemonic codes for reference proteomes with associated metadata',
                'range': 'UniProtSpeciesCode'
            }
        },
        'enums': {
            'UniProtSpeciesCode': {
                'description': 'UniProt species mnemonic codes for reference proteomes with associated metadata',
                'permissible_values': {}
            }
        }
    }

    # Add permissible values for each species
    for species in sorted(organisms, key=lambda x: x.get('code', '')):
        code = species.get('code', '')
        if not code:
            continue

        name = species.get('name', '')
        common_name = species.get('common_name')
        tax_id = species.get('tax_id', '')
        proteome_id = species.get('proteome_id')

        # Create the value key (adding SP_ prefix for consistency)
        value_key = f"SP_{code}"

        # Build description
        if common_name:
            description = f"{name} ({common_name})"
        else:
            description = name

        if proteome_id:
            description += f" - Proteome: {proteome_id}"

        # Build the permissible value entry
        pv_entry = {
            'description': description,
            'meaning': f"NCBITaxon:{tax_id}",
            'title': name,
            'exact_mappings': [f"NCBITaxon:{tax_id}"]
        }

        if proteome_id:
            pv_entry['exact_mappings'].append(f"uniprot.proteome:{proteome_id}")

        if common_name:
            pv_entry['aliases'] = [common_name]

        # Add source annotations for tracking
        sources = species.get('sources', [species.get('source', 'unknown')])
        if isinstance(sources, str):
            sources = [sources]
        pv_entry['annotations'] = {'sources': ', '.join(sources)}

        yaml_content['enums']['UniProtSpeciesCode']['permissible_values'][value_key] = pv_entry

    return yaml_content


def main():
    """Main function to merge UniProt species data."""
    parser = argparse.ArgumentParser(
        description='Merge UniProt species data from multiple sources'
    )
    parser.add_argument(
        '--go-organisms',
        type=str,
        default='cache/go_organisms.json',
        help='Path to GO organisms JSON (from fetch_from_go_goex.py)'
    )
    parser.add_argument(
        '--common-organisms',
        type=str,
        default='cache/common_organisms.json',
        help='Path to common organisms JSON (from sync_uniprot_species.py)'
    )
    parser.add_argument(
        '--extended-organisms',
        type=str,
        help='Path to extended organisms JSON (optional)'
    )
    parser.add_argument(
        '--existing',
        type=str,
        default='src/valuesets/schema/bio/uniprot_species.yaml',
        help='Path to existing YAML file'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='src/valuesets/schema/bio/uniprot_species.yaml',
        help='Output file path'
    )
    parser.add_argument(
        '--backup',
        action='store_true',
        default=True,
        help='Backup existing file before overwriting'
    )

    args = parser.parse_args()

    logger.info("=== Merging UniProt Species Data ===\n")

    # Load all sources
    sources = []

    # 1. Load existing YAML (lowest priority - base)
    existing_path = Path(args.existing)
    if existing_path.exists():
        existing_data = load_existing_yaml(existing_path)
        existing_organisms = extract_organisms_from_yaml(existing_data)
        sources.append(existing_organisms)

    # 2. Load common organisms
    common_path = Path(args.common_organisms)
    if common_path.exists():
        common_organisms = load_json_organisms(common_path)
        for org in common_organisms:
            org['source'] = 'common'
        sources.append(common_organisms)

    # 3. Load GO organisms (high priority)
    go_path = Path(args.go_organisms)
    if go_path.exists():
        go_organisms = load_json_organisms(go_path)
        for org in go_organisms:
            org['source'] = 'GO'
        sources.append(go_organisms)

    # 4. Load extended organisms (if provided)
    if args.extended_organisms:
        extended_path = Path(args.extended_organisms)
        if extended_path.exists():
            extended_organisms = load_json_organisms(extended_path)
            for org in extended_organisms:
                org['source'] = 'extended'
            sources.append(extended_organisms)

    if not sources:
        logger.error("No source data found. Run fetch scripts first.")
        return 1

    # Merge all sources
    logger.info("\n=== Merging Sources ===")
    merged_organisms = merge_organisms(*sources)

    # Generate YAML content
    logger.info("\n=== Generating YAML ===")
    yaml_content = generate_yaml_content(merged_organisms)

    # Write to file
    output_path = Path(args.output)

    # Backup existing file
    if args.backup and output_path.exists():
        backup_path = output_path.with_suffix('.yaml.bak')
        output_path.rename(backup_path)
        logger.info(f"Backed up existing file to {backup_path}")

    # Create directory if needed
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Write new file
    with open(output_path, 'w') as f:
        yaml.dump(yaml_content, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    logger.info(f"\n✓ Generated {output_path} with {len(merged_organisms)} species")

    # Statistics
    logger.info(f"\n=== Statistics ===")
    logger.info(f"Total unique species codes: {len(merged_organisms)}")

    with_proteomes = sum(1 for org in merged_organisms if org.get('proteome_id'))
    logger.info(f"With proteome IDs: {with_proteomes}")
    logger.info(f"Missing proteomes: {len(merged_organisms) - with_proteomes}")

    # Source breakdown
    source_counts: Dict[str, int] = {}
    for org in merged_organisms:
        sources_list = org.get('sources', [org.get('source', 'unknown')])
        if isinstance(sources_list, str):
            sources_list = [sources_list]
        for source in sources_list:
            source_counts[source] = source_counts.get(source, 0) + 1

    logger.info(f"\nSource breakdown:")
    for source, count in sorted(source_counts.items()):
        logger.info(f"  {source}: {count}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
