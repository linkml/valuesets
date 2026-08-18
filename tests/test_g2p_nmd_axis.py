"""
Consistency tests for the NMD axis in the G2P variant type enum.

The NMD-qualified variant types have two parents in SO. LinkML allows a single
``is_a``, so the base variant is the ``is_a`` and the NMD qualifier is a mixin.
``gen-owl`` currently emits only the ``is_a`` parent as ``rdfs:subClassOf`` and
drops the mixin, so the NMD axis is mirrored into an ``nmd_status`` annotation
that does survive generation.

That mirroring is the thing these tests protect. The two encodings have to stay
in agreement: if a new NMD-qualified type is added with a mixin but no
annotation, the OWL product silently loses the axis again with nothing else
failing.

These tests read the schema YAML directly rather than the generated
``valuesets.enums.clinical.gene2phenotype`` module, which does not exist until
the derived-file regeneration workflow runs on main.
"""

from pathlib import Path

import pytest
import yaml

SCHEMA_PATH = (
    Path(__file__).parent.parent
    / "src" / "valuesets" / "schema" / "clinical" / "gene2phenotype.yaml"
)

NMD_QUALIFIERS = {"NMD_TRIGGERING", "NMD_ESCAPING"}


@pytest.fixture(scope="module")
def variant_types():
    """Permissible values of G2PVariantType, keyed by permissible value name."""
    with open(SCHEMA_PATH) as f:
        schema = yaml.safe_load(f)
    return schema["enums"]["G2PVariantType"]["permissible_values"]


def _nmd_mixins(pv):
    return NMD_QUALIFIERS.intersection(pv.get("mixins") or [])


def _nmd_status(pv):
    return (pv.get("annotations") or {}).get("nmd_status")


def test_every_nmd_mixin_has_matching_annotation(variant_types):
    """A value carrying an NMD mixin must mirror it in nmd_status."""
    for name, pv in variant_types.items():
        mixins = _nmd_mixins(pv)
        if not mixins:
            continue
        assert len(mixins) == 1, f"{name} carries more than one NMD qualifier: {mixins}"
        assert _nmd_status(pv) == mixins.pop(), (
            f"{name} has an NMD mixin but nmd_status does not match it; "
            f"the OWL output would lose the NMD axis for this value"
        )


def test_every_nmd_annotation_has_matching_mixin(variant_types):
    """The converse: nmd_status must not claim an axis the mixins do not assert."""
    for name, pv in variant_types.items():
        status = _nmd_status(pv)
        if status is None:
            continue
        assert status in NMD_QUALIFIERS, f"{name} has unknown nmd_status {status!r}"
        assert _nmd_mixins(pv) == {status}, (
            f"{name} declares nmd_status {status} but no matching mixin"
        )


def test_nmd_status_values_are_permissible_value_keys(variant_types):
    """nmd_status must reference real permissible values, like variant_type_group does."""
    for name, pv in variant_types.items():
        status = _nmd_status(pv)
        if status is not None:
            assert status in variant_types, (
                f"{name} has nmd_status {status!r}, which is not a "
                f"permissible value of G2PVariantType"
            )


def test_abstract_qualifiers_do_not_annotate_themselves(variant_types):
    """
    NMD_TRIGGERING and NMD_ESCAPING are the axis, not members of it.

    Annotating them would make an nmd_status query and a mixin traversal return
    different sets, which is the drift these tests exist to prevent.
    """
    for name in NMD_QUALIFIERS:
        assert name in variant_types, f"{name} is missing from G2PVariantType"
        assert _nmd_status(variant_types[name]) is None, (
            f"{name} is an NMD qualifier and must not carry nmd_status"
        )


def test_nmd_axis_is_non_empty_and_balanced(variant_types):
    """Guard against the annotations being dropped wholesale."""
    statuses = [
        _nmd_status(pv) for pv in variant_types.values() if _nmd_status(pv) is not None
    ]
    assert len(statuses) == 8, f"expected 8 NMD-qualified types, found {len(statuses)}"
    assert statuses.count("NMD_TRIGGERING") == 4
    assert statuses.count("NMD_ESCAPING") == 4


def test_nmd_qualified_types_keep_a_base_variant_parent(variant_types):
    """The is_a parent is what reaches OWL, so it must be the base variant."""
    for name, pv in variant_types.items():
        if not _nmd_mixins(pv):
            continue
        parent = pv.get("is_a")
        assert parent is not None, f"{name} has an NMD mixin but no is_a parent"
        assert parent in variant_types, f"{name} has unknown is_a parent {parent!r}"
        assert parent not in NMD_QUALIFIERS, (
            f"{name} uses the NMD qualifier as its is_a parent; the base variant "
            f"should be the is_a so that it survives into OWL"
        )
