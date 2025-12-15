"""
Biosynthetic Gene Cluster Categories

Value sets for biosynthetic gene cluster (BGC) categories used in natural product biosynthesis.
These categories represent the major classes of secondary metabolites produced by BGCs.
Based on the MIBiG (Minimum Information about a Biosynthetic Gene cluster) standard.

Generated from: bio/bgc_categories.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class BgcCategoryEnum(RichEnum):
    """
    Categories of biosynthetic gene clusters based on the type of secondary metabolite produced.
    These categories are used in genome mining and natural product discovery.
    """
    # Enum members
    POLYKETIDE = "POLYKETIDE"
    NRP = "NRP"
    RIPP = "RIPP"
    TERPENE = "TERPENE"
    ALKALOID = "ALKALOID"
    SACCHARIDE = "SACCHARIDE"
    OTHER = "OTHER"

# Set metadata after class creation
BgcCategoryEnum._metadata = {
    "POLYKETIDE": {'description': 'Polyketide biosynthetic gene clusters', 'meaning': 'CHEBI:26188', 'annotations': {'definition': 'Natural products containing alternating carbonyl and methylene groups', 'biosynthetic_enzyme': 'Polyketide synthase (PKS)', 'examples': 'Erythromycin, lovastatin, rapamycin'}},
    "NRP": {'description': 'Non-ribosomal peptide biosynthetic gene clusters', 'annotations': {'definition': 'Peptides synthesized by non-ribosomal peptide synthetases', 'biosynthetic_enzyme': 'Non-ribosomal peptide synthetase (NRPS)', 'examples': 'Penicillin, vancomycin, cyclosporin'}},
    "RIPP": {'description': 'RiPP biosynthetic gene clusters', 'annotations': {'definition': 'Ribosomally synthesized peptides with extensive post-translational modifications', 'biosynthetic_enzyme': 'Various modifying enzymes', 'examples': 'Nisin, thiopeptides, lanthipeptides', 'related_chebi': 'CHEBI:71629 (nisin)'}},
    "TERPENE": {'description': 'Terpene biosynthetic gene clusters', 'meaning': 'CHEBI:35186', 'annotations': {'definition': 'Hydrocarbons derived from isoprene units', 'biosynthetic_enzyme': 'Terpene synthase', 'examples': 'Limonene, carotenoids, taxol'}},
    "ALKALOID": {'description': 'Alkaloid biosynthetic gene clusters', 'meaning': 'CHEBI:22315', 'annotations': {'definition': 'Nitrogen-containing organic compounds with diverse structures', 'biosynthetic_enzyme': 'Various enzymes', 'examples': 'Morphine, caffeine, nicotine'}},
    "SACCHARIDE": {'description': 'Saccharide/polysaccharide biosynthetic gene clusters', 'meaning': 'CHEBI:18154', 'annotations': {'definition': 'Carbohydrate polymers and oligomers', 'biosynthetic_enzyme': 'Glycosyltransferases', 'examples': 'Cellulose, chitin, bacterial capsular polysaccharides'}},
    "OTHER": {'description': 'Other or unclassified biosynthetic gene clusters', 'annotations': {'definition': 'BGCs that do not fit into standard categories or are of unknown type', 'examples': 'Novel or hybrid BGCs'}},
}

__all__ = [
    "BgcCategoryEnum",
]