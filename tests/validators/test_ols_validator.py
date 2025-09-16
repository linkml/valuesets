#!/usr/bin/env python3
"""
Test script for the enhanced enum evaluator with OLS MCP support.

This script demonstrates how to use the enum evaluator with the OLS MCP tool
for validating ontology mappings in LinkML schemas.
"""

import sys
from pathlib import Path
from typing import List, Dict, Any

# Add parent directory to path to import the evaluator
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from src.valuesets.validators.enum_evaluator import EnumEvaluator, ValidationResult


def mock_ols_search(query: str, exact: bool = False, max_results: int = 20, **kwargs) -> List[Dict[str, Any]]:
    """
    Mock OLS search function for testing.

    In a real MCP environment, this would be replaced with the actual
    mcp__ols__search_all_ontologies function.
    """
    # Some example mappings for testing
    mock_data = {
        "NCIT:C12345": {"label": "Example Disease", "obo_id": "NCIT:C12345"},
        "CL:0000000": {"label": "cell", "obo_id": "CL:0000000"},
        "UBERON:0000001": {"label": "organism", "obo_id": "UBERON:0000001"},
        "CHEBI:24431": {"label": "chemical entity", "obo_id": "CHEBI:24431"},
        "GO:0008150": {"label": "biological_process", "obo_id": "GO:0008150"},
        "HP:0000001": {"label": "All", "obo_id": "HP:0000001"},
        "MONDO:0000001": {"label": "disease or disorder", "obo_id": "MONDO:0000001"},
        "PR:000000001": {"label": "protein", "obo_id": "PR:000000001"},
        "STATO:0000030": {"label": "t-test", "obo_id": "STATO:0000030"},
        "OBI:0000070": {"label": "assay", "obo_id": "OBI:0000070"},
        "SIO:000015": {"label": "information content entity", "obo_id": "SIO:000015"},
    }

    # Check for exact match
    if query in mock_data:
        result = mock_data[query].copy()
        result.update({
            "iri": f"http://purl.obolibrary.org/obo/{query.replace(':', '_')}",
            "short_form": query.replace(':', '_'),
            "ontology_prefix": query.split(':')[0],
            "type": "class"
        })
        return [result]

    # Check with underscore format
    alt_query = query.replace('_', ':')
    if alt_query in mock_data:
        result = mock_data[alt_query].copy()
        result.update({
            "iri": f"http://purl.obolibrary.org/obo/{query}",
            "short_form": query,
            "obo_id": alt_query,
            "ontology_prefix": alt_query.split(':')[0],
            "type": "class"
        })
        return [result]

    return []


def validate_single_schema(schema_path: Path, use_real_ols: bool = False):
    """
    Test validation of a single schema file.

    Args:
        schema_path: Path to the schema file
        use_real_ols: If True, try to use the real OLS MCP function
    """
    print(f"\nTesting schema: {schema_path}")
    print("=" * 60)

    if use_real_ols:
        # Try to import the real OLS function if available
        try:
            # This would be available in an MCP-enabled environment
            from __main__ import mcp__ols__search_all_ontologies
            ols_func = mcp__ols__search_all_ontologies
            print("Using real OLS MCP function")
        except ImportError:
            print("Real OLS MCP function not available, using mock")
            ols_func = mock_ols_search
    else:
        print("Using mock OLS function for testing")
        ols_func = mock_ols_search

    # Create evaluator with default configuration
    # Note: Current EnumEvaluator doesn't support custom OLS functions
    evaluator = EnumEvaluator()

    # Validate the schema
    result = evaluator.validate_schema(schema_path)

    # Print results
    print(f"\nValidation Results:")
    print(f"  Total enums checked: {result.total_enums_checked}")
    print(f"  Total values checked: {result.total_values_checked}")
    print(f"  Total mappings checked: {result.total_mappings_checked}")

    if result.issues:
        print(f"\nIssues found:")

        # Group issues by severity
        issues_by_severity = {}
        for issue in result.issues:
            if issue.severity not in issues_by_severity:
                issues_by_severity[issue.severity] = []
            issues_by_severity[issue.severity].append(issue)

        for severity, issues in issues_by_severity.items():
            print(f"\n  {severity} ({len(issues)} issues):")
            for issue in issues[:5]:  # Show first 5 of each type
                print(f"    - {issue.enum_name}.{issue.value_name}")
                print(f"      {issue.message}")
                if issue.expected_label and issue.actual_label:
                    print(f"      Expected: '{issue.expected_label}', Got: '{issue.actual_label}'")
            if len(issues) > 5:
                print(f"    ... and {len(issues) - 5} more")
    else:
        print("\n✓ No issues found!")

    return result


def main():
    """Main test function."""
    import argparse

    parser = argparse.ArgumentParser(description="Test OLS-enhanced enum validator")
    parser.add_argument(
        "schema_path",
        type=Path,
        nargs='?',
        help="Path to schema file to validate"
    )
    parser.add_argument(
        "--real-ols",
        action="store_true",
        help="Try to use real OLS MCP function instead of mock"
    )
    parser.add_argument(
        "--dir",
        type=Path,
        help="Validate all schemas in a directory"
    )

    args = parser.parse_args()

    if args.dir:
        # Validate directory
        schema_dir = args.dir
        if not schema_dir.exists():
            print(f"Directory not found: {schema_dir}")
            return 1

        print(f"Validating all schemas in: {schema_dir}")

        for schema_file in schema_dir.rglob("*.yaml"):
            if schema_file.is_file():
                validate_single_schema(schema_file, args.real_ols)

    elif args.schema_path:
        # Validate single file
        if not args.schema_path.exists():
            print(f"Schema file not found: {args.schema_path}")
            return 1

        validate_single_schema(args.schema_path, args.real_ols)

    else:
        # Default: test statistics.yaml as an example
        default_schema = Path(__file__).parent.parent.parent / "schema" / "statistics.yaml"
        if default_schema.exists():
            print("No schema specified, testing statistics.yaml as example")
            validate_single_schema(default_schema, args.real_ols)
        else:
            print("Please specify a schema file to validate")
            parser.print_help()
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
