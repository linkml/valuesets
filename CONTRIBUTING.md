# Contributing to valuesets

:+1: First of all: Thank you for taking the time to contribute!

The following is a set of guidelines for contributing to
valuesets. These guidelines are not strict rules.
Use your best judgment, and feel free to propose changes to this document
in a pull request.

## Table Of Contents

* [Code of Conduct](#code-of-conduct)
* [Guidelines for Contributions and Requests](#contributions)
  * [Reporting issues and making requests](#reporting-issues)
  * [Questions and Discussion](#questions-and-discussion)
  * [Adding new elements yourself](#adding-elements)
* [Best Practices](#best-practices)
  * [How to write a great issue](#great-issues)
  * [How to create a great pull/merge request](#great-pulls)

<a id="code-of-conduct"></a>

## Code of Conduct

The valuesets team strives to create a
welcoming environment for editors, users and other contributors.
Please carefully read our [Code of Conduct](CODE_OF_CONDUCT.md).

<a id="contributions"></a>

## Guidelines for Contributions and Requests

<a id="reporting-issues"></a>

### Reporting problems and suggesting changes to with the data model

Please use our [Issue Tracker][issues] for any of the following:

- Reporting problems
- Requesting new schema elements

<a id="questions-and-discussions"></a>

### Questions and Discussions

Please use our [Discussions forum][discussions] to ask general questions or contribute to discussions.

<a id="adding-elements"></a>

### Adding new elements yourself

Please submit a [Pull Request][pulls] to submit a new term for consideration.

#### Adding Ontology Mappings with `meaning:`

When creating or updating enums in this project, you can (and should) link permissible values to ontology terms using the `meaning:` field. This provides semantic grounding and enables interoperability.

**Basic Example:**

```yaml
enums:
  AirPollutantEnum:
    description: Common air pollutants
    permissible_values:
      OZONE:
        description: Ground-level ozone (O3)
        meaning: CHEBI:25812
      NITROGEN_DIOXIDE:
        description: Nitrogen dioxide (NO2)
        meaning: CHEBI:33101
        title: nitrogen dioxide
```

**Best Practices:**

1. **Always verify ontology IDs** - Never guess CURIEs. Use [OLS (Ontology Lookup Service)](https://www.ebi.ac.uk/ols4/) to search and verify correct ontology term IDs
2. **Use standard OBO prefixes** - Prefer OBO Foundry ontologies (CHEBI, ENVO, NCIT, etc.) when available
3. **Use ROR for organizations** - For research organizations and institutions, use [ROR (Research Organization Registry)](https://ror.org/) identifiers (e.g., `meaning: ROR:05gvnxz63`)
4. **Include `title:` when labels differ** - If the ontology label differs from your enum value name, add a `title:` field with the exact ontology label
5. **One mapping per value** - Use `meaning:` for the primary ontology mapping (not `meanings:` plural)
6. **Declare prefixes in header** - Ensure the prefix is declared in the schema's `prefixes:` section:

```yaml
prefixes:
  CHEBI: http://purl.obolibrary.org/obo/CHEBI_
  ENVO: http://purl.obolibrary.org/obo/ENVO_
```

#### Ontology Validation System

This project uses a two-tier validation system for ontology mappings:

**1. OAK Configuration (`src/valuesets/validators/oak_config.yaml`)**

This file maps ontology prefixes to [OAK (Ontology Access Kit)](https://github.com/INCATools/ontology-access-kit) adapters. Prefixes listed here undergo **strict validation**:

```yaml
ontology_adapters:
  # Configured ontologies (strict validation)
  CHEBI: sqlite:obo:chebi
  ENVO: sqlite:obo:envo
  NCIT: sqlite:obo:ncit

  # Unconfigured ontologies (lenient validation)
  SOME_CUSTOM_PREFIX:   # Empty value = skip validation
```

- **Configured prefixes** (with adapter string): Missing or mismatched labels are treated as **ERRORS**
- **Unconfigured prefixes** (empty or not listed): Issues are reported as **INFO** only
- **Null adapters** (blank value): Validation is skipped entirely for these prefixes

**2. Validation Checks Performed**

When you run `just validate`, the following checks are performed:

1. **Term Existence**: Verifies the ontology term exists and can be retrieved
2. **Label Matching**: Compares the ontology's label against:
   - The permissible value name
   - The `title:` field (if present)
   - Any `aliases:` (if present)
   - Normalized versions of all the above (case-insensitive, punctuation-removed)
3. **Caching**: Valid terms are cached locally in `cache/<prefix>/terms.csv` for performance

**Example Validation Output:**

```
✅ PASS: AirPollutantEnum.OZONE → CHEBI:25812 (ozone)
❌ ERROR: AirPollutantEnum.PM25 → ENVO:99999999 (Could not retrieve label for configured ontology term)
⚠️  WARNING: CustomEnum.VALUE → CUSTOM:12345 (Label mismatch: expected 'VALUE', got 'Custom Value')
ℹ️  INFO: CustomEnum.OTHER → UNKNOWN:99999 (Could not retrieve label for UNKNOWN:99999)
```

**3. Running Validation**

```bash
# Validate all schemas
just validate

# Validate a specific schema file
just validate-schema src/valuesets/schema/environmental_health/exposures.yaml

# Validate using OLS web service (slower, no caching)
just validate-ols

# Strict mode (treat all warnings as errors)
just validate --strict
```

**4. REST API Adapters for Non-OAK Sources**

Some organization registries and identifier systems are not available through OAK but provide REST APIs. This project supports pluggable REST adapters that integrate seamlessly with the validation framework.

**Currently Supported REST APIs:**

- **ROR (Research Organization Registry)**: Use `ROR:` prefix for research organizations
  - API: https://api.ror.org/v2/organizations
  - Example: `meaning: ROR:05gvnxz63` (Argonne National Laboratory)
  - Format: 9-character base32 identifier (e.g., `05gvnxz63`)

**Configuration in `oak_config.yaml`:**

```yaml
ontology_adapters:
  # Standard OAK adapters
  CHEBI: sqlite:obo:chebi
  ENVO: sqlite:obo:envo

  # REST API adapters
  ROR: "rest:ror:"
```

**How It Works:**

1. When the validator encounters a `ROR:` prefix, it checks `oak_config.yaml`
2. The `"rest:ror:"` adapter string triggers the REST adapter factory
3. The `RORAdapter` makes API calls to validate organization names
4. Results are cached in memory using `@lru_cache` for performance
5. Validation follows the same strict/lenient rules as OAK adapters

**Adding New REST Adapters:**

To add support for a new REST API (e.g., Wikidata):

1. Create a new adapter class in `src/valuesets/validators/rest_adapters.py`:

```python
class WikidataAdapter(BaseRestAdapter):
    """Adapter for Wikidata entities."""

    def label(self, curie: str) -> Optional[str]:
        """Get label from Wikidata API."""
        # Implement API logic here
        ...
```

2. Register it in the `get_rest_adapter()` factory:

```python
adapters = {
    'ror': RORAdapter,
    'wikidata': WikidataAdapter,  # Add here
}
```

3. Configure in `oak_config.yaml`:

```yaml
WD: "rest:wikidata:"
```

**Benefits of This Architecture:**

- **Pluggable**: Easy to add new REST APIs without modifying core validation logic
- **Consistent**: REST adapters implement the same interface as OAK adapters
- **No Ad-hoc Scripts**: Everything runs through the standard validation workflow
- **Cached**: API calls are cached to minimize network requests
- **Transparent**: Users don't need to know which adapter is being used

**Example Usage:**

```yaml
# In your schema
enums:
  USDOENationalLaboratoryEnum:
    permissible_values:
      ARGONNE_NATIONAL_LABORATORY:
        title: Argonne National Laboratory
        meaning: ROR:05gvnxz63  # Validated via ROR API
```

```bash
# Validation automatically uses appropriate adapter
just validate
# ✅ ARGONNE_NATIONAL_LABORATORY → ROR:05gvnxz63 (Argonne National Laboratory)
```

#### Term Caching System

This project uses an ontology term caching system to improve validation performance and reduce external API calls. When you contribute new ontology mappings:

1. **Cache Updates**: Adding new ontology mappings may result in changes to the cache files in the `cache/` directory
2. **Include Cache Changes**: These cache updates should be included in your Pull Request
3. **Validation Process**: Run `just validate` before submitting to ensure all ontology mappings are valid
4. **Cache Structure**: The cache organizes terms by ontology prefix (e.g., `cache/ncit/`, `cache/vo/`) for efficient lookup

**Standard Operating Procedure for Contributors:**

- When adding enums with `meaning:` annotations pointing to ontology terms:
  - Run validation locally with `just validate`
  - Include any generated cache files in your commit
  - Ensure all ontology IDs are correct (never guess - use [OLS](https://www.ebi.ac.uk/ols4/) to verify)
  - Follow the project's naming conventions (e.g., `UPPER_CASE` for enum values)
  - Fix any validation errors before submitting your PR
  - If adding a new ontology prefix, consider adding it to `src/valuesets/validators/oak_config.yaml`

<a id="best-practices"></a>

## Best Practices

<a id="great-issues"></a>

### GitHub Best Practice

- Creating and curating issues
    - Read ["About Issues"][[about-issues]]
    - Issues should be focused and actionable
    - Complex issues should be broken down into simpler issues where possible
- Pull Requests
    - Read ["About Pull Requests"][about-pulls]
    - Read [GitHub Pull Requests: 10 Tips to Know](https://blog.mergify.com/github-pull-requests-10-tips-to-know/)
    - Pull Requests (PRs) should be atomic and aim to close a single issue
    - Long running PRs should be avoided where possible
    - PRs should reference issues following standard conventions (e.g. “fixes #123”)
    - Schema developers should always be working on a single issue at any one time
    - Never work on the main branch, always work on an issue/feature branch
    - Core developers can work on branches off origin rather than forks
    - Always create a PR on a branch to maximize transparency of what you are doing
    - PRs should be reviewed and merged in a timely fashion by the valuesets technical leads
    - PRs that do not pass GitHub actions should never be merged
    - In the case of git conflicts, the contributor should try and resolve the conflict
    - If a PR fails a GitHub action check, the contributor should try and resolve the issue in a timely fashion

### Understanding LinkML

Core developers should read the material on the [LinkML site](https://linkml.io/linkml), in particular:

- [Overview](https://linkml.io/linkml/intro/overview.html)
- [Tutorial](https://linkml.io/linkml/intro/tutorial.html)
- [Schemas](https://linkml.io/linkml/schemas/index.html)
- [FAQ](https://linkml.io/linkml/faq/index.html)

### Modeling Best Practice

- Follow Naming conventions
    - Standard LinkML naming conventions should be followed (UpperCamelCase for classes and enums, snake_case for slots)
    - Know how to use the LinkML linter to check style and conventions
    - The names for classes should be nouns or noun-phrases: Person, GenomeAnnotation, Address, Sample
    - Spell out abbreviations and short forms, except where this goes against convention (e.g. do not spell out DNA)
    - Elements that are imported from outside (e.g. schema.org) need not follow the same naming conventions
    - Multivalued slots should be named as plurals
- Document model elements
    - All model elements should have documentation (descriptions) and other textual annotations (e.g. comments, notes)
    - Textual annotations on classes, slots and enumerations should be written with minimal jargon, clear grammar and no misspellings
- Include examples and counter-examples (intentionally invalid examples)
    - Rationale: these serve as documentation and unit tests
    - These will be used by the automated test suite
    - All elements of the schema must be illustrated with valid and invalid data examples in src/data. New schema elements will not be merged into the main branch until examples are provided
    - Invalid example data files should be invalid for one single reason, which should be reflected in the filename. It should be possible to render the invalid example files valid by addressing that single fault.
- Use enums for categorical values
    - Rationale: Open-ended string ranges encourage multiple values to represent the same entity, like “water”, “H2O” and “HOH”
    - Any slot whose values could be constrained to a finite set should use an Enum
    - Non-categorical values, e.g. descriptive fields like `name` or `description` fall outside of this.
- Reuse
    - Existing scheme elements should be reused where appropriate, rather than making duplicative elements
    - More specific classes can be created by refinining classes using inheritance (`is_a`)

[about-branches]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches
[about-issues]: https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues
[about-pulls]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
[issues]: https://github.com/linkml/valuesets/issues/
[pulls]: https://github.com/linkml/valuesets/pulls/

We recommend also reading [GitHub Pull Requests: 10 Tips to Know](https://blog.mergify.com/github-pull-requests-10-tips-to-know/)
