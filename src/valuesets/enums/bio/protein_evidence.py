"""
Protein Evidence Value Sets

Value sets related to protein evidence and annotation status

Generated from: bio/protein_evidence.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ProteinEvidenceForExistence(RichEnum):
    """
    The evidence for the existence of a biological entity. See https://www.uniprot.org/help/protein_existence and https://www.ncbi.nlm.nih.gov/genbank/evidence/.
    """
    # Enum members
    EXPERIMENTAL_EVIDENCE_AT_PROTEIN_LEVEL = "EXPERIMENTAL_EVIDENCE_AT_PROTEIN_LEVEL"
    EXPERIMENTAL_EVIDENCE_AT_TRANSCRIPT_LEVEL = "EXPERIMENTAL_EVIDENCE_AT_TRANSCRIPT_LEVEL"
    PROTEIN_INFERRED_BY_HOMOLOGY = "PROTEIN_INFERRED_BY_HOMOLOGY"
    PROTEIN_PREDICTED = "PROTEIN_PREDICTED"
    PROTEIN_UNCERTAIN = "PROTEIN_UNCERTAIN"

# Set metadata after class creation
ProteinEvidenceForExistence._metadata = {
    "EXPERIMENTAL_EVIDENCE_AT_PROTEIN_LEVEL": {'description': 'Indicates that there is clear experimental evidence for the existence of the protein. The criteria include partial or complete Edman sequencing, clear identification by mass spectrometry, X-ray or NMR structure, good quality protein-protein interaction or detection of the protein by antibodies.'},
    "EXPERIMENTAL_EVIDENCE_AT_TRANSCRIPT_LEVEL": {'description': 'Indicates that the existence of a protein has not been strictly proven but that expression data (such as existence of cDNA(s), RT-PCR or Northern blots) indicate the existence of a transcript.'},
    "PROTEIN_INFERRED_BY_HOMOLOGY": {'description': 'Indicates that the existence of a protein is probable because clear orthologs exist in closely related species.'},
    "PROTEIN_PREDICTED": {'description': 'Used for entries without evidence at protein, transcript, or homology levels.'},
    "PROTEIN_UNCERTAIN": {'description': 'Indicates that the existence of the protein is unsure.'},
}

class RefSeqStatusType(RichEnum):
    """
    RefSeq status codes, taken from https://www.ncbi.nlm.nih.gov/genbank/evidence/.
    """
    # Enum members
    MODEL = "MODEL"
    INFERRED = "INFERRED"
    PREDICTED = "PREDICTED"
    PROVISIONAL = "PROVISIONAL"
    REVIEWED = "REVIEWED"
    VALIDATED = "VALIDATED"
    WGS = "WGS"

# Set metadata after class creation
RefSeqStatusType._metadata = {
    "MODEL": {'description': 'The RefSeq record is provided by the NCBI Genome Annotation pipeline and is not subject to individual review or revision between annotation runs.'},
    "INFERRED": {'description': 'The RefSeq record has been predicted by genome sequence analysis, but it is not yet supported by experimental evidence. The record may be partially supported by homology data.'},
    "PREDICTED": {'description': 'The RefSeq record has not yet been subject to individual review, and some aspect of the RefSeq record is predicted.'},
    "PROVISIONAL": {'description': 'The RefSeq record has not yet been subject to individual review. The initial sequence-to-gene association has been established by outside collaborators or NCBI staff.'},
    "REVIEWED": {'description': 'The RefSeq record has been reviewed by NCBI staff or by a collaborator. The NCBI review process includes assessing available sequence data and the literature. Some RefSeq records may incorporate expanded sequence and annotation information.'},
    "VALIDATED": {'description': 'The RefSeq record has undergone an initial review to provide the preferred sequence standard. The record has not yet been subject to final review at which time additional functional information may be provided.'},
    "WGS": {'description': 'The RefSeq record is provided to represent a collection of whole genome shotgun sequences. These records are not subject to individual review or revisions between genome updates.'},
}

__all__ = [
    "ProteinEvidenceForExistence",
    "RefSeqStatusType",
]