"""
Chemical Identifier Value Sets

Value sets for the identifier schemes used to reference chemical substances. Covers fields such as the PISCES Standard Flowsheet Format chemical registry_id ("CAS number or SMILES string").

Generated from: chemistry/identifiers.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ChemicalIdentifierScheme(RichEnum):
    """
    Schemes used to identify chemical substances, including registry numbers, line notations, structure-derived keys, and database accessions.
    """
    # Enum members
    CAS_RN = "CAS_RN"
    SMILES = "SMILES"
    INCHI = "INCHI"
    INCHIKEY = "INCHIKEY"
    IUPAC_NAME = "IUPAC_NAME"
    MOLECULAR_FORMULA = "MOLECULAR_FORMULA"
    PUBCHEM_CID = "PUBCHEM_CID"
    CHEBI_ID = "CHEBI_ID"
    KEGG_COMPOUND = "KEGG_COMPOUND"
    DRUGBANK_ID = "DRUGBANK_ID"
    EC_NUMBER = "EC_NUMBER"

# Set metadata after class creation
ChemicalIdentifierScheme._metadata = {
    "CAS_RN": {'description': 'CAS Registry Number assigned by the Chemical Abstracts Service', 'annotations': {'example': '64-17-5'}},
    "SMILES": {'description': 'Simplified Molecular-Input Line-Entry System structure notation', 'annotations': {'example': 'CCO'}},
    "INCHI": {'description': 'IUPAC International Chemical Identifier structure string', 'annotations': {'example': 'InChI=1S/C2H6O/c1-2-3/h3H,2H2,1H3'}},
    "INCHIKEY": {'description': 'Hashed fixed-length form of an InChI', 'annotations': {'example': 'LFQSCWFLJHTTHZ-UHFFFAOYSA-N'}},
    "IUPAC_NAME": {'description': 'Systematic IUPAC chemical name'},
    "MOLECULAR_FORMULA": {'description': 'Molecular or empirical chemical formula', 'annotations': {'example': 'C2H6O'}},
    "PUBCHEM_CID": {'description': 'PubChem Compound Identifier'},
    "CHEBI_ID": {'description': 'ChEBI ontology identifier'},
    "KEGG_COMPOUND": {'description': 'KEGG COMPOUND database accession'},
    "DRUGBANK_ID": {'description': 'DrugBank accession'},
    "EC_NUMBER": {'description': 'European Community (EINECS/EC) substance number'},
}

__all__ = [
    "ChemicalIdentifierScheme",
]