"""

Generated from: data_science/text_classification.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class NewsTopicCategoryEnum(RichEnum):
    """
    Common news article topic categories
    """
    # Enum members
    POLITICS = "POLITICS"
    BUSINESS = "BUSINESS"
    TECHNOLOGY = "TECHNOLOGY"
    SPORTS = "SPORTS"
    ENTERTAINMENT = "ENTERTAINMENT"
    SCIENCE = "SCIENCE"
    HEALTH = "HEALTH"
    WORLD = "WORLD"
    LOCAL = "LOCAL"

# Set metadata after class creation
NewsTopicCategoryEnum._metadata = {
    "POLITICS": {'description': 'Political news and government affairs'},
    "BUSINESS": {'description': 'Business, finance, and economic news', 'aliases': ['finance', 'economy']},
    "TECHNOLOGY": {'description': 'Technology and computing news', 'aliases': ['tech', 'IT']},
    "SPORTS": {'description': 'Sports news and events'},
    "ENTERTAINMENT": {'description': 'Entertainment and celebrity news', 'aliases': ['showbiz']},
    "SCIENCE": {'description': 'Scientific discoveries and research'},
    "HEALTH": {'description': 'Health, medicine, and wellness news', 'aliases': ['medical']},
    "WORLD": {'description': 'International news and events', 'aliases': ['international', 'global']},
    "LOCAL": {'description': 'Local and regional news', 'aliases': ['regional']},
}

class ToxicityClassificationEnum(RichEnum):
    """
    Text toxicity classification labels
    """
    # Enum members
    NON_TOXIC = "NON_TOXIC"
    TOXIC = "TOXIC"
    SEVERE_TOXIC = "SEVERE_TOXIC"
    OBSCENE = "OBSCENE"
    THREAT = "THREAT"
    INSULT = "INSULT"
    IDENTITY_HATE = "IDENTITY_HATE"

# Set metadata after class creation
ToxicityClassificationEnum._metadata = {
    "NON_TOXIC": {'description': 'Text is appropriate and non-harmful', 'meaning': 'SIO:001010', 'aliases': ['safe', 'clean', '0']},
    "TOXIC": {'description': 'Text contains harmful or inappropriate content', 'aliases': ['harmful', 'inappropriate', '1']},
    "SEVERE_TOXIC": {'description': 'Text contains severely harmful content'},
    "OBSCENE": {'description': 'Text contains obscene content'},
    "THREAT": {'description': 'Text contains threatening content'},
    "INSULT": {'description': 'Text contains insulting content'},
    "IDENTITY_HATE": {'description': 'Text contains identity-based hate'},
}

class IntentClassificationEnum(RichEnum):
    """
    Common chatbot/NLU intent categories
    """
    # Enum members
    GREETING = "GREETING"
    GOODBYE = "GOODBYE"
    THANKS = "THANKS"
    HELP = "HELP"
    INFORMATION = "INFORMATION"
    COMPLAINT = "COMPLAINT"
    FEEDBACK = "FEEDBACK"
    PURCHASE = "PURCHASE"
    CANCEL = "CANCEL"
    REFUND = "REFUND"

# Set metadata after class creation
IntentClassificationEnum._metadata = {
    "GREETING": {'description': 'User greeting or hello'},
    "GOODBYE": {'description': 'User saying goodbye'},
    "THANKS": {'description': 'User expressing gratitude'},
    "HELP": {'description': 'User requesting help or assistance'},
    "INFORMATION": {'description': 'User requesting information'},
    "COMPLAINT": {'description': 'User expressing dissatisfaction'},
    "FEEDBACK": {'description': 'User providing feedback'},
    "PURCHASE": {'description': 'User intent to buy or purchase'},
    "CANCEL": {'description': 'User intent to cancel'},
    "REFUND": {'description': 'User requesting refund'},
}

__all__ = [
    "NewsTopicCategoryEnum",
    "ToxicityClassificationEnum",
    "IntentClassificationEnum",
]