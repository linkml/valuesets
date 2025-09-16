"""Comparison utilities for enum values."""

from enum import Enum
from typing import Any, Optional, Union


def same_meaning_as(enum1: Any, enum2: Any) -> Optional[bool]:
    """
    Check if two enum values have the same semantic meaning.
    
    This function compares the 'meaning' attribute of two enum values.
    For rich enums generated from LinkML schemas, this will be the ontology term CURIE.
    For standard Python enums without a meaning attribute, this returns None.
    
    Args:
        enum1: First enum value to compare
        enum2: Second enum value to compare
        
    Returns:
        True if both enums have the same meaning
        False if both enums have meanings but they differ
        None if either enum lacks a meaning attribute
        
    Examples:
        >>> from enum import Enum
        
        # Create test enums with and without meaning attributes
        >>> class EnumWithMeaning(Enum):
        ...     VALUE1 = "val1"
        ...     VALUE2 = "val2"
        ...     def __init__(self, value):
        ...         self._value_ = value
        ...         # Simulate meaning attribute for some values
        ...         if self.name == 'VALUE1':
        ...             self.meaning = "ONTOLOGY:123"
        ...         elif self.name == 'VALUE2':
        ...             self.meaning = "ONTOLOGY:456"
        
        >>> class AnotherEnumWithMeaning(Enum):
        ...     ITEM1 = "item1"
        ...     ITEM2 = "item2"
        ...     def __init__(self, value):
        ...         self._value_ = value
        ...         # Same meaning as VALUE1
        ...         if self.name == 'ITEM1':
        ...             self.meaning = "ONTOLOGY:123"
        ...         elif self.name == 'ITEM2':
        ...             self.meaning = "ONTOLOGY:789"
        
        # Test with enums that have same meaning
        >>> same_meaning_as(EnumWithMeaning.VALUE1, AnotherEnumWithMeaning.ITEM1)
        True
        
        # Test with enums that have different meanings
        >>> same_meaning_as(EnumWithMeaning.VALUE1, EnumWithMeaning.VALUE2)
        False
        
        # Test with standard Python enum (no meaning attribute)
        >>> class StandardEnum(Enum):
        ...     VALUE1 = "val1"
        ...     VALUE2 = "val2"
        >>> same_meaning_as(StandardEnum.VALUE1, StandardEnum.VALUE2) is None
        True
        
        # Test mixed case - one has meaning, one doesn't
        >>> same_meaning_as(EnumWithMeaning.VALUE1, StandardEnum.VALUE1) is None
        True
        
        # Test with non-enum values
        >>> same_meaning_as("not_enum", EnumWithMeaning.VALUE1) is None
        True
        
        # Test with None values
        >>> same_meaning_as(None, EnumWithMeaning.VALUE1) is None
        True
        
        # Test identity case
        >>> same_meaning_as(EnumWithMeaning.VALUE1, EnumWithMeaning.VALUE1)
        True
    """
    # Handle None or non-enum inputs
    if enum1 is None or enum2 is None:
        return None
        
    if not isinstance(enum1, Enum) or not isinstance(enum2, Enum):
        return None
    
    # Check if both enums have meaning attributes
    meaning1 = getattr(enum1, 'meaning', None)
    meaning2 = getattr(enum2, 'meaning', None)
    
    # If either doesn't have a meaning, return None
    if meaning1 is None or meaning2 is None:
        return None
        
    # Both have meanings - compare them
    return meaning1 == meaning2


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)