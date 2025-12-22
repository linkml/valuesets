"""
Resource Relation Types

Relation types for linking research resources, based on DataCite 4.6.

These relations describe how resources are connected to each other,
supporting citation networks, version tracking, and provenance chains.

See: https://datacite-metadata-schema.readthedocs.io/


Generated from: data_catalog/relations.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class DataCiteRelationType(RichEnum):
    """
    Types of relationships between research resources from DataCite 4.6.
    Relations are expressed from the perspective of the resource being
    described (A) in relation to another resource (B).
    
    """
    # Enum members
    IS_CITED_BY = "IS_CITED_BY"
    CITES = "CITES"
    IS_SUPPLEMENT_TO = "IS_SUPPLEMENT_TO"
    IS_SUPPLEMENTED_BY = "IS_SUPPLEMENTED_BY"
    IS_CONTINUED_BY = "IS_CONTINUED_BY"
    CONTINUES = "CONTINUES"
    DESCRIBES = "DESCRIBES"
    IS_DESCRIBED_BY = "IS_DESCRIBED_BY"
    HAS_METADATA = "HAS_METADATA"
    IS_METADATA_FOR = "IS_METADATA_FOR"
    HAS_VERSION = "HAS_VERSION"
    IS_VERSION_OF = "IS_VERSION_OF"
    IS_NEW_VERSION_OF = "IS_NEW_VERSION_OF"
    IS_PREVIOUS_VERSION_OF = "IS_PREVIOUS_VERSION_OF"
    IS_PART_OF = "IS_PART_OF"
    HAS_PART = "HAS_PART"
    IS_PUBLISHED_IN = "IS_PUBLISHED_IN"
    IS_REFERENCED_BY = "IS_REFERENCED_BY"
    REFERENCES = "REFERENCES"
    IS_DOCUMENTED_BY = "IS_DOCUMENTED_BY"
    DOCUMENTS = "DOCUMENTS"
    IS_COMPILED_BY = "IS_COMPILED_BY"
    COMPILES = "COMPILES"
    IS_VARIANT_FORM_OF = "IS_VARIANT_FORM_OF"
    IS_ORIGINAL_FORM_OF = "IS_ORIGINAL_FORM_OF"
    IS_IDENTICAL_TO = "IS_IDENTICAL_TO"
    IS_REVIEWED_BY = "IS_REVIEWED_BY"
    REVIEWS = "REVIEWS"
    IS_DERIVED_FROM = "IS_DERIVED_FROM"
    IS_SOURCE_OF = "IS_SOURCE_OF"
    IS_REQUIRED_BY = "IS_REQUIRED_BY"
    REQUIRES = "REQUIRES"
    OBSOLETES = "OBSOLETES"
    IS_OBSOLETED_BY = "IS_OBSOLETED_BY"
    IS_COLLECTED_BY = "IS_COLLECTED_BY"
    COLLECTS = "COLLECTS"
    IS_TRANSLATION_OF = "IS_TRANSLATION_OF"
    HAS_TRANSLATION = "HAS_TRANSLATION"

# Set metadata after class creation
DataCiteRelationType._metadata = {
    "IS_CITED_BY": {'description': 'Indicates that B includes A in a citation.', 'meaning': 'DataCite:IsCitedBy', 'annotations': {'inverse': 'CITES', 'category': 'citation'}},
    "CITES": {'description': 'Indicates that A includes B in a citation.', 'meaning': 'DataCite:Cites', 'annotations': {'inverse': 'IS_CITED_BY', 'category': 'citation'}},
    "IS_SUPPLEMENT_TO": {'description': 'Indicates that A is a supplement to B.', 'meaning': 'DataCite:IsSupplementTo', 'annotations': {'inverse': 'IS_SUPPLEMENTED_BY', 'category': 'supplementary'}},
    "IS_SUPPLEMENTED_BY": {'description': 'Indicates that B is a supplement to A.', 'meaning': 'DataCite:IsSupplementedBy', 'annotations': {'inverse': 'IS_SUPPLEMENT_TO', 'category': 'supplementary'}},
    "IS_CONTINUED_BY": {'description': 'Indicates that A is continued by the work B.', 'meaning': 'DataCite:IsContinuedBy', 'annotations': {'inverse': 'CONTINUES', 'category': 'continuation'}},
    "CONTINUES": {'description': 'Indicates that A is a continuation of the work B.', 'meaning': 'DataCite:Continues', 'annotations': {'inverse': 'IS_CONTINUED_BY', 'category': 'continuation'}},
    "DESCRIBES": {'description': 'Indicates that A describes B.', 'meaning': 'DataCite:Describes', 'annotations': {'inverse': 'IS_DESCRIBED_BY', 'category': 'description'}},
    "IS_DESCRIBED_BY": {'description': 'Indicates that A is described by B.', 'meaning': 'DataCite:IsDescribedBy', 'annotations': {'inverse': 'DESCRIBES', 'category': 'description'}},
    "HAS_METADATA": {'description': 'Indicates that resource A has additional metadata B.', 'meaning': 'DataCite:HasMetadata', 'annotations': {'inverse': 'IS_METADATA_FOR', 'category': 'metadata'}},
    "IS_METADATA_FOR": {'description': 'Indicates that additional metadata A describes resource B.', 'meaning': 'DataCite:IsMetadataFor', 'annotations': {'inverse': 'HAS_METADATA', 'category': 'metadata'}},
    "HAS_VERSION": {'description': 'Indicates that A has a version B.', 'meaning': 'DataCite:HasVersion', 'annotations': {'inverse': 'IS_VERSION_OF', 'category': 'versioning'}},
    "IS_VERSION_OF": {'description': 'Indicates that A is a version of B.', 'meaning': 'DataCite:IsVersionOf', 'annotations': {'inverse': 'HAS_VERSION', 'category': 'versioning'}},
    "IS_NEW_VERSION_OF": {'description': 'Indicates that A is a new edition of B, where the new edition\nhas been modified or updated.\n', 'meaning': 'DataCite:IsNewVersionOf', 'annotations': {'inverse': 'IS_PREVIOUS_VERSION_OF', 'category': 'versioning'}},
    "IS_PREVIOUS_VERSION_OF": {'description': 'Indicates that A is a previous edition of B.', 'meaning': 'DataCite:IsPreviousVersionOf', 'annotations': {'inverse': 'IS_NEW_VERSION_OF', 'category': 'versioning'}},
    "IS_PART_OF": {'description': 'Indicates that A is a portion of B. May be used for elements\nof a series.\n', 'meaning': 'DataCite:IsPartOf', 'annotations': {'inverse': 'HAS_PART', 'category': 'partonomy'}},
    "HAS_PART": {'description': 'Indicates that A includes the part B.', 'meaning': 'DataCite:HasPart', 'annotations': {'inverse': 'IS_PART_OF', 'category': 'partonomy'}},
    "IS_PUBLISHED_IN": {'description': 'Indicates that A is published inside B, but is independent of\nother things published inside of B.\n', 'meaning': 'DataCite:IsPublishedIn', 'annotations': {'category': 'publication'}},
    "IS_REFERENCED_BY": {'description': 'Indicates that A is used as a source of information by B.', 'meaning': 'DataCite:IsReferencedBy', 'annotations': {'inverse': 'REFERENCES', 'category': 'reference'}},
    "REFERENCES": {'description': 'Indicates that B is used as a source of information for A.', 'meaning': 'DataCite:References', 'annotations': {'inverse': 'IS_REFERENCED_BY', 'category': 'reference'}},
    "IS_DOCUMENTED_BY": {'description': 'Indicates that B is documentation about/explaining A.', 'meaning': 'DataCite:IsDocumentedBy', 'annotations': {'inverse': 'DOCUMENTS', 'category': 'documentation'}},
    "DOCUMENTS": {'description': 'Indicates that A is documentation about/explaining B.', 'meaning': 'DataCite:Documents', 'annotations': {'inverse': 'IS_DOCUMENTED_BY', 'category': 'documentation'}},
    "IS_COMPILED_BY": {'description': 'Indicates that B is used to compile or create A.', 'meaning': 'DataCite:IsCompiledBy', 'annotations': {'inverse': 'COMPILES', 'category': 'derivation'}},
    "COMPILES": {'description': 'Indicates that B is the result of a compile or creation event using A.', 'meaning': 'DataCite:Compiles', 'annotations': {'inverse': 'IS_COMPILED_BY', 'category': 'derivation'}},
    "IS_VARIANT_FORM_OF": {'description': 'Indicates that A is a variant or different form of B.', 'meaning': 'DataCite:IsVariantFormOf', 'annotations': {'inverse': 'IS_ORIGINAL_FORM_OF', 'category': 'form'}},
    "IS_ORIGINAL_FORM_OF": {'description': 'Indicates that A is the original form of B.', 'meaning': 'DataCite:IsOriginalFormOf', 'annotations': {'inverse': 'IS_VARIANT_FORM_OF', 'category': 'form'}},
    "IS_IDENTICAL_TO": {'description': 'Indicates that A is identical to B, for use when there is a need\nto register two separate instances of the same resource.\n', 'meaning': 'DataCite:IsIdenticalTo', 'annotations': {'category': 'identity'}},
    "IS_REVIEWED_BY": {'description': 'Indicates that A is reviewed by B.', 'meaning': 'DataCite:IsReviewedBy', 'annotations': {'inverse': 'REVIEWS', 'category': 'review'}},
    "REVIEWS": {'description': 'Indicates that A is a review of B.', 'meaning': 'DataCite:Reviews', 'annotations': {'inverse': 'IS_REVIEWED_BY', 'category': 'review'}},
    "IS_DERIVED_FROM": {'description': 'Indicates that B is a source upon which A is based.', 'meaning': 'DataCite:IsDerivedFrom', 'annotations': {'inverse': 'IS_SOURCE_OF', 'category': 'derivation'}},
    "IS_SOURCE_OF": {'description': 'Indicates that A is a source upon which B is based.', 'meaning': 'DataCite:IsSourceOf', 'annotations': {'inverse': 'IS_DERIVED_FROM', 'category': 'derivation'}},
    "IS_REQUIRED_BY": {'description': 'Indicates that A is required by B.', 'meaning': 'DataCite:IsRequiredBy', 'annotations': {'inverse': 'REQUIRES', 'category': 'dependency'}},
    "REQUIRES": {'description': 'Indicates that A requires B.', 'meaning': 'DataCite:Requires', 'annotations': {'inverse': 'IS_REQUIRED_BY', 'category': 'dependency'}},
    "OBSOLETES": {'description': 'Indicates that A replaces B.', 'meaning': 'DataCite:Obsoletes', 'annotations': {'inverse': 'IS_OBSOLETED_BY', 'category': 'obsolescence'}},
    "IS_OBSOLETED_BY": {'description': 'Indicates that A is replaced by B.', 'meaning': 'DataCite:IsObsoletedBy', 'annotations': {'inverse': 'OBSOLETES', 'category': 'obsolescence'}},
    "IS_COLLECTED_BY": {'description': 'Indicates that A is collected by B.', 'meaning': 'DataCite:IsCollectedBy', 'annotations': {'inverse': 'COLLECTS', 'category': 'collection'}},
    "COLLECTS": {'description': 'Indicates that A collects B.', 'meaning': 'DataCite:Collects', 'annotations': {'inverse': 'IS_COLLECTED_BY', 'category': 'collection'}},
    "IS_TRANSLATION_OF": {'description': 'Indicates that A is a translation of B.', 'meaning': 'DataCite:IsTranslationOf', 'annotations': {'inverse': 'HAS_TRANSLATION', 'category': 'translation', 'added_version': '4.6'}},
    "HAS_TRANSLATION": {'description': 'Indicates that A has a translation B.', 'meaning': 'DataCite:HasTranslation', 'annotations': {'inverse': 'IS_TRANSLATION_OF', 'category': 'translation', 'added_version': '4.6'}},
}

__all__ = [
    "DataCiteRelationType",
]