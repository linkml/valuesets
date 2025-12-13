"""
ICD-O Cancer Classification Value Sets

Value sets based on the International Classification of Diseases for Oncology (ICD-O) bi-axial classification system. ICD-O uses two independent axes: topography (anatomic site) and morphology (histological type and behavior).

Generated from: medical/oncology/icdo.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class TumorTopography(RichEnum):
    """
    Major anatomic sites for tumor classification based on ICD-O topography codes (C00-C80). These represent primary sites where neoplasms occur.
    """
    # Enum members
    LIP_ORAL_CAVITY_PHARYNX = "LIP_ORAL_CAVITY_PHARYNX"
    DIGESTIVE_ORGANS = "DIGESTIVE_ORGANS"
    ESOPHAGUS = "ESOPHAGUS"
    STOMACH = "STOMACH"
    COLON = "COLON"
    RECTUM = "RECTUM"
    LIVER = "LIVER"
    PANCREAS = "PANCREAS"
    RESPIRATORY_INTRATHORACIC = "RESPIRATORY_INTRATHORACIC"
    LUNG = "LUNG"
    BONE_ARTICULAR_CARTILAGE = "BONE_ARTICULAR_CARTILAGE"
    SKIN = "SKIN"
    SOFT_TISSUE = "SOFT_TISSUE"
    BREAST = "BREAST"
    FEMALE_GENITAL = "FEMALE_GENITAL"
    CERVIX_UTERI = "CERVIX_UTERI"
    OVARY = "OVARY"
    MALE_GENITAL = "MALE_GENITAL"
    PROSTATE = "PROSTATE"
    TESTIS = "TESTIS"
    URINARY_TRACT = "URINARY_TRACT"
    KIDNEY = "KIDNEY"
    BLADDER = "BLADDER"
    EYE_BRAIN_CNS = "EYE_BRAIN_CNS"
    BRAIN = "BRAIN"
    THYROID_ENDOCRINE = "THYROID_ENDOCRINE"
    THYROID = "THYROID"
    LYMPH_NODES = "LYMPH_NODES"
    UNKNOWN_PRIMARY = "UNKNOWN_PRIMARY"

# Set metadata after class creation
TumorTopography._metadata = {
    "LIP_ORAL_CAVITY_PHARYNX": {'description': 'Malignant neoplasms of lip, oral cavity and pharynx (C00-C14)', 'annotations': {'icdo_range': 'C00-C14'}},
    "DIGESTIVE_ORGANS": {'description': 'Malignant neoplasms of digestive organs (C15-C26)', 'annotations': {'icdo_range': 'C15-C26'}},
    "ESOPHAGUS": {'description': 'Malignant neoplasm of esophagus (C15)', 'annotations': {'icdo_code': 'C15', 'uberon': 'UBERON:0001043'}},
    "STOMACH": {'description': 'Malignant neoplasm of stomach (C16)', 'annotations': {'icdo_code': 'C16', 'uberon': 'UBERON:0000945'}},
    "COLON": {'description': 'Malignant neoplasm of colon (C18)', 'annotations': {'icdo_code': 'C18', 'uberon': 'UBERON:0001155'}},
    "RECTUM": {'description': 'Malignant neoplasm of rectum (C20)', 'annotations': {'icdo_code': 'C20', 'uberon': 'UBERON:0001052'}},
    "LIVER": {'description': 'Malignant neoplasm of liver and intrahepatic bile ducts (C22)', 'annotations': {'icdo_code': 'C22', 'uberon': 'UBERON:0002107'}},
    "PANCREAS": {'description': 'Malignant neoplasm of pancreas (C25)', 'annotations': {'icdo_code': 'C25', 'uberon': 'UBERON:0001264'}},
    "RESPIRATORY_INTRATHORACIC": {'description': 'Malignant neoplasms of respiratory and intrathoracic organs (C30-C39)', 'annotations': {'icdo_range': 'C30-C39'}},
    "LUNG": {'description': 'Malignant neoplasm of bronchus and lung (C34)', 'annotations': {'icdo_code': 'C34', 'uberon': 'UBERON:0002048'}},
    "BONE_ARTICULAR_CARTILAGE": {'description': 'Malignant neoplasms of bone and articular cartilage (C40-C41)', 'annotations': {'icdo_range': 'C40-C41'}},
    "SKIN": {'description': 'Melanoma and other malignant neoplasms of skin (C43-C44)', 'annotations': {'icdo_range': 'C43-C44', 'uberon': 'UBERON:0002097'}},
    "SOFT_TISSUE": {'description': 'Malignant neoplasms of mesothelial and soft tissues (C45-C49)', 'annotations': {'icdo_range': 'C45-C49'}},
    "BREAST": {'description': 'Malignant neoplasm of breast (C50)', 'annotations': {'icdo_code': 'C50', 'uberon': 'UBERON:0000310'}},
    "FEMALE_GENITAL": {'description': 'Malignant neoplasms of female genital organs (C51-C58)', 'annotations': {'icdo_range': 'C51-C58'}},
    "CERVIX_UTERI": {'description': 'Malignant neoplasm of cervix uteri (C53)', 'annotations': {'icdo_code': 'C53'}},
    "OVARY": {'description': 'Malignant neoplasm of ovary (C56)', 'annotations': {'icdo_code': 'C56', 'uberon': 'UBERON:0000992'}},
    "MALE_GENITAL": {'description': 'Malignant neoplasms of male genital organs (C60-C63)', 'annotations': {'icdo_range': 'C60-C63'}},
    "PROSTATE": {'description': 'Malignant neoplasm of prostate (C61)', 'annotations': {'icdo_code': 'C61', 'uberon': 'UBERON:0002367'}},
    "TESTIS": {'description': 'Malignant neoplasm of testis (C62)', 'annotations': {'icdo_code': 'C62', 'uberon': 'UBERON:0000473'}},
    "URINARY_TRACT": {'description': 'Malignant neoplasms of urinary tract (C64-C68)', 'annotations': {'icdo_range': 'C64-C68'}},
    "KIDNEY": {'description': 'Malignant neoplasm of kidney (C64)', 'annotations': {'icdo_code': 'C64', 'uberon': 'UBERON:0002113'}},
    "BLADDER": {'description': 'Malignant neoplasm of bladder (C67)', 'annotations': {'icdo_code': 'C67', 'uberon': 'UBERON:0001255'}},
    "EYE_BRAIN_CNS": {'description': 'Malignant neoplasms of eye, brain and other parts of CNS (C69-C72)', 'annotations': {'icdo_range': 'C69-C72'}},
    "BRAIN": {'description': 'Malignant neoplasm of brain (C71)', 'annotations': {'icdo_code': 'C71', 'uberon': 'UBERON:0000955'}},
    "THYROID_ENDOCRINE": {'description': 'Malignant neoplasms of thyroid and other endocrine glands (C73-C75)', 'annotations': {'icdo_range': 'C73-C75'}},
    "THYROID": {'description': 'Malignant neoplasm of thyroid gland (C73)', 'annotations': {'icdo_code': 'C73', 'uberon': 'UBERON:0002046'}},
    "LYMPH_NODES": {'description': 'Malignant neoplasms of lymph nodes (C77)', 'annotations': {'icdo_code': 'C77'}},
    "UNKNOWN_PRIMARY": {'description': 'Malignant neoplasm of unknown primary site (C80)', 'annotations': {'icdo_code': 'C80'}},
}

class TumorMorphology(RichEnum):
    """
    Major histological types for tumor classification based on ICD-O morphology codes. These represent the cell type and histological pattern of neoplasms.
    """
    # Enum members
    CARCINOMA_NOS = "CARCINOMA_NOS"
    ADENOCARCINOMA_NOS = "ADENOCARCINOMA_NOS"
    SQUAMOUS_CELL_CARCINOMA = "SQUAMOUS_CELL_CARCINOMA"
    TRANSITIONAL_CELL_CARCINOMA = "TRANSITIONAL_CELL_CARCINOMA"
    SMALL_CELL_CARCINOMA = "SMALL_CELL_CARCINOMA"
    LARGE_CELL_CARCINOMA = "LARGE_CELL_CARCINOMA"
    SARCOMA_NOS = "SARCOMA_NOS"
    OSTEOSARCOMA = "OSTEOSARCOMA"
    CHONDROSARCOMA = "CHONDROSARCOMA"
    LIPOSARCOMA = "LIPOSARCOMA"
    LEIOMYOSARCOMA = "LEIOMYOSARCOMA"
    RHABDOMYOSARCOMA = "RHABDOMYOSARCOMA"
    LYMPHOMA_NOS = "LYMPHOMA_NOS"
    HODGKIN_LYMPHOMA = "HODGKIN_LYMPHOMA"
    NON_HODGKIN_LYMPHOMA = "NON_HODGKIN_LYMPHOMA"
    DIFFUSE_LARGE_B_CELL_LYMPHOMA = "DIFFUSE_LARGE_B_CELL_LYMPHOMA"
    LEUKEMIA_NOS = "LEUKEMIA_NOS"
    ACUTE_LYMPHOBLASTIC_LEUKEMIA = "ACUTE_LYMPHOBLASTIC_LEUKEMIA"
    ACUTE_MYELOID_LEUKEMIA = "ACUTE_MYELOID_LEUKEMIA"
    CHRONIC_LYMPHOCYTIC_LEUKEMIA = "CHRONIC_LYMPHOCYTIC_LEUKEMIA"
    CHRONIC_MYELOID_LEUKEMIA = "CHRONIC_MYELOID_LEUKEMIA"
    MELANOMA = "MELANOMA"
    MESOTHELIOMA = "MESOTHELIOMA"
    GERM_CELL_TUMOR = "GERM_CELL_TUMOR"
    NEUROENDOCRINE_TUMOR = "NEUROENDOCRINE_TUMOR"

# Set metadata after class creation
TumorMorphology._metadata = {
    "CARCINOMA_NOS": {'description': 'Malignant epithelial neoplasm, not otherwise specified. General term for cancers arising from epithelial cells.', 'meaning': 'NCIT:C2916', 'annotations': {'icdo_code': 8010}},
    "ADENOCARCINOMA_NOS": {'description': 'Malignant glandular epithelial neoplasm. Cancer arising from glandular epithelium.', 'meaning': 'NCIT:C2852', 'annotations': {'icdo_code': 8140}},
    "SQUAMOUS_CELL_CARCINOMA": {'description': 'Malignant neoplasm arising from squamous epithelium. Common in skin, lung, esophagus, and cervix.', 'meaning': 'NCIT:C2929', 'annotations': {'icdo_code': 8070}},
    "TRANSITIONAL_CELL_CARCINOMA": {'description': 'Malignant neoplasm arising from transitional epithelium (urothelium). Most common in bladder and urinary tract.', 'meaning': 'NCIT:C2930', 'annotations': {'icdo_code': 8120}},
    "SMALL_CELL_CARCINOMA": {'description': 'Highly malignant neuroendocrine carcinoma with small cells. Most common in lung.', 'meaning': 'NCIT:C3915', 'annotations': {'icdo_code': 8041}},
    "LARGE_CELL_CARCINOMA": {'description': 'Undifferentiated carcinoma with large cells.', 'annotations': {'icdo_code': 8012}},
    "SARCOMA_NOS": {'description': 'Malignant mesenchymal neoplasm, not otherwise specified. Cancers arising from connective tissue, bone, cartilage, fat, muscle, or blood vessels.', 'meaning': 'NCIT:C9118', 'annotations': {'icdo_code': 8800}},
    "OSTEOSARCOMA": {'description': 'Malignant bone-forming tumor. Most common primary malignant bone tumor.', 'meaning': 'NCIT:C9145', 'annotations': {'icdo_code': 9180}},
    "CHONDROSARCOMA": {'description': 'Malignant cartilage-forming tumor.', 'meaning': 'NCIT:C2946', 'annotations': {'icdo_code': 9220}},
    "LIPOSARCOMA": {'description': 'Malignant tumor arising from adipose tissue.', 'meaning': 'NCIT:C3194', 'annotations': {'icdo_code': 8850}},
    "LEIOMYOSARCOMA": {'description': 'Malignant tumor arising from smooth muscle.', 'meaning': 'NCIT:C3158', 'annotations': {'icdo_code': 8890}},
    "RHABDOMYOSARCOMA": {'description': 'Malignant tumor arising from skeletal muscle.', 'meaning': 'NCIT:C3359', 'annotations': {'icdo_code': 8900}},
    "LYMPHOMA_NOS": {'description': 'Malignant neoplasm of lymphoid tissue, not otherwise specified. Includes Hodgkin and non-Hodgkin lymphomas.', 'meaning': 'NCIT:C3208', 'annotations': {'icdo_code': 9590}},
    "HODGKIN_LYMPHOMA": {'description': 'Lymphoma characterized by presence of Reed-Sternberg cells and specific histological patterns.', 'meaning': 'NCIT:C9357', 'annotations': {'icdo_code': 9650}},
    "NON_HODGKIN_LYMPHOMA": {'description': 'All lymphomas other than Hodgkin lymphoma. Includes B-cell and T-cell lymphomas.', 'meaning': 'NCIT:C3211', 'annotations': {'icdo_codes': '9591, 9670-9729'}},
    "DIFFUSE_LARGE_B_CELL_LYMPHOMA": {'description': 'Most common type of non-Hodgkin lymphoma.', 'meaning': 'NCIT:C8851', 'annotations': {'icdo_code': 9680}},
    "LEUKEMIA_NOS": {'description': 'Malignant neoplasm of blood-forming tissues, not otherwise specified.', 'meaning': 'NCIT:C3161', 'annotations': {'icdo_code': 9800}},
    "ACUTE_LYMPHOBLASTIC_LEUKEMIA": {'description': 'Acute leukemia of lymphoid precursor cells.', 'meaning': 'NCIT:C3167', 'annotations': {'icdo_code': 9811}},
    "ACUTE_MYELOID_LEUKEMIA": {'description': 'Acute leukemia of myeloid precursor cells.', 'meaning': 'NCIT:C3171', 'annotations': {'icdo_code': 9861}},
    "CHRONIC_LYMPHOCYTIC_LEUKEMIA": {'description': 'Chronic leukemia of mature B lymphocytes.', 'meaning': 'NCIT:C3163', 'annotations': {'icdo_code': 9823}},
    "CHRONIC_MYELOID_LEUKEMIA": {'description': 'Chronic leukemia characterized by BCR-ABL1 fusion gene.', 'meaning': 'NCIT:C3174', 'annotations': {'icdo_code': 9875}},
    "MELANOMA": {'description': 'Malignant neoplasm arising from melanocytes.', 'meaning': 'NCIT:C3224', 'annotations': {'icdo_code': 8720}},
    "MESOTHELIOMA": {'description': 'Malignant tumor arising from mesothelial cells lining pleura, peritoneum, or pericardium. Strongly associated with asbestos exposure.', 'meaning': 'NCIT:C3234', 'annotations': {'icdo_code': 9050}},
    "GERM_CELL_TUMOR": {'description': 'Tumor arising from germ cells. Includes seminoma, teratoma, etc.', 'meaning': 'NCIT:C3708', 'annotations': {'icdo_codes': '9060-9110'}},
    "NEUROENDOCRINE_TUMOR": {'description': 'Tumor arising from neuroendocrine cells.', 'annotations': {'icdo_codes': '8240-8249'}},
}

class TumorBehavior(RichEnum):
    """
    Biological behavior codes used in ICD-O morphology (5th digit). Indicates whether a neoplasm is benign, uncertain, in situ, or malignant.
    """
    # Enum members
    BENIGN = "BENIGN"
    UNCERTAIN_BORDERLINE = "UNCERTAIN_BORDERLINE"
    IN_SITU = "IN_SITU"
    MALIGNANT_PRIMARY = "MALIGNANT_PRIMARY"
    MALIGNANT_METASTATIC = "MALIGNANT_METASTATIC"
    MALIGNANT_UNCERTAIN_PRIMARY_METASTATIC = "MALIGNANT_UNCERTAIN_PRIMARY_METASTATIC"

# Set metadata after class creation
TumorBehavior._metadata = {
    "BENIGN": {'description': 'Non-cancerous neoplasm that does not invade surrounding tissue or metastasize.', 'meaning': 'NCIT:C3677', 'annotations': {'icdo_behavior': '/0'}},
    "UNCERTAIN_BORDERLINE": {'description': 'Neoplasm with borderline malignancy or uncertain behavior. May recur but typically does not metastasize.', 'annotations': {'icdo_behavior': '/1'}},
    "IN_SITU": {'description': 'Malignant cells confined to epithelium without invasion through basement membrane. Pre-invasive cancer.', 'meaning': 'NCIT:C2917', 'annotations': {'icdo_behavior': '/2'}},
    "MALIGNANT_PRIMARY": {'description': 'Invasive malignant neoplasm at primary site. Cancer that has invaded through basement membrane.', 'annotations': {'icdo_behavior': '/3'}},
    "MALIGNANT_METASTATIC": {'description': 'Malignant neoplasm that has spread from primary site to secondary (metastatic) site.', 'annotations': {'icdo_behavior': '/6'}},
    "MALIGNANT_UNCERTAIN_PRIMARY_METASTATIC": {'description': 'Malignant neoplasm where it is uncertain if this is the primary site or a metastatic site.', 'annotations': {'icdo_behavior': '/9'}},
}

class TumorGrade(RichEnum):
    """
    Histological grade/differentiation codes used in ICD-O (6th digit). Indicates how abnormal the tumor cells appear compared to normal cells.
    """
    # Enum members
    GRADE_1 = "GRADE_1"
    GRADE_2 = "GRADE_2"
    GRADE_3 = "GRADE_3"
    GRADE_4 = "GRADE_4"
    GRADE_NOT_DETERMINED = "GRADE_NOT_DETERMINED"
    T_CELL = "T_CELL"
    B_CELL = "B_CELL"
    NULL_CELL = "NULL_CELL"
    NK_CELL = "NK_CELL"

# Set metadata after class creation
TumorGrade._metadata = {
    "GRADE_1": {'description': 'Tumor cells closely resemble normal cells. Typically slow-growing with better prognosis.', 'annotations': {'icdo_grade': 1, 'differentiation': 'well differentiated'}},
    "GRADE_2": {'description': 'Tumor cells show moderate resemblance to normal cells. Intermediate behavior.', 'annotations': {'icdo_grade': 2, 'differentiation': 'moderately differentiated'}},
    "GRADE_3": {'description': 'Tumor cells show little resemblance to normal cells. More aggressive with poorer prognosis.', 'annotations': {'icdo_grade': 3, 'differentiation': 'poorly differentiated'}},
    "GRADE_4": {'description': 'Tumor cells bear no resemblance to normal cells. Most aggressive with poorest prognosis.', 'annotations': {'icdo_grade': 4, 'differentiation': 'undifferentiated, anaplastic'}},
    "GRADE_NOT_DETERMINED": {'description': 'Histological grade has not been assessed or is not applicable.', 'annotations': {'icdo_grade': 9}},
    "T_CELL": {'description': 'Lymphoma/leukemia of T-cell origin.', 'annotations': {'icdo_grade': 5, 'use': 'lymphomas/leukemias'}},
    "B_CELL": {'description': 'Lymphoma/leukemia of B-cell origin.', 'annotations': {'icdo_grade': 6, 'use': 'lymphomas/leukemias'}},
    "NULL_CELL": {'description': 'Lymphoma/leukemia of neither T-cell nor B-cell origin.', 'annotations': {'icdo_grade': 7, 'use': 'lymphomas/leukemias'}},
    "NK_CELL": {'description': 'Lymphoma/leukemia of natural killer cell origin.', 'annotations': {'icdo_grade': 8, 'use': 'lymphomas/leukemias'}},
}

__all__ = [
    "TumorTopography",
    "TumorMorphology",
    "TumorBehavior",
    "TumorGrade",
]