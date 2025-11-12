# How to Sync UniProt Species Data

This guide explains how to keep the `uniprot_species.yaml` enum synchronized with multiple authoritative sources.

## Overview

The UniProt species enum is built from multiple sources:
1. **GO goex.yaml** - Organisms used in Gene Ontology annotations (171 organisms)
2. **Common model organisms** - Curated list of frequently used research organisms (~28 organisms)
3. **Extended proteomes** - All UniProt reference proteomes (500+ organisms, optional)
4. **Existing entries** - Any manually curated entries preserved during sync

## Quick Start

### Recommended Workflow

To sync with GO organisms and common model organisms (recommended):

```bash
just sync-uniprot
```

This will:
1. Fetch organisms from GO goex.yaml
2. Fetch common model organisms from UniProt
3. Merge with existing entries
4. Generate updated `src/valuesets/schema/bio/uniprot_species.yaml`

### Full Sync (with Extended Proteomes)

To include all 500+ reference proteomes:

```bash
just sync-uniprot-full
```

⚠️ **Warning**: This fetches many organisms and takes longer!

## Available Commands

### Individual Source Fetching

Fetch organisms from specific sources:

```bash
# Fetch from GO goex.yaml
just fetch-go-organisms

# Fetch common model organisms
just fetch-common-organisms

# Fetch all reference proteomes (500+)
just fetch-extended-organisms
```

These commands save data to JSON files in the `cache/` directory for later merging.

### Merging

Merge all available sources:

```bash
just merge-uniprot
```

This merges:
- Existing YAML entries
- GO organisms (if cached)
- Common organisms (if cached)
- Extended organisms (if cached and specified)

### Statistics

View current cache status:

```bash
just uniprot-stats
```

Output example:
```
=== UniProt Species Cache Statistics ===

GO organisms: 171
Common organisms: 28
Extended organisms: [not cached]
Current YAML entries: 294
```

## How the Merge Works

The merge strategy prioritizes data completeness:

1. **De-duplication**: By UniProt mnemonic code
2. **Preference**: Later sources override earlier ones
3. **Completeness**: Empty fields are filled from any source
4. **Source tracking**: Each organism tracks which sources contributed data

### Merge Priority (lowest to highest)

1. Existing YAML entries (baseline)
2. Common organisms
3. GO organisms (highest priority)
4. Extended organisms (if included)

## File Locations

### Scripts

- `scripts/fetch_from_go_goex.py` - Fetch GO organisms
- `scripts/sync_uniprot_species.py` - Fetch UniProt organisms
- `scripts/merge_uniprot_sources.py` - Merge all sources

### Cache

- `cache/go_organisms.json` - GO organisms cache
- `cache/common_organisms.json` - Common organisms cache
- `cache/extended_organisms.json` - Extended organisms cache (optional)

### Output

- `src/valuesets/schema/bio/uniprot_species.yaml` - Generated YAML schema
- `src/valuesets/schema/bio/uniprot_species.yaml.bak` - Automatic backup

## Manual Usage

### Fetch GO Organisms

```bash
uv run python scripts/fetch_from_go_goex.py \
  --output cache/go_organisms.json
```

### Fetch Common Organisms

```bash
uv run python scripts/sync_uniprot_species.py \
  --json-output cache/common_organisms.json \
  --output /dev/null
```

### Fetch Extended Organisms

```bash
uv run python scripts/sync_uniprot_species.py \
  --extended \
  --json-output cache/extended_organisms.json \
  --output /dev/null
```

### Merge Sources

```bash
uv run python scripts/merge_uniprot_sources.py \
  --go-organisms cache/go_organisms.json \
  --common-organisms cache/common_organisms.json \
  --existing src/valuesets/schema/bio/uniprot_species.yaml \
  --output src/valuesets/schema/bio/uniprot_species.yaml
```

With extended organisms:

```bash
uv run python scripts/merge_uniprot_sources.py \
  --extended-organisms cache/extended_organisms.json
```

## Verification

After syncing, verify the results:

```bash
# Check the generated YAML
just validate

# Rebuild and check documentation
just site

# Run tests
just test
```

## Data Sources

### GO goex.yaml

- URL: https://github.com/geneontology/go-site/blob/master/metadata/goex.yaml
- Contains: Organisms used in GO annotations
- Fields: taxon_id, full_name, code_uniprot, uniprot_proteome_id, common_name_uniprot

### UniProt Reference Proteomes

- API: https://rest.uniprot.org/proteomes/search
- Filter: `proteome_type:1` (reference proteomes only)
- Coverage: 500+ organisms with curated, representative proteomes

## Troubleshooting

### "No organisms found"

Check that sources are cached:
```bash
just uniprot-stats
```

If not cached, run individual fetch commands.

### "Missing proteome IDs"

Some organisms may not have reference proteomes. This is expected and logged as warnings.

### Merge conflicts

The merge script automatically resolves conflicts by preferring:
1. Non-empty values over empty
2. Longer, more descriptive names
3. Later sources over earlier

## Example Results

Before sync: 159 organisms
After sync with GO: 294 organisms (159 + 171 - duplicates)

The union includes:
- All GO organisms (for annotation compatibility)
- All common model organisms
- Any manually curated entries
- De-duplicated and enriched with latest proteome IDs
