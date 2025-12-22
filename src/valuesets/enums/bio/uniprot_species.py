"""
UniProt Species Codes Value Sets

Value sets for UniProt species mnemonic codes with associated proteome IDs

Generated from: bio/uniprot_species.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class UniProtSpeciesCode(RichEnum):
    """
    UniProt species mnemonic codes for reference proteomes with associated metadata
    """
    # Enum members
    SP_9ABAC = "SP_9ABAC"
    SP_9ACAR = "SP_9ACAR"
    SP_9ACTN = "SP_9ACTN"
    SP_9ACTO = "SP_9ACTO"
    SP_9ADEN = "SP_9ADEN"
    SP_9AGAM = "SP_9AGAM"
    SP_9AGAR = "SP_9AGAR"
    SP_9ALPC = "SP_9ALPC"
    SP_9ALPH = "SP_9ALPH"
    SP_9ALTE = "SP_9ALTE"
    SP_9ALVE = "SP_9ALVE"
    SP_9AMPH = "SP_9AMPH"
    SP_9ANNE = "SP_9ANNE"
    SP_9ANUR = "SP_9ANUR"
    SP_9APHY = "SP_9APHY"
    SP_9APIA = "SP_9APIA"
    SP_9APIC = "SP_9APIC"
    SP_9AQUI = "SP_9AQUI"
    SP_9ARAC = "SP_9ARAC"
    SP_9ARCH = "SP_9ARCH"
    SP_9ASCO = "SP_9ASCO"
    SP_9ASPA = "SP_9ASPA"
    SP_9ASTE = "SP_9ASTE"
    SP_9ASTR = "SP_9ASTR"
    SP_9AVES = "SP_9AVES"
    SP_9BACE = "SP_9BACE"
    SP_9BACI = "SP_9BACI"
    SP_9BACL = "SP_9BACL"
    SP_9BACT = "SP_9BACT"
    SP_9BACU = "SP_9BACU"
    SP_9BASI = "SP_9BASI"
    SP_9BBAC = "SP_9BBAC"
    SP_9BETA = "SP_9BETA"
    SP_9BETC = "SP_9BETC"
    SP_9BIFI = "SP_9BIFI"
    SP_9BILA = "SP_9BILA"
    SP_9BIVA = "SP_9BIVA"
    SP_9BORD = "SP_9BORD"
    SP_9BRAD = "SP_9BRAD"
    SP_9BRAS = "SP_9BRAS"
    SP_9BROM = "SP_9BROM"
    SP_9BURK = "SP_9BURK"
    SP_9CARY = "SP_9CARY"
    SP_9CAUD = "SP_9CAUD"
    SP_9CAUL = "SP_9CAUL"
    SP_9CBAC = "SP_9CBAC"
    SP_9CELL = "SP_9CELL"
    SP_9CERV = "SP_9CERV"
    SP_9CETA = "SP_9CETA"
    SP_9CHAR = "SP_9CHAR"
    SP_9CHIR = "SP_9CHIR"
    SP_9CHLA = "SP_9CHLA"
    SP_9CHLB = "SP_9CHLB"
    SP_9CHLO = "SP_9CHLO"
    SP_9CHLR = "SP_9CHLR"
    SP_9CHRO = "SP_9CHRO"
    SP_9CICH = "SP_9CICH"
    SP_9CILI = "SP_9CILI"
    SP_9CIRC = "SP_9CIRC"
    SP_9CLOS = "SP_9CLOS"
    SP_9CLOT = "SP_9CLOT"
    SP_9CNID = "SP_9CNID"
    SP_9COLU = "SP_9COLU"
    SP_9CORV = "SP_9CORV"
    SP_9CORY = "SP_9CORY"
    SP_9COXI = "SP_9COXI"
    SP_9CREN = "SP_9CREN"
    SP_9CRUS = "SP_9CRUS"
    SP_9CUCU = "SP_9CUCU"
    SP_9CYAN = "SP_9CYAN"
    SP_9DEIN = "SP_9DEIN"
    SP_9DEIO = "SP_9DEIO"
    SP_9DELA = "SP_9DELA"
    SP_9DELT = "SP_9DELT"
    SP_9DEND = "SP_9DEND"
    SP_9DINO = "SP_9DINO"
    SP_9DIPT = "SP_9DIPT"
    SP_9EIME = "SP_9EIME"
    SP_9EMBE = "SP_9EMBE"
    SP_9ENTE = "SP_9ENTE"
    SP_9ENTR = "SP_9ENTR"
    SP_9ERIC = "SP_9ERIC"
    SP_9EUCA = "SP_9EUCA"
    SP_9EUGL = "SP_9EUGL"
    SP_9EUKA = "SP_9EUKA"
    SP_9EUPU = "SP_9EUPU"
    SP_9EURO = "SP_9EURO"
    SP_9EURY = "SP_9EURY"
    SP_9FABA = "SP_9FABA"
    SP_9FIRM = "SP_9FIRM"
    SP_9FLAO = "SP_9FLAO"
    SP_9FLAV = "SP_9FLAV"
    SP_9FLOR = "SP_9FLOR"
    SP_9FRIN = "SP_9FRIN"
    SP_9FUNG = "SP_9FUNG"
    SP_9FURN = "SP_9FURN"
    SP_9FUSO = "SP_9FUSO"
    SP_9GALL = "SP_9GALL"
    SP_9GAMA = "SP_9GAMA"
    SP_9GAMC = "SP_9GAMC"
    SP_9GAMM = "SP_9GAMM"
    SP_9GAST = "SP_9GAST"
    SP_9GEMI = "SP_9GEMI"
    SP_9GLOM = "SP_9GLOM"
    SP_9GOBI = "SP_9GOBI"
    SP_9GRUI = "SP_9GRUI"
    SP_9HELI = "SP_9HELI"
    SP_9HELO = "SP_9HELO"
    SP_9HEMI = "SP_9HEMI"
    SP_9HEPA = "SP_9HEPA"
    SP_9HEXA = "SP_9HEXA"
    SP_9HYME = "SP_9HYME"
    SP_9HYPH = "SP_9HYPH"
    SP_9HYPO = "SP_9HYPO"
    SP_9INFA = "SP_9INFA"
    SP_9INSE = "SP_9INSE"
    SP_9LABR = "SP_9LABR"
    SP_ACIB2 = "SP_ACIB2"
    SP_ANOCA = "SP_ANOCA"
    SP_ANOGA = "SP_ANOGA"
    SP_AQUAE = "SP_AQUAE"
    SP_ARATH = "SP_ARATH"
    SP_ASPFU = "SP_ASPFU"
    SP_BACAN = "SP_BACAN"
    SP_BACCR = "SP_BACCR"
    SP_BACSU = "SP_BACSU"
    SP_BACTN = "SP_BACTN"
    SP_BATDJ = "SP_BATDJ"
    SP_BOVIN = "SP_BOVIN"
    SP_BRACM = "SP_BRACM"
    SP_BRADI = "SP_BRADI"
    SP_BRADU = "SP_BRADU"
    SP_BRAFL = "SP_BRAFL"
    SP_CAEBR = "SP_CAEBR"
    SP_CAEEL = "SP_CAEEL"
    SP_CAMJE = "SP_CAMJE"
    SP_CANAL = "SP_CANAL"
    SP_CANCO = "SP_CANCO"
    SP_CANDC = "SP_CANDC"
    SP_CANGB = "SP_CANGB"
    SP_CANLF = "SP_CANLF"
    SP_CANPA = "SP_CANPA"
    SP_CANTI = "SP_CANTI"
    SP_CHICK = "SP_CHICK"
    SP_CHLAA = "SP_CHLAA"
    SP_CHLRE = "SP_CHLRE"
    SP_CHLTR = "SP_CHLTR"
    SP_CIOIN = "SP_CIOIN"
    SP_CITK8 = "SP_CITK8"
    SP_CLALU = "SP_CLALU"
    SP_CLOBH = "SP_CLOBH"
    SP_COXBU = "SP_COXBU"
    SP_CRYD1 = "SP_CRYD1"
    SP_DANRE = "SP_DANRE"
    SP_DAPPU = "SP_DAPPU"
    SP_DEBHA = "SP_DEBHA"
    SP_DEIRA = "SP_DEIRA"
    SP_DICDI = "SP_DICDI"
    SP_DICPU = "SP_DICPU"
    SP_DICTD = "SP_DICTD"
    SP_DROME = "SP_DROME"
    SP_E__COLI_ECO57 = "SP_E. coli ECO57"
    SP_ECOLI = "SP_ECOLI"
    SP_EMENI = "SP_EMENI"
    SP_ENTCA = "SP_ENTCA"
    SP_ENTFA = "SP_ENTFA"
    SP_ENTGA = "SP_ENTGA"
    SP_ENTH1 = "SP_ENTH1"
    SP_EREGS = "SP_EREGS"
    SP_FELCA = "SP_FELCA"
    SP_FMDVO = "SP_FMDVO"
    SP_FUSNN = "SP_FUSNN"
    SP_GEOSL = "SP_GEOSL"
    SP_GIAIC = "SP_GIAIC"
    SP_GLOVI = "SP_GLOVI"
    SP_GORGO = "SP_GORGO"
    SP_GOSHI = "SP_GOSHI"
    SP_HAEIN = "SP_HAEIN"
    SP_HALH5 = "SP_HALH5"
    SP_HALSA = "SP_HALSA"
    SP_HBVCJ = "SP_HBVCJ"
    SP_HCMVA = "SP_HCMVA"
    SP_HCMVM = "SP_HCMVM"
    SP_HCV77 = "SP_HCV77"
    SP_HELAN = "SP_HELAN"
    SP_HELPY = "SP_HELPY"
    SP_HELRO = "SP_HELRO"
    SP_HHV11 = "SP_HHV11"
    SP_HORSE = "SP_HORSE"
    SP_HORVV = "SP_HORVV"
    SP_HPV16 = "SP_HPV16"
    SP_HUMAN = "SP_HUMAN"
    SP_HV1AN = "SP_HV1AN"
    SP_IXOSC = "SP_IXOSC"
    SP_JUGRE = "SP_JUGRE"
    SP_KLENI = "SP_KLENI"
    SP_KLEPH = "SP_KLEPH"
    SP_KLEPO = "SP_KLEPO"
    SP_KORCO = "SP_KORCO"
    SP_LACSA = "SP_LACSA"
    SP_LEIMA = "SP_LEIMA"
    SP_LEPIN = "SP_LEPIN"
    SP_LEPOC = "SP_LEPOC"
    SP_LISMO = "SP_LISMO"
    SP_LODEL = "SP_LODEL"
    SP_MACMU = "SP_MACMU"
    SP_MAIZE = "SP_MAIZE"
    SP_MANES = "SP_MANES"
    SP_MARPO = "SP_MARPO"
    SP_MEASC = "SP_MEASC"
    SP_MEDTR = "SP_MEDTR"
    SP_METAC = "SP_METAC"
    SP_METJA = "SP_METJA"
    SP_MONBE = "SP_MONBE"
    SP_MONDO = "SP_MONDO"
    SP_MOUSE = "SP_MOUSE"
    SP_MYCGE = "SP_MYCGE"
    SP_MYCMD = "SP_MYCMD"
    SP_MYCPN = "SP_MYCPN"
    SP_MYCTA = "SP_MYCTA"
    SP_MYCTU = "SP_MYCTU"
    SP_NEIMB = "SP_NEIMB"
    SP_NEIME = "SP_NEIME"
    SP_NELNU = "SP_NELNU"
    SP_NEMVE = "SP_NEMVE"
    SP_NEUCR = "SP_NEUCR"
    SP_NITMS = "SP_NITMS"
    SP_ORNAN = "SP_ORNAN"
    SP_ORYLA = "SP_ORYLA"
    SP_ORYSJ = "SP_ORYSJ"
    SP_PANTR = "SP_PANTR"
    SP_PARTE = "SP_PARTE"
    SP_PEA = "SP_PEA"
    SP_PHANO = "SP_PHANO"
    SP_PHYPA = "SP_PHYPA"
    SP_PHYRM = "SP_PHYRM"
    SP_PICGU = "SP_PICGU"
    SP_PIG = "SP_PIG"
    SP_PLAF7 = "SP_PLAF7"
    SP_POPTR = "SP_POPTR"
    SP_PRIPA = "SP_PRIPA"
    SP_PRUPE = "SP_PRUPE"
    SP_PSEAE = "SP_PSEAE"
    SP_PUCGT = "SP_PUCGT"
    SP_PYRAE = "SP_PYRAE"
    SP_RABIT = "SP_RABIT"
    SP_RAT = "SP_RAT"
    SP_RHOBA = "SP_RHOBA"
    SP_SACS2 = "SP_SACS2"
    SP_SALTY = "SP_SALTY"
    SP_SCHJY = "SP_SCHJY"
    SP_SCHPO = "SP_SCHPO"
    SP_SCLS1 = "SP_SCLS1"
    SP_SHEEP = "SP_SHEEP"
    SP_SHEON = "SP_SHEON"
    SP_SHIFL = "SP_SHIFL"
    SP_SOLLC = "SP_SOLLC"
    SP_SORBI = "SP_SORBI"
    SP_SOYBN = "SP_SOYBN"
    SP_SPIOL = "SP_SPIOL"
    SP_STAA8 = "SP_STAA8"
    SP_STAAU = "SP_STAAU"
    SP_STRCL = "SP_STRCL"
    SP_STRCO = "SP_STRCO"
    SP_STRP1 = "SP_STRP1"
    SP_STRP2 = "SP_STRP2"
    SP_STRPN = "SP_STRPN"
    SP_STRPU = "SP_STRPU"
    SP_STRR6 = "SP_STRR6"
    SP_SYNY3 = "SP_SYNY3"
    SP_THAPS = "SP_THAPS"
    SP_THECC = "SP_THECC"
    SP_THEKO = "SP_THEKO"
    SP_THEMA = "SP_THEMA"
    SP_THEYD = "SP_THEYD"
    SP_TOBAC = "SP_TOBAC"
    SP_TOXGO = "SP_TOXGO"
    SP_TRIAD = "SP_TRIAD"
    SP_TRICA = "SP_TRICA"
    SP_TRIV3 = "SP_TRIV3"
    SP_TRYB2 = "SP_TRYB2"
    SP_VACCW = "SP_VACCW"
    SP_VAR67 = "SP_VAR67"
    SP_VIBCH = "SP_VIBCH"
    SP_VITVI = "SP_VITVI"
    SP_VZVD = "SP_VZVD"
    SP_WHEAT = "SP_WHEAT"
    SP_XANCP = "SP_XANCP"
    SP_XENLA = "SP_XENLA"
    SP_XENTR = "SP_XENTR"
    SP_YARLI = "SP_YARLI"
    SP_YEAST = "SP_YEAST"
    SP_YERPE = "SP_YERPE"
    SP_ZIKV = "SP_ZIKV"

# Set metadata after class creation
UniProtSpeciesCode._metadata = {
    "SP_9ABAC": {'description': 'Lambdina fiscellaria nucleopolyhedrovirus - Proteome: UP000201190', 'meaning': 'NCBITaxon:1642929', 'annotations': {'sources': 'existing'}},
    "SP_9ACAR": {'description': 'Tropilaelaps mercedesae - Proteome: UP000192247', 'meaning': 'NCBITaxon:418985', 'annotations': {'sources': 'existing'}},
    "SP_9ACTN": {'description': 'Candidatus Protofrankia datiscae - Proteome: UP000001549', 'meaning': 'NCBITaxon:2716812', 'annotations': {'sources': 'existing'}},
    "SP_9ACTO": {'description': 'Actinomyces massiliensis F0489 - Proteome: UP000002941', 'meaning': 'NCBITaxon:1125718', 'annotations': {'sources': 'existing'}},
    "SP_9ADEN": {'description': 'Human adenovirus 53 - Proteome: UP000463865', 'meaning': 'NCBITaxon:556926', 'annotations': {'sources': 'existing'}},
    "SP_9AGAM": {'description': 'Jaapia argillacea MUCL 33604 - Proteome: UP000027265', 'meaning': 'NCBITaxon:933084', 'annotations': {'sources': 'existing'}},
    "SP_9AGAR": {'description': 'Collybiopsis luxurians FD-317 M1 - Proteome: UP000053593', 'meaning': 'NCBITaxon:944289', 'annotations': {'sources': 'existing'}},
    "SP_9ALPC": {'description': 'Feline coronavirus - Proteome: UP000141821', 'meaning': 'NCBITaxon:12663', 'annotations': {'sources': 'existing'}},
    "SP_9ALPH": {'description': 'Testudinid alphaherpesvirus 3 - Proteome: UP000100290', 'meaning': 'NCBITaxon:2560801', 'annotations': {'sources': 'existing'}},
    "SP_9ALTE": {'description': 'Paraglaciecola arctica BSs20135 - Proteome: UP000006327', 'meaning': 'NCBITaxon:493475', 'annotations': {'sources': 'existing'}},
    "SP_9ALVE": {'description': 'Perkinsus sp. BL_2016 - Proteome: UP000298064', 'meaning': 'NCBITaxon:2494336', 'annotations': {'sources': 'existing'}},
    "SP_9AMPH": {'description': 'Microcaecilia unicolor - Proteome: UP000515156', 'meaning': 'NCBITaxon:1415580', 'annotations': {'sources': 'existing'}},
    "SP_9ANNE": {'description': 'Dimorphilus gyrociliatus - Proteome: UP000549394', 'meaning': 'NCBITaxon:2664684', 'annotations': {'sources': 'existing'}},
    "SP_9ANUR": {'description': 'Leptobrachium leishanense - Proteome: UP000694569', 'meaning': 'NCBITaxon:445787', 'annotations': {'sources': 'existing'}},
    "SP_9APHY": {'description': 'Fibroporia radiculosa - Proteome: UP000006352', 'meaning': 'NCBITaxon:599839', 'annotations': {'sources': 'existing'}},
    "SP_9APIA": {'description': 'Heracleum sosnowskyi - Proteome: UP001237642', 'meaning': 'NCBITaxon:360622', 'annotations': {'sources': 'existing'}},
    "SP_9APIC": {'description': 'Babesia sp. Xinjiang - Proteome: UP000193856', 'meaning': 'NCBITaxon:462227', 'annotations': {'sources': 'existing'}},
    "SP_9AQUI": {'description': 'Sulfurihydrogenibium yellowstonense SS-5 - Proteome: UP000005540', 'meaning': 'NCBITaxon:432331', 'annotations': {'sources': 'existing'}},
    "SP_9ARAC": {'description': 'Trichonephila inaurata madagascariensis - Proteome: UP000886998', 'meaning': 'NCBITaxon:2747483', 'annotations': {'sources': 'existing'}},
    "SP_9ARCH": {'description': 'Candidatus Nitrosarchaeum limnium BG20 - Proteome: UP000014065', 'meaning': 'NCBITaxon:859192', 'annotations': {'sources': 'existing'}},
    "SP_9ASCO": {'description': 'Kuraishia capsulata CBS 1993 - Proteome: UP000019384', 'meaning': 'NCBITaxon:1382522', 'annotations': {'sources': 'existing'}},
    "SP_9ASPA": {'description': 'Dendrobium catenatum - Proteome: UP000233837', 'meaning': 'NCBITaxon:906689', 'annotations': {'sources': 'existing'}},
    "SP_9ASTE": {'description': 'Cuscuta australis - Proteome: UP000249390', 'meaning': 'NCBITaxon:267555', 'annotations': {'sources': 'existing'}},
    "SP_9ASTR": {'description': 'Mikania micrantha - Proteome: UP000326396', 'meaning': 'NCBITaxon:192012', 'annotations': {'sources': 'existing'}},
    "SP_9AVES": {'description': 'Anser brachyrhynchus - Proteome: UP000694426', 'meaning': 'NCBITaxon:132585', 'annotations': {'sources': 'existing'}},
    "SP_9BACE": {'description': 'Bacteroides caccae CL03T12C61 - Proteome: UP000002965', 'meaning': 'NCBITaxon:997873', 'annotations': {'sources': 'existing'}},
    "SP_9BACI": {'description': 'Fictibacillus macauensis ZFHKF-1 - Proteome: UP000004080', 'meaning': 'NCBITaxon:1196324', 'annotations': {'sources': 'existing'}},
    "SP_9BACL": {'description': 'Paenibacillus sp. HGF7 - Proteome: UP000003445', 'meaning': 'NCBITaxon:944559', 'annotations': {'sources': 'existing'}},
    "SP_9BACT": {'description': 'Parabacteroides johnsonii CL02T12C29 - Proteome: UP000001218', 'meaning': 'NCBITaxon:999419', 'annotations': {'sources': 'existing'}},
    "SP_9BACU": {'description': 'Samia ricini nucleopolyhedrovirus - Proteome: UP001226138', 'meaning': 'NCBITaxon:1920700', 'annotations': {'sources': 'existing'}},
    "SP_9BASI": {'description': 'Malassezia pachydermatis - Proteome: UP000037751', 'meaning': 'NCBITaxon:77020', 'annotations': {'sources': 'existing'}},
    "SP_9BBAC": {'description': 'Plutella xylostella granulovirus - Proteome: UP000201310', 'meaning': 'NCBITaxon:98383', 'annotations': {'sources': 'existing'}},
    "SP_9BETA": {'description': 'Saimiriine betaherpesvirus 4 - Proteome: UP000097892', 'meaning': 'NCBITaxon:1535247', 'annotations': {'sources': 'existing'}},
    "SP_9BETC": {'description': 'Coronavirus BtRt-BetaCoV/GX2018 - Proteome: UP001228689', 'meaning': 'NCBITaxon:2591238', 'annotations': {'sources': 'existing'}},
    "SP_9BIFI": {'description': 'Scardovia wiggsiae F0424 - Proteome: UP000006415', 'meaning': 'NCBITaxon:857290', 'annotations': {'sources': 'existing'}},
    "SP_9BILA": {'description': 'Ancylostoma ceylanicum - Proteome: UP000024635', 'meaning': 'NCBITaxon:53326', 'annotations': {'sources': 'existing'}},
    "SP_9BIVA": {'description': 'Potamilus streckersoni - Proteome: UP001195483', 'meaning': 'NCBITaxon:2493646', 'annotations': {'sources': 'existing'}},
    "SP_9BORD": {'description': 'Bordetella sp. N - Proteome: UP000064621', 'meaning': 'NCBITaxon:1746199', 'annotations': {'sources': 'existing'}},
    "SP_9BRAD": {'description': 'Afipia broomeae ATCC 49717 - Proteome: UP000001096', 'meaning': 'NCBITaxon:883078', 'annotations': {'sources': 'existing'}},
    "SP_9BRAS": {'description': 'Capsella rubella - Proteome: UP000029121', 'meaning': 'NCBITaxon:81985', 'annotations': {'sources': 'existing'}},
    "SP_9BROM": {'description': 'Prune dwarf virus - Proteome: UP000202132', 'meaning': 'NCBITaxon:33760', 'annotations': {'sources': 'existing'}},
    "SP_9BURK": {'description': 'Candidatus Paraburkholderia kirkii UZHbot1 - Proteome: UP000003511', 'meaning': 'NCBITaxon:1055526', 'annotations': {'sources': 'existing'}},
    "SP_9CARY": {'description': 'Carnegiea gigantea - Proteome: UP001153076', 'meaning': 'NCBITaxon:171969', 'annotations': {'sources': 'existing'}},
    "SP_9CAUD": {'description': 'Salmonella phage Vi06 - Proteome: UP000000335', 'meaning': 'NCBITaxon:866889', 'annotations': {'sources': 'existing'}},
    "SP_9CAUL": {'description': 'Brevundimonas abyssalis TAR-001 - Proteome: UP000016569', 'meaning': 'NCBITaxon:1391729', 'annotations': {'sources': 'existing'}},
    "SP_9CBAC": {'description': 'Neodiprion sertifer nucleopolyhedrovirus - Proteome: UP000243697', 'meaning': 'NCBITaxon:111874', 'annotations': {'sources': 'existing'}},
    "SP_9CELL": {'description': 'Actinotalea ferrariae CF5-4 - Proteome: UP000019753', 'meaning': 'NCBITaxon:948458', 'annotations': {'sources': 'existing'}},
    "SP_9CERV": {'description': 'Cervus hanglu yarkandensis - Proteome: UP000631465', 'meaning': 'NCBITaxon:84702', 'annotations': {'sources': 'existing'}},
    "SP_9CETA": {'description': 'Catagonus wagneri - Proteome: UP000694540', 'meaning': 'NCBITaxon:51154', 'annotations': {'sources': 'existing'}},
    "SP_9CHAR": {'description': 'Rostratula benghalensis - Proteome: UP000545435', 'meaning': 'NCBITaxon:118793', 'annotations': {'sources': 'existing'}},
    "SP_9CHIR": {'description': 'Phyllostomus discolor - Proteome: UP000504628', 'meaning': 'NCBITaxon:89673', 'annotations': {'sources': 'existing'}},
    "SP_9CHLA": {'description': 'Chlamydiales bacterium SCGC AG-110-P3 - Proteome: UP000196763', 'meaning': 'NCBITaxon:1871323', 'annotations': {'sources': 'existing'}},
    "SP_9CHLB": {'description': 'Chlorobium ferrooxidans DSM 13031 - Proteome: UP000004162', 'meaning': 'NCBITaxon:377431', 'annotations': {'sources': 'existing'}},
    "SP_9CHLO": {'description': 'Helicosporidium sp. ATCC 50920 - Proteome: UP000026042', 'meaning': 'NCBITaxon:1291522', 'annotations': {'sources': 'existing'}},
    "SP_9CHLR": {'description': 'Ardenticatena maritima - Proteome: UP000037784', 'meaning': 'NCBITaxon:872965', 'annotations': {'sources': 'existing'}},
    "SP_9CHRO": {'description': 'Gloeocapsa sp. PCC 7428 - Proteome: UP000010476', 'meaning': 'NCBITaxon:1173026', 'annotations': {'sources': 'existing'}},
    "SP_9CICH": {'description': 'Maylandia zebra - Proteome: UP000265160', 'meaning': 'NCBITaxon:106582', 'annotations': {'sources': 'existing'}},
    "SP_9CILI": {'description': 'Stentor coeruleus - Proteome: UP000187209', 'meaning': 'NCBITaxon:5963', 'annotations': {'sources': 'existing'}},
    "SP_9CIRC": {'description': 'Raven circovirus - Proteome: UP000097131', 'meaning': 'NCBITaxon:345250', 'annotations': {'sources': 'existing'}},
    "SP_9CLOS": {'description': 'Grapevine leafroll-associated virus 10 - Proteome: UP000203128', 'meaning': 'NCBITaxon:367121', 'annotations': {'sources': 'existing'}},
    "SP_9CLOT": {'description': 'Candidatus Arthromitus sp. SFB-rat-Yit - Proteome: UP000001273', 'meaning': 'NCBITaxon:1041504', 'annotations': {'sources': 'existing'}},
    "SP_9CNID": {'description': 'Clytia hemisphaerica - Proteome: UP000594262', 'meaning': 'NCBITaxon:252671', 'annotations': {'sources': 'existing'}},
    "SP_9COLU": {'description': 'Pampusana beccarii - Proteome: UP000541332', 'meaning': 'NCBITaxon:2953425', 'annotations': {'sources': 'existing'}},
    "SP_9CORV": {'description': 'Cnemophilus loriae - Proteome: UP000517678', 'meaning': 'NCBITaxon:254448', 'annotations': {'sources': 'existing'}},
    "SP_9CORY": {'description': 'Corynebacterium genitalium ATCC 33030 - Proteome: UP000004208', 'meaning': 'NCBITaxon:585529', 'annotations': {'sources': 'existing'}},
    "SP_9COXI": {'description': 'Coxiella endosymbiont of Amblyomma americanum - Proteome: UP000059222', 'meaning': 'NCBITaxon:325775', 'annotations': {'sources': 'existing'}},
    "SP_9CREN": {'description': 'Metallosphaera yellowstonensis MK1 - Proteome: UP000003980', 'meaning': 'NCBITaxon:671065', 'annotations': {'sources': 'existing'}},
    "SP_9CRUS": {'description': 'Daphnia magna - Proteome: UP000076858', 'meaning': 'NCBITaxon:35525', 'annotations': {'sources': 'existing'}},
    "SP_9CUCU": {'description': 'Ceutorhynchus assimilis - Proteome: UP001152799', 'meaning': 'NCBITaxon:467358', 'annotations': {'sources': 'existing'}},
    "SP_9CYAN": {'description': 'Leptolyngbyaceae cyanobacterium JSC-12 - Proteome: UP000001332', 'meaning': 'NCBITaxon:864702', 'annotations': {'sources': 'existing'}},
    "SP_9DEIN": {'description': 'Meiothermus sp. QL-1 - Proteome: UP000255346', 'meaning': 'NCBITaxon:2058095', 'annotations': {'sources': 'existing'}},
    "SP_9DEIO": {'description': 'Deinococcus sp. RL - Proteome: UP000027898', 'meaning': 'NCBITaxon:1489678', 'annotations': {'sources': 'existing'}},
    "SP_9DELA": {'description': 'Human T-cell leukemia virus type I - Proteome: UP000108043', 'meaning': 'NCBITaxon:11908', 'annotations': {'sources': 'existing'}},
    "SP_9DELT": {'description': 'Lujinxingia litoralis - Proteome: UP000249169', 'meaning': 'NCBITaxon:2211119', 'annotations': {'sources': 'existing'}},
    "SP_9DEND": {'description': 'Xiphorhynchus elegans - Proteome: UP000551443', 'meaning': 'NCBITaxon:269412', 'annotations': {'sources': 'existing'}},
    "SP_9DINO": {'description': 'Symbiodinium necroappetens - Proteome: UP000601435', 'meaning': 'NCBITaxon:1628268', 'annotations': {'sources': 'existing'}},
    "SP_9DIPT": {'description': 'Clunio marinus - Proteome: UP000183832', 'meaning': 'NCBITaxon:568069', 'annotations': {'sources': 'existing'}},
    "SP_9EIME": {'description': 'Eimeria praecox - Proteome: UP000018201', 'meaning': 'NCBITaxon:51316', 'annotations': {'sources': 'existing'}},
    "SP_9EMBE": {'description': 'Emberiza fucata - Proteome: UP000580681', 'meaning': 'NCBITaxon:337179', 'annotations': {'sources': 'existing'}},
    "SP_9ENTE": {'description': 'Enterococcus asini ATCC 700915 - Proteome: UP000013777', 'meaning': 'NCBITaxon:1158606', 'annotations': {'sources': 'existing'}},
    "SP_9ENTR": {'description': 'secondary endosymbiont of Heteropsylla cubana - Proteome: UP000003937', 'meaning': 'NCBITaxon:134287', 'annotations': {'sources': 'existing'}},
    "SP_9ERIC": {'description': 'Rhododendron williamsianum - Proteome: UP000428333', 'meaning': 'NCBITaxon:262921', 'annotations': {'sources': 'existing'}},
    "SP_9EUCA": {'description': 'Petrolisthes manimaculis - Proteome: UP001292094', 'meaning': 'NCBITaxon:1843537', 'annotations': {'sources': 'existing'}},
    "SP_9EUGL": {'description': 'Perkinsela sp. CCAP 1560/4 - Proteome: UP000036983', 'meaning': 'NCBITaxon:1314962', 'annotations': {'sources': 'existing'}},
    "SP_9EUKA": {'description': 'Chrysochromulina tobinii - Proteome: UP000037460', 'meaning': 'NCBITaxon:1460289', 'annotations': {'sources': 'existing'}},
    "SP_9EUPU": {'description': 'Candidula unifasciata - Proteome: UP000678393', 'meaning': 'NCBITaxon:100452', 'annotations': {'sources': 'existing'}},
    "SP_9EURO": {'description': 'Cladophialophora psammophila CBS 110553 - Proteome: UP000019471', 'meaning': 'NCBITaxon:1182543', 'annotations': {'sources': 'existing'}},
    "SP_9EURY": {'description': 'Methanoplanus limicola DSM 2279 - Proteome: UP000005741', 'meaning': 'NCBITaxon:937775', 'annotations': {'sources': 'existing'}},
    "SP_9FABA": {'description': 'Senna tora - Proteome: UP000634136', 'meaning': 'NCBITaxon:362788', 'annotations': {'sources': 'existing'}},
    "SP_9FIRM": {'description': 'Ruminococcaceae bacterium D16 - Proteome: UP000002801', 'meaning': 'NCBITaxon:552398', 'annotations': {'sources': 'existing'}},
    "SP_9FLAO": {'description': 'Capnocytophaga sp. oral taxon 338 str. F0234 - Proteome: UP000003023', 'meaning': 'NCBITaxon:888059', 'annotations': {'sources': 'existing'}},
    "SP_9FLAV": {'description': 'Tunisian sheep-like pestivirus - Proteome: UP001157330', 'meaning': 'NCBITaxon:3071305', 'annotations': {'sources': 'existing'}},
    "SP_9FLOR": {'description': 'Gracilariopsis chorda - Proteome: UP000247409', 'meaning': 'NCBITaxon:448386', 'annotations': {'sources': 'existing'}},
    "SP_9FRIN": {'description': 'Urocynchramus pylzowi - Proteome: UP000524542', 'meaning': 'NCBITaxon:571890', 'annotations': {'sources': 'existing'}},
    "SP_9FUNG": {'description': 'Lichtheimia corymbifera JMRC:FSU:9682 - Proteome: UP000027586', 'meaning': 'NCBITaxon:1263082', 'annotations': {'sources': 'existing'}},
    "SP_9FURN": {'description': 'Furnarius figulus - Proteome: UP000529852', 'meaning': 'NCBITaxon:463165', 'annotations': {'sources': 'existing'}},
    "SP_9FUSO": {'description': 'Fusobacterium gonidiaformans 3-1-5R - Proteome: UP000002975', 'meaning': 'NCBITaxon:469605', 'annotations': {'sources': 'existing'}},
    "SP_9GALL": {'description': 'Odontophorus gujanensis - Proteome: UP000522663', 'meaning': 'NCBITaxon:886794', 'annotations': {'sources': 'existing'}},
    "SP_9GAMA": {'description': 'Bovine gammaherpesvirus 6 - Proteome: UP000121539', 'meaning': 'NCBITaxon:1504288', 'annotations': {'sources': 'existing'}},
    "SP_9GAMC": {'description': 'Anser fabalis coronavirus NCN2 - Proteome: UP001251675', 'meaning': 'NCBITaxon:2860474', 'annotations': {'sources': 'existing'}},
    "SP_9GAMM": {'description': 'Buchnera aphidicola (Buchnera aphidicola (Cinara tujafilina)) - Proteome: UP000006811', 'meaning': 'NCBITaxon:261317', 'annotations': {'sources': 'existing'}, 'aliases': ['Buchnera aphidicola (Cinara tujafilina)']},
    "SP_9GAST": {'description': 'Elysia crispata - Proteome: UP001283361', 'meaning': 'NCBITaxon:231223', 'annotations': {'sources': 'existing'}},
    "SP_9GEMI": {'description': 'East African cassava mosaic Zanzibar virus - Proteome: UP000201107', 'meaning': 'NCBITaxon:223275', 'annotations': {'sources': 'existing'}},
    "SP_9GLOM": {'description': 'Paraglomus occultum - Proteome: UP000789572', 'meaning': 'NCBITaxon:144539', 'annotations': {'sources': 'existing'}},
    "SP_9GOBI": {'description': 'Neogobius melanostomus - Proteome: UP000694523', 'meaning': 'NCBITaxon:47308', 'annotations': {'sources': 'existing'}},
    "SP_9GRUI": {'description': 'Atlantisia rogersi - Proteome: UP000518911', 'meaning': 'NCBITaxon:2478892', 'annotations': {'sources': 'existing'}},
    "SP_9HELI": {'description': 'Helicobacter bilis ATCC 43879 - Proteome: UP000005085', 'meaning': 'NCBITaxon:613026', 'annotations': {'sources': 'existing'}},
    "SP_9HELO": {'description': 'Rhynchosporium graminicola - Proteome: UP000178129', 'meaning': 'NCBITaxon:2792576', 'annotations': {'sources': 'existing'}},
    "SP_9HEMI": {'description': 'Cinara cedri - Proteome: UP000325440', 'meaning': 'NCBITaxon:506608', 'annotations': {'sources': 'existing'}},
    "SP_9HEPA": {'description': 'Duck hepatitis B virus - Proteome: UP000137229', 'meaning': 'NCBITaxon:12639', 'annotations': {'sources': 'existing'}},
    "SP_9HEXA": {'description': 'Allacma fusca - Proteome: UP000708208', 'meaning': 'NCBITaxon:39272', 'annotations': {'sources': 'existing'}},
    "SP_9HYME": {'description': 'Melipona quadrifasciata - Proteome: UP000053105', 'meaning': 'NCBITaxon:166423', 'annotations': {'sources': 'existing'}},
    "SP_9HYPH": {'description': 'Mesorhizobium amorphae CCNWGS0123 - Proteome: UP000002949', 'meaning': 'NCBITaxon:1082933', 'annotations': {'sources': 'existing'}},
    "SP_9HYPO": {'description': '[Torrubiella] hemipterigena - Proteome: UP000039046', 'meaning': 'NCBITaxon:1531966', 'annotations': {'sources': 'existing'}},
    "SP_9INFA": {'description': 'Influenza A virus (A/California/VRDL364/2009 (Influenza A virus (A/California/VRDL364/2009(mixed))) - Proteome: UP000109975', 'meaning': 'NCBITaxon:1049605', 'annotations': {'sources': 'existing'}, 'aliases': ['Influenza A virus (A/California/VRDL364/2009(mixed))']},
    "SP_9INSE": {'description': 'Cloeon dipterum - Proteome: UP000494165', 'meaning': 'NCBITaxon:197152', 'annotations': {'sources': 'existing'}},
    "SP_9LABR": {'description': 'Labrus bergylta - Proteome: UP000261660', 'meaning': 'NCBITaxon:56723', 'annotations': {'sources': 'existing'}},
    "SP_ACIB2": {'description': 'Acinetobacter baumannii (strain ATCC 19606 / DSM 30007 / JCM 6841 / CCUG 19606 / CIP 70.34 / NBRC 109757 / NCIMB 12457 / NCTC 12156 / 81) (A. baumannii ATCC 19606) - Proteome: UP000498640', 'meaning': 'NCBITaxon:575584', 'annotations': {'sources': 'GO'}, 'aliases': ['A. baumannii ATCC 19606']},
    "SP_ANOCA": {'description': 'Anolis carolinensis (Green anole (American chameleon)) - Proteome: UP000001646', 'meaning': 'NCBITaxon:28377', 'annotations': {'sources': 'GO'}, 'aliases': ['Green anole (American chameleon)']},
    "SP_ANOGA": {'description': 'Anopheles gambiae (African malaria mosquito) - Proteome: UP000007062', 'meaning': 'NCBITaxon:7165', 'annotations': {'sources': 'GO'}, 'aliases': ['African malaria mosquito']},
    "SP_AQUAE": {'description': 'Aquifex aeolicus (aquaficae bacteria) - Proteome: UP000000798', 'meaning': 'NCBITaxon:224324', 'annotations': {'sources': 'GO'}, 'aliases': ['aquaficae bacteria']},
    "SP_ARATH": {'description': 'Arabidopsis thaliana (Mouse-ear cress) - Proteome: UP000006548', 'meaning': 'NCBITaxon:3702', 'annotations': {'sources': 'common, GO'}, 'aliases': ['Mouse-ear cress']},
    "SP_ASPFU": {'description': 'Neosartorya fumigata (ascomycote fungus) - Proteome: UP000002530', 'meaning': 'NCBITaxon:330879', 'annotations': {'sources': 'GO'}, 'aliases': ['ascomycote fungus']},
    "SP_BACAN": {'description': 'Bacillus anthracis - Proteome: UP000000594', 'meaning': 'NCBITaxon:1392', 'annotations': {'sources': 'GO'}},
    "SP_BACCR": {'description': 'Bacillus cereus (bacillus cereus) - Proteome: UP000001417', 'meaning': 'NCBITaxon:226900', 'annotations': {'sources': 'GO'}, 'aliases': ['bacillus cereus']},
    "SP_BACSU": {'description': 'Bacillus subtilis subsp. subtilis str. 168 (b subtilis) - Proteome: UP000001570', 'meaning': 'NCBITaxon:224308', 'annotations': {'sources': 'common, GO'}, 'aliases': ['b subtilis']},
    "SP_BACTN": {'description': 'Bacteroides thetaiotaomicron (bacteroidetes bacteria) - Proteome: UP000001414', 'meaning': 'NCBITaxon:226186', 'annotations': {'sources': 'GO'}, 'aliases': ['bacteroidetes bacteria']},
    "SP_BATDJ": {'description': 'Batrachochytrium dendrobatidis (Frog chytrid fungus) - Proteome: UP000007241', 'meaning': 'NCBITaxon:684364', 'annotations': {'sources': 'GO'}, 'aliases': ['Frog chytrid fungus']},
    "SP_BOVIN": {'description': 'Bos taurus (Cattle) - Proteome: UP000009136', 'meaning': 'NCBITaxon:9913', 'annotations': {'sources': 'common, GO'}, 'aliases': ['Cattle']},
    "SP_BRACM": {'description': 'Brassica campestris (Field mustard) - Proteome: UP000011750', 'meaning': 'NCBITaxon:3711', 'annotations': {'sources': 'GO'}, 'aliases': ['Field mustard']},
    "SP_BRADI": {'description': 'Brachypodium distachyon (Purple false brome) - Proteome: UP000008810', 'meaning': 'NCBITaxon:15368', 'annotations': {'sources': 'GO'}, 'aliases': ['Purple false brome']},
    "SP_BRADU": {'description': 'Bradyrhizobium diazoefficiens (alphaproteobacteria) - Proteome: UP000002526', 'meaning': 'NCBITaxon:224911', 'annotations': {'sources': 'GO'}, 'aliases': ['alphaproteobacteria']},
    "SP_BRAFL": {'description': 'Branchiostoma floridae (Florida lancelet (Amphioxus)) - Proteome: UP000001554', 'meaning': 'NCBITaxon:7739', 'annotations': {'sources': 'GO'}, 'aliases': ['Florida lancelet (Amphioxus)']},
    "SP_CAEBR": {'description': 'Caenorhabditis briggsae (nematode worm) - Proteome: UP000008549', 'meaning': 'NCBITaxon:6238', 'annotations': {'sources': 'GO'}, 'aliases': ['nematode worm']},
    "SP_CAEEL": {'description': 'Caenorhabditis elegans (nematode worm) - Proteome: UP000001940', 'meaning': 'NCBITaxon:6239', 'annotations': {'sources': 'common, GO'}, 'aliases': ['nematode worm']},
    "SP_CAMJE": {'description': 'Campylobacter jejuni subsp. jejuni serotype O:2 (strain ATCC 700819 / NCTC 11168) - Proteome: UP000000799', 'meaning': 'NCBITaxon:192222', 'annotations': {'sources': 'GO'}},
    "SP_CANAL": {'description': 'Candida albicans (Yeast) - Proteome: UP000000559', 'meaning': 'NCBITaxon:237561', 'annotations': {'sources': 'GO'}, 'aliases': ['Yeast']},
    "SP_CANCO": {'description': 'Candida orthopsilosis (strain 90-125) (Co 90-125) - Proteome: UP000005018', 'meaning': 'NCBITaxon:1136231', 'annotations': {'sources': 'GO'}},
    "SP_CANDC": {'description': 'Candida dubliniensis (strain CD36 / ATCC MYA-646 / CBS 7987 / NCPF 3949 / NRRL Y-17841) - Proteome: UP000002605', 'meaning': 'NCBITaxon:573826', 'annotations': {'sources': 'GO'}},
    "SP_CANGB": {'description': 'Candida glabrata (strain ATCC 2001 / BCRC 20586 / JCM 3761 / NBRC 0622 / NRRL Y-65 / CBS 138) (Nakaseomyces glabratus) - Proteome: UP000002428', 'meaning': 'NCBITaxon:284593', 'annotations': {'sources': 'GO'}},
    "SP_CANLF": {'description': 'Canis lupus familiaris (Dog) - Proteome: UP000805418', 'meaning': 'NCBITaxon:9615', 'annotations': {'sources': 'common, GO'}, 'aliases': ['Dog']},
    "SP_CANPA": {'description': 'Candida parapsilosis (strain CDC 317 / ATCC MYA-4646) - Proteome: UP000005221', 'meaning': 'NCBITaxon:578454', 'annotations': {'sources': 'GO'}},
    "SP_CANTI": {'description': 'Candida tropicalis (strain ATCC MYA-3404 / T1) - Proteome: UP000002037', 'meaning': 'NCBITaxon:294747', 'annotations': {'sources': 'GO'}},
    "SP_CHICK": {'description': 'Gallus gallus (Chicken) - Proteome: UP000000539', 'meaning': 'NCBITaxon:9031', 'annotations': {'sources': 'common, GO'}, 'aliases': ['Chicken']},
    "SP_CHLAA": {'description': 'Chloroflexus aurantiacus (chloroflexi bacteria) - Proteome: UP000002008', 'meaning': 'NCBITaxon:324602', 'annotations': {'sources': 'GO'}, 'aliases': ['chloroflexi bacteria']},
    "SP_CHLRE": {'description': 'Chlamydomonas reinhardtii (green algae) - Proteome: UP000006906', 'meaning': 'NCBITaxon:3055', 'annotations': {'sources': 'GO'}, 'aliases': ['green algae']},
    "SP_CHLTR": {'description': 'Chlamydia trachomatis (chlamydia) - Proteome: UP000000431', 'meaning': 'NCBITaxon:272561', 'annotations': {'sources': 'GO'}, 'aliases': ['chlamydia']},
    "SP_CIOIN": {'description': 'Ciona intestinalis (Transparent sea squirt) - Proteome: UP000008144', 'meaning': 'NCBITaxon:7719', 'annotations': {'sources': 'GO'}, 'aliases': ['Transparent sea squirt']},
    "SP_CITK8": {'description': 'Citrobacter koseri (strain ATCC BAA-895 / CDC 4225-83 / SGSC4696) - Proteome: UP000008148', 'meaning': 'NCBITaxon:290338', 'annotations': {'sources': 'GO'}},
    "SP_CLALU": {'description': 'Clavispora lusitaniae (strain ATCC 42720) - Proteome: UP000007703', 'meaning': 'NCBITaxon:306902', 'annotations': {'sources': 'GO'}},
    "SP_CLOBH": {'description': 'Clostridium botulinum (firmicutes bacteria) - Proteome: UP000001986', 'meaning': 'NCBITaxon:441771', 'annotations': {'sources': 'GO'}, 'aliases': ['firmicutes bacteria']},
    "SP_COXBU": {'description': 'Coxiella burnetii (gammaproteobacteria) - Proteome: UP000002671', 'meaning': 'NCBITaxon:227377', 'annotations': {'sources': 'GO'}, 'aliases': ['gammaproteobacteria']},
    "SP_CRYD1": {'description': 'Cryptococcus neoformans var. neoformans serotype D (Filobasidiella neoformans) (C. neoformans) - Proteome: UP000002149', 'meaning': 'NCBITaxon:214684', 'annotations': {'sources': 'GO'}, 'aliases': ['C. neoformans']},
    "SP_DANRE": {'description': 'Danio rerio (Zebrafish) - Proteome: UP000000437', 'meaning': 'NCBITaxon:7955', 'annotations': {'sources': 'common, GO'}, 'aliases': ['Zebrafish']},
    "SP_DAPPU": {'description': 'Daphnia pulex (Water flea) - Proteome: UP000000305', 'meaning': 'NCBITaxon:6669', 'annotations': {'sources': 'GO'}, 'aliases': ['Water flea']},
    "SP_DEBHA": {'description': 'Debaryomyces hansenii (strain ATCC 36239 / CBS 767 / BCRC 21394 / JCM 1990 / NBRC 0083 / IGC 2968) (Torulaspora hansenii) - Proteome: UP000000599', 'meaning': 'NCBITaxon:284592', 'annotations': {'sources': 'GO'}},
    "SP_DEIRA": {'description': 'Deinococcus radiodurans (deinococcus bacteria) - Proteome: UP000002524', 'meaning': 'NCBITaxon:243230', 'annotations': {'sources': 'GO'}, 'aliases': ['deinococcus bacteria']},
    "SP_DICDI": {'description': 'Dictyostelium discoideum (Social amoeba) - Proteome: UP000002195', 'meaning': 'NCBITaxon:44689', 'annotations': {'sources': 'GO'}, 'aliases': ['Social amoeba']},
    "SP_DICPU": {'description': 'Dictyostelium purpureum (Slime mold) - Proteome: UP000001064', 'meaning': 'NCBITaxon:5786', 'annotations': {'sources': 'GO'}, 'aliases': ['Slime mold']},
    "SP_DICTD": {'description': 'Dictyoglomus turgidum (dictyoglomi bacteria) - Proteome: UP000007719', 'meaning': 'NCBITaxon:515635', 'annotations': {'sources': 'GO'}, 'aliases': ['dictyoglomi bacteria']},
    "SP_DROME": {'description': 'Drosophila melanogaster (Fruit fly) - Proteome: UP000000803', 'meaning': 'NCBITaxon:7227', 'annotations': {'sources': 'common, GO'}, 'aliases': ['Fruit fly']},
    "SP_E__COLI_ECO57": {'description': 'Escherichia coli O157:H7 - Proteome: UP000000558', 'meaning': 'NCBITaxon:83334', 'annotations': {'sources': 'GO'}},
    "SP_ECOLI": {'description': 'Escherichia coli K-12 (E. coli) - Proteome: UP000000625', 'meaning': 'NCBITaxon:83333', 'annotations': {'sources': 'common, GO'}, 'aliases': ['E. coli']},
    "SP_EMENI": {'description': 'Emericella nidulans (ascomycote fungus) - Proteome: UP000000560', 'meaning': 'NCBITaxon:227321', 'annotations': {'sources': 'GO'}, 'aliases': ['ascomycote fungus']},
    "SP_ENTCA": {'description': 'Enterococcus casseliflavus EC20 - Proteome: UP000012675', 'meaning': 'NCBITaxon:565655', 'annotations': {'sources': 'GO'}},
    "SP_ENTFA": {'description': 'Enterococcus faecalis (strain ATCC 700802 / V583) - Proteome: UP000001415', 'meaning': 'NCBITaxon:226185', 'annotations': {'sources': 'GO'}},
    "SP_ENTGA": {'description': 'Enterococcus gallinarum - Proteome: UP000254807', 'meaning': 'NCBITaxon:1353', 'annotations': {'sources': 'GO'}},
    "SP_ENTH1": {'description': 'Entamoeba histolytica (amoeba) - Proteome: UP000001926', 'meaning': 'NCBITaxon:294381', 'annotations': {'sources': 'GO'}, 'aliases': ['amoeba']},
    "SP_EREGS": {'description': 'Eremothecium gossypii (Yeast) - Proteome: UP000000591', 'meaning': 'NCBITaxon:284811', 'annotations': {'sources': 'GO'}, 'aliases': ['Yeast']},
    "SP_FELCA": {'description': 'Felis catus (Cat) - Proteome: UP000011712', 'meaning': 'NCBITaxon:9685', 'annotations': {'sources': 'common, GO'}, 'aliases': ['Cat']},
    "SP_FMDVO": {'description': 'Foot-and-mouth disease virus serotype O (FMDV) (FMDV) - Proteome: UP000008765', 'meaning': 'NCBITaxon:12118', 'annotations': {'sources': 'GO'}, 'aliases': ['FMDV']},
    "SP_FUSNN": {'description': 'Fusobacterium nucleatum (strain ATCC 25586) (F. nucleatum ATCC 25586) - Proteome: UP000241660', 'meaning': 'NCBITaxon:190304', 'annotations': {'sources': 'GO'}, 'aliases': ['F. nucleatum ATCC 25586']},
    "SP_GEOSL": {'description': 'Geobacter sulfurreducens (deltaproteobacteria) - Proteome: UP000000577', 'meaning': 'NCBITaxon:243231', 'annotations': {'sources': 'GO'}, 'aliases': ['deltaproteobacteria']},
    "SP_GIAIC": {'description': 'Giardia intestinalis (giardia) - Proteome: UP000001548', 'meaning': 'NCBITaxon:184922', 'annotations': {'sources': 'GO'}, 'aliases': ['giardia']},
    "SP_GLOVI": {'description': 'Gloeobacter violaceus (cyanobacteria) - Proteome: UP000000557', 'meaning': 'NCBITaxon:251221', 'annotations': {'sources': 'GO'}, 'aliases': ['cyanobacteria']},
    "SP_GORGO": {'description': 'Gorilla gorilla gorilla (Western lowland gorilla) - Proteome: UP000001519', 'meaning': 'NCBITaxon:9593', 'annotations': {'sources': 'common, GO'}, 'aliases': ['Western lowland gorilla']},
    "SP_GOSHI": {'description': 'Gossypium hirsutum (Upland cotton) - Proteome: UP000189702', 'meaning': 'NCBITaxon:3635', 'annotations': {'sources': 'GO'}, 'aliases': ['Upland cotton']},
    "SP_HAEIN": {'description': 'Haemophilus influenzae (strain ATCC 51907 / DSM 11121 / KW20 / Rd) (H. influenzae strain ATCC 51907) - Proteome: UP000000579', 'meaning': 'NCBITaxon:71421', 'annotations': {'sources': 'GO'}, 'aliases': ['H. influenzae strain ATCC 51907']},
    "SP_HALH5": {'description': 'Halalkalibacterium halodurans (strain ATCC BAA-125 / DSM 18197 / FERM 7344 / JCM 9153 / C-125) (Bacillus halodurans) - Proteome: UP000001258', 'meaning': 'NCBITaxon:272558', 'annotations': {'sources': 'GO'}},
    "SP_HALSA": {'description': 'Halobacterium salinarum (euryarchaea) - Proteome: UP000000554', 'meaning': 'NCBITaxon:64091', 'annotations': {'sources': 'GO'}, 'aliases': ['euryarchaea']},
    "SP_HBVCJ": {'description': 'Hepatitis B virus genotype C subtype ayr (isolate Human/Japan/Okamoto/-) (HBV-C) - Proteome: UP000008591', 'meaning': 'NCBITaxon:928302', 'annotations': {'sources': 'GO'}, 'aliases': ['HBV-C']},
    "SP_HCMVA": {'description': 'Human cytomegalovirus (strain AD169) (Human herpesvirus 5 (HHV-5)) - Proteome: UP000008992', 'meaning': 'NCBITaxon:10360', 'annotations': {'sources': 'GO'}, 'aliases': ['Human herpesvirus 5 (HHV-5)']},
    "SP_HCMVM": {'description': 'Human cytomegalovirus (Human herpesvirus 5) strain Merlin (HHV-5 Merlin) - Proteome: UP000000938', 'meaning': 'NCBITaxon:295027', 'annotations': {'sources': 'GO'}, 'aliases': ['HHV-5 Merlin']},
    "SP_HCV77": {'description': 'Hepatitis C virus genotype 1a (isolate H77) (HCV) - Proteome: UP000000518', 'meaning': 'NCBITaxon:63746', 'annotations': {'sources': 'GO'}, 'aliases': ['HCV']},
    "SP_HELAN": {'description': 'Helianthus annuus (Common sunflower) - Proteome: UP000215914', 'meaning': 'NCBITaxon:4232', 'annotations': {'sources': 'GO'}, 'aliases': ['Common sunflower']},
    "SP_HELPY": {'description': 'Helicobacter pylori (Campylobacter pylori) strain ATCC 700392 / 26695 (H. pylori) - Proteome: UP000000429', 'meaning': 'NCBITaxon:85962', 'annotations': {'sources': 'GO'}, 'aliases': ['H. pylori']},
    "SP_HELRO": {'description': 'Helobdella robusta (Californian leech) - Proteome: UP000015101', 'meaning': 'NCBITaxon:6412', 'annotations': {'sources': 'GO'}, 'aliases': ['Californian leech']},
    "SP_HHV11": {'description': 'Human herpesvirus 1 (strain 17) (Human herpes simplex virus 1 (HHV-1)) - Proteome: UP000009294', 'meaning': 'NCBITaxon:10299', 'annotations': {'sources': 'GO'}, 'aliases': ['Human herpes simplex virus 1 (HHV-1)']},
    "SP_HORSE": {'description': 'Equus caballus (Horse) - Proteome: UP000002281', 'meaning': 'NCBITaxon:9796', 'annotations': {'sources': 'common, GO'}, 'aliases': ['Horse']},
    "SP_HORVV": {'description': 'Hordeum vulgare subsp. vulgare (Domesticated barley) - Proteome: UP000011116', 'meaning': 'NCBITaxon:112509', 'annotations': {'sources': 'GO'}, 'aliases': ['Domesticated barley']},
    "SP_HPV16": {'description': 'Human papillomavirus type 16 - Proteome: UP000009251', 'meaning': 'NCBITaxon:333760', 'annotations': {'sources': 'GO'}},
    "SP_HUMAN": {'description': 'Homo sapiens (Human) - Proteome: UP000005640', 'meaning': 'NCBITaxon:9606', 'annotations': {'sources': 'common, GO'}, 'aliases': ['Human']},
    "SP_HV1AN": {'description': 'Human immunodeficiency virus type 1 group O (isolate ANT70) - Proteome: UP000007689', 'meaning': 'NCBITaxon:327105', 'annotations': {'sources': 'GO'}},
    "SP_IXOSC": {'description': 'Ixodes scapularis (Deer tick) - Proteome: UP000001555', 'meaning': 'NCBITaxon:6945', 'annotations': {'sources': 'GO'}, 'aliases': ['Deer tick']},
    "SP_JUGRE": {'description': 'Juglans regia (English walnut) - Proteome: UP000235220', 'meaning': 'NCBITaxon:51240', 'annotations': {'sources': 'GO'}, 'aliases': ['English walnut']},
    "SP_KLENI": {'description': 'Klebsormidium nitens (Green alga) - Proteome: UP000054558', 'meaning': 'NCBITaxon:105231', 'annotations': {'sources': 'GO'}, 'aliases': ['Green alga']},
    "SP_KLEPH": {'description': 'Klebsiella pneumoniae subsp. pneumoniae (strain HS11286) - Proteome: UP000007841', 'meaning': 'NCBITaxon:1125630', 'annotations': {'sources': 'GO'}},
    "SP_KLEPO": {'description': 'Klebsiella pneumoniae subsp. ozaenae (subspecies) - Proteome: UP000255382', 'meaning': 'NCBITaxon:574', 'annotations': {'sources': 'GO'}},
    "SP_KORCO": {'description': 'Korarchaeum cryptofilum (candidatus archaea) - Proteome: UP000001686', 'meaning': 'NCBITaxon:374847', 'annotations': {'sources': 'GO'}, 'aliases': ['candidatus archaea']},
    "SP_LACSA": {'description': 'Lactuca sativa (Garden lettuce) - Proteome: UP000235145', 'meaning': 'NCBITaxon:4236', 'annotations': {'sources': 'GO'}, 'aliases': ['Garden lettuce']},
    "SP_LEIMA": {'description': 'Leishmania major strain Friedlin (leishmania) - Proteome: UP000000542', 'meaning': 'NCBITaxon:347515', 'annotations': {'sources': 'GO'}, 'aliases': ['leishmania']},
    "SP_LEPIN": {'description': 'Leptospira interrogans (spirochaetes bacteria) - Proteome: UP000001408', 'meaning': 'NCBITaxon:189518', 'annotations': {'sources': 'GO'}, 'aliases': ['spirochaetes bacteria']},
    "SP_LEPOC": {'description': 'Lepisosteus oculatus (Spotted gar) - Proteome: UP000018468', 'meaning': 'NCBITaxon:7918', 'annotations': {'sources': 'GO'}, 'aliases': ['Spotted gar']},
    "SP_LISMO": {'description': 'Listeria monocytogenes serovar 1/2a (strain ATCC BAA-679 / EGD-e) - Proteome: UP000000817', 'meaning': 'NCBITaxon:169963', 'annotations': {'sources': 'GO'}},
    "SP_LODEL": {'description': 'Lodderomyces elongisporus (strain ATCC 11503 / CBS 2605 / JCM 1781 / NBRC 1676 / NRRL YB-4239) (Saccharomyces elongisporus) - Proteome: UP000001996', 'meaning': 'NCBITaxon:379508', 'annotations': {'sources': 'GO'}},
    "SP_MACMU": {'description': 'Macaca mulatta (Rhesus macaque) - Proteome: UP000006718', 'meaning': 'NCBITaxon:9544', 'annotations': {'sources': 'common, GO'}, 'aliases': ['Rhesus macaque']},
    "SP_MAIZE": {'description': 'Zea mays (Maize) - Proteome: UP000007305', 'meaning': 'NCBITaxon:4577', 'annotations': {'sources': 'common, GO'}, 'aliases': ['Maize']},
    "SP_MANES": {'description': 'Manihot esculenta (Cassava) - Proteome: UP000091857', 'meaning': 'NCBITaxon:3983', 'annotations': {'sources': 'GO'}, 'aliases': ['Cassava']},
    "SP_MARPO": {'description': 'Marchantia polymorpha (Common liverwort) - Proteome: UP000244005', 'meaning': 'NCBITaxon:3197', 'annotations': {'sources': 'GO'}, 'aliases': ['Common liverwort']},
    "SP_MEASC": {'description': 'Measles virus (Subacute sclerose panencephalitis virus) strain Ichinose-B95a (MeV strain Ichinose-B95a) - Proteome: UP000008699', 'meaning': 'NCBITaxon:645098', 'annotations': {'sources': 'GO'}, 'aliases': ['MeV strain Ichinose-B95a']},
    "SP_MEDTR": {'description': 'Medicago truncatula (Barrel medic) - Proteome: UP000002051', 'meaning': 'NCBITaxon:3880', 'annotations': {'sources': 'GO'}, 'aliases': ['Barrel medic']},
    "SP_METAC": {'description': 'Methanosarcina acetivorans (euryarchaea) - Proteome: UP000002487', 'meaning': 'NCBITaxon:188937', 'annotations': {'sources': 'GO'}, 'aliases': ['euryarchaea']},
    "SP_METJA": {'description': 'Methanocaldococcus jannaschii (methanococci archaea) - Proteome: UP000000805', 'meaning': 'NCBITaxon:243232', 'annotations': {'sources': 'GO'}, 'aliases': ['methanococci archaea']},
    "SP_MONBE": {'description': 'Monosiga brevicollis (sponge) - Proteome: UP000001357', 'meaning': 'NCBITaxon:81824', 'annotations': {'sources': 'GO'}, 'aliases': ['sponge']},
    "SP_MONDO": {'description': 'Monodelphis domestica (Gray short-tailed opossum) - Proteome: UP000002280', 'meaning': 'NCBITaxon:13616', 'annotations': {'sources': 'GO'}, 'aliases': ['Gray short-tailed opossum']},
    "SP_MOUSE": {'description': 'Mus musculus (Mouse) - Proteome: UP000000589', 'meaning': 'NCBITaxon:10090', 'annotations': {'sources': 'common, GO'}, 'aliases': ['Mouse']},
    "SP_MYCGE": {'description': 'Mycoplasma genitalium (mollicutes bacteria) - Proteome: UP000000807', 'meaning': 'NCBITaxon:243273', 'annotations': {'sources': 'GO'}, 'aliases': ['mollicutes bacteria']},
    "SP_MYCMD": {'description': 'Mycosarcoma maydis (Ustilago maydis) (Corn smut fungus) - Proteome: UP000000561', 'meaning': 'NCBITaxon:5270', 'annotations': {'sources': 'GO'}, 'aliases': ['Corn smut fungus']},
    "SP_MYCPN": {'description': 'Mycoplasma pneumoniae strain ATCC 29342 / M129 / Subtype 1 - Proteome: UP000000808', 'meaning': 'NCBITaxon:272634', 'annotations': {'sources': 'GO'}},
    "SP_MYCTA": {'description': 'Mycobacterium tuberculosis (strain ATCC 25177 / H37Ra) - Proteome: UP000001988', 'meaning': 'NCBITaxon:419947', 'annotations': {'sources': 'GO'}},
    "SP_MYCTU": {'description': 'Mycobacterium tuberculosis H37Rv (actinobacteria) - Proteome: UP000001584', 'meaning': 'NCBITaxon:83332', 'annotations': {'sources': 'GO'}, 'aliases': ['actinobacteria']},
    "SP_NEIMB": {'description': 'Neisseria meningitidis serogroup B (strain ATCC BAA-335 / MC58) (betaproteobacteria) - Proteome: UP000000425', 'meaning': 'NCBITaxon:122586', 'annotations': {'sources': 'GO'}, 'aliases': ['betaproteobacteria']},
    "SP_NEIME": {'description': 'Neisseria meningitidis MC58 - Proteome: UP000000425', 'meaning': 'NCBITaxon:122586', 'annotations': {'sources': 'existing'}},
    "SP_NELNU": {'description': 'Nelumbo nucifera (Sacred lotus) - Proteome: UP000189703', 'meaning': 'NCBITaxon:4432', 'annotations': {'sources': 'GO'}, 'aliases': ['Sacred lotus']},
    "SP_NEMVE": {'description': 'Nematostella vectensis (Starlet sea anemone) - Proteome: UP000001593', 'meaning': 'NCBITaxon:45351', 'annotations': {'sources': 'GO'}, 'aliases': ['Starlet sea anemone']},
    "SP_NEUCR": {'description': 'Neurospora crassa (ascomycote fungus) - Proteome: UP000001805', 'meaning': 'NCBITaxon:367110', 'annotations': {'sources': 'GO'}, 'aliases': ['ascomycote fungus']},
    "SP_NITMS": {'description': 'Nitrosopumilus maritimus (thaumarchaea) - Proteome: UP000000792', 'meaning': 'NCBITaxon:436308', 'annotations': {'sources': 'GO'}, 'aliases': ['thaumarchaea']},
    "SP_ORNAN": {'description': 'Ornithorhynchus anatinus (Duckbill platypus) - Proteome: UP000002279', 'meaning': 'NCBITaxon:9258', 'annotations': {'sources': 'GO'}, 'aliases': ['Duckbill platypus']},
    "SP_ORYLA": {'description': 'Oryzias latipes (Japanese rice fish) - Proteome: UP000001038', 'meaning': 'NCBITaxon:8090', 'annotations': {'sources': 'GO'}, 'aliases': ['Japanese rice fish']},
    "SP_ORYSJ": {'description': 'Oryza sativa subsp. japonica (Rice) - Proteome: UP000059680', 'meaning': 'NCBITaxon:39947', 'annotations': {'sources': 'common, GO'}, 'aliases': ['Rice']},
    "SP_PANTR": {'description': 'Pan troglodytes (Chimpanzee) - Proteome: UP000002277', 'meaning': 'NCBITaxon:9598', 'annotations': {'sources': 'common, GO'}, 'aliases': ['Chimpanzee']},
    "SP_PARTE": {'description': 'Paramecium tetraurelia (alveolate) - Proteome: UP000000600', 'meaning': 'NCBITaxon:5888', 'annotations': {'sources': 'GO'}, 'aliases': ['alveolate']},
    "SP_PEA": {'description': 'Pisum sativum (Garden pea) - Proteome: UP001058974', 'meaning': 'NCBITaxon:3888', 'annotations': {'sources': 'common'}, 'aliases': ['Garden pea']},
    "SP_PHANO": {'description': 'Phaeosphaeria nodorum (Glume blotch fungus) - Proteome: UP000663193', 'meaning': 'NCBITaxon:321614', 'annotations': {'sources': 'GO'}, 'aliases': ['Glume blotch fungus']},
    "SP_PHYPA": {'description': 'Physcomitrella patens (Spreading-leaved earth moss) - Proteome: UP000006727', 'meaning': 'NCBITaxon:3218', 'annotations': {'sources': 'GO'}, 'aliases': ['Spreading-leaved earth moss']},
    "SP_PHYRM": {'description': 'Phytophthora ramorum (Sudden oak death agent) - Proteome: UP000005238', 'meaning': 'NCBITaxon:164328', 'annotations': {'sources': 'GO'}, 'aliases': ['Sudden oak death agent']},
    "SP_PICGU": {'description': 'Meyerozyma guilliermondii (strain ATCC 6260 / CBS 566 / DSM 6381 / JCM 1539 / NBRC 10279 / NRRL Y-324) (Candida guilliermondii) - Proteome: UP000001997', 'meaning': 'NCBITaxon:294746', 'annotations': {'sources': 'GO'}},
    "SP_PIG": {'description': 'Sus scrofa (Pig) - Proteome: UP000008227', 'meaning': 'NCBITaxon:9823', 'annotations': {'sources': 'common, GO'}, 'aliases': ['Pig']},
    "SP_PLAF7": {'description': 'Plasmodium falciparum 3D7 (Malaria parasite) - Proteome: UP000001450', 'meaning': 'NCBITaxon:36329', 'annotations': {'sources': 'GO'}, 'aliases': ['Malaria parasite']},
    "SP_POPTR": {'description': 'Populus trichocarpa (Western balsam poplar) - Proteome: UP000006729', 'meaning': 'NCBITaxon:3694', 'annotations': {'sources': 'GO'}, 'aliases': ['Western balsam poplar']},
    "SP_PRIPA": {'description': 'Pristionchus pacificus (Parasitic nematode) - Proteome: UP000005239', 'meaning': 'NCBITaxon:54126', 'annotations': {'sources': 'GO'}, 'aliases': ['Parasitic nematode']},
    "SP_PRUPE": {'description': 'Prunus persica (Peach) - Proteome: UP000006882', 'meaning': 'NCBITaxon:3760', 'annotations': {'sources': 'GO'}, 'aliases': ['Peach']},
    "SP_PSEAE": {'description': 'Pseudomonas aeruginosa PAO1 (gammaproteobacteria) - Proteome: UP000002438', 'meaning': 'NCBITaxon:208964', 'annotations': {'sources': 'GO'}, 'aliases': ['gammaproteobacteria']},
    "SP_PUCGT": {'description': 'Puccinia graminis (Black stem rust fungus) - Proteome: UP000008783', 'meaning': 'NCBITaxon:418459', 'annotations': {'sources': 'GO'}, 'aliases': ['Black stem rust fungus']},
    "SP_PYRAE": {'description': 'Pyrobaculum aerophilum (crenarchaea) - Proteome: UP000002439', 'meaning': 'NCBITaxon:178306', 'annotations': {'sources': 'GO'}, 'aliases': ['crenarchaea']},
    "SP_RABIT": {'description': 'Oryctolagus cuniculus (Rabbit) - Proteome: UP000001811', 'meaning': 'NCBITaxon:9986', 'annotations': {'sources': 'common'}, 'aliases': ['Rabbit']},
    "SP_RAT": {'description': 'Rattus norvegicus (Rat) - Proteome: UP000002494', 'meaning': 'NCBITaxon:10116', 'annotations': {'sources': 'common, GO'}, 'aliases': ['Rat']},
    "SP_RHOBA": {'description': 'Rhodopirellula baltica (planctomycetes bacteria) - Proteome: UP000001025', 'meaning': 'NCBITaxon:243090', 'annotations': {'sources': 'GO'}, 'aliases': ['planctomycetes bacteria']},
    "SP_SACS2": {'description': 'Sulfolobus solfataricus (crenarchaea) - Proteome: UP000001974', 'meaning': 'NCBITaxon:273057', 'annotations': {'sources': 'GO'}, 'aliases': ['crenarchaea']},
    "SP_SALTY": {'description': 'Salmonella typhimurium (strain LT2 / SGSC1412 / ATCC 700720) (S. typhimurium LT2) - Proteome: UP000001014', 'meaning': 'NCBITaxon:99287', 'annotations': {'sources': 'GO'}, 'aliases': ['S. typhimurium LT2']},
    "SP_SCHJY": {'description': 'Schizosaccharomyces japonicus (Fission yeast) - Proteome: UP000001744', 'meaning': 'NCBITaxon:402676', 'annotations': {'sources': 'GO'}, 'aliases': ['Fission yeast']},
    "SP_SCHPO": {'description': 'Schizosaccharomyces pombe 972h- (Fission yeast) - Proteome: UP000002485', 'meaning': 'NCBITaxon:284812', 'annotations': {'sources': 'common, GO'}, 'aliases': ['Fission yeast']},
    "SP_SCLS1": {'description': 'Sclerotinia sclerotiorum (White mold) - Proteome: UP000001312', 'meaning': 'NCBITaxon:665079', 'annotations': {'sources': 'GO'}, 'aliases': ['White mold']},
    "SP_SHEEP": {'description': 'Ovis aries (Sheep) - Proteome: UP000002356', 'meaning': 'NCBITaxon:9940', 'annotations': {'sources': 'common'}, 'aliases': ['Sheep']},
    "SP_SHEON": {'description': 'Shewanella oneidensis (shewanella) - Proteome: UP000008186', 'meaning': 'NCBITaxon:211586', 'annotations': {'sources': 'GO'}, 'aliases': ['shewanella']},
    "SP_SHIFL": {'description': 'Shigella flexneri - Proteome: UP000001006', 'meaning': 'NCBITaxon:623', 'annotations': {'sources': 'GO'}},
    "SP_SOLLC": {'description': 'Solanum lycopersicum (Tomato) - Proteome: UP000004994', 'meaning': 'NCBITaxon:4081', 'annotations': {'sources': 'GO'}, 'aliases': ['Tomato']},
    "SP_SORBI": {'description': 'Sorghum bicolor (Sorghum) - Proteome: UP000000768', 'meaning': 'NCBITaxon:4558', 'annotations': {'sources': 'GO'}, 'aliases': ['Sorghum']},
    "SP_SOYBN": {'description': 'Glycine max (Soybean) - Proteome: UP000008827', 'meaning': 'NCBITaxon:3847', 'annotations': {'sources': 'GO'}, 'aliases': ['Soybean']},
    "SP_SPIOL": {'description': 'Spinacia oleracea (Spinach) - Proteome: UP001155700', 'meaning': 'NCBITaxon:3562', 'annotations': {'sources': 'GO'}, 'aliases': ['Spinach']},
    "SP_STAA8": {'description': 'Staphylococcus aureus (strain NCTC 8325 / PS 47) (S. aureus NCTC 8325) - Proteome: UP000008816', 'meaning': 'NCBITaxon:93061', 'annotations': {'sources': 'GO'}, 'aliases': ['S. aureus NCTC 8325']},
    "SP_STAAU": {'description': 'Staphylococcus aureus subsp. aureus NCTC 8325 - Proteome: UP000008816', 'meaning': 'NCBITaxon:93061', 'annotations': {'sources': 'existing'}},
    "SP_STRCL": {'description': 'Streptomyces clavuligerus - Proteome: UP000002357', 'meaning': 'NCBITaxon:1901', 'annotations': {'sources': 'GO'}},
    "SP_STRCO": {'description': 'Streptomyces coelicolor (actinobacteria) - Proteome: UP000001973', 'meaning': 'NCBITaxon:100226', 'annotations': {'sources': 'GO'}, 'aliases': ['actinobacteria']},
    "SP_STRP1": {'description': 'Streptococcus pyogenes serotype M1 (Strain: ATCC 700294 / SF370 / Serotype M1) - Proteome: UP000000750', 'meaning': 'NCBITaxon:301447', 'annotations': {'sources': 'GO'}},
    "SP_STRP2": {'description': 'Streptococcus pneumoniae serotype 2 (strain D39 / NCTC 7466) - Proteome: UP000001452', 'meaning': 'NCBITaxon:373153', 'annotations': {'sources': 'GO'}},
    "SP_STRPN": {'description': 'Streptococcus pneumoniae serotype 4 (strain ATCC BAA-334 / TIGR4) - Proteome: UP000000586', 'meaning': 'NCBITaxon:171101', 'annotations': {'sources': 'GO'}},
    "SP_STRPU": {'description': 'Strongylocentrotus purpuratus (Purple sea urchin) - Proteome: UP000007110', 'meaning': 'NCBITaxon:7668', 'annotations': {'sources': 'GO'}, 'aliases': ['Purple sea urchin']},
    "SP_STRR6": {'description': 'Streptococcus pneumoniae (strep) - Proteome: UP000000586', 'meaning': 'NCBITaxon:171101', 'annotations': {'sources': 'GO'}, 'aliases': ['strep']},
    "SP_SYNY3": {'description': 'Synechocystis sp. (cyanobacteria) - Proteome: UP000001425', 'meaning': 'NCBITaxon:1111708', 'annotations': {'sources': 'GO'}, 'aliases': ['cyanobacteria']},
    "SP_THAPS": {'description': 'Thalassiosira pseudonana (Marine diatom) - Proteome: UP000001449', 'meaning': 'NCBITaxon:35128', 'annotations': {'sources': 'GO'}, 'aliases': ['Marine diatom']},
    "SP_THECC": {'description': 'Theobroma cacao (Cacao) - Proteome: UP000026915', 'meaning': 'NCBITaxon:3641', 'annotations': {'sources': 'GO'}, 'aliases': ['Cacao']},
    "SP_THEKO": {'description': 'Thermococcus kodakaraensis (euryarchaea) - Proteome: UP000000536', 'meaning': 'NCBITaxon:69014', 'annotations': {'sources': 'GO'}, 'aliases': ['euryarchaea']},
    "SP_THEMA": {'description': 'Thermotoga maritima (thermotogae bacteria) - Proteome: UP000008183', 'meaning': 'NCBITaxon:243274', 'annotations': {'sources': 'GO'}, 'aliases': ['thermotogae bacteria']},
    "SP_THEYD": {'description': 'Thermodesulfovibrio yellowstonii (nitrospirae bacteria) - Proteome: UP000000718', 'meaning': 'NCBITaxon:289376', 'annotations': {'sources': 'GO'}, 'aliases': ['nitrospirae bacteria']},
    "SP_TOBAC": {'description': 'Nicotiana tabacum (Common tobacco) - Proteome: UP000084051', 'meaning': 'NCBITaxon:4097', 'annotations': {'sources': 'common, GO'}, 'aliases': ['Common tobacco']},
    "SP_TOXGO": {'description': 'Toxoplasma gondii ME49 - Proteome: UP000001529', 'meaning': 'NCBITaxon:508771', 'annotations': {'sources': 'existing'}},
    "SP_TRIAD": {'description': 'Trichoplax adhaerens (placozoan) - Proteome: UP000009022', 'meaning': 'NCBITaxon:10228', 'annotations': {'sources': 'GO'}, 'aliases': ['placozoan']},
    "SP_TRICA": {'description': 'Tribolium castaneum (Red flour beetle) - Proteome: UP000007266', 'meaning': 'NCBITaxon:7070', 'annotations': {'sources': 'GO'}, 'aliases': ['Red flour beetle']},
    "SP_TRIV3": {'description': 'Trichomonas vaginalis (excavate) - Proteome: UP000001542', 'meaning': 'NCBITaxon:412133', 'annotations': {'sources': 'GO'}, 'aliases': ['excavate']},
    "SP_TRYB2": {'description': 'Trypanosoma brucei brucei TREU927 (excavate) - Proteome: UP000008524', 'meaning': 'NCBITaxon:185431', 'annotations': {'sources': 'GO'}, 'aliases': ['excavate']},
    "SP_VACCW": {'description': 'Vaccinia virus (strain Western Reserve) (VACV strain WR) - Proteome: UP000000344', 'meaning': 'NCBITaxon:10254', 'annotations': {'sources': 'GO'}, 'aliases': ['VACV strain WR']},
    "SP_VAR67": {'description': 'Variola virus (Smallpox virus) (isolate Human/India/Ind3/1967) (VARV) - Proteome: UP000002060', 'meaning': 'NCBITaxon:587200', 'annotations': {'sources': 'GO'}, 'aliases': ['VARV']},
    "SP_VIBCH": {'description': 'Vibrio cholerae (cholera) - Proteome: UP000000584', 'meaning': 'NCBITaxon:243277', 'annotations': {'sources': 'GO'}, 'aliases': ['cholera']},
    "SP_VITVI": {'description': 'Vitis vinifera (Grape) - Proteome: UP000009183', 'meaning': 'NCBITaxon:29760', 'annotations': {'sources': 'GO'}, 'aliases': ['Grape']},
    "SP_VZVD": {'description': 'Varicella-zoster virus (Human herpesvirus 3) strain Dumas (HHV-3 strain Dumas) - Proteome: UP000002602', 'meaning': 'NCBITaxon:10338', 'annotations': {'sources': 'GO'}, 'aliases': ['HHV-3 strain Dumas']},
    "SP_WHEAT": {'description': 'Triticum aestivum (Wheat) - Proteome: UP000019116', 'meaning': 'NCBITaxon:4565', 'annotations': {'sources': 'GO'}, 'aliases': ['Wheat']},
    "SP_XANCP": {'description': 'Xanthomonas campestris (xanthomonas) - Proteome: UP000001010', 'meaning': 'NCBITaxon:340', 'annotations': {'sources': 'GO'}, 'aliases': ['xanthomonas']},
    "SP_XENLA": {'description': 'Xenopus laevis (African clawed frog) - Proteome: UP000186698', 'meaning': 'NCBITaxon:8355', 'annotations': {'sources': 'common, GO'}, 'aliases': ['African clawed frog']},
    "SP_XENTR": {'description': 'Xenopus tropicalis (Western clawed frog) - Proteome: UP000008143', 'meaning': 'NCBITaxon:8364', 'annotations': {'sources': 'common, GO'}, 'aliases': ['Western clawed frog']},
    "SP_YARLI": {'description': 'Yarrowia lipolytica (Yeast) - Proteome: UP000001300', 'meaning': 'NCBITaxon:4952', 'annotations': {'sources': 'GO'}, 'aliases': ['Yeast']},
    "SP_YEAST": {'description': "Saccharomyces cerevisiae S288C (Baker's yeast) - Proteome: UP000002311", 'meaning': 'NCBITaxon:559292', 'annotations': {'sources': 'common, GO'}, 'aliases': ["Baker's yeast"]},
    "SP_YERPE": {'description': 'Yersinia pestis (plague bacteria) - Proteome: UP000000815', 'meaning': 'NCBITaxon:632', 'annotations': {'sources': 'GO'}, 'aliases': ['plague bacteria']},
    "SP_ZIKV": {'description': 'Zika virus (ZIKV) - Proteome: UP000054557', 'meaning': 'NCBITaxon:64320', 'annotations': {'sources': 'GO'}, 'aliases': ['ZIKV']},
}

__all__ = [
    "UniProtSpeciesCode",
]