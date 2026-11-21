"""
Consistency tests for the computational modeling value sets.

The computational modeling enums keep each descriptive axis in its own enum
(state variable type, time, stochasticity, space, entity resolution, ...).
Two places record values of one enum inside another as "|"-separated
annotation strings, which no schema validator checks:

* ``ModelingFramework`` names common combinations of the formalism axes and
  records each combination in annotations (``paradigm``,
  ``state_variable_type``, ...).
* ``CommonSimulationAlgorithm`` records the frameworks an algorithm applies to
  (``framework``), and ``ModelingSoftware`` records each tool's ``roles``,
  ``frameworks`` and ``formats``.

These tests check that every such annotation value is a permissible value of
the enum it refers to, so renaming or removing a value cannot silently leave a
dangling reference.

They read the schema YAML directly rather than the generated
``valuesets.enums.computational_modeling`` modules, which do not exist until
the derived-file regeneration workflow runs on main.
"""

from pathlib import Path

import pytest
import yaml

SCHEMA_DIR = (
    Path(__file__).parent.parent / "src" / "valuesets" / "schema" / "computational_modeling"
)
FILES = [
    "model_formalism.yaml",
    "model_context.yaml",
    "model_formats.yaml",
    "simulation_methods.yaml",
    "modeling_software.yaml",
]


def _load_enums():
    enums = {}
    for name in FILES:
        doc = yaml.safe_load((SCHEMA_DIR / name).read_text())
        for enum_name, enum_def in (doc.get("enums") or {}).items():
            assert enum_name not in enums, f"duplicate enum {enum_name}"
            enums[enum_name] = enum_def
    return enums


ENUMS = _load_enums()


def _values(enum_name):
    return set((ENUMS[enum_name].get("permissible_values") or {}).keys())


def _annotation_refs(enum_name, annotation_to_enum):
    """Yield (pv, annotation, referenced value, target enum) for every reference."""
    for pv, pv_def in ENUMS[enum_name]["permissible_values"].items():
        annotations = (pv_def or {}).get("annotations") or {}
        for annotation, target in annotation_to_enum.items():
            if annotation not in annotations:
                continue
            for value in str(annotations[annotation]).split("|"):
                yield pv, annotation, value.strip(), target


FRAMEWORK_AXES = {
    "paradigm": "ModelingParadigm",
    "state_variable_type": "ModelStateVariableType",
    "time_representation": "ModelTimeRepresentation",
    "stochasticity": "ModelStochasticity",
    "spatial_representation": "ModelSpatialRepresentation",
    "entity_resolution": "ModelEntityResolution",
}

CHECKS = [
    ("ModelingFramework", FRAMEWORK_AXES),
    ("CommonSimulationAlgorithm", {"framework": "ModelingFramework"}),
    (
        "ModelingSoftware",
        {
            "roles": "ModelingSoftwareRole",
            "frameworks": "ModelingFramework",
            "formats": "ModelEncodingFormat",
        },
    ),
]


@pytest.mark.parametrize(
    "enum_name,annotation_to_enum", CHECKS, ids=[c[0] for c in CHECKS]
)
def test_annotation_values_are_permissible_values(enum_name, annotation_to_enum):
    bad = [
        f"{pv}.{annotation}={value} (not in {target})"
        for pv, annotation, value, target in _annotation_refs(enum_name, annotation_to_enum)
        if value not in _values(target)
    ]
    assert not bad, "dangling annotation references:\n" + "\n".join(bad)


def test_checks_can_fail():
    """Guard against a vacuous pass: the checks above must see real references."""
    for enum_name, annotation_to_enum in CHECKS:
        refs = list(_annotation_refs(enum_name, annotation_to_enum))
        assert refs, f"no annotation references found in {enum_name}"


def test_mechanistic_dynamical_frameworks_declare_every_axis():
    """A named mechanistic framework must say where it sits on every formalism axis."""
    missing = []
    for pv, pv_def in ENUMS["ModelingFramework"]["permissible_values"].items():
        annotations = (pv_def or {}).get("annotations") or {}
        if not str(annotations.get("paradigm", "")).startswith("MECHANISTIC"):
            continue
        for axis in FRAMEWORK_AXES:
            if axis not in annotations:
                missing.append(f"{pv} lacks {axis}")
    assert not missing, "\n".join(missing)


def test_all_files_imported_by_main_schema():
    main = yaml.safe_load(
        (SCHEMA_DIR.parent / "valuesets.yaml").read_text()
    )
    imports = set(main.get("imports") or [])
    for name in FILES:
        assert f"computational_modeling/{name.removesuffix('.yaml')}" in imports
