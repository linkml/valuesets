#!/usr/bin/env python3
"""
SSSOM TSV generator for LinkML enum mappings.

Generates Simple Standard for Sharing Ontological Mappings (SSSOM) TSV files
from LinkML enum definitions with ontology mappings.
"""

import csv
import logging
from pathlib import Path
from typing import List, Dict, Optional, Any
from datetime import datetime

from linkml_runtime.utils.schemaview import SchemaView
from linkml_runtime.linkml_model import EnumDefinition, PermissibleValue

# Import shared mapping utilities
try:
    from ..utils.mapping_utils import extract_all_mappings, deduplicate_mappings
except ImportError:
    # Fallback for running as script
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent.parent.parent))
    from valuesets.utils.mapping_utils import extract_all_mappings, deduplicate_mappings

try:
    from oaklib import get_adapter
    HAS_OAK = True
except ImportError:
    HAS_OAK = False

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# SSSOM required prefixes
SSSOM_PREFIXES = {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "sssom": "https://w3id.org/sssom/",
    "dcterms": "http://purl.org/dc/terms/",
    "semapv": "https://w3id.org/semapv/",
}


class SSSOMGenerator:
    """Generator for SSSOM TSV files from LinkML schemas."""

    def __init__(self, oak_adapter_string: str = "sqlite:obo:", cache_labels: bool = True):
        """
        Initialize the SSSOM generator.

        Args:
            oak_adapter_string: OAK adapter configuration
            cache_labels: Whether to cache ontology labels
        """
        self.oak_adapter_string = oak_adapter_string
        self._label_cache = {} if cache_labels else None
        self._per_prefix_adapters = {}
        self._initialize_oak()

    def _initialize_oak(self):
        """Initialize OAK for label lookups."""
        if not HAS_OAK:
            logger.warning("OAK not installed - labels will not be retrieved")
            return

        # Similar to enum_evaluator, we'll create adapters on demand
        if self.oak_adapter_string == "sqlite:obo:":
            logger.info("Using dynamic OAK adapter selection")
        else:
            try:
                self._per_prefix_adapters['_default'] = get_adapter(self.oak_adapter_string)
                logger.info(f"Initialized OAK adapter: {self.oak_adapter_string}")
            except Exception as e:
                logger.warning(f"Could not initialize OAK: {e}")

    def get_ontology_label(self, curie: str) -> Optional[str]:
        """Get label for an ontology term."""
        if not HAS_OAK:
            return None

        # Check cache
        if self._label_cache is not None and curie in self._label_cache:
            return self._label_cache[curie]

        label = None
        prefix = curie.split(":")[0].lower() if ":" in curie else None

        # Get or create adapter
        if self.oak_adapter_string == "sqlite:obo:" and prefix:
            if prefix not in self._per_prefix_adapters:
                try:
                    adapter_string = f"sqlite:obo:{prefix}"
                    self._per_prefix_adapters[prefix] = get_adapter(adapter_string)
                    logger.debug(f"Created adapter for {prefix}")
                except:
                    # Try merged as fallback
                    try:
                        self._per_prefix_adapters[prefix] = get_adapter("sqlite:obo:merged")
                    except:
                        self._per_prefix_adapters[prefix] = None

            adapter = self._per_prefix_adapters.get(prefix)
        else:
            adapter = self._per_prefix_adapters.get('_default')

        # Get label
        if adapter:
            try:
                label = adapter.label(curie)
            except Exception as e:
                logger.debug(f"Could not get label for {curie}: {e}")

        # Cache result
        if self._label_cache is not None:
            self._label_cache[curie] = label

        return label

    def generate_mappings(self, schema_path: Path) -> List[Dict[str, Any]]:
        """
        Generate SSSOM mappings from a LinkML schema.

        Args:
            schema_path: Path to LinkML schema file

        Returns:
            List of mapping dictionaries
        """
        mappings = []

        try:
            sv = SchemaView(str(schema_path))
            schema_id = sv.schema.id or str(schema_path)

            # Process each enum
            for enum_name, enum_def in sv.all_enums().items():
                if not enum_def.permissible_values:
                    continue

                # Build enum URI
                if sv.schema.default_prefix:
                    prefix = sv.schema.default_prefix
                    enum_uri = f"{prefix}:{enum_name}"
                else:
                    enum_uri = f"{schema_id}#{enum_name}"

                # Process each permissible value
                for value_name, pv in enum_def.permissible_values.items():
                    # Extract all mappings using shared utility
                    pv_mappings = extract_all_mappings(pv, include_meaning=True, include_annotations=True)

                    # Skip if no mappings
                    if not pv_mappings:
                        continue

                    # Deduplicate mappings
                    pv_mappings = deduplicate_mappings(pv_mappings)

                    # Build subject URI
                    subject_id = f"{enum_uri}.{value_name}"

                    # Process each mapping
                    for object_id, predicate, mapping_comment in pv_mappings:
                        # Get object label
                        object_label = self.get_ontology_label(object_id)

                        # Build comment
                        comment_parts = []
                        if pv.description:
                            comment_parts.append(pv.description)
                        if mapping_comment:
                            comment_parts.append(mapping_comment)
                        comment = "; ".join(comment_parts)

                        # Determine confidence based on predicate
                        confidence = 1.0
                        if predicate == "skos:closeMatch":
                            confidence = 0.9
                        elif predicate == "skos:narrowMatch" or predicate == "skos:broadMatch":
                            confidence = 0.8
                        elif predicate == "skos:relatedMatch":
                            confidence = 0.7

                        # Create mapping
                        mapping = {
                            "subject_id": subject_id,
                            "subject_label": pv.title or value_name,
                            "predicate_id": predicate,
                            "object_id": object_id,
                            "object_label": object_label or "",
                            "mapping_justification": "semapv:ManualMappingCuration",
                            "subject_source": schema_id,
                            "object_source": self._extract_ontology_source(object_id),
                            "mapping_tool": "linkml-valuesets",
                            "confidence": confidence,
                            "subject_type": "enum_value",
                            "object_type": "ontology_class",
                            "comment": comment
                        }

                        mappings.append(mapping)

        except Exception as e:
            logger.error(f"Error processing schema {schema_path}: {e}")

        return mappings

    def _extract_ontology_source(self, curie: str) -> str:
        """Extract ontology source from CURIE."""
        if ":" in curie:
            prefix = curie.split(":")[0]
            # Map common prefixes to ontology names
            ontology_map = {
                "NCIT": "ncit",
                "CHEBI": "chebi",
                "GO": "go",
                "UBERON": "uberon",
                "HP": "hp",
                "MONDO": "mondo",
                "ENVO": "envo",
                "OBI": "obi",
                "SNOMED": "snomed",
                "LOINC": "loinc",
                "MSIO": "msio",
                "mesh": "mesh",
                "IAO": "iao",
                "FABIO": "fabio",
                "PATO": "pato",
                "GENO": "geno",
                "GSSO": "gsso",
                "MS": "ms",
                "CRediT": "credit",
                "TIME": "time",
                "greg": "gregorian"
            }
            return ontology_map.get(prefix, prefix.lower())
        return ""

    def write_sssom_tsv(self, mappings: List[Dict[str, Any]], output_path: Path,
                        metadata: Optional[Dict[str, str]] = None):
        """
        Write mappings to SSSOM TSV file.

        Args:
            mappings: List of mapping dictionaries
            output_path: Output file path
            metadata: Optional metadata for SSSOM header
        """
        if not mappings:
            logger.warning("No mappings to write")
            return

        # Prepare metadata
        meta = metadata or {}
        meta.setdefault("mapping_set_id", f"https://w3id.org/linkml/valuesets/mappings")
        meta.setdefault("mapping_set_version", datetime.now().strftime("%Y-%m-%d"))
        meta.setdefault("license", "https://creativecommons.org/publicdomain/zero/1.0/")
        meta.setdefault("creator_id", "https://github.com/linkml/linkml-valuesets")

        with open(output_path, 'w', newline='') as f:
            # Write metadata header
            f.write("#curie_map:\n")
            for prefix, uri in SSSOM_PREFIXES.items():
                f.write(f"#  {prefix}: \"{uri}\"\n")
            f.write("#\n")

            for key, value in meta.items():
                f.write(f"#{key}: {value}\n")
            f.write("#\n")

            # Define field order (SSSOM standard order)
            fieldnames = [
                "subject_id",
                "subject_label",
                "predicate_id",
                "object_id",
                "object_label",
                "mapping_justification",
                "subject_source",
                "object_source",
                "mapping_tool",
                "confidence",
                "subject_type",
                "object_type",
                "comment"
            ]

            # Write TSV data
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='\t',
                                   extrasaction='ignore')
            writer.writeheader()
            writer.writerows(mappings)

        logger.info(f"Wrote {len(mappings)} mappings to {output_path}")

    def generate_from_directory(self, schema_dir: Path, output_path: Path,
                               metadata: Optional[Dict[str, str]] = None):
        """
        Generate SSSOM TSV from all schemas in a directory.

        Args:
            schema_dir: Directory containing LinkML schemas
            output_path: Output TSV file path
            metadata: Optional SSSOM metadata
        """
        all_mappings = []

        for schema_file in sorted(schema_dir.rglob("*.yaml")):
            # Skip linkml model files
            if "linkml_model" in str(schema_file):
                continue

            logger.info(f"Processing {schema_file.name}")
            mappings = self.generate_mappings(schema_file)
            all_mappings.extend(mappings)

        self.write_sssom_tsv(all_mappings, output_path, metadata)
        return all_mappings


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate SSSOM TSV from LinkML enum mappings"
    )
    parser.add_argument(
        "input",
        type=Path,
        help="Input LinkML schema file or directory"
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=Path("mappings.sssom.tsv"),
        help="Output SSSOM TSV file (default: mappings.sssom.tsv)"
    )
    parser.add_argument(
        "--adapter",
        default="sqlite:obo:",
        help="OAK adapter string for label lookups"
    )
    parser.add_argument(
        "--no-labels",
        action="store_true",
        help="Skip ontology label lookups"
    )
    parser.add_argument(
        "--mapping-set-id",
        help="Mapping set ID for SSSOM metadata"
    )
    parser.add_argument(
        "--license",
        help="License URL for SSSOM metadata"
    )

    args = parser.parse_args()

    # Create generator
    if args.no_labels:
        generator = SSSOMGenerator(oak_adapter_string=None)
    else:
        generator = SSSOMGenerator(oak_adapter_string=args.adapter)

    # Prepare metadata
    metadata = {}
    if args.mapping_set_id:
        metadata["mapping_set_id"] = args.mapping_set_id
    if args.license:
        metadata["license"] = args.license

    # Generate mappings
    if args.input.is_file():
        mappings = generator.generate_mappings(args.input)
        generator.write_sssom_tsv(mappings, args.output, metadata)
    elif args.input.is_dir():
        generator.generate_from_directory(args.input, args.output, metadata)
    else:
        print(f"Error: {args.input} is not a file or directory")
        return 1

    print(f"Generated SSSOM TSV: {args.output}")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
