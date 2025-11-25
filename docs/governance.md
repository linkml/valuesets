# Governance and Stewardship

This document describes the governance model for value sets in this repository.

## Current Status

Most value sets in this repository are currently in **DRAFT** status. This means:

- They are functional and can be used in downstream applications
- They have not yet undergone formal review
- Their structure and content may change
- Community feedback is welcome and encouraged

## Source of Truth Model

Value sets in this repository fall into two categories:

### 1. Mirrored Value Sets (External Stewardship)

Some value sets are **mirrors** of authoritative definitions maintained by external organizations.
For these, the external organization is the Source of Truth (SoT), and this repository provides
a LinkML-compatible representation.

Examples include:

| Value Set | Steward | Source |
|-----------|---------|--------|
| GO Evidence Codes | [Gene Ontology Consortium](https://geneontology.org) | ECO mappings |
| Phenopackets Enums | [GA4GH Phenopackets](https://phenopackets.org) | Phenopacket Schema |
| INSDC Vocabularies | [Genomic Standards Consortium](https://gensc.org) | INSDC controlled vocabularies |

For mirrored value sets:

- Changes to the authoritative source should be reflected here
- Issues with the underlying definitions should be reported to the steward organization
- This repository tracks the `source` and `stewards` annotations for provenance

### 2. Community Value Sets (Internal Stewardship)

Some value sets are **originated and maintained** within this repository. For these,
this repository is the Source of Truth.

For community value sets:

- Stewardship is managed through working groups
- Changes follow the contribution and review process described below
- The goal is to mature these to STANDARD status through community review

## Maturity Levels

Value sets progress through maturity levels (defined in `StandardsMaturityLevel`):

| Status | Description |
|--------|-------------|
| `DRAFT` | Initial development, may change significantly |
| `WORKING_DRAFT` | Active work by a working group |
| `COMMITTEE_DRAFT` | Under formal review |
| `CANDIDATE_RECOMMENDATION` | Ready for implementation testing |
| `PROPOSED_STANDARD` | Stable, ready for adoption |
| `STANDARD` | Approved and published |
| `MATURE_STANDARD` | Well-established with wide adoption |
| `SUPERSEDED` | Replaced by a newer version |
| `WITHDRAWN` | No longer recommended |

## Stewardship Metadata

Each value set should include stewardship metadata:

```yaml
enums:
  MyValueSet:
    title: My Value Set
    description: Description of the value set
    status: DRAFT
    contributors:
      - orcid:0000-0000-0000-0000
    instantiates:
      - valuesets_meta:ValueSetEnumDefinitionWithStewardship
    annotations:
      stewards: https://example.org/steward
      publishers: https://example.org/publisher
```

### Stewardship Roles

Following [FHIR MetadataResource](https://build.fhir.org/metadataresource.html) patterns:

- **Stewards**: Organizations responsible for ongoing curation and maintenance
- **Publishers**: Organizations responsible for release and distribution
- **Endorsers**: Organizations that officially recommend the value set for adoption

## Contributing

### Proposing New Value Sets

1. Open an issue describing the value set and its use case
2. If accepted, submit a PR with the value set in DRAFT status
3. Include appropriate metadata (title, description, contributors)
4. Map permissible values to ontology terms where applicable

### Becoming a Steward

Stewards are responsible for:

- Reviewing proposed changes to value sets in their domain
- Ensuring value sets remain accurate and up-to-date
- Responding to community feedback and issues
- Coordinating with external stewards for mirrored value sets

To become a steward or join a working group:

**[Sign up here](https://example.org/valuesets-stewardship-signup)** (placeholder)

### Review Process

For value sets to advance from DRAFT to higher maturity levels:

1. **Working Group Review**: Domain experts review the value set
2. **Community Feedback**: Open period for community input
3. **Steward Approval**: Designated steward(s) approve the advancement
4. **Status Update**: PR to update the status field

## Governance Bodies

### Steering Committee

(To be established)

Responsibilities:
- Overall project governance
- Resolving disputes
- Approving new working groups

### Working Groups

Domain-specific working groups are responsible for value sets in their area:

| Domain | Working Group | Status |
|--------|---------------|--------|
| Bioinformatics | TBD | Planned |
| Clinical/Healthcare | TBD | Planned |
| Earth Sciences | TBD | Planned |

## Contact

- **Issues**: [GitHub Issues](https://github.com/linkml/valuesets/issues)
- **Discussions**: [GitHub Discussions](https://github.com/linkml/valuesets/discussions)
- **Stewardship Signup**: [Sign up form](https://example.org/valuesets-stewardship-signup)
