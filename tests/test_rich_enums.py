"""
Unit tests for rich enum functionality
"""

import pytest
from valuesets.enums.spatial.spatial_qualifiers import AnatomicalSide, AnatomicalPlane
from valuesets.enums.bio.structural_biology import StructuralBiologyTechnique, SampleType
from valuesets.enums.core import PresenceEnum
from valuesets.enums.bio.taxonomy import BiologicalKingdom


class TestRichEnumBasics:
    """Test basic enum functionality"""

    def test_enum_inheritance(self):
        """Test that rich enums are proper Python enums"""
        left = AnatomicalSide.LEFT
        assert isinstance(left, AnatomicalSide)
        assert isinstance(left, str)
        assert str(left) == "AnatomicalSide.LEFT"  # str() returns full enum representation
        assert left.name == "LEFT"
        assert left.value == "LEFT"

    def test_enum_equality(self):
        """Test enum equality comparisons"""
        left = AnatomicalSide.LEFT
        assert left == "LEFT"
        assert left == AnatomicalSide.LEFT
        assert left != AnatomicalSide.RIGHT
        assert left != "RIGHT"

    def test_enum_iteration(self):
        """Test enum iteration"""
        sides = list(AnatomicalSide)
        assert len(sides) == 19  # Expected number of anatomical sides
        assert AnatomicalSide.LEFT in sides
        assert AnatomicalSide.RIGHT in sides

    def test_enum_members(self):
        """Test accessing enum members"""
        assert hasattr(AnatomicalSide, 'LEFT')
        assert hasattr(AnatomicalSide, 'RIGHT')
        assert hasattr(AnatomicalSide, 'ANTERIOR')


class TestMetadataAccess:
    """Test metadata access methods"""

    def test_get_description(self):
        """Test description access"""
        # AnatomicalSide.LEFT doesn't have a description in the metadata
        left = AnatomicalSide.LEFT
        description = left.get_description()
        assert description is None  # No description in metadata

        # Test enum with description
        present = PresenceEnum.PRESENT
        assert present.get_description() == "The entity is present"

    def test_get_meaning(self):
        """Test ontology meaning access"""
        left = AnatomicalSide.LEFT
        meaning = left.get_meaning()
        assert meaning == "BSPO:0000000"

        right = AnatomicalSide.RIGHT
        assert right.get_meaning() == "BSPO:0000007"

    def test_get_annotations(self):
        """Test annotations access"""
        anterior = AnatomicalSide.ANTERIOR
        annotations = anterior.get_annotations()
        assert isinstance(annotations, dict)
        assert "aliases" in annotations
        assert annotations["aliases"] == "front, rostral, cranial (in head region)"

    def test_get_metadata_complete(self):
        """Test complete metadata access"""
        left = AnatomicalSide.LEFT
        metadata = left.get_metadata()

        assert metadata["name"] == "LEFT"
        assert metadata["value"] == "LEFT"
        # No description in metadata for LEFT
        assert "description" not in metadata or metadata.get("description") is None
        assert metadata["meaning"] == "BSPO:0000000"

        # Test with annotations
        anterior = AnatomicalSide.ANTERIOR
        metadata = anterior.get_metadata()
        assert "annotations" in metadata
        assert metadata["annotations"]["aliases"] == "front, rostral, cranial (in head region)"


class TestMeaningLookup:
    """Test ontology meaning lookup functionality"""

    def test_from_meaning_basic(self):
        """Test basic meaning lookup"""
        found = AnatomicalSide.from_meaning("BSPO:0000000")
        assert found == AnatomicalSide.LEFT

        found = AnatomicalSide.from_meaning("BSPO:0000007")
        assert found == AnatomicalSide.RIGHT

    def test_from_meaning_not_found(self):
        """Test meaning lookup with non-existent term"""
        found = AnatomicalSide.from_meaning("FAKE:123456")
        assert found is None

        found = AnatomicalSide.from_meaning("")
        assert found is None

    def test_from_meaning_none_input(self):
        """Test meaning lookup with None input"""
        found = AnatomicalSide.from_meaning(None)
        assert found is None

    def test_from_meaning_different_enums(self):
        """Test meaning lookup across different enum types"""
        # Anatomical planes
        sagittal = AnatomicalPlane.from_meaning("BSPO:0000417")
        assert sagittal == AnatomicalPlane.SAGITTAL

        midsagittal = AnatomicalPlane.from_meaning("BSPO:0000009")
        assert midsagittal == AnatomicalPlane.MIDSAGITTAL

        # Structural biology
        cryo_em = StructuralBiologyTechnique.from_meaning("CHMO:0002413")  # Correct CURIE
        assert cryo_em == StructuralBiologyTechnique.CRYO_EM


class TestClassMethods:
    """Test class-level methods"""

    def test_get_all_meanings(self):
        """Test getting all meanings"""
        meanings = AnatomicalSide.get_all_meanings()

        assert isinstance(meanings, dict)
        assert len(meanings) > 0
        assert "LEFT" in meanings
        assert meanings["LEFT"] == "BSPO:0000000"
        assert "RIGHT" in meanings
        assert meanings["RIGHT"] == "BSPO:0000007"

        # Check that all values are valid CURIE-like strings
        for name, meaning in meanings.items():
            assert isinstance(name, str)
            assert isinstance(meaning, str)
            assert ":" in meaning  # Basic CURIE format check

    def test_get_all_descriptions(self):
        """Test getting all descriptions"""
        # AnatomicalSide doesn't have descriptions, use PresenceEnum instead
        descriptions = PresenceEnum.get_all_descriptions()

        assert isinstance(descriptions, dict)
        assert len(descriptions) > 0
        assert "PRESENT" in descriptions
        assert descriptions["PRESENT"] == "The entity is present"

        # All values should be non-empty strings
        for name, desc in descriptions.items():
            assert isinstance(name, str)
            assert isinstance(desc, str)
            assert len(desc) > 0

    def test_list_metadata(self):
        """Test listing all metadata"""
        all_metadata = AnatomicalSide.list_metadata()

        assert isinstance(all_metadata, dict)
        assert len(all_metadata) > 0
        assert "LEFT" in all_metadata

        left_meta = all_metadata["LEFT"]
        assert left_meta["name"] == "LEFT"
        assert left_meta["value"] == "LEFT"
        # AnatomicalSide.LEFT doesn't have description
        assert "meaning" in left_meta


class TestMultipleEnumTypes:
    """Test functionality across different enum types"""

    def test_structural_biology_enums(self):
        """Test structural biology specific enums"""
        protein = SampleType.PROTEIN
        assert protein.get_description() == "Purified protein sample"
        # SampleType.PROTEIN has NCIT mapping
        assert protein.get_meaning() == "NCIT:C17021"

        cryo_em = StructuralBiologyTechnique.CRYO_EM
        annotations = cryo_em.get_annotations()
        assert "resolution_range" in annotations
        assert annotations["resolution_range"] == "2-30 Å typical"

    def test_biological_kingdom_enum(self):
        """Test biological kingdom enum"""
        eukaryota = BiologicalKingdom.EUKARYOTA
        assert eukaryota.get_description() == "Eukaryota domain"
        assert eukaryota.get_meaning() == "NCBITaxon:2759"

        # Test lookup
        found = BiologicalKingdom.from_meaning("NCBITaxon:2759")
        assert found == BiologicalKingdom.EUKARYOTA

    def test_cross_enum_meaning_isolation(self):
        """Test that meaning lookups are isolated between enums"""
        # This meaning exists in AnatomicalSide but not in SampleType
        anatomical_result = AnatomicalSide.from_meaning("BSPO:0000000")
        sample_result = SampleType.from_meaning("BSPO:0000000")

        assert anatomical_result == AnatomicalSide.LEFT
        assert sample_result is None  # Should not be found in different enum


class TestEdgeCases:
    """Test edge cases and error conditions"""

    def test_empty_metadata_handling(self):
        """Test handling of members without certain metadata fields"""
        # Find a member without meaning (if any)
        for member in PresenceEnum:
            if not member.get_meaning():
                assert member.get_meaning() is None
                # Should still have description
                assert member.get_description() is not None
                break

    def test_metadata_dict_immutability(self):
        """Test that metadata dictionaries can be safely modified"""
        left = AnatomicalSide.LEFT
        metadata1 = left.get_metadata()
        metadata2 = left.get_metadata()

        # Should be independent dict instances
        metadata1["test"] = "modified"
        assert "test" not in metadata2

    def test_annotations_dict_handling(self):
        """Test annotations dictionary handling"""
        anterior = AnatomicalSide.ANTERIOR
        annotations = anterior.get_annotations()

        # Should be a proper dict
        assert isinstance(annotations, dict)

        # Note: Currently annotations return the same dict object
        # This tests the current behavior - modifications affect subsequent calls
        annotations["test"] = "modified"
        fresh_annotations = anterior.get_annotations()
        assert "test" in fresh_annotations  # Same object, so modification persists

        # Clean up for other tests
        del annotations["test"]


class TestJSONSerialization:
    """Test JSON serialization compatibility"""

    def test_json_serialization(self):
        """Test that enums serialize properly to JSON"""
        import json

        left = AnatomicalSide.LEFT
        serialized = json.dumps(left)
        assert serialized == '"LEFT"'

        # Test list serialization
        sides = [AnatomicalSide.LEFT, AnatomicalSide.RIGHT]
        serialized_list = json.dumps(sides)
        assert serialized_list == '["LEFT", "RIGHT"]'

    def test_json_with_metadata(self):
        """Test serializing metadata"""
        import json

        left = AnatomicalSide.LEFT
        metadata = left.get_metadata()
        serialized = json.dumps(metadata)

        # Should serialize without error
        assert isinstance(serialized, str)

        # Should be deserializable
        deserialized = json.loads(serialized)
        assert deserialized["name"] == "LEFT"
        assert deserialized["meaning"] == "BSPO:0000000"


class TestCompatibility:
    """Test compatibility with standard enum operations"""

    def test_in_operator(self):
        """Test 'in' operator works with collections"""
        sides = [AnatomicalSide.LEFT, AnatomicalSide.RIGHT]
        assert AnatomicalSide.LEFT in sides
        assert AnatomicalSide.ANTERIOR not in sides

    def test_set_operations(self):
        """Test set operations"""
        sides_set = {AnatomicalSide.LEFT, AnatomicalSide.RIGHT, AnatomicalSide.LEFT}
        assert len(sides_set) == 2  # Should deduplicate
        assert AnatomicalSide.LEFT in sides_set

    def test_dict_keys(self):
        """Test using enums as dictionary keys"""
        side_data = {
            AnatomicalSide.LEFT: "left_data",
            AnatomicalSide.RIGHT: "right_data"
        }

        assert side_data[AnatomicalSide.LEFT] == "left_data"
        assert side_data[AnatomicalSide.RIGHT] == "right_data"

    def test_repr_and_str(self):
        """Test string representations"""
        left = AnatomicalSide.LEFT

        # Test str() - returns full enum representation
        assert str(left) == "AnatomicalSide.LEFT"

        # Test repr() contains useful info
        repr_str = repr(left)
        assert "AnatomicalSide" in repr_str
        assert "LEFT" in repr_str


if __name__ == "__main__":
    pytest.main([__file__])
