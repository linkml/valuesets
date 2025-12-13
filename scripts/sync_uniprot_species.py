#!/usr/bin/env python3
"""
Script to sync UniProt species data with reference proteomes.
Fetches the complete list from UniProt and generates/updates the YAML file.

Usage:
    python scripts/sync_uniprot_species.py [--extended]

Options:
    --extended: Fetch extended list including more species (default: common model organisms only)
"""

import yaml
import json
import requests
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Optional
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# Common model organisms - these are the most frequently used in research
COMMON_ORGANISMS = {
    'HUMAN': {'tax_id': '9606', 'name': 'Homo sapiens', 'common_name': 'Human'},
    'MOUSE': {'tax_id': '10090', 'name': 'Mus musculus', 'common_name': 'Mouse'},
    'RAT': {'tax_id': '10116', 'name': 'Rattus norvegicus', 'common_name': 'Rat'},
    'BOVIN': {'tax_id': '9913', 'name': 'Bos taurus', 'common_name': 'Cattle'},
    'CHICK': {'tax_id': '9031', 'name': 'Gallus gallus', 'common_name': 'Chicken'},
    'DANRE': {'tax_id': '7955', 'name': 'Danio rerio', 'common_name': 'Zebrafish'},
    'DROME': {'tax_id': '7227', 'name': 'Drosophila melanogaster', 'common_name': 'Fruit fly'},
    'CAEEL': {'tax_id': '6239', 'name': 'Caenorhabditis elegans', 'common_name': None},
    'YEAST': {'tax_id': '559292', 'name': 'Saccharomyces cerevisiae S288C', 'common_name': "Baker's yeast"},
    'SCHPO': {'tax_id': '284812', 'name': 'Schizosaccharomyces pombe 972h-', 'common_name': 'Fission yeast'},
    'ECOLI': {'tax_id': '83333', 'name': 'Escherichia coli K-12', 'common_name': None},
    'BACSU': {'tax_id': '224308', 'name': 'Bacillus subtilis subsp. subtilis str. 168', 'common_name': None},
    'ARATH': {'tax_id': '3702', 'name': 'Arabidopsis thaliana', 'common_name': 'Thale cress'},
    'MAIZE': {'tax_id': '4577', 'name': 'Zea mays', 'common_name': 'Maize'},
    'ORYSJ': {'tax_id': '39947', 'name': 'Oryza sativa subsp. japonica', 'common_name': 'Rice'},
    'XENLA': {'tax_id': '8355', 'name': 'Xenopus laevis', 'common_name': 'African clawed frog'},
    'XENTR': {'tax_id': '8364', 'name': 'Xenopus tropicalis', 'common_name': 'Western clawed frog'},
    'PIG': {'tax_id': '9823', 'name': 'Sus scrofa', 'common_name': 'Pig'},
    'SHEEP': {'tax_id': '9940', 'name': 'Ovis aries', 'common_name': 'Sheep'},
    'HORSE': {'tax_id': '9796', 'name': 'Equus caballus', 'common_name': 'Horse'},
    'RABIT': {'tax_id': '9986', 'name': 'Oryctolagus cuniculus', 'common_name': 'Rabbit'},
    'CANLF': {'tax_id': '9615', 'name': 'Canis lupus familiaris', 'common_name': 'Dog'},
    'FELCA': {'tax_id': '9685', 'name': 'Felis catus', 'common_name': 'Cat'},
    'MACMU': {'tax_id': '9544', 'name': 'Macaca mulatta', 'common_name': 'Rhesus macaque'},
    'PANTR': {'tax_id': '9598', 'name': 'Pan troglodytes', 'common_name': 'Chimpanzee'},
    'GORGO': {'tax_id': '9593', 'name': 'Gorilla gorilla gorilla', 'common_name': 'Western lowland gorilla'},
    'PEA': {'tax_id': '3888', 'name': 'Pisum sativum', 'common_name': 'Garden pea'},
    'TOBAC': {'tax_id': '4097', 'name': 'Nicotiana tabacum', 'common_name': 'Common tobacco'},
}

# Extended list for comprehensive coverage (add more as needed)
EXTENDED_ORGANISMS = {
    'MYCTU': {'tax_id': '83332', 'name': 'Mycobacterium tuberculosis H37Rv', 'common_name': None},
    'STRPN': {'tax_id': '171101', 'name': 'Streptococcus pneumoniae R6', 'common_name': None},
    'STAAU': {'tax_id': '93061', 'name': 'Staphylococcus aureus subsp. aureus NCTC 8325', 'common_name': None},
    'PSEAE': {'tax_id': '208964', 'name': 'Pseudomonas aeruginosa PAO1', 'common_name': None},
    'HELPY': {'tax_id': '85962', 'name': 'Helicobacter pylori 26695', 'common_name': None},
    'NEIME': {'tax_id': '122586', 'name': 'Neisseria meningitidis MC58', 'common_name': None},
    'DICDI': {'tax_id': '44689', 'name': 'Dictyostelium discoideum', 'common_name': 'Slime mold'},
    'PLAF7': {'tax_id': '36329', 'name': 'Plasmodium falciparum 3D7', 'common_name': 'Malaria parasite'},
    'TOXGO': {'tax_id': '508771', 'name': 'Toxoplasma gondii ME49', 'common_name': None},
    'TRYB2': {'tax_id': '185431', 'name': 'Trypanosoma brucei brucei TREU927', 'common_name': None},
    'LEIMA': {'tax_id': '347515', 'name': 'Leishmania major strain Friedlin', 'common_name': None},
    'WHEAT': {'tax_id': '4565', 'name': 'Triticum aestivum', 'common_name': 'Wheat'},
    'SOYBN': {'tax_id': '3847', 'name': 'Glycine max', 'common_name': 'Soybean'},
    'MEDTR': {'tax_id': '3880', 'name': 'Medicago truncatula', 'common_name': 'Barrel medic'},
}

def fetch_proteome_id(tax_id: str) -> Optional[str]:
    """
    Fetch the reference proteome ID for a given taxonomy ID from UniProt.
    """
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

def fetch_reference_proteomes() -> List[Dict]:
    """
    Fetch all UniProt reference proteomes directly from the API.
    """
    species_list = []
    base_url = "https://rest.uniprot.org/proteomes/search"

    try:
        # Fetch reference proteomes (proteome_type:1)
        params = {
            'query': 'proteome_type:1',
            'format': 'json',
            'size': 500  # Maximum allowed by API
        }

        logger.info("Fetching all reference proteomes from UniProt...")
        logger.debug(f"URL: {base_url} with params: {params}")
        response = requests.get(base_url, params=params, timeout=30)
        logger.debug(f"Response status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            results = data.get('results', [])
            logger.info(f"Retrieved {len(results)} reference proteomes")

            for result in results:
                organism = result.get('taxonomy', {})
                proteome_id = result.get('id', '')

                code = organism.get('mnemonic', '')
                tax_id = str(organism.get('taxonId', ''))
                name = organism.get('scientificName', '')
                common_name = organism.get('commonName')

                if code and tax_id and name:
                    species_entry = {
                        'code': code,
                        'tax_id': tax_id,
                        'name': name,
                        'common_name': common_name,
                        'proteome_id': proteome_id
                    }
                    species_list.append(species_entry)
        else:
            logger.error(f"Failed to fetch proteomes: HTTP {response.status_code}")
            logger.error(f"Response text: {response.text[:500]}")

    except Exception as e:
        logger.error(f"Failed to fetch reference proteomes: {e}")

    return species_list

def fetch_uniprot_species_data(extended: bool = False) -> List[Dict]:
    """
    Fetch species data from UniProt reference proteomes.
    """
    if extended:
        logger.info("Fetching all reference proteomes")
        return fetch_reference_proteomes()
    else:
        # Use manual curated list for non-extended mode
        species_list = []
        organisms = COMMON_ORGANISMS.copy()
        logger.info("Using common model organisms only")

        # Fetch proteome IDs for each organism
        total = len(organisms)
        for idx, (code, info) in enumerate(organisms.items(), 1):
            logger.info(f"[{idx}/{total}] Fetching data for {code} ({info['name']})...")

            proteome_id = fetch_proteome_id(info['tax_id'])

            species_entry = {
                'code': code,
                'tax_id': info['tax_id'],
                'name': info['name'],
                'common_name': info.get('common_name'),
                'proteome_id': proteome_id
            }
            species_list.append(species_entry)

            if proteome_id:
                logger.info(f"  ✓ Found proteome {proteome_id}")
            else:
                logger.warning(f"  ✗ No proteome found")

        return species_list

def generate_yaml_content(species_list: List[Dict]) -> Dict:
    """
    Generate the YAML content for the UniProt species file.
    """
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
    for species in sorted(species_list, key=lambda x: x['code']):
        code = species['code']
        name = species['name']
        common_name = species.get('common_name')
        tax_id = species['tax_id']
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

        yaml_content['enums']['UniProtSpeciesCode']['permissible_values'][value_key] = pv_entry

    return yaml_content

def main():
    """Main function to sync UniProt species data."""
    parser = argparse.ArgumentParser(
        description='Sync UniProt species data with reference proteomes'
    )
    parser.add_argument(
        '--extended',
        action='store_true',
        help='Fetch all UniProt reference proteomes (~500+ organisms) instead of common model organisms only'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='src/valuesets/schema/bio/uniprot_species.yaml',
        help='Output file path (default: src/valuesets/schema/bio/uniprot_species.yaml)'
    )
    parser.add_argument(
        '--merge',
        action='store_true',
        default=True,
        help='Merge with existing entries (default: True)'
    )
    parser.add_argument(
        '--replace',
        action='store_true',
        help='Replace all existing entries instead of merging'
    )
    parser.add_argument(
        '--json-output',
        type=str,
        help='Also save raw data to JSON file for merging (e.g., cache/common_organisms.json)'
    )

    args = parser.parse_args()

    logger.info("=== UniProt Species Data Sync ===")

    # Load existing data if merging
    existing_content = None
    if args.merge and not args.replace and str(args.output) != '/dev/null' and Path(args.output).exists():
        logger.info(f"Loading existing data from {args.output} for merging...")
        with open(args.output, 'r') as f:
            existing_content = yaml.safe_load(f)

    # Fetch the species data
    species_list = fetch_uniprot_species_data(extended=args.extended)

    if not species_list:
        logger.error("No species data retrieved")
        return 1

    logger.info(f"\nRetrieved {len(species_list)} species")

    # Generate YAML content
    yaml_content = generate_yaml_content(species_list)

    # Merge with existing if requested
    if existing_content and args.merge and not args.replace:
        existing_pvs = existing_content.get('enums', {}).get('UniProtSpeciesCode', {}).get('permissible_values', {})
        new_pvs = yaml_content['enums']['UniProtSpeciesCode']['permissible_values']

        # Merge: add new entries and update existing ones that we have data for
        for key, value in new_pvs.items():
            existing_pvs[key] = value

        yaml_content['enums']['UniProtSpeciesCode']['permissible_values'] = existing_pvs
        logger.info(f"Merged with existing data: {len(existing_pvs)} total entries")

    # Write to file
    output_path = Path(args.output)

    # Skip writing if output is /dev/null
    if str(output_path) == '/dev/null':
        logger.info("Skipping YAML output (output is /dev/null)")
    else:
        # Create directory if it doesn't exist
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Backup existing file
        if output_path.exists():
            backup_path = output_path.with_suffix('.yaml.bak')
            output_path.rename(backup_path)
            logger.info(f"Backed up existing file to {backup_path}")

        # Write new file
        with open(output_path, 'w') as f:
            yaml.dump(yaml_content, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

        logger.info(f"✓ Generated {output_path} with {len(species_list)} species")

    # Save JSON if requested
    if args.json_output:
        json_path = Path(args.json_output)
        json_path.parent.mkdir(parents=True, exist_ok=True)
        with open(json_path, 'w') as f:
            json.dump(species_list, f, indent=2)
        logger.info(f"✓ Saved raw data to {json_path}")

    # List the codes that were added
    codes = [s['code'] for s in species_list]
    logger.info(f"\nSpecies codes: {', '.join(sorted(codes))}")

    # Report any missing proteomes
    missing_proteomes = [s['code'] for s in species_list if not s.get('proteome_id')]
    if missing_proteomes:
        logger.warning(f"\nSpecies without proteome IDs: {', '.join(missing_proteomes)}")

    return 0

if __name__ == "__main__":
    sys.exit(main())