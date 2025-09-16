"""
Shared utilities for extracting and processing mappings from LinkML schemas.

This module provides reusable functions for extracting all types of mappings
from PermissibleValue objects, which can be used by both the SSSOM generator
and the enum validator.
"""

from typing import List, Dict, Tuple, Optional, Any, Union
from linkml_runtime.linkml_model import PermissibleValue
import logging

logger = logging.getLogger(__name__)

# Mapping predicates for different mapping types
MAPPING_PREDICATES = {
    'meaning': 'skos:exactMatch',
    'exact_mappings': 'skos:exactMatch',
    'close_mappings': 'skos:closeMatch',
    'narrow_mappings': 'skos:narrowMatch',
    'broad_mappings': 'skos:broadMatch',
    'related_mappings': 'skos:relatedMatch'
}


def extract_all_mappings(
    pv: PermissibleValue,
    include_meaning: bool = True,
    include_annotations: bool = True
) -> List[Tuple[str, str, Optional[str]]]:
    """
    Extract all mappings from a PermissibleValue.

    Args:
        pv: The PermissibleValue object to extract mappings from
        include_meaning: Whether to include the 'meaning' field
        include_annotations: Whether to check annotations for related_mappings

    Returns:
        List of tuples: (object_id, predicate, comment)

    Example:
        >>> pv = PermissibleValue(
        ...     meaning="NCIT:C12345",
        ...     exact_mappings=["IAO:0000013", "FABIO:Article"],
        ...     close_mappings=["MESH:D012345"]
        ... )
        >>> mappings = extract_all_mappings(pv)
        >>> # Returns: [
        >>> #   ("NCIT:C12345", "skos:exactMatch", None),
        >>> #   ("IAO:0000013", "skos:exactMatch", None),
        >>> #   ("FABIO:Article", "skos:exactMatch", None),
        >>> #   ("MESH:D012345", "skos:closeMatch", None)
        >>> # ]
    """
    mappings = []

    # Extract 'meaning' field
    if include_meaning and hasattr(pv, 'meaning') and pv.meaning:
        mappings.append((pv.meaning, MAPPING_PREDICATES['meaning'], None))

    # Extract exact_mappings
    if hasattr(pv, 'exact_mappings') and pv.exact_mappings:
        for mapping in pv.exact_mappings:
            if mapping and isinstance(mapping, str):
                mappings.append((mapping, MAPPING_PREDICATES['exact_mappings'], None))

    # Extract close_mappings
    if hasattr(pv, 'close_mappings') and pv.close_mappings:
        for mapping in pv.close_mappings:
            if mapping and isinstance(mapping, str):
                mappings.append((mapping, MAPPING_PREDICATES['close_mappings'], None))

    # Extract narrow_mappings
    if hasattr(pv, 'narrow_mappings') and pv.narrow_mappings:
        for mapping in pv.narrow_mappings:
            if mapping and isinstance(mapping, str):
                mappings.append((mapping, MAPPING_PREDICATES['narrow_mappings'], None))

    # Extract broad_mappings
    if hasattr(pv, 'broad_mappings') and pv.broad_mappings:
        for mapping in pv.broad_mappings:
            if mapping and isinstance(mapping, str):
                mappings.append((mapping, MAPPING_PREDICATES['broad_mappings'], None))

    # Extract related_mappings from annotations if present
    if include_annotations and hasattr(pv, 'annotations') and pv.annotations:
        related = pv.annotations.get('related_mappings')
        if related:
            if isinstance(related, list):
                for mapping in related:
                    if mapping and isinstance(mapping, str):
                        mappings.append((mapping, MAPPING_PREDICATES['related_mappings'], "From annotations"))
            elif isinstance(related, str):
                # Handle single value
                mappings.append((related, MAPPING_PREDICATES['related_mappings'], "From annotations"))

    # Also check for the related_mappings field directly (if it exists)
    if hasattr(pv, 'related_mappings') and pv.related_mappings:
        for mapping in pv.related_mappings:
            if mapping and isinstance(mapping, str):
                mappings.append((mapping, MAPPING_PREDICATES['related_mappings'], None))

    return mappings


def get_mapping_statistics(pv: PermissibleValue) -> Dict[str, int]:
    """
    Get statistics about mappings in a PermissibleValue.

    Args:
        pv: The PermissibleValue object

    Returns:
        Dictionary with counts for each mapping type
    """
    stats = {
        'meaning': 0,
        'exact_mappings': 0,
        'close_mappings': 0,
        'narrow_mappings': 0,
        'broad_mappings': 0,
        'related_mappings': 0,
        'total': 0
    }

    if hasattr(pv, 'meaning') and pv.meaning:
        stats['meaning'] = 1

    for mapping_type in ['exact_mappings', 'close_mappings', 'narrow_mappings', 'broad_mappings', 'related_mappings']:
        if hasattr(pv, mapping_type):
            value = getattr(pv, mapping_type)
            if value:
                if isinstance(value, list):
                    stats[mapping_type] = len(value)
                else:
                    stats[mapping_type] = 1

    stats['total'] = sum(v for k, v in stats.items() if k != 'total')
    return stats


def validate_curie_format(curie: str) -> bool:
    """
    Validate that a string is in CURIE format (prefix:local_id).

    Args:
        curie: String to validate

    Returns:
        True if valid CURIE format, False otherwise
    """
    if not curie or not isinstance(curie, str):
        return False

    parts = curie.split(':')
    if len(parts) != 2:
        return False

    prefix, local_id = parts
    if not prefix or not local_id:
        return False

    # Basic validation - prefix should be alphanumeric (allowing underscores)
    # local_id can contain more characters
    return prefix.replace('_', '').isalnum()


def extract_ontology_prefix(curie: str) -> Optional[str]:
    """
    Extract the ontology prefix from a CURIE.

    Args:
        curie: CURIE string (e.g., "NCIT:C12345")

    Returns:
        The prefix part or None if invalid
    """
    if not validate_curie_format(curie):
        return None

    return curie.split(':')[0]


def group_mappings_by_ontology(
    mappings: List[Tuple[str, str, Optional[str]]]
) -> Dict[str, List[Tuple[str, str, Optional[str]]]]:
    """
    Group mappings by their ontology prefix.

    Args:
        mappings: List of mapping tuples from extract_all_mappings

    Returns:
        Dictionary with ontology prefixes as keys and lists of mappings as values
    """
    grouped = {}

    for object_id, predicate, comment in mappings:
        prefix = extract_ontology_prefix(object_id)
        if prefix:
            if prefix not in grouped:
                grouped[prefix] = []
            grouped[prefix].append((object_id, predicate, comment))
        else:
            # Handle non-CURIE mappings
            if 'OTHER' not in grouped:
                grouped['OTHER'] = []
            grouped['OTHER'].append((object_id, predicate, comment))

    return grouped


def deduplicate_mappings(
    mappings: List[Tuple[str, str, Optional[str]]]
) -> List[Tuple[str, str, Optional[str]]]:
    """
    Remove duplicate mappings, keeping the first occurrence.

    Args:
        mappings: List of mapping tuples

    Returns:
        Deduplicated list of mappings
    """
    seen = set()
    deduped = []

    for object_id, predicate, comment in mappings:
        # Use object_id and predicate as the key for deduplication
        key = (object_id, predicate)
        if key not in seen:
            seen.add(key)
            deduped.append((object_id, predicate, comment))

    return deduped