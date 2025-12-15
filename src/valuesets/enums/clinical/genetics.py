"""
Clinical Genetics Value Sets

Value sets for clinical genetics including modes of inheritance

Generated from: clinical/genetics.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ModeOfInheritance(RichEnum):
    """
    Patterns of genetic inheritance describing how traits or disorders are passed between generations. Based on HP:0000005 (Mode of inheritance).
    """
    # Enum members
    AUTOSOMAL_DOMINANT = "AUTOSOMAL_DOMINANT"
    AUTOSOMAL_RECESSIVE = "AUTOSOMAL_RECESSIVE"
    X_LINKED = "X_LINKED"
    X_LINKED_DOMINANT = "X_LINKED_DOMINANT"
    X_LINKED_RECESSIVE = "X_LINKED_RECESSIVE"
    Y_LINKED = "Y_LINKED"
    MITOCHONDRIAL = "MITOCHONDRIAL"
    MENDELIAN = "MENDELIAN"
    NON_MENDELIAN = "NON_MENDELIAN"
    DIGENIC = "DIGENIC"
    OLIGOGENIC = "OLIGOGENIC"
    POLYGENIC = "POLYGENIC"
    SEMIDOMINANT = "SEMIDOMINANT"
    PSEUDOAUTOSOMAL = "PSEUDOAUTOSOMAL"
    PSEUDOAUTOSOMAL_DOMINANT = "PSEUDOAUTOSOMAL_DOMINANT"
    PSEUDOAUTOSOMAL_RECESSIVE = "PSEUDOAUTOSOMAL_RECESSIVE"

# Set metadata after class creation
ModeOfInheritance._metadata = {
    "AUTOSOMAL_DOMINANT": {'description': 'A mode of inheritance that is observed for traits related to a gene encoded on one of the autosomes in which a trait manifests in heterozygotes.', 'meaning': 'HP:0000006'},
    "AUTOSOMAL_RECESSIVE": {'description': 'A mode of inheritance that is observed for traits related to a gene encoded on one of the autosomes in which a trait manifests in individuals with two pathogenic alleles.', 'meaning': 'HP:0000007'},
    "X_LINKED": {'description': 'A mode of inheritance that is observed for traits related to a gene encoded on the X chromosome.', 'meaning': 'HP:0001417'},
    "X_LINKED_DOMINANT": {'description': 'A mode of inheritance that is observed for dominant traits related to a gene encoded on the X chromosome.', 'meaning': 'HP:0001423'},
    "X_LINKED_RECESSIVE": {'description': 'A mode of inheritance that is observed for recessive traits related to a gene encoded on the X chromosome.', 'meaning': 'HP:0001419'},
    "Y_LINKED": {'description': 'A mode of inheritance that is observed for traits related to a gene encoded on the Y chromosome.', 'meaning': 'HP:0001450'},
    "MITOCHONDRIAL": {'description': 'A mode of inheritance that is observed for traits related to a gene encoded on the mitochondrial genome. Maternally inherited.', 'meaning': 'HP:0001427'},
    "MENDELIAN": {'description': 'A mode of inheritance of diseases whose pathophysiology can be traced back to deleterious variants in a single gene.', 'meaning': 'HP:0034345'},
    "NON_MENDELIAN": {'description': 'A mode of inheritance that depends on genetic determinants in more than one gene.', 'meaning': 'HP:0001426'},
    "DIGENIC": {'description': 'A type of multifactorial inheritance governed by the simultaneous action of two gene loci.', 'meaning': 'HP:0010984'},
    "OLIGOGENIC": {'description': 'A type of multifactorial inheritance governed by the simultaneous action of a few gene loci (typically three).', 'meaning': 'HP:0010983'},
    "POLYGENIC": {'description': 'A mode of inheritance that depends on a mixture of major and minor genetic determinants possibly together with environmental factors.', 'meaning': 'HP:0010982'},
    "SEMIDOMINANT": {'description': 'A mode of inheritance for traits that can manifest in both monoallelic and biallelic states, with similar or differing phenotype severity.', 'meaning': 'HP:0032113'},
    "PSEUDOAUTOSOMAL": {'description': 'A pattern of inheritance observed for alleles in the X-Y identical regions, resembling autosomal inheritance.', 'meaning': 'HP:0034339'},
    "PSEUDOAUTOSOMAL_DOMINANT": {'description': 'A type of pseudoautosomal inheritance that is dominant.', 'meaning': 'HP:0034340'},
    "PSEUDOAUTOSOMAL_RECESSIVE": {'description': 'A type of pseudoautosomal inheritance that is recessive.', 'meaning': 'HP:0034341'},
}

__all__ = [
    "ModeOfInheritance",
]