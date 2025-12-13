"""
Genome Feature Types

Genome feature types from SOFA (Sequence Ontology Feature Annotation),
the subset of SO used in GFF3 files for genome annotation.
Organized hierarchically following the Sequence Ontology structure.

Generated from: bio/genome_features.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class GenomeFeatureType(RichEnum):
    """
    Genome feature types from SOFA (Sequence Ontology Feature Annotation).
    This is the subset of Sequence Ontology terms used in GFF3 files.
    Organized hierarchically following the Sequence Ontology structure.
    """
    # Enum members
    REGION = "REGION"
    BIOLOGICAL_REGION = "BIOLOGICAL_REGION"
    GENE = "GENE"
    TRANSCRIPT = "TRANSCRIPT"
    PRIMARY_TRANSCRIPT = "PRIMARY_TRANSCRIPT"
    MRNA = "MRNA"
    EXON = "EXON"
    CDS = "CDS"
    INTRON = "INTRON"
    FIVE_PRIME_UTR = "FIVE_PRIME_UTR"
    THREE_PRIME_UTR = "THREE_PRIME_UTR"
    NCRNA = "NCRNA"
    RRNA = "RRNA"
    TRNA = "TRNA"
    SNRNA = "SNRNA"
    SNORNA = "SNORNA"
    MIRNA = "MIRNA"
    LNCRNA = "LNCRNA"
    RIBOZYME = "RIBOZYME"
    ANTISENSE_RNA = "ANTISENSE_RNA"
    PSEUDOGENE = "PSEUDOGENE"
    PROCESSED_PSEUDOGENE = "PROCESSED_PSEUDOGENE"
    REGULATORY_REGION = "REGULATORY_REGION"
    PROMOTER = "PROMOTER"
    ENHANCER = "ENHANCER"
    SILENCER = "SILENCER"
    TERMINATOR = "TERMINATOR"
    ATTENUATOR = "ATTENUATOR"
    POLYA_SIGNAL_SEQUENCE = "POLYA_SIGNAL_SEQUENCE"
    BINDING_SITE = "BINDING_SITE"
    TFBS = "TFBS"
    RIBOSOME_ENTRY_SITE = "RIBOSOME_ENTRY_SITE"
    POLYA_SITE = "POLYA_SITE"
    REPEAT_REGION = "REPEAT_REGION"
    DISPERSED_REPEAT = "DISPERSED_REPEAT"
    TANDEM_REPEAT = "TANDEM_REPEAT"
    INVERTED_REPEAT = "INVERTED_REPEAT"
    TRANSPOSABLE_ELEMENT = "TRANSPOSABLE_ELEMENT"
    MOBILE_ELEMENT = "MOBILE_ELEMENT"
    SEQUENCE_ALTERATION = "SEQUENCE_ALTERATION"
    INSERTION = "INSERTION"
    DELETION = "DELETION"
    INVERSION = "INVERSION"
    DUPLICATION = "DUPLICATION"
    SUBSTITUTION = "SUBSTITUTION"
    ORIGIN_OF_REPLICATION = "ORIGIN_OF_REPLICATION"
    POLYC_TRACT = "POLYC_TRACT"
    GAP = "GAP"
    ASSEMBLY_GAP = "ASSEMBLY_GAP"
    CHROMOSOME = "CHROMOSOME"
    SUPERCONTIG = "SUPERCONTIG"
    CONTIG = "CONTIG"
    SCAFFOLD = "SCAFFOLD"
    CLONE = "CLONE"
    PLASMID = "PLASMID"
    POLYPEPTIDE = "POLYPEPTIDE"
    MATURE_PROTEIN_REGION = "MATURE_PROTEIN_REGION"
    SIGNAL_PEPTIDE = "SIGNAL_PEPTIDE"
    TRANSIT_PEPTIDE = "TRANSIT_PEPTIDE"
    PROPEPTIDE = "PROPEPTIDE"
    OPERON = "OPERON"
    STEM_LOOP = "STEM_LOOP"
    D_LOOP = "D_LOOP"
    MATCH = "MATCH"
    CDNA_MATCH = "CDNA_MATCH"
    EST_MATCH = "EST_MATCH"
    PROTEIN_MATCH = "PROTEIN_MATCH"
    NUCLEOTIDE_MATCH = "NUCLEOTIDE_MATCH"
    JUNCTION_FEATURE = "JUNCTION_FEATURE"
    SPLICE_SITE = "SPLICE_SITE"
    FIVE_PRIME_SPLICE_SITE = "FIVE_PRIME_SPLICE_SITE"
    THREE_PRIME_SPLICE_SITE = "THREE_PRIME_SPLICE_SITE"
    START_CODON = "START_CODON"
    STOP_CODON = "STOP_CODON"
    CENTROMERE = "CENTROMERE"
    TELOMERE = "TELOMERE"

# Set metadata after class creation
GenomeFeatureType._metadata = {
    "REGION": {'description': 'A sequence feature with an extent greater than zero', 'meaning': 'SO:0000001'},
    "BIOLOGICAL_REGION": {'description': 'A region defined by its biological properties', 'meaning': 'SO:0001411'},
    "GENE": {'description': 'A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript', 'meaning': 'SO:0000704'},
    "TRANSCRIPT": {'description': 'An RNA synthesized on a DNA or RNA template by an RNA polymerase', 'meaning': 'SO:0000673'},
    "PRIMARY_TRANSCRIPT": {'description': 'A transcript that has not been processed', 'meaning': 'SO:0000185'},
    "MRNA": {'description': "Messenger RNA; includes 5'UTR, coding sequences and 3'UTR", 'meaning': 'SO:0000234'},
    "EXON": {'description': 'A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA splicing', 'meaning': 'SO:0000147'},
    "CDS": {'description': 'Coding sequence; sequence of nucleotides that corresponds with the sequence of amino acids in a protein', 'meaning': 'SO:0000316'},
    "INTRON": {'description': 'A region of a primary transcript that is transcribed, but removed from within the transcript by splicing', 'meaning': 'SO:0000188'},
    "FIVE_PRIME_UTR": {'description': "5' untranslated region", 'meaning': 'SO:0000204'},
    "THREE_PRIME_UTR": {'description': "3' untranslated region", 'meaning': 'SO:0000205'},
    "NCRNA": {'description': 'Non-protein coding RNA', 'meaning': 'SO:0000655'},
    "RRNA": {'description': 'Ribosomal RNA', 'meaning': 'SO:0000252'},
    "TRNA": {'description': 'Transfer RNA', 'meaning': 'SO:0000253'},
    "SNRNA": {'description': 'Small nuclear RNA', 'meaning': 'SO:0000274'},
    "SNORNA": {'description': 'Small nucleolar RNA', 'meaning': 'SO:0000275'},
    "MIRNA": {'description': 'MicroRNA', 'meaning': 'SO:0000276'},
    "LNCRNA": {'description': 'Long non-coding RNA', 'meaning': 'SO:0001877'},
    "RIBOZYME": {'description': 'An RNA with catalytic activity', 'meaning': 'SO:0000374'},
    "ANTISENSE_RNA": {'description': 'RNA that is complementary to other RNA', 'meaning': 'SO:0000644'},
    "PSEUDOGENE": {'description': 'A sequence that closely resembles a known functional gene but does not produce a functional product', 'meaning': 'SO:0000336'},
    "PROCESSED_PSEUDOGENE": {'description': 'A pseudogene arising from reverse transcription of mRNA', 'meaning': 'SO:0000043'},
    "REGULATORY_REGION": {'description': 'A region involved in the control of the process of gene expression', 'meaning': 'SO:0005836'},
    "PROMOTER": {'description': 'A regulatory region initiating transcription', 'meaning': 'SO:0000167'},
    "ENHANCER": {'description': 'A cis-acting sequence that increases transcription', 'meaning': 'SO:0000165'},
    "SILENCER": {'description': 'A regulatory region which upon binding of transcription factors, suppresses transcription', 'meaning': 'SO:0000625'},
    "TERMINATOR": {'description': 'The sequence of DNA located either at the end of the transcript that causes RNA polymerase to terminate transcription', 'meaning': 'SO:0000141'},
    "ATTENUATOR": {'description': 'A sequence that causes transcription termination', 'meaning': 'SO:0000140'},
    "POLYA_SIGNAL_SEQUENCE": {'description': 'The recognition sequence for the cleavage and polyadenylation machinery', 'meaning': 'SO:0000551'},
    "BINDING_SITE": {'description': 'A region on a molecule that binds to another molecule', 'meaning': 'SO:0000409'},
    "TFBS": {'description': 'Transcription factor binding site', 'meaning': 'SO:0000235'},
    "RIBOSOME_ENTRY_SITE": {'description': 'Region where ribosome assembles on mRNA', 'meaning': 'SO:0000139'},
    "POLYA_SITE": {'description': 'Polyadenylation site', 'meaning': 'SO:0000553'},
    "REPEAT_REGION": {'description': 'A region of sequence containing one or more repeat units', 'meaning': 'SO:0000657'},
    "DISPERSED_REPEAT": {'description': 'A repeat that is interspersed in the genome', 'meaning': 'SO:0000658'},
    "TANDEM_REPEAT": {'description': 'A repeat where the same sequence is repeated in the same orientation', 'meaning': 'SO:0000705'},
    "INVERTED_REPEAT": {'description': 'A repeat where the sequence is repeated in the opposite orientation', 'meaning': 'SO:0000294'},
    "TRANSPOSABLE_ELEMENT": {'description': 'A DNA segment that can change its position within the genome', 'meaning': 'SO:0000101'},
    "MOBILE_ELEMENT": {'description': 'A nucleotide region with the ability to move from one place in the genome to another', 'meaning': 'SO:0001037'},
    "SEQUENCE_ALTERATION": {'description': 'A sequence that deviates from the reference sequence', 'meaning': 'SO:0001059'},
    "INSERTION": {'description': 'The sequence of one or more nucleotides added between two adjacent nucleotides', 'meaning': 'SO:0000667'},
    "DELETION": {'description': 'The removal of a sequences of nucleotides from the genome', 'meaning': 'SO:0000159'},
    "INVERSION": {'description': 'A continuous nucleotide sequence is inverted in the same position', 'meaning': 'SO:1000036'},
    "DUPLICATION": {'description': 'One or more nucleotides are added between two adjacent nucleotides', 'meaning': 'SO:1000035'},
    "SUBSTITUTION": {'description': 'A sequence alteration where one nucleotide replaced by another', 'meaning': 'SO:1000002'},
    "ORIGIN_OF_REPLICATION": {'description': 'The origin of replication; starting site for duplication of a nucleic acid molecule', 'meaning': 'SO:0000296'},
    "POLYC_TRACT": {'description': 'A sequence of Cs'},
    "GAP": {'description': 'A gap in the sequence', 'meaning': 'SO:0000730'},
    "ASSEMBLY_GAP": {'description': 'A gap between two sequences in an assembly', 'meaning': 'SO:0000730'},
    "CHROMOSOME": {'description': 'Structural unit composed of DNA and proteins', 'meaning': 'SO:0000340'},
    "SUPERCONTIG": {'description': 'One or more contigs that have been ordered and oriented using end-read information', 'meaning': 'SO:0000148'},
    "CONTIG": {'description': 'A contiguous sequence derived from sequence assembly', 'meaning': 'SO:0000149'},
    "SCAFFOLD": {'description': 'One or more contigs that have been ordered and oriented', 'meaning': 'SO:0000148'},
    "CLONE": {'description': 'A piece of DNA that has been inserted into a vector', 'meaning': 'SO:0000151'},
    "PLASMID": {'description': 'A self-replicating circular DNA molecule', 'meaning': 'SO:0000155'},
    "POLYPEPTIDE": {'description': 'A sequence of amino acids linked by peptide bonds', 'meaning': 'SO:0000104'},
    "MATURE_PROTEIN_REGION": {'description': 'The polypeptide sequence that remains after post-translational processing', 'meaning': 'SO:0000419'},
    "SIGNAL_PEPTIDE": {'description': 'A peptide region that targets a polypeptide to a specific location', 'meaning': 'SO:0000418'},
    "TRANSIT_PEPTIDE": {'description': 'A peptide that directs the transport of a protein to an organelle', 'meaning': 'SO:0000725'},
    "PROPEPTIDE": {'description': 'A peptide region that is cleaved during maturation', 'meaning': 'SO:0001062'},
    "OPERON": {'description': 'A group of contiguous genes transcribed as a single unit', 'meaning': 'SO:0000178'},
    "STEM_LOOP": {'description': 'A double-helical region formed by base-pairing between adjacent sequences', 'meaning': 'SO:0000313'},
    "D_LOOP": {'description': 'Displacement loop; a region where DNA is displaced by an invading strand', 'meaning': 'SO:0000297'},
    "MATCH": {'description': 'A region of sequence similarity', 'meaning': 'SO:0000343'},
    "CDNA_MATCH": {'description': 'A match to a cDNA sequence', 'meaning': 'SO:0000689'},
    "EST_MATCH": {'description': 'A match to an EST sequence', 'meaning': 'SO:0000668'},
    "PROTEIN_MATCH": {'description': 'A match to a protein sequence', 'meaning': 'SO:0000349'},
    "NUCLEOTIDE_MATCH": {'description': 'A match to a nucleotide sequence', 'meaning': 'SO:0000347'},
    "JUNCTION_FEATURE": {'description': 'A boundary or junction between sequence regions', 'meaning': 'SO:0000699'},
    "SPLICE_SITE": {'description': 'The position where intron is excised', 'meaning': 'SO:0000162'},
    "FIVE_PRIME_SPLICE_SITE": {'description': "The 5' splice site (donor site)", 'meaning': 'SO:0000163'},
    "THREE_PRIME_SPLICE_SITE": {'description': "The 3' splice site (acceptor site)", 'meaning': 'SO:0000164'},
    "START_CODON": {'description': 'The first codon to be translated', 'meaning': 'SO:0000318'},
    "STOP_CODON": {'description': 'The codon that terminates translation', 'meaning': 'SO:0000319'},
    "CENTROMERE": {'description': 'A region where chromatids are held together', 'meaning': 'SO:0000577'},
    "TELOMERE": {'description': 'The terminal region of a linear chromosome', 'meaning': 'SO:0000624'},
}

__all__ = [
    "GenomeFeatureType",
]