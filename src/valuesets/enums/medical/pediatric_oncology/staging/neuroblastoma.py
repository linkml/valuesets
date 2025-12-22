"""
Neuroblastoma Staging Value Sets

Staging systems for neuroblastoma including the International Neuroblastoma Risk Group Staging System (INRGSS) and International Neuroblastoma Staging System (INSS). INRGSS is the current standard (effective 2024+) based on imaging and image-defined risk factors. INSS is the legacy surgical staging system still used for historical data.

Generated from: medical/pediatric_oncology/staging/neuroblastoma.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class INRGSSStage(RichEnum):
    """
    International Neuroblastoma Risk Group Staging System (INRGSS) stages. A clinical staging system based on imaging and image-defined risk factors (IDRFs), effective for diagnosis years 2024+. Allows staging before any treatment, unlike the surgical INSS system.
    """
    # Enum members
    L1 = "L1"
    L2 = "L2"
    M = "M"
    MS = "MS"

# Set metadata after class creation
INRGSSStage._metadata = {
    "L1": {'description': 'Localized tumor not involving vital structures as defined by the list of image-defined risk factors and confined to one body compartment (neck, chest, abdomen, or pelvis).', 'meaning': 'NCIT:C133428', 'annotations': {'localized': True, 'idrfs_present': False}},
    "L2": {'description': 'Locoregional tumor with presence of one or more image-defined risk factors. The tumor has not spread far from where it started but has at least one IDRF.', 'meaning': 'NCIT:C133429', 'annotations': {'localized': True, 'idrfs_present': True}},
    "M": {'description': 'Distant metastatic disease (except as defined for MS). The tumor has spread (metastasized) to distant parts of the body.', 'meaning': 'NCIT:C133430', 'annotations': {'metastatic': True}},
    "MS": {'description': 'Metastatic disease in children younger than 18 months with metastases confined to skin, liver, and/or bone marrow (bone marrow involvement limited to <10% tumor cells). This stage has a favorable prognosis despite metastatic disease.', 'meaning': 'NCIT:C133431', 'annotations': {'metastatic': True, 'special_category': True, 'age_restriction': '<18 months', 'favorable_prognosis': True}, 'aliases': ['Stage 4S equivalent']},
}

class INSSStage(RichEnum):
    """
    International Neuroblastoma Staging System (INSS) stages. A post-surgical staging system based on extent of tumor resection, lymph node involvement, and metastatic spread. This is the legacy system; INRGSS is now preferred for diagnosis years 2024+.
    """
    # Enum members
    STAGE_1 = "STAGE_1"
    STAGE_2A = "STAGE_2A"
    STAGE_2B = "STAGE_2B"
    STAGE_3 = "STAGE_3"
    STAGE_4 = "STAGE_4"
    STAGE_4S = "STAGE_4S"

# Set metadata after class creation
INSSStage._metadata = {
    "STAGE_1": {'description': 'Localized tumor with complete gross excision, with or without microscopic residual disease; representative ipsilateral lymph nodes negative for tumor microscopically.', 'meaning': 'NCIT:C85417', 'annotations': {'localized': True, 'resection': 'complete'}},
    "STAGE_2A": {'description': 'Localized tumor with incomplete gross excision; representative ipsilateral nonadherent lymph nodes negative for tumor microscopically.', 'meaning': 'NCIT:C85418', 'annotations': {'localized': True, 'resection': 'incomplete', 'lymph_nodes': 'negative'}},
    "STAGE_2B": {'description': 'Localized tumor with or without complete gross excision, with ipsilateral nonadherent lymph nodes positive for tumor. Enlarged contralateral lymph nodes must be negative microscopically.', 'meaning': 'NCIT:C85419', 'annotations': {'localized': True, 'lymph_nodes': 'ipsilateral_positive'}},
    "STAGE_3": {'description': 'Unresectable unilateral tumor infiltrating across the midline, with or without regional lymph node involvement; or localized unilateral tumor with contralateral regional lymph node involvement; or midline tumor with bilateral extension by infiltration (unresectable) or by lymph node involvement.', 'meaning': 'NCIT:C85420', 'annotations': {'localized': False, 'crosses_midline': True}},
    "STAGE_4": {'description': 'Any primary tumor with dissemination to distant lymph nodes, bone, bone marrow, liver, skin, and/or other organs (except as defined for stage 4S).', 'meaning': 'NCIT:C85421', 'annotations': {'metastatic': True}},
    "STAGE_4S": {'description': 'Localized primary tumor (as defined for stage 1, 2A, or 2B) with dissemination limited to skin, liver, and/or bone marrow (limited to infants <1 year of age). Marrow involvement should be minimal (<10% of total nucleated cells).', 'meaning': 'NCIT:C85422', 'annotations': {'metastatic': True, 'special_category': True, 'age_restriction': '<12 months', 'favorable_prognosis': True}, 'aliases': ['Special stage 4']},
}

class NeuroblastomaRiskGroup(RichEnum):
    """
    International Neuroblastoma Risk Group (INRG) pretreatment risk classification groups. Combines INRGSS stage with tumor histology, MYCN status, ploidy, and other prognostic factors.
    """
    # Enum members
    VERY_LOW = "VERY_LOW"
    LOW = "LOW"
    INTERMEDIATE = "INTERMEDIATE"
    HIGH = "HIGH"

# Set metadata after class creation
NeuroblastomaRiskGroup._metadata = {
    "VERY_LOW": {'description': 'Very low risk neuroblastoma with excellent prognosis. Typically includes L1 tumors and MS without MYCN amplification.', 'annotations': {'expected_efs': '>85%'}},
    "LOW": {'description': 'Low risk neuroblastoma with favorable prognosis. Treatment may include surgery alone or observation.', 'annotations': {'expected_efs': '>75%'}},
    "INTERMEDIATE": {'description': 'Intermediate risk neuroblastoma requiring multimodal treatment including chemotherapy.', 'annotations': {'expected_efs': '50-75%'}},
    "HIGH": {'description': 'High risk neuroblastoma with poor prognosis. Requires intensive multimodal therapy including high-dose chemotherapy with autologous stem cell rescue, surgery, radiation, and immunotherapy.', 'meaning': 'NCIT:C150281', 'annotations': {'expected_efs': '<50%', 'mycn_amplified': 'often'}},
}

class ImageDefinedRiskFactor(RichEnum):
    """
    Image-defined risk factors (IDRFs) used in INRGSS staging to determine surgical risk. Presence of any IDRF upgrades a tumor from L1 to L2.
    """
    # Enum members
    IPSILATERAL_TUMOR_EXTENSION_TO_BODY_CAVITIES = "IPSILATERAL_TUMOR_EXTENSION_TO_BODY_CAVITIES"
    NECK_ENCASING_CAROTID_OR_VERTEBRAL = "NECK_ENCASING_CAROTID_OR_VERTEBRAL"
    NECK_ENCASING_JUGULAR = "NECK_ENCASING_JUGULAR"
    NECK_EXTENDING_TO_SKULL_BASE = "NECK_EXTENDING_TO_SKULL_BASE"
    NECK_COMPRESSING_TRACHEA = "NECK_COMPRESSING_TRACHEA"
    CERVICOTHORACIC_ENCASING_BRACHIAL_PLEXUS = "CERVICOTHORACIC_ENCASING_BRACHIAL_PLEXUS"
    CERVICOTHORACIC_ENCASING_SUBCLAVIAN = "CERVICOTHORACIC_ENCASING_SUBCLAVIAN"
    CERVICOTHORACIC_COMPRESSING_TRACHEA = "CERVICOTHORACIC_COMPRESSING_TRACHEA"
    THORAX_ENCASING_AORTA = "THORAX_ENCASING_AORTA"
    THORAX_COMPRESSING_TRACHEA_BRONCHI = "THORAX_COMPRESSING_TRACHEA_BRONCHI"
    THORAX_LOWER_MEDIASTINUM_INFILTRATING = "THORAX_LOWER_MEDIASTINUM_INFILTRATING"
    THORACOABDOMINAL_ENCASING_AORTA_CELIAC = "THORACOABDOMINAL_ENCASING_AORTA_CELIAC"
    ABDOMEN_PELVIS_ENCASING_CELIAC_SMA = "ABDOMEN_PELVIS_ENCASING_CELIAC_SMA"
    ABDOMEN_PELVIS_ENCASING_RENAL_VESSELS = "ABDOMEN_PELVIS_ENCASING_RENAL_VESSELS"
    ABDOMEN_PELVIS_ENCASING_AORTA_IVC = "ABDOMEN_PELVIS_ENCASING_AORTA_IVC"
    ABDOMEN_PELVIS_ENCASING_ILIAC_VESSELS = "ABDOMEN_PELVIS_ENCASING_ILIAC_VESSELS"
    ABDOMEN_PELVIS_PELVIC_CROSSING_SCIATIC_NOTCH = "ABDOMEN_PELVIS_PELVIC_CROSSING_SCIATIC_NOTCH"
    INTRASPINAL_EXTENSION = "INTRASPINAL_EXTENSION"
    ADJACENT_ORGAN_INFILTRATION = "ADJACENT_ORGAN_INFILTRATION"

# Set metadata after class creation
ImageDefinedRiskFactor._metadata = {
    "IPSILATERAL_TUMOR_EXTENSION_TO_BODY_CAVITIES": {'description': 'Tumor extension from neck to chest, chest to abdomen, or abdomen to pelvis.'},
    "NECK_ENCASING_CAROTID_OR_VERTEBRAL": {'description': 'Tumor encasing carotid artery and/or vertebral artery.'},
    "NECK_ENCASING_JUGULAR": {'description': 'Tumor encasing internal jugular vein.'},
    "NECK_EXTENDING_TO_SKULL_BASE": {'description': 'Tumor extending to base of skull.'},
    "NECK_COMPRESSING_TRACHEA": {'description': 'Tumor compressing the trachea.'},
    "CERVICOTHORACIC_ENCASING_BRACHIAL_PLEXUS": {'description': 'Tumor encasing brachial plexus roots (C5-T1).'},
    "CERVICOTHORACIC_ENCASING_SUBCLAVIAN": {'description': 'Tumor encasing subclavian vessels and/or vertebral artery and/or carotid artery.'},
    "CERVICOTHORACIC_COMPRESSING_TRACHEA": {'description': 'Tumor compressing the trachea.'},
    "THORAX_ENCASING_AORTA": {'description': 'Tumor encasing aorta and/or major branches.'},
    "THORAX_COMPRESSING_TRACHEA_BRONCHI": {'description': 'Tumor compressing trachea and/or principal bronchi.'},
    "THORAX_LOWER_MEDIASTINUM_INFILTRATING": {'description': 'Lower mediastinal tumor infiltrating the costo-vertebral junction between T9 and T12.'},
    "THORACOABDOMINAL_ENCASING_AORTA_CELIAC": {'description': 'Tumor encasing the aorta and/or vena cava.'},
    "ABDOMEN_PELVIS_ENCASING_CELIAC_SMA": {'description': 'Tumor encasing celiac axis and/or superior mesenteric artery.'},
    "ABDOMEN_PELVIS_ENCASING_RENAL_VESSELS": {'description': 'Tumor encasing origin of renal vessels.'},
    "ABDOMEN_PELVIS_ENCASING_AORTA_IVC": {'description': 'Tumor encasing aorta and/or inferior vena cava.'},
    "ABDOMEN_PELVIS_ENCASING_ILIAC_VESSELS": {'description': 'Tumor encasing iliac vessels.'},
    "ABDOMEN_PELVIS_PELVIC_CROSSING_SCIATIC_NOTCH": {'description': 'Pelvic tumor crossing the sciatic notch.'},
    "INTRASPINAL_EXTENSION": {'description': 'Intraspinal tumor extension provided that more than one third of the spinal canal in the axial plane is invaded and/or the perimedullary leptomeningeal spaces are not visible and/or spinal cord signal is abnormal.'},
    "ADJACENT_ORGAN_INFILTRATION": {'description': 'Infiltration of adjacent organs/structures such as pericardium, diaphragm, kidney, liver, duodeno-pancreatic block, and mesentery.'},
}

__all__ = [
    "INRGSSStage",
    "INSSStage",
    "NeuroblastomaRiskGroup",
    "ImageDefinedRiskFactor",
]