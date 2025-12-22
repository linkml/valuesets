"""
International Classification of Childhood Cancer, Third Edition (ICCC-3)

Value sets based on the International Classification of Childhood Cancer, Third Edition (ICCC-3). The ICCC is the standard classification for childhood cancers, emphasizing tumor morphology rather than primary site (as used for adult cancers). ICCC-3 classifies tumors coded according to ICD-O-3 into 12 main groups and 47 subgroups.

Generated from: medical/pediatric_oncology/iccc3.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ICCC3MainGroup(RichEnum):
    """
    The 12 main diagnostic groups of the International Classification of Childhood Cancer, Third Edition. Based on tumor morphology and primary site with emphasis on morphology.
    """
    # Enum members
    I_LEUKEMIAS_MYELOPROLIFERATIVE_MYELODYSPLASTIC = "I_LEUKEMIAS_MYELOPROLIFERATIVE_MYELODYSPLASTIC"
    II_LYMPHOMAS_RETICULOENDOTHELIAL = "II_LYMPHOMAS_RETICULOENDOTHELIAL"
    III_CNS_INTRACRANIAL_INTRASPINAL = "III_CNS_INTRACRANIAL_INTRASPINAL"
    IV_NEUROBLASTOMA_PERIPHERAL_NERVOUS = "IV_NEUROBLASTOMA_PERIPHERAL_NERVOUS"
    V_RETINOBLASTOMA = "V_RETINOBLASTOMA"
    VI_RENAL_TUMORS = "VI_RENAL_TUMORS"
    VII_HEPATIC_TUMORS = "VII_HEPATIC_TUMORS"
    VIII_MALIGNANT_BONE_TUMORS = "VIII_MALIGNANT_BONE_TUMORS"
    IX_SOFT_TISSUE_SARCOMAS = "IX_SOFT_TISSUE_SARCOMAS"
    X_GERM_CELL_GONADAL = "X_GERM_CELL_GONADAL"
    XI_EPITHELIAL_MELANOMA = "XI_EPITHELIAL_MELANOMA"
    XII_OTHER_UNSPECIFIED = "XII_OTHER_UNSPECIFIED"

# Set metadata after class creation
ICCC3MainGroup._metadata = {
    "I_LEUKEMIAS_MYELOPROLIFERATIVE_MYELODYSPLASTIC": {'description': 'Includes lymphoid leukemias, acute myeloid leukemias, chronic myeloproliferative diseases, myelodysplastic syndrome and other myeloproliferative diseases, and unspecified and other specified leukemias.', 'meaning': 'NCIT:C3161', 'annotations': {'iccc_code': 'I', 'subgroup_count': 5}},
    "II_LYMPHOMAS_RETICULOENDOTHELIAL": {'description': 'Includes Hodgkin lymphomas, non-Hodgkin lymphomas (except Burkitt lymphoma), Burkitt lymphoma, and miscellaneous lymphoreticular neoplasms.', 'meaning': 'NCIT:C3208', 'annotations': {'iccc_code': 'II', 'subgroup_count': 4}},
    "III_CNS_INTRACRANIAL_INTRASPINAL": {'description': 'Includes ependymomas and choroid plexus tumor, astrocytomas, intracranial and intraspinal embryonal tumors, other gliomas, other specified intracranial and intraspinal neoplasms, and unspecified intracranial and intraspinal neoplasms. Also includes nonmalignant CNS tumors.', 'meaning': 'NCIT:C2907', 'annotations': {'iccc_code': 'III', 'subgroup_count': 6, 'includes_nonmalignant': True}},
    "IV_NEUROBLASTOMA_PERIPHERAL_NERVOUS": {'description': 'Includes neuroblastoma and ganglioneuroblastoma, and other peripheral nervous cell tumors.', 'meaning': 'NCIT:C3270', 'annotations': {'iccc_code': 'IV', 'subgroup_count': 2}},
    "V_RETINOBLASTOMA": {'description': 'Malignant neoplasm of the retina. Single group with no subgroups.', 'meaning': 'NCIT:C7541', 'annotations': {'iccc_code': 'V', 'subgroup_count': 1}},
    "VI_RENAL_TUMORS": {'description': 'Includes nephroblastoma and other nonepithelial renal tumors, renal carcinomas, and unspecified malignant renal tumors.', 'meaning': 'NCIT:C7548', 'annotations': {'iccc_code': 'VI', 'subgroup_count': 3}},
    "VII_HEPATIC_TUMORS": {'description': 'Includes hepatoblastoma, hepatic carcinomas, and unspecified malignant hepatic tumors.', 'meaning': 'NCIT:C7927', 'annotations': {'iccc_code': 'VII', 'subgroup_count': 3}},
    "VIII_MALIGNANT_BONE_TUMORS": {'description': 'Includes osteosarcomas, chondrosarcomas, Ewing tumor and related sarcomas of bone, other specified malignant bone tumors, and unspecified malignant bone tumors.', 'meaning': 'NCIT:C4016', 'annotations': {'iccc_code': 'VIII', 'subgroup_count': 5}},
    "IX_SOFT_TISSUE_SARCOMAS": {'description': 'Includes rhabdomyosarcomas, fibrosarcomas/peripheral nerve sheath tumors/other fibrous neoplasms, Kaposi sarcoma, other specified soft tissue sarcomas, and unspecified soft tissue sarcomas.', 'meaning': 'NCIT:C9306', 'annotations': {'iccc_code': 'IX', 'subgroup_count': 5}},
    "X_GERM_CELL_GONADAL": {'description': 'Includes intracranial and intraspinal germ cell tumors, malignant extracranial and extragonadal germ cell tumors, malignant gonadal germ cell tumors, gonadal carcinomas, and other and unspecified malignant gonadal tumors.', 'meaning': 'NCIT:C3708', 'annotations': {'iccc_code': 'X', 'subgroup_count': 5}},
    "XI_EPITHELIAL_MELANOMA": {'description': 'Includes adrenocortical carcinomas, thyroid carcinomas, nasopharyngeal carcinomas, malignant melanomas, skin carcinomas, and other and unspecified carcinomas.', 'meaning': 'NCIT:C3709', 'annotations': {'iccc_code': 'XI', 'subgroup_count': 6}},
    "XII_OTHER_UNSPECIFIED": {'description': 'Includes other specified malignant tumors and other unspecified malignant tumors not classifiable in groups I-XI.', 'meaning': 'NCIT:C3262', 'annotations': {'iccc_code': 'XII', 'subgroup_count': 2}},
}

class ICCC3Subgroup(RichEnum):
    """
    The 47 diagnostic subgroups of the International Classification of Childhood Cancer, Third Edition. These provide more detailed classification within each of the 12 main groups.
    """
    # Enum members
    IA_LYMPHOID_LEUKEMIAS = "Ia_LYMPHOID_LEUKEMIAS"
    IB_ACUTE_MYELOID_LEUKEMIAS = "Ib_ACUTE_MYELOID_LEUKEMIAS"
    IC_CHRONIC_MYELOPROLIFERATIVE = "Ic_CHRONIC_MYELOPROLIFERATIVE"
    ID_MYELODYSPLASTIC_OTHER_MYELOPROLIFERATIVE = "Id_MYELODYSPLASTIC_OTHER_MYELOPROLIFERATIVE"
    IE_UNSPECIFIED_OTHER_LEUKEMIAS = "Ie_UNSPECIFIED_OTHER_LEUKEMIAS"
    IIA_HODGKIN_LYMPHOMAS = "IIa_HODGKIN_LYMPHOMAS"
    IIB_NON_HODGKIN_LYMPHOMAS = "IIb_NON_HODGKIN_LYMPHOMAS"
    IIC_BURKITT_LYMPHOMA = "IIc_BURKITT_LYMPHOMA"
    IID_MISC_LYMPHORETICULAR = "IId_MISC_LYMPHORETICULAR"
    IIIA_EPENDYMOMAS = "IIIa_EPENDYMOMAS"
    IIIB_ASTROCYTOMAS = "IIIb_ASTROCYTOMAS"
    IIIC_INTRACRANIAL_EMBRYONAL = "IIIc_INTRACRANIAL_EMBRYONAL"
    IIID_OTHER_GLIOMAS = "IIId_OTHER_GLIOMAS"
    IIIE_OTHER_INTRACRANIAL_INTRASPINAL = "IIIe_OTHER_INTRACRANIAL_INTRASPINAL"
    IIIF_UNSPECIFIED_INTRACRANIAL = "IIIf_UNSPECIFIED_INTRACRANIAL"
    IVA_NEUROBLASTOMA_GANGLIONEUROBLASTOMA = "IVa_NEUROBLASTOMA_GANGLIONEUROBLASTOMA"
    IVB_OTHER_PERIPHERAL_NERVOUS = "IVb_OTHER_PERIPHERAL_NERVOUS"
    V_RETINOBLASTOMA = "V_RETINOBLASTOMA"
    VIA_NEPHROBLASTOMA = "VIa_NEPHROBLASTOMA"
    VIB_RENAL_CARCINOMAS = "VIb_RENAL_CARCINOMAS"
    VIC_UNSPECIFIED_RENAL = "VIc_UNSPECIFIED_RENAL"
    VIIA_HEPATOBLASTOMA = "VIIa_HEPATOBLASTOMA"
    VIIB_HEPATIC_CARCINOMAS = "VIIb_HEPATIC_CARCINOMAS"
    VIIC_UNSPECIFIED_HEPATIC = "VIIc_UNSPECIFIED_HEPATIC"
    VIIIA_OSTEOSARCOMAS = "VIIIa_OSTEOSARCOMAS"
    VIIIB_CHONDROSARCOMAS = "VIIIb_CHONDROSARCOMAS"
    VIIIC_EWING_TUMOR_BONE = "VIIIc_EWING_TUMOR_BONE"
    VIIID_OTHER_BONE = "VIIId_OTHER_BONE"
    VIIIE_UNSPECIFIED_BONE = "VIIIe_UNSPECIFIED_BONE"
    IXA_RHABDOMYOSARCOMAS = "IXa_RHABDOMYOSARCOMAS"
    IXB_FIBROSARCOMAS = "IXb_FIBROSARCOMAS"
    IXC_KAPOSI_SARCOMA = "IXc_KAPOSI_SARCOMA"
    IXD_OTHER_SOFT_TISSUE = "IXd_OTHER_SOFT_TISSUE"
    IXE_UNSPECIFIED_SOFT_TISSUE = "IXe_UNSPECIFIED_SOFT_TISSUE"
    XA_INTRACRANIAL_GERM_CELL = "Xa_INTRACRANIAL_GERM_CELL"
    XB_EXTRACRANIAL_EXTRAGONADAL_GERM_CELL = "Xb_EXTRACRANIAL_EXTRAGONADAL_GERM_CELL"
    XC_GONADAL_GERM_CELL = "Xc_GONADAL_GERM_CELL"
    XD_GONADAL_CARCINOMAS = "Xd_GONADAL_CARCINOMAS"
    XE_OTHER_GONADAL = "Xe_OTHER_GONADAL"
    XIA_ADRENOCORTICAL_CARCINOMAS = "XIa_ADRENOCORTICAL_CARCINOMAS"
    XIB_THYROID_CARCINOMAS = "XIb_THYROID_CARCINOMAS"
    XIC_NASOPHARYNGEAL_CARCINOMAS = "XIc_NASOPHARYNGEAL_CARCINOMAS"
    XID_MALIGNANT_MELANOMAS = "XId_MALIGNANT_MELANOMAS"
    XIE_SKIN_CARCINOMAS = "XIe_SKIN_CARCINOMAS"
    XIF_OTHER_CARCINOMAS = "XIf_OTHER_CARCINOMAS"
    XIIA_OTHER_SPECIFIED = "XIIa_OTHER_SPECIFIED"
    XIIB_OTHER_UNSPECIFIED = "XIIb_OTHER_UNSPECIFIED"

# Set metadata after class creation
ICCC3Subgroup._metadata = {
    "IA_LYMPHOID_LEUKEMIAS": {'description': 'Precursor cell lymphoblastic leukemia, NOS; precursor cell lymphoblastic leukemia, B-cell; precursor cell lymphoblastic leukemia, T-cell; Burkitt cell leukemia; and other lymphoid leukemias.', 'meaning': 'NCIT:C3167', 'annotations': {'main_group': 'I', 'icdo3_codes': '9820-9827, 9835-9837'}},
    "IB_ACUTE_MYELOID_LEUKEMIAS": {'description': 'Acute myeloid leukemia and variants including AML with maturation, acute promyelocytic leukemia, acute myelomonocytic leukemia, acute monoblastic leukemia, acute megakaryoblastic leukemia, etc.', 'meaning': 'NCIT:C3171', 'annotations': {'main_group': 'I', 'icdo3_codes': '9840, 9861, 9866-9867, 9870-9874, 9891, 9895-9897, 9910, 9920, 9931'}},
    "IC_CHRONIC_MYELOPROLIFERATIVE": {'description': 'Chronic myeloid leukemia, NOS; juvenile myelomonocytic leukemia; and other chronic myeloproliferative diseases.', 'meaning': 'NCIT:C4345', 'annotations': {'main_group': 'I', 'icdo3_codes': '9863, 9875-9876, 9945-9946, 9950, 9960-9964'}},
    "ID_MYELODYSPLASTIC_OTHER_MYELOPROLIFERATIVE": {'description': 'Myelodysplastic syndrome, NOS; refractory anemia; refractory anemia with ringed sideroblasts; refractory anemia with excess blasts.', 'meaning': 'NCIT:C3247', 'annotations': {'main_group': 'I', 'icdo3_codes': '9945, 9980, 9982-9983, 9985-9989'}},
    "IE_UNSPECIFIED_OTHER_LEUKEMIAS": {'description': 'Leukemia, NOS and other specified leukemias not elsewhere classified.', 'meaning': 'NCIT:C3161', 'annotations': {'main_group': 'I', 'icdo3_codes': '9800-9801, 9805-9809, 9860, 9930'}},
    "IIA_HODGKIN_LYMPHOMAS": {'description': 'Classical Hodgkin lymphoma and nodular lymphocyte predominant Hodgkin lymphoma.', 'meaning': 'NCIT:C9357', 'annotations': {'main_group': 'II', 'icdo3_codes': '9650-9655, 9659, 9661-9665, 9667'}},
    "IIB_NON_HODGKIN_LYMPHOMAS": {'description': 'Diffuse large B-cell lymphoma, follicular lymphoma, peripheral T-cell lymphoma, anaplastic large cell lymphoma, and other non-Hodgkin lymphomas.', 'meaning': 'NCIT:C3211', 'annotations': {'main_group': 'II', 'icdo3_codes': '9591, 9670-9686, 9689-9691, 9695, 9698-9702, 9705, 9708-9709, 9714-9719, 9727-9729'}},
    "IIC_BURKITT_LYMPHOMA": {'description': 'Burkitt lymphoma and Burkitt-like lymphoma.', 'meaning': 'NCIT:C2912', 'annotations': {'main_group': 'II', 'icdo3_codes': '9687'}},
    "IID_MISC_LYMPHORETICULAR": {'description': 'Lymphoreticular neoplasms not elsewhere classified including lymphomatoid granulomatosis and post-transplant lymphoproliferative disorder.', 'meaning': 'NCIT:C27134', 'annotations': {'main_group': 'II', 'icdo3_codes': '9740-9742, 9750, 9754-9758, 9930, 9970'}},
    "IIIA_EPENDYMOMAS": {'description': 'Ependymoma, anaplastic ependymoma, myxopapillary ependymoma, and choroid plexus papilloma and carcinoma.', 'meaning': 'NCIT:C3017', 'annotations': {'main_group': 'III', 'icdo3_codes': '9383, 9390-9394'}},
    "IIIB_ASTROCYTOMAS": {'description': 'Pilocytic astrocytoma, diffuse astrocytoma, anaplastic astrocytoma, glioblastoma, and other astrocytic tumors.', 'meaning': 'NCIT:C60781', 'annotations': {'main_group': 'III', 'icdo3_codes': '9380, 9384, 9400-9411, 9420, 9424'}},
    "IIIC_INTRACRANIAL_EMBRYONAL": {'description': 'Medulloblastoma, primitive neuroectodermal tumor, medulloepithelioma, atypical teratoid/rhabdoid tumor, and other embryonal tumors.', 'meaning': 'NCIT:C6990', 'annotations': {'main_group': 'III', 'icdo3_codes': '9470-9474, 9480, 9490, 9500-9508'}},
    "IIID_OTHER_GLIOMAS": {'description': 'Oligodendroglioma, anaplastic oligodendroglioma, mixed glioma, and other gliomas not elsewhere classified.', 'meaning': 'NCIT:C3059', 'annotations': {'main_group': 'III', 'icdo3_codes': '9380-9382, 9430, 9440-9460'}},
    "IIIE_OTHER_INTRACRANIAL_INTRASPINAL": {'description': 'Pituitary adenoma, craniopharyngioma, pineal tumors, and other specified intracranial neoplasms.', 'meaning': 'NCIT:C2907', 'annotations': {'main_group': 'III'}},
    "IIIF_UNSPECIFIED_INTRACRANIAL": {'description': 'Intracranial and intraspinal neoplasms, NOS.', 'meaning': 'NCIT:C2907', 'annotations': {'main_group': 'III', 'icdo3_codes': '8000-8005'}},
    "IVA_NEUROBLASTOMA_GANGLIONEUROBLASTOMA": {'description': 'Neuroblastoma, NOS and ganglioneuroblastoma.', 'meaning': 'NCIT:C3270', 'annotations': {'main_group': 'IV', 'icdo3_codes': '9490, 9500'}},
    "IVB_OTHER_PERIPHERAL_NERVOUS": {'description': 'Other peripheral nerve tumors including ganglioneuroma and peripheral nerve sheath tumors.', 'meaning': 'NCIT:C3321', 'annotations': {'main_group': 'IV', 'icdo3_codes': '9501-9504, 9520-9523'}},
    "V_RETINOBLASTOMA": {'description': 'Retinoblastoma.', 'meaning': 'NCIT:C7541', 'annotations': {'main_group': 'V', 'icdo3_codes': '9510-9514'}},
    "VIA_NEPHROBLASTOMA": {'description': 'Wilms tumor (nephroblastoma), clear cell sarcoma of kidney, rhabdoid tumor of kidney, and other nonepithelial renal tumors.', 'meaning': 'NCIT:C3267', 'annotations': {'main_group': 'VI', 'icdo3_codes': '8960, 8963-8964'}},
    "VIB_RENAL_CARCINOMAS": {'description': 'Renal cell carcinoma and other renal carcinomas.', 'meaning': 'NCIT:C9385', 'annotations': {'main_group': 'VI'}},
    "VIC_UNSPECIFIED_RENAL": {'description': 'Malignant renal tumors, NOS.', 'meaning': 'NCIT:C7548', 'annotations': {'main_group': 'VI'}},
    "VIIA_HEPATOBLASTOMA": {'description': 'Hepatoblastoma.', 'meaning': 'NCIT:C3728', 'annotations': {'main_group': 'VII', 'icdo3_codes': '8970'}},
    "VIIB_HEPATIC_CARCINOMAS": {'description': 'Hepatocellular carcinoma, cholangiocarcinoma, and other hepatic carcinomas.', 'meaning': 'NCIT:C3099', 'annotations': {'main_group': 'VII'}},
    "VIIC_UNSPECIFIED_HEPATIC": {'description': 'Malignant hepatic tumors, NOS.', 'meaning': 'NCIT:C7927', 'annotations': {'main_group': 'VII'}},
    "VIIIA_OSTEOSARCOMAS": {'description': 'Osteosarcoma, NOS and variants including chondroblastic, fibroblastic, telangiectatic, and small cell osteosarcoma.', 'meaning': 'NCIT:C9145', 'annotations': {'main_group': 'VIII', 'icdo3_codes': '9180-9187, 9191-9195'}},
    "VIIIB_CHONDROSARCOMAS": {'description': 'Chondrosarcoma, NOS and variants.', 'meaning': 'NCIT:C2946', 'annotations': {'main_group': 'VIII', 'icdo3_codes': '9220-9231, 9240-9243'}},
    "VIIIC_EWING_TUMOR_BONE": {'description': 'Ewing sarcoma of bone and peripheral primitive neuroectodermal tumor of bone.', 'meaning': 'NCIT:C4817', 'annotations': {'main_group': 'VIII', 'icdo3_codes': '9260, 9364'}},
    "VIIID_OTHER_BONE": {'description': 'Other specified malignant bone tumors including giant cell tumor of bone, malignant and adamantinoma.', 'meaning': 'NCIT:C4016', 'annotations': {'main_group': 'VIII'}},
    "VIIIE_UNSPECIFIED_BONE": {'description': 'Malignant bone tumors, NOS.', 'meaning': 'NCIT:C4016', 'annotations': {'main_group': 'VIII'}},
    "IXA_RHABDOMYOSARCOMAS": {'description': 'Rhabdomyosarcoma, NOS; embryonal rhabdomyosarcoma; alveolar rhabdomyosarcoma; and other rhabdomyosarcomas.', 'meaning': 'NCIT:C3359', 'annotations': {'main_group': 'IX', 'icdo3_codes': '8900-8905, 8910, 8912, 8920'}},
    "IXB_FIBROSARCOMAS": {'description': 'Fibrosarcoma, NOS; infantile fibrosarcoma; dermatofibrosarcoma; and malignant peripheral nerve sheath tumor.', 'meaning': 'NCIT:C3043', 'annotations': {'main_group': 'IX', 'icdo3_codes': '8810-8815, 8820-8823, 8830, 8832-8833, 9540, 9560-9561'}},
    "IXC_KAPOSI_SARCOMA": {'description': 'Kaposi sarcoma.', 'meaning': 'NCIT:C9087', 'annotations': {'main_group': 'IX', 'icdo3_codes': '9140'}},
    "IXD_OTHER_SOFT_TISSUE": {'description': 'Includes liposarcoma, leiomyosarcoma, synovial sarcoma, hemangiosarcoma, and other specified soft tissue sarcomas.', 'meaning': 'NCIT:C9306', 'annotations': {'main_group': 'IX'}},
    "IXE_UNSPECIFIED_SOFT_TISSUE": {'description': 'Soft tissue sarcomas, NOS.', 'meaning': 'NCIT:C9306', 'annotations': {'main_group': 'IX'}},
    "XA_INTRACRANIAL_GERM_CELL": {'description': 'CNS germ cell tumors including germinoma, teratoma, and nongerminomatous germ cell tumors.', 'meaning': 'NCIT:C5461', 'annotations': {'main_group': 'X', 'icdo3_codes': '9060-9102'}},
    "XB_EXTRACRANIAL_EXTRAGONADAL_GERM_CELL": {'description': 'Extracranial germ cell tumors not involving the gonads including sacrococcygeal, retroperitoneal, and mediastinal germ cell tumors.', 'meaning': 'NCIT:C8881', 'annotations': {'main_group': 'X'}},
    "XC_GONADAL_GERM_CELL": {'description': 'Germ cell tumors of the ovary and testis including dysgerminoma, yolk sac tumor, embryonal carcinoma, and mixed germ cell tumors.', 'meaning': 'NCIT:C3708', 'annotations': {'main_group': 'X'}},
    "XD_GONADAL_CARCINOMAS": {'description': 'Carcinomas arising in the ovary and testis.', 'meaning': 'NCIT:C3709', 'annotations': {'main_group': 'X'}},
    "XE_OTHER_GONADAL": {'description': 'Other specified and unspecified gonadal tumors.', 'meaning': 'NCIT:C3708', 'annotations': {'main_group': 'X'}},
    "XIA_ADRENOCORTICAL_CARCINOMAS": {'description': 'Adrenocortical carcinoma.', 'meaning': 'NCIT:C9325', 'annotations': {'main_group': 'XI', 'icdo3_codes': '8370'}},
    "XIB_THYROID_CARCINOMAS": {'description': 'Papillary thyroid carcinoma, follicular thyroid carcinoma, and medullary thyroid carcinoma.', 'meaning': 'NCIT:C7510', 'annotations': {'main_group': 'XI'}},
    "XIC_NASOPHARYNGEAL_CARCINOMAS": {'description': 'Nasopharyngeal carcinoma and related carcinomas.', 'meaning': 'NCIT:C3871', 'annotations': {'main_group': 'XI'}},
    "XID_MALIGNANT_MELANOMAS": {'description': 'Cutaneous and non-cutaneous malignant melanomas.', 'meaning': 'NCIT:C3224', 'annotations': {'main_group': 'XI'}},
    "XIE_SKIN_CARCINOMAS": {'description': 'Basal cell carcinoma, squamous cell carcinoma of skin, and other skin carcinomas.', 'meaning': 'NCIT:C3372', 'annotations': {'main_group': 'XI'}},
    "XIF_OTHER_CARCINOMAS": {'description': 'Carcinomas at other sites and carcinomas, NOS.', 'meaning': 'NCIT:C3709', 'annotations': {'main_group': 'XI'}},
    "XIIA_OTHER_SPECIFIED": {'description': 'Malignant tumors not classifiable in groups I-XI but with specified histology.', 'meaning': 'NCIT:C3262', 'annotations': {'main_group': 'XII'}},
    "XIIB_OTHER_UNSPECIFIED": {'description': 'Malignant tumors, NOS not classifiable in groups I-XI.', 'meaning': 'NCIT:C3262', 'annotations': {'main_group': 'XII'}},
}

__all__ = [
    "ICCC3MainGroup",
    "ICCC3Subgroup",
]