"""
INSDC Geographic Location Vocabulary

INSDC controlled vocabulary for geographic locations used in sequence records.
This vocabulary is used for the /geo_loc_name qualifier in INSDC databases (GenBank, ENA, DDBJ).
Countries are mapped to ISO 3166-1 alpha-2 codes using Library of Congress URIs.
Source: https://www.insdc.org/submitting-standards/geo_loc_name-qualifier-vocabulary/

Generated from: bio/insdc_geographic_locations.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class InsdcGeographicLocationEnum(RichEnum):
    """
    INSDC controlled vocabulary for geographic locations of collected samples.
    Includes countries, oceans, seas, and other geographic regions as defined by INSDC.
    Countries use ISO 3166-1 alpha-2 codes from Library of Congress as canonical identifiers.
    """
    # Enum members
    AFGHANISTAN = "AFGHANISTAN"
    ALBANIA = "ALBANIA"
    ALGERIA = "ALGERIA"
    AMERICAN_SAMOA = "AMERICAN_SAMOA"
    ANDORRA = "ANDORRA"
    ANGOLA = "ANGOLA"
    ANGUILLA = "ANGUILLA"
    ANTARCTICA = "ANTARCTICA"
    ANTIGUA_AND_BARBUDA = "ANTIGUA_AND_BARBUDA"
    ARCTIC_OCEAN = "ARCTIC_OCEAN"
    ARGENTINA = "ARGENTINA"
    ARMENIA = "ARMENIA"
    ARUBA = "ARUBA"
    ASHMORE_AND_CARTIER_ISLANDS = "ASHMORE_AND_CARTIER_ISLANDS"
    ATLANTIC_OCEAN = "ATLANTIC_OCEAN"
    AUSTRALIA = "AUSTRALIA"
    AUSTRIA = "AUSTRIA"
    AZERBAIJAN = "AZERBAIJAN"
    BAHAMAS = "BAHAMAS"
    BAHRAIN = "BAHRAIN"
    BALTIC_SEA = "BALTIC_SEA"
    BAKER_ISLAND = "BAKER_ISLAND"
    BANGLADESH = "BANGLADESH"
    BARBADOS = "BARBADOS"
    BASSAS_DA_INDIA = "BASSAS_DA_INDIA"
    BELARUS = "BELARUS"
    BELGIUM = "BELGIUM"
    BELIZE = "BELIZE"
    BENIN = "BENIN"
    BERMUDA = "BERMUDA"
    BHUTAN = "BHUTAN"
    BOLIVIA = "BOLIVIA"
    BORNEO = "BORNEO"
    BOSNIA_AND_HERZEGOVINA = "BOSNIA_AND_HERZEGOVINA"
    BOTSWANA = "BOTSWANA"
    BOUVET_ISLAND = "BOUVET_ISLAND"
    BRAZIL = "BRAZIL"
    BRITISH_VIRGIN_ISLANDS = "BRITISH_VIRGIN_ISLANDS"
    BRUNEI = "BRUNEI"
    BULGARIA = "BULGARIA"
    BURKINA_FASO = "BURKINA_FASO"
    BURUNDI = "BURUNDI"
    CAMBODIA = "CAMBODIA"
    CAMEROON = "CAMEROON"
    CANADA = "CANADA"
    CAPE_VERDE = "CAPE_VERDE"
    CAYMAN_ISLANDS = "CAYMAN_ISLANDS"
    CENTRAL_AFRICAN_REPUBLIC = "CENTRAL_AFRICAN_REPUBLIC"
    CHAD = "CHAD"
    CHILE = "CHILE"
    CHINA = "CHINA"
    CHRISTMAS_ISLAND = "CHRISTMAS_ISLAND"
    CLIPPERTON_ISLAND = "CLIPPERTON_ISLAND"
    COCOS_ISLANDS = "COCOS_ISLANDS"
    COLOMBIA = "COLOMBIA"
    COMOROS = "COMOROS"
    COOK_ISLANDS = "COOK_ISLANDS"
    CORAL_SEA_ISLANDS = "CORAL_SEA_ISLANDS"
    COSTA_RICA = "COSTA_RICA"
    COTE_DIVOIRE = "COTE_DIVOIRE"
    CROATIA = "CROATIA"
    CUBA = "CUBA"
    CURACAO = "CURACAO"
    CYPRUS = "CYPRUS"
    CZECHIA = "CZECHIA"
    DEMOCRATIC_REPUBLIC_OF_THE_CONGO = "DEMOCRATIC_REPUBLIC_OF_THE_CONGO"
    DENMARK = "DENMARK"
    DJIBOUTI = "DJIBOUTI"
    DOMINICA = "DOMINICA"
    DOMINICAN_REPUBLIC = "DOMINICAN_REPUBLIC"
    ECUADOR = "ECUADOR"
    EGYPT = "EGYPT"
    EL_SALVADOR = "EL_SALVADOR"
    EQUATORIAL_GUINEA = "EQUATORIAL_GUINEA"
    ERITREA = "ERITREA"
    ESTONIA = "ESTONIA"
    ESWATINI = "ESWATINI"
    ETHIOPIA = "ETHIOPIA"
    EUROPA_ISLAND = "EUROPA_ISLAND"
    FALKLAND_ISLANDS = "FALKLAND_ISLANDS"
    FAROE_ISLANDS = "FAROE_ISLANDS"
    FIJI = "FIJI"
    FINLAND = "FINLAND"
    FRANCE = "FRANCE"
    FRENCH_GUIANA = "FRENCH_GUIANA"
    FRENCH_POLYNESIA = "FRENCH_POLYNESIA"
    FRENCH_SOUTHERN_AND_ANTARCTIC_LANDS = "FRENCH_SOUTHERN_AND_ANTARCTIC_LANDS"
    GABON = "GABON"
    GAMBIA = "GAMBIA"
    GAZA_STRIP = "GAZA_STRIP"
    GEORGIA = "GEORGIA"
    GERMANY = "GERMANY"
    GHANA = "GHANA"
    GIBRALTAR = "GIBRALTAR"
    GLORIOSO_ISLANDS = "GLORIOSO_ISLANDS"
    GREECE = "GREECE"
    GREENLAND = "GREENLAND"
    GRENADA = "GRENADA"
    GUADELOUPE = "GUADELOUPE"
    GUAM = "GUAM"
    GUATEMALA = "GUATEMALA"
    GUERNSEY = "GUERNSEY"
    GUINEA = "GUINEA"
    GUINEA_BISSAU = "GUINEA_BISSAU"
    GUYANA = "GUYANA"
    HAITI = "HAITI"
    HEARD_ISLAND_AND_MCDONALD_ISLANDS = "HEARD_ISLAND_AND_MCDONALD_ISLANDS"
    HONDURAS = "HONDURAS"
    HONG_KONG = "HONG_KONG"
    HOWLAND_ISLAND = "HOWLAND_ISLAND"
    HUNGARY = "HUNGARY"
    ICELAND = "ICELAND"
    INDIA = "INDIA"
    INDIAN_OCEAN = "INDIAN_OCEAN"
    INDONESIA = "INDONESIA"
    IRAN = "IRAN"
    IRAQ = "IRAQ"
    IRELAND = "IRELAND"
    ISLE_OF_MAN = "ISLE_OF_MAN"
    ISRAEL = "ISRAEL"
    ITALY = "ITALY"
    JAMAICA = "JAMAICA"
    JAN_MAYEN = "JAN_MAYEN"
    JAPAN = "JAPAN"
    JARVIS_ISLAND = "JARVIS_ISLAND"
    JERSEY = "JERSEY"
    JOHNSTON_ATOLL = "JOHNSTON_ATOLL"
    JORDAN = "JORDAN"
    JUAN_DE_NOVA_ISLAND = "JUAN_DE_NOVA_ISLAND"
    KAZAKHSTAN = "KAZAKHSTAN"
    KENYA = "KENYA"
    KERGUELEN_ARCHIPELAGO = "KERGUELEN_ARCHIPELAGO"
    KINGMAN_REEF = "KINGMAN_REEF"
    KIRIBATI = "KIRIBATI"
    KOSOVO = "KOSOVO"
    KUWAIT = "KUWAIT"
    KYRGYZSTAN = "KYRGYZSTAN"
    LAOS = "LAOS"
    LATVIA = "LATVIA"
    LEBANON = "LEBANON"
    LESOTHO = "LESOTHO"
    LIBERIA = "LIBERIA"
    LIBYA = "LIBYA"
    LIECHTENSTEIN = "LIECHTENSTEIN"
    LINE_ISLANDS = "LINE_ISLANDS"
    LITHUANIA = "LITHUANIA"
    LUXEMBOURG = "LUXEMBOURG"
    MACAU = "MACAU"
    MADAGASCAR = "MADAGASCAR"
    MALAWI = "MALAWI"
    MALAYSIA = "MALAYSIA"
    MALDIVES = "MALDIVES"
    MALI = "MALI"
    MALTA = "MALTA"
    MARSHALL_ISLANDS = "MARSHALL_ISLANDS"
    MARTINIQUE = "MARTINIQUE"
    MAURITANIA = "MAURITANIA"
    MAURITIUS = "MAURITIUS"
    MAYOTTE = "MAYOTTE"
    MEDITERRANEAN_SEA = "MEDITERRANEAN_SEA"
    MEXICO = "MEXICO"
    MICRONESIA_FEDERATED_STATES_OF = "MICRONESIA_FEDERATED_STATES_OF"
    MIDWAY_ISLANDS = "MIDWAY_ISLANDS"
    MOLDOVA = "MOLDOVA"
    MONACO = "MONACO"
    MONGOLIA = "MONGOLIA"
    MONTENEGRO = "MONTENEGRO"
    MONTSERRAT = "MONTSERRAT"
    MOROCCO = "MOROCCO"
    MOZAMBIQUE = "MOZAMBIQUE"
    MYANMAR = "MYANMAR"
    NAMIBIA = "NAMIBIA"
    NAURU = "NAURU"
    NAVASSA_ISLAND = "NAVASSA_ISLAND"
    NEPAL = "NEPAL"
    NETHERLANDS = "NETHERLANDS"
    NEW_CALEDONIA = "NEW_CALEDONIA"
    NEW_ZEALAND = "NEW_ZEALAND"
    NICARAGUA = "NICARAGUA"
    NIGER = "NIGER"
    NIGERIA = "NIGERIA"
    NIUE = "NIUE"
    NORFOLK_ISLAND = "NORFOLK_ISLAND"
    NORTH_KOREA = "NORTH_KOREA"
    NORTH_MACEDONIA = "NORTH_MACEDONIA"
    NORTH_SEA = "NORTH_SEA"
    NORTHERN_MARIANA_ISLANDS = "NORTHERN_MARIANA_ISLANDS"
    NORWAY = "NORWAY"
    OMAN = "OMAN"
    PACIFIC_OCEAN = "PACIFIC_OCEAN"
    PAKISTAN = "PAKISTAN"
    PALAU = "PALAU"
    PALMYRA_ATOLL = "PALMYRA_ATOLL"
    PANAMA = "PANAMA"
    PAPUA_NEW_GUINEA = "PAPUA_NEW_GUINEA"
    PARACEL_ISLANDS = "PARACEL_ISLANDS"
    PARAGUAY = "PARAGUAY"
    PERU = "PERU"
    PHILIPPINES = "PHILIPPINES"
    PITCAIRN_ISLANDS = "PITCAIRN_ISLANDS"
    POLAND = "POLAND"
    PORTUGAL = "PORTUGAL"
    PUERTO_RICO = "PUERTO_RICO"
    QATAR = "QATAR"
    REPUBLIC_OF_THE_CONGO = "REPUBLIC_OF_THE_CONGO"
    REUNION = "REUNION"
    ROMANIA = "ROMANIA"
    ROSS_SEA = "ROSS_SEA"
    RUSSIA = "RUSSIA"
    RWANDA = "RWANDA"
    SAINT_BARTHELEMY = "SAINT_BARTHELEMY"
    SAINT_HELENA = "SAINT_HELENA"
    SAINT_KITTS_AND_NEVIS = "SAINT_KITTS_AND_NEVIS"
    SAINT_LUCIA = "SAINT_LUCIA"
    SAINT_MARTIN = "SAINT_MARTIN"
    SAINT_PIERRE_AND_MIQUELON = "SAINT_PIERRE_AND_MIQUELON"
    SAINT_VINCENT_AND_THE_GRENADINES = "SAINT_VINCENT_AND_THE_GRENADINES"
    SAMOA = "SAMOA"
    SAN_MARINO = "SAN_MARINO"
    SAO_TOME_AND_PRINCIPE = "SAO_TOME_AND_PRINCIPE"
    SAUDI_ARABIA = "SAUDI_ARABIA"
    SENEGAL = "SENEGAL"
    SERBIA = "SERBIA"
    SEYCHELLES = "SEYCHELLES"
    SIERRA_LEONE = "SIERRA_LEONE"
    SINGAPORE = "SINGAPORE"
    SINT_MAARTEN = "SINT_MAARTEN"
    SLOVAKIA = "SLOVAKIA"
    SLOVENIA = "SLOVENIA"
    SOLOMON_ISLANDS = "SOLOMON_ISLANDS"
    SOMALIA = "SOMALIA"
    SOUTH_AFRICA = "SOUTH_AFRICA"
    SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS = "SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS"
    SOUTH_KOREA = "SOUTH_KOREA"
    SOUTH_SUDAN = "SOUTH_SUDAN"
    SOUTHERN_OCEAN = "SOUTHERN_OCEAN"
    SPAIN = "SPAIN"
    SPRATLY_ISLANDS = "SPRATLY_ISLANDS"
    SRI_LANKA = "SRI_LANKA"
    STATE_OF_PALESTINE = "STATE_OF_PALESTINE"
    SUDAN = "SUDAN"
    SURINAME = "SURINAME"
    SVALBARD = "SVALBARD"
    SWEDEN = "SWEDEN"
    SWITZERLAND = "SWITZERLAND"
    SYRIA = "SYRIA"
    TAIWAN = "TAIWAN"
    TAJIKISTAN = "TAJIKISTAN"
    TANZANIA = "TANZANIA"
    TASMAN_SEA = "TASMAN_SEA"
    THAILAND = "THAILAND"
    TIMOR_LESTE = "TIMOR_LESTE"
    TOGO = "TOGO"
    TOKELAU = "TOKELAU"
    TONGA = "TONGA"
    TRINIDAD_AND_TOBAGO = "TRINIDAD_AND_TOBAGO"
    TROMELIN_ISLAND = "TROMELIN_ISLAND"
    TUNISIA = "TUNISIA"
    TURKEY = "TURKEY"
    TURKMENISTAN = "TURKMENISTAN"
    TURKS_AND_CAICOS_ISLANDS = "TURKS_AND_CAICOS_ISLANDS"
    TUVALU = "TUVALU"
    UGANDA = "UGANDA"
    UKRAINE = "UKRAINE"
    UNITED_ARAB_EMIRATES = "UNITED_ARAB_EMIRATES"
    UNITED_KINGDOM = "UNITED_KINGDOM"
    URUGUAY = "URUGUAY"
    USA = "USA"
    UZBEKISTAN = "UZBEKISTAN"
    VANUATU = "VANUATU"
    VENEZUELA = "VENEZUELA"
    VIET_NAM = "VIET_NAM"
    VIRGIN_ISLANDS = "VIRGIN_ISLANDS"
    WAKE_ISLAND = "WAKE_ISLAND"
    WALLIS_AND_FUTUNA = "WALLIS_AND_FUTUNA"
    WEST_BANK = "WEST_BANK"
    WESTERN_SAHARA = "WESTERN_SAHARA"
    YEMEN = "YEMEN"
    ZAMBIA = "ZAMBIA"
    ZIMBABWE = "ZIMBABWE"

# Set metadata after class creation
InsdcGeographicLocationEnum._metadata = {
    "AFGHANISTAN": {'description': 'Afghanistan', 'meaning': 'iso3166loc:af'},
    "ALBANIA": {'description': 'Albania', 'meaning': 'iso3166loc:al'},
    "ALGERIA": {'description': 'Algeria', 'meaning': 'iso3166loc:dz'},
    "AMERICAN_SAMOA": {'description': 'American Samoa', 'meaning': 'iso3166loc:as'},
    "ANDORRA": {'description': 'Andorra', 'meaning': 'iso3166loc:ad'},
    "ANGOLA": {'description': 'Angola', 'meaning': 'iso3166loc:ao'},
    "ANGUILLA": {'description': 'Anguilla', 'meaning': 'iso3166loc:ai'},
    "ANTARCTICA": {'description': 'Antarctica', 'meaning': 'iso3166loc:aq'},
    "ANTIGUA_AND_BARBUDA": {'description': 'Antigua and Barbuda', 'meaning': 'iso3166loc:ag'},
    "ARCTIC_OCEAN": {'description': 'Arctic Ocean', 'meaning': 'geonames:3371123/'},
    "ARGENTINA": {'description': 'Argentina', 'meaning': 'iso3166loc:ar'},
    "ARMENIA": {'description': 'Armenia', 'meaning': 'iso3166loc:am'},
    "ARUBA": {'description': 'Aruba', 'meaning': 'iso3166loc:aw'},
    "ASHMORE_AND_CARTIER_ISLANDS": {'description': 'Ashmore and Cartier Islands', 'annotations': {'note': 'Australian external territory'}},
    "ATLANTIC_OCEAN": {'description': 'Atlantic Ocean', 'meaning': 'geonames:3411923/'},
    "AUSTRALIA": {'description': 'Australia', 'meaning': 'iso3166loc:au'},
    "AUSTRIA": {'description': 'Austria', 'meaning': 'iso3166loc:at'},
    "AZERBAIJAN": {'description': 'Azerbaijan', 'meaning': 'iso3166loc:az'},
    "BAHAMAS": {'description': 'Bahamas', 'meaning': 'iso3166loc:bs'},
    "BAHRAIN": {'description': 'Bahrain', 'meaning': 'iso3166loc:bh'},
    "BALTIC_SEA": {'description': 'Baltic Sea', 'meaning': 'geonames:2673730/'},
    "BAKER_ISLAND": {'description': 'Baker Island', 'meaning': 'iso3166loc:um', 'annotations': {'note': 'US Minor Outlying Islands'}},
    "BANGLADESH": {'description': 'Bangladesh', 'meaning': 'iso3166loc:bd'},
    "BARBADOS": {'description': 'Barbados', 'meaning': 'iso3166loc:bb'},
    "BASSAS_DA_INDIA": {'description': 'Bassas da India', 'annotations': {'note': 'French Southern and Antarctic Lands territory'}},
    "BELARUS": {'description': 'Belarus', 'meaning': 'iso3166loc:by'},
    "BELGIUM": {'description': 'Belgium', 'meaning': 'iso3166loc:be'},
    "BELIZE": {'description': 'Belize', 'meaning': 'iso3166loc:bz'},
    "BENIN": {'description': 'Benin', 'meaning': 'iso3166loc:bj'},
    "BERMUDA": {'description': 'Bermuda', 'meaning': 'iso3166loc:bm'},
    "BHUTAN": {'description': 'Bhutan', 'meaning': 'iso3166loc:bt'},
    "BOLIVIA": {'description': 'Bolivia', 'meaning': 'iso3166loc:bo'},
    "BORNEO": {'description': 'Borneo', 'meaning': 'geonames:1642188/', 'annotations': {'note': 'Island shared by Brunei, Indonesia, and Malaysia'}},
    "BOSNIA_AND_HERZEGOVINA": {'description': 'Bosnia and Herzegovina', 'meaning': 'iso3166loc:ba'},
    "BOTSWANA": {'description': 'Botswana', 'meaning': 'iso3166loc:bw'},
    "BOUVET_ISLAND": {'description': 'Bouvet Island', 'meaning': 'iso3166loc:bv'},
    "BRAZIL": {'description': 'Brazil', 'meaning': 'iso3166loc:br'},
    "BRITISH_VIRGIN_ISLANDS": {'description': 'British Virgin Islands', 'meaning': 'iso3166loc:vg'},
    "BRUNEI": {'description': 'Brunei', 'meaning': 'iso3166loc:bn'},
    "BULGARIA": {'description': 'Bulgaria', 'meaning': 'iso3166loc:bg'},
    "BURKINA_FASO": {'description': 'Burkina Faso', 'meaning': 'iso3166loc:bf'},
    "BURUNDI": {'description': 'Burundi', 'meaning': 'iso3166loc:bi'},
    "CAMBODIA": {'description': 'Cambodia', 'meaning': 'iso3166loc:kh'},
    "CAMEROON": {'description': 'Cameroon', 'meaning': 'iso3166loc:cm'},
    "CANADA": {'description': 'Canada', 'meaning': 'iso3166loc:ca'},
    "CAPE_VERDE": {'description': 'Cape Verde', 'meaning': 'iso3166loc:cv'},
    "CAYMAN_ISLANDS": {'description': 'Cayman Islands', 'meaning': 'iso3166loc:ky'},
    "CENTRAL_AFRICAN_REPUBLIC": {'description': 'Central African Republic', 'meaning': 'iso3166loc:cf'},
    "CHAD": {'description': 'Chad', 'meaning': 'iso3166loc:td'},
    "CHILE": {'description': 'Chile', 'meaning': 'iso3166loc:cl'},
    "CHINA": {'description': 'China', 'meaning': 'iso3166loc:cn'},
    "CHRISTMAS_ISLAND": {'description': 'Christmas Island', 'meaning': 'iso3166loc:cx'},
    "CLIPPERTON_ISLAND": {'description': 'Clipperton Island', 'annotations': {'note': 'French overseas territory'}},
    "COCOS_ISLANDS": {'description': 'Cocos Islands', 'meaning': 'iso3166loc:cc'},
    "COLOMBIA": {'description': 'Colombia', 'meaning': 'iso3166loc:co'},
    "COMOROS": {'description': 'Comoros', 'meaning': 'iso3166loc:km'},
    "COOK_ISLANDS": {'description': 'Cook Islands', 'meaning': 'iso3166loc:ck'},
    "CORAL_SEA_ISLANDS": {'description': 'Coral Sea Islands', 'annotations': {'note': 'Australian external territory'}},
    "COSTA_RICA": {'description': 'Costa Rica', 'meaning': 'iso3166loc:cr'},
    "COTE_DIVOIRE": {'description': "Cote d'Ivoire", 'meaning': 'iso3166loc:ci'},
    "CROATIA": {'description': 'Croatia', 'meaning': 'iso3166loc:hr'},
    "CUBA": {'description': 'Cuba', 'meaning': 'iso3166loc:cu'},
    "CURACAO": {'description': 'Curacao', 'meaning': 'iso3166loc:cw'},
    "CYPRUS": {'description': 'Cyprus', 'meaning': 'iso3166loc:cy'},
    "CZECHIA": {'description': 'Czechia', 'meaning': 'iso3166loc:cz'},
    "DEMOCRATIC_REPUBLIC_OF_THE_CONGO": {'description': 'Democratic Republic of the Congo', 'meaning': 'iso3166loc:cd'},
    "DENMARK": {'description': 'Denmark', 'meaning': 'iso3166loc:dk'},
    "DJIBOUTI": {'description': 'Djibouti', 'meaning': 'iso3166loc:dj'},
    "DOMINICA": {'description': 'Dominica', 'meaning': 'iso3166loc:dm'},
    "DOMINICAN_REPUBLIC": {'description': 'Dominican Republic', 'meaning': 'iso3166loc:do'},
    "ECUADOR": {'description': 'Ecuador', 'meaning': 'iso3166loc:ec'},
    "EGYPT": {'description': 'Egypt', 'meaning': 'iso3166loc:eg'},
    "EL_SALVADOR": {'description': 'El Salvador', 'meaning': 'iso3166loc:sv'},
    "EQUATORIAL_GUINEA": {'description': 'Equatorial Guinea', 'meaning': 'iso3166loc:gq'},
    "ERITREA": {'description': 'Eritrea', 'meaning': 'iso3166loc:er'},
    "ESTONIA": {'description': 'Estonia', 'meaning': 'iso3166loc:ee'},
    "ESWATINI": {'description': 'Eswatini', 'meaning': 'iso3166loc:sz'},
    "ETHIOPIA": {'description': 'Ethiopia', 'meaning': 'iso3166loc:et'},
    "EUROPA_ISLAND": {'description': 'Europa Island', 'annotations': {'note': 'French Southern and Antarctic Lands territory'}},
    "FALKLAND_ISLANDS": {'description': 'Falkland Islands (Islas Malvinas)', 'meaning': 'iso3166loc:fk'},
    "FAROE_ISLANDS": {'description': 'Faroe Islands', 'meaning': 'iso3166loc:fo'},
    "FIJI": {'description': 'Fiji', 'meaning': 'iso3166loc:fj'},
    "FINLAND": {'description': 'Finland', 'meaning': 'iso3166loc:fi'},
    "FRANCE": {'description': 'France', 'meaning': 'iso3166loc:fr'},
    "FRENCH_GUIANA": {'description': 'French Guiana', 'meaning': 'iso3166loc:gf'},
    "FRENCH_POLYNESIA": {'description': 'French Polynesia', 'meaning': 'iso3166loc:pf'},
    "FRENCH_SOUTHERN_AND_ANTARCTIC_LANDS": {'description': 'French Southern and Antarctic Lands', 'meaning': 'iso3166loc:tf'},
    "GABON": {'description': 'Gabon', 'meaning': 'iso3166loc:ga'},
    "GAMBIA": {'description': 'Gambia', 'meaning': 'iso3166loc:gm'},
    "GAZA_STRIP": {'description': 'Gaza Strip', 'annotations': {'note': 'Palestinian territory'}},
    "GEORGIA": {'description': 'Georgia', 'meaning': 'iso3166loc:ge'},
    "GERMANY": {'description': 'Germany', 'meaning': 'iso3166loc:de'},
    "GHANA": {'description': 'Ghana', 'meaning': 'iso3166loc:gh'},
    "GIBRALTAR": {'description': 'Gibraltar', 'meaning': 'iso3166loc:gi'},
    "GLORIOSO_ISLANDS": {'description': 'Glorioso Islands', 'annotations': {'note': 'French Southern and Antarctic Lands territory'}},
    "GREECE": {'description': 'Greece', 'meaning': 'iso3166loc:gr'},
    "GREENLAND": {'description': 'Greenland', 'meaning': 'iso3166loc:gl'},
    "GRENADA": {'description': 'Grenada', 'meaning': 'iso3166loc:gd'},
    "GUADELOUPE": {'description': 'Guadeloupe', 'meaning': 'iso3166loc:gp'},
    "GUAM": {'description': 'Guam', 'meaning': 'iso3166loc:gu'},
    "GUATEMALA": {'description': 'Guatemala', 'meaning': 'iso3166loc:gt'},
    "GUERNSEY": {'description': 'Guernsey', 'meaning': 'iso3166loc:gg'},
    "GUINEA": {'description': 'Guinea', 'meaning': 'iso3166loc:gn'},
    "GUINEA_BISSAU": {'description': 'Guinea-Bissau', 'meaning': 'iso3166loc:gw'},
    "GUYANA": {'description': 'Guyana', 'meaning': 'iso3166loc:gy'},
    "HAITI": {'description': 'Haiti', 'meaning': 'iso3166loc:ht'},
    "HEARD_ISLAND_AND_MCDONALD_ISLANDS": {'description': 'Heard Island and McDonald Islands', 'meaning': 'iso3166loc:hm'},
    "HONDURAS": {'description': 'Honduras', 'meaning': 'iso3166loc:hn'},
    "HONG_KONG": {'description': 'Hong Kong', 'meaning': 'iso3166loc:hk'},
    "HOWLAND_ISLAND": {'description': 'Howland Island', 'meaning': 'iso3166loc:um', 'annotations': {'note': 'US Minor Outlying Islands'}},
    "HUNGARY": {'description': 'Hungary', 'meaning': 'iso3166loc:hu'},
    "ICELAND": {'description': 'Iceland', 'meaning': 'iso3166loc:is'},
    "INDIA": {'description': 'India', 'meaning': 'iso3166loc:in'},
    "INDIAN_OCEAN": {'description': 'Indian Ocean', 'meaning': 'geonames:1545739/'},
    "INDONESIA": {'description': 'Indonesia', 'meaning': 'iso3166loc:id'},
    "IRAN": {'description': 'Iran', 'meaning': 'iso3166loc:ir'},
    "IRAQ": {'description': 'Iraq', 'meaning': 'iso3166loc:iq'},
    "IRELAND": {'description': 'Ireland', 'meaning': 'iso3166loc:ie'},
    "ISLE_OF_MAN": {'description': 'Isle of Man', 'meaning': 'iso3166loc:im'},
    "ISRAEL": {'description': 'Israel', 'meaning': 'iso3166loc:il'},
    "ITALY": {'description': 'Italy', 'meaning': 'iso3166loc:it'},
    "JAMAICA": {'description': 'Jamaica', 'meaning': 'iso3166loc:jm'},
    "JAN_MAYEN": {'description': 'Jan Mayen', 'annotations': {'note': 'Norwegian territory'}},
    "JAPAN": {'description': 'Japan', 'meaning': 'iso3166loc:jp'},
    "JARVIS_ISLAND": {'description': 'Jarvis Island', 'meaning': 'iso3166loc:um', 'annotations': {'note': 'US Minor Outlying Islands'}},
    "JERSEY": {'description': 'Jersey', 'meaning': 'iso3166loc:je'},
    "JOHNSTON_ATOLL": {'description': 'Johnston Atoll', 'meaning': 'iso3166loc:um', 'annotations': {'note': 'US Minor Outlying Islands'}},
    "JORDAN": {'description': 'Jordan', 'meaning': 'iso3166loc:jo'},
    "JUAN_DE_NOVA_ISLAND": {'description': 'Juan de Nova Island', 'annotations': {'note': 'French Southern and Antarctic Lands territory'}},
    "KAZAKHSTAN": {'description': 'Kazakhstan', 'meaning': 'iso3166loc:kz'},
    "KENYA": {'description': 'Kenya', 'meaning': 'iso3166loc:ke'},
    "KERGUELEN_ARCHIPELAGO": {'description': 'Kerguelen Archipelago', 'annotations': {'note': 'French Southern and Antarctic Lands territory'}},
    "KINGMAN_REEF": {'description': 'Kingman Reef', 'meaning': 'iso3166loc:um', 'annotations': {'note': 'US Minor Outlying Islands'}},
    "KIRIBATI": {'description': 'Kiribati', 'meaning': 'iso3166loc:ki'},
    "KOSOVO": {'description': 'Kosovo', 'meaning': 'iso3166loc:xk', 'annotations': {'note': 'Provisional ISO 3166 code'}},
    "KUWAIT": {'description': 'Kuwait', 'meaning': 'iso3166loc:kw'},
    "KYRGYZSTAN": {'description': 'Kyrgyzstan', 'meaning': 'iso3166loc:kg'},
    "LAOS": {'description': 'Laos', 'meaning': 'iso3166loc:la'},
    "LATVIA": {'description': 'Latvia', 'meaning': 'iso3166loc:lv'},
    "LEBANON": {'description': 'Lebanon', 'meaning': 'iso3166loc:lb'},
    "LESOTHO": {'description': 'Lesotho', 'meaning': 'iso3166loc:ls'},
    "LIBERIA": {'description': 'Liberia', 'meaning': 'iso3166loc:lr'},
    "LIBYA": {'description': 'Libya', 'meaning': 'iso3166loc:ly'},
    "LIECHTENSTEIN": {'description': 'Liechtenstein', 'meaning': 'iso3166loc:li'},
    "LINE_ISLANDS": {'description': 'Line Islands', 'annotations': {'note': 'Island group in Pacific Ocean (part of Kiribati)'}},
    "LITHUANIA": {'description': 'Lithuania', 'meaning': 'iso3166loc:lt'},
    "LUXEMBOURG": {'description': 'Luxembourg', 'meaning': 'iso3166loc:lu'},
    "MACAU": {'description': 'Macau', 'meaning': 'iso3166loc:mo'},
    "MADAGASCAR": {'description': 'Madagascar', 'meaning': 'iso3166loc:mg'},
    "MALAWI": {'description': 'Malawi', 'meaning': 'iso3166loc:mw'},
    "MALAYSIA": {'description': 'Malaysia', 'meaning': 'iso3166loc:my'},
    "MALDIVES": {'description': 'Maldives', 'meaning': 'iso3166loc:mv'},
    "MALI": {'description': 'Mali', 'meaning': 'iso3166loc:ml'},
    "MALTA": {'description': 'Malta', 'meaning': 'iso3166loc:mt'},
    "MARSHALL_ISLANDS": {'description': 'Marshall Islands', 'meaning': 'iso3166loc:mh'},
    "MARTINIQUE": {'description': 'Martinique', 'meaning': 'iso3166loc:mq'},
    "MAURITANIA": {'description': 'Mauritania', 'meaning': 'iso3166loc:mr'},
    "MAURITIUS": {'description': 'Mauritius', 'meaning': 'iso3166loc:mu'},
    "MAYOTTE": {'description': 'Mayotte', 'meaning': 'iso3166loc:yt'},
    "MEDITERRANEAN_SEA": {'description': 'Mediterranean Sea', 'meaning': 'geonames:2593778/'},
    "MEXICO": {'description': 'Mexico', 'meaning': 'iso3166loc:mx'},
    "MICRONESIA_FEDERATED_STATES_OF": {'description': 'Micronesia, Federated States of', 'meaning': 'iso3166loc:fm'},
    "MIDWAY_ISLANDS": {'description': 'Midway Islands', 'meaning': 'iso3166loc:um', 'annotations': {'note': 'US Minor Outlying Islands'}},
    "MOLDOVA": {'description': 'Moldova', 'meaning': 'iso3166loc:md'},
    "MONACO": {'description': 'Monaco', 'meaning': 'iso3166loc:mc'},
    "MONGOLIA": {'description': 'Mongolia', 'meaning': 'iso3166loc:mn'},
    "MONTENEGRO": {'description': 'Montenegro', 'meaning': 'iso3166loc:me'},
    "MONTSERRAT": {'description': 'Montserrat', 'meaning': 'iso3166loc:ms'},
    "MOROCCO": {'description': 'Morocco', 'meaning': 'iso3166loc:ma'},
    "MOZAMBIQUE": {'description': 'Mozambique', 'meaning': 'iso3166loc:mz'},
    "MYANMAR": {'description': 'Myanmar', 'meaning': 'iso3166loc:mm'},
    "NAMIBIA": {'description': 'Namibia', 'meaning': 'iso3166loc:na'},
    "NAURU": {'description': 'Nauru', 'meaning': 'iso3166loc:nr'},
    "NAVASSA_ISLAND": {'description': 'Navassa Island', 'meaning': 'iso3166loc:um', 'annotations': {'note': 'US Minor Outlying Islands'}},
    "NEPAL": {'description': 'Nepal', 'meaning': 'iso3166loc:np'},
    "NETHERLANDS": {'description': 'Netherlands', 'meaning': 'iso3166loc:nl'},
    "NEW_CALEDONIA": {'description': 'New Caledonia', 'meaning': 'iso3166loc:nc'},
    "NEW_ZEALAND": {'description': 'New Zealand', 'meaning': 'iso3166loc:nz'},
    "NICARAGUA": {'description': 'Nicaragua', 'meaning': 'iso3166loc:ni'},
    "NIGER": {'description': 'Niger', 'meaning': 'iso3166loc:ne'},
    "NIGERIA": {'description': 'Nigeria', 'meaning': 'iso3166loc:ng'},
    "NIUE": {'description': 'Niue', 'meaning': 'iso3166loc:nu'},
    "NORFOLK_ISLAND": {'description': 'Norfolk Island', 'meaning': 'iso3166loc:nf'},
    "NORTH_KOREA": {'description': 'North Korea', 'meaning': 'iso3166loc:kp'},
    "NORTH_MACEDONIA": {'description': 'North Macedonia', 'meaning': 'iso3166loc:mk'},
    "NORTH_SEA": {'description': 'North Sea', 'meaning': 'geonames:2960848/'},
    "NORTHERN_MARIANA_ISLANDS": {'description': 'Northern Mariana Islands', 'meaning': 'iso3166loc:mp'},
    "NORWAY": {'description': 'Norway', 'meaning': 'iso3166loc:no'},
    "OMAN": {'description': 'Oman', 'meaning': 'iso3166loc:om'},
    "PACIFIC_OCEAN": {'description': 'Pacific Ocean', 'meaning': 'geonames:2363254/'},
    "PAKISTAN": {'description': 'Pakistan', 'meaning': 'iso3166loc:pk'},
    "PALAU": {'description': 'Palau', 'meaning': 'iso3166loc:pw'},
    "PALMYRA_ATOLL": {'description': 'Palmyra Atoll', 'meaning': 'iso3166loc:um', 'annotations': {'note': 'US Minor Outlying Islands'}},
    "PANAMA": {'description': 'Panama', 'meaning': 'iso3166loc:pa'},
    "PAPUA_NEW_GUINEA": {'description': 'Papua New Guinea', 'meaning': 'iso3166loc:pg'},
    "PARACEL_ISLANDS": {'description': 'Paracel Islands', 'annotations': {'note': 'Disputed territory in South China Sea'}},
    "PARAGUAY": {'description': 'Paraguay', 'meaning': 'iso3166loc:py'},
    "PERU": {'description': 'Peru', 'meaning': 'iso3166loc:pe'},
    "PHILIPPINES": {'description': 'Philippines', 'meaning': 'iso3166loc:ph'},
    "PITCAIRN_ISLANDS": {'description': 'Pitcairn Islands', 'meaning': 'iso3166loc:pn'},
    "POLAND": {'description': 'Poland', 'meaning': 'iso3166loc:pl'},
    "PORTUGAL": {'description': 'Portugal', 'meaning': 'iso3166loc:pt'},
    "PUERTO_RICO": {'description': 'Puerto Rico', 'meaning': 'iso3166loc:pr'},
    "QATAR": {'description': 'Qatar', 'meaning': 'iso3166loc:qa'},
    "REPUBLIC_OF_THE_CONGO": {'description': 'Republic of the Congo', 'meaning': 'iso3166loc:cg'},
    "REUNION": {'description': 'Reunion', 'meaning': 'iso3166loc:re'},
    "ROMANIA": {'description': 'Romania', 'meaning': 'iso3166loc:ro'},
    "ROSS_SEA": {'description': 'Ross Sea', 'meaning': 'geonames:4036621/'},
    "RUSSIA": {'description': 'Russia', 'meaning': 'iso3166loc:ru'},
    "RWANDA": {'description': 'Rwanda', 'meaning': 'iso3166loc:rw'},
    "SAINT_BARTHELEMY": {'description': 'Saint Barthelemy', 'meaning': 'iso3166loc:bl'},
    "SAINT_HELENA": {'description': 'Saint Helena', 'meaning': 'iso3166loc:sh'},
    "SAINT_KITTS_AND_NEVIS": {'description': 'Saint Kitts and Nevis', 'meaning': 'iso3166loc:kn'},
    "SAINT_LUCIA": {'description': 'Saint Lucia', 'meaning': 'iso3166loc:lc'},
    "SAINT_MARTIN": {'description': 'Saint Martin', 'meaning': 'iso3166loc:mf'},
    "SAINT_PIERRE_AND_MIQUELON": {'description': 'Saint Pierre and Miquelon', 'meaning': 'iso3166loc:pm'},
    "SAINT_VINCENT_AND_THE_GRENADINES": {'description': 'Saint Vincent and the Grenadines', 'meaning': 'iso3166loc:vc'},
    "SAMOA": {'description': 'Samoa', 'meaning': 'iso3166loc:ws'},
    "SAN_MARINO": {'description': 'San Marino', 'meaning': 'iso3166loc:sm'},
    "SAO_TOME_AND_PRINCIPE": {'description': 'Sao Tome and Principe', 'meaning': 'iso3166loc:st'},
    "SAUDI_ARABIA": {'description': 'Saudi Arabia', 'meaning': 'iso3166loc:sa'},
    "SENEGAL": {'description': 'Senegal', 'meaning': 'iso3166loc:sn'},
    "SERBIA": {'description': 'Serbia', 'meaning': 'iso3166loc:rs'},
    "SEYCHELLES": {'description': 'Seychelles', 'meaning': 'iso3166loc:sc'},
    "SIERRA_LEONE": {'description': 'Sierra Leone', 'meaning': 'iso3166loc:sl'},
    "SINGAPORE": {'description': 'Singapore', 'meaning': 'iso3166loc:sg'},
    "SINT_MAARTEN": {'description': 'Sint Maarten', 'meaning': 'iso3166loc:sx'},
    "SLOVAKIA": {'description': 'Slovakia', 'meaning': 'iso3166loc:sk'},
    "SLOVENIA": {'description': 'Slovenia', 'meaning': 'iso3166loc:si'},
    "SOLOMON_ISLANDS": {'description': 'Solomon Islands', 'meaning': 'iso3166loc:sb'},
    "SOMALIA": {'description': 'Somalia', 'meaning': 'iso3166loc:so'},
    "SOUTH_AFRICA": {'description': 'South Africa', 'meaning': 'iso3166loc:za'},
    "SOUTH_GEORGIA_AND_THE_SOUTH_SANDWICH_ISLANDS": {'description': 'South Georgia and the South Sandwich Islands', 'meaning': 'iso3166loc:gs'},
    "SOUTH_KOREA": {'description': 'South Korea', 'meaning': 'iso3166loc:kr'},
    "SOUTH_SUDAN": {'description': 'South Sudan', 'meaning': 'iso3166loc:ss'},
    "SOUTHERN_OCEAN": {'description': 'Southern Ocean', 'meaning': 'geonames:4036776/'},
    "SPAIN": {'description': 'Spain', 'meaning': 'iso3166loc:es'},
    "SPRATLY_ISLANDS": {'description': 'Spratly Islands', 'annotations': {'note': 'Disputed territory in South China Sea'}},
    "SRI_LANKA": {'description': 'Sri Lanka', 'meaning': 'iso3166loc:lk'},
    "STATE_OF_PALESTINE": {'description': 'State of Palestine', 'meaning': 'iso3166loc:ps'},
    "SUDAN": {'description': 'Sudan', 'meaning': 'iso3166loc:sd'},
    "SURINAME": {'description': 'Suriname', 'meaning': 'iso3166loc:sr'},
    "SVALBARD": {'description': 'Svalbard', 'annotations': {'note': 'Norwegian territory (part of Svalbard and Jan Mayen - SJ)'}},
    "SWEDEN": {'description': 'Sweden', 'meaning': 'iso3166loc:se'},
    "SWITZERLAND": {'description': 'Switzerland', 'meaning': 'iso3166loc:ch'},
    "SYRIA": {'description': 'Syria', 'meaning': 'iso3166loc:sy'},
    "TAIWAN": {'description': 'Taiwan', 'meaning': 'iso3166loc:tw'},
    "TAJIKISTAN": {'description': 'Tajikistan', 'meaning': 'iso3166loc:tj'},
    "TANZANIA": {'description': 'Tanzania', 'meaning': 'iso3166loc:tz'},
    "TASMAN_SEA": {'description': 'Tasman Sea', 'meaning': 'geonames:2363247/'},
    "THAILAND": {'description': 'Thailand', 'meaning': 'iso3166loc:th'},
    "TIMOR_LESTE": {'description': 'Timor-Leste', 'meaning': 'iso3166loc:tl'},
    "TOGO": {'description': 'Togo', 'meaning': 'iso3166loc:tg'},
    "TOKELAU": {'description': 'Tokelau', 'meaning': 'iso3166loc:tk'},
    "TONGA": {'description': 'Tonga', 'meaning': 'iso3166loc:to'},
    "TRINIDAD_AND_TOBAGO": {'description': 'Trinidad and Tobago', 'meaning': 'iso3166loc:tt'},
    "TROMELIN_ISLAND": {'description': 'Tromelin Island', 'annotations': {'note': 'French Southern and Antarctic Lands territory'}},
    "TUNISIA": {'description': 'Tunisia', 'meaning': 'iso3166loc:tn'},
    "TURKEY": {'description': 'Turkey', 'meaning': 'iso3166loc:tr'},
    "TURKMENISTAN": {'description': 'Turkmenistan', 'meaning': 'iso3166loc:tm'},
    "TURKS_AND_CAICOS_ISLANDS": {'description': 'Turks and Caicos Islands', 'meaning': 'iso3166loc:tc'},
    "TUVALU": {'description': 'Tuvalu', 'meaning': 'iso3166loc:tv'},
    "UGANDA": {'description': 'Uganda', 'meaning': 'iso3166loc:ug'},
    "UKRAINE": {'description': 'Ukraine', 'meaning': 'iso3166loc:ua'},
    "UNITED_ARAB_EMIRATES": {'description': 'United Arab Emirates', 'meaning': 'iso3166loc:ae'},
    "UNITED_KINGDOM": {'description': 'United Kingdom', 'meaning': 'iso3166loc:gb'},
    "URUGUAY": {'description': 'Uruguay', 'meaning': 'iso3166loc:uy'},
    "USA": {'description': 'USA', 'meaning': 'iso3166loc:us'},
    "UZBEKISTAN": {'description': 'Uzbekistan', 'meaning': 'iso3166loc:uz'},
    "VANUATU": {'description': 'Vanuatu', 'meaning': 'iso3166loc:vu'},
    "VENEZUELA": {'description': 'Venezuela', 'meaning': 'iso3166loc:ve'},
    "VIET_NAM": {'description': 'Viet Nam', 'meaning': 'iso3166loc:vn'},
    "VIRGIN_ISLANDS": {'description': 'Virgin Islands', 'meaning': 'iso3166loc:vi'},
    "WAKE_ISLAND": {'description': 'Wake Island', 'meaning': 'iso3166loc:um', 'annotations': {'note': 'US Minor Outlying Islands'}},
    "WALLIS_AND_FUTUNA": {'description': 'Wallis and Futuna', 'meaning': 'iso3166loc:wf'},
    "WEST_BANK": {'description': 'West Bank', 'annotations': {'note': 'Palestinian territory'}},
    "WESTERN_SAHARA": {'description': 'Western Sahara', 'meaning': 'iso3166loc:eh'},
    "YEMEN": {'description': 'Yemen', 'meaning': 'iso3166loc:ye'},
    "ZAMBIA": {'description': 'Zambia', 'meaning': 'iso3166loc:zm'},
    "ZIMBABWE": {'description': 'Zimbabwe', 'meaning': 'iso3166loc:zw'},
}

__all__ = [
    "InsdcGeographicLocationEnum",
]