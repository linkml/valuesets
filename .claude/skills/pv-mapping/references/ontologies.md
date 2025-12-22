# Ontology Reference

## Domain to Ontology Mapping

| Domain | Ontology | Prefix |
|--------|----------|--------|
| Biological processes/functions | Gene Ontology | GO |
| Chemical entities | ChEBI | CHEBI |
| Biomedical concepts | NCI Thesaurus | NCIT |
| Experimental methods | OBI, CHMO | OBI, CHMO |
| Protein modifications | PSI-MOD | MOD |
| Imaging/microscopy | FBbi | FBbi |
| File formats | EDAM | EDAM |
| Diseases | MONDO, Disease Ontology | MONDO, DOID |
| Anatomy | Uberon | UBERON |
| Cell types | Cell Ontology | CL |
| Phenotypes | PATO | PATO |
| Environment/exposures | ECTO, ENVO | ECTO, ENVO |
| Units | UO, QUDT | UO, qudt |

## CURIE Format Patterns

| Ontology | Pattern | Example |
|----------|---------|---------|
| GO | `GO:NNNNNNN` | GO:0032991 |
| CHEBI | `CHEBI:NNNNN` | CHEBI:18154 |
| NCIT | `NCIT:CNNNNN` | NCIT:C706 |
| CHMO | `CHMO:NNNNNNN` | CHMO:0000698 |
| MOD | `MOD:NNNNN` | MOD:00033 |
| EDAM (formats) | `EDAM:format_NNNN` | EDAM:format_1476 |
| EDAM (data) | `EDAM:data_NNNN` | EDAM:data_2968 |
| FBbi | `FBbi:NNNNNNNN` | FBbi:00000399 |
| OBI | `OBI:NNNNNNN` | OBI:0001138 |
| UBERON | `UBERON:NNNNNNN` | UBERON:0000955 |
| CL | `CL:NNNNNNN` | CL:0000540 |
| PATO | `PATO:NNNNNNN` | PATO:0001340 |
| MONDO | `MONDO:NNNNNNN` | MONDO:0005015 |
| MESH | `MESH:DNNNNNN` | MESH:D056804 |

## OAK Commands

For complex ontology operations beyond OLS:

```bash
# Search
runoak -i sqlite:obo:go search "protein complex"

# Get term info
runoak -i sqlite:obo:go info GO:0032991

# Get ancestors
runoak -i sqlite:obo:go ancestors GO:0032991

# Get label
runoak -i sqlite:obo:go labels GO:0032991
```

Available OAK adapters: `sqlite:obo:<ontology>` for any OBO ontology (go, chebi, uberon, cl, etc.)
