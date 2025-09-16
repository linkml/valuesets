#!/usr/bin/env python
"""
Test the enum validator with some known mappings.
"""

from pathlib import Path
from valuesets.validators import EnumEvaluator, ValidationResult

# Create a mock OAK adapter for testing
class MockOakAdapter:
    """Mock OAK adapter that returns known labels for testing."""

    def __init__(self):
        # Add some known mappings we can test
        self.labels = {
            # Correct blood type mappings
            "SNOMED:278149003": "Blood group A Rh(D) positive",
            "SNOMED:278152006": "Blood group A Rh(D) negative",
            "SNOMED:278150003": "Blood group B Rh(D) positive",
            "SNOMED:278153001": "Blood group B Rh(D) negative",
            "SNOMED:278151004": "Blood group AB Rh(D) positive",
            "SNOMED:278154007": "Blood group AB Rh(D) negative",
            "SNOMED:278147001": "Blood group O Rh(D) positive",
            "SNOMED:278148006": "Blood group O Rh(D) negative",

            # Anatomical systems
            "UBERON:0004535": "cardiovascular system",
            "UBERON:0001004": "respiratory system",
            "UBERON:0001016": "nervous system",

            # Some that might not match exactly
            "OBI:0001046": "bioreactor",  # Too broad for "stirred tank reactor"
            "NCIT:C112927": "Production",  # Might not match "PRODUCTION_SCALE"
        }

    def label(self, curie: str) -> str:
        """Return the label for a CURIE."""
        return self.labels.get(curie)


def test_blood_types():
    """Test validation of blood type mappings."""
    print("Testing blood type enum validation...")

    # Create evaluator with default configuration
    # Note: The current EnumEvaluator doesn't support injecting custom adapters
    # It will use the default OAK adapter configuration
    evaluator = EnumEvaluator()

    # Validate the clinical schema
    schema_path = Path("src/valuesets/schema/medical/clinical.yaml")
    if not schema_path.exists():
        print(f"Schema not found: {schema_path}")
        return

    result = evaluator.validate_schema(schema_path)

    # Check specific issues
    print(f"\nChecked {result.total_values_checked} values")
    print(f"Found {len(result.issues)} issues")

    # Group issues by severity
    by_severity = {}
    for issue in result.issues:
        by_severity.setdefault(issue.severity, []).append(issue)

    for severity, issues in by_severity.items():
        print(f"\n{severity}: {len(issues)} issues")
        for issue in issues[:5]:  # Show first 5
            print(f"  - {issue.enum_name}.{issue.value_name}: {issue.message}")
            if issue.expected_label:
                print(f"    Expected: '{issue.expected_label}'")
                print(f"    Actual: '{issue.actual_label}'")


def test_bioprocessing():
    """Test validation of bioprocessing mappings."""
    print("\n" + "="*50)
    print("Testing bioprocessing enum validation...")

    # Create evaluator with default configuration
    # Note: The current EnumEvaluator doesn't support injecting custom adapters
    # It will use the default OAK adapter configuration
    evaluator = EnumEvaluator()

    # Validate the bioprocessing schema
    schema_path = Path("src/valuesets/schema/bioprocessing/scale_up.yaml")
    if not schema_path.exists():
        print(f"Schema not found: {schema_path}")
        return

    result = evaluator.validate_schema(schema_path)

    print(f"\nChecked {result.total_values_checked} values")
    print(f"Found {len(result.issues)} issues")

    # Show warnings
    warnings = [i for i in result.issues if i.severity == "WARNING"]
    if warnings:
        print(f"\nWarnings found:")
        for issue in warnings[:10]:
            print(f"  - {issue.enum_name}.{issue.value_name}: {issue.message}")
            if issue.meaning:
                print(f"    Mapping: {issue.meaning}")


if __name__ == "__main__":
    test_blood_types()
    test_bioprocessing()
