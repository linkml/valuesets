"""
Research Organizations and Institutions

Value sets for research organizations, institutions, and facilities.

## Guidelines for Organization Identifiers

When mapping organization names to ontology terms, **use ROR (Research Organization Registry) as the primary source**.
ROR provides persistent identifiers for research organizations worldwide and is the preferred standard
for identifying research institutions.

- ROR Homepage: https://ror.org/
- ROR Search: https://ror.org/search
- ROR API: https://api.ror.org/organizations

ROR IDs should be used in the `meaning` field with the full URL format (e.g., https://ror.org/05gvnxz63).


Generated from: academic/organizations.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class USDOENationalLaboratoryEnum(RichEnum):
    """
    United States Department of Energy National Laboratories.
    
    The DOE operates 17 National Laboratories that serve as powerhouses of science and technology,
    tackling critical scientific challenges and conducting cutting-edge research across multiple disciplines.
    
    These laboratories are managed by contractors and stewarded by various DOE program offices,
    with the Office of Science stewarding 10 of the 17 laboratories.
    
    """
    # Enum members
    AMES_LABORATORY = "AMES_LABORATORY"
    ARGONNE_NATIONAL_LABORATORY = "ARGONNE_NATIONAL_LABORATORY"
    BROOKHAVEN_NATIONAL_LABORATORY = "BROOKHAVEN_NATIONAL_LABORATORY"
    FERMI_NATIONAL_ACCELERATOR_LABORATORY = "FERMI_NATIONAL_ACCELERATOR_LABORATORY"
    IDAHO_NATIONAL_LABORATORY = "IDAHO_NATIONAL_LABORATORY"
    LAWRENCE_BERKELEY_NATIONAL_LABORATORY = "LAWRENCE_BERKELEY_NATIONAL_LABORATORY"
    LAWRENCE_LIVERMORE_NATIONAL_LABORATORY = "LAWRENCE_LIVERMORE_NATIONAL_LABORATORY"
    LOS_ALAMOS_NATIONAL_LABORATORY = "LOS_ALAMOS_NATIONAL_LABORATORY"
    NATIONAL_ENERGY_TECHNOLOGY_LABORATORY = "NATIONAL_ENERGY_TECHNOLOGY_LABORATORY"
    NATIONAL_RENEWABLE_ENERGY_LABORATORY = "NATIONAL_RENEWABLE_ENERGY_LABORATORY"
    OAK_RIDGE_NATIONAL_LABORATORY = "OAK_RIDGE_NATIONAL_LABORATORY"
    PACIFIC_NORTHWEST_NATIONAL_LABORATORY = "PACIFIC_NORTHWEST_NATIONAL_LABORATORY"
    PRINCETON_PLASMA_PHYSICS_LABORATORY = "PRINCETON_PLASMA_PHYSICS_LABORATORY"
    SANDIA_NATIONAL_LABORATORIES = "SANDIA_NATIONAL_LABORATORIES"
    SAVANNAH_RIVER_NATIONAL_LABORATORY = "SAVANNAH_RIVER_NATIONAL_LABORATORY"
    SLAC_NATIONAL_ACCELERATOR_LABORATORY = "SLAC_NATIONAL_ACCELERATOR_LABORATORY"
    THOMAS_JEFFERSON_NATIONAL_ACCELERATOR_FACILITY = "THOMAS_JEFFERSON_NATIONAL_ACCELERATOR_FACILITY"

# Set metadata after class creation
USDOENationalLaboratoryEnum._metadata = {
    "AMES_LABORATORY": {'description': 'National laboratory focused on materials science and chemistry research', 'meaning': 'ROR:041m9xr71', 'annotations': {'location': 'Ames, Iowa', 'established': 1947, 'stewarding_office': 'Office of Science', 'website': 'https://www.ameslab.gov/'}},
    "ARGONNE_NATIONAL_LABORATORY": {'description': 'Multidisciplinary science and engineering research center', 'meaning': 'ROR:05gvnxz63', 'annotations': {'location': 'Lemont, Illinois', 'established': 1946, 'stewarding_office': 'Office of Science', 'website': 'https://www.anl.gov/'}},
    "BROOKHAVEN_NATIONAL_LABORATORY": {'description': 'Research center for nuclear and high-energy physics', 'meaning': 'ROR:02ex6cf31', 'annotations': {'location': 'Upton, New York', 'established': 1947, 'stewarding_office': 'Office of Science', 'website': 'https://www.bnl.gov/'}},
    "FERMI_NATIONAL_ACCELERATOR_LABORATORY": {'description': 'Particle physics and accelerator research laboratory', 'meaning': 'ROR:020hgte69', 'annotations': {'location': 'Batavia, Illinois', 'established': 1967, 'stewarding_office': 'Office of Science', 'website': 'https://www.fnal.gov/'}, 'aliases': ['Fermilab']},
    "IDAHO_NATIONAL_LABORATORY": {'description': 'Nuclear energy research and national security laboratory', 'meaning': 'ROR:00ty2a548', 'annotations': {'location': 'Idaho Falls, Idaho', 'established': 1949, 'stewarding_office': 'Office of Nuclear Energy', 'website': 'https://inl.gov/'}},
    "LAWRENCE_BERKELEY_NATIONAL_LABORATORY": {'description': 'Multidisciplinary research laboratory', 'meaning': 'ROR:02jbv0t02', 'annotations': {'location': 'Berkeley, California', 'established': 1931, 'stewarding_office': 'Office of Science', 'website': 'https://www.lbl.gov/'}, 'aliases': ['Berkeley Lab', 'LBNL']},
    "LAWRENCE_LIVERMORE_NATIONAL_LABORATORY": {'description': 'National security laboratory focused on nuclear weapons and advanced technology', 'meaning': 'ROR:041nk4h53', 'annotations': {'location': 'Livermore, California', 'established': 1952, 'stewarding_office': 'National Nuclear Security Administration', 'website': 'https://www.llnl.gov/'}, 'aliases': ['LLNL']},
    "LOS_ALAMOS_NATIONAL_LABORATORY": {'description': 'Multidisciplinary research institution for national security', 'meaning': 'ROR:01e41cf67', 'annotations': {'location': 'Los Alamos, New Mexico', 'established': 1943, 'stewarding_office': 'National Nuclear Security Administration', 'website': 'https://www.lanl.gov/'}, 'aliases': ['LANL']},
    "NATIONAL_ENERGY_TECHNOLOGY_LABORATORY": {'description': 'Federal research laboratory focused on energy and environmental technology', 'meaning': 'ROR:01x26mz03', 'annotations': {'location': 'Pittsburgh, Pennsylvania and Morgantown, West Virginia', 'established': 1910, 'stewarding_office': 'Office of Fossil Energy and Carbon Management', 'website': 'https://www.netl.doe.gov/'}, 'aliases': ['NETL']},
    "NATIONAL_RENEWABLE_ENERGY_LABORATORY": {'description': 'Research and development laboratory focused on renewable energy and energy efficiency', 'meaning': 'ROR:036266993', 'annotations': {'location': 'Golden, Colorado', 'established': 1977, 'stewarding_office': 'Office of Energy Efficiency and Renewable Energy', 'website': 'https://www.nrel.gov/'}, 'aliases': ['NREL']},
    "OAK_RIDGE_NATIONAL_LABORATORY": {'description': 'Multidisciplinary science and technology laboratory', 'meaning': 'ROR:01qz5mb56', 'annotations': {'location': 'Oak Ridge, Tennessee', 'established': 1943, 'stewarding_office': 'Office of Science', 'website': 'https://www.ornl.gov/'}, 'aliases': ['ORNL']},
    "PACIFIC_NORTHWEST_NATIONAL_LABORATORY": {'description': 'Research laboratory focused on energy, environment, and national security', 'meaning': 'ROR:05h992307', 'annotations': {'location': 'Richland, Washington', 'established': 1965, 'stewarding_office': 'Office of Science', 'website': 'https://www.pnnl.gov/'}, 'aliases': ['PNNL']},
    "PRINCETON_PLASMA_PHYSICS_LABORATORY": {'description': 'Plasma physics and fusion energy research laboratory', 'meaning': 'ROR:03vn1ts68', 'annotations': {'location': 'Princeton, New Jersey', 'established': 1951, 'stewarding_office': 'Office of Science', 'website': 'https://www.pppl.gov/'}, 'aliases': ['PPPL']},
    "SANDIA_NATIONAL_LABORATORIES": {'description': 'Multimission laboratory for national security and technology innovation', 'meaning': 'ROR:01apwpt12', 'annotations': {'location': 'Albuquerque, New Mexico and Livermore, California', 'established': 1949, 'stewarding_office': 'National Nuclear Security Administration', 'website': 'https://www.sandia.gov/'}, 'aliases': ['Sandia', 'SNL']},
    "SAVANNAH_RIVER_NATIONAL_LABORATORY": {'description': 'Applied research laboratory for environmental and national security missions', 'meaning': 'ROR:05vc7qy59', 'annotations': {'location': 'Aiken, South Carolina', 'established': 1951, 'stewarding_office': 'Office of Environmental Management', 'website': 'https://www.srnl.gov/'}, 'aliases': ['SRNL']},
    "SLAC_NATIONAL_ACCELERATOR_LABORATORY": {'description': 'Particle physics and photon science research laboratory', 'meaning': 'ROR:05gzmn429', 'annotations': {'location': 'Menlo Park, California', 'established': 1962, 'stewarding_office': 'Office of Science', 'website': 'https://www6.slac.stanford.edu/'}, 'aliases': ['SLAC']},
    "THOMAS_JEFFERSON_NATIONAL_ACCELERATOR_FACILITY": {'description': 'Nuclear physics research laboratory with particle accelerator', 'meaning': 'ROR:02vwzrd76', 'annotations': {'location': 'Newport News, Virginia', 'established': 1984, 'stewarding_office': 'Office of Science', 'website': 'https://www.jlab.org/'}, 'aliases': ['Jefferson Lab', 'JLab']},
}

class USFederalFundingAgencyEnum(RichEnum):
    """
    Major United States Federal Research Funding Agencies.
    
    These agencies provide funding for basic and applied research across various scientific disciplines,
    supporting universities, national laboratories, and other research institutions.
    
    """
    # Enum members
    NIH = "NIH"
    NSF = "NSF"
    DOE = "DOE"
    NASA = "NASA"
    EPA = "EPA"
    NOAA = "NOAA"
    NIST = "NIST"
    USDA_ARS = "USDA_ARS"
    DOD = "DOD"
    USGS = "USGS"

# Set metadata after class creation
USFederalFundingAgencyEnum._metadata = {
    "NIH": {'description': 'Primary federal agency for biomedical and public health research', 'meaning': 'ROR:01cwqze88', 'annotations': {'parent_department': 'Department of Health and Human Services', 'website': 'https://www.nih.gov/', 'established': 1887}, 'aliases': ['National Institutes of Health']},
    "NSF": {'description': 'Federal agency supporting fundamental research and education in non-medical fields', 'meaning': 'ROR:021nxhr62', 'annotations': {'website': 'https://www.nsf.gov/', 'established': 1950}, 'aliases': ['National Science Foundation']},
    "DOE": {'description': 'Federal department overseeing energy policy and nuclear weapons program', 'meaning': 'ROR:01bj3aw27', 'annotations': {'website': 'https://www.energy.gov/', 'established': 1977}, 'aliases': ['Department of Energy', 'U.S. Department of Energy']},
    "NASA": {'description': 'Federal agency responsible for civil space program and aeronautics research', 'meaning': 'ROR:027ka1x80', 'annotations': {'website': 'https://www.nasa.gov/', 'established': 1958}},
    "EPA": {'description': 'Federal agency protecting human health and the environment', 'meaning': 'ROR:03tns0030', 'annotations': {'website': 'https://www.epa.gov/', 'established': 1970}, 'aliases': ['U.S. Environmental Protection Agency']},
    "NOAA": {'description': 'Federal agency focused on ocean, atmosphere, and coastal research', 'meaning': 'ROR:02z5nhe81', 'annotations': {'parent_department': 'Department of Commerce', 'website': 'https://www.noaa.gov/', 'established': 1970}},
    "NIST": {'description': 'Federal agency promoting innovation and industrial competitiveness', 'meaning': 'ROR:05xpvk416', 'annotations': {'parent_department': 'Department of Commerce', 'website': 'https://www.nist.gov/', 'established': 1901}},
    "USDA_ARS": {'description': 'Principal research agency of the U.S. Department of Agriculture', 'meaning': 'ROR:02d2m2044', 'annotations': {'parent_department': 'Department of Agriculture', 'website': 'https://www.ars.usda.gov/', 'established': 1953}, 'aliases': ['USDA ARS']},
    "DOD": {'description': 'Federal department responsible for military research and development', 'meaning': 'ROR:0447fe631', 'annotations': {'website': 'https://www.defense.gov/', 'established': 1947}, 'aliases': ['Department of Defense', 'U.S. Department of Defense']},
    "USGS": {'description': 'Federal agency for earth science research and monitoring', 'meaning': 'ROR:035a68863', 'annotations': {'parent_department': 'Department of the Interior', 'website': 'https://www.usgs.gov/', 'established': 1879}},
}

class NIHInstituteCenterEnum(RichEnum):
    """
    National Institutes of Health (NIH) Institutes and Centers.
    
    NIH comprises 27 Institutes and Centers, each with a specific research agenda focused on particular
    diseases or body systems. These are the major NIH ICs that fund extramural research.
    
    """
    # Enum members
    NCI = "NCI"
    NHLBI = "NHLBI"
    NIAID = "NIAID"
    NIMH = "NIMH"
    NINDS = "NINDS"
    NIDDK = "NIDDK"
    NHGRI = "NHGRI"
    NIGMS = "NIGMS"
    NIEHS = "NIEHS"
    NEI = "NEI"
    NIA = "NIA"
    NLM = "NLM"

# Set metadata after class creation
NIHInstituteCenterEnum._metadata = {
    "NCI": {'description': 'NIH institute for cancer research and training', 'meaning': 'ROR:02t771148', 'annotations': {'parent_organization': 'National Institutes of Health', 'website': 'https://www.cancer.gov/', 'established': 1937}, 'aliases': ['National Cancer Institute']},
    "NHLBI": {'description': 'NIH institute for heart, lung, and blood diseases research', 'meaning': 'ROR:012pb6c26', 'annotations': {'parent_organization': 'National Institutes of Health', 'website': 'https://www.nhlbi.nih.gov/', 'established': 1948}, 'aliases': ['National Heart, Lung, and Blood Institute']},
    "NIAID": {'description': 'NIH institute for infectious, immunologic, and allergic diseases research', 'meaning': 'ROR:043z4tv69', 'annotations': {'parent_organization': 'National Institutes of Health', 'website': 'https://www.niaid.nih.gov/', 'established': 1948}},
    "NIMH": {'description': 'NIH institute for mental health research', 'meaning': 'ROR:04t0s7x83', 'annotations': {'parent_organization': 'National Institutes of Health', 'website': 'https://www.nimh.nih.gov/', 'established': 1949}},
    "NINDS": {'description': 'NIH institute for neurological disorders research', 'meaning': 'ROR:01s5ya894', 'annotations': {'parent_organization': 'National Institutes of Health', 'website': 'https://www.ninds.nih.gov/', 'established': 1950}},
    "NIDDK": {'description': 'NIH institute for diabetes, digestive, and kidney diseases research', 'meaning': 'ROR:00adh9b73', 'annotations': {'parent_organization': 'National Institutes of Health', 'website': 'https://www.niddk.nih.gov/', 'established': 1950}},
    "NHGRI": {'description': 'NIH institute for genomics and genetics research', 'meaning': 'ROR:00baak391', 'annotations': {'parent_organization': 'National Institutes of Health', 'website': 'https://www.genome.gov/', 'established': 1989}},
    "NIGMS": {'description': 'NIH institute supporting basic biomedical research', 'meaning': 'ROR:04q48ey07', 'annotations': {'parent_organization': 'National Institutes of Health', 'website': 'https://www.nigms.nih.gov/', 'established': 1962}},
    "NIEHS": {'description': 'NIH institute for environmental health sciences research', 'meaning': 'ROR:00j4k1h63', 'annotations': {'parent_organization': 'National Institutes of Health', 'website': 'https://www.niehs.nih.gov/', 'established': 1966}},
    "NEI": {'description': 'NIH institute for vision and eye disease research', 'meaning': 'ROR:03wkg3b53', 'annotations': {'parent_organization': 'National Institutes of Health', 'website': 'https://www.nei.nih.gov/', 'established': 1968}},
    "NIA": {'description': 'NIH institute for aging research', 'meaning': 'ROR:049v75w11', 'annotations': {'parent_organization': 'National Institutes of Health', 'website': 'https://www.nia.nih.gov/', 'established': 1974}},
    "NLM": {'description': "World's largest biomedical library and NIH component", 'meaning': 'ROR:0060t0j89', 'annotations': {'parent_organization': 'National Institutes of Health', 'website': 'https://www.nlm.nih.gov/', 'established': 1956}, 'aliases': ['National Library of Medicine']},
}

class StandardsOrganizationEnum(RichEnum):
    """
    Major International Standards Development Organizations.
    
    These organizations develop technical standards, specifications, and guidelines used globally
    across various industries including information technology, healthcare, and engineering.
    
    """
    # Enum members
    ISO = "ISO"
    W3C = "W3C"
    IEEE = "IEEE"
    HL7 = "HL7"

# Set metadata after class creation
StandardsOrganizationEnum._metadata = {
    "ISO": {'description': 'International standard-setting body for industrial and commercial standards', 'meaning': 'ROR:004s85t07', 'annotations': {'website': 'https://www.iso.org/', 'established': 1947, 'headquarters': 'Geneva, Switzerland'}},
    "W3C": {'description': 'International standards organization for World Wide Web standards', 'meaning': 'ROR:0059y1582', 'annotations': {'website': 'https://www.w3.org/', 'established': 1994, 'headquarters': 'Cambridge, Massachusetts'}},
    "IEEE": {'description': 'Professional association for electronic and electrical engineering', 'meaning': 'ROR:01n002310', 'annotations': {'website': 'https://www.ieee.org/', 'established': 1963, 'headquarters': 'New York, USA'}},
    "HL7": {'description': 'Standards development organization for healthcare information exchange', 'meaning': 'ROR:029ga8k16', 'annotations': {'website': 'https://www.hl7.org/', 'established': 1987, 'headquarters': 'Ann Arbor, Michigan'}, 'aliases': ['Health Level Seven']},
}

class UNSpecializedAgencyEnum(RichEnum):
    """
    United Nations Specialized Agencies.
    
    UN specialized agencies are autonomous international organizations that coordinate their work
    with the UN through negotiated agreements. They address international issues in their respective fields.
    
    """
    # Enum members
    WHO = "WHO"
    UNESCO = "UNESCO"
    IAEA = "IAEA"
    WMO = "WMO"
    UNEP = "UNEP"

# Set metadata after class creation
UNSpecializedAgencyEnum._metadata = {
    "WHO": {'description': 'UN agency for international public health', 'meaning': 'ROR:01f80g185', 'annotations': {'website': 'https://www.who.int/', 'established': 1948, 'headquarters': 'Geneva, Switzerland'}},
    "UNESCO": {'description': 'UN Educational, Scientific and Cultural Organization', 'meaning': 'ROR:04h4z8k05', 'annotations': {'website': 'https://www.unesco.org/', 'established': 1945, 'headquarters': 'Paris, France'}, 'aliases': ['United Nations Educational, Scientific and Cultural Organization']},
    "IAEA": {'description': 'International organization promoting peaceful use of nuclear energy', 'meaning': 'ROR:00gtfax65', 'annotations': {'website': 'https://www.iaea.org/', 'established': 1957, 'headquarters': 'Vienna, Austria'}},
    "WMO": {'description': 'UN agency for weather, climate and water resources', 'meaning': 'ROR:011pjwf87', 'annotations': {'website': 'https://public.wmo.int/', 'established': 1950, 'headquarters': 'Geneva, Switzerland'}},
    "UNEP": {'description': 'UN program coordinating environmental activities', 'meaning': 'ROR:015z29x25', 'annotations': {'website': 'https://www.unep.org/', 'established': 1972, 'headquarters': 'Nairobi, Kenya'}},
}

__all__ = [
    "USDOENationalLaboratoryEnum",
    "USFederalFundingAgencyEnum",
    "NIHInstituteCenterEnum",
    "StandardsOrganizationEnum",
    "UNSpecializedAgencyEnum",
]