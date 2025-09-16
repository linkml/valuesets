#!/usr/bin/env python3
"""
Direct validation script using OLS MCP for ontology term validation.

This script is designed to work with the actual MCP OLS tool when available.
"""

import sys
from pathlib import Path
from typing import List, Dict, Any, Optional

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from src.valuesets.validators.enum_evaluator import (
    EnumEvaluator,
    ValidationResult,
    ValidationIssue
)


def validate_schema_with_ols(
    schema_path: Path,
    ols_search_func,
    verbose: bool = False
) -> ValidationResult:
    """
    Validate a schema using the OLS MCP tool.

    Args:
        schema_path: Path to the LinkML schema file
        ols_search_func: The mcp__ols__search_all_ontologies function
        verbose: If True, print detailed progress

    Returns:
        ValidationResult with all issues found
    """
    if verbose:
        print(f"Validating {schema_path.name} with OLS...")

    # Create evaluator with OLS function
    evaluator = EnumEvaluator(ols_search_func=ols_search_func)

    # Run validation
    result = evaluator.validate_schema(schema_path)

    if verbose and result.total_mappings_checked > 0:
        print(f"  Checked {result.total_mappings_checked} ontology mappings")

    return result


def validate_and_report(
    schema_path: Path,
    ols_search_func,
    show_all: bool = False
) -> bool:
    """
    Validate a schema and print a detailed report.

    Args:
        schema_path: Path to the schema file
        ols_search_func: The OLS search function
        show_all: If True, show all issues (not just first 10)

    Returns:
        True if validation passed (no errors), False otherwise
    """
    print(f"\n{'='*70}")
    print(f"Validating: {schema_path.name}")
    print(f"{'='*70}")

    result = validate_schema_with_ols(schema_path, ols_search_func, verbose=True)

    # Print summary stats
    print(f"\nSummary:")
    print(f"  Enums processed: {result.total_enums_checked}")
    print(f"  Values checked: {result.total_values_checked}")
    print(f"  Mappings validated: {result.total_mappings_checked}")

    # Categorize issues
    errors = [i for i in result.issues if i.severity == "ERROR"]
    warnings = [i for i in result.issues if i.severity == "WARNING"]
    info = [i for i in result.issues if i.severity == "INFO"]

    print(f"\nIssues:")
    print(f"  Errors: {len(errors)}")
    print(f"  Warnings: {len(warnings)}")
    print(f"  Info: {len(info)}")

    # Show errors
    if errors:
        print(f"\n{'❌ ERRORS:'}")
        print("-" * 60)
        limit = None if show_all else 10
        for i, issue in enumerate(errors[:limit], 1):
            print(f"{i}. {issue.enum_name}.{issue.value_name}")
            print(f"   Issue: {issue.message}")
            if issue.meaning:
                print(f"   CURIE: {issue.meaning}")
        if not show_all and len(errors) > 10:
            print(f"   ... and {len(errors) - 10} more errors")

    # Show warnings
    if warnings:
        print(f"\n{'⚠️  WARNINGS:'}")
        print("-" * 60)
        limit = None if show_all else 10
        for i, issue in enumerate(warnings[:limit], 1):
            print(f"{i}. {issue.enum_name}.{issue.value_name}")
            print(f"   Issue: {issue.message}")
            if issue.meaning:
                print(f"   CURIE: {issue.meaning}")
            if issue.expected_label and issue.actual_label:
                print(f"   Expected: '{issue.expected_label}'")
                print(f"   Actual: '{issue.actual_label}'")
        if not show_all and len(warnings) > 10:
            print(f"   ... and {len(warnings) - 10} more warnings")

    # Show info messages (only if verbose)
    if info and show_all:
        print(f"\n{'ℹ️  INFO:'}")
        print("-" * 60)
        for i, issue in enumerate(info[:5], 1):
            print(f"{i}. {issue.enum_name}.{issue.value_name}: {issue.message}")
        if len(info) > 5:
            print(f"   ... and {len(info) - 5} more info messages")

    # Final status
    if not errors and not warnings:
        print(f"\n✅ Validation PASSED - All ontology mappings are correct!")
        return True
    elif not errors:
        print(f"\n⚠️  Validation PASSED with warnings")
        return True
    else:
        print(f"\n❌ Validation FAILED - Errors found")
        return False


def run_validation_with_ols_mcp():
    """
    Main function to run validation using the actual OLS MCP tool.

    This function expects to be run in an environment where the
    mcp__ols__search_all_ontologies function is available.
    """
    import argparse

    parser = argparse.ArgumentParser(
        description="Validate LinkML enum ontology mappings using OLS"
    )
    parser.add_argument(
        "path",
        type=Path,
        help="Path to schema file or directory"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Show all issues (not just first 10)"
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Only show summary, not detailed issues"
    )

    args = parser.parse_args()

    # Import the OLS function - this should be available in the MCP environment
    try:
        # In the MCP environment, this function should be available
        from __main__ import mcp__ols__search_all_ontologies as ols_search
        print("✓ OLS MCP tool is available")
    except ImportError:
        print("❌ Error: OLS MCP tool (mcp__ols__search_all_ontologies) is not available")
        print("This script must be run in an MCP-enabled environment")
        return 1

    path = args.path

    if path.is_file():
        # Validate single file
        success = validate_and_report(path, ols_search, show_all=args.all)
        return 0 if success else 1

    elif path.is_dir():
        # Validate all schemas in directory
        schema_files = list(path.rglob("*.yaml"))
        if not schema_files:
            print(f"No YAML files found in {path}")
            return 1

        print(f"Found {len(schema_files)} schema files to validate")

        all_success = True
        total_errors = 0
        total_warnings = 0

        for schema_file in sorted(schema_files):
            result = validate_schema_with_ols(schema_file, ols_search, verbose=not args.quiet)

            errors = sum(1 for i in result.issues if i.severity == "ERROR")
            warnings = sum(1 for i in result.issues if i.severity == "WARNING")

            total_errors += errors
            total_warnings += warnings

            if errors > 0:
                all_success = False
                status = "❌ FAILED"
            elif warnings > 0:
                status = "⚠️  WARNING"
            else:
                status = "✅ OK"

            if not args.quiet:
                print(f"{status} {schema_file.relative_to(path)}: "
                      f"{errors} errors, {warnings} warnings")

        print(f"\n{'='*70}")
        print(f"Overall Summary:")
        print(f"  Files validated: {len(schema_files)}")
        print(f"  Total errors: {total_errors}")
        print(f"  Total warnings: {total_warnings}")

        if all_success:
            print(f"\n✅ All schemas validated successfully!")
            return 0
        else:
            print(f"\n❌ Validation failed for some schemas")
            return 1

    else:
        print(f"Error: {path} is neither a file nor a directory")
        return 1


if __name__ == "__main__":
    sys.exit(run_validation_with_ols_mcp())
