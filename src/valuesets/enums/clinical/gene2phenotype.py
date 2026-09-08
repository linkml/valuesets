"""
Gene2Phenotype (G2P) Terminology Value Sets

Value sets for the controlled vocabularies used by Gene2Phenotype (G2P), the EBI resource of curated gene-disease associations. G2P records a locus-genotype-mechanism- disease-evidence (LGMDE) thread for each association, and each component of that thread draws on a controlled vocabulary. The terms and definitions here follow the G2P terminology page at https://www.ebi.ac.uk/gene2phenotype/about/terminology, which reuses community standards where they exist: GenCC classification terms for confidence, HPO mode-of-inheritance terms for allelic requirement, HPO inheritance qualifiers for cross-cutting modifiers, the Backwell and Marsh framework (PMID:35395171) for molecular mechanism, the ClinGen gene-disease validity SOP for mechanism evidence, and Sequence Ontology terms for variant consequence and variant type.
Permissible value descriptions are quoted verbatim from those sources, retaining their original spelling and grammar (for example "casual role" for causal role, and "segregration" for segregation in the GenCC confidence text) so that the text here can be diffed against the source. Where a quoted definition is itself inconsistent this is called out in the value's description rather than silently corrected.
Throughout this schema, where a permissible value is mapped to an ontology term, title is the ontology term's label and any differing G2P string is carried as an alias. Consumers wanting G2P's own display string should read aliases rather than title.

Generated from: clinical/gene2phenotype.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class G2PConfidenceCategory(RichEnum):
    """
    The level of confidence that a gene-disease association is real, as asserted by G2P curators. G2P uses the GenCC gene-disease validity classification terms. Operationally several groups use definitive, strong and moderate for clinical reporting; limited, disputed and refuted are not used for clinical reporting. GenCC classification identifiers are recorded in the gencc_classification_id annotation rather than as meaning:, because the GENCC prefix is not registered in bioregistry, OLS or the OBO PURL system and so cannot be resolved; the identifiers were taken from GenCC's own submissions export.
    """
    # Enum members
    DEFINITIVE = "DEFINITIVE"
    STRONG = "STRONG"
    MODERATE = "MODERATE"
    LIMITED = "LIMITED"
    DISPUTED = "DISPUTED"
    REFUTED = "REFUTED"

# Set metadata after class creation
G2PConfidenceCategory._metadata = {
    "DEFINITIVE": {'description': "The role of this gene in this particular disease has been repeatedly demonstrated in both the research and clinical diagnostic settings, and has been upheld over time (at least 2 independent publication over 3 years' time). No convincing evidence has emerged that contradicts the role of the gene in the specified disease. (previously labelled as confirmed) The strength of evidence within publications as well as their number and publication dates is taken into account. In practice, this usually means at least 4 publications over 5 years. Typically this will also include convincing bioinformatic or functional evidence of causation, making it very unlikely that this gene-disease association would ever be refuted.", 'annotations': {'gencc_classification_id': 'GENCC:100001', 'clinical_reporting': 'true'}, 'aliases': ['confirmed']},
    "STRONG": {'description': "The role of this gene as a monogenic cause of disease has been repeatedly and independently demonstrated providing very strong convincing evidence in humans and no conflicting evidence for this gene's role in this disease. (previously labelled as probable).", 'annotations': {'gencc_classification_id': 'GENCC:100002', 'clinical_reporting': 'true'}, 'aliases': ['probable']},
    "MODERATE": {'description': 'There is moderate evidence in humans to support a casual role for this gene in this disease with no contradictory evidence. The body of evidence is not large (e.g possibly only one key paper) but appears convincing enough that the gene-disease pair is likely to be validated with additional evidence in the near future.', 'annotations': {'gencc_classification_id': 'GENCC:100003', 'clinical_reporting': 'true'}},
    "LIMITED": {'description': 'Little human evidence exists to support a casual role for this gene in this disease, but not all evidence has been refuted. For example, there may be a collection of rare missense variants in humans but without convincing functional impact, segregration data that could either arise by chance (e.g across one or two meioses) or does not implicate a single gene, or functional data without direct recapitulation of the phenotype. Overall, the body of evidence does not meet contemporary criteria for claiming a valid association with disease. The majority are probably false associations. (previously labelled as possible).', 'annotations': {'gencc_classification_id': 'GENCC:100004', 'clinical_reporting': 'false'}, 'aliases': ['possible']},
    "DISPUTED": {'description': 'Although evidence has been reported, other evidence of equal weight disputes the claim.', 'annotations': {'gencc_classification_id': 'GENCC:100005', 'clinical_reporting': 'false'}},
    "REFUTED": {'description': 'There has been an assertion of a gene-disease association in the literature, but new valid evidence has arisen that refutes the entire original body of evidence.', 'annotations': {'gencc_classification_id': 'GENCC:100006', 'clinical_reporting': 'false'}},
}

class G2PAllelicRequirement(RichEnum):
    """
    The genotype required at the locus for the disease to manifest, also referred to in G2P as the genotype. HPO mode of inheritance (MOI) terminology is used; G2P uses synonyms of the MOI terms as many of the disorders described are de novo.
    The nine values are G2P's published genotype list, taken verbatim from the API the terminology page itself calls (GET /gene2phenotype/api/attribs/, key "genotype"), which includes the bare monoallelic_X alongside monoallelic_X_hemizygous and monoallelic_X_heterozygous.
    All nine G2P genotype strings are recorded by HPO as oio:hasExactSynonym of the term mapped below (verified against the HPO release directly; note that the OLS obo_synonym field under-reports these, listing only synonyms that carry an xref). That exact-synonym correspondence is what makes these mappings unambiguous.
    By convention in this enum, title is the HPO term label and the G2P string is carried as an alias, matching the pv-mapping guidance and clinical/genetics.yaml; consumers wanting G2P's own display string should read aliases.
    """
    # Enum members
    MONOALLELIC_AUTOSOMAL = "MONOALLELIC_AUTOSOMAL"
    BIALLELIC_AUTOSOMAL = "BIALLELIC_AUTOSOMAL"
    MONOALLELIC_X = "MONOALLELIC_X"
    MONOALLELIC_X_HEMIZYGOUS = "MONOALLELIC_X_HEMIZYGOUS"
    MONOALLELIC_X_HETEROZYGOUS = "MONOALLELIC_X_HETEROZYGOUS"
    MONOALLELIC_Y_HEMIZYGOUS = "MONOALLELIC_Y_HEMIZYGOUS"
    MONOALLELIC_PAR = "MONOALLELIC_PAR"
    BIALLELIC_PAR = "BIALLELIC_PAR"
    MITOCHONDRIAL = "MITOCHONDRIAL"

# Set metadata after class creation
G2PAllelicRequirement._metadata = {
    "MONOALLELIC_AUTOSOMAL": {'description': 'Plausible disease-causing mutations on an autosomal chromosome identified on one allele in all or the vast majority of with specific disorder.', 'meaning': 'HP:0000006', 'aliases': ['monoallelic_autosomal']},
    "BIALLELIC_AUTOSOMAL": {'description': 'Plausible disease-causing homozygous or compound heterozygous mutations identified on both alleles in the autosomal chromosome.', 'meaning': 'HP:0000007', 'aliases': ['biallelic_autosomal']},
    "MONOALLELIC_X": {'description': 'Plausible disease-causing mutations identified on the X chromosome.', 'meaning': 'HP:0001417', 'aliases': ['monoallelic_X']},
    "MONOALLELIC_X_HEMIZYGOUS": {'description': 'Plausible disease-causing mutations identified on the X chromosome in a male as a cause of a specific disease, the disorder being predominantly recessive in female carriers.', 'meaning': 'HP:0001419', 'aliases': ['monoallelic_X_hemizygous']},
    "MONOALLELIC_X_HETEROZYGOUS": {'description': 'Plausible disease-causing mutations identified in one copy of the X chromosome in females as a cause of a specific disease, include disorders where heterozygous females and hemizygous males are similarly affected e.g SMC1A mutations.', 'meaning': 'HP:0001423', 'aliases': ['monoallelic_X_heterozygous']},
    "MONOALLELIC_Y_HEMIZYGOUS": {'description': 'Plausible disease-causing mutations identified in an allele found in the Y chromosome. The Y chromosome is passed from father to son as this mutation may affect only males.', 'meaning': 'HP:0001450', 'aliases': ['monoallelic_Y_hemizygous']},
    "MONOALLELIC_PAR": {'description': 'Plausible disease-causing mutations identified in an allele found in the pseudoautosomal regions. Inheritance is not strictly sex-linked.', 'meaning': 'HP:0034340', 'aliases': ['monoallelic_PAR']},
    "BIALLELIC_PAR": {'description': 'Plausible disease-causing homozygous or compound heterozygous mutations identified on both alleles found in the pseudoautosomal regions. Inheritance is not strictly sex-linked.', 'meaning': 'HP:0034341', 'aliases': ['biallelic_PAR']},
    "MITOCHONDRIAL": {'description': 'Plausible disease-causing mutations identified on mitochondrial DNA where homoplasmy or heteroplasmy are associated with a specific disorder.', 'meaning': 'HP:0001427', 'aliases': ['mitochondrial']},
}

class G2PCrossCuttingModifier(RichEnum):
    """
    Additional qualifiers applied to the allelic requirement of a G2P gene-disease association. HPO inheritance qualifier terms (HP:0034335) are used where available. Potential secondary finding and restricted mutation set are G2P-specific and have no HPO equivalent.
    """
    # Enum members
    DISPLAYS_ANTICIPATION = "DISPLAYS_ANTICIPATION"
    IMPRINTED_REGION = "IMPRINTED_REGION"
    TYPICALLY_DE_NOVO = "TYPICALLY_DE_NOVO"
    TYPICALLY_MOSAIC = "TYPICALLY_MOSAIC"
    TYPIFIED_BY_INCOMPLETE_PENETRANCE = "TYPIFIED_BY_INCOMPLETE_PENETRANCE"
    POTENTIAL_SECONDARY_FINDING = "POTENTIAL_SECONDARY_FINDING"
    RESTRICTED_MUTATION_SET = "RESTRICTED_MUTATION_SET"

# Set metadata after class creation
G2PCrossCuttingModifier._metadata = {
    "DISPLAYS_ANTICIPATION": {'description': 'A phenomenon in which the severity of a disorder increases, or the age of onset decreases, as the disorder is passed from one generation to the next, typically due to expansion of a repeat sequence. For example, Myotonic Dystrophy is caused by triplet repeat expansion in the DMPK gene.', 'meaning': 'HP:0003743', 'aliases': ['displays anticipation']},
    "IMPRINTED_REGION": {'description': 'Requires that the abnormal allele be paternal or maternal in origin, depending on the disease-gene relationship. Imprinting refers to a normal developmental process in which either the paternal or maternal allele is inactivated, depending on the specific locus, thus leading to expression from only one copy of the gene. Disease typically manifests when a deleterious variant is inherited from a parent whose copy of the gene would normally be expressed, but not when a deleterious variant is inherited from a parent whose copy of the gene would normally be inactivated.', 'meaning': 'HP:0034338', 'aliases': ['imprinted region']},
    "TYPICALLY_DE_NOVO": {'description': 'Plausible disease causing mutations that occur post zygotically (formation of gametes). Note that this G2P wording is internally inconsistent: post-zygotic events are somatic, which is what TYPICALLY_MOSAIC describes, whereas gametogenesis is pre-zygotic. The mapped HPO term HP:0025352 carries the intended sense, defining conditions that are exclusively or predominantly observed to display de novo variants.', 'meaning': 'HP:0025352', 'aliases': ['typically de novo']},
    "TYPICALLY_MOSAIC": {'description': 'Plausible disease causing mutations identified on one allele in a proportion of cells with the others being wild-type.', 'meaning': 'HP:0001442', 'aliases': ['typically mosaic']},
    "TYPIFIED_BY_INCOMPLETE_PENETRANCE": {'description': 'A condition in which not all individuals carrying the disease-causing genotype manifest the associated phenotype.', 'meaning': 'HP:0003829', 'aliases': ['typified by incomplete penetrance']},
    "POTENTIAL_SECONDARY_FINDING": {'description': 'This includes ACMG Secondary Findings and/or late onset conditions.'},
    "RESTRICTED_MUTATION_SET": {'description': 'This is used when a disease is associated with a single recurrent variant or a set of variants only found in a particular protein domain.'},
}

class G2PMolecularMechanism(RichEnum):
    """
    The mechanism of disease derived from the available evidence, following the definitions of Backwell and Marsh (PMID:35395171). These mechanisms describe a gene-disease association rather than an individual variant, so the Sequence Ontology variant terms are recorded as close mappings rather than exact meanings.
    """
    # Enum members
    LOSS_OF_FUNCTION = "LOSS_OF_FUNCTION"
    GAIN_OF_FUNCTION = "GAIN_OF_FUNCTION"
    DOMINANT_NEGATIVE = "DOMINANT_NEGATIVE"
    UNDETERMINED_NON_LOSS_OF_FUNCTION = "UNDETERMINED_NON_LOSS_OF_FUNCTION"
    UNDETERMINED = "UNDETERMINED"

# Set metadata after class creation
G2PMolecularMechanism._metadata = {
    "LOSS_OF_FUNCTION": {'description': 'Loss-of-function variants involve a loss of the normal biological function of a protein. Often these are nonsense or frameshift mutations that introduce premature stop codons. Due to nonsense-mediated decay of the resulting mRNAs, most premature stop codons will result in no protein being produced, rather than a truncated protein. However, there are also many examples of loss-of-function variants that change the amino acid sequence and result in non-functional protein products. These mutations can cause a complete loss of function (amorphic), analogous to a protein null mutation, or only a partial loss of function (hypomorphic). May also include variants in regulatory regions.', 'aliases': ['loss_of_function_variant']},
    "GAIN_OF_FUNCTION": {'description': 'Gain-of-function variants have their phenotypic effect because the mutant protein does something different than the wild-type protein. Often, these variants cause disease by increasing protein activity (hypermorphic) or introducing a completely new function (neomorphic), but the specific molecular mechanisms underlying gain-of-function mutations can be complex. May also include variants in regulatory regions.', 'aliases': ['gain_of_function_variant']},
    "DOMINANT_NEGATIVE": {'description': 'Dominant-negative variants involve the mutant protein directly or indirectly blocking the normal biological function of the wild-type protein (antimorphic). They can thus cause a disproportionate (>50%) loss of function, even though only half of the protein is mutated eg. heterozygous variants in COL1A1 that disrupt the triple collagen helix.', 'aliases': ['antimorphic', 'dominant_negative_variant']},
    "UNDETERMINED_NON_LOSS_OF_FUNCTION": {'description': 'Very often it is difficult to distinguish between dominant negative and gain of function, but it is clearly a non-loss-of-function mechanism (e.g. from co-expression experiments showing a damaging effect from the mutant allele).', 'aliases': ['undetermined non-loss-of-function']},
    "UNDETERMINED": {'description': 'Not known.'},
}

class G2PMolecularMechanismSynopsis(RichEnum):
    """
    A more detailed description of the molecular mechanism of a G2P gene-disease association, following the definitions of Backwell and Marsh (PMID:35395171). A synopsis refines the higher-level molecular mechanism; more than one synopsis may apply to a single gene-disease association.
    """
    # Enum members
    DESTABILISING_LOF = "DESTABILISING_LOF"
    INTERACTION_DISRUPTING_LOF = "INTERACTION_DISRUPTING_LOF"
    LOSS_OF_ACTIVITY_LOF = "LOSS_OF_ACTIVITY_LOF"
    LOF_DUE_TO_PROTEIN_MISLOCALISATION = "LOF_DUE_TO_PROTEIN_MISLOCALISATION"
    ASSEMBLY_MEDIATED_DOMINANT_NEGATIVE = "ASSEMBLY_MEDIATED_DOMINANT_NEGATIVE"
    COMPETITIVE_DOMINANT_NEGATIVE = "COMPETITIVE_DOMINANT_NEGATIVE"
    ASSEMBLY_MEDIATED_GOF = "ASSEMBLY_MEDIATED_GOF"
    LOCAL_LOF_LEADING_TO_OVERALL_GOF = "LOCAL_LOF_LEADING_TO_OVERALL_GOF"
    AGGREGATION = "AGGREGATION"
    OTHER_GOF = "OTHER_GOF"

# Set metadata after class creation
G2PMolecularMechanismSynopsis._metadata = {
    "DESTABILISING_LOF": {'description': 'A process whereby a missense change destabilises the protein structure resulting in loss of function.', 'annotations': {'parent_mechanism': 'LOSS_OF_FUNCTION'}},
    "INTERACTION_DISRUPTING_LOF": {'description': 'A process whereby a variant allele disrupts interaction resulting in loss of function, for example a change in an interaction site.', 'annotations': {'parent_mechanism': 'LOSS_OF_FUNCTION'}},
    "LOSS_OF_ACTIVITY_LOF": {'description': 'A process whereby a variant allele disrupts activity resulting in loss of function, for example a change in an active site.', 'annotations': {'parent_mechanism': 'LOSS_OF_FUNCTION'}},
    "LOF_DUE_TO_PROTEIN_MISLOCALISATION": {'description': 'A loss of function caused by mislocalisation of a protein, rather than direct disruption of its structure or function.', 'annotations': {'parent_mechanism': 'LOSS_OF_FUNCTION'}},
    "ASSEMBLY_MEDIATED_DOMINANT_NEGATIVE": {'description': 'A protein change which does not prevent coassembly into a complex with wild-type subunits but results in poisoning the activity of the hybrid complex, causing a disproportionate loss of function.', 'annotations': {'parent_mechanism': 'DOMINANT_NEGATIVE'}},
    "COMPETITIVE_DOMINANT_NEGATIVE": {'description': 'A process whereby the novel protein disrupts specific interactions by competing with wild-type protein, thus having a dominant-negative effect.', 'annotations': {'parent_mechanism': 'DOMINANT_NEGATIVE'}},
    "ASSEMBLY_MEDIATED_GOF": {'description': 'A process whereby incorporation of a mutant subunit into a protein complex leads to a gain of function, for example through constitutive activation of a channel.', 'annotations': {'parent_mechanism': 'GAIN_OF_FUNCTION'}},
    "LOCAL_LOF_LEADING_TO_OVERALL_GOF": {'description': 'A gain of function caused by the localised loss of a specific function within a protein, for example binding of a regulatory domain is disrupted but enzymatic activity is retained.', 'annotations': {'parent_mechanism': 'GAIN_OF_FUNCTION'}},
    "AGGREGATION": {'description': 'A process by which the variant allele causes aggregation usually causing toxic gain of function, for example misfolded proteins self-assembling into large aggregates or RNA binding protein gelation.', 'annotations': {'parent_mechanism': 'GAIN_OF_FUNCTION'}},
    "OTHER_GOF": {'description': 'A gain of function process other than local loss of function or assembly mediated, for example a mutation in an active site which changes histone binding causing a novel function.', 'annotations': {'parent_mechanism': 'GAIN_OF_FUNCTION'}},
}

class G2PMolecularMechanismSupport(RichEnum):
    """
    Whether the molecular mechanism recorded for a G2P gene-disease association is directly supported by reported evidence, or inferred by the curator.
    """
    # Enum members
    EVIDENCE = "EVIDENCE"
    INFERRED = "INFERRED"

# Set metadata after class creation
G2PMolecularMechanismSupport._metadata = {
    "EVIDENCE": {'description': 'The molecular mechanism is directly supported by experimental evidence reported in a publication attached to the record.'},
    "INFERRED": {'description': 'The molecular mechanism is inferred by the curator rather than directly evidenced in the attached publications.'},
}

class G2PMechanismEvidenceCategory(RichEnum):
    """
    The broad category of experimental evidence supporting a molecular mechanism in G2P. G2P evidence classifications reuse terms from the ClinGen gene-disease validity SOP Experimental Evidence Summary Matrix.
    """
    # Enum members
    FUNCTION = "FUNCTION"
    FUNCTIONAL_ALTERATION = "FUNCTIONAL_ALTERATION"
    MODELS = "MODELS"
    RESCUE = "RESCUE"

# Set metadata after class creation
G2PMechanismEvidenceCategory._metadata = {
    "FUNCTION": {'description': 'Evidence about the biochemical function, expression or interactions of the gene product.'},
    "FUNCTIONAL_ALTERATION": {'description': 'Evidence from cells in which the function of the gene has been disrupted, showing a phenotype consistent with the human disease process.'},
    "MODELS": {'description': 'Evidence from a cell culture model or non-human model organism with a disrupted copy of the gene.'},
    "RESCUE": {'description': 'Evidence that the phenotype can be rescued by restoring the wild-type gene or gene product.'},
}

class G2PFunctionEvidence(RichEnum):
    """
    Types of evidence in the function category of the G2P molecular mechanism evidence classification.
    """
    # Enum members
    BIOCHEMICAL = "BIOCHEMICAL"
    PROTEIN_INTERACTION = "PROTEIN_INTERACTION"
    PROTEIN_EXPRESSION = "PROTEIN_EXPRESSION"
    IN_SILICO_MODELLING = "IN_SILICO_MODELLING"

# Set metadata after class creation
G2PFunctionEvidence._metadata = {
    "BIOCHEMICAL": {'description': 'Evidence showing the gene product performs a biochemical function: (A) shared with other known genes in the disease of interest, or (B) consistent with the phenotype.'},
    "PROTEIN_INTERACTION": {'description': 'Evidence showing the gene product interacts with proteins previously implicated in the disease of interest.'},
    "PROTEIN_EXPRESSION": {'description': 'Evidence showing the gene is expressed in tissues relevant to the disease of interest and/or is altered in expression in patients who have the disease.'},
    "IN_SILICO_MODELLING": {'description': 'Evidence generated using computer simulations and models predicting the functional impact of relevant gene-specific variants. These models can predict protein structure changes, disruption of protein interactions, or changes in gene and/or protein expression.'},
}

class G2PFunctionalAlterationEvidence(RichEnum):
    """
    Types of evidence in the functional alteration category of the G2P molecular mechanism evidence classification, distinguished by whether the cells came from an affected individual.
    """
    # Enum members
    PATIENT_CELLS = "PATIENT_CELLS"
    NON_PATIENT_CELLS = "NON_PATIENT_CELLS"

# Set metadata after class creation
G2PFunctionalAlterationEvidence._metadata = {
    "PATIENT_CELLS": {'description': 'Evidence showing that cultured patient cells, in which the function of the gene has been disrupted, have a phenotype that is consistent with the human disease process.'},
    "NON_PATIENT_CELLS": {'description': 'Evidence showing that cultured non-patient cells, in which the function of the gene has been disrupted, have a phenotype that is consistent with the human disease process.'},
}

class G2PModelsEvidence(RichEnum):
    """
    Types of evidence in the models category of the G2P molecular mechanism evidence classification.
    """
    # Enum members
    CELL_CULTURE_MODEL = "CELL_CULTURE_MODEL"
    NON_HUMAN_MODEL_ORGANISM = "NON_HUMAN_MODEL_ORGANISM"

# Set metadata after class creation
G2PModelsEvidence._metadata = {
    "CELL_CULTURE_MODEL": {'description': 'A cell culture model with a disrupted copy of the gene shows a phenotype consistent with the human disease state.'},
    "NON_HUMAN_MODEL_ORGANISM": {'description': 'A non-human model organism with a disrupted copy of the gene shows a phenotype consistent with the human disease state.'},
}

class G2PRescueEvidence(RichEnum):
    """
    Types of evidence in the rescue category of the G2P molecular mechanism evidence classification, distinguished by the system in which rescue was demonstrated.
    """
    # Enum members
    PATIENT_CELLS = "PATIENT_CELLS"
    CELL_CULTURE_MODEL = "CELL_CULTURE_MODEL"
    NON_HUMAN_MODEL_ORGANISM = "NON_HUMAN_MODEL_ORGANISM"

# Set metadata after class creation
G2PRescueEvidence._metadata = {
    "PATIENT_CELLS": {'description': 'Evidence showing that the phenotype can be rescued in patient cells.'},
    "CELL_CULTURE_MODEL": {'description': 'Evidence showing that the phenotype can be rescued in cell culture models.'},
    "NON_HUMAN_MODEL_ORGANISM": {'description': 'Evidence showing that the phenotype can be rescued in non-human model organisms.'},
}

class G2PVariantConsequence(RichEnum):
    """
    The consequence of the reported variants at the protein (for protein-coding genes) or the RNA (for non-protein coding genes), per allele. These are Sequence Ontology terms developed for G2P and described in PMID:37982373; the descriptions below are the G2P-authored usage notes rather than the SO text definitions. As in the other SO-backed enums here, title is uniformly the SO term label and any differing G2P label is carried as an alias; for four of the six values the SO and G2P labels coincide, which is why only altered_gene_product_sequence and function_uncertain_variant carry an alias.
    """
    # Enum members
    ALTERED_GENE_PRODUCT_LEVEL = "ALTERED_GENE_PRODUCT_LEVEL"
    DECREASED_GENE_PRODUCT_LEVEL = "DECREASED_GENE_PRODUCT_LEVEL"
    ABSENT_GENE_PRODUCT = "ABSENT_GENE_PRODUCT"
    INCREASED_GENE_PRODUCT_LEVEL = "INCREASED_GENE_PRODUCT_LEVEL"
    ALTERED_GENE_PRODUCT_STRUCTURE = "ALTERED_GENE_PRODUCT_STRUCTURE"
    UNCERTAIN = "UNCERTAIN"

# Set metadata after class creation
G2PVariantConsequence._metadata = {
    "ALTERED_GENE_PRODUCT_LEVEL": {'description': 'A sequence variant that alters the level or amount of gene product produced. This high-level term can be applied where the direction of level change (increased vs decreased gene product level) is unknown or not confirmed, e.g., promoter or enhancer variants, some splice variants.', 'meaning': 'SO:0002314'},
    "DECREASED_GENE_PRODUCT_LEVEL": {'description': "A sequence variant that decreases the level or amount of gene product produced, e.g., a 5' UTR variant that reduced protein levels by disrupting translation, a 3' UTR variant that affects RNA stability, splice variants that decrease but do not stop expression, variants leading to nonsense-mediated-decay (NMD)-competent premature termination codon (PTCs), or gene-disrupting structural variants.", 'meaning': 'SO:0002316'},
    "ABSENT_GENE_PRODUCT": {'description': 'A sequence variant that results in no gene product. e.g., whole gene or other large scale disruptive structural variant, variants producing NMD-competent PTCs.', 'meaning': 'SO:0002317'},
    "INCREASED_GENE_PRODUCT_LEVEL": {'description': 'A variant that increases the level or amount of gene product produced, e.g., non-disruptive gene duplications, some promoter or enhancer variants.', 'meaning': 'SO:0002315'},
    "ALTERED_GENE_PRODUCT_STRUCTURE": {'description': 'A sequence variant that alters the sequence of a gene product. e.g., missense variants, NMD-incompetent PTCs, and other length-changing variants (in-frame indels, stop loss).', 'meaning': 'SO:0002318', 'aliases': ['altered gene product structure']},
    "UNCERTAIN": {'description': 'A sequence variant in which the function of a gene product is unknown with respect to a reference. Used by G2P where the consequence of the reported variants could not be determined.', 'meaning': 'SO:0002220', 'aliases': ['uncertain']},
}

class G2PVariantTypeGroup(RichEnum):
    """
    The primary type grouping under which G2P organises the variant types associated with a curated gene-disease pair.
    """
    # Enum members
    NMD_VARIANTS = "NMD_VARIANTS"
    SPLICE_VARIANTS = "SPLICE_VARIANTS"
    REGULATORY_VARIANTS = "REGULATORY_VARIANTS"
    PROTEIN_CHANGING_VARIANTS = "PROTEIN_CHANGING_VARIANTS"
    OTHER_VARIANTS = "OTHER_VARIANTS"

# Set metadata after class creation
G2PVariantTypeGroup._metadata = {
    "NMD_VARIANTS": {'description': 'Variant types qualified by whether the resulting transcript is predicted to trigger or escape nonsense-mediated decay.'},
    "SPLICE_VARIANTS": {'description': 'Variant types affecting splice sites or splice regions.'},
    "REGULATORY_VARIANTS": {'description': 'Variant types in untranslated or regulatory regions.'},
    "PROTEIN_CHANGING_VARIANTS": {'description': 'Variant types that change the coding sequence of the gene product.'},
    "OTHER_VARIANTS": {'description': 'Variant types not covered by the NMD, splice, regulatory or protein changing groups, including structural and repeat changes.'},
}

class G2PVariantType(RichEnum):
    """
    The types of variants associated with the curated gene-disease pair reported in the publication. All terms are Sequence Ontology terms. Where G2P uses a label that differs from the current SO label, the G2P label is recorded as an alias. Descriptions are the SO text definitions where SO provides one.
    The NMD-qualified types have two parents in SO, so they are modelled with the base variant as is_a and the NMD qualifier as a mixin. LinkML preserves both, but as of linkml 1.9.5 the OWL generator emits only the is_a parent as rdfs:subClassOf and drops the mixin, so the NMD axis is additionally recorded in the nmd_status annotation to keep it available in every generated artifact. If a later linkml emits permissible-value mixins, that annotation is redundant and can go.
    """
    # Enum members
    NMD_TRIGGERING = "NMD_TRIGGERING"
    NMD_ESCAPING = "NMD_ESCAPING"
    STOP_GAINED_NMD_TRIGGERING = "STOP_GAINED_NMD_TRIGGERING"
    STOP_GAINED_NMD_ESCAPING = "STOP_GAINED_NMD_ESCAPING"
    FRAMESHIFT_VARIANT_NMD_TRIGGERING = "FRAMESHIFT_VARIANT_NMD_TRIGGERING"
    FRAMESHIFT_VARIANT_NMD_ESCAPING = "FRAMESHIFT_VARIANT_NMD_ESCAPING"
    SPLICE_DONOR_VARIANT_NMD_TRIGGERING = "SPLICE_DONOR_VARIANT_NMD_TRIGGERING"
    SPLICE_DONOR_VARIANT_NMD_ESCAPING = "SPLICE_DONOR_VARIANT_NMD_ESCAPING"
    SPLICE_ACCEPTOR_VARIANT_NMD_TRIGGERING = "SPLICE_ACCEPTOR_VARIANT_NMD_TRIGGERING"
    SPLICE_ACCEPTOR_VARIANT_NMD_ESCAPING = "SPLICE_ACCEPTOR_VARIANT_NMD_ESCAPING"
    SPLICE_REGION_VARIANT = "SPLICE_REGION_VARIANT"
    SPLICE_ACCEPTOR_VARIANT = "SPLICE_ACCEPTOR_VARIANT"
    SPLICE_DONOR_VARIANT = "SPLICE_DONOR_VARIANT"
    FIVE_PRIME_UTR_VARIANT = "FIVE_PRIME_UTR_VARIANT"
    THREE_PRIME_UTR_VARIANT = "THREE_PRIME_UTR_VARIANT"
    REGULATORY_REGION_VARIANT = "REGULATORY_REGION_VARIANT"
    START_LOST = "START_LOST"
    STOP_GAINED = "STOP_GAINED"
    STOP_LOST = "STOP_LOST"
    FRAMESHIFT_VARIANT = "FRAMESHIFT_VARIANT"
    MISSENSE_VARIANT = "MISSENSE_VARIANT"
    INFRAME_INSERTION = "INFRAME_INSERTION"
    INFRAME_DELETION = "INFRAME_DELETION"
    SYNONYMOUS_VARIANT = "SYNONYMOUS_VARIANT"
    INTRON_VARIANT = "INTRON_VARIANT"
    INTERGENIC_VARIANT = "INTERGENIC_VARIANT"
    NON_CODING_TRANSCRIPT_VARIANT = "NON_CODING_TRANSCRIPT_VARIANT"
    SHORT_TANDEM_REPEAT_CHANGE = "SHORT_TANDEM_REPEAT_CHANGE"
    COPY_NUMBER_VARIATION = "COPY_NUMBER_VARIATION"
    WHOLE_PARTIAL_GENE_DELETION = "WHOLE_PARTIAL_GENE_DELETION"
    WHOLE_PARTIAL_GENE_DUPLICATION = "WHOLE_PARTIAL_GENE_DUPLICATION"

# Set metadata after class creation
G2PVariantType._metadata = {
    "NMD_TRIGGERING": {'description': 'A sequence variant that leads to a change in the location of a termination codon in a transcript that leads to nonsense-mediated decay (NMD). The change in location of a termination codon can be caused by several different types of sequence variants, including stop_gained (SO:0001587), frameshift_variant (SO:0001589), splice_donor_variant (SO:0001575), and splice_acceptor_variant (SO:0001574) types of variants.', 'meaning': 'SO:0002319', 'annotations': {'variant_type_group': 'NMD_VARIANTS'}, 'aliases': ['NMD_triggering']},
    "NMD_ESCAPING": {'description': 'A sequence variant that leads to a change in the location of a termination codon in a transcript but allows the transcript to escape nonsense-mediated decay (NMD). The change in location of a termination codon can be caused by several different types of sequence variants, including stop_gained (SO:0001587), frameshift_variant (SO:0001589), splice_donor_variant (SO:0001575), and splice_acceptor_variant (SO:0001574) types of variants.', 'meaning': 'SO:0002320', 'annotations': {'variant_type_group': 'NMD_VARIANTS'}, 'aliases': ['NMD_escaping']},
    "STOP_GAINED_NMD_TRIGGERING": {'description': 'A stop_gained (SO:0001587) variant that is degraded by nonsense-mediated decay (NMD).', 'meaning': 'SO:0002321', 'annotations': {'variant_type_group': 'NMD_VARIANTS', 'nmd_status': 'NMD_TRIGGERING'}},
    "STOP_GAINED_NMD_ESCAPING": {'description': 'A stop_gained (SO:0001587) variant that allows the transcript to escape nonsense-mediated decay (NMD).', 'meaning': 'SO:0002322', 'annotations': {'variant_type_group': 'NMD_VARIANTS', 'nmd_status': 'NMD_ESCAPING'}},
    "FRAMESHIFT_VARIANT_NMD_TRIGGERING": {'description': 'A frameshift_variant (SO:0001589) that is degraded by nonsense-mediated decay (NMD).', 'meaning': 'SO:0002323', 'annotations': {'variant_type_group': 'NMD_VARIANTS', 'nmd_status': 'NMD_TRIGGERING'}},
    "FRAMESHIFT_VARIANT_NMD_ESCAPING": {'description': 'A frameshift_variant (SO:0001589) that allows the transcript to escape nonsense-mediated decay (NMD).', 'meaning': 'SO:0002324', 'annotations': {'variant_type_group': 'NMD_VARIANTS', 'nmd_status': 'NMD_ESCAPING'}},
    "SPLICE_DONOR_VARIANT_NMD_TRIGGERING": {'description': 'A splice_donor_variant (SO:0001575) that is degraded by nonsense-mediated decay (NMD).', 'meaning': 'SO:0002325', 'annotations': {'variant_type_group': 'NMD_VARIANTS', 'nmd_status': 'NMD_TRIGGERING'}},
    "SPLICE_DONOR_VARIANT_NMD_ESCAPING": {'description': 'A splice_donor_variant (SO:0001575) that allows the transcript to escape nonsense-mediated decay (NMD).', 'meaning': 'SO:0002326', 'annotations': {'variant_type_group': 'NMD_VARIANTS', 'nmd_status': 'NMD_ESCAPING'}},
    "SPLICE_ACCEPTOR_VARIANT_NMD_TRIGGERING": {'description': 'A splice_acceptor_variant (SO:0001574) that is degraded by nonsense-mediated decay (NMD).', 'meaning': 'SO:0002327', 'annotations': {'variant_type_group': 'NMD_VARIANTS', 'nmd_status': 'NMD_TRIGGERING'}},
    "SPLICE_ACCEPTOR_VARIANT_NMD_ESCAPING": {'description': 'A splice_acceptor_variant (SO:0001574) that allows the transcript to escape nonsense-mediated decay (NMD).', 'meaning': 'SO:0002328', 'annotations': {'variant_type_group': 'NMD_VARIANTS', 'nmd_status': 'NMD_ESCAPING'}},
    "SPLICE_REGION_VARIANT": {'description': 'A sequence variant in which a change has occurred within the region of the splice site, either within 1-3 bases of the exon or 3-8 bases of the intron.', 'meaning': 'SO:0001630', 'annotations': {'variant_type_group': 'SPLICE_VARIANTS'}},
    "SPLICE_ACCEPTOR_VARIANT": {'description': "A splice variant that changes the 2 base region at the 3' end of an intron.", 'meaning': 'SO:0001574', 'annotations': {'variant_type_group': 'SPLICE_VARIANTS'}},
    "SPLICE_DONOR_VARIANT": {'description': "A splice variant that changes the 2 base pair region at the 5' end of an intron.", 'meaning': 'SO:0001575', 'annotations': {'variant_type_group': 'SPLICE_VARIANTS'}},
    "FIVE_PRIME_UTR_VARIANT": {'description': "A UTR variant of the 5' UTR.", 'meaning': 'SO:0001623', 'annotations': {'variant_type_group': 'REGULATORY_VARIANTS'}},
    "THREE_PRIME_UTR_VARIANT": {'description': "A UTR variant of the 3' UTR.", 'meaning': 'SO:0001624', 'annotations': {'variant_type_group': 'REGULATORY_VARIANTS'}},
    "REGULATORY_REGION_VARIANT": {'description': 'A sequence variant located within a regulatory region.', 'meaning': 'SO:0001566', 'annotations': {'variant_type_group': 'REGULATORY_VARIANTS'}},
    "START_LOST": {'description': 'A codon variant that changes at least one base of the canonical start codon.', 'meaning': 'SO:0002012', 'annotations': {'variant_type_group': 'PROTEIN_CHANGING_VARIANTS'}},
    "STOP_GAINED": {'description': 'A sequence variant whereby at least one base of a codon is changed, resulting in a premature stop codon, leading to a shortened polypeptide.', 'meaning': 'SO:0001587', 'annotations': {'variant_type_group': 'PROTEIN_CHANGING_VARIANTS'}},
    "STOP_LOST": {'description': 'A sequence variant where at least one base of the terminator codon (stop) is changed, resulting in an elongated transcript.', 'meaning': 'SO:0001578', 'annotations': {'variant_type_group': 'PROTEIN_CHANGING_VARIANTS'}},
    "FRAMESHIFT_VARIANT": {'description': 'A sequence variant which causes a disruption of the translational reading frame, because the number of nucleotides inserted or deleted is not a multiple of three.', 'meaning': 'SO:0001589', 'annotations': {'variant_type_group': 'PROTEIN_CHANGING_VARIANTS'}},
    "MISSENSE_VARIANT": {'description': 'A sequence variant, that changes one or more bases, resulting in a different amino acid sequence but where the length is preserved.', 'meaning': 'SO:0001583', 'annotations': {'variant_type_group': 'PROTEIN_CHANGING_VARIANTS'}},
    "INFRAME_INSERTION": {'description': 'An inframe non synonymous variant that inserts bases into in the coding sequence.', 'meaning': 'SO:0001821', 'annotations': {'variant_type_group': 'PROTEIN_CHANGING_VARIANTS'}},
    "INFRAME_DELETION": {'description': 'An inframe non synonymous variant that deletes bases from the coding sequence.', 'meaning': 'SO:0001822', 'annotations': {'variant_type_group': 'PROTEIN_CHANGING_VARIANTS'}},
    "SYNONYMOUS_VARIANT": {'description': 'A sequence variant where there is no resulting change to the encoded amino acid.', 'meaning': 'SO:0001819', 'annotations': {'variant_type_group': 'OTHER_VARIANTS'}},
    "INTRON_VARIANT": {'description': 'A transcript variant occurring within an intron.', 'meaning': 'SO:0001627', 'annotations': {'variant_type_group': 'OTHER_VARIANTS'}},
    "INTERGENIC_VARIANT": {'description': 'A sequence variant located in the intergenic region, between genes.', 'meaning': 'SO:0001628', 'annotations': {'variant_type_group': 'OTHER_VARIANTS'}},
    "NON_CODING_TRANSCRIPT_VARIANT": {'description': 'A transcript variant of a non coding RNA gene.', 'meaning': 'SO:0001619', 'annotations': {'variant_type_group': 'OTHER_VARIANTS'}},
    "SHORT_TANDEM_REPEAT_CHANGE": {'description': 'A sequence variant where the copies of a short tandem repeat (STR) feature are either contracted or expanded. SO:0002161 carries no text definition; this description is taken from the SO term comment.', 'meaning': 'SO:0002161', 'annotations': {'variant_type_group': 'OTHER_VARIANTS'}},
    "COPY_NUMBER_VARIATION": {'description': 'A variation that increases or decreases the copy number of a given region.', 'meaning': 'SO:0001019', 'annotations': {'variant_type_group': 'OTHER_VARIANTS'}},
    "WHOLE_PARTIAL_GENE_DELETION": {'description': 'A feature ablation whereby the deleted region includes a transcript feature. Used by G2P to record whole or partial gene deletions.', 'meaning': 'SO:0001893', 'annotations': {'variant_type_group': 'OTHER_VARIANTS'}, 'aliases': ['whole_partial_gene_deletion']},
    "WHOLE_PARTIAL_GENE_DUPLICATION": {'description': 'A feature amplification of a region containing a transcript. Used by G2P to record whole or partial gene duplications.', 'meaning': 'SO:0001889', 'annotations': {'variant_type_group': 'OTHER_VARIANTS'}, 'aliases': ['whole_partial_gene_duplication']},
}

class G2PPanel(RichEnum):
    """
    The disease-area panels into which G2P organises its curated gene-disease associations. A gene-disease association may appear on more than one panel.
    """
    # Enum members
    CANCER = "CANCER"
    CARDIAC = "CARDIAC"
    DD = "DD"
    EAR = "EAR"
    EYE = "EYE"
    SKELETAL = "SKELETAL"
    SKIN = "SKIN"

# Set metadata after class creation
G2PPanel._metadata = {
    "CANCER": {'description': 'Cancer disorders.'},
    "CARDIAC": {'description': 'Cardiac disorders.'},
    "DD": {'description': 'Developmental disorders.', 'aliases': ['Developmental disorders']},
    "EAR": {'description': 'Ear disorders.'},
    "EYE": {'description': 'Eye disorders.'},
    "SKELETAL": {'description': 'Skeletal disorders.'},
    "SKIN": {'description': 'Skin disorders.'},
}

__all__ = [
    "G2PConfidenceCategory",
    "G2PAllelicRequirement",
    "G2PCrossCuttingModifier",
    "G2PMolecularMechanism",
    "G2PMolecularMechanismSynopsis",
    "G2PMolecularMechanismSupport",
    "G2PMechanismEvidenceCategory",
    "G2PFunctionEvidence",
    "G2PFunctionalAlterationEvidence",
    "G2PModelsEvidence",
    "G2PRescueEvidence",
    "G2PVariantConsequence",
    "G2PVariantTypeGroup",
    "G2PVariantType",
    "G2PPanel",
]