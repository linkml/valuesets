"""
Remote Sensing Value Sets

Value sets for remote sensing data types and platforms used in earth observation and subsurface characterization

Generated from: earth_science/remote_sensing.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class RemoteSensingPlatformType(RichEnum):
    """
    Classification of platforms used to carry remote sensing instruments for earth observation and environmental monitoring.
    """
    # Enum members
    SATELLITE = "SATELLITE"
    AIRBORNE = "AIRBORNE"
    UAV_DRONE = "UAV_DRONE"
    GROUND_BASED = "GROUND_BASED"
    SHIPBORNE = "SHIPBORNE"

# Set metadata after class creation
RemoteSensingPlatformType._metadata = {
    "SATELLITE": {'description': 'An artificial satellite orbiting Earth carrying remote sensing instruments'},
    "AIRBORNE": {'description': 'A manned aircraft carrying remote sensing instruments'},
    "UAV_DRONE": {'description': 'An unmanned aerial vehicle or drone carrying remote sensing instruments', 'annotations': {'aliases': 'UAV, drone'}},
    "GROUND_BASED": {'description': 'A stationary or mobile ground-based platform carrying remote sensing instruments'},
    "SHIPBORNE": {'description': 'A watercraft carrying remote sensing instruments for maritime or coastal observation'},
}

class RemoteSensingDataType(RichEnum):
    """
    Classification of data types acquired by remote sensing instruments, covering electromagnetic and potential field measurements.
    """
    # Enum members
    MULTISPECTRAL = "MULTISPECTRAL"
    HYPERSPECTRAL = "HYPERSPECTRAL"
    SYNTHETIC_APERTURE_RADAR = "SYNTHETIC_APERTURE_RADAR"
    LIDAR = "LIDAR"
    THERMAL_INFRARED = "THERMAL_INFRARED"
    MICROWAVE_RADIOMETRY = "MICROWAVE_RADIOMETRY"
    GRAVIMETRY = "GRAVIMETRY"
    MAGNETOMETRY = "MAGNETOMETRY"
    PHOTOGRAMMETRY = "PHOTOGRAMMETRY"

# Set metadata after class creation
RemoteSensingDataType._metadata = {
    "MULTISPECTRAL": {'description': 'Imagery acquired in a limited number of discrete spectral bands across the electromagnetic spectrum'},
    "HYPERSPECTRAL": {'description': 'Imagery acquired in many narrow, contiguous spectral bands providing detailed spectral information'},
    "SYNTHETIC_APERTURE_RADAR": {'description': 'Radar imagery produced by synthesizing a large antenna aperture from a moving platform to achieve high spatial resolution', 'annotations': {'abbreviation': 'SAR'}},
    "LIDAR": {'description': 'Active remote sensing data acquired by measuring the time delay of reflected laser pulses to determine distances and surface topography', 'annotations': {'full_name': 'Light Detection And Ranging'}},
    "THERMAL_INFRARED": {'description': 'Imagery acquired in the thermal infrared portion of the spectrum, measuring emitted thermal radiation'},
    "MICROWAVE_RADIOMETRY": {'description': "Passive measurement of naturally emitted microwave radiation from the Earth's surface and atmosphere"},
    "GRAVIMETRY": {'description': 'Measurement of variations in the gravitational field from airborne or satellite platforms'},
    "MAGNETOMETRY": {'description': 'Measurement of variations in the magnetic field from airborne or satellite platforms'},
    "PHOTOGRAMMETRY": {'description': 'The science of making measurements from photographs or imagery, typically to produce 3D models or maps'},
}

__all__ = [
    "RemoteSensingPlatformType",
    "RemoteSensingDataType",
]