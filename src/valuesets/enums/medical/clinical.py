"""
Clinical and Medical Value Sets

Value sets for clinical and medical domains including blood types, anatomical systems, medical specialties, drug routes, and diagnostic categories.


Generated from: medical/clinical.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class BloodTypeEnum(RichEnum):
    """
    ABO and Rh blood group classifications
    """
    # Enum members
    A_POSITIVE = "A_POSITIVE"
    A_NEGATIVE = "A_NEGATIVE"
    B_POSITIVE = "B_POSITIVE"
    B_NEGATIVE = "B_NEGATIVE"
    AB_POSITIVE = "AB_POSITIVE"
    AB_NEGATIVE = "AB_NEGATIVE"
    O_POSITIVE = "O_POSITIVE"
    O_NEGATIVE = "O_NEGATIVE"

# Set metadata after class creation
BloodTypeEnum._metadata = {
    "A_POSITIVE": {'description': 'Blood type A, Rh positive', 'meaning': 'SNOMED:278149003', 'annotations': {'abo': 'A', 'rh': 'positive', 'can_receive': 'A+, A-, O+, O-', 'can_donate': 'A+, AB+'}},
    "A_NEGATIVE": {'description': 'Blood type A, Rh negative', 'meaning': 'SNOMED:278152006', 'annotations': {'abo': 'A', 'rh': 'negative', 'can_receive': 'A-, O-', 'can_donate': 'A+, A-, AB+, AB-'}},
    "B_POSITIVE": {'description': 'Blood type B, Rh positive', 'meaning': 'SNOMED:278150003', 'annotations': {'abo': 'B', 'rh': 'positive', 'can_receive': 'B+, B-, O+, O-', 'can_donate': 'B+, AB+'}},
    "B_NEGATIVE": {'description': 'Blood type B, Rh negative', 'meaning': 'SNOMED:278153001', 'annotations': {'abo': 'B', 'rh': 'negative', 'can_receive': 'B-, O-', 'can_donate': 'B+, B-, AB+, AB-'}},
    "AB_POSITIVE": {'description': 'Blood type AB, Rh positive (universal recipient)', 'meaning': 'SNOMED:278151004', 'annotations': {'abo': 'AB', 'rh': 'positive', 'can_receive': 'all types', 'can_donate': 'AB+', 'special': 'universal recipient'}},
    "AB_NEGATIVE": {'description': 'Blood type AB, Rh negative', 'meaning': 'SNOMED:278154007', 'annotations': {'abo': 'AB', 'rh': 'negative', 'can_receive': 'A-, B-, AB-, O-', 'can_donate': 'AB+, AB-'}},
    "O_POSITIVE": {'description': 'Blood type O, Rh positive', 'meaning': 'SNOMED:278147001', 'annotations': {'abo': 'O', 'rh': 'positive', 'can_receive': 'O+, O-', 'can_donate': 'A+, B+, AB+, O+'}},
    "O_NEGATIVE": {'description': 'Blood type O, Rh negative (universal donor)', 'meaning': 'SNOMED:278148006', 'annotations': {'abo': 'O', 'rh': 'negative', 'can_receive': 'O-', 'can_donate': 'all types', 'special': 'universal donor'}},
}

class AnatomicalSystemEnum(RichEnum):
    """
    Major anatomical systems of the body
    """
    # Enum members
    CARDIOVASCULAR = "CARDIOVASCULAR"
    RESPIRATORY = "RESPIRATORY"
    NERVOUS = "NERVOUS"
    DIGESTIVE = "DIGESTIVE"
    MUSCULOSKELETAL = "MUSCULOSKELETAL"
    INTEGUMENTARY = "INTEGUMENTARY"
    ENDOCRINE = "ENDOCRINE"
    URINARY = "URINARY"
    REPRODUCTIVE = "REPRODUCTIVE"
    IMMUNE = "IMMUNE"
    HEMATOLOGIC = "HEMATOLOGIC"

# Set metadata after class creation
AnatomicalSystemEnum._metadata = {
    "CARDIOVASCULAR": {'meaning': 'UBERON:0004535', 'annotations': {'components': 'heart, arteries, veins, capillaries'}, 'aliases': ['cardiovascular system']},
    "RESPIRATORY": {'meaning': 'UBERON:0001004', 'annotations': {'components': 'lungs, trachea, bronchi, diaphragm'}, 'aliases': ['respiratory system']},
    "NERVOUS": {'meaning': 'UBERON:0001016', 'annotations': {'components': 'brain, spinal cord, nerves'}, 'aliases': ['nervous system']},
    "DIGESTIVE": {'meaning': 'UBERON:0001007', 'annotations': {'components': 'mouth, esophagus, stomach, intestines, liver, pancreas'}, 'aliases': ['digestive system']},
    "MUSCULOSKELETAL": {'meaning': 'UBERON:0002204', 'annotations': {'components': 'bones, muscles, tendons, ligaments, cartilage'}, 'aliases': ['musculoskeletal system']},
    "INTEGUMENTARY": {'meaning': 'UBERON:0002416', 'annotations': {'components': 'skin, hair, nails, glands'}, 'aliases': ['integumental system']},
    "ENDOCRINE": {'meaning': 'UBERON:0000949', 'annotations': {'components': 'pituitary, thyroid, adrenals, pancreas'}, 'aliases': ['endocrine system']},
    "URINARY": {'meaning': 'UBERON:0001008', 'annotations': {'components': 'kidneys, ureters, bladder, urethra'}, 'aliases': ['renal system']},
    "REPRODUCTIVE": {'meaning': 'UBERON:0000990', 'annotations': {'components': 'gonads, ducts, external genitalia'}, 'aliases': ['reproductive system']},
    "IMMUNE": {'meaning': 'UBERON:0002405', 'annotations': {'components': 'lymph nodes, spleen, thymus, bone marrow'}, 'aliases': ['immune system']},
    "HEMATOLOGIC": {'meaning': 'UBERON:0002390', 'annotations': {'components': 'blood, bone marrow, spleen'}, 'aliases': ['hematopoietic system']},
}

class MedicalSpecialtyEnum(RichEnum):
    # Enum members
    ANESTHESIOLOGY = "ANESTHESIOLOGY"
    CARDIOLOGY = "CARDIOLOGY"
    DERMATOLOGY = "DERMATOLOGY"
    EMERGENCY_MEDICINE = "EMERGENCY_MEDICINE"
    ENDOCRINOLOGY = "ENDOCRINOLOGY"
    FAMILY_MEDICINE = "FAMILY_MEDICINE"
    GASTROENTEROLOGY = "GASTROENTEROLOGY"
    HEMATOLOGY = "HEMATOLOGY"
    INFECTIOUS_DISEASE = "INFECTIOUS_DISEASE"
    INTERNAL_MEDICINE = "INTERNAL_MEDICINE"
    NEPHROLOGY = "NEPHROLOGY"
    NEUROLOGY = "NEUROLOGY"
    OBSTETRICS_GYNECOLOGY = "OBSTETRICS_GYNECOLOGY"
    ONCOLOGY = "ONCOLOGY"
    OPHTHALMOLOGY = "OPHTHALMOLOGY"
    ORTHOPEDICS = "ORTHOPEDICS"
    OTOLARYNGOLOGY = "OTOLARYNGOLOGY"
    PATHOLOGY = "PATHOLOGY"
    PEDIATRICS = "PEDIATRICS"
    PSYCHIATRY = "PSYCHIATRY"
    PULMONOLOGY = "PULMONOLOGY"
    RADIOLOGY = "RADIOLOGY"
    RHEUMATOLOGY = "RHEUMATOLOGY"
    SURGERY = "SURGERY"
    UROLOGY = "UROLOGY"

# Set metadata after class creation
MedicalSpecialtyEnum._metadata = {
}

class DrugRouteEnum(RichEnum):
    # Enum members
    ORAL = "ORAL"
    INTRAVENOUS = "INTRAVENOUS"
    INTRAMUSCULAR = "INTRAMUSCULAR"
    SUBCUTANEOUS = "SUBCUTANEOUS"
    TOPICAL = "TOPICAL"
    INHALATION = "INHALATION"
    RECTAL = "RECTAL"
    INTRANASAL = "INTRANASAL"
    TRANSDERMAL = "TRANSDERMAL"
    SUBLINGUAL = "SUBLINGUAL"
    EPIDURAL = "EPIDURAL"
    INTRATHECAL = "INTRATHECAL"
    OPHTHALMIC = "OPHTHALMIC"
    OTIC = "OTIC"

# Set metadata after class creation
DrugRouteEnum._metadata = {
    "ORAL": {'meaning': 'NCIT:C38288', 'annotations': {'abbreviation': 'PO', 'absorption': 'GI tract'}, 'aliases': ['Oral Route of Administration']},
    "INTRAVENOUS": {'meaning': 'NCIT:C38276', 'annotations': {'abbreviation': 'IV', 'onset': 'immediate'}, 'aliases': ['Intravenous Route of Administration']},
    "INTRAMUSCULAR": {'meaning': 'NCIT:C28161', 'annotations': {'abbreviation': 'IM', 'sites': 'deltoid, gluteus, vastus lateralis'}, 'aliases': ['Intramuscular Route of Administration']},
    "SUBCUTANEOUS": {'meaning': 'NCIT:C38299', 'annotations': {'abbreviation': 'SC, SubQ', 'absorption': 'slow'}, 'aliases': ['Subcutaneous Route of Administration']},
    "TOPICAL": {'meaning': 'NCIT:C38304', 'annotations': {'forms': 'cream, ointment, gel'}, 'aliases': ['Topical Route of Administration']},
    "INHALATION": {'meaning': 'NCIT:C38216', 'annotations': {'devices': 'inhaler, nebulizer'}, 'aliases': ['Inhalation Route of Administration']},
    "RECTAL": {'meaning': 'NCIT:C38295', 'annotations': {'forms': 'suppository, enema'}, 'aliases': ['Rectal Route of Administration']},
    "INTRANASAL": {'meaning': 'NCIT:C38284', 'annotations': {'forms': 'spray, drops'}, 'aliases': ['Nasal Route of Administration']},
    "TRANSDERMAL": {'meaning': 'NCIT:C38305', 'annotations': {'forms': 'patch'}, 'aliases': ['Transdermal Route of Administration']},
    "SUBLINGUAL": {'meaning': 'NCIT:C38300', 'annotations': {'absorption': 'rapid'}, 'aliases': ['Sublingual Route of Administration']},
    "EPIDURAL": {'meaning': 'NCIT:C38243', 'annotations': {'use': 'anesthesia, analgesia'}, 'aliases': ['Intraepidermal Route of Administration']},
    "INTRATHECAL": {'meaning': 'NCIT:C38277', 'annotations': {'use': 'CNS drugs'}, 'aliases': ['Intraventricular Route of Administration']},
    "OPHTHALMIC": {'meaning': 'NCIT:C38287', 'annotations': {'forms': 'drops, ointment'}, 'aliases': ['Ophthalmic Route of Administration']},
    "OTIC": {'meaning': 'NCIT:C38192', 'annotations': {'forms': 'drops'}, 'aliases': ['Auricular Route of Administration']},
}

class VitalSignEnum(RichEnum):
    # Enum members
    HEART_RATE = "HEART_RATE"
    BLOOD_PRESSURE_SYSTOLIC = "BLOOD_PRESSURE_SYSTOLIC"
    BLOOD_PRESSURE_DIASTOLIC = "BLOOD_PRESSURE_DIASTOLIC"
    RESPIRATORY_RATE = "RESPIRATORY_RATE"
    TEMPERATURE = "TEMPERATURE"
    OXYGEN_SATURATION = "OXYGEN_SATURATION"
    PAIN_SCALE = "PAIN_SCALE"

# Set metadata after class creation
VitalSignEnum._metadata = {
    "HEART_RATE": {'meaning': 'LOINC:8867-4', 'annotations': {'normal_range': '60-100 bpm', 'units': 'beats/min'}},
    "BLOOD_PRESSURE_SYSTOLIC": {'meaning': 'LOINC:8480-6', 'annotations': {'normal_range': '<120 mmHg', 'units': 'mmHg'}},
    "BLOOD_PRESSURE_DIASTOLIC": {'meaning': 'LOINC:8462-4', 'annotations': {'normal_range': '<80 mmHg', 'units': 'mmHg'}},
    "RESPIRATORY_RATE": {'meaning': 'LOINC:9279-1', 'annotations': {'normal_range': '12-20 breaths/min', 'units': 'breaths/min'}},
    "TEMPERATURE": {'meaning': 'LOINC:8310-5', 'annotations': {'normal_range': '36.5-37.5°C', 'units': '°C or °F'}},
    "OXYGEN_SATURATION": {'meaning': 'LOINC:2708-6', 'annotations': {'normal_range': '95-100%', 'units': '%'}},
    "PAIN_SCALE": {'meaning': 'LOINC:38208-5', 'annotations': {'scale': '0-10', 'type': 'subjective'}},
}

class DiagnosticTestTypeEnum(RichEnum):
    # Enum members
    BLOOD_TEST = "BLOOD_TEST"
    URINE_TEST = "URINE_TEST"
    IMAGING_XRAY = "IMAGING_XRAY"
    IMAGING_CT = "IMAGING_CT"
    IMAGING_MRI = "IMAGING_MRI"
    IMAGING_ULTRASOUND = "IMAGING_ULTRASOUND"
    IMAGING_PET = "IMAGING_PET"
    ECG = "ECG"
    EEG = "EEG"
    BIOPSY = "BIOPSY"
    ENDOSCOPY = "ENDOSCOPY"
    GENETIC_TEST = "GENETIC_TEST"

# Set metadata after class creation
DiagnosticTestTypeEnum._metadata = {
    "BLOOD_TEST": {'meaning': 'NCIT:C15189', 'annotations': {'samples': 'serum, plasma, whole blood'}, 'aliases': ['Biopsy Procedure']},
    "URINE_TEST": {'annotations': {'types': 'urinalysis, culture, drug screen'}, 'aliases': ['Tissue Factor']},
    "IMAGING_XRAY": {'meaning': 'NCIT:C17262', 'annotations': {'radiation': 'yes'}, 'aliases': ['X-Ray']},
    "IMAGING_CT": {'meaning': 'NCIT:C17204', 'annotations': {'radiation': 'yes'}, 'aliases': ['Computed Tomography']},
    "IMAGING_MRI": {'meaning': 'NCIT:C16809', 'annotations': {'radiation': 'no'}, 'aliases': ['Magnetic Resonance Imaging']},
    "IMAGING_ULTRASOUND": {'meaning': 'NCIT:C17230', 'annotations': {'radiation': 'no'}, 'aliases': ['Ultrasound Imaging']},
    "IMAGING_PET": {'meaning': 'NCIT:C17007', 'annotations': {'uses': 'radiotracer'}, 'aliases': ['Positron Emission Tomography']},
    "ECG": {'meaning': 'NCIT:C38054', 'annotations': {'measures': 'heart electrical activity'}, 'aliases': ['Electroencephalography']},
    "EEG": {'annotations': {'measures': 'brain electrical activity'}, 'aliases': ['Djibouti']},
    "BIOPSY": {'meaning': 'NCIT:C15189', 'annotations': {'invasive': 'yes'}, 'aliases': ['Biopsy Procedure']},
    "ENDOSCOPY": {'meaning': 'NCIT:C16546', 'annotations': {'types': 'colonoscopy, gastroscopy, bronchoscopy'}, 'aliases': ['Endoscopic Procedure']},
    "GENETIC_TEST": {'meaning': 'NCIT:C15709', 'annotations': {'types': 'karyotype, sequencing, PCR'}, 'aliases': ['Genetic Testing']},
}

class SymptomSeverityEnum(RichEnum):
    # Enum members
    ABSENT = "ABSENT"
    MILD = "MILD"
    MODERATE = "MODERATE"
    SEVERE = "SEVERE"
    LIFE_THREATENING = "LIFE_THREATENING"

# Set metadata after class creation
SymptomSeverityEnum._metadata = {
    "ABSENT": {'annotations': {'grade': '0'}, 'aliases': ['Blood group B']},
    "MILD": {'meaning': 'HP:0012825', 'annotations': {'grade': '1', 'impact': 'minimal daily activity limitation'}},
    "MODERATE": {'meaning': 'HP:0012826', 'annotations': {'grade': '2', 'impact': 'some daily activity limitation'}},
    "SEVERE": {'meaning': 'HP:0012828', 'annotations': {'grade': '3', 'impact': 'significant daily activity limitation'}},
    "LIFE_THREATENING": {'annotations': {'grade': '4', 'impact': 'urgent intervention required'}, 'aliases': ['Profound']},
}

class AllergyTypeEnum(RichEnum):
    # Enum members
    DRUG = "DRUG"
    FOOD = "FOOD"
    ENVIRONMENTAL = "ENVIRONMENTAL"
    CONTACT = "CONTACT"
    INSECT = "INSECT"
    ANAPHYLAXIS = "ANAPHYLAXIS"

# Set metadata after class creation
AllergyTypeEnum._metadata = {
    "DRUG": {'meaning': 'NCIT:C3114', 'annotations': {'examples': 'penicillin, sulfa drugs'}, 'aliases': ['Hypersensitivity']},
    "FOOD": {'annotations': {'common': 'nuts, shellfish, eggs, milk'}},
    "ENVIRONMENTAL": {'annotations': {'examples': 'pollen, dust, mold'}},
    "CONTACT": {'annotations': {'examples': 'latex, nickel, poison ivy'}},
    "INSECT": {'annotations': {'examples': 'bee, wasp, hornet'}},
    "ANAPHYLAXIS": {'annotations': {'severity': 'life-threatening'}},
}

class VaccineTypeEnum(RichEnum):
    # Enum members
    LIVE_ATTENUATED = "LIVE_ATTENUATED"
    INACTIVATED = "INACTIVATED"
    SUBUNIT = "SUBUNIT"
    TOXOID = "TOXOID"
    MRNA = "MRNA"
    VIRAL_VECTOR = "VIRAL_VECTOR"

# Set metadata after class creation
VaccineTypeEnum._metadata = {
    "LIVE_ATTENUATED": {'annotations': {'examples': 'MMR, varicella, yellow fever'}},
    "INACTIVATED": {'annotations': {'examples': 'flu shot, hepatitis A, rabies'}},
    "SUBUNIT": {'annotations': {'examples': 'hepatitis B, HPV, pertussis'}},
    "TOXOID": {'annotations': {'examples': 'diphtheria, tetanus'}},
    "MRNA": {'annotations': {'examples': 'COVID-19 (Pfizer, Moderna)'}},
    "VIRAL_VECTOR": {'annotations': {'examples': 'COVID-19 (J&J, AstraZeneca)'}},
}

class BMIClassificationEnum(RichEnum):
    # Enum members
    UNDERWEIGHT = "UNDERWEIGHT"
    NORMAL_WEIGHT = "NORMAL_WEIGHT"
    OVERWEIGHT = "OVERWEIGHT"
    OBESE_CLASS_I = "OBESE_CLASS_I"
    OBESE_CLASS_II = "OBESE_CLASS_II"
    OBESE_CLASS_III = "OBESE_CLASS_III"

# Set metadata after class creation
BMIClassificationEnum._metadata = {
    "UNDERWEIGHT": {'annotations': {'bmi_range': '<18.5'}},
    "NORMAL_WEIGHT": {'annotations': {'bmi_range': '18.5-24.9'}},
    "OVERWEIGHT": {'annotations': {'bmi_range': '25.0-29.9'}},
    "OBESE_CLASS_I": {'annotations': {'bmi_range': '30.0-34.9'}},
    "OBESE_CLASS_II": {'annotations': {'bmi_range': '35.0-39.9'}},
    "OBESE_CLASS_III": {'annotations': {'bmi_range': '≥40.0', 'aliases': 'morbid obesity'}},
}

__all__ = [
    "BloodTypeEnum",
    "AnatomicalSystemEnum",
    "MedicalSpecialtyEnum",
    "DrugRouteEnum",
    "VitalSignEnum",
    "DiagnosticTestTypeEnum",
    "SymptomSeverityEnum",
    "AllergyTypeEnum",
    "VaccineTypeEnum",
    "BMIClassificationEnum",
]