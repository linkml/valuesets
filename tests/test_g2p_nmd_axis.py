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

The dropped-mixin behaviour was measured on linkml 1.9.5 / linkml-runtime 1.9.5,
on both of the repo's OWL paths: ``gen-owl`` invoked bare, as ``just gen-owl``
does to produce the shipped ``project/owl/valuesets.owl.ttl``, and ``gen-owl``
invoked with ``config.yaml``'s ``generator_args.owl``, as ``gen-project`` does.
The latter includes ``mixins_as_expressions: true``, which despite the name does
not surface permissible-value mixins -- it governs class mixins. If a later
version emits permissible-value mixins as ``rdfs:subClassOf``, the ``nmd_status``
annotation becomes redundant and both it and these tests can go -- re-check
``gen-owl`` output before assuming the workaround is still needed.

These tests read the schema YAML directly rather than the generated
``valuesets.enums.clinical.gene2phenotype`` module, which does not exist until
the derived-file regeneration workflow runs on main.

What this suite is and is not for
---------------------------------
Structural references are already enforced by code generation: a permissible
value whose ``is_a`` or ``mixins`` names a key that does not exist fails
``just test`` at ``_test-schema``, because ``gen-project`` builds OWL and OWL
generation resolves both (``ValueError: Cannot find permissible value``). That
holds for ``mixins`` even though ``gen-owl`` then discards them -- it resolves
first, drops after. So the mixin check below is a faster, more specific echo of
an existing guarantee rather than the only thing standing between a typo and a
broken build.

That guarantee was measured on linkml 1.9.5 and holds only while ``owl`` is
absent from ``excludes`` in ``config.yaml``. Adding it there would stop
``_test-schema`` resolving permissible-value ``is_a``/``mixins`` at all, and
nothing would report that this paragraph had become false -- so re-check both if
either changes.

Annotation values are the genuinely unguarded surface. They are free-form
strings, so a misspelled ``nmd_status``/``variant_type_group``/
``parent_mechanism``, or an omitted ``nmd_status``, passes ``_test-schema``
with exit 0 and produces no diagnostic anywhere. That is what these tests exist
for.

The guard is not total. ``test_nmd_named_types_carry_the_axis`` keys off the
name suffix, which is exact for the current eight values but would not see an
NMD-qualified type named the other way round (``NMD_TRIGGERING_STOP_LOST``)
that also omitted both encodings. A looser "key contains NMD" rule was
considered and rejected: it would false-positive on a legitimate
``NMD_TRANSCRIPT_VARIANT`` (SO:0001621), a plausible future addition.
"""

from pathlib import Path

import pytest
import yaml

SCHEMA_PATH = (
    Path(__file__).parent.parent
    / "src" / "valuesets" / "schema" / "clinical" / "gene2phenotype.yaml"
)

NMD_QUALIFIERS = {"NMD_TRIGGERING", "NMD_ESCAPING"}

# Number of NMD-qualified variant types currently in the schema. This is a
# tripwire against the annotations being dropped wholesale, not a claim that the
# count is fixed -- if G2P or SO add a type, update it deliberately.
EXPECTED_NMD_QUALIFIED = 8

# Annotations that name a permissible value of another enum. Each entry is
# (annotation key, enum whose keys it must resolve against).
PV_REFERENCE_ANNOTATIONS = [
    ("nmd_status", "G2PVariantType"),
    ("variant_type_group", "G2PVariantTypeGroup"),
    ("parent_mechanism", "G2PMolecularMechanism"),
]


@pytest.fixture(scope="module")
def schema():
    with open(SCHEMA_PATH) as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def variant_types(schema):
    """
    Permissible values of G2PVariantType, keyed by permissible value name.

    Bodies are normalised to a dict so that a value written without one
    (``SOME_KEY:``, which YAML parses as None) does not raise AttributeError in
    the helpers below.
    """
    return {
        name: pv or {}
        for name, pv in schema["enums"]["G2PVariantType"]["permissible_values"].items()
    }


def _annotation(pv, key):
    """
    Read an annotation value.

    Tolerates the three shapes LinkML accepts: a compact ``key: value`` mapping,
    a ``key: {tag, value}`` mapping, and a list of ``{tag, value}`` dicts.
    """
    annotations = pv.get("annotations") or {}
    if isinstance(annotations, list):
        for item in annotations:
            if isinstance(item, dict) and item.get("tag") == key:
                return item.get("value")
        return None
    raw = annotations.get(key)
    if isinstance(raw, dict):
        return raw.get("value")
    return raw


def _nmd_mixins(pv):
    return NMD_QUALIFIERS.intersection(pv.get("mixins") or [])


def _nmd_status(pv):
    return _annotation(pv, "nmd_status")


def test_mixins_resolve_to_permissible_values(variant_types):
    """
    Every mixin must name a real permissible value.

    Without this, a misspelled qualifier (NMD_ESCAPPING) is skipped by every
    other test in this file rather than flagged. Code generation also rejects
    it, so this is not the sole defence. Its value is under a direct ``pytest``
    run (editor, ``uv run pytest``), where it names the offending key; under
    ``just test`` the reader sees the generator traceback instead, because
    ``_test-schema`` runs before pytest and aborts first.
    """
    for name, pv in variant_types.items():
        for mixin in pv.get("mixins") or []:
            assert mixin in variant_types, (
                f"{name} has mixin {mixin!r}, which is not a permissible value "
                f"of G2PVariantType"
            )


def test_nmd_named_types_carry_the_axis(variant_types):
    """
    A value named for an NMD qualifier must actually carry that axis.

    Catches a new NMD-qualified type that was added without the mixin, the
    annotation, or both.
    """
    for name, pv in variant_types.items():
        for qualifier in NMD_QUALIFIERS:
            if name == qualifier or not name.endswith(f"_{qualifier}"):
                continue
            assert qualifier in (pv.get("mixins") or []), (
                f"{name} is named for {qualifier} but does not carry it as a mixin"
            )
            assert _nmd_status(pv) == qualifier, (
                f"{name} is named for {qualifier} but its nmd_status is "
                f"{_nmd_status(pv)!r}; the OWL output would lose the NMD axis"
            )


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


@pytest.mark.parametrize("annotation_key,target_enum", PV_REFERENCE_ANNOTATIONS)
def test_cross_reference_annotations_resolve(schema, annotation_key, target_enum):
    """
    Annotations naming a permissible value must resolve in their target enum.

    These annotations use permissible value keys rather than display strings so
    they are machine-resolvable; a typo would otherwise resolve to nothing with
    nothing complaining.
    """
    targets = schema["enums"][target_enum]["permissible_values"]
    checked = 0
    for enum_name, enum_def in schema["enums"].items():
        for pv_name, pv in ((enum_def or {}).get("permissible_values") or {}).items():
            value = _annotation(pv or {}, annotation_key)
            if value is None:
                continue
            checked += 1
            assert value in targets, (
                f"{enum_name}.{pv_name} has {annotation_key}={value!r}, which is "
                f"not a permissible value of {target_enum}"
            )
    assert checked, f"no {annotation_key} annotations found; has the convention changed?"


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


def test_nmd_axis_is_not_dropped_wholesale(variant_types):
    """
    Tripwire for the annotations being deleted en masse, which the pairwise
    tests cannot see (they skip values carrying neither encoding).
    """
    annotated = [
        name for name, pv in variant_types.items() if _nmd_status(pv) is not None
    ]
    assert len(annotated) == EXPECTED_NMD_QUALIFIED, (
        f"expected {EXPECTED_NMD_QUALIFIED} NMD-qualified types, found "
        f"{len(annotated)}. If G2P or SO legitimately added or removed one, "
        f"update EXPECTED_NMD_QUALIFIED deliberately; otherwise the nmd_status "
        f"annotations have gone missing and the OWL output has lost the axis."
    )


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
