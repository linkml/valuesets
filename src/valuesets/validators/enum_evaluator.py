"""
Enum evaluator for validating ontology mappings in LinkML schemas.

This module validates that ontology term mappings (meanings) in enum definitions
match the expected labels from the ontology.

Uses OAK (Ontology Access Kit) as the abstraction layer for all ontology access.
"""

import re
import logging
import sys
import os
import warnings
import csv
import yaml
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Dict, Set
from pydantic import BaseModel, Field, ConfigDict
from linkml_runtime.utils.schemaview import SchemaView
from linkml_runtime.linkml_model import EnumDefinition, PermissibleValue

LIMIT = 300

try:
    from oaklib import get_adapter
    HAS_OAK = True
except ImportError:
    HAS_OAK = False

try:
    from .rest_adapters import get_rest_adapter
    HAS_REST_ADAPTERS = True
except ImportError:
    HAS_REST_ADAPTERS = False

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ValidationConfig(BaseModel):
    """Configuration for validation."""
    model_config = ConfigDict(extra="forbid")

    oak_adapter_string: str = Field(
        default="sqlite:obo:",
        description="OAK adapter string (e.g., sqlite:obo:, ols:, bioportal:)"
    )
    strict_mode: bool = Field(
        default=False,
        description="Treat warnings as errors"
    )
    cache_labels: bool = Field(
        default=True,
        description="Cache ontology labels to avoid redundant lookups"
    )
    oak_config_path: Optional[Path] = Field(
        default=None,
        description="Path to OAK configuration YAML file"
    )
    cache_dir: Path = Field(
        default=Path("cache"),
        description="Directory for storing cached terms"
    )


class ValidationIssue(BaseModel):
    """Represents a single validation issue."""
    model_config = ConfigDict(extra="forbid")

    enum_name: str
    value_name: str
    severity: str = Field(pattern="^(ERROR|WARNING|INFO)$")
    message: str
    meaning: Optional[str] = None
    expected_label: Optional[str] = None
    actual_label: Optional[str] = None


class ValidationResult(BaseModel):
    """Results from validating a schema."""
    model_config = ConfigDict(extra="forbid")

    schema_path: Optional[Path] = None
    issues: List[ValidationIssue] = Field(default_factory=list)
    total_enums_checked: int = 0
    total_values_checked: int = 0
    total_mappings_checked: int = 0

    def has_errors(self) -> bool:
        """Check if there are any errors."""
        return any(i.severity == "ERROR" for i in self.issues)

    def has_warnings(self) -> bool:
        """Check if there are any warnings."""
        return any(i.severity == "WARNING" for i in self.issues)

    def print_summary(self):
        """Print a summary of validation results."""
        print(f"\nValidation Summary:")
        print(f"  Enums checked: {self.total_enums_checked}")
        print(f"  Values checked: {self.total_values_checked}")
        print(f"  Mappings checked: {self.total_mappings_checked}")

        errors = [i for i in self.issues if i.severity == "ERROR"]
        warnings = [i for i in self.issues if i.severity == "WARNING"]
        info = [i for i in self.issues if i.severity == "INFO"]

        print(f"  Errors: {len(errors)}")
        print(f"  Warnings: {len(warnings)}")
        print(f"  Info: {len(info)}")


class EnumEvaluator:
    """Evaluator for validating ontology mappings in enums."""

    def __init__(self, config: Optional[ValidationConfig] = None):
        """
        Initialize the evaluator.

        Args:
            config: Validation configuration
        """
        self.config = config or ValidationConfig()
        self._label_cache = {} if self.config.cache_labels else None
        self._per_prefix_adapters = {}  # Cache of per-ontology adapters
        self._oak_config = self._load_oak_config()
        self._prefix_caches = {}  # Initialize here to avoid AttributeError
        self._warned_prefixes = set()  # Track prefixes we've already warned about
        self._initialize_oak()

    def _load_oak_config(self) -> Dict[str, str]:
        """Load OAK configuration from YAML file."""
        config_path = self.config.oak_config_path
        if not config_path:
            # Default to config file next to this module
            config_path = Path(__file__).parent / "oak_config.yaml"

        if not config_path.exists():
            logger.warning(f"OAK config file not found: {config_path}")
            return {}

        try:
            with open(config_path, 'r') as f:
                config_data = yaml.safe_load(f)
                adapters = config_data.get('ontology_adapters', {})
                # Convert keys to lowercase for case-insensitive lookup
                oak_config = {k.lower(): v for k, v in adapters.items()}

                # Validate REST adapter configurations
                self._validate_oak_config(oak_config)

                return oak_config
        except Exception as e:
            logger.warning(f"Could not load OAK config: {e}")
            return {}

    def _validate_oak_config(self, oak_config: Dict[str, str]):
        """
        Validate OAK configuration for potential issues.

        Checks for REST adapter configurations when REST adapters module is not available.
        Logs warnings but does not raise exceptions to maintain graceful degradation.
        """
        for prefix, adapter_string in oak_config.items():
            if adapter_string and adapter_string.startswith("rest:"):
                if not HAS_REST_ADAPTERS:
                    logger.error(
                        f"Configuration error: Prefix '{prefix.upper()}' is configured to use "
                        f"REST adapter '{adapter_string}' but REST adapters module is not available. "
                        f"Install required dependencies or update oak_config.yaml."
                    )

    def _get_cache_file(self, prefix: str) -> Path:
        """Get the cache file path for a given prefix."""
        cache_dir = self.config.cache_dir / prefix.lower()
        cache_dir.mkdir(parents=True, exist_ok=True)
        return cache_dir / "terms.csv"

    def _load_cache(self, prefix: str) -> Dict[str, str]:
        """Load cached terms for a prefix."""
        cache_file = self._get_cache_file(prefix)
        cache = {}

        if cache_file.exists():
            try:
                with open(cache_file, 'r', newline='') as f:
                    reader = csv.reader(f)
                    next(reader)  # Skip header
                    for row in reader:
                        if len(row) >= 2:
                            cache[row[0]] = row[1]  # curie -> label
            except Exception as e:
                logger.warning(f"Could not load cache for {prefix}: {e}")

        return cache

    def _save_to_cache(self, prefix: str, curie: str, label: Optional[str]):
        """Save a term to cache."""
        if prefix.lower() not in self._oak_config:
            return  # Only cache for configured prefixes

        cache_file = self._get_cache_file(prefix)

        # Read existing cache
        existing_cache = set()
        if cache_file.exists():
            try:
                with open(cache_file, 'r', newline='') as f:
                    reader = csv.reader(f)
                    next(reader)  # Skip header
                    for row in reader:
                        if len(row) >= 1:
                            existing_cache.add(row[0])
            except Exception:
                pass

        # Don't add if already exists
        if curie in existing_cache:
            return

        # Append new entry
        try:
            # Create file with header if it doesn't exist
            if not cache_file.exists():
                with open(cache_file, 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(['curie', 'label', 'retrieved_at'])

            # Append new row
            with open(cache_file, 'a', newline='') as f:
                writer = csv.writer(f)
                timestamp = datetime.now().isoformat()
                writer.writerow([curie, label or '', timestamp])
        except Exception as e:
            logger.warning(f"Could not save to cache for {prefix}: {e}")

    def _initialize_oak(self):
        """Initialize OAK adapters dynamically based on usage."""
        if not HAS_OAK:
            logger.warning("OAK is not installed. Install with: pip install oaklib")
            return

        # Don't initialize a main adapter if using dynamic sqlite:obo:
        # We'll create per-prefix adapters on demand
        if self.config.oak_adapter_string == "sqlite:obo:":
            logger.info("Using dynamic SemSQL adapter selection based on CURIE prefix")
            return

        # For other adapter types (ols:, bioportal:, etc), create a single adapter
        try:
            self._per_prefix_adapters['_default'] = get_adapter(self.config.oak_adapter_string)
            logger.info(f"Initialized OAK adapter: {self.config.oak_adapter_string}")
        except Exception as e:
            logger.warning(f"Could not initialize OAK adapter: {e}")

    def get_ontology_label(self, curie: str) -> Optional[str]:
        """
        Get the label for an ontology term using OAK.

        Checks local cache first, then tries OAK lookup, then saves to cache.
        """
        # Check in-memory cache first
        if self._label_cache is not None and curie in self._label_cache:
            return self._label_cache[curie]

        # Parse the CURIE to get the prefix
        prefix = curie.split(":")[0] if ":" in curie else None
        if not prefix:
            return None

        prefix_lower = prefix.lower()

        # Check file cache for configured prefixes
        if prefix_lower in self._prefix_caches:
            if curie in self._prefix_caches[prefix_lower]:
                label = self._prefix_caches[prefix_lower][curie]
                # Also cache in memory
                if self._label_cache is not None:
                    self._label_cache[curie] = label
                return label if label else None

        label = None
        adapter = None

        # Load cache for this prefix if not already loaded
        if prefix_lower in self._oak_config and prefix_lower not in self._prefix_caches:
            self._prefix_caches[prefix_lower] = self._load_cache(prefix)

        # Try configured adapter first for this prefix
        if prefix_lower in self._oak_config:
            adapter_string = self._oak_config[prefix_lower]

            # If adapter string is empty or None, skip validation entirely
            if not adapter_string:
                logger.debug(f"Skipping validation for {prefix} (empty adapter string in config)")
                self._per_prefix_adapters[prefix_lower] = None
                return None

            if prefix_lower not in self._per_prefix_adapters:
                try:
                    # Check if this is a REST adapter (e.g., "rest:ror:")
                    if adapter_string.startswith("rest:"):
                        if not HAS_REST_ADAPTERS:
                            logger.warning(f"REST adapters module not available for {prefix}")
                            self._per_prefix_adapters[prefix_lower] = None
                        else:
                            adapter = get_rest_adapter(adapter_string)
                            if adapter:
                                self._per_prefix_adapters[prefix_lower] = adapter
                                logger.info(f"Created REST adapter for {prefix}: {adapter_string}")
                            else:
                                logger.warning(f"Could not create REST adapter for {prefix}: {adapter_string}")
                                self._per_prefix_adapters[prefix_lower] = None
                    else:
                        # Standard OAK adapter
                        self._per_prefix_adapters[prefix_lower] = get_adapter(adapter_string)
                        logger.info(f"Created configured adapter for {prefix} ontology")
                except Exception as e:
                    logger.warning(f"Could not create configured adapter for {prefix}: {e}")
                    self._per_prefix_adapters[prefix_lower] = None

            adapter = self._per_prefix_adapters.get(prefix_lower)
        elif self.config.oak_adapter_string == "sqlite:obo:" and prefix:
            # Dynamic mode: create per-ontology adapter on demand
            if prefix_lower not in self._per_prefix_adapters:
                try:
                    adapter_string = f"sqlite:obo:{prefix_lower}"
                    self._per_prefix_adapters[prefix_lower] = get_adapter(adapter_string)
                    logger.info(f"Created adapter for {prefix} ontology")
                except Exception as e:
                    logger.debug(f"Could not create adapter for {prefix}: {e}")
                    # Track unknown prefix for end-of-run reporting
                    if prefix_lower not in self._warned_prefixes:
                        self._warned_prefixes.add(prefix_lower)
                    self._per_prefix_adapters[prefix_lower] = None

            adapter = self._per_prefix_adapters.get(prefix_lower)
        else:
            # Use default adapter for other configurations
            adapter = self._per_prefix_adapters.get('_default')

        # Get the label
        if adapter:
            try:
                label = adapter.label(curie)
            except Exception as e:
                logger.debug(f"Could not get label for {curie}: {e}")

        # Cache the result in memory
        if self._label_cache is not None:
            self._label_cache[curie] = label

        # Save to file cache for configured prefixes
        if prefix_lower in self._oak_config:
            self._save_to_cache(prefix, curie, label)
            # Also update in-memory cache
            if prefix_lower in self._prefix_caches:
                self._prefix_caches[prefix_lower][curie] = label or ''

        return label

    def is_prefix_configured(self, prefix: str) -> bool:
        """Check if a prefix is configured for strict validation."""
        prefix_lower = prefix.lower()
        return (prefix_lower in self._oak_config and
                bool(self._oak_config[prefix_lower]))

    def normalize_string(self, s: str) -> str:
        """
        Normalize a string for comparison by removing non-alphanumeric chars
        and converting to lowercase.
        """
        if not s:
            return ""
        # Remove non-alphanumeric characters
        s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
        # Collapse multiple spaces
        s = re.sub(r'\s+', ' ', s)
        return s.strip().lower()

    def extract_aliases(self, pv: PermissibleValue, value_name: str) -> Set[str]:
        """
        Extract all possible aliases for a permissible value.

        This includes:
        - The value name itself
        - The title (if present)
        - Any aliases (if present)
        - Annotations that might contain display names
        """
        aliases = {value_name}

        if pv.title:
            aliases.add(pv.title)

        if pv.aliases:
            aliases.update(pv.aliases)

        # Add structured_aliases if present
        if hasattr(pv, 'structured_aliases') and pv.structured_aliases:
            for struct_alias in pv.structured_aliases:
                if hasattr(struct_alias, 'literal_form') and struct_alias.literal_form:
                    aliases.add(struct_alias.literal_form)

        # Check annotations for common alias fields
        if pv.annotations:
            for key in ['label', 'display_name', 'preferred_name', 'synonym']:
                if key in pv.annotations:
                    val = pv.annotations[key]
                    if val and hasattr(val, 'value'):
                        aliases.add(str(val.value))
                    elif val:
                        aliases.add(str(val))

        return aliases

    def validate_enum(self, enum_def: EnumDefinition, enum_name: str) -> List[ValidationIssue]:
        """
        Validate a single enum definition.
        """
        issues = []

        if not enum_def.permissible_values:
            return issues

        for value_name, pv in enum_def.permissible_values.items():
            # Check if there's a meaning (ontology mapping)
            meaning = pv.meaning
            if not meaning:
                continue

            # Check if this prefix has an empty adapter string (skip validation)
            prefix = meaning.split(":")[0] if ":" in meaning else None
            if prefix and prefix.lower() in self._oak_config and not self._oak_config[prefix.lower()]:
                logger.debug(f"Skipping validation for {meaning} (empty adapter string in config)")
                continue

            # Get the actual label from ontology
            actual_label = self.get_ontology_label(meaning)

            # Get all possible expected labels
            expected_labels = self.extract_aliases(pv, value_name)

            # Normalize for comparison
            normalized_expected = {self.normalize_string(label) for label in expected_labels}
            normalized_actual = self.normalize_string(actual_label) if actual_label else None

            # Check if actual label matches any expected label
            if actual_label is None:
                # Could not retrieve label - severity depends on whether prefix is configured
                prefix = meaning.split(":")[0] if ":" in meaning else None
                if prefix and self.is_prefix_configured(prefix):
                    # Strict mode for configured prefixes
                    severity = "ERROR"
                    message = f"Could not retrieve label for configured ontology term {meaning}"
                else:
                    # Lenient mode for unconfigured prefixes
                    severity = "INFO"
                    message = f"Could not retrieve label for {meaning}"

                issue = ValidationIssue(
                    enum_name=enum_name,
                    value_name=value_name,
                    severity=severity,
                    message=message,
                    meaning=meaning
                )
                issues.append(issue)
            elif normalized_actual not in normalized_expected:
                # Label mismatch - treat as ERROR for configured prefixes or in strict mode
                prefix = meaning.split(":")[0] if ":" in meaning else None
                is_configured = prefix and self.is_prefix_configured(prefix)
                severity = "ERROR" if (self.config.strict_mode or is_configured) else "WARNING"
                issue = ValidationIssue(
                    enum_name=enum_name,
                    value_name=value_name,
                    severity=severity,
                    message=f"Ontology label mismatch: expected one of {expected_labels}, got '{actual_label}'",
                    meaning=meaning,
                    expected_label=value_name,
                    actual_label=actual_label
                )
                issues.append(issue)

        return issues

    def validate_schema(self, schema_path: Path) -> ValidationResult:
        """
        Validate all enums in a schema.
        """
        result = ValidationResult(schema_path=schema_path)

        try:
            # Load schema
            sv = SchemaView(str(schema_path))

            # Validate each enum
            for enum_name, enum_def in sv.all_enums().items():
                result.total_enums_checked += 1

                if enum_def.permissible_values:
                    result.total_values_checked += len(enum_def.permissible_values)

                    # Count mappings
                    for pv in enum_def.permissible_values.values():
                        if pv.meaning:
                            result.total_mappings_checked += 1

                    # Validate the enum
                    issues = self.validate_enum(enum_def, enum_name)
                    result.issues.extend(issues)

        except Exception as e:
            logger.error(f"Error validating schema {schema_path}: {e}")
            issue = ValidationIssue(
                enum_name="<schema>",
                value_name="<error>",
                severity="ERROR",
                message=f"Failed to validate schema: {e}",
                meaning=None
            )
            result.issues.append(issue)

        return result

    def report_unknown_prefixes(self) -> None:
        """Report unknown ontology prefixes that were encountered during validation."""
        if self._warned_prefixes:
            print(f"\n📋 Unknown ontology prefixes encountered:")
            print("   Consider adding these to oak_config.yaml if they are valid ontologies:")
            for prefix in sorted(self._warned_prefixes):
                print(f"   • {prefix.upper()}: sqlite:obo:{prefix}")
            print(f"   Or remove the 'meaning:' mappings if these are not valid ontology terms.")


def main():
    """Main function for CLI usage."""
    import argparse

    parser = argparse.ArgumentParser(description="Validate LinkML enum ontology mappings")
    parser.add_argument("path", type=Path, help="Path to schema file or directory")
    parser.add_argument("--adapter", default="sqlite:obo:",
                       help="OAK adapter string (e.g., sqlite:obo:, sqlite:obo:merged, ols:, bioportal:)")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    parser.add_argument("--no-cache", action="store_true", help="Disable label caching")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output with detailed information")

    args = parser.parse_args()

    # Build configuration
    config = ValidationConfig(
        oak_adapter_string=args.adapter,
        strict_mode=args.strict,
        cache_labels=not args.no_cache
    )

    # Configure logging based on verbose flag
    if args.verbose:
        logging.basicConfig(level=logging.INFO, force=True)
    else:
        # Suppress all logging output in non-verbose mode
        logging.basicConfig(level=logging.CRITICAL, force=True)
        # Also suppress oaklib and other library logging
        for logger_name in ['oaklib', 'root', 'pystow', 'linkml_runtime', 'urllib3', 'httpx', 'httpcore']:
            logging.getLogger(logger_name).setLevel(logging.CRITICAL)

        # Suppress pystow progress bars
        import os
        os.environ['PYSTOW_NO_PROGRESS'] = '1'

    # Create evaluator
    evaluator = EnumEvaluator(config)

    if not HAS_OAK:
        print("Error: OAK is not installed. Please install with: pip install oaklib")
        return 1

    # Process path
    if args.path.is_file():
        result = evaluator.validate_schema(args.path)

        # Handle output based on results and verbosity
        if not result.has_errors() and not result.has_warnings():
            if args.verbose:
                result.print_summary()
            else:
                print("✅")  # Just a checkmark for success

            # Report unknown prefixes even on success
            evaluator.report_unknown_prefixes()
            return 0
        else:
            # Always show errors and warnings, but format differently based on verbosity
            if args.verbose:
                result.print_summary()
                # Show all issues in verbose mode
                for issue in result.issues:
                    print(f"\n{issue.severity}: {issue.enum_name}.{issue.value_name}")
                    print(f"  {issue.message}")
                    if issue.meaning:
                        print(f"  CURIE: {issue.meaning}")
            else:
                # Concise output for non-verbose mode
                errors = [i for i in result.issues if i.severity == "ERROR"]
                warnings = [i for i in result.issues if i.severity == "WARNING"]

                if errors:
                    print(f"❌ Validation failed with {len(errors)} error(s)\n")
                    print("ERRORS:")
                    for issue in errors:
                        print(f"  • {args.path.name}:{issue.enum_name}.{issue.value_name}: {issue.message}")
                        if issue.meaning:
                            print(f"    Fix: Check CURIE {issue.meaning}")

                if warnings and not args.strict:
                    print(f"\n⚠️  {len(warnings)} warning(s):")
                    for issue in warnings[:LIMIT]:  # Show first 100 warnings
                        id_info = f" [{issue.meaning}]" if issue.meaning else ""
                        print(f"  • {issue.enum_name}.{issue.value_name}{id_info}: {issue.message}")
                    if len(warnings) > LIMIT:
                        print(f"  ... and {len(warnings) - LIMIT} more warnings")

            # Report unknown prefixes
            evaluator.report_unknown_prefixes()

            return 1 if result.has_errors() or (args.strict and result.has_warnings()) else 0

    elif args.path.is_dir():
        all_results = []
        schema_files = sorted([f for f in args.path.rglob("*.yaml")
                               if "linkml_model" not in str(f)])

        if args.verbose:
            print(f"🔍 Validating {len(schema_files)} schema files...\n")

        # Collect results
        for schema_file in schema_files:
            if args.verbose:
                print(f"Validating {schema_file.name}...")

            result = evaluator.validate_schema(schema_file)
            result.schema_path = schema_file  # Store path for error reporting
            all_results.append(result)

            if args.verbose:
                result.print_summary()

        # Calculate totals
        total_errors = sum(len([i for i in r.issues if i.severity == "ERROR"]) for r in all_results)
        total_warnings = sum(len([i for i in r.issues if i.severity == "WARNING"]) for r in all_results)

        # Output based on results
        if total_errors == 0 and total_warnings == 0:
            if args.verbose:
                print(f"\n{'='*60}")
                print(f"✅ All {len(schema_files)} schemas validated successfully!")
            else:
                print("✅")  # Just a checkmark for complete success

            # Report unknown prefixes even on success
            evaluator.report_unknown_prefixes()
            return 0
        else:
            # Show errors and warnings
            if not args.verbose:
                # Concise error listing
                if total_errors > 0:
                    print(f"❌ Validation failed with {total_errors} error(s) in {sum(1 for r in all_results if r.has_errors())} file(s)\n")
                    print("ERRORS:")
                    for result in all_results:
                        errors = [i for i in result.issues if i.severity == "ERROR"]
                        if errors:
                            for issue in errors:
                                schema_name = result.schema_path.name if hasattr(result, 'schema_path') else 'unknown'
                                print(f"  • {schema_name}:{issue.enum_name}.{issue.value_name}: {issue.message}")
                                if issue.meaning:
                                    print(f"    Fix: Check CURIE {issue.meaning}")

                if total_warnings > 0 and not args.strict:
                    print(f"\n⚠️  {total_warnings} warning(s) in {sum(1 for r in all_results if r.has_warnings())} file(s)")
                    # Show first few warnings
                    warning_count = 0
                    for result in all_results:
                        warnings = [i for i in result.issues if i.severity == "WARNING"]
                        for issue in warnings:
                            if warning_count < 100:
                                schema_name = result.schema_path.name if hasattr(result, 'schema_path') else 'unknown'
                                id_info = f" [{issue.meaning}]" if issue.meaning else ""
                                print(f"  • {schema_name}:{issue.enum_name}.{issue.value_name}{id_info}: {issue.message}")
                                warning_count += 1
                            else:
                                break
                        if warning_count >= 100:
                            break
                    if total_warnings > 100:
                        print(f"  ... and {total_warnings - 100} more warnings")
            else:
                # Verbose output
                print(f"\n{'='*60}")
                print(f"Overall: {total_errors} errors, {total_warnings} warnings in {len(schema_files)} files")

            # Report unknown prefixes
            evaluator.report_unknown_prefixes()

            return 1 if total_errors > 0 or (args.strict and total_warnings > 0) else 0
    else:
        print(f"Error: {args.path} is not a file or directory")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
