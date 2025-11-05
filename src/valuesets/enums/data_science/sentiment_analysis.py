"""

Generated from: data_science/sentiment_analysis.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class SentimentClassificationEnum(RichEnum):
    """
    Standard labels for sentiment analysis classification tasks
    """
    # Enum members
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    NEUTRAL = "NEUTRAL"

# Set metadata after class creation
SentimentClassificationEnum._metadata = {
    "POSITIVE": {'description': 'Positive sentiment or opinion', 'meaning': 'NCIT:C38758', 'aliases': ['pos', '1', '+']},
    "NEGATIVE": {'description': 'Negative sentiment or opinion', 'meaning': 'NCIT:C35681', 'aliases': ['neg', '0', '-']},
    "NEUTRAL": {'description': 'Neutral sentiment, neither positive nor negative', 'meaning': 'NCIT:C14165', 'aliases': ['neu', '2']},
}

class FineSentimentClassificationEnum(RichEnum):
    """
    Fine-grained sentiment analysis labels with intensity levels
    """
    # Enum members
    VERY_POSITIVE = "VERY_POSITIVE"
    POSITIVE = "POSITIVE"
    NEUTRAL = "NEUTRAL"
    NEGATIVE = "NEGATIVE"
    VERY_NEGATIVE = "VERY_NEGATIVE"

# Set metadata after class creation
FineSentimentClassificationEnum._metadata = {
    "VERY_POSITIVE": {'description': 'Strongly positive sentiment', 'meaning': 'NCIT:C38758', 'aliases': ['5', '++']},
    "POSITIVE": {'description': 'Positive sentiment', 'meaning': 'NCIT:C38758', 'aliases': ['4', '+']},
    "NEUTRAL": {'description': 'Neutral sentiment', 'meaning': 'NCIT:C14165', 'aliases': ['3', '0']},
    "NEGATIVE": {'description': 'Negative sentiment', 'meaning': 'NCIT:C35681', 'aliases': ['2', '-']},
    "VERY_NEGATIVE": {'description': 'Strongly negative sentiment', 'meaning': 'NCIT:C35681', 'aliases': ['1', '--']},
}

__all__ = [
    "SentimentClassificationEnum",
    "FineSentimentClassificationEnum",
]