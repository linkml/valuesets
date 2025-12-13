"""

Generated from: data_science/emotion_classification.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class BasicEmotionEnum(RichEnum):
    """
    Ekman's six basic emotions commonly used in emotion recognition
    """
    # Enum members
    ANGER = "ANGER"
    DISGUST = "DISGUST"
    FEAR = "FEAR"
    HAPPINESS = "HAPPINESS"
    SADNESS = "SADNESS"
    SURPRISE = "SURPRISE"

# Set metadata after class creation
BasicEmotionEnum._metadata = {
    "ANGER": {'description': 'Feeling of displeasure or hostility', 'meaning': 'MFOEM:000009', 'aliases': ['angry', 'mad']},
    "DISGUST": {'description': 'Feeling of revulsion or strong disapproval', 'meaning': 'MFOEM:000019', 'aliases': ['disgusted', 'repulsed']},
    "FEAR": {'description': 'Feeling of anxiety or apprehension', 'meaning': 'MFOEM:000026', 'aliases': ['afraid', 'scared']},
    "HAPPINESS": {'description': 'Feeling of pleasure or contentment', 'meaning': 'MFOEM:000042', 'aliases': ['happy', 'joy', 'joyful']},
    "SADNESS": {'description': 'Feeling of sorrow or unhappiness', 'meaning': 'MFOEM:000056', 'aliases': ['sad', 'sorrow']},
    "SURPRISE": {'description': 'Feeling of mild astonishment or shock', 'meaning': 'MFOEM:000032', 'aliases': ['surprised', 'shocked']},
}

class ExtendedEmotionEnum(RichEnum):
    """
    Extended emotion set including complex emotions
    """
    # Enum members
    ANGER = "ANGER"
    DISGUST = "DISGUST"
    FEAR = "FEAR"
    HAPPINESS = "HAPPINESS"
    SADNESS = "SADNESS"
    SURPRISE = "SURPRISE"
    CONTEMPT = "CONTEMPT"
    ANTICIPATION = "ANTICIPATION"
    TRUST = "TRUST"
    LOVE = "LOVE"

# Set metadata after class creation
ExtendedEmotionEnum._metadata = {
    "ANGER": {'description': 'Feeling of displeasure or hostility', 'meaning': 'MFOEM:000009'},
    "DISGUST": {'description': 'Feeling of revulsion', 'meaning': 'MFOEM:000019'},
    "FEAR": {'description': 'Feeling of anxiety', 'meaning': 'MFOEM:000026'},
    "HAPPINESS": {'description': 'Feeling of pleasure', 'meaning': 'MFOEM:000042'},
    "SADNESS": {'description': 'Feeling of sorrow', 'meaning': 'MFOEM:000056'},
    "SURPRISE": {'description': 'Feeling of astonishment', 'meaning': 'MFOEM:000032'},
    "CONTEMPT": {'description': 'Feeling that something is worthless', 'meaning': 'MFOEM:000018'},
    "ANTICIPATION": {'description': 'Feeling of excitement about something that will happen', 'meaning': 'MFOEM:000175', 'aliases': ['expectation', 'expectant']},
    "TRUST": {'description': 'Feeling of confidence in someone or something', 'meaning': 'MFOEM:000224'},
    "LOVE": {'description': 'Feeling of deep affection', 'meaning': 'MFOEM:000048'},
}

__all__ = [
    "BasicEmotionEnum",
    "ExtendedEmotionEnum",
]