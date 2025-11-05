"""
Nuclear Safety Classifications and Emergency Levels

Nuclear safety classifications including INES scale, emergency action levels, nuclear security categories, and safety system classifications. Based on IAEA standards, NRC regulations, and international nuclear safety frameworks.

Generated from: energy/nuclear/nuclear_safety.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class INESLevelEnum(RichEnum):
    """
    International Nuclear and Radiological Event Scale (INES) levels
    """
    # Enum members
    LEVEL_0 = "LEVEL_0"
    LEVEL_1 = "LEVEL_1"
    LEVEL_2 = "LEVEL_2"
    LEVEL_3 = "LEVEL_3"
    LEVEL_4 = "LEVEL_4"
    LEVEL_5 = "LEVEL_5"
    LEVEL_6 = "LEVEL_6"
    LEVEL_7 = "LEVEL_7"

# Set metadata after class creation
INESLevelEnum._metadata = {
    "LEVEL_0": {'description': 'Events without safety significance', 'annotations': {'scale_position': 'below scale', 'safety_significance': 'no safety significance', 'public_impact': 'none', 'examples': 'minor technical issues'}},
    "LEVEL_1": {'description': 'Anomaly beyond authorized operating regime', 'annotations': {'scale_position': 'incidents', 'safety_significance': 'minor', 'public_impact': 'none', 'examples': 'minor contamination, minor safety system failure'}},
    "LEVEL_2": {'description': 'Incident with significant defenses remaining', 'annotations': {'scale_position': 'incidents', 'safety_significance': 'minor', 'public_impact': 'none', 'radiation_dose': '<10 mSv to workers'}},
    "LEVEL_3": {'description': 'Serious incident with some defense degradation', 'annotations': {'scale_position': 'incidents', 'safety_significance': 'minor', 'public_impact': 'very minor', 'radiation_dose': '<100 mSv to workers', 'examples': 'near accident, serious contamination'}},
    "LEVEL_4": {'description': 'Accident with minor off-site releases', 'annotations': {'scale_position': 'accidents', 'safety_significance': 'moderate', 'public_impact': 'minor local impact', 'evacuation': 'not required', 'examples': 'partial core damage'}},
    "LEVEL_5": {'description': 'Accident with limited off-site releases', 'annotations': {'scale_position': 'accidents', 'safety_significance': 'moderate to major', 'public_impact': 'limited wider impact', 'protective_actions': 'limited evacuation', 'examples': 'Three Mile Island (1979)'}},
    "LEVEL_6": {'description': 'Serious accident with significant releases', 'annotations': {'scale_position': 'accidents', 'safety_significance': 'major', 'public_impact': 'significant', 'protective_actions': 'extensive evacuation and countermeasures'}},
    "LEVEL_7": {'description': 'Major accident with widespread health and environmental effects', 'annotations': {'scale_position': 'accidents', 'safety_significance': 'major', 'public_impact': 'widespread', 'examples': 'Chernobyl (1986), Fukushima (2011)', 'consequences': 'long-term environmental contamination'}},
}

class EmergencyClassificationEnum(RichEnum):
    """
    Nuclear emergency action levels and classifications
    """
    # Enum members
    NOTIFICATION_UNUSUAL_EVENT = "NOTIFICATION_UNUSUAL_EVENT"
    ALERT = "ALERT"
    SITE_AREA_EMERGENCY = "SITE_AREA_EMERGENCY"
    GENERAL_EMERGENCY = "GENERAL_EMERGENCY"

# Set metadata after class creation
EmergencyClassificationEnum._metadata = {
    "NOTIFICATION_UNUSUAL_EVENT": {'description': 'Events that are in process or have occurred which indicate potential degradation', 'annotations': {'severity': 'lowest emergency level', 'off_site_response': 'notification only', 'public_protective_actions': 'none required', 'emergency_response': 'minimal activation'}, 'aliases': ['NOUE', 'Unusual Event']},
    "ALERT": {'description': 'Events involving actual or potential substantial degradation of plant safety', 'annotations': {'severity': 'second emergency level', 'off_site_response': 'notification and standby', 'public_protective_actions': 'none required, but preparation', 'emergency_response': 'partial activation', 'plant_status': 'substantial safety degradation possible'}},
    "SITE_AREA_EMERGENCY": {'description': 'Events with actual or likely major failures of plant protective systems', 'annotations': {'severity': 'third emergency level', 'off_site_response': 'offsite centers activated', 'public_protective_actions': 'may be required near site', 'emergency_response': 'full activation', 'plant_status': 'major plant safety systems failure'}, 'aliases': ['SAE']},
    "GENERAL_EMERGENCY": {'description': 'Events involving actual or imminent substantial core degradation', 'annotations': {'severity': 'highest emergency level', 'off_site_response': 'full activation', 'public_protective_actions': 'implementation likely', 'emergency_response': 'maximum response', 'plant_status': 'core degradation or containment failure'}},
}

class NuclearSecurityCategoryEnum(RichEnum):
    """
    IAEA nuclear material security categories (INFCIRC/225)
    """
    # Enum members
    CATEGORY_I = "CATEGORY_I"
    CATEGORY_II = "CATEGORY_II"
    CATEGORY_III = "CATEGORY_III"
    CATEGORY_IV = "CATEGORY_IV"

# Set metadata after class creation
NuclearSecurityCategoryEnum._metadata = {
    "CATEGORY_I": {'description': 'Material that can be used directly to manufacture nuclear explosive devices', 'annotations': {'direct_use': True, 'proliferation_risk': 'highest', 'protection_requirements': 'maximum', 'examples': 'HEU ≥20%, Pu ≥2kg, U-233 ≥2kg', 'physical_protection': 'multiple independent physical barriers'}},
    "CATEGORY_II": {'description': 'Material requiring further processing to manufacture nuclear explosive devices', 'annotations': {'direct_use': 'requires processing', 'proliferation_risk': 'moderate', 'protection_requirements': 'substantial', 'examples': 'HEU <20% but >5%, natural uranium >500kg', 'physical_protection': 'significant barriers required'}},
    "CATEGORY_III": {'description': 'Material posing radiation hazard but minimal proliferation risk', 'annotations': {'direct_use': False, 'proliferation_risk': 'low', 'protection_requirements': 'basic', 'examples': 'natural uranium 10-500kg, depleted uranium', 'physical_protection': 'basic measures sufficient'}},
    "CATEGORY_IV": {'description': 'Material with minimal security significance', 'annotations': {'direct_use': False, 'proliferation_risk': 'minimal', 'protection_requirements': 'administrative', 'examples': 'small quantities of natural uranium'}},
}

class SafetySystemClassEnum(RichEnum):
    """
    Nuclear safety system classifications (based on IEEE and ASME standards)
    """
    # Enum members
    CLASS_1E = "CLASS_1E"
    SAFETY_RELATED = "SAFETY_RELATED"
    SAFETY_SIGNIFICANT = "SAFETY_SIGNIFICANT"
    NON_SAFETY_RELATED = "NON_SAFETY_RELATED"

# Set metadata after class creation
SafetySystemClassEnum._metadata = {
    "CLASS_1E": {'description': 'Safety systems essential to emergency reactor shutdown and core cooling', 'annotations': {'safety_function': 'essential to safety', 'redundancy': 'required', 'independence': 'required', 'power_supply': 'independent emergency power', 'seismic_qualification': 'required', 'examples': 'reactor protection system, emergency core cooling'}},
    "SAFETY_RELATED": {'description': 'Systems important to safety but not classified as Class 1E', 'annotations': {'safety_function': 'important to safety', 'quality_requirements': 'enhanced', 'testing_requirements': 'extensive', 'examples': 'some support systems, barriers'}},
    "SAFETY_SIGNIFICANT": {'description': 'Systems with risk significance but not safety-related', 'annotations': {'safety_function': 'risk-significant', 'quality_requirements': 'graded approach', 'risk_informed': 'classification based on risk assessment'}},
    "NON_SAFETY_RELATED": {'description': 'Systems not required for nuclear safety functions', 'annotations': {'safety_function': 'not required for safety', 'quality_requirements': 'commercial standards', 'failure_impact': 'minimal safety impact'}},
}

class ReactorSafetyFunctionEnum(RichEnum):
    """
    Fundamental nuclear reactor safety functions
    """
    # Enum members
    REACTIVITY_CONTROL = "REACTIVITY_CONTROL"
    HEAT_REMOVAL = "HEAT_REMOVAL"
    CONTAINMENT_INTEGRITY = "CONTAINMENT_INTEGRITY"
    CORE_COOLING = "CORE_COOLING"
    SHUTDOWN_CAPABILITY = "SHUTDOWN_CAPABILITY"

# Set metadata after class creation
ReactorSafetyFunctionEnum._metadata = {
    "REACTIVITY_CONTROL": {'description': 'Control of nuclear chain reaction', 'annotations': {'function': 'maintain reactor subcritical when required', 'systems': 'control rods, neutron absorbers', 'failure_consequence': 'criticality accident', 'defense_category': 'prevent accidents'}},
    "HEAT_REMOVAL": {'description': 'Removal of decay heat from reactor core', 'annotations': {'function': 'prevent fuel overheating', 'systems': 'cooling systems, heat exchangers', 'failure_consequence': 'core damage, meltdown', 'defense_category': 'mitigate consequences'}},
    "CONTAINMENT_INTEGRITY": {'description': 'Confinement of radioactive materials', 'annotations': {'function': 'prevent radioactive release', 'systems': 'containment structure, isolation systems', 'failure_consequence': 'environmental contamination', 'defense_category': 'mitigate consequences'}},
    "CORE_COOLING": {'description': 'Maintenance of adequate core cooling', 'annotations': {'function': 'prevent fuel damage', 'systems': 'primary cooling, emergency cooling', 'failure_consequence': 'fuel damage', 'time_sensitivity': 'immediate to long-term'}},
    "SHUTDOWN_CAPABILITY": {'description': 'Ability to shut down and maintain shutdown', 'annotations': {'function': 'terminate power operation safely', 'systems': 'control systems, shutdown systems', 'time_requirement': 'rapid response capability'}},
}

class DefenseInDepthLevelEnum(RichEnum):
    """
    Defense in depth barrier levels for nuclear safety
    """
    # Enum members
    LEVEL_1 = "LEVEL_1"
    LEVEL_2 = "LEVEL_2"
    LEVEL_3 = "LEVEL_3"
    LEVEL_4 = "LEVEL_4"
    LEVEL_5 = "LEVEL_5"

# Set metadata after class creation
DefenseInDepthLevelEnum._metadata = {
    "LEVEL_1": {'description': 'Conservative design and high quality in construction and operation', 'annotations': {'objective': 'prevent deviations from normal operation', 'approach': 'conservative design, quality assurance', 'examples': 'design margins, quality construction'}},
    "LEVEL_2": {'description': 'Control of abnormal operation and detection of failures', 'annotations': {'objective': 'control abnormal operation and failures', 'approach': 'control systems, protection systems', 'examples': 'reactor protection systems, safety systems'}},
    "LEVEL_3": {'description': 'Control of accidents to prevent progression to severe conditions', 'annotations': {'objective': 'control design basis accidents', 'approach': 'engineered safety features', 'examples': 'emergency core cooling, containment systems'}},
    "LEVEL_4": {'description': 'Control of severe accidents including prevention of core melt progression', 'annotations': {'objective': 'control severe accidents', 'approach': 'severe accident management', 'examples': 'cavity flooding, filtered venting'}},
    "LEVEL_5": {'description': 'Mitigation of off-site radiological consequences', 'annotations': {'objective': 'protect public and environment', 'approach': 'emergency planning and response', 'examples': 'evacuation plans, protective actions'}},
}

class RadiationProtectionZoneEnum(RichEnum):
    """
    Radiation protection zone classifications for nuclear facilities
    """
    # Enum members
    EXCLUSION_AREA = "EXCLUSION_AREA"
    LOW_POPULATION_ZONE = "LOW_POPULATION_ZONE"
    EMERGENCY_PLANNING_ZONE = "EMERGENCY_PLANNING_ZONE"
    INGESTION_PATHWAY_ZONE = "INGESTION_PATHWAY_ZONE"
    CONTROLLED_AREA = "CONTROLLED_AREA"
    SUPERVISED_AREA = "SUPERVISED_AREA"

# Set metadata after class creation
RadiationProtectionZoneEnum._metadata = {
    "EXCLUSION_AREA": {'description': 'Area under control of reactor operator with restricted access', 'annotations': {'control': 'reactor operator', 'public_access': 'restricted', 'size': 'typically few hundred meters radius', 'purpose': 'immediate accident response control'}},
    "LOW_POPULATION_ZONE": {'description': 'Area with low population density surrounding exclusion area', 'annotations': {'population_density': 'low', 'evacuation': 'feasible if needed', 'size': 'typically few kilometers radius', 'dose_limit': 'design basis for accident consequences'}},
    "EMERGENCY_PLANNING_ZONE": {'description': 'Area for which emergency planning is conducted', 'annotations': {'planning_required': 'comprehensive emergency plans', 'size': 'typically 10-mile (16 km) radius', 'protective_actions': 'evacuation and sheltering plans'}},
    "INGESTION_PATHWAY_ZONE": {'description': 'Area for controlling food and water contamination', 'annotations': {'contamination_control': 'food and water supplies', 'size': 'typically 50-mile (80 km) radius', 'monitoring': 'food chain monitoring required'}},
    "CONTROLLED_AREA": {'description': 'Area within facility boundary with access control', 'annotations': {'access_control': 'personnel monitoring required', 'radiation_monitoring': 'continuous monitoring', 'training_required': 'radiation safety training'}},
    "SUPERVISED_AREA": {'description': 'Area with potential for radiation exposure but lower than controlled', 'annotations': {'monitoring': 'periodic monitoring', 'access_control': 'limited restrictions', 'training_required': 'basic radiation awareness'}},
}

__all__ = [
    "INESLevelEnum",
    "EmergencyClassificationEnum",
    "NuclearSecurityCategoryEnum",
    "SafetySystemClassEnum",
    "ReactorSafetyFunctionEnum",
    "DefenseInDepthLevelEnum",
    "RadiationProtectionZoneEnum",
]