"""
Tests for the enum evaluator module.
"""

import pytest
from pathlib import Path
from unittest.mock import Mock, MagicMock

from valuesets.validators.enum_evaluator import (
    EnumEvaluator,
    ValidationConfig,
    ValidationIssue,
    ValidationResult
)


def test_validation_config():
    """Test ValidationConfig model."""
    # Default config
    config = ValidationConfig()
    assert config.oak_adapter_string == "sqlite:obo:"
    assert config.cache_labels is True
    assert config.strict_mode is False

    # Custom config
    config = ValidationConfig(
        oak_adapter_string="ols:",
        strict_mode=True
    )
    assert config.oak_adapter_string == "ols:"
    assert config.strict_mode is True


def test_validation_issue():
    """Test ValidationIssue model."""
    issue = ValidationIssue(
        enum_name="TestEnum",
        value_name="TEST_VALUE",
        severity="WARNING",
        message="Test message",
        meaning="NCIT:C12345"
    )
    assert issue.enum_name == "TestEnum"
    assert issue.severity == "WARNING"
    assert issue.meaning == "NCIT:C12345"

    # Test validation
    with pytest.raises(ValueError):
        ValidationIssue(
            enum_name="TestEnum",
            value_name="TEST_VALUE",
            severity="INVALID",  # Invalid severity
            message="Test message"
        )


def test_validation_result():
    """Test ValidationResult model."""
    result = ValidationResult(schema_path=Path("test.yaml"))
    assert result.schema_path == Path("test.yaml")
    assert result.has_errors() is False
    assert len(result.issues) == 0

    # Add an error
    result.issues.append(
        ValidationIssue(
            enum_name="TestEnum",
            value_name="TEST_VALUE",
            severity="ERROR",
            message="Test error"
        )
    )
    assert result.has_errors() is True


def test_curie_handling():
    """Test CURIE handling in label lookups."""
    evaluator = EnumEvaluator()

    # Test that CURIEs are passed correctly to adapters
    mock_adapter = Mock()
    mock_adapter.label = Mock(return_value="Test Label")
    evaluator._per_prefix_adapters['ncit'] = mock_adapter

    # Test with colon format
    label = evaluator.get_ontology_label("NCIT:C12345")
    # The CURIE should be passed as-is to the adapter
    mock_adapter.label.assert_called_with("NCIT:C12345")


def test_normalize_string():
    """Test string normalization."""
    evaluator = EnumEvaluator()

    assert evaluator.normalize_string("Blood Type A+") == "blood type a"
    assert evaluator.normalize_string("PRODUCTION_SCALE") == "production scale"
    assert evaluator.normalize_string("Blood group A Rh(D) positive") == "blood group a rh d positive"
    assert evaluator.normalize_string("") == ""
    assert evaluator.normalize_string(None) == ""


def test_extract_aliases():
    """Test alias extraction from permissible values."""
    from linkml_runtime.linkml_model import PermissibleValue

    evaluator = EnumEvaluator()

    # Basic permissible value
    pv = PermissibleValue(text="TEST_VALUE", description="Test value")
    aliases = evaluator.extract_aliases(pv, "TEST_VALUE")
    assert "TEST_VALUE" in aliases
    assert len(aliases) == 1

    # With title
    pv = PermissibleValue(text="TEST_VALUE", description="Test value", title="Test Title")
    aliases = evaluator.extract_aliases(pv, "TEST_VALUE")
    assert "TEST_VALUE" in aliases
    assert "Test Title" in aliases

    # With aliases
    pv = PermissibleValue(
        text="TEST_VALUE",
        description="Test value",
        aliases=["alias1", "alias2"]
    )
    aliases = evaluator.extract_aliases(pv, "TEST_VALUE")
    assert "TEST_VALUE" in aliases
    assert "alias1" in aliases
    assert "alias2" in aliases


def test_oak_label_lookup():
    """Test OAK label lookup with mock."""
    # Create mock adapter that returns our test label
    mock_adapter = Mock()
    mock_adapter.label = Mock(return_value="Blood group A Rh(D) positive")

    # Create evaluator with a dummy config to avoid creating real adapters
    config = ValidationConfig(oak_adapter_string="dummy:")
    evaluator = EnumEvaluator(config=config)

    # The dummy adapter creation should fail, so _default should be None or missing
    assert '_default' not in evaluator._per_prefix_adapters or evaluator._per_prefix_adapters['_default'] is None

    # Inject mock adapter - this simulates having a working adapter connection
    evaluator._per_prefix_adapters['_default'] = mock_adapter

    # Verify injection worked
    assert evaluator._per_prefix_adapters['_default'] is mock_adapter

    # Test successful lookup
    label = evaluator.get_ontology_label("TESTONT:278149003")
    assert label == "Blood group A Rh(D) positive"
    mock_adapter.label.assert_called_with("TESTONT:278149003")

    # Test with no results (adapter returns None)
    mock_adapter.label.return_value = None
    # Clear the cache first to ensure we hit the adapter
    if evaluator._label_cache is not None:
        evaluator._label_cache.clear()

    label = evaluator.get_ontology_label("TESTONT:123")
    assert label is None
    mock_adapter.label.assert_called_with("TESTONT:123")


def test_evaluator_creation():
    """Test evaluator creation with different configurations."""
    # Default config
    evaluator = EnumEvaluator()
    assert evaluator.config.oak_adapter_string == "sqlite:obo:"

    # Custom config
    config = ValidationConfig(
        oak_adapter_string="ols:",
        strict_mode=True
    )
    evaluator = EnumEvaluator(config)
    assert evaluator.config.oak_adapter_string == "ols:"
    assert evaluator.config.strict_mode is True


def test_cache_behavior():
    """Test label caching."""
    config = ValidationConfig(
        oak_adapter_string="ols:",
        cache_labels=True
    )
    evaluator = EnumEvaluator(config=config)

    # Mock adapter
    mock_adapter = Mock()
    mock_adapter.label = Mock(return_value="Test Label")
    evaluator._per_prefix_adapters['_default'] = mock_adapter

    # First call should use adapter
    label1 = evaluator.get_ontology_label("TEST:123")
    assert mock_adapter.label.call_count == 1

    # Second call should use cache
    label2 = evaluator.get_ontology_label("TEST:123")
    assert mock_adapter.label.call_count == 1  # Still 1, not 2
    assert label1 == label2

    # Test with caching disabled
    config.cache_labels = False
    evaluator = EnumEvaluator(config=config)
    evaluator._per_prefix_adapters['_default'] = mock_adapter
    mock_adapter.label.reset_mock()

    label1 = evaluator.get_ontology_label("TEST:123")
    label2 = evaluator.get_ontology_label("TEST:123")
    assert mock_adapter.label.call_count == 2  # Called twice


def _evaluator_with_mock(tmp_path, labels):
    """Evaluator whose NCIT adapter is a mock returning labels from the given dict."""
    config = ValidationConfig(oak_adapter_string="dummy:", cache_dir=tmp_path / "cache")
    evaluator = EnumEvaluator(config=config)
    mock_adapter = Mock()
    mock_adapter.label = Mock(side_effect=lambda curie: labels.get(curie))
    # NCIT is a configured (strict) prefix in oak_config.yaml; inject before any lookup
    evaluator._per_prefix_adapters['ncit'] = mock_adapter
    evaluator._prefix_caches['ncit'] = {}
    evaluator._per_prefix_adapters['_default'] = mock_adapter
    return evaluator


def test_validate_reachable_from_source_nodes(tmp_path):
    """Dynamic enums have their source nodes resolved even with no permissible values."""
    from linkml_runtime.linkml_model.meta import EnumDefinition, ReachabilityQuery

    evaluator = _evaluator_with_mock(tmp_path, {"NCIT:C17204": "Computed Tomography"})

    good = EnumDefinition(
        name="GoodDynamic",
        reachable_from=ReachabilityQuery(source_nodes=["NCIT:C17204"]),
    )
    assert evaluator.validate_enum(good, "GoodDynamic") == []

    bad = EnumDefinition(
        name="BadDynamic",
        reachable_from=ReachabilityQuery(source_nodes=["NCIT:C999999999"]),
    )
    issues = evaluator.validate_enum(bad, "BadDynamic")
    assert len(issues) == 1
    assert issues[0].severity == "ERROR"
    assert issues[0].value_name == "<reachable_from>"
    assert issues[0].meaning == "NCIT:C999999999"


def test_validate_mapping_slots(tmp_path):
    """exact/close/broad mappings must resolve; a resolvable one needs no label match."""
    from linkml_runtime.linkml_model import EnumDefinition, PermissibleValue

    evaluator = _evaluator_with_mock(tmp_path, {
        "NCIT:C17204": "Computed Tomography",
        "NCIT:C38101": "X-Ray Imaging",
    })

    enum_def = EnumDefinition(
        name="Modality",
        permissible_values={
            "CT": PermissibleValue(
                text="CT",
                title="Computed Tomography",
                meaning="NCIT:C17204",
                close_mappings=["NCIT:C38101"],  # label differs from title: allowed for mappings
                exact_mappings=["NCIT:C999999999"],  # does not resolve
            ),
        },
    )
    issues = evaluator.validate_enum(enum_def, "Modality")
    assert len(issues) == 1
    assert issues[0].severity == "ERROR"
    assert issues[0].meaning == "NCIT:C999999999"
    assert "exact_mappings" in issues[0].message


def test_unconfigured_prefix_mapping_is_info(tmp_path):
    """Unresolvable mappings with an unconfigured prefix are INFO, not ERROR."""
    from linkml_runtime.linkml_model import EnumDefinition, PermissibleValue

    evaluator = _evaluator_with_mock(tmp_path, {})
    enum_def = EnumDefinition(
        name="Tools",
        permissible_values={
            "X": PermissibleValue(text="X", exact_mappings=["TESTONT:1"]),
        },
    )
    issues = evaluator.validate_enum(enum_def, "Tools")
    assert len(issues) == 1
    assert issues[0].severity == "INFO"
