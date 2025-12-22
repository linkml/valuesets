"""
Pediatric Oncology Diagnosis Categories

High-level pediatric cancer diagnosis groupings based on CCDI CDE 16607972 (Diagnosis Pediatric Oncology Grouping Category). These categories were developed through consensus by St. Jude, CBTN, Treehouse, and NCI to enable cohort aggregation across federated pediatric cancer data resources. Categories are aligned with WHO CNS5, WHO-HAEM5, and WHO Pediatric Blue Book.

Generated from: medical/pediatric_oncology/diagnosis_categories.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class PediatricOncologyDiagnosisCategory(RichEnum):
    """
    High-level groupings for pediatric cancer diagnoses per CCDI CDE 16607972. Designed for cohort aggregation across federated data resources. Each diagnosis maps to a single dominant category.
    """
    # Enum members
    ATYPICAL_TERATOID_RHABDOID_TUMOR = "ATYPICAL_TERATOID_RHABDOID_TUMOR"
    CHOROID_PLEXUS_TUMOR = "CHOROID_PLEXUS_TUMOR"
    CNS_GERM_CELL_TUMOR = "CNS_GERM_CELL_TUMOR"
    CNS_SARCOMA = "CNS_SARCOMA"
    CRANIOPHARYNGIOMA = "CRANIOPHARYNGIOMA"
    EPENDYMOMA = "EPENDYMOMA"
    GLIONEURONAL_AND_NEURONAL_TUMOR = "GLIONEURONAL_AND_NEURONAL_TUMOR"
    HIGH_GRADE_GLIOMA = "HIGH_GRADE_GLIOMA"
    LOW_GRADE_GLIOMA = "LOW_GRADE_GLIOMA"
    MEDULLOBLASTOMA = "MEDULLOBLASTOMA"
    OTHER_CNS_EMBRYONAL_TUMOR = "OTHER_CNS_EMBRYONAL_TUMOR"
    OTHER_GLIOMA = "OTHER_GLIOMA"
    OTHER_BRAIN_TUMOR = "OTHER_BRAIN_TUMOR"
    LYMPHOBLASTIC_LEUKEMIA = "LYMPHOBLASTIC_LEUKEMIA"
    MYELOID_LEUKEMIA = "MYELOID_LEUKEMIA"
    HODGKIN_LYMPHOMA = "HODGKIN_LYMPHOMA"
    NON_HODGKIN_LYMPHOMA = "NON_HODGKIN_LYMPHOMA"
    LYMPHOPROLIFERATIVE_DISEASE = "LYMPHOPROLIFERATIVE_DISEASE"
    OTHER_HEME_TUMOR = "OTHER_HEME_TUMOR"
    NEUROBLASTOMA = "NEUROBLASTOMA"
    OSTEOSARCOMA = "OSTEOSARCOMA"
    EWING_SARCOMA = "EWING_SARCOMA"
    RHABDOMYOSARCOMA = "RHABDOMYOSARCOMA"
    SOFT_TISSUE_TUMOR = "SOFT_TISSUE_TUMOR"
    RHABDOID_TUMOR = "RHABDOID_TUMOR"
    RENAL_TUMOR = "RENAL_TUMOR"
    RETINOBLASTOMA = "RETINOBLASTOMA"
    GERM_CELL_TUMOR = "GERM_CELL_TUMOR"
    ENDOCRINE_AND_NEUROENDOCRINE_TUMOR = "ENDOCRINE_AND_NEUROENDOCRINE_TUMOR"
    OTHER_SOLID_TUMOR = "OTHER_SOLID_TUMOR"

# Set metadata after class creation
PediatricOncologyDiagnosisCategory._metadata = {
    "ATYPICAL_TERATOID_RHABDOID_TUMOR": {'description': 'Highly malignant embryonal CNS tumor characterized by loss of SMARCB1 (INI1) or SMARCA4 expression. Predominantly occurs in young children.', 'meaning': 'NCIT:C6906', 'annotations': {'category': 'brain_tumor', 'who_classification': 'WHO CNS5'}},
    "CHOROID_PLEXUS_TUMOR": {'description': 'Neoplasms arising from the choroid plexus epithelium, including papilloma, atypical papilloma, and carcinoma.', 'meaning': 'NCIT:C3473', 'annotations': {'category': 'brain_tumor', 'who_classification': 'WHO CNS5'}},
    "CNS_GERM_CELL_TUMOR": {'description': 'Germ cell tumors arising within the central nervous system, including germinoma and non-germinomatous germ cell tumors.', 'meaning': 'NCIT:C5461', 'annotations': {'category': 'brain_tumor', 'who_classification': 'WHO CNS5'}},
    "CNS_SARCOMA": {'description': 'Sarcomas arising primarily in the central nervous system, including Ewing sarcoma and rhabdomyosarcoma of CNS.', 'meaning': 'NCIT:C5153', 'annotations': {'category': 'brain_tumor'}},
    "CRANIOPHARYNGIOMA": {'description': 'Benign epithelial tumors arising from remnants of Rathke pouch, including adamantinomatous and papillary subtypes.', 'meaning': 'NCIT:C2964', 'annotations': {'category': 'brain_tumor', 'who_classification': 'WHO CNS5'}},
    "EPENDYMOMA": {'description': 'Glial tumors arising from ependymal cells lining the ventricular system and central canal. Includes molecular subtypes defined by WHO CNS5.', 'meaning': 'NCIT:C3017', 'annotations': {'category': 'brain_tumor', 'who_classification': 'WHO CNS5'}},
    "GLIONEURONAL_AND_NEURONAL_TUMOR": {'description': 'Tumors with neuronal differentiation including ganglioglioma, dysembryoplastic neuroepithelial tumor (DNET), and central neurocytoma.', 'meaning': 'NCIT:C4747', 'annotations': {'category': 'brain_tumor', 'who_classification': 'WHO CNS5'}},
    "HIGH_GRADE_GLIOMA": {'description': 'Aggressive glial tumors including pediatric-type diffuse high-grade gliomas (H3 K27-altered, H3 G34-mutant, and H3/IDH-wildtype), as well as glioblastoma.', 'meaning': 'NCIT:C4822', 'annotations': {'category': 'brain_tumor', 'who_classification': 'WHO CNS5', 'grade': 'high'}},
    "LOW_GRADE_GLIOMA": {'description': 'Indolent glial tumors including pilocytic astrocytoma and pediatric-type diffuse low-grade gliomas (MYB/MYBL1-altered, MAPK pathway-altered).', 'meaning': 'NCIT:C132067', 'annotations': {'category': 'brain_tumor', 'who_classification': 'WHO CNS5', 'grade': 'low'}},
    "MEDULLOBLASTOMA": {'description': 'Embryonal tumor of the cerebellum, classified by molecular subgroups (WNT-activated, SHH-activated, Group 3, Group 4) per WHO CNS5.', 'meaning': 'NCIT:C3222', 'annotations': {'category': 'brain_tumor', 'who_classification': 'WHO CNS5'}},
    "OTHER_CNS_EMBRYONAL_TUMOR": {'description': 'Embryonal tumors of the CNS other than medulloblastoma and ATRT, including embryonal tumor with multilayered rosettes (ETMR), CNS neuroblastoma, and pineoblastoma.', 'meaning': 'NCIT:C6990', 'annotations': {'category': 'brain_tumor', 'who_classification': 'WHO CNS5'}, 'aliases': ['CNS Embryonal Tumor, NOS']},
    "OTHER_GLIOMA": {'description': 'Glial tumors not classified as high-grade or low-grade glioma, including angiocentric glioma and astroblastoma.', 'meaning': 'NCIT:C3059', 'annotations': {'category': 'brain_tumor'}},
    "OTHER_BRAIN_TUMOR": {'description': 'CNS tumors not fitting other brain tumor categories, including meningioma, schwannoma, and hemangioblastoma.', 'meaning': 'NCIT:C2907', 'annotations': {'category': 'brain_tumor'}},
    "LYMPHOBLASTIC_LEUKEMIA": {'description': 'Acute lymphoblastic leukemia (ALL) including B-ALL and T-ALL with all molecular subtypes (BCR::ABL1, ETV6::RUNX1, KMT2A-r, DUX4, MEF2D, etc.).', 'meaning': 'NCIT:C3167', 'annotations': {'category': 'hematologic', 'who_classification': 'WHO-HAEM5'}, 'aliases': ['ALL', 'Acute Lymphoblastic Leukemia']},
    "MYELOID_LEUKEMIA": {'description': 'Acute myeloid leukemia (AML) and related myeloid neoplasms including AML with defining genetic abnormalities, therapy-related AML, and juvenile myelomonocytic leukemia (JMML).', 'meaning': 'NCIT:C3171', 'annotations': {'category': 'hematologic', 'who_classification': 'WHO-HAEM5'}, 'aliases': ['AML', 'Acute Myeloid Leukemia']},
    "HODGKIN_LYMPHOMA": {'description': 'Lymphoid neoplasm characterized by Reed-Sternberg cells, including classical Hodgkin lymphoma and nodular lymphocyte predominant Hodgkin lymphoma.', 'meaning': 'NCIT:C9357', 'annotations': {'category': 'hematologic', 'who_classification': 'WHO-HAEM5'}},
    "NON_HODGKIN_LYMPHOMA": {'description': 'Lymphoid neoplasms other than Hodgkin lymphoma, including Burkitt lymphoma, diffuse large B-cell lymphoma, anaplastic large cell lymphoma, and lymphoblastic lymphoma.', 'meaning': 'NCIT:C3211', 'annotations': {'category': 'hematologic', 'who_classification': 'WHO-HAEM5'}, 'aliases': ['NHL']},
    "LYMPHOPROLIFERATIVE_DISEASE": {'description': 'Disorders characterized by abnormal lymphocyte proliferation, including post-transplant lymphoproliferative disorder (PTLD) and hemophagocytic lymphohistiocytosis (HLH).', 'meaning': 'NCIT:C9308', 'annotations': {'category': 'hematologic'}},
    "OTHER_HEME_TUMOR": {'description': 'Hematologic malignancies not classified elsewhere, including histiocytic disorders, myelodysplastic syndromes, and myeloproliferative neoplasms.', 'meaning': 'NCIT:C27134', 'annotations': {'category': 'hematologic'}},
    "NEUROBLASTOMA": {'description': 'Embryonal tumor of the peripheral sympathetic nervous system, arising from neural crest cells. Includes ganglioneuroblastoma and ganglioneuroma.', 'meaning': 'NCIT:C3270', 'annotations': {'category': 'solid_tumor', 'who_classification': 'WHO Pediatric Blue Book'}},
    "OSTEOSARCOMA": {'description': 'Primary malignant bone tumor characterized by osteoid production, including conventional, telangiectatic, and small cell variants.', 'meaning': 'NCIT:C9145', 'annotations': {'category': 'solid_tumor', 'who_classification': 'WHO Bone/Soft Tissue'}},
    "EWING_SARCOMA": {'description': 'Small round cell sarcoma typically harboring EWSR1 rearrangements, arising in bone or soft tissue. Includes Ewing sarcoma family of tumors.', 'meaning': 'NCIT:C4817', 'annotations': {'category': 'solid_tumor', 'who_classification': 'WHO Bone/Soft Tissue'}},
    "RHABDOMYOSARCOMA": {'description': 'Malignant soft tissue tumor with skeletal muscle differentiation, including embryonal, alveolar, and spindle cell/sclerosing subtypes.', 'meaning': 'NCIT:C3359', 'annotations': {'category': 'solid_tumor', 'who_classification': 'WHO Bone/Soft Tissue'}},
    "SOFT_TISSUE_TUMOR": {'description': 'Soft tissue neoplasms other than rhabdomyosarcoma and Ewing sarcoma, including synovial sarcoma, fibrosarcoma, and other sarcomas. Also includes non-sarcomatous soft tissue tumors.', 'meaning': 'NCIT:C9306', 'annotations': {'category': 'solid_tumor'}, 'aliases': ['Soft Tissue Sarcoma']},
    "RHABDOID_TUMOR": {'description': 'Highly aggressive tumors characterized by SMARCB1 loss, occurring outside the CNS (extracranial rhabdoid tumor). Includes malignant rhabdoid tumor of kidney.', 'meaning': 'NCIT:C3808', 'annotations': {'category': 'solid_tumor'}},
    "RENAL_TUMOR": {'description': 'Kidney tumors including Wilms tumor (nephroblastoma), clear cell sarcoma of kidney, renal cell carcinoma, and congenital mesoblastic nephroma.', 'meaning': 'NCIT:C7548', 'annotations': {'category': 'solid_tumor', 'who_classification': 'WHO Pediatric Blue Book'}, 'aliases': ['Kidney Tumor', 'Wilms Tumor', 'Renal Tumors']},
    "RETINOBLASTOMA": {'description': 'Malignant neoplasm of the retina arising from developing retinal cells, associated with RB1 mutations.', 'meaning': 'NCIT:C7541', 'annotations': {'category': 'solid_tumor', 'who_classification': 'WHO Pediatric Blue Book'}},
    "GERM_CELL_TUMOR": {'description': 'Tumors arising from primordial germ cells, occurring in gonadal or extragonadal sites. Includes teratoma, yolk sac tumor, germinoma, choriocarcinoma, and mixed germ cell tumors. Excludes CNS germ cell tumors.', 'meaning': 'NCIT:C3708', 'annotations': {'category': 'solid_tumor'}},
    "ENDOCRINE_AND_NEUROENDOCRINE_TUMOR": {'description': 'Tumors of endocrine glands and neuroendocrine cells, including thyroid carcinoma, adrenocortical carcinoma, pheochromocytoma, and paraganglioma.', 'meaning': 'NCIT:C3010', 'annotations': {'category': 'solid_tumor'}},
    "OTHER_SOLID_TUMOR": {'description': 'Solid tumors not classified elsewhere, including hepatoblastoma, pleuropulmonary blastoma, nasopharyngeal carcinoma, melanoma, and carcinomas.', 'meaning': 'NCIT:C9107', 'annotations': {'category': 'solid_tumor'}},
}

__all__ = [
    "PediatricOncologyDiagnosisCategory",
]