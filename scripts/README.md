# Scripts Directory

This directory contains scripts for managing and syncing value sets.

## UniProt Species Sync Scripts

### Overview

Three scripts work together to maintain `uniprot_species.yaml` from multiple sources:

1. **`fetch_from_go_goex.py`** - Fetch organisms from GO metadata
2. **`sync_uniprot_species.py`** - Fetch organisms from UniProt API
3. **`merge_uniprot_sources.py`** - Merge all sources into best union

### Quick Usage

Use the justfile commands instead of running scripts directly:

```bash
# Recommended: sync with GO and common organisms
just sync-uniprot

# Full sync with all reference proteomes (500+)
just sync-uniprot-full

# Check current status
just uniprot-stats
```

See [docs/how-to-guides/sync-uniprot-species.md](../docs/how-to-guides/sync-uniprot-species.md) for detailed documentation.

### Scripts Details

#### fetch_from_go_goex.py

Fetches organisms from GO's goex.yaml metadata file.

```bash
uv run python scripts/fetch_from_go_goex.py \
  --output cache/go_organisms.json
```

**Source**: https://github.com/geneontology/go-site/blob/master/metadata/goex.yaml

**Output**: JSON file with organism data including proteome IDs

#### sync_uniprot_species.py

Fetches organisms from UniProt's proteome API.

```bash
# Common model organisms only
uv run python scripts/sync_uniprot_species.py \
  --json-output cache/common_organisms.json \
  --output /dev/null

# All reference proteomes (500+)
uv run python scripts/sync_uniprot_species.py \
  --extended \
  --json-output cache/extended_organisms.json \
  --output /dev/null
```

**Options**:
- `--extended` - Fetch all reference proteomes (default: common organisms only)
- `--json-output` - Save raw data as JSON for merging
- `--output` - Output YAML file (use `/dev/null` to skip YAML generation)
- `--merge` - Merge with existing YAML (default: true)
- `--replace` - Replace instead of merge

#### merge_uniprot_sources.py

Merges multiple organism sources into a single YAML file.

```bash
uv run python scripts/merge_uniprot_sources.py \
  --go-organisms cache/go_organisms.json \
  --common-organisms cache/common_organisms.json \
  --existing src/valuesets/schema/bio/uniprot_species.yaml \
  --output src/valuesets/schema/bio/uniprot_species.yaml
```

**Options**:
- `--go-organisms` - GO organisms JSON
- `--common-organisms` - Common organisms JSON
- `--extended-organisms` - Extended organisms JSON (optional)
- `--existing` - Existing YAML to preserve manual edits
- `--output` - Output YAML file
- `--backup` - Create backup (default: true)

**Merge Strategy**:
1. Load all sources (existing YAML, GO, common, extended)
2. De-duplicate by UniProt mnemonic code
3. Prefer later sources for conflicts
4. Fill in missing fields from any source
5. Track sources for each organism

### Cache Files

Scripts cache data in `cache/` directory:

- `cache/go_organisms.json` - GO organisms (171 entries)
- `cache/common_organisms.json` - Common model organisms (~28 entries)
- `cache/extended_organisms.json` - Extended proteomes (500+ entries)

Cache files are used for faster merging and can be regenerated anytime.

## Other Scripts

### fetch_uniprot_species.py

Older/simpler version of `sync_uniprot_species.py`. Still functional but `sync_uniprot_species.py` is recommended.

### add_ncbitaxon_aliases.py

Adds NCBI Taxonomy aliases to enum entries.

## Development

When adding new sync scripts:

1. Fetch data from source to JSON
2. Add merge logic to `merge_uniprot_sources.py`
3. Add justfile command for convenience
4. Update documentation

See existing scripts as templates.
