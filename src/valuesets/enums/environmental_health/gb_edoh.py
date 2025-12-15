"""
Geospatial-Based Environmental Determinants of Health Value Sets

Value sets supporting the NIH/NIEHS Health and Extreme Weather (HEW) Data Accelerator program for standardizing geospatial-based environmental determinants of health (GB-EDoH) data and metadata. These value sets support OMOP integration and environmental epidemiology studies.

Generated from: environmental_health/gb_edoh.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ExtremeWeatherEventEnum(RichEnum):
    """
    Types of extreme weather events relevant to health outcomes and environmental epidemiology. Used for characterizing weather-related health impacts in the NIH Health and Extreme Weather (HEW) program.
    """
    # Enum members
    HEAT_WAVE = "HEAT_WAVE"
    COLD_WAVE = "COLD_WAVE"
    WILDFIRE = "WILDFIRE"
    FOREST_FIRE = "FOREST_FIRE"
    TROPICAL_STORM = "TROPICAL_STORM"
    HURRICANE = "HURRICANE"
    TORNADO = "TORNADO"
    FLOOD = "FLOOD"
    RIVERINE_FLOOD = "RIVERINE_FLOOD"
    COASTAL_FLOOD = "COASTAL_FLOOD"
    FLASH_FLOOD = "FLASH_FLOOD"
    DROUGHT = "DROUGHT"
    BLIZZARD = "BLIZZARD"
    WINTER_STORM = "WINTER_STORM"
    SEVERE_THUNDERSTORM = "SEVERE_THUNDERSTORM"
    DUST_STORM = "DUST_STORM"
    EXTREME_PRECIPITATION = "EXTREME_PRECIPITATION"
    STORM_SURGE = "STORM_SURGE"
    LANDSLIDE = "LANDSLIDE"
    AIR_QUALITY_EVENT = "AIR_QUALITY_EVENT"

# Set metadata after class creation
ExtremeWeatherEventEnum._metadata = {
    "HEAT_WAVE": {'description': 'Prolonged period of excessively hot weather relative to the expected conditions for a given area. Associated with increased mortality, heat stroke, and cardiovascular events.', 'annotations': {'health_impacts': 'heat stroke, cardiovascular events, mortality', 'nws_threshold': '2+ days of heat index >= 105F'}},
    "COLD_WAVE": {'description': 'Prolonged period of excessively cold weather relative to the expected conditions for a given area. Associated with hypothermia and cardiovascular events.', 'annotations': {'health_impacts': 'hypothermia, cardiovascular events, frostbite'}},
    "WILDFIRE": {'description': 'Uncontrolled fire in vegetated areas producing smoke containing particulate matter and hazardous air pollutants. Major source of PM2.5 exposure.', 'meaning': 'ENVO:01000787', 'annotations': {'health_impacts': 'respiratory illness, cardiovascular events, mental health', 'exposure_agent': 'PM2.5, CO, VOCs'}},
    "FOREST_FIRE": {'description': 'Wildfire occurring primarily in forested areas, producing dense smoke plumes that can travel long distances.', 'meaning': 'ENVO:01000791'},
    "TROPICAL_STORM": {'description': 'Atmospheric storm originating over tropical waters with organized circulation and sustained winds 39-73 mph. Precursor to hurricanes.', 'meaning': 'ENVO:01001296', 'annotations': {'health_impacts': 'injuries, drowning, displacement, mental health'}},
    "HURRICANE": {'description': 'Intense tropical cyclone with sustained winds of 74 mph or greater. Called hurricane (Atlantic/E. Pacific), typhoon (W. Pacific), or cyclone (Indian Ocean).', 'annotations': {'saffir_simpson': 'Category 1-5', 'health_impacts': 'traumatic injuries, drowning, displacement, infectious disease', 'related': 'ENVO:01001297'}},
    "TORNADO": {'description': 'Violently rotating column of air extending from a thunderstorm to the ground. Characterized by extreme winds and path of destruction.', 'meaning': 'ENVO:01001482', 'annotations': {'ef_scale': 'EF0-EF5', 'health_impacts': 'traumatic injuries, death, mental health'}},
    "FLOOD": {'description': 'Unusual accumulation of water above ground caused by high tide, heavy rain, melting snow, or dam failure.', 'meaning': 'ENVO:01000710', 'annotations': {'health_impacts': 'drowning, waterborne disease, injuries, displacement'}},
    "RIVERINE_FLOOD": {'description': 'Flood occurring when river flow exceeds channel capacity, typically developing over hours to days.', 'meaning': 'ENVO:01000712'},
    "COASTAL_FLOOD": {'description': 'Flood caused by storm surge, high tides, or sea level rise affecting coastal areas.', 'meaning': 'ENVO:01000711'},
    "FLASH_FLOOD": {'description': 'Rapid flooding of low-lying areas within 6 hours of heavy rainfall or dam failure. Particularly dangerous due to sudden onset.', 'meaning': 'ENVO:01000713'},
    "DROUGHT": {'description': 'Extended period of deficient precipitation resulting in water shortage. Affects water quality, food security, and mental health.', 'meaning': 'ENVO:1000745', 'annotations': {'health_impacts': 'water quality, food insecurity, mental health', 'indices': 'PDSI, SPI, USDM'}},
    "BLIZZARD": {'description': 'Severe snowstorm with sustained winds >= 35 mph and reduced visibility for 3+ hours. Creates dangerous travel conditions and cold exposure risk.', 'meaning': 'ENVO:01000903', 'annotations': {'health_impacts': 'hypothermia, injuries, carbon monoxide poisoning'}},
    "WINTER_STORM": {'description': "Storm producing significant snow, ice, or sleet. Includes ice storms, nor'easters, and lake-effect snow events.", 'annotations': {'health_impacts': 'injuries, hypothermia, carbon monoxide poisoning'}},
    "SEVERE_THUNDERSTORM": {'description': 'Thunderstorm producing hail >= 1 inch, wind gusts >= 58 mph, or a tornado. Source of lightning, flash flooding, and wind damage.', 'meaning': 'ENVO:01001294', 'annotations': {'health_impacts': 'lightning injuries, wind injuries, flash flooding'}},
    "DUST_STORM": {'description': 'Meteorological event with strong winds lifting large amounts of sand and dust into the atmosphere. Reduces visibility and air quality.', 'annotations': {'health_impacts': 'respiratory illness, traffic accidents', 'related': 'haboob, sandstorm'}},
    "EXTREME_PRECIPITATION": {'description': 'Precipitation event exceeding historical norms for intensity or duration. Often precedes flooding events.', 'annotations': {'health_impacts': 'flooding, infrastructure damage'}},
    "STORM_SURGE": {'description': 'Abnormal rise in sea level during a storm, caused by wind pushing water toward shore. Major cause of hurricane-related deaths.', 'meaning': 'ENVO:01000714', 'annotations': {'health_impacts': 'drowning, injuries'}},
    "LANDSLIDE": {'description': 'Mass movement of rock, debris, or earth down a slope. Often triggered by extreme precipitation or earthquakes.', 'annotations': {'health_impacts': 'traumatic injuries, burial, displacement'}},
    "AIR_QUALITY_EVENT": {'description': 'Period of degraded air quality due to pollution accumulation, typically during temperature inversions or stagnant air conditions.', 'annotations': {'health_impacts': 'respiratory illness, cardiovascular events', 'indices': 'AQI, PM2.5, ozone'}},
}

class ExposureAgentCategoryEnum(RichEnum):
    """
    Categories of environmental exposure agents for GB-EDoH classification. Used to categorize the type of environmental factor being measured and modeled in geospatial exposure assessments.
    """
    # Enum members
    CRITERIA_AIR_POLLUTANT = "CRITERIA_AIR_POLLUTANT"
    HAZARDOUS_AIR_POLLUTANT = "HAZARDOUS_AIR_POLLUTANT"
    WILDFIRE_SMOKE = "WILDFIRE_SMOKE"
    WATER_CONTAMINANT = "WATER_CONTAMINANT"
    SOIL_CONTAMINANT = "SOIL_CONTAMINANT"
    RADIONUCLIDE = "RADIONUCLIDE"
    EXTREME_HEAT = "EXTREME_HEAT"
    EXTREME_COLD = "EXTREME_COLD"
    UV_RADIATION = "UV_RADIATION"
    NOISE = "NOISE"
    LIGHT_POLLUTION = "LIGHT_POLLUTION"
    ALLERGEN = "ALLERGEN"
    VECTOR_HABITAT = "VECTOR_HABITAT"
    GREEN_SPACE = "GREEN_SPACE"
    BLUE_SPACE = "BLUE_SPACE"
    BUILT_ENVIRONMENT = "BUILT_ENVIRONMENT"
    SOCIOECONOMIC_DEPRIVATION = "SOCIOECONOMIC_DEPRIVATION"

# Set metadata after class creation
ExposureAgentCategoryEnum._metadata = {
    "CRITERIA_AIR_POLLUTANT": {'description': 'EPA-regulated criteria air pollutants under the Clean Air Act: PM2.5, PM10, O3, NO2, SO2, CO, and Pb.', 'annotations': {'examples': 'PM2.5, PM10, O3, NO2, SO2, CO, Pb', 'regulatory': 'EPA NAAQS'}},
    "HAZARDOUS_AIR_POLLUTANT": {'description': 'EPA-designated hazardous air pollutants (HAPs) known to cause cancer or other serious health effects.', 'annotations': {'examples': 'benzene, formaldehyde, acetaldehyde', 'regulatory': 'EPA HAPs list (187 pollutants)'}},
    "WILDFIRE_SMOKE": {'description': 'Smoke from wildfires containing PM2.5, CO, VOCs, and other combustion products. Distinct from anthropogenic air pollution.', 'annotations': {'components': 'PM2.5, CO, VOCs, PAHs'}},
    "WATER_CONTAMINANT": {'description': 'Chemical, biological, or physical contaminants in drinking water or recreational water bodies.', 'annotations': {'examples': 'lead, arsenic, nitrates, PFAS, pathogens'}},
    "SOIL_CONTAMINANT": {'description': 'Chemical contaminants in soil that may affect health through direct contact, ingestion, or vapor intrusion.', 'annotations': {'examples': 'lead, arsenic, petroleum, pesticides'}},
    "RADIONUCLIDE": {'description': 'Naturally occurring or anthropogenic radioactive materials in the environment, including radon gas.', 'annotations': {'examples': 'radon-222, uranium, radium'}},
    "EXTREME_HEAT": {'description': 'Ambient heat exposure characterized by temperature, heat index, or other thermal comfort metrics.', 'annotations': {'metrics': 'temperature, heat index, WBGT, apparent temperature'}},
    "EXTREME_COLD": {'description': 'Ambient cold exposure characterized by temperature or wind chill.', 'annotations': {'metrics': 'temperature, wind chill'}},
    "UV_RADIATION": {'description': 'Solar ultraviolet radiation exposure, particularly UVB relevant to skin cancer and vitamin D synthesis.', 'annotations': {'metrics': 'UV index, erythemal UV dose'}},
    "NOISE": {'description': 'Ambient noise from traffic, airports, industry, and other sources. Associated with cardiovascular and mental health effects.', 'annotations': {'metrics': 'Lden, Lnight, LAeq'}},
    "LIGHT_POLLUTION": {'description': 'Artificial light at night from urban and industrial sources. Associated with circadian disruption.', 'annotations': {'metrics': 'radiance, sky brightness'}},
    "ALLERGEN": {'description': 'Airborne allergens including pollen, mold spores, and other biological particles triggering allergic responses.', 'annotations': {'examples': 'tree pollen, grass pollen, ragweed, mold spores'}},
    "VECTOR_HABITAT": {'description': 'Environmental conditions favoring disease vector populations (mosquitoes, ticks) based on climate and land use.', 'annotations': {'vectors': 'Aedes mosquitoes, Ixodes ticks', 'diseases': 'dengue, Zika, Lyme disease'}},
    "GREEN_SPACE": {'description': 'Access to and amount of vegetated areas including parks, forests, and urban greenery. Associated with mental and physical health benefits.', 'annotations': {'metrics': 'NDVI, park access, tree canopy cover'}},
    "BLUE_SPACE": {'description': 'Access to and proximity to water bodies including lakes, rivers, and coastal areas.', 'annotations': {'metrics': 'distance to water, water body area'}},
    "BUILT_ENVIRONMENT": {'description': 'Characteristics of the human-made environment including walkability, food access, and housing quality.', 'annotations': {'metrics': 'walkability score, food desert index, housing age'}},
    "SOCIOECONOMIC_DEPRIVATION": {'description': 'Area-level measures of socioeconomic disadvantage that modify or mediate environmental health effects.', 'annotations': {'indices': 'ADI, NDI, SVI'}},
}

class TemporalAggregationEnum(RichEnum):
    """
    Methods used to aggregate environmental exposure data over time. Critical metadata for GB-EDoH to ensure comparability across studies and integration with health outcome data.
    """
    # Enum members
    INSTANTANEOUS = "INSTANTANEOUS"
    HOURLY_MEAN = "HOURLY_MEAN"
    DAILY_MEAN = "DAILY_MEAN"
    DAILY_MAX = "DAILY_MAX"
    DAILY_MIN = "DAILY_MIN"
    DAILY_MAX_8HR = "DAILY_MAX_8HR"
    WEEKLY_MEAN = "WEEKLY_MEAN"
    MONTHLY_MEAN = "MONTHLY_MEAN"
    QUARTERLY_MEAN = "QUARTERLY_MEAN"
    ANNUAL_MEAN = "ANNUAL_MEAN"
    CUMULATIVE = "CUMULATIVE"
    DAYS_ABOVE_THRESHOLD = "DAYS_ABOVE_THRESHOLD"
    PERCENTILE = "PERCENTILE"
    MOVING_AVERAGE = "MOVING_AVERAGE"
    TRIMESTER_MEAN = "TRIMESTER_MEAN"
    HEATING_SEASON_MEAN = "HEATING_SEASON_MEAN"
    COOLING_SEASON_MEAN = "COOLING_SEASON_MEAN"

# Set metadata after class creation
TemporalAggregationEnum._metadata = {
    "INSTANTANEOUS": {'description': 'Single point-in-time measurement without temporal aggregation.', 'annotations': {'example': 'hourly sensor reading'}},
    "HOURLY_MEAN": {'description': 'Arithmetic mean of measurements within a 1-hour window.', 'annotations': {'window': '1 hour'}},
    "DAILY_MEAN": {'description': 'Arithmetic mean of measurements over a 24-hour period. Standard for many EPA air quality standards.', 'annotations': {'window': '24 hours', 'regulatory': 'EPA PM2.5 24-hour standard'}},
    "DAILY_MAX": {'description': 'Maximum value recorded during a 24-hour period.', 'annotations': {'window': '24 hours'}},
    "DAILY_MIN": {'description': 'Minimum value recorded during a 24-hour period.', 'annotations': {'window': '24 hours'}},
    "DAILY_MAX_8HR": {'description': 'Maximum of rolling 8-hour averages within a day. Standard metric for ozone exposure assessment.', 'annotations': {'window': '8-hour rolling within 24 hours', 'regulatory': 'EPA ozone standard'}},
    "WEEKLY_MEAN": {'description': 'Arithmetic mean of daily values over a 7-day period.', 'annotations': {'window': '7 days'}},
    "MONTHLY_MEAN": {'description': 'Arithmetic mean of daily values over a calendar month.', 'annotations': {'window': 'calendar month'}},
    "QUARTERLY_MEAN": {'description': 'Arithmetic mean of daily values over a 3-month period.', 'annotations': {'window': '3 months'}},
    "ANNUAL_MEAN": {'description': 'Arithmetic mean of daily values over a calendar year. Standard for EPA PM2.5 annual standard.', 'annotations': {'window': 'calendar year', 'regulatory': 'EPA PM2.5 annual standard'}},
    "CUMULATIVE": {'description': 'Sum of exposure values over a defined period, representing total dose.', 'annotations': {'example': 'cumulative UV dose, total precipitation'}},
    "DAYS_ABOVE_THRESHOLD": {'description': 'Count of days exceeding a specified threshold value within a period.', 'annotations': {'example': 'days with AQI > 100'}},
    "PERCENTILE": {'description': 'Specified percentile of distribution (e.g., 98th percentile of daily values). Captures extreme exposure events.', 'annotations': {'example': '98th percentile of daily PM2.5'}},
    "MOVING_AVERAGE": {'description': 'Rolling average over a specified window (e.g., 7-day moving average). Smooths short-term variability.', 'annotations': {'example': '7-day rolling average'}},
    "TRIMESTER_MEAN": {'description': 'Mean exposure during a pregnancy trimester. Used in birth outcomes research.', 'annotations': {'window': '~13 weeks', 'use_case': 'perinatal epidemiology'}},
    "HEATING_SEASON_MEAN": {'description': 'Mean during heating season (typically Oct-Mar in Northern Hemisphere). Relevant for indoor air quality.', 'annotations': {'window': 'heating season'}},
    "COOLING_SEASON_MEAN": {'description': 'Mean during cooling season (typically May-Sep in Northern Hemisphere). Relevant for heat exposure and ozone.', 'annotations': {'window': 'cooling season'}},
}

class SpatialResolutionEnum(RichEnum):
    """
    Geographic units and spatial resolutions used for GB-EDoH exposure estimates. Critical metadata for understanding exposure misclassification and supporting OMOP geocoding requirements.
    """
    # Enum members
    POINT_LOCATION = "POINT_LOCATION"
    ADDRESS_GEOCODED = "ADDRESS_GEOCODED"
    CENSUS_BLOCK = "CENSUS_BLOCK"
    CENSUS_BLOCK_GROUP = "CENSUS_BLOCK_GROUP"
    CENSUS_TRACT = "CENSUS_TRACT"
    ZIP_CODE = "ZIP_CODE"
    ZCTA = "ZCTA"
    COUNTY = "COUNTY"
    STATE = "STATE"
    GRID_1KM = "GRID_1KM"
    GRID_4KM = "GRID_4KM"
    GRID_12KM = "GRID_12KM"
    GRID_36KM = "GRID_36KM"
    HUC8 = "HUC8"
    HUC12 = "HUC12"
    AIRSHED = "AIRSHED"
    BUFFER_500M = "BUFFER_500M"
    BUFFER_1KM = "BUFFER_1KM"
    BUFFER_5KM = "BUFFER_5KM"
    CUSTOM_POLYGON = "CUSTOM_POLYGON"

# Set metadata after class creation
SpatialResolutionEnum._metadata = {
    "POINT_LOCATION": {'description': 'Exact geographic coordinates. Highest spatial precision but may require privacy protection measures.', 'annotations': {'precision': 'exact coordinates', 'privacy': 'requires protection'}},
    "ADDRESS_GEOCODED": {'description': 'Address geocoded to rooftop or parcel level. Standard for linking patient data to environmental exposures.', 'annotations': {'precision': 'parcel level', 'use_case': 'patient-level exposure'}},
    "CENSUS_BLOCK": {'description': 'US Census block, the smallest geographic unit. Typically contains 600-3000 people.', 'annotations': {'typical_population': '600-3000', 'country': 'US'}},
    "CENSUS_BLOCK_GROUP": {'description': 'US Census block group, a cluster of blocks. Standard unit for many socioeconomic and environmental datasets.', 'annotations': {'typical_population': '600-3000', 'country': 'US'}},
    "CENSUS_TRACT": {'description': 'US Census tract, designed to be relatively homogeneous in population characteristics. Common for health research.', 'annotations': {'typical_population': '2500-8000', 'country': 'US'}},
    "ZIP_CODE": {'description': 'US Postal Service ZIP code. Common in administrative health data but boundaries change and may cross jurisdictions.', 'annotations': {'typical_population': 'varies widely', 'country': 'US', 'limitations': 'unstable boundaries'}},
    "ZCTA": {'description': 'Census Bureau generalization of ZIP codes with stable boundaries. Preferred over ZIP codes for research.', 'annotations': {'country': 'US', 'advantage': 'stable boundaries'}},
    "COUNTY": {'description': 'County or parish level. Used for many public health surveillance systems and vital statistics.', 'annotations': {'country': 'US', 'use_case': 'vital statistics, surveillance'}},
    "STATE": {'description': 'State or territory level. Coarsest common administrative unit.', 'annotations': {'country': 'US'}},
    "GRID_1KM": {'description': '1 kilometer resolution grid. Common for satellite-derived and modeled air quality data.', 'annotations': {'resolution': '1 km', 'example': 'EPA downscaler output'}},
    "GRID_4KM": {'description': '4 kilometer resolution grid. Common for weather and some air quality models.', 'annotations': {'resolution': '4 km', 'example': 'HRRR weather model'}},
    "GRID_12KM": {'description': '12 kilometer resolution grid. Standard CMAQ model output resolution.', 'annotations': {'resolution': '12 km', 'example': 'EPA CMAQ output'}},
    "GRID_36KM": {'description': '36 kilometer resolution grid. Coarse model output.', 'annotations': {'resolution': '36 km'}},
    "HUC8": {'description': '8-digit Hydrologic Unit Code watershed. Medium-sized watershed for water quality assessment.', 'annotations': {'typical_area': '700 sq mi', 'use_case': 'water quality'}},
    "HUC12": {'description': '12-digit Hydrologic Unit Code subwatershed. Finest watershed unit.', 'annotations': {'typical_area': '40 sq mi', 'use_case': 'local water quality'}},
    "AIRSHED": {'description': 'Geographic area defined by air pollution transport patterns. May cross administrative boundaries.', 'annotations': {'example': 'South Coast Air Basin'}},
    "BUFFER_500M": {'description': 'Circular buffer of 500 meters around a point. Common for traffic-related air pollution exposure.', 'annotations': {'radius': '500 m', 'use_case': 'TRAP exposure'}},
    "BUFFER_1KM": {'description': 'Circular buffer of 1 kilometer around a point.', 'annotations': {'radius': '1 km'}},
    "BUFFER_5KM": {'description': 'Circular buffer of 5 kilometers around a point.', 'annotations': {'radius': '5 km'}},
    "CUSTOM_POLYGON": {'description': 'User-defined geographic area. Requires specification of boundary source.', 'annotations': {'example': 'school district, hospital service area'}},
}

__all__ = [
    "ExtremeWeatherEventEnum",
    "ExposureAgentCategoryEnum",
    "TemporalAggregationEnum",
    "SpatialResolutionEnum",
]