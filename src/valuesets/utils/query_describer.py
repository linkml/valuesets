"""
Utility for describing dynamic enum queries in human-readable text.

Converts LinkML reachable_from definitions into readable descriptions
like "subclasses of 'cell' (CL:0000000)".
"""

from dataclasses import dataclass, field
from typing import Any


# Standard OBO prefix expansions
OBO_PREFIXES = {
    "UBERON": "http://purl.obolibrary.org/obo/UBERON_",
    "CL": "http://purl.obolibrary.org/obo/CL_",
    "MONDO": "http://purl.obolibrary.org/obo/MONDO_",
    "CHEBI": "http://purl.obolibrary.org/obo/CHEBI_",
    "HP": "http://purl.obolibrary.org/obo/HP_",
    "GO": "http://purl.obolibrary.org/obo/GO_",
    "DOID": "http://purl.obolibrary.org/obo/DOID_",
    "NCBITaxon": "http://purl.obolibrary.org/obo/NCBITaxon_",
    "ENVO": "http://purl.obolibrary.org/obo/ENVO_",
    "PO": "http://purl.obolibrary.org/obo/PO_",
    "PR": "http://purl.obolibrary.org/obo/PR_",
    "SO": "http://purl.obolibrary.org/obo/SO_",
    "PATO": "http://purl.obolibrary.org/obo/PATO_",
    "RO": "http://purl.obolibrary.org/obo/RO_",
    "BFO": "http://purl.obolibrary.org/obo/BFO_",
    "OBI": "http://purl.obolibrary.org/obo/OBI_",
    "IAO": "http://purl.obolibrary.org/obo/IAO_",
    "ECO": "http://purl.obolibrary.org/obo/ECO_",
    "NCIT": "http://purl.obolibrary.org/obo/NCIT_",
    "GAZ": "http://purl.obolibrary.org/obo/GAZ_",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "obo": "http://purl.obolibrary.org/obo/",
}


@dataclass
class QueryDescription:
    """Description of a dynamic enum query."""

    text: str
    prefixes: set[str]
    markdown: str = ""

    def __str__(self) -> str:
        return self.text


def extract_prefix(curie: str) -> str | None:
    """Extract prefix from a CURIE.

    >>> extract_prefix("CL:0000000")
    'CL'
    >>> extract_prefix("rdfs:subClassOf")
    'rdfs'
    >>> extract_prefix("not_a_curie")
    """
    if ":" in curie:
        return curie.split(":")[0]
    return None


def curie_to_uri(curie: str, prefix_map: dict[str, str] | None = None) -> str | None:
    """Expand a CURIE to a full URI.

    >>> curie_to_uri("CL:0000000")
    'http://purl.obolibrary.org/obo/CL_0000000'
    >>> curie_to_uri("rdfs:subClassOf")
    'http://www.w3.org/2000/01/rdf-schema#subClassOf'
    >>> curie_to_uri("UNKNOWN:123")
    """
    if ":" not in curie:
        return None

    prefix, local = curie.split(":", 1)

    # Check provided prefix map first
    if prefix_map and prefix in prefix_map:
        return f"{prefix_map[prefix]}{local}"

    # Fall back to OBO prefixes
    if prefix in OBO_PREFIXES:
        return f"{OBO_PREFIXES[prefix]}{local}"

    return None


def format_markdown_link(curie: str, label: str | None = None, prefix_map: dict[str, str] | None = None) -> str:
    """Format a CURIE as a markdown link.

    >>> format_markdown_link("CL:0000000", "cell")
    '[cell](http://purl.obolibrary.org/obo/CL_0000000)'
    >>> format_markdown_link("CL:0000000")
    '[CL:0000000](http://purl.obolibrary.org/obo/CL_0000000)'
    >>> format_markdown_link("UNKNOWN:123")
    'UNKNOWN:123'
    """
    uri = curie_to_uri(curie, prefix_map)
    display = label if label else curie
    if uri:
        return f"[{display}]({uri})"
    return curie


def get_prefixes_from_query(reachable_from: dict[str, Any]) -> set[str]:
    """Extract all prefixes used in a reachable_from query.

    >>> get_prefixes_from_query({"source_nodes": ["CL:0000000"], "relationship_types": ["rdfs:subClassOf"]})
    {'CL', 'rdfs'}
    >>> get_prefixes_from_query({"source_nodes": ["UBERON:0000061", "CL:0000000"]})
    {'CL', 'UBERON'}
    """
    prefixes = set()

    # Source nodes
    for node in reachable_from.get("source_nodes", []):
        if prefix := extract_prefix(node):
            prefixes.add(prefix)

    # Relationship types
    for rel in reachable_from.get("relationship_types", []):
        if prefix := extract_prefix(rel):
            prefixes.add(prefix)

    # Source ontology (extract from obo:xxx format)
    if source_ont := reachable_from.get("source_ontology"):
        if prefix := extract_prefix(source_ont):
            prefixes.add(prefix)

    return prefixes


def describe_relationship_types(rel_types: list[str]) -> str:
    """Describe relationship types in human-readable form.

    >>> describe_relationship_types(["rdfs:subClassOf"])
    'subclasses'
    >>> describe_relationship_types(["rdfs:subClassOf", "BFO:0000050"])
    'subclasses or BFO:0000050 related'
    >>> describe_relationship_types([])
    'descendants'
    """
    if not rel_types:
        return "descendants"

    if rel_types == ["rdfs:subClassOf"]:
        return "subclasses"

    if "rdfs:subClassOf" in rel_types:
        others = [r for r in rel_types if r != "rdfs:subClassOf"]
        if others:
            return f"subclasses or {', '.join(others)} related"
        return "subclasses"

    return f"{', '.join(rel_types)} related"


def describe_reachable_from(
    reachable_from: dict[str, Any],
    label_lookup: dict[str, str] | None = None,
    prefix_map: dict[str, str] | None = None,
) -> QueryDescription:
    """Describe a reachable_from query in human-readable text.

    Args:
        reachable_from: The reachable_from dict from a LinkML enum definition
        label_lookup: Optional dict mapping CURIEs to labels
        prefix_map: Optional dict mapping prefixes to URI bases

    Returns:
        QueryDescription with text, prefixes, and markdown

    >>> desc = describe_reachable_from({"source_nodes": ["CL:0000000"], "relationship_types": ["rdfs:subClassOf"]})
    >>> desc.text
    "subclasses of 'CL:0000000'"
    >>> desc.prefixes
    {'CL', 'rdfs'}

    >>> desc = describe_reachable_from({"source_nodes": ["CL:0000000"], "include_self": True})
    >>> "'CL:0000000' and descendants" in desc.text
    True

    >>> desc = describe_reachable_from({"source_nodes": ["CL:0000000"]}, {"CL:0000000": "cell"})
    >>> "cell" in desc.markdown
    True
    """
    label_lookup = label_lookup or {}
    prefixes = get_prefixes_from_query(reachable_from)

    source_nodes = reachable_from.get("source_nodes", [])
    rel_types = reachable_from.get("relationship_types", [])
    include_self = reachable_from.get("include_self", False)
    is_direct = reachable_from.get("is_direct", False)

    # Format source nodes - plain text version
    def format_node(node: str) -> str:
        if node in label_lookup:
            return f"'{label_lookup[node]}' ({node})"
        return f"'{node}'"

    # Format source nodes - markdown version with links
    def format_node_md(node: str) -> str:
        label = label_lookup.get(node)
        return format_markdown_link(node, label, prefix_map)

    formatted_nodes = [format_node(n) for n in source_nodes]
    formatted_nodes_md = [format_node_md(n) for n in source_nodes]

    # Build description
    if len(formatted_nodes) == 0:
        nodes_text = "[no source nodes]"
        nodes_text_md = "[no source nodes]"
    elif len(formatted_nodes) == 1:
        nodes_text = formatted_nodes[0]
        nodes_text_md = formatted_nodes_md[0]
    else:
        nodes_text = " | ".join(formatted_nodes)
        nodes_text_md = " | ".join(formatted_nodes_md)

    rel_desc = describe_relationship_types(rel_types)

    if is_direct:
        rel_desc = f"direct {rel_desc}"

    if include_self:
        text = f"{nodes_text} and {rel_desc}"
        markdown = f"{nodes_text_md} and {rel_desc}"
    else:
        text = f"{rel_desc} of {nodes_text}"
        markdown = f"{rel_desc} of {nodes_text_md}"

    return QueryDescription(text=text, prefixes=prefixes, markdown=markdown)


def describe_enum_query(
    enum_def: dict[str, Any],
    label_lookup: dict[str, str] | None = None,
    prefix_map: dict[str, str] | None = None,
) -> QueryDescription | None:
    """Describe the query for an enum definition.

    Handles simple reachable_from, plus include/minus composition.

    Args:
        enum_def: The enum definition dict
        label_lookup: Optional dict mapping CURIEs to labels
        prefix_map: Optional dict mapping prefixes to URI bases

    Returns:
        QueryDescription or None if not a dynamic enum

    >>> desc = describe_enum_query({"reachable_from": {"source_nodes": ["CL:0000000"]}})
    >>> desc is not None
    True
    """
    if "reachable_from" not in enum_def:
        return None

    reachable_from = enum_def["reachable_from"]

    # Handle include/minus composition
    if "include" in enum_def or "minus" in enum_def:
        parts = []
        parts_md = []
        all_prefixes = set()

        if "include" in enum_def:
            for inc in enum_def["include"]:
                if "reachable_from" in inc:
                    desc = describe_reachable_from(inc["reachable_from"], label_lookup, prefix_map)
                    parts.append(f"INCLUDE {desc.text}")
                    parts_md.append(f"INCLUDE {desc.markdown}")
                    all_prefixes.update(desc.prefixes)

        if "reachable_from" in enum_def:
            desc = describe_reachable_from(reachable_from, label_lookup, prefix_map)
            parts.append(desc.text)
            parts_md.append(desc.markdown)
            all_prefixes.update(desc.prefixes)

        if "minus" in enum_def:
            minus = enum_def["minus"]
            if "concepts" in minus:
                concepts = minus["concepts"]
                formatted = [label_lookup.get(c, c) if label_lookup else c for c in concepts]
                formatted_md = [format_markdown_link(c, label_lookup.get(c) if label_lookup else None, prefix_map) for c in concepts]
                parts.append(f"MINUS [{', '.join(formatted)}]")
                parts_md.append(f"MINUS [{', '.join(formatted_md)}]")
                for c in concepts:
                    if prefix := extract_prefix(c):
                        all_prefixes.add(prefix)

        return QueryDescription(text=" ".join(parts), prefixes=all_prefixes, markdown=" ".join(parts_md))

    # Simple reachable_from
    return describe_reachable_from(reachable_from, label_lookup, prefix_map)


def get_prefix_signature(enum_def: dict[str, Any]) -> set[str]:
    """Get just the prefix signature from an enum definition.

    >>> get_prefix_signature({"reachable_from": {"source_nodes": ["CL:0000000", "UBERON:0000061"]}})
    {'CL', 'UBERON'}
    """
    desc = describe_enum_query(enum_def)
    return desc.prefixes if desc else set()


def list_dynamic_enums(schema_dir: str, markdown: bool = False, fetch_labels: bool = False) -> None:
    """List all dynamic enums in a schema directory with their descriptions.

    Args:
        schema_dir: Path to schema directory
        markdown: If True, output markdown format with links
        fetch_labels: If True, fetch labels from OLS (slower)
    """
    import yaml
    from pathlib import Path

    label_cache: dict[str, str] = {}

    def get_label(curie: str) -> str | None:
        """Get label for a CURIE, with caching."""
        if curie in label_cache:
            return label_cache[curie]

        if not fetch_labels:
            return None

        # Try OLS lookup
        label = fetch_label_from_ols(curie)
        label_cache[curie] = label
        return label

    schema_path = Path(schema_dir)
    for f in sorted(schema_path.rglob("*.yaml")):
        schema = yaml.safe_load(f.read_text())
        if schema and "enums" in schema:
            # Extract prefix map from schema
            prefix_map = schema.get("prefixes", {})

            for name, defn in schema["enums"].items():
                if "reachable_from" in defn:
                    # Build label lookup for source nodes
                    label_lookup = {}
                    if fetch_labels:
                        for node in defn.get("reachable_from", {}).get("source_nodes", []):
                            if label := get_label(node):
                                label_lookup[node] = label

                    desc = describe_enum_query(defn, label_lookup, prefix_map)
                    prefixes = ",".join(sorted(desc.prefixes)) if desc else ""

                    if markdown:
                        query = desc.markdown if desc else ""
                        print(f"### {name}")
                        print(f"**File:** `{f.relative_to(schema_path)}`")
                        print(f"**Prefixes:** `{prefixes}`")
                        print(f"**Query:** {query}")
                        print()
                    else:
                        query = desc.text if desc else ""
                        print(f"{f.relative_to(schema_path)}: {name}")
                        print(f"  prefixes: [{prefixes}]")
                        print(f"  query: {query}")


def fetch_label_from_ols(curie: str) -> str | None:
    """Fetch a label from OLS for a CURIE.

    Returns None if lookup fails.

    >>> fetch_label_from_ols("CL:0000000")  # doctest: +SKIP
    'cell'
    """
    import urllib.request
    import urllib.parse
    import json

    uri = curie_to_uri(curie)
    if not uri:
        return None

    # Extract ontology from prefix for OLS4 API
    prefix = extract_prefix(curie)
    if not prefix:
        return None

    ontology = prefix.lower()
    encoded_uri = urllib.parse.quote(urllib.parse.quote(uri, safe=""), safe="")
    url = f"https://www.ebi.ac.uk/ols4/api/ontologies/{ontology}/terms/{encoded_uri}"

    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            data = json.loads(response.read().decode())
            return data.get("label")
    except Exception:
        pass

    return None


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Describe dynamic enum queries")
    parser.add_argument("--list", action="store_true", help="List all dynamic enums")
    parser.add_argument("--markdown", "-m", action="store_true", help="Output in markdown format")
    parser.add_argument("--labels", "-l", action="store_true", help="Fetch labels from OLS (slower)")
    parser.add_argument("--test", action="store_true", help="Run doctests")
    parser.add_argument("schema_dir", nargs="?", default="src/valuesets/schema", help="Schema directory")

    args = parser.parse_args()

    if args.test:
        import doctest
        doctest.testmod()
    elif args.list:
        list_dynamic_enums(args.schema_dir, markdown=args.markdown, fetch_labels=args.labels)
    else:
        parser.print_help()
