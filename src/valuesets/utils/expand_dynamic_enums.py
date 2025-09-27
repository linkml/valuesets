#!/usr/bin/env python
"""
Utility script to expand all dynamic enums from LinkML schemas using OAK's vskit.

This script:
1. Scans all schema files for dynamic enum definitions
2. Uses OAK's vskit expand_in_place to expand each dynamic enum
3. Saves the expanded enums to a parallel directory structure under src/valuesets/expanded/
"""

import yaml
from pathlib import Path
from typing import Dict, Any, Optional, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging
import tempfile
from oaklib.utilities.subsets.value_set_expander import ValueSetExpander
from copy import deepcopy

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class DynamicEnumExpander:
    """Expands dynamic enums from LinkML schemas using OAK's vskit."""

    def __init__(self, schema_dir: Path, output_dir: Path):
        """
        Initialize the expander.

        Args:
            schema_dir: Directory containing LinkML schema files
            output_dir: Directory where expanded enums will be saved
        """
        self.schema_dir = Path(schema_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Cache for value set expanders
        self.expanders = {}

    def get_expander(self, ontology: str) -> Optional[ValueSetExpander]:
        """Get or create a ValueSetExpander for an ontology."""
        if ontology not in self.expanders:
            try:
                # Use OBO format for standard ontologies
                if ontology.startswith('obo:'):
                    ontology_id = ontology.replace('obo:', '')
                    adapter_spec = f"sqlite:obo:{ontology_id}"
                else:
                    adapter_spec = ontology

                logger.info(f"Creating expander for {ontology}: {adapter_spec}")
                # Create expander
                self.expanders[ontology] = ValueSetExpander(resource=adapter_spec)
            except Exception as e:
                logger.error(f"Failed to create expander for {ontology}: {e}")
                import traceback
                logger.error(f"Traceback: {traceback.format_exc()}")
                return None
        return self.expanders[ontology]

    def expand_dynamic_enum(self, enum_name: str, enum_def: Dict[str, Any],
                           source_file: Path, source_schema: Dict[str, Any] = None) -> Optional[Dict[str, Any]]:
        """
        Expand a single dynamic enum definition using OAK's expand_in_place.

        Args:
            enum_name: Name of the enum
            enum_def: Enum definition from schema
            source_file: Path to the source schema file
            source_schema: The full source schema (for extracting prefixes)

        Returns:
            Expanded enum with permissible_values populated
        """
        if 'reachable_from' not in enum_def:
            return None

        reachable = enum_def['reachable_from']
        source_ontology = reachable.get('source_ontology')

        # If no source_ontology specified, try to infer from source_nodes
        if not source_ontology:
            source_nodes = reachable.get('source_nodes', [])
            if source_nodes:
                first_node = source_nodes[0] if isinstance(source_nodes, list) else source_nodes
                # Infer ontology from prefix
                if first_node.startswith('OBI:'):
                    source_ontology = 'obo:obi'
                elif first_node.startswith('NCBITaxon:'):
                    source_ontology = 'obo:ncbitaxon'
                elif first_node.startswith('MONDO:'):
                    source_ontology = 'obo:mondo'
                elif first_node.startswith('HP:'):
                    source_ontology = 'obo:hp'
                elif first_node.startswith('UBERON:'):
                    source_ontology = 'obo:uberon'
                elif first_node.startswith('CL:'):
                    source_ontology = 'obo:cl'
                elif first_node.startswith('PO:'):
                    source_ontology = 'obo:po'
                elif first_node.startswith('PATO:'):
                    source_ontology = 'obo:pato'
                elif first_node.startswith('CHEBI:'):
                    source_ontology = 'obo:chebi'
                elif first_node.startswith('GO:'):
                    source_ontology = 'obo:go'
                else:
                    # Default fallback
                    source_ontology = 'obo:mondo'
                logger.info(f"  Inferred source_ontology={source_ontology} from node {first_node}")

        if not source_ontology:
            source_ontology = 'obo:mondo'  # Ultimate fallback

        logger.info(f"Expanding {enum_name} from {source_file}")
        logger.info(f"  Source: {source_ontology}")

        expander = self.get_expander(source_ontology)
        if not expander:
            logger.error(f"Could not get expander for {source_ontology}")
            return None

        try:
            # Create a copy of the enum definition for expansion
            expanded_enum = deepcopy(enum_def)

            # Ensure source_ontology is set in reachable_from
            if 'reachable_from' in expanded_enum:
                expanded_enum['reachable_from']['source_ontology'] = source_ontology

            # Create a minimal schema with just this enum
            schema_dict = {
                'id': f'https://example.org/temp/{enum_name}',
                'name': f'temp_schema_{enum_name}',
                'enums': {
                    enum_name: expanded_enum
                }
            }

            # Write to temporary files for expand_in_place
            with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as tmp:
                yaml.safe_dump(schema_dict, tmp)
                tmp_path = tmp.name

            with tempfile.NamedTemporaryFile(mode='w', suffix='_expanded.yaml', delete=False) as out:
                out_path = out.name

            try:
                # Use expand_in_place with pv_syntax for LABEL format and output_path
                expanded_schema = expander.expand_in_place(
                    tmp_path,
                    value_set_names=[enum_name],
                    output_path=out_path,
                    pv_syntax="{label}"  # Use label as the text field
                )

                # Read the expanded schema from output file
                try:
                    with open(out_path, 'r') as f:
                        expanded_data = yaml.safe_load(f)

                    # Get the expanded enum
                    if expanded_data and 'enums' in expanded_data and enum_name in expanded_data['enums']:
                        expanded_enum_def = expanded_data['enums'][enum_name]
                    else:
                        logger.warning(f"No expanded enum found for {enum_name}")
                        expanded_enum_def = {'permissible_values': {}}
                except yaml.YAMLError as e:
                    # If YAML parsing fails, try using a safer pv_syntax
                    logger.warning(f"YAML parsing failed for {enum_name}, retrying with ID-based keys: {e}")

                    # Clean up the failed output file
                    Path(out_path).unlink(missing_ok=True)

                    # Retry with ID-based syntax which should be YAML-safe
                    with tempfile.NamedTemporaryFile(mode='w', suffix='_expanded_safe.yaml', delete=False) as out2:
                        out_path2 = out2.name

                    try:
                        expanded_schema = expander.expand_in_place(
                            tmp_path,
                            value_set_names=[enum_name],
                            output_path=out_path2,
                            pv_syntax="{id}"  # Use ID which should be YAML-safe
                        )

                        with open(out_path2, 'r') as f:
                            expanded_data = yaml.safe_load(f)

                        if expanded_data and 'enums' in expanded_data and enum_name in expanded_data['enums']:
                            expanded_enum_def = expanded_data['enums'][enum_name]
                        else:
                            expanded_enum_def = {'permissible_values': {}}
                    finally:
                        Path(out_path2).unlink(missing_ok=True)
            finally:
                # Clean up temp files
                Path(tmp_path).unlink(missing_ok=True)
                Path(out_path).unlink(missing_ok=True)

            # Extract just the parts we need
            result = {
                'description': expanded_enum_def.get('description', f'Expanded from {enum_name}'),
                'permissible_values': expanded_enum_def.get('permissible_values', {}),
                '_source': {
                    'enum_name': enum_name,
                    'source_file': str(source_file),
                    'source_ontology': source_ontology,
                    'reachable_from': reachable,
                    'total_terms': len(expanded_enum_def.get('permissible_values', {})),
                    'source_schema': source_schema  # Include source schema for prefix extraction
                }
            }

            logger.info(f"  Expanded to {result['_source']['total_terms']} permissible values")
            return result

        except Exception as e:
            logger.error(f"Failed to expand {enum_name}: {e}")
            return None

    def find_dynamic_enums(self) -> Dict[Path, Tuple[Dict[str, Any], Dict[str, Any]]]:
        """
        Find all dynamic enum definitions in schema files.

        Returns:
            Dictionary mapping file paths to tuples of (dynamic_enums, full_schema)
        """
        dynamic_enums = {}

        for yaml_file in self.schema_dir.rglob('*.yaml'):
            try:
                with open(yaml_file, 'r') as f:
                    schema = yaml.safe_load(f)

                if not schema or 'enums' not in schema:
                    continue

                file_dynamic_enums = {}
                for enum_name, enum_def in schema['enums'].items():
                    if 'reachable_from' in enum_def:
                        file_dynamic_enums[enum_name] = enum_def

                if file_dynamic_enums:
                    dynamic_enums[yaml_file] = (file_dynamic_enums, schema)
                    logger.info(f"Found {len(file_dynamic_enums)} dynamic enums in {yaml_file}")

            except Exception as e:
                logger.warning(f"Could not parse {yaml_file}: {e}")

        return dynamic_enums

    def save_expanded_enum(self, enum_name: str, expanded_enum: Dict[str, Any],
                          source_file: Path) -> Path:
        """
        Save an expanded enum to the output directory as a valid LinkML schema YAML.

        Args:
            enum_name: Name of the enum
            expanded_enum: Expanded enum data
            source_file: Original source file path

        Returns:
            Path to the saved file
        """
        # Create parallel directory structure
        relative_path = source_file.relative_to(self.schema_dir)
        output_file = self.output_dir / relative_path.parent / f"{enum_name}.yaml"
        output_file.parent.mkdir(parents=True, exist_ok=True)

        # Get prefixes from source schema if available
        source_schema = expanded_enum.get('_source', {}).get('source_schema', {})
        prefixes = source_schema.get('prefixes', {}).copy() if source_schema else {}

        # Ensure basic prefixes are present
        if 'linkml' not in prefixes:
            prefixes['linkml'] = 'https://w3id.org/linkml/'
        if 'valuesets' not in prefixes:
            prefixes['valuesets'] = 'https://w3id.org/valuesets/'

        # Get default prefix from source or use valuesets
        default_prefix = source_schema.get('default_prefix', 'valuesets') if source_schema else 'valuesets'

        # Create a valid LinkML schema with the enum
        schema_yaml = {
            'id': f'https://w3id.org/valuesets/expanded/{enum_name}',
            'name': f'{enum_name}_expanded',
            'description': f'Expanded value set for {enum_name}',
            'imports': ['linkml:types'],
            'prefixes': prefixes,
            'default_prefix': default_prefix,
            'enums': {
                enum_name: {
                    'description': expanded_enum['description'],
                    'permissible_values': expanded_enum['permissible_values']
                }
            }
        }

        # Save as YAML using safe_dump to avoid Python object tags
        with open(output_file, 'w') as f:
            yaml.safe_dump(schema_yaml, f, default_flow_style=False, sort_keys=False,
                          allow_unicode=True, width=120)

        logger.info(f"Saved expanded enum to {output_file}")
        return output_file

    def expand_all(self, max_workers: int = 4):
        """
        Expand all dynamic enums found in the schema directory.

        Args:
            max_workers: Maximum number of parallel workers
        """
        # Find all dynamic enums
        dynamic_enums = self.find_dynamic_enums()

        if not dynamic_enums:
            logger.info("No dynamic enums found")
            return

        logger.info(f"Found dynamic enums in {len(dynamic_enums)} files")

        # Process enums
        total_enums = sum(len(enums_and_schema[0]) for enums_and_schema in dynamic_enums.values())
        processed = 0
        failed = 0

        # Create a flat list of tasks
        tasks = []
        for file_path, (enums, schema) in dynamic_enums.items():
            for enum_name, enum_def in enums.items():
                tasks.append((enum_name, enum_def, file_path, schema))

        # Process in parallel
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {}

            for enum_name, enum_def, file_path, schema in tasks:
                future = executor.submit(
                    self.expand_dynamic_enum,
                    enum_name,
                    enum_def,
                    file_path,
                    schema
                )
                futures[future] = (enum_name, file_path)

            for future in as_completed(futures):
                enum_name, file_path = futures[future]
                try:
                    expanded_enum = future.result(timeout=60)
                    if expanded_enum:
                        self.save_expanded_enum(enum_name, expanded_enum, file_path)
                        processed += 1
                    else:
                        failed += 1
                except Exception as e:
                    logger.error(f"Failed to process {enum_name}: {e}")
                    failed += 1

        logger.info(f"Expansion complete: {processed} successful, {failed} failed out of {total_enums} total")

        # Create summary file
        summary = {
            'total_enums': total_enums,
            'processed': processed,
            'failed': failed,
            'source_files': [str(f) for f in dynamic_enums.keys()]
        }

        summary_file = self.output_dir / 'expansion_summary.yaml'
        with open(summary_file, 'w') as f:
            yaml.safe_dump(summary, f, default_flow_style=False, sort_keys=False)

        logger.info(f"Summary saved to {summary_file}")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Expand dynamic enums from LinkML schemas using OAK'
    )
    parser.add_argument(
        '--schema-dir',
        type=Path,
        default=Path('src/valuesets/schema'),
        help='Directory containing LinkML schema files'
    )
    parser.add_argument(
        '--output-dir',
        type=Path,
        default=Path('src/valuesets/expanded'),
        help='Output directory for expanded enums (default: src/valuesets/expanded)'
    )
    parser.add_argument(
        '--workers',
        type=int,
        default=4,
        help='Number of parallel workers'
    )

    args = parser.parse_args()

    expander = DynamicEnumExpander(args.schema_dir, args.output_dir)
    expander.expand_all(max_workers=args.workers)


if __name__ == '__main__':
    main()