## Add your own just recipes here. This is imported by the main justfile.

# Override the default gen-python to use modular rich enum generator
# This is THE canonical form for Python generation - modular rich enums
gen-python:
  @echo "🔧 Generating modular Python enums with rich metadata..."
  # Generate modular enums in src/valuesets/enums/
  uv run python -m src.valuesets.generators.modular_rich_generator {{source_schema_dir}} -o src/{{schema_name}}/enums
  @echo "✅ Generated modular rich enums in src/{{schema_name}}/enums/"
  # Keep legacy datamodel for backwards compatibility
  uv run gen-project -d {{pymodel}} -I python {{source_schema_path}}
  mv {{pymodel}}/{{schema_name}}.py {{pymodel}}/{{schema_name}}_dataclass.py
  uv run python -m src.valuesets.generators.rich_pydantic_generator {{source_schema_path}} -o {{pymodel}}/{{schema_name}}.py
  @echo "✅ Generated Python with modular rich enums"

# Override the default gen-project to use modular rich enum generator
[group('model development')]
gen-project:
  @echo "🔧 Generating project with modular rich enum support..."
  # Generate modular enums FIRST
  uv run python -m src.valuesets.generators.modular_rich_generator {{source_schema_dir}} -o src/{{schema_name}}/enums
  @echo "✅ Generated modular rich enums in src/{{schema_name}}/enums/"
  # Then generate standard project files
  uv run gen-project {{config_yaml}} -d {{dest}} {{source_schema_path}}
  # Move the standard generated files (for legacy support) - check if they exist first
  @if ls {{dest}}/*.py 1> /dev/null 2>&1; then \
    mv {{dest}}/*.py {{pymodel}} && \
    mv {{pymodel}}/{{schema_name}}.py {{pymodel}}/{{schema_name}}_dataclass.py ; \
  fi
  # Generate rich enum version as the main Python file
  uv run python -m src.valuesets.generators.rich_pydantic_generator {{source_schema_path}} -o {{pymodel}}/{{schema_name}}.py
  # Also generate the pydantic version with rich enums
  uv run python -m src.valuesets.generators.rich_pydantic_generator {{source_schema_path}} -o {{pymodel}}/{{schema_name}}_pydantic.py
  # Generate other artifacts
  uv run gen-java {{gen_java_args}} --output-directory {{dest}}/java/ {{source_schema_path}}
  just gen-owl
  @if [ ! ${{gen_ts_args}} ]; then \
    uv run gen-typescript {{gen_ts_args}} {{source_schema_path}} > {{dest}}/typescript/{{schema_name}}.ts || true ; \
  fi
  @echo "✅ Generated project with rich Python enums"

# Alias for backward compatibility (or if you want the dataclass version)
gen-python-dataclass:
  uv run gen-project -d {{pymodel}} -I python {{source_schema_path}}

# Merge all schemas into a single hierarchical structure
[group('model development')]
merge-hierarchy:
  @echo "🔀 Merging all schemas into hierarchical structure..."
  @mkdir -p src/valuesets/merged
  uv run python scripts/merge_enums_hierarchy.py --output src/valuesets/merged/merged_hierarchy.yaml
  @echo "✅ Merged hierarchy written to src/valuesets/merged/merged_hierarchy.yaml"

# Validate merged hierarchy
[group('model development')]
validate-merged:
  @echo "🔍 Validating merged hierarchy schema..."
  uv run linkml-validate --schema src/valuesets/merged/merged_hierarchy.yaml
  @echo "✅ Merged hierarchy schema is valid"

# Generate OWL from merged hierarchy
[group('model development')]
gen-owl:
  @echo "🦉 Generating OWL from merged hierarchy..."
  # Ensure merged hierarchy exists
  @if [ ! -f src/valuesets/merged/merged_hierarchy.yaml ]; then \
    echo "⚠️  Merged hierarchy not found, creating it..."; \
    just merge-hierarchy; \
  fi
  # Create output directory
  mkdir -p project/owl
  # Generate OWL
  uv run gen-owl src/valuesets/merged/merged_hierarchy.yaml > project/owl/valuesets.owl.ttl
  @echo "✅ Generated OWL at project/owl/valuesets.owl.ttl"
  # Get file size for verification
  @ls -lh project/owl/valuesets.owl.ttl | awk '{print "📊 File size: " $$5}'


# Validate ontology mappings in enum definitions
[group('model development')]
validate *ARGS:
  @echo "🔍 Validating ontology mappings in enums..."
  uv run python -m src.valuesets.validators.enum_evaluator {{source_schema_dir}} {{ARGS}}

# Validate a specific schema file or directory
[group('model development')]
validate-schema SCHEMA_PATH *ARGS:
  @echo "🔍 Validating ontology mappings in {{SCHEMA_PATH}}..."
  uv run python -m src.valuesets.validators.enum_evaluator {{SCHEMA_PATH}} {{ARGS}}

# Validate using OLS web service
[group('model development')]
validate-ols *ARGS:
  @echo "🔍 Validating ontology mappings using OLS..."
  uv run python -m src.valuesets.validators.enum_evaluator {{source_schema_dir}} --adapter "ols:" {{ARGS}}

# Run validation tests with mock data
[group('model development')]
test-validate:
  @echo "🧪 Running validation tests..."
  uv run python src/valuesets/validators/test_validator.py

# Generate SSSOM TSV file with ontology mappings
[group('model development')]
gen-sssom *ARGS:
  @echo "📊 Generating SSSOM TSV with ontology mappings..."
  @mkdir -p project/mappings
  uv run python -m src.valuesets.generators.sssom_generator {{source_schema_dir}} -o project/mappings/enum_mappings.sssom.tsv {{ARGS}}
  @echo "✅ Generated project/mappings/enum_mappings.sssom.tsv"

# Generate SSSOM for a specific schema
[group('model development')]
gen-sssom-schema SCHEMA_PATH OUTPUT="project/mappings/schema_mappings.sssom.tsv" *ARGS:
  @echo "📊 Generating SSSOM TSV for {{SCHEMA_PATH}}..."
  @mkdir -p project/mappings
  uv run python -m src.valuesets.generators.sssom_generator {{SCHEMA_PATH}} -o {{OUTPUT}} {{ARGS}}
  @echo "✅ Generated {{OUTPUT}}"

# List all dynamic enums (those with reachable_from definitions)
[group('model development')]
list-dynamic-enums:
  uv run python -m src.valuesets.utils.query_describer --list {{source_schema_dir}}

# List dynamic enums in markdown format (with links)
[group('model development')]
list-dynamic-enums-md:
  uv run python -m src.valuesets.utils.query_describer --list --markdown {{source_schema_dir}}

# List dynamic enums in markdown with labels from OLS (slower)
[group('model development')]
list-dynamic-enums-full:
  uv run python -m src.valuesets.utils.query_describer --list --markdown --labels {{source_schema_dir}}

# Generate md documentation for the schema (with dynamic enum enrichment)
[group('model development')]
gen-doc: _gen-yaml
  uv run gen-doc {{gen_doc_args}} -d {{docdir}} {{source_schema_path}}
  @echo "Enriching dynamic enum documentation..."
  uv run python scripts/enrich_enum_docs.py --schema-dir {{source_schema_dir}} --docs-dir {{docdir}}

# Expand all dynamic enums using OAK
[group('model development')]
expand-enums workers="4":
  @echo "🔄 Expanding all dynamic enums using OAK..."
  @echo "   This may take a while on first run as ontologies are downloaded..."
  uv run python -m src.valuesets.utils.expand_dynamic_enums \
    --schema-dir {{source_schema_dir}} \
    --workers {{workers}}
  @echo "✅ Expanded enums saved to src/valuesets/expanded/"

# Expand dynamic enums from a specific schema file
[group('model development')]
expand-enums-schema SCHEMA_PATH OUTPUT_DIR="src/valuesets/expanded" WORKERS="4":
  @echo "🔄 Expanding dynamic enums from {{SCHEMA_PATH}}..."
  uv run python -m src.valuesets.utils.expand_dynamic_enums \
    --schema-dir {{SCHEMA_PATH}} \
    --output-dir {{OUTPUT_DIR}} \
    --workers {{WORKERS}}
  @echo "✅ Expanded enums saved to {{OUTPUT_DIR}}/"

# ============== UniProt Data Sync ==============

# Sync UniProt species data from the UniProt API
[group('data sync')]
sync-uniprot-species:
  @echo "🔄 Syncing UniProt species data..."
  uv run python scripts/sync_uniprot_species.py
  @echo "✅ UniProt species data synced to src/valuesets/schema/bio/uniprot_species.yaml"

# Sync all UniProt reference proteomes (~500 organisms)
[group('data sync')]
sync-uniprot-reference:
  @echo "🔄 Syncing all UniProt reference proteomes..."
  uv run python scripts/sync_uniprot_species.py --extended
  @echo "✅ All UniProt reference proteomes synced (~500 organisms)"

# Preview UniProt sync without making changes
[group('data sync')]
preview-uniprot-sync:
  @echo "👀 Previewing UniProt species sync (dry run)..."
  @cp src/valuesets/schema/bio/uniprot_species.yaml /tmp/uniprot_species_preview.yaml
  uv run python scripts/sync_uniprot_species.py --output /tmp/uniprot_species_preview.yaml
  @echo "Preview saved to /tmp/uniprot_species_preview.yaml"
  @echo "Run 'diff src/valuesets/schema/bio/uniprot_species.yaml /tmp/uniprot_species_preview.yaml' to see changes"
