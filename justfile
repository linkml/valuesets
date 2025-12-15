# ============ Hint for for Windows Users ============

# On Windows the "sh" shell that comes with Git for Windows should be used.
# If it is not on path, provide the path to the executable in the following line.
#set windows-shell := ["C:/Program Files/Git/usr/bin/sh", "-cu"]

# ============ Variables used in recipes ============

# Load environment variables from config.public.mk or specified file
set dotenv-load := true
# set dotenv-filename := env_var_or_default("LINKML_ENVIRONMENT_FILENAME", "config.public.mk")
set dotenv-filename := x'${LINKML_ENVIRONMENT_FILENAME:-config.public.mk}'

# Set shebang line for cross-platform Python recipes (assumes presence of launcher on Windows)
shebang := if os() == 'windows' {
  'py'
} else {
  '/usr/bin/env python3'
}

# Environment variables with defaults
schema_name := env_var_or_default("LINKML_SCHEMA_NAME", "_no_schema_given_")
source_schema_dir := env_var_or_default("LINKML_SCHEMA_SOURCE_DIR", "")
config_yaml := if env_var_or_default("LINKML_GENERATORS_CONFIG_YAML", "") != "" {
  "--config-file " + env_var_or_default("LINKML_GENERATORS_CONFIG_YAML", "")
} else {
  ""
}
gen_doc_args := env_var_or_default("LINKML_GENERATORS_DOC_ARGS", "")
gen_java_args := env_var_or_default("LINKML_GENERATORS_JAVA_ARGS", "")
gen_owl_args := env_var_or_default("LINKML_GENERATORS_OWL_ARGS", "")
gen_pydantic_args := env_var_or_default("LINKML_GENERATORS_PYDANTIC_ARGS", "")
gen_ts_args := env_var_or_default("LINKML_GENERATORS_TYPESCRIPT_ARGS", "")

# Directory variables
src := "src"
dest := "project"
pymodel := src / schema_name / "datamodel"
source_schema_path := source_schema_dir / schema_name + ".yaml"
docdir := "docs/elements"  # Directory for generated documentation
merged_schema_path := "docs/schema" / schema_name + ".yaml"

# ============== Project recipes ==============

# List all commands as default command. The prefix "_" hides the command.
_default: _status
    @just --list

# Initialize a new project (use this for projects not yet under version control)
[group('project management')]
setup: _check-config _git-init install _git-add && _setup_part2
  git commit -m "Initialise git with minimal project" -a

_setup_part2: gen-project gen-doc
  @echo
  @echo '=== Setup completed! ==='
  @echo 'Various model representations have been created under directory "project". By default'
  @echo 'they are ignored by git. You decide whether you want to add them to git tracking or'
  @echo 'continue to git-ignore them as they can be regenerated if needed.'
  @echo 'For tracking specific subfolders, add !project/[foldername]/* line(s) to ".gitignore".'

# Install project dependencies
[group('project management')]
install:
  uv sync --group dev

# Updates project template and LinkML package
[group('project management')]
update: _update-template _update-linkml

# Clean all generated files
[group('project management')]
clean: _clean_project
  rm -rf tmp
  rm -rf {{docdir}}/*.md

# (Re-)Generate project and documentation locally
[group('model development')]
site: gen-project gen-doc gen-slides

# Deploy documentation site to Github Pages
[group('deployment')]
deploy: site
  mkd-gh-deploy

# Run all tests
[group('model development')]
test: _test-schema _test-python _test-examples

# Run linting
[group('model development')]
lint:
  uv run linkml-lint {{source_schema_dir}}

# Generate md documentation for the schema
# NOTE: Overridden in project.justfile to include dynamic enum enrichment
# [group('model development')]
# gen-doc: _gen-yaml
#   uv run gen-doc {{gen_doc_args}} -d {{docdir}} {{source_schema_path}}

# Build docs and run test server
[group('model development')]
testdoc: gen-doc _serve

# Generate presentation slides in all formats
[group('model development')]
gen-slides:
  cd docs/slides && marp valuesets-slides.md --allow-local-files -o valuesets-slides.html
  cd docs/slides && marp valuesets-slides.md --allow-local-files --pdf -o valuesets-slides.pdf
  cd docs/slides && marp valuesets-slides.md --allow-local-files --pptx -o valuesets-slides.pptx
  @echo "Slides generated in docs/slides/"

# Generate the Python data models (dataclasses & pydantic)
# NOTE: Overridden in project.justfile to use rich enums as default
# gen-python:
#   uv run gen-project -d  {{pymodel}} -I python {{source_schema_path}}
#   uv run gen-pydantic {{gen_pydantic_args}} {{source_schema_path}} > {{pymodel}}/{{schema_name}}.py

# Generate project files including Python data model
# NOTE: Overridden in project.justfile to use rich enums as default
# [group('model development')]
# gen-project:
#   uv run gen-project {{config_yaml}} -d {{dest}} {{source_schema_path}}
#   mv {{dest}}/*.py {{pymodel}}
#   uv run gen-pydantic {{gen_pydantic_args}} {{source_schema_path}} > {{pymodel}}/{{schema_name}}_pydantic.py
#   uv run gen-java {{gen_java_args}} --output-directory {{dest}}/java/ {{source_schema_path}}
#   @if [ ! ${{gen_owl_args}} ]; then \
#     mkdir -p {{dest}}/owl && \
#     uv run gen-owl {{gen_owl_args}} {{source_schema_path}} > {{dest}}/owl/{{schema_name}}.owl.ttl || true ; \
#   fi
#   @if [ ! ${{gen_ts_args}} ]; then \
#     uv run gen-typescript {{gen_ts_args}} {{source_schema_path}} > {{dest}}/typescript/{{schema_name}}.ts || true ; \
#   fi

# ============== Migrations recipes for Copier ==============

# Hidden command to adjust the directory layout on upgrading a project
# created with linkml-project-copier v0.1.x to v0.2.0 or newer.
# Use with care! - It may not work for customized projects.
_post_upgrade_v020: && _post_upgrade_v020py
  mv docs/*.md docs/elements

_post_upgrade_v020py:
    #!{{shebang}}
    import subprocess
    from pathlib import Path
    # Git move files from folder src to folder dest
    tasks = [
        (Path("src/docs/files"), Path("docs")),
        (Path("src/docs/templates"), Path("docs/templates-linkml")),
        (Path("src/data/examples"), Path("tests/data/")),
    ]
    for src, dest in tasks:
        for path_obj in src.rglob("*"):
            if not path_obj.is_file():
                continue
            file_dest = dest / path_obj.relative_to(src)
            if not file_dest.parent.exists():
                file_dest.parent.mkdir(parents=True)
            print(f"Moving {path_obj} --> {file_dest}")
            subprocess.run(["git", "mv", str(path_obj), str(file_dest)])
    print(
        "Migration to v0.2.x completed! Check the changes carefully before committing."
    )

# ============== Hidden internal recipes ==============

# Show current project status
_status: _check-config
  @echo "Project: {{schema_name}}"
  @echo "Source: {{source_schema_path}}"

# Check project configuration
_check-config:
    #!{{shebang}}
    import os
    schema_name = os.getenv('LINKML_SCHEMA_NAME')
    if not schema_name:
        print('**Project not configured**:\n - See \'.env.public\'')
        exit(1)
    print('Project-status: Ok')

# Update project template
_update-template:
  copier update --trust --skip-answered

# Update LinkML to latest version
_update-linkml:
  uv add linkml --upgrade-package linkml

# Test schema generation
_test-schema:
  uv run gen-project {{config_yaml}} -d tmp {{source_schema_path}}

# Run Python unit tests with pytest
_test-python: gen-python
  uv run python -m pytest

# Run example tests
_test-examples: _ensure_examples_output
  uv run linkml-run-examples \
    --input-formats json \
    --input-formats yaml \
    --output-formats json \
    --output-formats yaml \
    --counter-example-input-directory tests/data/invalid \
    --input-directory tests/data/valid \
    --output-directory examples/output \
    --schema {{source_schema_path}} > examples/output/README.md

# Generate merged model
_gen-yaml:
  -mkdir -p docs/schema
  uv run gen-yaml {{source_schema_path}} > {{merged_schema_path}}

# Run documentation server
_serve:
  uv run mkdocs serve

# Initialize git repository
_git-init:
  git init

# Add files to git
_git-add:
  git add .

# Commit files to git
_git-commit:
  git commit -m 'chore: just setup was run' -a

# Show git status
_git-status:
  git status

_clean_project:
    #!{{shebang}}
    import shutil, pathlib
    # remove the generated project files
    for d in pathlib.Path("{{dest}}").iterdir():
        if d.is_dir():
            print(f'removing "{d}"')
            shutil.rmtree(d, ignore_errors=True)
    # remove the generated python data model
    for d in pathlib.Path("{{pymodel}}").iterdir():
        if d.name == "__init__.py":
            continue
        print(f'removing "{d}"')
        if d.is_dir():
            shutil.rmtree(d, ignore_errors=True)
        else:
            d.unlink()

_ensure_examples_output:  # Ensure a clean examples/output directory exists
  -mkdir -p examples/output
  -rm -rf examples/output/*.*

# ============== Slot Generation Recipes ==============

# Generate slots for a single schema file
[group('slot generation')]
gen-slots file:
  uv run python src/valuesets/generators/smart_slot_syncer.py {{file}} --in-place -v

# Preview slot generation for a single schema file
[group('slot generation')]
preview-slots file:
  uv run python src/valuesets/generators/smart_slot_syncer.py {{file}} --dry-run -v

# Generate slots for ALL schemas in the project
[group('slot generation')]
gen-all-slots:
  uv run python src/valuesets/generators/smart_slot_syncer.py src/valuesets/schema --batch --in-place

# Sync slots for all schemas in the project (alias for gen-all-slots)
[group('slot generation')]
sync-all-slots:
  uv run python src/valuesets/generators/smart_slot_syncer.py src/valuesets/schema --batch --in-place

# Preview slot sync for all schemas
[group('slot generation')]
preview-all-slots:
  uv run python src/valuesets/generators/smart_slot_syncer.py src/valuesets/schema --batch --dry-run

# Generate comprehensive slots file from all enums
[group('slot generation')]
gen-slots-file:
  uv run python src/valuesets/generators/auto_slot_injector.py src/valuesets/schema --mode generate --output src/valuesets/schema/generated_slots.yaml

# Refresh all slots (regenerate from scratch, losing customizations)
[group('slot generation')]
refresh-slots file:
  uv run python src/valuesets/generators/smart_slot_syncer.py {{file}} --in-place --mode refresh -v

# Conservative slot sync (only add new, never modify existing)
[group('slot generation')]
conservative-slots file:
  uv run python src/valuesets/generators/smart_slot_syncer.py {{file}} --in-place --mode conservative -v

# Clean up orphaned slots (remove slots for deleted enums)
[group('slot generation')]
cleanup-slots file:
  uv run python src/valuesets/generators/smart_slot_syncer.py {{file}} --in-place --remove-orphans -v

# Standardize prefixes across all schemas
[group('slot generation')]
standardize-prefixes:
  uv run python src/valuesets/generators/prefix_standardizer.py src/valuesets/schema

# Preview prefix standardization changes
[group('slot generation')]
preview-prefix-changes:
  uv run python src/valuesets/generators/prefix_standardizer.py src/valuesets/schema --dry-run

# ============== UniProt Species Sync Recipes ==============

# Fetch organisms from GO goex.yaml and cache to JSON
[group('uniprot sync')]
fetch-go-organisms:
  uv run python scripts/fetch_from_go_goex.py --output cache/go_organisms.json

# Fetch common model organisms from UniProt and cache to JSON
[group('uniprot sync')]
fetch-common-organisms:
  uv run python scripts/sync_uniprot_species.py --json-output cache/common_organisms.json --output /dev/null

# Fetch ALL reference proteomes from UniProt and cache to JSON (500+ organisms)
[group('uniprot sync')]
fetch-extended-organisms:
  uv run python scripts/sync_uniprot_species.py --extended --json-output cache/extended_organisms.json --output /dev/null

# Merge all sources into best union for uniprot_species.yaml
[group('uniprot sync')]
merge-uniprot: fetch-go-organisms fetch-common-organisms
  uv run python scripts/merge_uniprot_sources.py

# Full sync workflow: fetch all sources and merge into best union (includes extended)
[group('uniprot sync')]
sync-uniprot-full: fetch-go-organisms fetch-common-organisms fetch-extended-organisms
  uv run python scripts/merge_uniprot_sources.py --extended-organisms cache/extended_organisms.json

# Quick sync workflow: just GO and common organisms (recommended)
[group('uniprot sync')]
sync-uniprot: merge-uniprot

# Show statistics about cached organism sources
[group('uniprot sync')]
uniprot-stats:
  @echo "=== UniProt Species Cache Statistics ==="
  @echo ""
  @if [ -f cache/go_organisms.json ]; then \
    echo "GO organisms: $(grep -c '"code"' cache/go_organisms.json || echo 0)"; \
  else \
    echo "GO organisms: [not cached]"; \
  fi
  @if [ -f cache/common_organisms.json ]; then \
    echo "Common organisms: $(grep -c '"code"' cache/common_organisms.json || echo 0)"; \
  else \
    echo "Common organisms: [not cached]"; \
  fi
  @if [ -f cache/extended_organisms.json ]; then \
    echo "Extended organisms: $(grep -c '"code"' cache/extended_organisms.json || echo 0)"; \
  else \
    echo "Extended organisms: [not cached]"; \
  fi
  @if [ -f src/valuesets/schema/bio/uniprot_species.yaml ]; then \
    echo "Current YAML entries: $(grep -c '^      SP_' src/valuesets/schema/bio/uniprot_species.yaml || echo 0)"; \
  else \
    echo "Current YAML: [not found]"; \
  fi

# Generate CSV report of all enums with mapping statistics
[group('reports')]
enum-report:
  uv run python scripts/generate_enum_report.py
  @echo "Report saved to enum_report.csv"

# ============== Include project-specific recipes ==============

import "python.justfile"
import "project.justfile"
