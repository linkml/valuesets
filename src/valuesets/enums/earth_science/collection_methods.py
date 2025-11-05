"""
Earth Science Sample Collection Methods

Methods for collecting earth samples, based on SESAR (System for Earth Sample Registration) vocabulary

Generated from: earth_science/collection_methods.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class SESARCollectionMethod(RichEnum):
    """
    Sample collection methods as defined by SESAR (System for Earth Sample Registration). These describe the method by which a sample was collected.
    """
    # Enum members
    BLASTING = "BLASTING"
    CAMERA_SLED = "CAMERA_SLED"
    CORING = "CORING"
    CORING_BOX_CORER = "CORING_BOX_CORER"
    CORING_CAMERA_MOUNTED = "CORING_CAMERA_MOUNTED"
    CORING_DRILL_CORER = "CORING_DRILL_CORER"
    CORING_FREE_FALL_CORER = "CORING_FREE_FALL_CORER"
    CORING_GRAVITY = "CORING_GRAVITY"
    CORING_HAND_HELD = "CORING_HAND_HELD"
    CORING_KASTENLOT = "CORING_KASTENLOT"
    CORING_MULTI = "CORING_MULTI"
    CORING_PISTON = "CORING_PISTON"
    CORING_ROCK = "CORING_ROCK"
    CORING_SIDE_SADDLE = "CORING_SIDE_SADDLE"
    CORING_SUBMERSIBLE_MOUNTED = "CORING_SUBMERSIBLE_MOUNTED"
    CORING_TRIGGER_WEIGHT = "CORING_TRIGGER_WEIGHT"
    CORING_VIBRATING = "CORING_VIBRATING"
    DREDGING = "DREDGING"
    DREDGING_CHAIN_BAG = "DREDGING_CHAIN_BAG"
    DREDGING_CHAIN_BAG_DREDGE = "DREDGING_CHAIN_BAG_DREDGE"
    EXPERIMENTAL_APPARATUS = "EXPERIMENTAL_APPARATUS"
    GRAB = "GRAB"
    GRAB_HOV = "GRAB_HOV"
    GRAB_ROV = "GRAB_ROV"
    MANUAL = "MANUAL"
    MANUAL_HAMMER = "MANUAL_HAMMER"
    PROBE = "PROBE"
    SEDIMENT_TRAP = "SEDIMENT_TRAP"
    SUSPENDED_SEDIMENT = "SUSPENDED_SEDIMENT"
    UNKNOWN = "UNKNOWN"

# Set metadata after class creation
SESARCollectionMethod._metadata = {
    "BLASTING": {'description': 'Sample collected using blasting techniques'},
    "CAMERA_SLED": {'description': 'Sample collected via camera sled or camera tow', 'annotations': {'aliases': 'Camera tow'}},
    "CORING": {'description': 'Sample collected using coring techniques'},
    "CORING_BOX_CORER": {'description': 'Sample collected using a box corer', 'annotations': {'parent_method': 'Coring'}},
    "CORING_CAMERA_MOUNTED": {'description': 'Sample collected using camera-mounted corer', 'annotations': {'parent_method': 'Coring'}},
    "CORING_DRILL_CORER": {'description': 'Sample collected using a drill corer', 'annotations': {'parent_method': 'Coring'}},
    "CORING_FREE_FALL_CORER": {'description': 'Sample collected using a free-fall corer', 'annotations': {'parent_method': 'Coring'}},
    "CORING_GRAVITY": {'description': 'Sample collected using a gravity corer', 'annotations': {'parent_method': 'Coring'}},
    "CORING_HAND_HELD": {'description': 'Sample collected using a hand-held corer', 'annotations': {'parent_method': 'Coring'}},
    "CORING_KASTENLOT": {'description': 'Sample collected using a kastenlot corer', 'annotations': {'parent_method': 'Coring'}},
    "CORING_MULTI": {'description': 'Sample collected using a multi-corer', 'annotations': {'parent_method': 'Coring'}},
    "CORING_PISTON": {'description': 'Sample collected using a piston corer', 'annotations': {'parent_method': 'Coring'}},
    "CORING_ROCK": {'description': 'Sample collected using a rock corer', 'annotations': {'parent_method': 'Coring'}},
    "CORING_SIDE_SADDLE": {'description': 'Sample collected using a side saddle corer', 'annotations': {'parent_method': 'Coring'}},
    "CORING_SUBMERSIBLE_MOUNTED": {'description': 'Sample collected using a submersible-mounted corer', 'annotations': {'parent_method': 'Coring'}},
    "CORING_TRIGGER_WEIGHT": {'description': 'Sample collected using a trigger weight corer', 'annotations': {'parent_method': 'Coring'}},
    "CORING_VIBRATING": {'description': 'Sample collected using a vibrating corer', 'annotations': {'parent_method': 'Coring'}},
    "DREDGING": {'description': 'Sample collected by dredging'},
    "DREDGING_CHAIN_BAG": {'description': 'Sample collected using a chain bag dredge', 'annotations': {'parent_method': 'Dredging'}},
    "DREDGING_CHAIN_BAG_DREDGE": {'description': 'Sample collected using a chain bag dredge', 'annotations': {'parent_method': 'Dredging'}},
    "EXPERIMENTAL_APPARATUS": {'description': 'Sample collected using experimental apparatus'},
    "GRAB": {'description': 'Sample collected using a grab sampler'},
    "GRAB_HOV": {'description': 'Sample collected using Human-Occupied Vehicle grab', 'annotations': {'parent_method': 'Grab', 'full_name': 'Human-Occupied Vehicle'}},
    "GRAB_ROV": {'description': 'Sample collected using Remotely Operated Vehicle grab', 'annotations': {'parent_method': 'Grab', 'full_name': 'Remotely Operated Vehicle'}},
    "MANUAL": {'description': 'Sample collected manually'},
    "MANUAL_HAMMER": {'description': 'Sample collected manually using a hammer', 'annotations': {'parent_method': 'Manual'}},
    "PROBE": {'description': 'Sample collected using a probe'},
    "SEDIMENT_TRAP": {'description': 'Sample collected using a sediment trap'},
    "SUSPENDED_SEDIMENT": {'description': 'Suspended sediment sample'},
    "UNKNOWN": {'description': 'Collection method unknown'},
}

__all__ = [
    "SESARCollectionMethod",
]