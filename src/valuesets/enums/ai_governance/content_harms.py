"""
Content Harm Categories

A content-harm classification for AI-generated and AI-surfaced content, extending the narrow toxicity label set in data_science/text_classification (ToxicityClassificationEnum) into categories usable for safety policy, evaluation, red-teaming, and incident classification.
RELATIONSHIP TO ToxicityClassificationEnum: that enum encodes the label set of the Jigsaw toxic-comment task -- TOXIC, SEVERE_TOXIC, OBSCENE, THREAT, INSULT, IDENTITY_HATE. It remains in place and is not deprecated, because it is a recognisable published label set and datasets coded against it should keep using it. It is, however, a classifier output space for a single text span rather than a harm taxonomy: it collapses distinct harms into "toxicity", carries a severity axis (SEVERE_TOXIC) inside its category axis, and has no coverage of sexual content, self-harm, dangerous capability uplift, deception, or privacy. This module supplies the wider set. Every Jigsaw label has a corresponding value here, recorded in the `jigsaw_label` annotation.
RELATIONSHIP TO THE ENCODED SOTs: this is a refinement of a single subdomain of the MIT AI Risk Repository -- 1.2 Exposure to toxic content -- whose own description enumerates hate speech, violence, extremism, illegal acts, child sexual abuse material, profanity, inflammatory political speech, and pornography without giving them category status. Several values here instead refine other subdomains, and each records which via `mit_air_subdomain`. The categories are a synthesis of those source enumerations with the Jigsaw labels and with Weidinger et al.'s risks 2.1.2 and 2.3.2; they are not a transcription of any single published taxonomy, and are marked DRAFT accordingly.
SCOPE AND BOUNDARY CONDITIONS: these categories describe *content*, and so are the wrong instrument for harms that are not carried by a piece of content -- unequal model performance across groups, environmental cost, labour effects, power concentration, governance failure. Those are covered by the domain taxonomies in the sibling modules. The categories also carry no severity, likelihood, or context judgement: the same content may be harmful in one deployment and appropriate in another (medical, legal, educational, artistic, and security-research contexts are the usual examples), so a value here records what the content is, not that a harm occurred. Pair with data_science/priority_severity for severity and with ai_governance/risk_taxonomy_dimensions for evidence status and affected party.
Categories are not mutually exclusive; a single item of content frequently carries several.

Generated from: ai_governance/content_harms.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ContentHarmCategoryEnum(RichEnum):
    """
    Categories of harm carried by AI-generated or AI-surfaced content. Top-level values are harm groups; leaf values are specific categories linked by is_a. Not mutually exclusive.
    """
    # Enum members
    NO_CONTENT_HARM = "NO_CONTENT_HARM"
    HATEFUL_CONTENT = "HATEFUL_CONTENT"
    IDENTITY_BASED_HATE = "IDENTITY_BASED_HATE"
    DEMEANING_STEREOTYPING = "DEMEANING_STEREOTYPING"
    EXCLUSIONARY_LANGUAGE = "EXCLUSIONARY_LANGUAGE"
    HARASSMENT_AND_ABUSE = "HARASSMENT_AND_ABUSE"
    INSULT = "INSULT"
    THREAT = "THREAT"
    SEXUAL_HARASSMENT = "SEXUAL_HARASSMENT"
    DOXXING = "DOXXING"
    VIOLENT_CONTENT = "VIOLENT_CONTENT"
    GRAPHIC_VIOLENCE = "GRAPHIC_VIOLENCE"
    INCITEMENT_TO_VIOLENCE = "INCITEMENT_TO_VIOLENCE"
    VIOLENT_EXTREMISM = "VIOLENT_EXTREMISM"
    SEXUAL_CONTENT = "SEXUAL_CONTENT"
    ADULT_SEXUAL_CONTENT = "ADULT_SEXUAL_CONTENT"
    NON_CONSENSUAL_INTIMATE_IMAGERY = "NON_CONSENSUAL_INTIMATE_IMAGERY"
    CHILD_SEXUAL_ABUSE_MATERIAL = "CHILD_SEXUAL_ABUSE_MATERIAL"
    SELF_HARM_CONTENT = "SELF_HARM_CONTENT"
    SUICIDE_AND_SELF_HARM_PROMOTION = "SUICIDE_AND_SELF_HARM_PROMOTION"
    DISORDERED_EATING_PROMOTION = "DISORDERED_EATING_PROMOTION"
    DANGEROUS_FACILITATION = "DANGEROUS_FACILITATION"
    DANGEROUS_MEDICAL_ADVICE = "DANGEROUS_MEDICAL_ADVICE"
    DANGEROUS_LEGAL_OR_FINANCIAL_ADVICE = "DANGEROUS_LEGAL_OR_FINANCIAL_ADVICE"
    WEAPONS_FACILITATION = "WEAPONS_FACILITATION"
    CBRN_FACILITATION = "CBRN_FACILITATION"
    CYBER_OFFENSE_FACILITATION = "CYBER_OFFENSE_FACILITATION"
    OTHER_ILLEGAL_ACT_FACILITATION = "OTHER_ILLEGAL_ACT_FACILITATION"
    DECEPTIVE_CONTENT = "DECEPTIVE_CONTENT"
    MISINFORMATION = "MISINFORMATION"
    DISINFORMATION = "DISINFORMATION"
    IMPERSONATION = "IMPERSONATION"
    FRAUD_AND_SCAM_CONTENT = "FRAUD_AND_SCAM_CONTENT"
    UNDISCLOSED_SYNTHETIC_CONTENT = "UNDISCLOSED_SYNTHETIC_CONTENT"
    PRIVACY_VIOLATING_CONTENT = "PRIVACY_VIOLATING_CONTENT"
    PERSONAL_DATA_DISCLOSURE = "PERSONAL_DATA_DISCLOSURE"
    SENSITIVE_ATTRIBUTE_INFERENCE = "SENSITIVE_ATTRIBUTE_INFERENCE"
    NORM_VIOLATING_CONTENT = "NORM_VIOLATING_CONTENT"
    PROFANITY = "PROFANITY"
    INFLAMMATORY_POLITICAL_SPEECH = "INFLAMMATORY_POLITICAL_SPEECH"
    SPAM = "SPAM"

# Set metadata after class creation
ContentHarmCategoryEnum._metadata = {
    "NO_CONTENT_HARM": {'description': 'Content carrying none of the harm categories below. Provided as an explicit negative class for classifier outputs.', 'annotations': {'node_type': 'category', 'jigsaw_label': 'NON_TOXIC'}, 'aliases': ['non-toxic', 'safe']},
    "HATEFUL_CONTENT": {'description': 'Content expressing hatred or contempt toward people based on identity.', 'annotations': {'node_type': 'group', 'mit_air_subdomain': '1.2'}},
    "IDENTITY_BASED_HATE": {'description': 'Content attacking, dehumanising, or inciting hatred against people on the basis of a protected or identity characteristic.', 'annotations': {'node_type': 'category', 'jigsaw_label': 'IDENTITY_HATE', 'mit_air_subdomain': '1.2'}, 'aliases': ['hate speech']},
    "DEMEANING_STEREOTYPING": {'description': 'Content reproducing demeaning stereotypes about a group without rising to explicit hatred. Distinguished from IDENTITY_BASED_HATE because the representational harm occurs without an attack.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '1.1'}},
    "EXCLUSIONARY_LANGUAGE": {'description': "Content whose norms or presuppositions exclude or erase identities, for example by treating one group's experience as universal.", 'annotations': {'node_type': 'category', 'mit_air_subdomain': '1.1'}},
    "HARASSMENT_AND_ABUSE": {'description': 'Content directed at a person or people so as to demean, intimidate, or coerce.', 'annotations': {'node_type': 'group', 'mit_air_subdomain': '1.2'}},
    "INSULT": {'description': 'Content demeaning or disparaging a person.', 'annotations': {'node_type': 'category', 'jigsaw_label': 'INSULT', 'mit_air_subdomain': '1.2'}},
    "THREAT": {'description': 'Content threatening harm against a person or group.', 'annotations': {'node_type': 'category', 'jigsaw_label': 'THREAT', 'mit_air_subdomain': '1.2'}},
    "SEXUAL_HARASSMENT": {'description': 'Unwanted sexual content directed at a person.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '1.2'}},
    "DOXXING": {'description': 'Publication of identifying or locating information about a person without consent, so as to expose them to harm.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '2.1'}},
    "VIOLENT_CONTENT": {'description': 'Content depicting, glorifying, or inciting violence.', 'annotations': {'node_type': 'group', 'mit_air_subdomain': '1.2'}},
    "GRAPHIC_VIOLENCE": {'description': 'Graphic depiction of violence or its aftermath.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '1.2'}},
    "INCITEMENT_TO_VIOLENCE": {'description': 'Content encouraging or calling for violent acts.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '1.2'}},
    "VIOLENT_EXTREMISM": {'description': 'Content promoting or produced by violent extremist or terrorist movements, including recruitment and propaganda.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '1.2'}},
    "SEXUAL_CONTENT": {'description': 'Sexually explicit content. Whether such content constitutes a harm is strongly deployment-dependent, except for the two categories below which are harmful in all contexts.', 'annotations': {'node_type': 'group', 'mit_air_subdomain': '1.2'}},
    "ADULT_SEXUAL_CONTENT": {'description': 'Consensual adult sexual or pornographic content.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '1.2'}, 'aliases': ['pornography']},
    "NON_CONSENSUAL_INTIMATE_IMAGERY": {'description': 'Sexual or intimate depictions of a real person produced or distributed without their consent, including synthetic depictions.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '4.3'}, 'aliases': ['NCII']},
    "CHILD_SEXUAL_ABUSE_MATERIAL": {'description': 'Sexual content depicting minors, including synthetic depictions.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '1.2'}, 'aliases': ['CSAM']},
    "SELF_HARM_CONTENT": {'description': 'Content promoting, instructing in, or encouraging self-inflicted harm.', 'annotations': {'node_type': 'group', 'mit_air_subdomain': '1.2'}},
    "SUICIDE_AND_SELF_HARM_PROMOTION": {'description': 'Content encouraging suicide or self-injury, or providing method instruction for either.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '1.2'}},
    "DISORDERED_EATING_PROMOTION": {'description': 'Content promoting or instructing in disordered eating behaviours.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '1.2'}},
    "DANGEROUS_FACILITATION": {'description': 'Content providing capability uplift toward acts that cause serious physical, financial, or infrastructural harm.', 'annotations': {'node_type': 'group', 'mit_air_subdomain': '4.2'}},
    "DANGEROUS_MEDICAL_ADVICE": {'description': 'False or hazardous health guidance, such as incorrect dosages, that may lead a user to harm themselves or others.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '3.1'}},
    "DANGEROUS_LEGAL_OR_FINANCIAL_ADVICE": {'description': 'False or hazardous legal or financial guidance that may lead a user to unwitting legal jeopardy or material loss.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '3.1'}},
    "WEAPONS_FACILITATION": {'description': 'Content assisting the acquisition, construction, or use of conventional weapons or explosives.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '4.2'}},
    "CBRN_FACILITATION": {'description': 'Content assisting the development or use of chemical, biological, radiological, or nuclear capabilities.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '4.2'}},
    "CYBER_OFFENSE_FACILITATION": {'description': 'Content assisting the development or deployment of malicious code, intrusion, or other cyber-offensive capability.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '4.2'}},
    "OTHER_ILLEGAL_ACT_FACILITATION": {'description': 'Content assisting illegal acts not covered by the more specific facilitation categories.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '1.2'}},
    "DECEPTIVE_CONTENT": {'description': 'Content that misleads, whether or not the deception is intended.', 'annotations': {'node_type': 'group', 'mit_air_subdomain': '3.1'}},
    "MISINFORMATION": {'description': 'False or misleading content generated without intent to deceive. Distinguished from DISINFORMATION by the absence of intent.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '3.1'}},
    "DISINFORMATION": {'description': 'False content generated or deployed with intent to deceive.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '4.1'}},
    "IMPERSONATION": {'description': 'Content presenting itself as originating from a real person or organisation without authorisation.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '4.3'}},
    "FRAUD_AND_SCAM_CONTENT": {'description': 'Content designed to obtain money, credentials, or advantage by deception.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '4.3'}},
    "UNDISCLOSED_SYNTHETIC_CONTENT": {'description': 'AI-generated content presented without disclosure where disclosure is expected or required.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '3.2'}},
    "PRIVACY_VIOLATING_CONTENT": {'description': 'Content disclosing or inferring information a person has not consented to share.', 'annotations': {'node_type': 'group', 'mit_air_subdomain': '2.1'}},
    "PERSONAL_DATA_DISCLOSURE": {'description': 'Content leaking personal data memorised from training data or otherwise disclosed without consent.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '2.1'}},
    "SENSITIVE_ATTRIBUTE_INFERENCE": {'description': 'Content inferring protected or sensitive attributes about a person. Harm may arise even where the inference is incorrect, if it is believed and acted upon.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '2.1'}},
    "NORM_VIOLATING_CONTENT": {'description': 'Content violating community standards without necessarily causing harm in the sense of the categories above. Grouped separately because conflating community-standard violation with harm is a common source of over-broad moderation.', 'annotations': {'node_type': 'group', 'mit_air_subdomain': '1.2'}},
    "PROFANITY": {'description': 'Coarse or obscene language.', 'annotations': {'node_type': 'category', 'jigsaw_label': 'OBSCENE', 'mit_air_subdomain': '1.2'}},
    "INFLAMMATORY_POLITICAL_SPEECH": {'description': 'Politically inflammatory content violating community norms.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '1.2'}},
    "SPAM": {'description': 'Unsolicited bulk or low-value content.', 'annotations': {'node_type': 'category', 'mit_air_subdomain': '1.2'}},
}

__all__ = [
    "ContentHarmCategoryEnum",
]