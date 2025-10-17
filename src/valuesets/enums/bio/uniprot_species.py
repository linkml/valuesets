"""
UniProt Species Codes Value Sets

Value sets for UniProt species mnemonic codes with associated proteome IDs

Generated from: bio/uniprot_species.yaml
"""

from __future__ import annotations

from typing import Dict, Any, Optional
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
    SP_ARATH = "SP_ARATH"
    SP_BACSU = "SP_BACSU"
    SP_BOVIN = "SP_BOVIN"
    SP_CAEEL = "SP_CAEEL"
    SP_CANLF = "SP_CANLF"
    SP_CHICK = "SP_CHICK"
    SP_DANRE = "SP_DANRE"
    SP_DROME = "SP_DROME"
    SP_ECOLI = "SP_ECOLI"
    SP_FELCA = "SP_FELCA"
    SP_GORGO = "SP_GORGO"
    SP_HORSE = "SP_HORSE"
    SP_HUMAN = "SP_HUMAN"
    SP_MACMU = "SP_MACMU"
    SP_MAIZE = "SP_MAIZE"
    SP_MOUSE = "SP_MOUSE"
    SP_ORYSJ = "SP_ORYSJ"
    SP_PANTR = "SP_PANTR"
    SP_PIG = "SP_PIG"
    SP_RABIT = "SP_RABIT"
    SP_RAT = "SP_RAT"
    SP_SCHPO = "SP_SCHPO"
    SP_SHEEP = "SP_SHEEP"
    SP_XENLA = "SP_XENLA"
    SP_XENTR = "SP_XENTR"
    SP_YEAST = "SP_YEAST"
    SP_DICDI = "SP_DICDI"
    SP_HELPY = "SP_HELPY"
    SP_LEIMA = "SP_LEIMA"
    SP_MEDTR = "SP_MEDTR"
    SP_MYCTU = "SP_MYCTU"
    SP_NEIME = "SP_NEIME"
    SP_PLAF7 = "SP_PLAF7"
    SP_PSEAE = "SP_PSEAE"
    SP_SOYBN = "SP_SOYBN"
    SP_STAAU = "SP_STAAU"
    SP_STRPN = "SP_STRPN"
    SP_TOXGO = "SP_TOXGO"
    SP_TRYB2 = "SP_TRYB2"
    SP_WHEAT = "SP_WHEAT"
    SP_PEA = "SP_PEA"
    SP_TOBAC = "SP_TOBAC"

# Set metadata after class creation
UniProtSpeciesCode._metadata = {
    "SP_9ABAC": {'description': 'Lambdina fiscellaria nucleopolyhedrovirus - Proteome: UP000201190', 'meaning': 'NCBITaxon:1642929'},
    "SP_9ACAR": {'description': 'Tropilaelaps mercedesae - Proteome: UP000192247', 'meaning': 'NCBITaxon:418985'},
    "SP_9ACTN": {'description': 'Candidatus Protofrankia datiscae - Proteome: UP000001549', 'meaning': 'NCBITaxon:2716812'},
    "SP_9ACTO": {'description': 'Actinomyces massiliensis F0489 - Proteome: UP000002941', 'meaning': 'NCBITaxon:1125718'},
    "SP_9ADEN": {'description': 'Human adenovirus 53 - Proteome: UP000463865', 'meaning': 'NCBITaxon:556926'},
    "SP_9AGAM": {'description': 'Jaapia argillacea MUCL 33604 - Proteome: UP000027265', 'meaning': 'NCBITaxon:933084'},
    "SP_9AGAR": {'description': 'Collybiopsis luxurians FD-317 M1 - Proteome: UP000053593', 'meaning': 'NCBITaxon:944289'},
    "SP_9ALPC": {'description': 'Feline coronavirus - Proteome: UP000141821', 'meaning': 'NCBITaxon:12663'},
    "SP_9ALPH": {'description': 'Testudinid alphaherpesvirus 3 - Proteome: UP000100290', 'meaning': 'NCBITaxon:2560801'},
    "SP_9ALTE": {'description': 'Paraglaciecola arctica BSs20135 - Proteome: UP000006327', 'meaning': 'NCBITaxon:493475'},
    "SP_9ALVE": {'description': 'Perkinsus sp. BL_2016 - Proteome: UP000298064', 'meaning': 'NCBITaxon:2494336'},
    "SP_9AMPH": {'description': 'Microcaecilia unicolor - Proteome: UP000515156', 'meaning': 'NCBITaxon:1415580'},
    "SP_9ANNE": {'description': 'Dimorphilus gyrociliatus - Proteome: UP000549394', 'meaning': 'NCBITaxon:2664684'},
    "SP_9ANUR": {'description': 'Leptobrachium leishanense (Leishan spiny toad) - Proteome: UP000694569', 'meaning': 'NCBITaxon:445787'},
    "SP_9APHY": {'description': 'Fibroporia radiculosa - Proteome: UP000006352', 'meaning': 'NCBITaxon:599839'},
    "SP_9APIA": {'description': 'Heracleum sosnowskyi - Proteome: UP001237642', 'meaning': 'NCBITaxon:360622'},
    "SP_9APIC": {'description': 'Babesia sp. Xinjiang - Proteome: UP000193856', 'meaning': 'NCBITaxon:462227'},
    "SP_9AQUI": {'description': 'Sulfurihydrogenibium yellowstonense SS-5 - Proteome: UP000005540', 'meaning': 'NCBITaxon:432331'},
    "SP_9ARAC": {'description': 'Trichonephila inaurata madagascariensis - Proteome: UP000886998', 'meaning': 'NCBITaxon:2747483'},
    "SP_9ARCH": {'description': 'Candidatus Nitrosarchaeum limnium BG20 - Proteome: UP000014065', 'meaning': 'NCBITaxon:859192'},
    "SP_9ASCO": {'description': 'Kuraishia capsulata CBS 1993 - Proteome: UP000019384', 'meaning': 'NCBITaxon:1382522'},
    "SP_9ASPA": {'description': 'Dendrobium catenatum - Proteome: UP000233837', 'meaning': 'NCBITaxon:906689'},
    "SP_9ASTE": {'description': 'Cuscuta australis - Proteome: UP000249390', 'meaning': 'NCBITaxon:267555'},
    "SP_9ASTR": {'description': 'Mikania micrantha - Proteome: UP000326396', 'meaning': 'NCBITaxon:192012'},
    "SP_9AVES": {'description': 'Anser brachyrhynchus (Pink-footed goose) - Proteome: UP000694426', 'meaning': 'NCBITaxon:132585'},
    "SP_9BACE": {'description': 'Bacteroides caccae CL03T12C61 - Proteome: UP000002965', 'meaning': 'NCBITaxon:997873'},
    "SP_9BACI": {'description': 'Fictibacillus macauensis ZFHKF-1 - Proteome: UP000004080', 'meaning': 'NCBITaxon:1196324'},
    "SP_9BACL": {'description': 'Paenibacillus sp. HGF7 - Proteome: UP000003445', 'meaning': 'NCBITaxon:944559'},
    "SP_9BACT": {'description': 'Parabacteroides johnsonii CL02T12C29 - Proteome: UP000001218', 'meaning': 'NCBITaxon:999419'},
    "SP_9BACU": {'description': 'Samia ricini nucleopolyhedrovirus - Proteome: UP001226138', 'meaning': 'NCBITaxon:1920700'},
    "SP_9BASI": {'description': 'Malassezia pachydermatis - Proteome: UP000037751', 'meaning': 'NCBITaxon:77020'},
    "SP_9BBAC": {'description': 'Plutella xylostella granulovirus - Proteome: UP000201310', 'meaning': 'NCBITaxon:98383'},
    "SP_9BETA": {'description': 'Saimiriine betaherpesvirus 4 - Proteome: UP000097892', 'meaning': 'NCBITaxon:1535247'},
    "SP_9BETC": {'description': 'Coronavirus BtRt-BetaCoV/GX2018 - Proteome: UP001228689', 'meaning': 'NCBITaxon:2591238'},
    "SP_9BIFI": {'description': 'Scardovia wiggsiae F0424 - Proteome: UP000006415', 'meaning': 'NCBITaxon:857290'},
    "SP_9BILA": {'description': 'Ancylostoma ceylanicum - Proteome: UP000024635', 'meaning': 'NCBITaxon:53326'},
    "SP_9BIVA": {'description': 'Potamilus streckersoni - Proteome: UP001195483', 'meaning': 'NCBITaxon:2493646'},
    "SP_9BORD": {'description': 'Bordetella sp. N - Proteome: UP000064621', 'meaning': 'NCBITaxon:1746199'},
    "SP_9BRAD": {'description': 'Afipia broomeae ATCC 49717 - Proteome: UP000001096', 'meaning': 'NCBITaxon:883078'},
    "SP_9BRAS": {'description': 'Capsella rubella - Proteome: UP000029121', 'meaning': 'NCBITaxon:81985'},
    "SP_9BROM": {'description': 'Prune dwarf virus - Proteome: UP000202132', 'meaning': 'NCBITaxon:33760'},
    "SP_9BURK": {'description': 'Candidatus Paraburkholderia kirkii UZHbot1 - Proteome: UP000003511', 'meaning': 'NCBITaxon:1055526'},
    "SP_9CARY": {'description': 'Carnegiea gigantea - Proteome: UP001153076', 'meaning': 'NCBITaxon:171969'},
    "SP_9CAUD": {'description': 'Salmonella phage Vi06 - Proteome: UP000000335', 'meaning': 'NCBITaxon:866889'},
    "SP_9CAUL": {'description': 'Brevundimonas abyssalis TAR-001 - Proteome: UP000016569', 'meaning': 'NCBITaxon:1391729'},
    "SP_9CBAC": {'description': 'Neodiprion sertifer nucleopolyhedrovirus - Proteome: UP000243697', 'meaning': 'NCBITaxon:111874'},
    "SP_9CELL": {'description': 'Actinotalea ferrariae CF5-4 - Proteome: UP000019753', 'meaning': 'NCBITaxon:948458'},
    "SP_9CERV": {'description': 'Cervus hanglu yarkandensis (Yarkand deer) - Proteome: UP000631465', 'meaning': 'NCBITaxon:84702'},
    "SP_9CETA": {'description': 'Catagonus wagneri (Chacoan peccary) - Proteome: UP000694540', 'meaning': 'NCBITaxon:51154'},
    "SP_9CHAR": {'description': 'Rostratula benghalensis (greater painted-snipe) - Proteome: UP000545435', 'meaning': 'NCBITaxon:118793'},
    "SP_9CHIR": {'description': 'Phyllostomus discolor (pale spear-nosed bat) - Proteome: UP000504628', 'meaning': 'NCBITaxon:89673'},
    "SP_9CHLA": {'description': 'Chlamydiales bacterium SCGC AG-110-P3 - Proteome: UP000196763', 'meaning': 'NCBITaxon:1871323'},
    "SP_9CHLB": {'description': 'Chlorobium ferrooxidans DSM 13031 - Proteome: UP000004162', 'meaning': 'NCBITaxon:377431'},
    "SP_9CHLO": {'description': 'Helicosporidium sp. ATCC 50920 - Proteome: UP000026042', 'meaning': 'NCBITaxon:1291522'},
    "SP_9CHLR": {'description': 'Ardenticatena maritima - Proteome: UP000037784', 'meaning': 'NCBITaxon:872965'},
    "SP_9CHRO": {'description': 'Gloeocapsa sp. PCC 7428 - Proteome: UP000010476', 'meaning': 'NCBITaxon:1173026'},
    "SP_9CICH": {'description': 'Maylandia zebra (zebra mbuna) - Proteome: UP000265160', 'meaning': 'NCBITaxon:106582'},
    "SP_9CILI": {'description': 'Stentor coeruleus - Proteome: UP000187209', 'meaning': 'NCBITaxon:5963'},
    "SP_9CIRC": {'description': 'Raven circovirus - Proteome: UP000097131', 'meaning': 'NCBITaxon:345250'},
    "SP_9CLOS": {'description': 'Grapevine leafroll-associated virus 10 - Proteome: UP000203128', 'meaning': 'NCBITaxon:367121'},
    "SP_9CLOT": {'description': 'Candidatus Arthromitus sp. SFB-rat-Yit - Proteome: UP000001273', 'meaning': 'NCBITaxon:1041504'},
    "SP_9CNID": {'description': 'Clytia hemisphaerica - Proteome: UP000594262', 'meaning': 'NCBITaxon:252671'},
    "SP_9COLU": {'description': 'Pampusana beccarii (Western bronze ground-dove) - Proteome: UP000541332', 'meaning': 'NCBITaxon:2953425'},
    "SP_9CORV": {'description': "Cnemophilus loriae (Loria's bird-of-paradise) - Proteome: UP000517678", 'meaning': 'NCBITaxon:254448'},
    "SP_9CORY": {'description': 'Corynebacterium genitalium ATCC 33030 - Proteome: UP000004208', 'meaning': 'NCBITaxon:585529'},
    "SP_9COXI": {'description': 'Coxiella endosymbiont of Amblyomma americanum - Proteome: UP000059222', 'meaning': 'NCBITaxon:325775'},
    "SP_9CREN": {'description': 'Metallosphaera yellowstonensis MK1 - Proteome: UP000003980', 'meaning': 'NCBITaxon:671065'},
    "SP_9CRUS": {'description': 'Daphnia magna - Proteome: UP000076858', 'meaning': 'NCBITaxon:35525'},
    "SP_9CUCU": {'description': 'Ceutorhynchus assimilis (cabbage seed weevil) - Proteome: UP001152799', 'meaning': 'NCBITaxon:467358'},
    "SP_9CYAN": {'description': 'Leptolyngbyaceae cyanobacterium JSC-12 - Proteome: UP000001332', 'meaning': 'NCBITaxon:864702'},
    "SP_9DEIN": {'description': 'Meiothermus sp. QL-1 - Proteome: UP000255346', 'meaning': 'NCBITaxon:2058095'},
    "SP_9DEIO": {'description': 'Deinococcus sp. RL - Proteome: UP000027898', 'meaning': 'NCBITaxon:1489678'},
    "SP_9DELA": {'description': 'Human T-cell leukemia virus type I - Proteome: UP000108043', 'meaning': 'NCBITaxon:11908'},
    "SP_9DELT": {'description': 'Lujinxingia litoralis - Proteome: UP000249169', 'meaning': 'NCBITaxon:2211119'},
    "SP_9DEND": {'description': 'Xiphorhynchus elegans (elegant woodcreeper) - Proteome: UP000551443', 'meaning': 'NCBITaxon:269412'},
    "SP_9DINO": {'description': 'Symbiodinium necroappetens - Proteome: UP000601435', 'meaning': 'NCBITaxon:1628268'},
    "SP_9DIPT": {'description': 'Clunio marinus - Proteome: UP000183832', 'meaning': 'NCBITaxon:568069'},
    "SP_9EIME": {'description': 'Eimeria praecox - Proteome: UP000018201', 'meaning': 'NCBITaxon:51316'},
    "SP_9EMBE": {'description': 'Emberiza fucata - Proteome: UP000580681', 'meaning': 'NCBITaxon:337179'},
    "SP_9ENTE": {'description': 'Enterococcus asini ATCC 700915 - Proteome: UP000013777', 'meaning': 'NCBITaxon:1158606'},
    "SP_9ENTR": {'description': 'secondary endosymbiont of Heteropsylla cubana - Proteome: UP000003937', 'meaning': 'NCBITaxon:134287'},
    "SP_9ERIC": {'description': 'Rhododendron williamsianum - Proteome: UP000428333', 'meaning': 'NCBITaxon:262921'},
    "SP_9EUCA": {'description': 'Petrolisthes manimaculis - Proteome: UP001292094', 'meaning': 'NCBITaxon:1843537'},
    "SP_9EUGL": {'description': 'Perkinsela sp. CCAP 1560/4 - Proteome: UP000036983', 'meaning': 'NCBITaxon:1314962'},
    "SP_9EUKA": {'description': 'Chrysochromulina tobinii - Proteome: UP000037460', 'meaning': 'NCBITaxon:1460289'},
    "SP_9EUPU": {'description': 'Candidula unifasciata - Proteome: UP000678393', 'meaning': 'NCBITaxon:100452'},
    "SP_9EURO": {'description': 'Cladophialophora psammophila CBS 110553 - Proteome: UP000019471', 'meaning': 'NCBITaxon:1182543'},
    "SP_9EURY": {'description': 'Methanoplanus limicola DSM 2279 - Proteome: UP000005741', 'meaning': 'NCBITaxon:937775'},
    "SP_9FABA": {'description': 'Senna tora - Proteome: UP000634136', 'meaning': 'NCBITaxon:362788'},
    "SP_9FIRM": {'description': 'Ruminococcaceae bacterium D16 - Proteome: UP000002801', 'meaning': 'NCBITaxon:552398'},
    "SP_9FLAO": {'description': 'Capnocytophaga sp. oral taxon 338 str. F0234 - Proteome: UP000003023', 'meaning': 'NCBITaxon:888059'},
    "SP_9FLAV": {'description': 'Tunisian sheep-like pestivirus - Proteome: UP001157330', 'meaning': 'NCBITaxon:3071305'},
    "SP_9FLOR": {'description': 'Gracilariopsis chorda - Proteome: UP000247409', 'meaning': 'NCBITaxon:448386'},
    "SP_9FRIN": {'description': 'Urocynchramus pylzowi - Proteome: UP000524542', 'meaning': 'NCBITaxon:571890'},
    "SP_9FUNG": {'description': 'Lichtheimia corymbifera JMRC:FSU:9682 - Proteome: UP000027586', 'meaning': 'NCBITaxon:1263082'},
    "SP_9FURN": {'description': 'Furnarius figulus - Proteome: UP000529852', 'meaning': 'NCBITaxon:463165'},
    "SP_9FUSO": {'description': 'Fusobacterium gonidiaformans 3-1-5R - Proteome: UP000002975', 'meaning': 'NCBITaxon:469605'},
    "SP_9GALL": {'description': 'Odontophorus gujanensis (marbled wood quail) - Proteome: UP000522663', 'meaning': 'NCBITaxon:886794'},
    "SP_9GAMA": {'description': 'Bovine gammaherpesvirus 6 - Proteome: UP000121539', 'meaning': 'NCBITaxon:1504288'},
    "SP_9GAMC": {'description': 'Anser fabalis coronavirus NCN2 - Proteome: UP001251675', 'meaning': 'NCBITaxon:2860474'},
    "SP_9GAMM": {'description': 'Buchnera aphidicola (Cinara tujafilina) - Proteome: UP000006811', 'meaning': 'NCBITaxon:261317', 'aliases': ['Buchnera aphidicola (Cinara tujafilina)']},
    "SP_9GAST": {'description': 'Elysia crispata (lettuce slug) - Proteome: UP001283361', 'meaning': 'NCBITaxon:231223'},
    "SP_9GEMI": {'description': 'East African cassava mosaic Zanzibar virus - Proteome: UP000201107', 'meaning': 'NCBITaxon:223275'},
    "SP_9GLOM": {'description': 'Paraglomus occultum - Proteome: UP000789572', 'meaning': 'NCBITaxon:144539'},
    "SP_9GOBI": {'description': 'Neogobius melanostomus (round goby) - Proteome: UP000694523', 'meaning': 'NCBITaxon:47308'},
    "SP_9GRUI": {'description': 'Atlantisia rogersi (Inaccessible Island rail) - Proteome: UP000518911', 'meaning': 'NCBITaxon:2478892'},
    "SP_9HELI": {'description': 'Helicobacter bilis ATCC 43879 - Proteome: UP000005085', 'meaning': 'NCBITaxon:613026'},
    "SP_9HELO": {'description': 'Rhynchosporium graminicola - Proteome: UP000178129', 'meaning': 'NCBITaxon:2792576'},
    "SP_9HEMI": {'description': 'Cinara cedri - Proteome: UP000325440', 'meaning': 'NCBITaxon:506608'},
    "SP_9HEPA": {'description': 'Duck hepatitis B virus - Proteome: UP000137229', 'meaning': 'NCBITaxon:12639'},
    "SP_9HEXA": {'description': 'Allacma fusca - Proteome: UP000708208', 'meaning': 'NCBITaxon:39272'},
    "SP_9HYME": {'description': 'Melipona quadrifasciata - Proteome: UP000053105', 'meaning': 'NCBITaxon:166423'},
    "SP_9HYPH": {'description': 'Mesorhizobium amorphae CCNWGS0123 - Proteome: UP000002949', 'meaning': 'NCBITaxon:1082933'},
    "SP_9HYPO": {'description': '[Torrubiella] hemipterigena - Proteome: UP000039046', 'meaning': 'NCBITaxon:1531966'},
    "SP_9INFA": {'description': 'Influenza A virus (A/California/VRDL364/2009 (mixed) - Proteome: UP000109975', 'meaning': 'NCBITaxon:1049605', 'aliases': ['Influenza A virus (A/California/VRDL364/2009(mixed))']},
    "SP_9INSE": {'description': 'Cloeon dipterum - Proteome: UP000494165', 'meaning': 'NCBITaxon:197152'},
    "SP_9LABR": {'description': 'Labrus bergylta (ballan wrasse) - Proteome: UP000261660', 'meaning': 'NCBITaxon:56723'},
    "SP_ARATH": {'description': 'Arabidopsis thaliana (Thale cress) - Proteome: UP000006548', 'meaning': 'NCBITaxon:3702', 'aliases': ['Thale cress']},
    "SP_BACSU": {'description': 'Bacillus subtilis subsp. subtilis str. 168 - Proteome: UP000001570', 'meaning': 'NCBITaxon:224308'},
    "SP_BOVIN": {'description': 'Bos taurus (Cattle) - Proteome: UP000009136', 'meaning': 'NCBITaxon:9913', 'aliases': ['Cattle']},
    "SP_CAEEL": {'description': 'Caenorhabditis elegans - Proteome: UP000001940', 'meaning': 'NCBITaxon:6239'},
    "SP_CANLF": {'description': 'Canis lupus familiaris (Dog) - Proteome: UP000805418', 'meaning': 'NCBITaxon:9615', 'aliases': ['Dog']},
    "SP_CHICK": {'description': 'Gallus gallus (Chicken) - Proteome: UP000000539', 'meaning': 'NCBITaxon:9031', 'aliases': ['Chicken']},
    "SP_DANRE": {'description': 'Danio rerio (Zebrafish) - Proteome: UP000000437', 'meaning': 'NCBITaxon:7955', 'aliases': ['Zebrafish']},
    "SP_DROME": {'description': 'Drosophila melanogaster (Fruit fly) - Proteome: UP000000803', 'meaning': 'NCBITaxon:7227', 'aliases': ['Fruit fly']},
    "SP_ECOLI": {'description': 'Escherichia coli K-12 - Proteome: UP000000625', 'meaning': 'NCBITaxon:83333'},
    "SP_FELCA": {'description': 'Felis catus (Cat) - Proteome: UP000011712', 'meaning': 'NCBITaxon:9685', 'aliases': ['Cat']},
    "SP_GORGO": {'description': 'Gorilla gorilla gorilla (Western lowland gorilla) - Proteome: UP000001519', 'meaning': 'NCBITaxon:9593', 'aliases': ['Western lowland gorilla']},
    "SP_HORSE": {'description': 'Equus caballus (Horse) - Proteome: UP000002281', 'meaning': 'NCBITaxon:9796', 'aliases': ['Horse']},
    "SP_HUMAN": {'description': 'Homo sapiens (Human) - Proteome: UP000005640', 'meaning': 'NCBITaxon:9606', 'aliases': ['Human']},
    "SP_MACMU": {'description': 'Macaca mulatta (Rhesus macaque) - Proteome: UP000006718', 'meaning': 'NCBITaxon:9544', 'aliases': ['Rhesus macaque']},
    "SP_MAIZE": {'description': 'Zea mays (Maize) - Proteome: UP000007305', 'meaning': 'NCBITaxon:4577', 'aliases': ['Maize']},
    "SP_MOUSE": {'description': 'Mus musculus (Mouse) - Proteome: UP000000589', 'meaning': 'NCBITaxon:10090', 'aliases': ['Mouse']},
    "SP_ORYSJ": {'description': 'Oryza sativa subsp. japonica (Rice) - Proteome: UP000059680', 'meaning': 'NCBITaxon:39947', 'aliases': ['Rice']},
    "SP_PANTR": {'description': 'Pan troglodytes (Chimpanzee) - Proteome: UP000002277', 'meaning': 'NCBITaxon:9598', 'aliases': ['Chimpanzee']},
    "SP_PIG": {'description': 'Sus scrofa (Pig) - Proteome: UP000008227', 'meaning': 'NCBITaxon:9823', 'aliases': ['Pig']},
    "SP_RABIT": {'description': 'Oryctolagus cuniculus (Rabbit) - Proteome: UP000001811', 'meaning': 'NCBITaxon:9986', 'aliases': ['Rabbit']},
    "SP_RAT": {'description': 'Rattus norvegicus (Rat) - Proteome: UP000002494', 'meaning': 'NCBITaxon:10116', 'aliases': ['Rat']},
    "SP_SCHPO": {'description': 'Schizosaccharomyces pombe 972h- (Fission yeast) - Proteome: UP000002485', 'meaning': 'NCBITaxon:284812', 'aliases': ['Fission yeast']},
    "SP_SHEEP": {'description': 'Ovis aries (Sheep) - Proteome: UP000002356', 'meaning': 'NCBITaxon:9940', 'aliases': ['Sheep']},
    "SP_XENLA": {'description': 'Xenopus laevis (African clawed frog) - Proteome: UP000186698', 'meaning': 'NCBITaxon:8355', 'aliases': ['African clawed frog']},
    "SP_XENTR": {'description': 'Xenopus tropicalis (Western clawed frog) - Proteome: UP000008143', 'meaning': 'NCBITaxon:8364', 'aliases': ['Western clawed frog']},
    "SP_YEAST": {'description': "Saccharomyces cerevisiae S288C (Baker's yeast) - Proteome: UP000002311", 'meaning': 'NCBITaxon:559292', 'aliases': ["Baker's yeast"]},
    "SP_DICDI": {'description': 'Dictyostelium discoideum (Slime mold) - Proteome: UP000002195', 'meaning': 'NCBITaxon:44689', 'aliases': ['Slime mold']},
    "SP_HELPY": {'description': 'Helicobacter pylori 26695 - Proteome: UP000000429', 'meaning': 'NCBITaxon:85962'},
    "SP_LEIMA": {'description': 'Leishmania major strain Friedlin', 'meaning': 'NCBITaxon:347515'},
    "SP_MEDTR": {'description': 'Medicago truncatula (Barrel medic) - Proteome: UP000002051', 'meaning': 'NCBITaxon:3880', 'aliases': ['Barrel medic']},
    "SP_MYCTU": {'description': 'Mycobacterium tuberculosis H37Rv - Proteome: UP000001584', 'meaning': 'NCBITaxon:83332'},
    "SP_NEIME": {'description': 'Neisseria meningitidis MC58 - Proteome: UP000000425', 'meaning': 'NCBITaxon:122586'},
    "SP_PLAF7": {'description': 'Plasmodium falciparum 3D7 (Malaria parasite) - Proteome: UP000001450', 'meaning': 'NCBITaxon:36329', 'aliases': ['Malaria parasite']},
    "SP_PSEAE": {'description': 'Pseudomonas aeruginosa PAO1 - Proteome: UP000002438', 'meaning': 'NCBITaxon:208964'},
    "SP_SOYBN": {'description': 'Glycine max (Soybean) - Proteome: UP000008827', 'meaning': 'NCBITaxon:3847', 'aliases': ['Soybean']},
    "SP_STAAU": {'description': 'Staphylococcus aureus subsp. aureus NCTC 8325 - Proteome: UP000008816', 'meaning': 'NCBITaxon:93061'},
    "SP_STRPN": {'description': 'Streptococcus pneumoniae R6 - Proteome: UP000000586', 'meaning': 'NCBITaxon:171101'},
    "SP_TOXGO": {'description': 'Toxoplasma gondii ME49 - Proteome: UP000001529', 'meaning': 'NCBITaxon:508771'},
    "SP_TRYB2": {'description': 'Trypanosoma brucei brucei TREU927 - Proteome: UP000008524', 'meaning': 'NCBITaxon:185431'},
    "SP_WHEAT": {'description': 'Triticum aestivum (Wheat) - Proteome: UP000019116', 'meaning': 'NCBITaxon:4565', 'aliases': ['Wheat']},
    "SP_PEA": {'description': 'Pisum sativum (Garden pea) - Proteome: UP001058974', 'meaning': 'NCBITaxon:3888', 'aliases': ['Garden pea']},
    "SP_TOBAC": {'description': 'Nicotiana tabacum (Common tobacco) - Proteome: UP000084051', 'meaning': 'NCBITaxon:4097', 'aliases': ['Common tobacco']},
}

__all__ = [
    "UniProtSpeciesCode",
]