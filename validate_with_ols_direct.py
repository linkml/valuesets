#!/usr/bin/env python3
"""
Direct validation of ontology mappings using OLS MCP tool.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from src.valuesets.validators.enum_evaluator import EnumEvaluator

def validate_clinical_schema():
    """Validate the clinical schema mappings using OLS."""

    # Import the function that will be available in Claude Code
    from mcp__ols__search_all_ontologies import mcp__ols__search_all_ontologies

    # Create evaluator with OLS support
    evaluator = EnumEvaluator(ols_search_func=mcp__ols__search_all_ontologies)

    # Validate the clinical schema that we know has SNOMED mappings
    schema_path = Path("src/valuesets/schema/medical/clinical.yaml")

    print(f"Validating {schema_path}...")
    result = evaluator.validate_schema(schema_path)

    # Show results
    print(f"\nValidation Summary:")
    print(f"  Enums checked: {result.total_enums_checked}")
    print(f"  Values checked: {result.total_values_checked}")
    print(f"  Mappings checked: {result.total_mappings_checked}")

    errors = [i for i in result.issues if i.severity == "ERROR"]
    warnings = [i for i in result.issues if i.severity == "WARNING"]
    info = [i for i in result.issues if i.severity == "INFO"]

    print(f"\nIssues Found:")
    print(f"  Errors: {len(errors)}")
    print(f"  Warnings: {len(warnings)}")
    print(f"  Info: {len(info)}")

    # Show first few warnings as examples
    if warnings:
        print(f"\nExample Warnings:")
        for issue in warnings[:5]:
            print(f"\n- {issue.enum_name}.{issue.value_name}:")
            print(f"  CURIE: {issue.meaning}")
            print(f"  Issue: {issue.message}")
            if issue.expected_label and issue.actual_label:
                print(f"  Expected: '{issue.expected_label}'")
                print(f"  Got: '{issue.actual_label}'")

    return result

if __name__ == "__main__":
    validate_clinical_schema()
