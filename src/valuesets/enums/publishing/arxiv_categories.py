"""
arXiv Subject Categories

Value sets for arXiv preprint subject categories and taxonomy. Based on the official arXiv category taxonomy.

Generated from: publishing/arxiv_categories.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class ArxivCategory(RichEnum):
    """
    arXiv subject categories for classifying preprints and publications. Categories are organized by major subject groups.
    """
    # Enum members
    CS = "cs"
    ECON = "econ"
    EESS = "eess"
    MATH = "math"
    ASTRO_PH = "astro-ph"
    COND_MAT = "cond-mat"
    HEP = "hep"
    NLIN = "nlin"
    NUCL = "nucl"
    PHYSICS = "physics"
    Q_BIO = "q-bio"
    Q_FIN = "q-fin"
    STAT = "stat"
    CS_AI = "cs.AI"
    CS_AR = "cs.AR"
    CS_CC = "cs.CC"
    CS_CE = "cs.CE"
    CS_CG = "cs.CG"
    CS_CL = "cs.CL"
    CS_CR = "cs.CR"
    CS_CV = "cs.CV"
    CS_CY = "cs.CY"
    CS_DB = "cs.DB"
    CS_DC = "cs.DC"
    CS_DL = "cs.DL"
    CS_DM = "cs.DM"
    CS_DS = "cs.DS"
    CS_ET = "cs.ET"
    CS_FL = "cs.FL"
    CS_GL = "cs.GL"
    CS_GR = "cs.GR"
    CS_GT = "cs.GT"
    CS_HC = "cs.HC"
    CS_IR = "cs.IR"
    CS_IT = "cs.IT"
    CS_LG = "cs.LG"
    CS_LO = "cs.LO"
    CS_MA = "cs.MA"
    CS_MM = "cs.MM"
    CS_MS = "cs.MS"
    CS_NA = "cs.NA"
    CS_NE = "cs.NE"
    CS_NI = "cs.NI"
    CS_OH = "cs.OH"
    CS_OS = "cs.OS"
    CS_PF = "cs.PF"
    CS_PL = "cs.PL"
    CS_RO = "cs.RO"
    CS_SC = "cs.SC"
    CS_SD = "cs.SD"
    CS_SE = "cs.SE"
    CS_SI = "cs.SI"
    CS_SY = "cs.SY"
    ECON_EM = "econ.EM"
    ECON_GN = "econ.GN"
    ECON_TH = "econ.TH"
    EESS_AS = "eess.AS"
    EESS_IV = "eess.IV"
    EESS_SP = "eess.SP"
    EESS_SY = "eess.SY"
    MATH_AC = "math.AC"
    MATH_AG = "math.AG"
    MATH_AP = "math.AP"
    MATH_AT = "math.AT"
    MATH_CA = "math.CA"
    MATH_CO = "math.CO"
    MATH_CT = "math.CT"
    MATH_CV = "math.CV"
    MATH_DG = "math.DG"
    MATH_DS = "math.DS"
    MATH_FA = "math.FA"
    MATH_GM = "math.GM"
    MATH_GN = "math.GN"
    MATH_GR = "math.GR"
    MATH_GT = "math.GT"
    MATH_HO = "math.HO"
    MATH_IT = "math.IT"
    MATH_KT = "math.KT"
    MATH_LO = "math.LO"
    MATH_MG = "math.MG"
    MATH_MP = "math.MP"
    MATH_NA = "math.NA"
    MATH_NT = "math.NT"
    MATH_OA = "math.OA"
    MATH_OC = "math.OC"
    MATH_PR = "math.PR"
    MATH_QA = "math.QA"
    MATH_RA = "math.RA"
    MATH_RT = "math.RT"
    MATH_SG = "math.SG"
    MATH_SP = "math.SP"
    MATH_ST = "math.ST"
    ASTRO_PH_CO = "astro-ph.CO"
    ASTRO_PH_EP = "astro-ph.EP"
    ASTRO_PH_GA = "astro-ph.GA"
    ASTRO_PH_HE = "astro-ph.HE"
    ASTRO_PH_IM = "astro-ph.IM"
    ASTRO_PH_SR = "astro-ph.SR"
    COND_MAT_DIS_NN = "cond-mat.dis-nn"
    COND_MAT_MES_HALL = "cond-mat.mes-hall"
    COND_MAT_MTRL_SCI = "cond-mat.mtrl-sci"
    COND_MAT_OTHER = "cond-mat.other"
    COND_MAT_QUANT_GAS = "cond-mat.quant-gas"
    COND_MAT_SOFT = "cond-mat.soft"
    COND_MAT_STAT_MECH = "cond-mat.stat-mech"
    COND_MAT_STR_EL = "cond-mat.str-el"
    COND_MAT_SUPR_CON = "cond-mat.supr-con"
    HEP_EX = "hep-ex"
    HEP_LAT = "hep-lat"
    HEP_PH = "hep-ph"
    HEP_TH = "hep-th"
    GR_QC = "gr-qc"
    MATH_PH = "math-ph"
    QUANT_PH = "quant-ph"
    NLIN_AO = "nlin.AO"
    NLIN_CD = "nlin.CD"
    NLIN_CG = "nlin.CG"
    NLIN_PS = "nlin.PS"
    NLIN_SI = "nlin.SI"
    NUCL_EX = "nucl-ex"
    NUCL_TH = "nucl-th"
    PHYSICS_ACC_PH = "physics.acc-ph"
    PHYSICS_AO_PH = "physics.ao-ph"
    PHYSICS_APP_PH = "physics.app-ph"
    PHYSICS_ATM_CLUS = "physics.atm-clus"
    PHYSICS_ATOM_PH = "physics.atom-ph"
    PHYSICS_BIO_PH = "physics.bio-ph"
    PHYSICS_CHEM_PH = "physics.chem-ph"
    PHYSICS_CLASS_PH = "physics.class-ph"
    PHYSICS_COMP_PH = "physics.comp-ph"
    PHYSICS_DATA_AN = "physics.data-an"
    PHYSICS_ED_PH = "physics.ed-ph"
    PHYSICS_FLU_DYN = "physics.flu-dyn"
    PHYSICS_GEN_PH = "physics.gen-ph"
    PHYSICS_GEO_PH = "physics.geo-ph"
    PHYSICS_HIST_PH = "physics.hist-ph"
    PHYSICS_INS_DET = "physics.ins-det"
    PHYSICS_MED_PH = "physics.med-ph"
    PHYSICS_OPTICS = "physics.optics"
    PHYSICS_PLASM_PH = "physics.plasm-ph"
    PHYSICS_POP_PH = "physics.pop-ph"
    PHYSICS_SOC_PH = "physics.soc-ph"
    PHYSICS_SPACE_PH = "physics.space-ph"
    Q_BIO_BM = "q-bio.BM"
    Q_BIO_CB = "q-bio.CB"
    Q_BIO_GN = "q-bio.GN"
    Q_BIO_MN = "q-bio.MN"
    Q_BIO_NC = "q-bio.NC"
    Q_BIO_OT = "q-bio.OT"
    Q_BIO_PE = "q-bio.PE"
    Q_BIO_QM = "q-bio.QM"
    Q_BIO_SC = "q-bio.SC"
    Q_BIO_TO = "q-bio.TO"
    Q_FIN_CP = "q-fin.CP"
    Q_FIN_EC = "q-fin.EC"
    Q_FIN_GN = "q-fin.GN"
    Q_FIN_MF = "q-fin.MF"
    Q_FIN_PM = "q-fin.PM"
    Q_FIN_PR = "q-fin.PR"
    Q_FIN_RM = "q-fin.RM"
    Q_FIN_ST = "q-fin.ST"
    Q_FIN_TR = "q-fin.TR"
    STAT_AP = "stat.AP"
    STAT_CO = "stat.CO"
    STAT_ME = "stat.ME"
    STAT_ML = "stat.ML"
    STAT_OT = "stat.OT"
    STAT_TH = "stat.TH"

# Set metadata after class creation
ArxivCategory._metadata = {
    "CS": {'description': 'Computer science research areas'},
    "ECON": {'description': 'Economics research areas'},
    "EESS": {'description': 'Electrical engineering and systems science research areas'},
    "MATH": {'description': 'Mathematics research areas'},
    "ASTRO_PH": {'description': 'Astrophysics research areas'},
    "COND_MAT": {'description': 'Condensed matter physics research areas'},
    "HEP": {'description': 'High energy physics research areas'},
    "NLIN": {'description': 'Nonlinear sciences research areas'},
    "NUCL": {'description': 'Nuclear physics research areas'},
    "PHYSICS": {'description': 'General physics research areas'},
    "Q_BIO": {'description': 'Quantitative biology research areas'},
    "Q_FIN": {'description': 'Quantitative finance research areas'},
    "STAT": {'description': 'Statistics research areas'},
    "CS_AI": {'description': 'Covers all areas of AI except Vision, Robotics, Machine Learning, Multiagent Systems, and NLP. Includes Expert Systems, Theorem Proving, Knowledge Representation, Planning, and Uncertainty in AI.'},
    "CS_AR": {'description': 'Covers systems organization and hardware architecture. Roughly includes material in ACM Subject Class C.0, C.1, and C.5.'},
    "CS_CC": {'description': 'Covers models of computation, complexity classes, structural complexity, complexity tradeoffs, upper and lower bounds.'},
    "CS_CE": {'description': 'Covers applications of computer science to the mathematical modeling of complex systems in science, engineering, and finance.'},
    "CS_CG": {'description': 'Geometric algorithms, discrete differential geometry, and directly related problems.'},
    "CS_CL": {'description': 'Covers natural language processing. Includes computational linguistics, speech processing, text retrieval and processing.'},
    "CS_CR": {'description': 'Covers all areas of cryptography and security including authentication, public key cryptosystems, proof-carrying code, etc.'},
    "CS_CV": {'description': 'Covers image processing, computer vision, pattern recognition, and scene understanding.'},
    "CS_CY": {'description': 'Covers impact of computers on society, computer ethics, information technology and public policy, legal aspects of computing.'},
    "CS_DB": {'description': 'Covers database management, datamining, and data processing. Roughly includes material in ACM Subject Classes H.2, H.3, and H.4.'},
    "CS_DC": {'description': 'Covers fault-tolerance, distributed algorithms, stabilization, parallel computation, and cluster computing.'},
    "CS_DL": {'description': 'Covers all aspects of digital library design and document creation. Note this may overlap with other areas.'},
    "CS_DM": {'description': 'Covers combinatorics, graph theory, applications of probability. Roughly includes material in ACM Subject Classes G.2 and G.3.'},
    "CS_DS": {'description': 'Covers data structures and analysis of algorithms. Roughly includes material in ACM Subject Classes E.1, E.2, F.2.1, and F.2.2.'},
    "CS_ET": {'description': 'Covers approaches to computing based on emerging technologies such as quantum computing, DNA computing, optical computing.'},
    "CS_FL": {'description': 'Covers automata theory, formal language theory, grammars, and combinatorics on words.'},
    "CS_GL": {'description': 'Covers introductory material, survey material, predictions of future trends, biographies, and miscellaneous computer-science related material.'},
    "CS_GR": {'description': 'Covers all aspects of computer graphics. Roughly includes material in ACM Subject Classes I.3.0-I.3.8.'},
    "CS_GT": {'description': 'Covers all theoretical and applied aspects at the intersection of computer science and game theory.'},
    "CS_HC": {'description': 'Covers human factors, user interfaces, and collaborative computing. Roughly includes material in ACM Subject Classes H.1.2 and H.5.'},
    "CS_IR": {'description': 'Covers indexing, dictionaries, retrieval, content and analysis. Roughly includes material in ACM Subject Classes H.3.0-H.3.4.'},
    "CS_IT": {'description': 'Covers theoretical and experimental aspects of information theory and coding.'},
    "CS_LG": {'description': 'Papers on all aspects of machine learning research, including supervised, unsupervised, reinforcement learning, bandit algorithms.'},
    "CS_LO": {'description': 'Covers all aspects of logic in computer science, including finite model theory, logics of programs, modal logic, and program verification.'},
    "CS_MA": {'description': 'Covers multiagent systems, distributed artificial intelligence, intelligent agents, coordinated interactions.'},
    "CS_MM": {'description': 'Covers all aspects of multimedia systems, including hypermedia and information systems design.'},
    "CS_MS": {'description': 'Covers aspects of mathematical software for mathematical computation and related support.'},
    "CS_NA": {'description': 'Covers numerical algorithms for problems in analysis and algebra. Includes numerical linear algebra, optimization, and interpolation.'},
    "CS_NE": {'description': 'Covers neural networks, connectionism, genetic algorithms, artificial life, adaptive behavior.'},
    "CS_NI": {'description': 'Covers all aspects of computer communication networks, including network architecture and design.'},
    "CS_OH": {'description': 'Covers topics not fitting other computer science categories.'},
    "CS_OS": {'description': 'Covers aspects of operating systems including structure, design, management, and synchronization.'},
    "CS_PF": {'description': 'Covers performance measurement, simulation, and evaluation methodology.'},
    "CS_PL": {'description': 'Covers programming language semantics, language features, programming approaches, compilers.'},
    "CS_RO": {'description': 'Covers all aspects of robotics, including control, manipulation, planning, and robot learning.'},
    "CS_SC": {'description': 'Covers symbolics, including computer algebra systems, implementation, and applications.'},
    "CS_SD": {'description': 'Covers all aspects of computing with sound, and sound as an information channel.'},
    "CS_SE": {'description': 'Covers design tools, software metrics, testing and debugging, programming environments, requirements, specifications.'},
    "CS_SI": {'description': 'Covers design, analysis, and modeling of social and information networks, including their applications for online systems.'},
    "CS_SY": {'description': 'Covers theoretical and practical aspects of systems and control, including control system design.'},
    "ECON_EM": {'description': 'Econometric theory and practice, including estimation, hypothesis testing, and forecasting.'},
    "ECON_GN": {'description': 'General methodological, applied, and empirical contributions to economics.'},
    "ECON_TH": {'description': 'Includes decision theory, game theory, mechanism design, and mathematical modeling in economics.'},
    "EESS_AS": {'description': 'Theory and methods for processing signals representing audio, speech, and language, and their applications.'},
    "EESS_IV": {'description': 'Theory, algorithms, and applications for the formation, capture, processing, communication, analysis, and display of images.'},
    "EESS_SP": {'description': 'Theory, algorithms, performance analysis and applications of signal and data analysis.'},
    "EESS_SY": {'description': 'Analysis and design of control systems, covering mathematical modeling and automatic control.'},
    "MATH_AC": {'description': 'Commutative rings, modules, ideals, homological algebra, computational aspects, local rings.'},
    "MATH_AG": {'description': 'Algebraic varieties, stacks, sheaves, schemes, moduli spaces, complex geometry, quantum cohomology.'},
    "MATH_AP": {'description': 'Existence and uniqueness, boundary conditions, linear and non-linear operators, stability, soliton theory.'},
    "MATH_AT": {'description': 'Homotopy theory, homological algebra, algebraic treatments of manifolds.'},
    "MATH_CA": {'description': 'Special functions, orthogonal polynomials, harmonic analysis, ODEs, differential relations.'},
    "MATH_CO": {'description': 'Discrete mathematics, graph theory, enumeration, combinatorial optimization.'},
    "MATH_CT": {'description': 'Enriched categories, topoi, abelian categories, monoidal categories, homological algebra.'},
    "MATH_CV": {'description': 'Holomorphic functions, automorphic group actions, and their generalizations, complex geometry.'},
    "MATH_DG": {'description': 'Complex, contact, Riemannian, pseudo-Riemannian, symplectic geometry, relativity, gauge theory.'},
    "MATH_DS": {'description': 'Dynamics of differential equations and flows, mechanics, classical few-body problems.'},
    "MATH_FA": {'description': 'Banach spaces, function spaces, real functions, distributions, measures, integration.'},
    "MATH_GM": {'description': 'Mathematical material of general interest, broadly accessible expositions of research results.'},
    "MATH_GN": {'description': 'Continuum theory, point-set topology, spaces with algebraic structure, topological dynamics.'},
    "MATH_GR": {'description': 'Finite groups, topological groups, representation theory, cohomology, classification.'},
    "MATH_GT": {'description': 'Manifolds, orbifolds, polyhedra, cell complexes, foliations, geometric structures.'},
    "MATH_HO": {'description': 'Biographies, philosophy of mathematics, mathematics education, recreational mathematics.'},
    "MATH_IT": {'description': 'Math methods in information theory and coding theory.'},
    "MATH_KT": {'description': 'Algebraic and topological K-theory, relations with topology, commutative algebra, index theories.'},
    "MATH_LO": {'description': 'Logic, set theory, point-set topology, formal mathematics.'},
    "MATH_MG": {'description': 'Euclidean, hyperbolic, discrete, convex, coarse geometry, comparisons in Riemannian geometry.'},
    "MATH_MP": {'description': 'Articles in which math methods are used to study physics problems, or math questions arising from physics.'},
    "MATH_NA": {'description': 'Numerical algorithms for problems in analysis and algebra, scientific computation.'},
    "MATH_NT": {'description': 'Prime numbers, diophantine equations, analytic number theory, algebraic number theory, arithmetic geometry.'},
    "MATH_OA": {'description': 'Algebras of operators on Hilbert space, C*-algebras, von Neumann algebras, non-commutative geometry.'},
    "MATH_OC": {'description': 'Operations research, linear programming, control theory, systems theory, optimal control.'},
    "MATH_PR": {'description': 'Theory and applications of probability and stochastic processes, including stochastic differential equations.'},
    "MATH_QA": {'description': 'Quantum groups, skein theories, operadic and diagrammatic algebra, quantum field theory.'},
    "MATH_RA": {'description': 'Non-commutative rings and algebras, non-associative algebras, universal algebra.'},
    "MATH_RT": {'description': 'Linear representations of algebras and groups, Lie theory, associative algebras.'},
    "MATH_SG": {'description': 'Hamiltonian systems, symplectic flows, classical integrable systems.'},
    "MATH_SP": {'description': 'Schrodinger operators, differential operators, spectral measures, scattering theory.'},
    "MATH_ST": {'description': 'Applied, computational and theoretical statistics including probability, coverage, learning theory.'},
    "ASTRO_PH_CO": {'description': 'Phenomenology of early universe, cosmic microwave background, cosmological parameters, primordial element abundances.'},
    "ASTRO_PH_EP": {'description': 'Interplanetary medium, planetary physics, terrestrial planets, extrasolar planets, irregular satellites.'},
    "ASTRO_PH_GA": {'description': 'Phenomena pertaining to galaxies or combinations of galaxies, interstellar medium, star clusters.'},
    "ASTRO_PH_HE": {'description': 'Cosmic ray production, gamma rays, X-rays, charged particles, supernovae, neutron stars, pulsars.'},
    "ASTRO_PH_IM": {'description': 'Detector and calculation design, space and laboratory observatories, data analysis methods.'},
    "ASTRO_PH_SR": {'description': 'White dwarfs, brown dwarfs, stars, solar system, helioseismology, stellar evolution.'},
    "COND_MAT_DIS_NN": {'description': 'Glasses and spin glasses; random systems; information theory in physics; neural networks.'},
    "COND_MAT_MES_HALL": {'description': 'Quantum dots and wires, nanotubes, graphene, ballistic transport, mesoscale and nanoscale systems.'},
    "COND_MAT_MTRL_SCI": {'description': 'Techniques, synthesis, characterization, structure; mechanical and structural phase transitions.'},
    "COND_MAT_OTHER": {'description': 'Work in condensed matter that does not fit into other cond-mat classifications.'},
    "COND_MAT_QUANT_GAS": {'description': 'Ultracold atomic gases, Bose-Einstein condensation, Feshbach resonances, spinor condensates.'},
    "COND_MAT_SOFT": {'description': 'Membranes, emulsions, gels, foams, nematic phases, polymers, liquid crystals.'},
    "COND_MAT_STAT_MECH": {'description': 'Phase transitions, thermodynamics, field theory, non-equilibrium phenomena, renormalization.'},
    "COND_MAT_STR_EL": {'description': 'Quantum magnetism, non-Fermi liquid, spin liquids, stripe phases, electron-phonon interactions.'},
    "COND_MAT_SUPR_CON": {'description': 'Superconductivity theory, models, phenomenology, experimental results.'},
    "HEP_EX": {'description': 'Results from high-energy/particle physics experiments at accelerators and observatories.'},
    "HEP_LAT": {'description': 'Lattice field theory results with desired precision and algorithmic advances.'},
    "HEP_PH": {'description': 'Theoretical particle physics and its relation to experiment. Covers Standard Model and beyond.'},
    "HEP_TH": {'description': 'Formal aspects of quantum field theory, string theory, quantum gravity.'},
    "GR_QC": {'description': 'General relativity, gravitational physics, cosmological models, relativistic astrophysics.'},
    "MATH_PH": {'description': 'Applications of mathematics to problems in physics and development of mathematical methods for such applications.'},
    "QUANT_PH": {'description': 'Quantum foundations, quantum information, quantum computation, quantum mechanics.'},
    "NLIN_AO": {'description': 'Self-organization, adaptation, and autonomous systems.'},
    "NLIN_CD": {'description': 'Dynamical systems with chaotic behavior, routes to chaos, spectral analysis, Lyapunov exponents.'},
    "NLIN_CG": {'description': 'Cellular automata, lattice Boltzmann, lattice gas automata, signal processing with cellular automata.'},
    "NLIN_PS": {'description': 'Pattern formation, coherent structures, solitons, waves.'},
    "NLIN_SI": {'description': 'Integrable PDEs, integrable ODEs, Painleve analysis, integrable discrete systems.'},
    "NUCL_EX": {'description': 'Experimental results from nuclear physics laboratories, such as heavy-ion collisions.'},
    "NUCL_TH": {'description': 'Theory of nuclear structure and low-energy reactions, including heavy-ion physics.'},
    "PHYSICS_ACC_PH": {'description': 'Accelerator theory and target design, beam physics, secondary beams, photon sources.'},
    "PHYSICS_AO_PH": {'description': 'Atmospheric and oceanic processes, climate dynamics, waves, boundary layer physics.'},
    "PHYSICS_APP_PH": {'description': 'Applications of physics to new technology, medical physics, instrumentation.'},
    "PHYSICS_ATM_CLUS": {'description': 'Binding, structure, and properties of clusters, nanoparticles.'},
    "PHYSICS_ATOM_PH": {'description': 'Atomic and molecular structure, spectra, collisions, and data. Ultrafast physics, molecular physics.'},
    "PHYSICS_BIO_PH": {'description': 'Molecular biophysics, cellular biophysics, single molecule biophysics.'},
    "PHYSICS_CHEM_PH": {'description': 'Experimental, methods, and results in chemical physics and molecular dynamics.'},
    "PHYSICS_CLASS_PH": {'description': 'Newtonian and Lagrangian mechanics, electromagnetism, thermodynamics, special relativity.'},
    "PHYSICS_COMP_PH": {'description': 'All aspects of computational science applied to physics problems.'},
    "PHYSICS_DATA_AN": {'description': 'Methods, software, and results in physics data analysis.'},
    "PHYSICS_ED_PH": {'description': 'Physics teaching and learning research.'},
    "PHYSICS_FLU_DYN": {'description': 'Turbulence, instabilities, incompressible and compressible flows, boundary layers.'},
    "PHYSICS_GEN_PH": {'description': 'General physics that does not fit elsewhere.'},
    "PHYSICS_GEO_PH": {'description': 'Computational and theoretical geophysics including seismology, potential theory.'},
    "PHYSICS_HIST_PH": {'description': 'History and philosophy of all aspects of physics.'},
    "PHYSICS_INS_DET": {'description': 'Instrumentation and detectors for accelerator, astro-, geo-, or particle physics.'},
    "PHYSICS_MED_PH": {'description': 'Radiation therapy, biomedical imaging, health physics.'},
    "PHYSICS_OPTICS": {'description': 'Adaptive optics, polarimetry, quantum optics, ultrafast optics, photonics.'},
    "PHYSICS_PLASM_PH": {'description': 'Fundamental plasma physics, magnetic and inertial confinement, astrophysical plasmas.'},
    "PHYSICS_POP_PH": {'description': 'General physics topics for a broad audience.'},
    "PHYSICS_SOC_PH": {'description': 'Sociophysics, structure and dynamics of societies, opinion dynamics.'},
    "PHYSICS_SPACE_PH": {'description': 'Space plasma physics, magnetospheric physics, solar wind, cosmic rays.'},
    "Q_BIO_BM": {'description': 'DNA, RNA, proteins, lipids, small molecules; molecular structure and dynamics; molecular engineering.'},
    "Q_BIO_CB": {'description': 'Cell-cell signaling, morphogenesis, development; cell division/cycle; immunology.'},
    "Q_BIO_GN": {'description': 'DNA sequencing and assembly; gene finding; genome structure, organization, and regulation.'},
    "Q_BIO_MN": {'description': 'Gene regulation, signal transduction, metabolic networks, kinetics, synthetic biology.'},
    "Q_BIO_NC": {'description': 'Synapse, receptor dynamics, learning, neural coding, neuroinformatics.'},
    "Q_BIO_OT": {'description': 'Work in quantitative biology that does not fit in the other q-bio classifications.'},
    "Q_BIO_PE": {'description': 'Population dynamics, spatio-temporal evolution, migration, phylogeny, biodiversity.'},
    "Q_BIO_QM": {'description': 'Research papers with experimental, numerical, or statistical contributions of value to biologists.'},
    "Q_BIO_SC": {'description': 'Subcellular structures, molecular motors, organelle transport, packaging.'},
    "Q_BIO_TO": {'description': 'Blood flow, biomechanics, tumor growth, tissue morphogenesis.'},
    "Q_FIN_CP": {'description': 'Monte Carlo, PDE, and other numerical methods with applications to quantitative finance.'},
    "Q_FIN_EC": {'description': 'General economics topics with quantitative approaches.'},
    "Q_FIN_GN": {'description': 'General quantitative financial methodologies covering multiple sub-fields.'},
    "Q_FIN_MF": {'description': 'Mathematical and analytical methods in finance, stochastic methods, hedging strategies.'},
    "Q_FIN_PM": {'description': 'Security selection and optimization, capital allocation, investment strategies.'},
    "Q_FIN_PR": {'description': 'Valuation and hedging of financial securities, their derivatives, and structured products.'},
    "Q_FIN_RM": {'description': 'Measurement and management of financial risks in trading, banking, insurance.'},
    "Q_FIN_ST": {'description': 'Statistical, econometric methods applied to financial markets.'},
    "Q_FIN_TR": {'description': 'Market microstructure, algorithmic trading, order book dynamics.'},
    "STAT_AP": {'description': 'Biology, education, epidemiology, engineering, environmental sciences, medical, physical sciences.'},
    "STAT_CO": {'description': 'Algorithms, computational methods, simulation, visualization.'},
    "STAT_ME": {'description': 'Design, surveys, model selection, regression, testing, time series.'},
    "STAT_ML": {'description': 'Covers machine learning papers with a statistical or theoretical grounding.'},
    "STAT_OT": {'description': 'Work in statistics that does not fit into the other stat-* classifications.'},
    "STAT_TH": {'description': 'Asymptotics, Bayesian inference, decision theory, estimation, foundations, inference.'},
}

__all__ = [
    "ArxivCategory",
]