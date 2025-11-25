"""
Ecological Interactions Value Sets

Value sets for ecological and biological interactions, based on the Relations Ontology (RO) biotically interacts with (RO:0002437) hierarchy.


Generated from: ecological_interactions.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class RelativeTimeEnum(RichEnum):
    """
    Temporal relationships between events or time points
    """
    # Enum members
    BEFORE = "BEFORE"
    AFTER = "AFTER"
    AT_SAME_TIME_AS = "AT_SAME_TIME_AS"

# Set metadata after class creation
RelativeTimeEnum._metadata = {
    "BEFORE": {'description': 'Occurs before the reference time point'},
    "AFTER": {'description': 'Occurs after the reference time point'},
    "AT_SAME_TIME_AS": {'description': 'Occurs at the same time as the reference time point'},
}

class PresenceEnum(RichEnum):
    """
    Classification of whether an entity is present, absent, or at detection limits
    """
    # Enum members
    PRESENT = "PRESENT"
    ABSENT = "ABSENT"
    BELOW_DETECTION_LIMIT = "BELOW_DETECTION_LIMIT"
    ABOVE_DETECTION_LIMIT = "ABOVE_DETECTION_LIMIT"

# Set metadata after class creation
PresenceEnum._metadata = {
    "PRESENT": {'description': 'The entity is present'},
    "ABSENT": {'description': 'The entity is absent'},
    "BELOW_DETECTION_LIMIT": {'description': 'The entity is below the detection limit'},
    "ABOVE_DETECTION_LIMIT": {'description': 'The entity is above the detection limit'},
}

class BioticInteractionType(RichEnum):
    """
    Types of biotic interactions between organisms, based on RO:0002437 (biotically interacts with). These represent ecological relationships where at least one partner is an organism.
    
    """
    # Enum members
    BIOTICALLY_INTERACTS_WITH = "BIOTICALLY_INTERACTS_WITH"
    TROPHICALLY_INTERACTS_WITH = "TROPHICALLY_INTERACTS_WITH"
    PREYS_ON = "PREYS_ON"
    PREYED_UPON_BY = "PREYED_UPON_BY"
    EATS = "EATS"
    IS_EATEN_BY = "IS_EATEN_BY"
    ACQUIRES_NUTRIENTS_FROM = "ACQUIRES_NUTRIENTS_FROM"
    PROVIDES_NUTRIENTS_FOR = "PROVIDES_NUTRIENTS_FOR"
    SYMBIOTICALLY_INTERACTS_WITH = "SYMBIOTICALLY_INTERACTS_WITH"
    COMMENSUALLY_INTERACTS_WITH = "COMMENSUALLY_INTERACTS_WITH"
    MUTUALISTICALLY_INTERACTS_WITH = "MUTUALISTICALLY_INTERACTS_WITH"
    INTERACTS_VIA_PARASITE_HOST = "INTERACTS_VIA_PARASITE_HOST"
    SYMBIOTROPHICALLY_INTERACTS_WITH = "SYMBIOTROPHICALLY_INTERACTS_WITH"
    PARASITE_OF = "PARASITE_OF"
    HOST_OF = "HOST_OF"
    HAS_HOST = "HAS_HOST"
    PARASITOID_OF = "PARASITOID_OF"
    ECTOPARASITE_OF = "ECTOPARASITE_OF"
    ENDOPARASITE_OF = "ENDOPARASITE_OF"
    INTRACELLULAR_ENDOPARASITE_OF = "INTRACELLULAR_ENDOPARASITE_OF"
    INTERCELLULAR_ENDOPARASITE_OF = "INTERCELLULAR_ENDOPARASITE_OF"
    HEMIPARASITE_OF = "HEMIPARASITE_OF"
    STEM_PARASITE_OF = "STEM_PARASITE_OF"
    ROOT_PARASITE_OF = "ROOT_PARASITE_OF"
    OBLIGATE_PARASITE_OF = "OBLIGATE_PARASITE_OF"
    FACULTATIVE_PARASITE_OF = "FACULTATIVE_PARASITE_OF"
    TROPHIC_PARASITE_OF = "TROPHIC_PARASITE_OF"
    PATHOGEN_OF = "PATHOGEN_OF"
    HAS_PATHOGEN = "HAS_PATHOGEN"
    RESERVOIR_HOST_OF = "RESERVOIR_HOST_OF"
    HAS_RESERVOIR_HOST = "HAS_RESERVOIR_HOST"
    IS_VECTOR_FOR = "IS_VECTOR_FOR"
    POLLINATES = "POLLINATES"
    PARTICIPATES_IN_ABIOTIC_BIOTIC_INTERACTION_WITH = "PARTICIPATES_IN_ABIOTIC_BIOTIC_INTERACTION_WITH"
    ECOLOGICALLY_CO_OCCURS_WITH = "ECOLOGICALLY_CO_OCCURS_WITH"
    HYPERPARASITE_OF = "HYPERPARASITE_OF"
    MESOPARASITE_OF = "MESOPARASITE_OF"
    KLEPTOPARASITE_OF = "KLEPTOPARASITE_OF"
    EPIPHYTE_OF = "EPIPHYTE_OF"
    ALLELOPATH_OF = "ALLELOPATH_OF"
    VISITS = "VISITS"
    VISITS_FLOWERS_OF = "VISITS_FLOWERS_OF"
    HAS_FLOWERS_VISITED_BY = "HAS_FLOWERS_VISITED_BY"
    LAYS_EGGS_IN = "LAYS_EGGS_IN"
    HAS_EGGS_LAID_IN_BY = "HAS_EGGS_LAID_IN_BY"
    LAYS_EGGS_ON = "LAYS_EGGS_ON"
    HAS_EGGS_LAID_ON_BY = "HAS_EGGS_LAID_ON_BY"
    CREATES_HABITAT_FOR = "CREATES_HABITAT_FOR"

# Set metadata after class creation
BioticInteractionType._metadata = {
    "BIOTICALLY_INTERACTS_WITH": {'description': 'An interaction relationship in which at least one of the partners is an organism and the other is either an organism or an abiotic entity with which the organism interacts.\n', 'meaning': 'RO:0002437'},
    "TROPHICALLY_INTERACTS_WITH": {'description': 'An interaction relationship in which the partners are related via a feeding relationship.', 'meaning': 'RO:0002438'},
    "PREYS_ON": {'description': 'An interaction relationship involving a predation process, where the subject kills the target in order to eat it or to feed to siblings, offspring or group members.\n', 'meaning': 'RO:0002439'},
    "PREYED_UPON_BY": {'description': 'Inverse of preys on', 'meaning': 'RO:0002458'},
    "EATS": {'description': 'A biotic interaction where one organism consumes a material entity through a type of mouth or other oral opening.\n', 'meaning': 'RO:0002470'},
    "IS_EATEN_BY": {'description': 'Inverse of eats', 'meaning': 'RO:0002471'},
    "ACQUIRES_NUTRIENTS_FROM": {'description': 'Inverse of provides nutrients for', 'meaning': 'RO:0002457'},
    "PROVIDES_NUTRIENTS_FOR": {'description': 'A biotic interaction where a material entity provides nutrition for an organism.', 'meaning': 'RO:0002469'},
    "SYMBIOTICALLY_INTERACTS_WITH": {'description': 'A biotic interaction in which the two organisms live together in more or less intimate association.\n', 'meaning': 'RO:0002440'},
    "COMMENSUALLY_INTERACTS_WITH": {'description': 'An interaction relationship between two organisms living together in more or less intimate association in a relationship in which one benefits and the other is unaffected.\n', 'meaning': 'RO:0002441'},
    "MUTUALISTICALLY_INTERACTS_WITH": {'description': 'An interaction relationship between two organisms living together in more or less intimate association in a relationship in which both organisms benefit from each other.\n', 'meaning': 'RO:0002442'},
    "INTERACTS_VIA_PARASITE_HOST": {'description': 'An interaction relationship between two organisms living together in more or less intimate association in a relationship in which association is disadvantageous or destructive to one of the organisms.\n', 'meaning': 'RO:0002443'},
    "SYMBIOTROPHICALLY_INTERACTS_WITH": {'description': 'A trophic interaction in which one organism acquires nutrients through a symbiotic relationship with another organism.\n', 'meaning': 'RO:0008510'},
    "PARASITE_OF": {'description': 'A parasite-host relationship where an organism benefits at the expense of another.', 'meaning': 'RO:0002444'},
    "HOST_OF": {'description': 'Inverse of has host', 'meaning': 'RO:0002453'},
    "HAS_HOST": {'description': "X 'has host' y if and only if: x is an organism, y is an organism, and x can live on the surface of or within the body of y.\n", 'meaning': 'RO:0002454'},
    "PARASITOID_OF": {'description': 'A parasite that kills or sterilizes its host', 'meaning': 'RO:0002208'},
    "ECTOPARASITE_OF": {'description': 'A sub-relation of parasite-of in which the parasite lives on or in the integumental system of the host.\n', 'meaning': 'RO:0002632'},
    "ENDOPARASITE_OF": {'description': 'A parasite that lives inside its host', 'meaning': 'RO:0002634'},
    "INTRACELLULAR_ENDOPARASITE_OF": {'description': 'A sub-relation of endoparasite-of in which the parasite inhabits host cells.', 'meaning': 'RO:0002640'},
    "INTERCELLULAR_ENDOPARASITE_OF": {'description': 'A sub-relation of endoparasite-of in which the parasite inhabits the spaces between host cells.\n', 'meaning': 'RO:0002638'},
    "HEMIPARASITE_OF": {'description': 'A sub-relation of parasite-of in which the parasite is a plant, and the parasite is parasitic under natural conditions and is also photosynthetic to some degree.\n', 'meaning': 'RO:0002237'},
    "STEM_PARASITE_OF": {'description': 'A parasite-of relationship in which the host is a plant and the parasite that attaches to the host stem.\n', 'meaning': 'RO:0002235'},
    "ROOT_PARASITE_OF": {'description': 'A parasite-of relationship in which the host is a plant and the parasite that attaches to the host root.\n', 'meaning': 'RO:0002236'},
    "OBLIGATE_PARASITE_OF": {'description': 'A sub-relation of parasite-of in which the parasite that cannot complete its life cycle without a host.\n', 'meaning': 'RO:0002227'},
    "FACULTATIVE_PARASITE_OF": {'description': 'A sub-relations of parasite-of in which the parasite that can complete its life cycle independent of a host.\n', 'meaning': 'RO:0002228'},
    "TROPHIC_PARASITE_OF": {'description': 'A symbiotrophic interaction in which one organism acquires nutrients through a parasitic relationship with another organism.\n', 'meaning': 'RO:0008511'},
    "PATHOGEN_OF": {'description': 'Inverse of has pathogen', 'meaning': 'RO:0002556'},
    "HAS_PATHOGEN": {'description': 'A host interaction where the smaller of the two members of a symbiosis causes a disease in the larger member.\n', 'meaning': 'RO:0002557'},
    "RESERVOIR_HOST_OF": {'description': 'A relation between a host organism and a hosted organism in which the hosted organism naturally occurs in an indefinitely maintained reservoir provided by the host.\n', 'meaning': 'RO:0002802'},
    "HAS_RESERVOIR_HOST": {'description': 'Inverse of reservoir host of', 'meaning': 'RO:0002803'},
    "IS_VECTOR_FOR": {'description': 'Organism acts as a vector for transmitting another organism', 'meaning': 'RO:0002459'},
    "POLLINATES": {'description': 'An interaction where an organism transfers pollen to a plant', 'meaning': 'RO:0002455'},
    "PARTICIPATES_IN_ABIOTIC_BIOTIC_INTERACTION_WITH": {'description': 'A biotic interaction relationship in which one partner is an organism and the other partner is inorganic. For example, the relationship between a sponge and the substrate to which is it anchored.\n', 'meaning': 'RO:0002446'},
    "ECOLOGICALLY_CO_OCCURS_WITH": {'description': 'An interaction relationship describing organisms that often occur together at the same time and space or in the same environment.\n', 'meaning': 'RO:0008506'},
    "HYPERPARASITE_OF": {'description': 'x is a hyperparasite of y iff x is a parasite of a parasite of the target organism y', 'meaning': 'RO:0002553'},
    "MESOPARASITE_OF": {'description': 'A sub-relation of parasite-of in which the parasite is partially an endoparasite and partially an ectoparasite.\n', 'meaning': 'RO:0002636'},
    "KLEPTOPARASITE_OF": {'description': 'A sub-relation of parasite of in which a parasite steals resources from another organism, usually food or nest material.\n', 'meaning': 'RO:0008503'},
    "EPIPHYTE_OF": {'description': 'An interaction relationship wherein a plant or algae is living on the outside surface of another plant.\n', 'meaning': 'RO:0008501'},
    "ALLELOPATH_OF": {'description': 'A relationship between organisms where one organism is influenced by the biochemicals produced by another. Allelopathy is a phenomenon in which one organism releases chemicals to positively or negatively influence the growth, survival or reproduction of other organisms in its vicinity.\n', 'meaning': 'RO:0002555'},
    "VISITS": {'description': 'An interaction where an organism visits another organism or location', 'meaning': 'RO:0002618'},
    "VISITS_FLOWERS_OF": {'description': 'An interaction where an organism visits the flowers of a plant', 'meaning': 'RO:0002622'},
    "HAS_FLOWERS_VISITED_BY": {'description': 'Inverse of visits flowers of', 'meaning': 'RO:0002623'},
    "LAYS_EGGS_IN": {'description': 'An interaction where an organism deposits eggs inside another organism', 'meaning': 'RO:0002624'},
    "HAS_EGGS_LAID_IN_BY": {'description': 'Inverse of lays eggs in', 'meaning': 'RO:0002625'},
    "LAYS_EGGS_ON": {'description': 'An interaction relationship in which organism a lays eggs on the outside surface of organism b. Organism b is neither helped nor harmed in the process of egg laying or incubation.\n', 'meaning': 'RO:0008507'},
    "HAS_EGGS_LAID_ON_BY": {'description': 'Inverse of lays eggs on', 'meaning': 'RO:0008508'},
    "CREATES_HABITAT_FOR": {'description': 'An interaction relationship wherein one organism creates a structure or environment that is lived in by another organism.\n', 'meaning': 'RO:0008505'},
}

__all__ = [
    "RelativeTimeEnum",
    "PresenceEnum",
    "BioticInteractionType",
]