"""
Statistical Test Value Sets

Value sets for statistical hypothesis tests and closely related concepts, including t-tests, ANOVA, non-parametric tests, normality and homoscedasticity tests, post-hoc multiple comparison procedures, multiple testing correction methods, correlation coefficients, and test tailedness. Terms are mapped to STATO (the Statistical Methods Ontology) where possible, falling back to OBI and NCIT.

Generated from: statistics/statistical_tests.yaml
"""

from __future__ import annotations

from valuesets.generators.rich_enum import RichEnum

class StatisticalTestEnum(RichEnum):
    """
    Statistical hypothesis tests, drawn primarily from the descendants of 'statistical hypothesis test' (OBI:0000673) in STATO.
    This enum deliberately mixes abstraction levels: alongside concrete tests it retains STATO's grouping classes (GOODNESS_OF_FIT_TEST, HOMOSKEDASTICITY_TEST, SPHERICITY_TEST, POST_HOC_ANALYSIS, NON_PARAMETRIC_TEST and similar) so that a source reporting only "a test of normality was applied" can still be annotated. Prefer the most specific value that the source supports, and use a grouping value only when the specific test is genuinely not stated.
    Several values are also repeated in the narrower enums below (TTestTypeEnum, NormalityTestEnum, HomoscedasticityTestEnum, PostHocTestEnum), which exist to constrain slot ranges. The duplicated meanings are intentional; from_meaning() resolves per enum class.
    """
    # Enum members
    STUDENTS_T_TEST = "STUDENTS_T_TEST"
    ONE_SAMPLE_T_TEST = "ONE_SAMPLE_T_TEST"
    PAIRED_T_TEST = "PAIRED_T_TEST"
    TWO_SAMPLE_T_TEST_EQUAL_VARIANCE = "TWO_SAMPLE_T_TEST_EQUAL_VARIANCE"
    TWO_SAMPLE_T_TEST_UNEQUAL_VARIANCE = "TWO_SAMPLE_T_TEST_UNEQUAL_VARIANCE"
    YUEN_T_TEST = "YUEN_T_TEST"
    Z_TEST = "Z_TEST"
    ONE_SAMPLE_HOTELLING_T2_TEST = "ONE_SAMPLE_HOTELLING_T2_TEST"
    TWO_SAMPLE_HOTELLING_T2_TEST = "TWO_SAMPLE_HOTELLING_T2_TEST"
    ANOVA = "ANOVA"
    ONE_WAY_ANOVA = "ONE_WAY_ANOVA"
    TWO_WAY_ANOVA = "TWO_WAY_ANOVA"
    MULTIWAY_ANOVA = "MULTIWAY_ANOVA"
    REPEATED_MEASURES_ANOVA = "REPEATED_MEASURES_ANOVA"
    MANOVA = "MANOVA"
    ANCOVA = "ANCOVA"
    F_TEST = "F_TEST"
    MANN_WHITNEY_U_TEST = "MANN_WHITNEY_U_TEST"
    WILCOXON_SIGNED_RANK_TEST = "WILCOXON_SIGNED_RANK_TEST"
    KRUSKAL_WALLIS_TEST = "KRUSKAL_WALLIS_TEST"
    FRIEDMAN_TEST = "FRIEDMAN_TEST"
    SIGN_TEST = "SIGN_TEST"
    CHI_SQUARE_TEST = "CHI_SQUARE_TEST"
    PEARSON_CHI_SQUARE_TEST_OF_INDEPENDENCE = "PEARSON_CHI_SQUARE_TEST_OF_INDEPENDENCE"
    PEARSON_CHI_SQUARE_GOODNESS_OF_FIT_TEST = "PEARSON_CHI_SQUARE_GOODNESS_OF_FIT_TEST"
    YATES_CORRECTED_CHI_SQUARE_TEST = "YATES_CORRECTED_CHI_SQUARE_TEST"
    CHI_SQUARE_TEST_FOR_HOMOGENEITY = "CHI_SQUARE_TEST_FOR_HOMOGENEITY"
    FISHERS_EXACT_TEST = "FISHERS_EXACT_TEST"
    BARNARDS_TEST = "BARNARDS_TEST"
    MCNEMAR_TEST = "MCNEMAR_TEST"
    COCHRANS_Q_TEST = "COCHRANS_Q_TEST"
    COCHRAN_ARMITAGE_TEST_FOR_TREND = "COCHRAN_ARMITAGE_TEST_FOR_TREND"
    COCHRAN_MANTEL_HAENSZEL_TEST = "COCHRAN_MANTEL_HAENSZEL_TEST"
    EXACT_BINOMIAL_TEST = "EXACT_BINOMIAL_TEST"
    HYPERGEOMETRIC_TEST = "HYPERGEOMETRIC_TEST"
    TEST_OF_ASSOCIATION_BETWEEN_CATEGORICAL_VARIABLES = "TEST_OF_ASSOCIATION_BETWEEN_CATEGORICAL_VARIABLES"
    GOODNESS_OF_FIT_TEST = "GOODNESS_OF_FIT_TEST"
    SHAPIRO_WILK_TEST = "SHAPIRO_WILK_TEST"
    KOLMOGOROV_SMIRNOV_TEST = "KOLMOGOROV_SMIRNOV_TEST"
    ANDERSON_DARLING_TEST = "ANDERSON_DARLING_TEST"
    HOSMER_LEMESHOW_TEST = "HOSMER_LEMESHOW_TEST"
    LEVENES_TEST = "LEVENES_TEST"
    BARTLETTS_TEST = "BARTLETTS_TEST"
    BROWN_FORSYTHE_TEST = "BROWN_FORSYTHE_TEST"
    BREUSCH_PAGAN_TEST = "BREUSCH_PAGAN_TEST"
    HOMOSKEDASTICITY_TEST = "HOMOSKEDASTICITY_TEST"
    HOMOGENEITY_TEST = "HOMOGENEITY_TEST"
    SPHERICITY_TEST = "SPHERICITY_TEST"
    MAUCHLYS_TEST = "MAUCHLYS_TEST"
    ODDS_RATIO_HOMOGENEITY_TEST = "ODDS_RATIO_HOMOGENEITY_TEST"
    BRESLOW_DAY_TEST = "BRESLOW_DAY_TEST"
    TARONES_TEST = "TARONES_TEST"
    WOOLFS_TEST = "WOOLFS_TEST"
    POST_HOC_ANALYSIS = "POST_HOC_ANALYSIS"
    TUKEY_HSD_TEST = "TUKEY_HSD_TEST"
    NEWMAN_KEULS_TEST = "NEWMAN_KEULS_TEST"
    SCHEFFE_TEST = "SCHEFFE_TEST"
    LEAST_SIGNIFICANT_DIFFERENCE_TEST = "LEAST_SIGNIFICANT_DIFFERENCE_TEST"
    DUNNS_TEST = "DUNNS_TEST"
    CONOVER_IMAN_TEST = "CONOVER_IMAN_TEST"
    GRUBBS_TEST = "GRUBBS_TEST"
    DIXON_Q_TEST = "DIXON_Q_TEST"
    TIETJEN_MOORE_TEST = "TIETJEN_MOORE_TEST"
    GENERALIZED_ESD_TEST = "GENERALIZED_ESD_TEST"
    LIKELIHOOD_RATIO_TEST = "LIKELIHOOD_RATIO_TEST"
    WALD_TEST = "WALD_TEST"
    LOG_RANK_TEST = "LOG_RANK_TEST"
    HARDY_WEINBERG_EQUILIBRIUM_TEST = "HARDY_WEINBERG_EQUILIBRIUM_TEST"
    TRANSMISSION_DISEQUILIBRIUM_TEST = "TRANSMISSION_DISEQUILIBRIUM_TEST"
    PEARSON_CORRELATION_TEST = "PEARSON_CORRELATION_TEST"
    SPEARMAN_CORRELATION_TEST = "SPEARMAN_CORRELATION_TEST"
    AB_TEST = "AB_TEST"
    BETWEEN_GROUP_COMPARISON_TEST = "BETWEEN_GROUP_COMPARISON_TEST"
    WITHIN_SUBJECT_COMPARISON_TEST = "WITHIN_SUBJECT_COMPARISON_TEST"
    NON_PARAMETRIC_TEST = "NON_PARAMETRIC_TEST"

# Set metadata after class creation
StatisticalTestEnum._metadata = {
    "STUDENTS_T_TEST": {'description': "Test in which the test statistic follows a Student's t distribution under the null hypothesis; used when the population is assumed normal but the sample is small", 'meaning': 'OBI:0000739', 'aliases': ['t-test', 't-Test']},
    "ONE_SAMPLE_T_TEST": {'description': "Student's t-test comparing a sample mean against a specified population mean", 'meaning': 'STATO:0000302'},
    "PAIRED_T_TEST": {'description': "Student's t-test for differences between paired observations, as in a repeated measures design with two measurements per subject", 'meaning': 'STATO:0000095'},
    "TWO_SAMPLE_T_TEST_EQUAL_VARIANCE": {'description': 'Two-sample t-test comparing the means of two independent samples assumed to have equal variances', 'meaning': 'STATO:0000303', 'annotations': {'note': 'The bare terms "unpaired t-test" and "independent samples t-test" are ambiguous: they are attached here because this is the classical equal-variance form, but common software defaults to the Welch variant (R\'s t.test, scipy.stats.ttest_ind with equal_var=False). Choose TWO_SAMPLE_T_TEST_UNEQUAL_VARIANCE when the source did not assume equal variances.'}, 'aliases': ['independent samples t-test', 'unpaired t-test']},
    "TWO_SAMPLE_T_TEST_UNEQUAL_VARIANCE": {'description': 'Two-sample t-test used when the variances of the two populations are not assumed equal', 'meaning': 'STATO:0000304', 'annotations': {'note': 'This is the default two-sample t-test in R and SciPy, so an unqualified "unpaired t-test" in a methods section often means this rather than TWO_SAMPLE_T_TEST_EQUAL_VARIANCE.'}, 'aliases': ["Welch's t-test"]},
    "YUEN_T_TEST": {'description': 'Robust two-sample t-test computed on trimmed means and winsorized variances', 'meaning': 'STATO:0000406'},
    "Z_TEST": {'description': 'Test evaluating the null hypothesis that the means of two populations are equal using a normal reference distribution', 'meaning': 'STATO:0000052'},
    "ONE_SAMPLE_HOTELLING_T2_TEST": {'description': 'Multivariate extension of the one-sample t-test comparing a vector of means against a reference vector', 'meaning': 'STATO:0000153'},
    "TWO_SAMPLE_HOTELLING_T2_TEST": {'description': 'Multivariate generalization of the two-sample t-test comparing mean vectors of two populations', 'meaning': 'STATO:0000098'},
    "ANOVA": {'description': 'Analysis of variance testing whether the means of several groups are equal', 'meaning': 'OBI:0200201', 'aliases': ['analysis of variance']},
    "ONE_WAY_ANOVA": {'description': 'Analysis of variance in which the groups compared correspond to the levels of a single independent variable', 'meaning': 'STATO:0000044'},
    "TWO_WAY_ANOVA": {'description': 'Analysis of variance in which the groups compared correspond to the levels of exactly two independent variables', 'meaning': 'STATO:0000045'},
    "MULTIWAY_ANOVA": {'description': 'Analysis of variance in which the groups compared correspond to the levels of more than two independent variables', 'meaning': 'STATO:0000048'},
    "REPEATED_MEASURES_ANOVA": {'description': 'Analysis of variance developed for non-independent observations arising from repeated measurements on the same experimental unit', 'meaning': 'STATO:0000260'},
    "MANOVA": {'description': 'Procedure for comparing multivariate sample means when there are two or more dependent variables', 'meaning': 'STATO:0000454'},
    "ANCOVA": {'description': 'Analysis of covariance evaluating whether population means of a dependent variable are equal across levels of a categorical independent variable while controlling for covariates', 'meaning': 'STATO:0000179', 'aliases': ['analysis of covariance']},
    "F_TEST": {'description': 'Test in which the test statistic follows an F-distribution under the null hypothesis', 'meaning': 'STATO:0000086'},
    "MANN_WHITNEY_U_TEST": {'description': 'Non-parametric test comparing two independent groups without assuming normally distributed values', 'meaning': 'STATO:0000076', 'aliases': ['Wilcoxon rank sum test', 'Mann-Whitney Test']},
    "WILCOXON_SIGNED_RANK_TEST": {'description': 'Non-parametric test of the null hypothesis that the median difference between paired observations is zero', 'meaning': 'STATO:0000092'},
    "KRUSKAL_WALLIS_TEST": {'description': 'Non-parametric test comparing two or more groups without assuming normally distributed values', 'meaning': 'STATO:0000094', 'aliases': ['Kruskal-Wallis Test']},
    "FRIEDMAN_TEST": {'description': 'Non-parametric test for differences among multiple related groups; extension of the Wilcoxon signed-rank test to more than two conditions', 'meaning': 'STATO:0000641'},
    "SIGN_TEST": {'description': 'Non-parametric test assessing whether the median of a population equals a specified value', 'meaning': 'STATO:0000644'},
    "CHI_SQUARE_TEST": {'description': 'Test in which the sampling distribution of the test statistic is a chi-square distribution under the null hypothesis', 'meaning': 'OBI:0200200'},
    "PEARSON_CHI_SQUARE_TEST_OF_INDEPENDENCE": {'description': 'Chi-square test of the independence of two categorical variables in a contingency table', 'meaning': 'STATO:0000081'},
    "PEARSON_CHI_SQUARE_GOODNESS_OF_FIT_TEST": {'description': 'Chi-square test evaluating the goodness of fit of observed counts to an expected distribution', 'meaning': 'STATO:0000309'},
    "YATES_CORRECTED_CHI_SQUARE_TEST": {'description': 'Chi-square test of association between two dichotomous variables with a continuity correction', 'meaning': 'STATO:0000070', 'aliases': ["Yates' chi-squared test"]},
    "CHI_SQUARE_TEST_FOR_HOMOGENEITY": {'description': 'Test comparing proportions observed across multiple groups using contingency table frequencies', 'meaning': 'STATO:0000701'},
    "FISHERS_EXACT_TEST": {'description': 'Exact test for non-random association between two categorical variables', 'meaning': 'STATO:0000073'},
    "BARNARDS_TEST": {'description': "Exact unconditional test of association between two categorical variables, often more powerful than Fisher's exact test", 'meaning': 'STATO:0000310'},
    "MCNEMAR_TEST": {'description': 'Test applied to 2 x 2 contingency tables of paired nominal data to compare marginal frequencies', 'meaning': 'STATO:0000433'},
    "COCHRANS_Q_TEST": {'description': 'Test for unreplicated randomized block designs with a binary response and paired data', 'meaning': 'STATO:0000434'},
    "COCHRAN_ARMITAGE_TEST_FOR_TREND": {'description': 'Test for association between a dichotomous variable and an ordered categorical variable', 'meaning': 'STATO:0000148'},
    "COCHRAN_MANTEL_HAENSZEL_TEST": {'description': 'Test of independence between two categorical variables stratified by a third variable', 'meaning': 'STATO:0000074', 'aliases': ['Cochran-Mantel-Haenszel test']},
    "EXACT_BINOMIAL_TEST": {'description': 'Test of the statistical significance of deviations from a theoretically expected distribution of observations into two categories', 'meaning': 'STATO:0000298', 'aliases': ['binomial test']},
    "HYPERGEOMETRIC_TEST": {'description': 'Test evaluating whether a random variable follows a hypergeometric distribution; widely used for over-representation analysis', 'meaning': 'STATO:0000285', 'aliases': ['over-representation test']},
    "TEST_OF_ASSOCIATION_BETWEEN_CATEGORICAL_VARIABLES": {'description': 'Test evaluating whether a discrete predictor variable is associated with a discrete response variable', 'meaning': 'STATO:0000027'},
    "GOODNESS_OF_FIT_TEST": {'description': 'Test evaluating whether a sample distribution can be considered equivalent to a theoretical distribution', 'meaning': 'STATO:0000191'},
    "SHAPIRO_WILK_TEST": {'description': 'Goodness of fit test of the null hypothesis that a sample is drawn from a normally distributed population', 'meaning': 'STATO:0000077'},
    "KOLMOGOROV_SMIRNOV_TEST": {'description': 'Goodness of fit test of the null hypothesis that a sample is drawn from a specified continuous probability distribution', 'meaning': 'STATO:0000083'},
    "ANDERSON_DARLING_TEST": {'description': 'Goodness of fit test of whether a sample is drawn from a given probability distribution, weighting the tails more heavily', 'meaning': 'STATO:0000042'},
    "HOSMER_LEMESHOW_TEST": {'description': 'Goodness of fit test for logistic regression models comparing predicted probabilities against observed outcomes', 'meaning': 'STATO:0000653'},
    "LEVENES_TEST": {'description': 'Test of the null hypothesis of equality of variance across several populations', 'meaning': 'STATO:0000078'},
    "BARTLETTS_TEST": {'description': 'Test of whether k samples are drawn from populations with equal variances; sensitive to departures from normality', 'meaning': 'STATO:0000079', 'aliases': ["Bartlett's test"]},
    "BROWN_FORSYTHE_TEST": {'description': 'Test of equality of group variances based on deviations from the group medians', 'meaning': 'STATO:0000080'},
    "BREUSCH_PAGAN_TEST": {'description': 'Score test of the hypothesis of constant error variance against the alternative that error variance depends on the fitted values', 'meaning': 'STATO:0000284'},
    "HOMOSKEDASTICITY_TEST": {'description': 'Test evaluating whether variances from several random samples are similar', 'meaning': 'STATO:0000137', 'aliases': ['homoscedasticity test']},
    "HOMOGENEITY_TEST": {'description': 'Test evaluating whether a statistical measure computed from several random samples is similar', 'meaning': 'STATO:0000697'},
    "SPHERICITY_TEST": {'description': 'Test of the null hypothesis of equality of the variances of differences between levels of a repeated measures factor', 'meaning': 'STATO:0000131'},
    "MAUCHLYS_TEST": {'description': 'Test of sphericity in the context of repeated measures analysis of variance', 'meaning': 'STATO:0000199'},
    "ODDS_RATIO_HOMOGENEITY_TEST": {'description': 'Test of the null hypothesis that odds ratios are consistent across strata of a population', 'meaning': 'STATO:0000247'},
    "BRESLOW_DAY_TEST": {'description': 'Test of whether odds ratios are homogeneous across several 2x2 contingency tables', 'meaning': 'STATO:0000130'},
    "TARONES_TEST": {'description': 'Test of the null hypothesis that odds ratios are homogeneous across strata', 'meaning': 'STATO:0000136'},
    "WOOLFS_TEST": {'description': 'Test of the null hypothesis that odds ratios are the same across all strata of the population under investigation', 'meaning': 'STATO:0000246'},
    "POST_HOC_ANALYSIS": {'description': 'Test carried out following an analysis of variance that rejected the null hypothesis, to identify which groups differ', 'meaning': 'STATO:0000133'},
    "TUKEY_HSD_TEST": {'description': 'Post-hoc test following a significant ANOVA that determines which means differ, controlling the family-wise error rate', 'meaning': 'STATO:0000187', 'aliases': ['Tukey honestly significant difference test']},
    "NEWMAN_KEULS_TEST": {'description': 'Stepwise multiple comparison procedure identifying sample means that differ significantly, based on the studentized range statistic', 'meaning': 'STATO:0000261', 'aliases': ['Student-Newman-Keuls test']},
    "SCHEFFE_TEST": {'description': 'Conservative post-hoc procedure evaluating all possible contrasts while adjusting significance levels for multiple comparisons', 'meaning': 'STATO:0000156', 'aliases': ['Scheffé test']},
    "LEAST_SIGNIFICANT_DIFFERENCE_TEST": {'description': 'Post-hoc test for multiple comparisons of treatments by means of the least significant difference following an ANOVA', 'meaning': 'STATO:0000157', 'aliases': ["Fisher's LSD test", 'Least significant difference test']},
    "DUNNS_TEST": {'description': 'Non-parametric post-hoc test run after a Kruskal-Wallis test to identify which groups differ', 'meaning': 'STATO:0000490', 'aliases': ["Dunn's multiple comparison test"]},
    "CONOVER_IMAN_TEST": {'description': 'Post-hoc test for pairwise multiple comparisons using rank sums following a Kruskal-Wallis test', 'meaning': 'STATO:0000491'},
    "GRUBBS_TEST": {'description': 'Test detecting a single outlier in a univariate data set assumed to come from a normally distributed population', 'meaning': 'STATO:0000441'},
    "DIXON_Q_TEST": {'description': 'Test detecting outliers in a univariate data set assumed to come from a normally distributed population', 'meaning': 'STATO:0000440'},
    "TIETJEN_MOORE_TEST": {'description': "Generalization of Grubbs' test allowing detection of more than one outlier", 'meaning': 'STATO:0000442'},
    "GENERALIZED_ESD_TEST": {'description': 'Outlier detection test with a built-in correction for multiple testing', 'meaning': 'STATO:0000443', 'aliases': ['generalized ESD test']},
    "LIKELIHOOD_RATIO_TEST": {'description': 'Test of whether there is evidence for moving from a simple model to a more complex model in which the simple model is nested', 'meaning': 'OBI:0000861'},
    "WALD_TEST": {'description': 'Test evaluating whether one or more model coefficients differ from zero, given their variance-covariance matrix', 'meaning': 'STATO:0000559', 'aliases': ['Wald chi-squared test']},
    "LOG_RANK_TEST": {'description': 'Test comparing the survival distributions of two or more groups', 'meaning': 'STATO:0000640', 'aliases': ['logrank test']},
    "HARDY_WEINBERG_EQUILIBRIUM_TEST": {'description': "Test of whether a population's allele proportions are in Hardy-Weinberg equilibrium, often used as a genotyping quality control", 'meaning': 'STATO:0000181'},
    "TRANSMISSION_DISEQUILIBRIUM_TEST": {'description': 'Test for genetic linkage between a genetic marker and a trait in families, robust to population structure', 'meaning': 'STATO:0000275'},
    "PEARSON_CORRELATION_TEST": {'description': "Test of whether two continuous variables are linearly associated, based on Pearson's correlation coefficient", 'meaning': 'NCIT:C53244'},
    "SPEARMAN_CORRELATION_TEST": {'description': "Non-parametric test of whether two variables are monotonically associated, based on Spearman's rank correlation coefficient", 'meaning': 'NCIT:C53249'},
    "AB_TEST": {'description': 'Statistical testing comparing two types of treatments or interventions', 'meaning': 'STATO:0000715'},
    "BETWEEN_GROUP_COMPARISON_TEST": {'description': 'Test detecting differences between the means computed for each study group population', 'meaning': 'STATO:0000279'},
    "WITHIN_SUBJECT_COMPARISON_TEST": {'description': 'Test evaluating whether a change occurs within one experimental unit over time following a treatment or event', 'meaning': 'STATO:0000202'},
    "NON_PARAMETRIC_TEST": {'description': 'Test making no assumption about the underlying data distribution', 'meaning': 'STATO:0000198'},
}

class TTestTypeEnum(RichEnum):
    """
    Variants of Student's t-test
    """
    # Enum members
    ONE_SAMPLE = "ONE_SAMPLE"
    PAIRED = "PAIRED"
    TWO_SAMPLE_EQUAL_VARIANCE = "TWO_SAMPLE_EQUAL_VARIANCE"
    TWO_SAMPLE_UNEQUAL_VARIANCE = "TWO_SAMPLE_UNEQUAL_VARIANCE"
    TRIMMED_MEANS = "TRIMMED_MEANS"

# Set metadata after class creation
TTestTypeEnum._metadata = {
    "ONE_SAMPLE": {'description': 'Compares a sample mean against a specified population mean', 'meaning': 'STATO:0000302'},
    "PAIRED": {'description': 'Compares paired observations from the same experimental units', 'meaning': 'STATO:0000095'},
    "TWO_SAMPLE_EQUAL_VARIANCE": {'description': 'Compares the means of two independent samples assumed to have equal variances', 'meaning': 'STATO:0000303'},
    "TWO_SAMPLE_UNEQUAL_VARIANCE": {'description': "Compares the means of two independent samples with unequal variances (Welch's t-test)", 'meaning': 'STATO:0000304'},
    "TRIMMED_MEANS": {'description': 'Robust t-test computed on trimmed means and winsorized variances', 'meaning': 'STATO:0000406'},
}

class NormalityTestEnum(RichEnum):
    """
    Goodness of fit tests commonly used to assess whether a sample is drawn from a normally distributed population
    """
    # Enum members
    SHAPIRO_WILK = "SHAPIRO_WILK"
    KOLMOGOROV_SMIRNOV = "KOLMOGOROV_SMIRNOV"
    ANDERSON_DARLING = "ANDERSON_DARLING"

# Set metadata after class creation
NormalityTestEnum._metadata = {
    "SHAPIRO_WILK": {'description': 'Tests the null hypothesis that a sample comes from a normal distribution', 'meaning': 'STATO:0000077'},
    "KOLMOGOROV_SMIRNOV": {'description': 'Tests whether a sample is drawn from a specified continuous probability distribution', 'meaning': 'STATO:0000083'},
    "ANDERSON_DARLING": {'description': 'Tests whether a sample is drawn from a given probability distribution, with added sensitivity in the tails', 'meaning': 'STATO:0000042'},
}

class HomoscedasticityTestEnum(RichEnum):
    """
    Tests evaluating equality of variances across groups or samples
    """
    # Enum members
    LEVENE = "LEVENE"
    BARTLETT = "BARTLETT"
    BROWN_FORSYTHE = "BROWN_FORSYTHE"
    BREUSCH_PAGAN = "BREUSCH_PAGAN"

# Set metadata after class creation
HomoscedasticityTestEnum._metadata = {
    "LEVENE": {'description': 'Tests the null hypothesis of equality of variance in several populations', 'meaning': 'STATO:0000078'},
    "BARTLETT": {'description': 'Tests whether k samples come from populations with equal variances', 'meaning': 'STATO:0000079', 'aliases': ["Bartlett's test"]},
    "BROWN_FORSYTHE": {'description': 'Tests equality of group variances using deviations from group medians', 'meaning': 'STATO:0000080'},
    "BREUSCH_PAGAN": {'description': 'Tests for heteroscedasticity of regression residuals', 'meaning': 'STATO:0000284'},
}

class PostHocTestEnum(RichEnum):
    """
    Multiple comparison procedures carried out after a significant omnibus test such as an ANOVA or Kruskal-Wallis test
    """
    # Enum members
    TUKEY_HSD = "TUKEY_HSD"
    NEWMAN_KEULS = "NEWMAN_KEULS"
    SCHEFFE = "SCHEFFE"
    LEAST_SIGNIFICANT_DIFFERENCE = "LEAST_SIGNIFICANT_DIFFERENCE"
    DUNN = "DUNN"
    CONOVER_IMAN = "CONOVER_IMAN"

# Set metadata after class creation
PostHocTestEnum._metadata = {
    "TUKEY_HSD": {'description': 'Determines which means differ after a significant ANOVA while controlling the family-wise error rate', 'meaning': 'STATO:0000187'},
    "NEWMAN_KEULS": {'description': 'Stepwise multiple comparison procedure based on the studentized range', 'meaning': 'STATO:0000261'},
    "SCHEFFE": {'description': 'Conservative procedure evaluating all possible contrasts', 'meaning': 'STATO:0000156', 'aliases': ['Scheffé test']},
    "LEAST_SIGNIFICANT_DIFFERENCE": {'description': 'Pairwise comparisons using the least significant difference following an ANOVA', 'meaning': 'STATO:0000157', 'aliases': ["Fisher's LSD test", 'Least significant difference test']},
    "DUNN": {'description': 'Non-parametric post-hoc test following a Kruskal-Wallis test', 'meaning': 'STATO:0000490'},
    "CONOVER_IMAN": {'description': 'Pairwise rank-sum comparisons following a Kruskal-Wallis test', 'meaning': 'STATO:0000491'},
}

class MultipleTestingCorrectionEnum(RichEnum):
    """
    Methods for adjusting p-values or significance thresholds when many hypotheses are tested simultaneously.
    As with StatisticalTestEnum, concrete methods (BONFERRONI, HOLM_BONFERRONI, BENJAMINI_HOCHBERG) sit alongside the error-rate classes they belong to (FAMILY_WISE_ERROR_RATE, FALSE_DISCOVERY_RATE) and procedural classes (SIMULTANEOUS, SEQUENTIAL). The classes are intended for sources that report only "FDR-corrected" without naming a procedure.
    """
    # Enum members
    BONFERRONI = "BONFERRONI"
    HOLM_BONFERRONI = "HOLM_BONFERRONI"
    BENJAMINI_HOCHBERG = "BENJAMINI_HOCHBERG"
    BENJAMINI_YEKUTIELI = "BENJAMINI_YEKUTIELI"
    HOLM_FDR = "HOLM_FDR"
    HOMMEL_FDR = "HOMMEL_FDR"
    FAMILY_WISE_ERROR_RATE = "FAMILY_WISE_ERROR_RATE"
    FALSE_DISCOVERY_RATE = "FALSE_DISCOVERY_RATE"
    SIMULTANEOUS = "SIMULTANEOUS"
    SEQUENTIAL = "SEQUENTIAL"
    ALPHA_SPENDING = "ALPHA_SPENDING"
    ALPHA_INVESTING = "ALPHA_INVESTING"
    NONE = "NONE"

# Set metadata after class creation
MultipleTestingCorrectionEnum._metadata = {
    "BONFERRONI": {'description': 'Divides the desired family-wise significance level by the number of comparisons made', 'meaning': 'NCIT:C61594', 'aliases': ['Bonferroni correction']},
    "HOLM_BONFERRONI": {'description': 'Sequentially rejective closed-test procedure controlling the family-wise error rate', 'meaning': 'OBI:0200066', 'aliases': ['Holm correction']},
    "BENJAMINI_HOCHBERG": {'description': 'Sequential p-value procedure controlling the false discovery rate under independence or positive dependence', 'meaning': 'OBI:0200036', 'aliases': ['BH', 'BH-FDR']},
    "BENJAMINI_YEKUTIELI": {'description': 'False discovery rate procedure valid under arbitrary dependence between tests', 'meaning': 'OBI:0200049', 'aliases': ['BY']},
    "HOLM_FDR": {'description': 'Application of the Holm p-value procedure to correct false discovery rate. Note that Holm\'s step-down procedure controls the family-wise error rate, not the false discovery rate; the "false discovery rate" wording is STATO\'s own label for this term. Prefer HOLM_BONFERRONI unless you specifically need the STATO term.', 'meaning': 'STATO:0000551'},
    "HOMMEL_FDR": {'description': 'Application of the Hommel p-value procedure to correct false discovery rate', 'meaning': 'STATO:0000552'},
    "FAMILY_WISE_ERROR_RATE": {'description': 'Procedure controlling the probability of making at least one false positive across a family of tests', 'meaning': 'OBI:0200073', 'aliases': ['FWER correction']},
    "FALSE_DISCOVERY_RATE": {'description': 'Procedure controlling the expected proportion of false positives among rejected hypotheses', 'meaning': 'OBI:0200163'},
    "SIMULTANEOUS": {'description': 'Correction method applying a single adjustment across all tests simultaneously', 'meaning': 'STATO:0000601'},
    "SEQUENTIAL": {'description': 'Correction method applying adjustments in a stepwise, ordered fashion', 'meaning': 'STATO:0000602'},
    "ALPHA_SPENDING": {'description': 'Sequential procedure allocating portions of the overall type I error rate across interim analyses', 'meaning': 'STATO:0000605'},
    "ALPHA_INVESTING": {'description': 'Sequential procedure that earns and spends alpha as hypotheses are tested', 'meaning': 'STATO:0000604'},
    "NONE": {'description': 'No adjustment made for multiple testing', 'annotations': {'note': 'No appropriate ontology term found for absence of correction'}},
}

class CorrelationCoefficientEnum(RichEnum):
    """
    Coefficients quantifying the strength of association between two variables
    """
    # Enum members
    PEARSON = "PEARSON"
    SPEARMAN = "SPEARMAN"
    KENDALL = "KENDALL"

# Set metadata after class creation
CorrelationCoefficientEnum._metadata = {
    "PEARSON": {'description': 'Evaluates the strength of linear association between two continuous variables', 'meaning': 'STATO:0000280', 'aliases': ["Pearson's r"]},
    "SPEARMAN": {'description': 'Non-parametric measure of statistical dependence between two ranked variables', 'meaning': 'STATO:0000201', 'aliases': ["Spearman's rho"]},
    "KENDALL": {'description': 'Correlation coefficient between two ordinal or ranked variables', 'meaning': 'STATO:0000240', 'aliases': ["Kendall's tau"]},
}

class TestTailednessEnum(RichEnum):
    """
    Whether a statistical test allocates the significance level to one or both tails of the reference distribution
    """
    # Enum members
    ONE_TAILED = "ONE_TAILED"
    TWO_TAILED = "TWO_TAILED"

# Set metadata after class creation
TestTailednessEnum._metadata = {
    "ONE_TAILED": {'description': 'Allocates all of the significance level to one tail, evaluating a directional alternative hypothesis', 'meaning': 'STATO:0000286', 'aliases': ['one-sided test']},
    "TWO_TAILED": {'description': 'Allocates half of the significance level to each tail, evaluating a non-directional alternative hypothesis', 'meaning': 'STATO:0000287', 'aliases': ['two-sided test']},
}

class DistributionalAssumptionEnum(RichEnum):
    """
    Whether an inference procedure assumes a parametric form for the underlying population distribution.
    Note the deliberate type approximation: the values denote a property of a procedure, but the available ontology terms (NCIT:C53230, STATO:0000198) denote classes of test. Neither PATO nor OBI currently has a quality or characteristic term for "parametric", so the test classes are used as the closest available referent.
    """
    # Enum members
    PARAMETRIC = "PARAMETRIC"
    NON_PARAMETRIC = "NON_PARAMETRIC"

# Set metadata after class creation
DistributionalAssumptionEnum._metadata = {
    "PARAMETRIC": {'description': 'Procedure that incorporates assumptions about the population probability distribution', 'meaning': 'NCIT:C53230'},
    "NON_PARAMETRIC": {'description': 'Procedure that makes no assumption about the underlying data distribution', 'meaning': 'STATO:0000198', 'aliases': ['Non-Parametric Test']},
}

class ComparisonObjectiveEnum(RichEnum):
    """
    The objective of a between-group comparison, particularly in the design of controlled trials
    """
    # Enum members
    SUPERIORITY = "SUPERIORITY"
    NON_INFERIORITY = "NON_INFERIORITY"
    EQUIVALENCE = "EQUIVALENCE"

# Set metadata after class creation
ComparisonObjectiveEnum._metadata = {
    "SUPERIORITY": {'description': 'Comparison intended to show that the difference in effects exceeds a prespecified threshold of meaningful benefit', 'meaning': 'STATO:0000718'},
    "NON_INFERIORITY": {'description': 'Comparison intended to show that any difference in effects lies below a prespecified threshold of meaningful harm', 'meaning': 'STATO:0000716'},
    "EQUIVALENCE": {'description': 'Comparison intended to show that the absolute difference in effects is smaller than a prespecified threshold', 'meaning': 'STATO:0000717'},
}

__all__ = [
    "StatisticalTestEnum",
    "TTestTypeEnum",
    "NormalityTestEnum",
    "HomoscedasticityTestEnum",
    "PostHocTestEnum",
    "MultipleTestingCorrectionEnum",
    "CorrelationCoefficientEnum",
    "TestTailednessEnum",
    "DistributionalAssumptionEnum",
    "ComparisonObjectiveEnum",
]