"""
Rich Enum Implementation with Metadata Support

This module provides enums that maintain full compatibility with standard Python 
enums while adding metadata support using __init_subclass__.
"""

from enum import Enum
from typing import Dict, Any, Optional, Type


class RichEnum(str, Enum):
    """
    Base class for enums with metadata support.
    
    This class creates enums that:
    1. Are fully compatible with standard Python enums
    2. Support string values (inherit from str)
    3. Have metadata access methods
    4. Can be looked up by ontology meaning
    
    The metadata should be set AFTER class creation to avoid it becoming
    an enum member.
    
    Usage:
        class MyEnum(RichEnum):
            VALUE1 = "value1"
            VALUE2 = "value2"
        
        # Set metadata after class creation
        MyEnum._metadata = {
            "VALUE1": {
                "description": "First value",
                "meaning": "ONTO:0000001",
                "annotations": {"category": "group1"}
            },
            "VALUE2": {
                "description": "Second value", 
                "meaning": "ONTO:0000002"
            }
        }
    """
    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        
        # Add metadata access methods to the class
        def get_description(self) -> Optional[str]:
            """Get the description for this enum member."""
            metadata = self.__class__.__dict__.get('_metadata', {})
            member_metadata = metadata.get(self.name, {})
            return member_metadata.get("description")
        
        def get_meaning(self) -> Optional[str]:
            """Get the ontology meaning/mapping for this enum member."""
            metadata = self.__class__.__dict__.get('_metadata', {})
            member_metadata = metadata.get(self.name, {})
            return member_metadata.get("meaning")
        
        def get_annotations(self) -> Dict[str, Any]:
            """Get the annotations dictionary for this enum member."""
            metadata = self.__class__.__dict__.get('_metadata', {})
            member_metadata = metadata.get(self.name, {})
            return member_metadata.get("annotations", {})
        
        def get_metadata(self) -> Dict[str, Any]:
            """Get all metadata for this enum member."""
            base = {"name": self.name, "value": self.value}
            metadata = self.__class__.__dict__.get('_metadata', {})
            base.update(metadata.get(self.name, {}))
            return base
        
        @classmethod
        def from_meaning(cls_inner, meaning: str) -> Optional['RichEnum']:
            """
            Find an enum member by its ontology meaning.
            
            Args:
                meaning: The ontology term (e.g., "BSPO:0000000")
                
            Returns:
                The enum member with the given meaning, or None if not found
            """
            for member in cls_inner:
                if member.get_meaning() == meaning:
                    return member
            return None
        
        @classmethod
        def get_all_meanings(cls_inner) -> Dict[str, str]:
            """Get a mapping of all member names to their meanings."""
            meanings = {}
            for member in cls_inner:
                meaning = member.get_meaning()
                if meaning:
                    meanings[member.name] = meaning
            return meanings
        
        @classmethod
        def get_all_descriptions(cls_inner) -> Dict[str, str]:
            """Get a mapping of all member names to their descriptions."""
            descriptions = {}
            for member in cls_inner:
                description = member.get_description()
                if description:
                    descriptions[member.name] = description
            return descriptions
        
        @classmethod
        def list_metadata(cls_inner) -> Dict[str, Dict[str, Any]]:
            """Get all metadata for all members."""
            return {member.name: member.get_metadata() for member in cls_inner}
        
        # Set methods on the class
        setattr(cls, 'get_description', get_description)
        setattr(cls, 'get_meaning', get_meaning) 
        setattr(cls, 'get_annotations', get_annotations)
        setattr(cls, 'get_metadata', get_metadata)
        setattr(cls, 'from_meaning', from_meaning)
        setattr(cls, 'get_all_meanings', get_all_meanings)
        setattr(cls, 'get_all_descriptions', get_all_descriptions)
        setattr(cls, 'list_metadata', list_metadata)


# Type alias for clarity  
RichEnumType = Type[RichEnum]
RichEnumMeta = None  # For backwards compatibility