# Slot Generation for Value Set Enums

This repository includes utilities to automatically generate LinkML slots for every enum defined in the schemas. This ensures that for every enum `FooBarEnum`, there's a corresponding slot `foo_bar` with range `FooBarEnum`.

## Utilities Available

### 1. `auto_slot_injector.py` - Basic Slot Generation

Simple utility for generating slot definitions from enums.

```bash
# Preview slots for a single schema
uv run python src/valuesets/generators/auto_slot_injector.py schema.yaml --mode preview

# Generate comprehensive slots file for all schemas
uv run python src/valuesets/generators/auto_slot_injector.py src/valuesets/schema --mode generate --output generated_slots.yaml

# Inject slots into a specific schema
uv run python src/valuesets/generators/auto_slot_injector.py schema.yaml --mode inject --output modified.yaml
```

### 2. `smart_slot_syncer.py` - Intelligent Synchronization

Advanced utility designed for periodic synchronization with `--in-place` modifications.

## Key Behaviors for `--in-place` Usage

### Sync Modes

1. **`update` (default)** - Smart updates preserving manual customizations
2. **`refresh`** - Regenerate all enum-based slots
3. **`conservative`** - Only add new slots, never modify existing

### Customization Detection

The syncer automatically detects manual customizations and preserves them:

**Auto-preserved customizations:**
- `required: true`
- `identifier: true`
- Validation constraints (`pattern`, `minimum_value`, etc.)
- Additional fields (`domain`, `subproperty_of`, etc.)
- Comments containing "manual", "custom", or "do not modify"

**Example of protected slot:**
```yaml
mineralogy_feedstock:
  description: Types of mineral feedstock sources...
  range: MineralogyFeedstockClass
  required: true  # Manual customization - preserved
  comments:
    - "Required field for mining operation records"
    - "Manual customization - do not modify"  # Protection marker
```

### Periodic Sync Scenarios

#### First Run - Add Slots
```bash
# Add slots to schema for first time
uv run python src/valuesets/generators/smart_slot_syncer.py schema.yaml --in-place

# Result: Adds all missing slots for enums
# ✓ Added: 10 new slots
# ✓ Preserved: 0 (none existed)
```

#### Subsequent Runs - Preserve Existing
```bash
# Run again - no changes needed
uv run python src/valuesets/generators/smart_slot_syncer.py schema.yaml --in-place

# Result: No modifications
# ✓ Preserved: 10 existing slots
# ✓ Added: 0 (all exist)
```

#### New Enum Added
```yaml
# Add new enum to schema
enums:
  NewProcessType:
    permissible_values:
      ENHANCED: {}
      STANDARD: {}
```

```bash
# Sync picks up new enum
uv run python src/valuesets/generators/smart_slot_syncer.py schema.yaml --in-place

# Result: Adds slot for new enum only
# ✓ Added: 1 (new_process_type)
# ✓ Preserved: 10 (existing slots unchanged)
```

#### Enum Renamed
```yaml
# Enum renamed in schema
enums:
  MineralogyFeedstockType:  # Was: MineralogyFeedstockClass
```

```bash
# Smart sync detects range update needed
uv run python src/valuesets/generators/smart_slot_syncer.py schema.yaml --in-place

# Result: Updates range but preserves customizations
# ✓ Updated: 1 (mineralogy_feedstock range only)
# ⚠ Warning: Updated range MineralogyFeedstockClass → MineralogyFeedstockType, preserved customizations
```

#### Enum Deleted with Cleanup
```bash
# Remove orphaned slots for deleted enums
uv run python src/valuesets/generators/smart_slot_syncer.py schema.yaml --in-place --remove-orphans

# Result: Removes slots for deleted enums (unless customized)
# ✓ Removed: 2 (orphaned slots)
# ⚠ Warning: old_custom_slot: Orphaned slot with customizations (manual review needed)
```

### Batch Processing

Process all schemas in a directory:

```bash
# Sync all schemas at once
uv run python src/valuesets/generators/smart_slot_syncer.py src/valuesets/schema --batch --in-place

# Result: Processes all .yaml files
# Batch Summary: 15 files modified
#   Total added: 127
#   Total updated: 3
#   Total removed: 0
```

### Audit Trail

Track changes with changelog:

```bash
# Generate with audit trail
uv run python src/valuesets/generators/smart_slot_syncer.py schema.yaml --in-place --changelog changes.json -v

# changes.json contains:
[
  {
    "timestamp": "2025-10-02T18:30:22.123456",
    "change": "ADD: mineralogy_feedstock (range: MineralogyFeedstockClass)"
  },
  {
    "timestamp": "2025-10-02T18:30:22.124567",
    "change": "UPDATE: old_slot range: OldEnum → NewEnum"
  }
]
```

## Best Practices for Periodic Sync

### 1. Development Workflow
```bash
# After adding/modifying enums, sync slots
uv run python src/valuesets/generators/smart_slot_syncer.py schema.yaml --in-place

# Preview changes first if unsure
uv run python src/valuesets/generators/smart_slot_syncer.py schema.yaml --dry-run -v
```

### 2. CI/CD Integration
```bash
# In CI pipeline - ensure slots are in sync
uv run python src/valuesets/generators/smart_slot_syncer.py src/valuesets/schema --batch --dry-run

# Exit with error if slots are out of sync
# (Add --in-place to auto-fix in CI)
```

### 3. Protecting Manual Customizations
```yaml
# Mark slots that should not be auto-updated
my_custom_slot:
  description: "Manually crafted slot"
  range: MyEnum
  required: true
  comments:
    - "Custom validation logic - do not modify"
```

### 4. Major Refactoring
```bash
# For major enum reorganization, use refresh mode
uv run python src/valuesets/generators/smart_slot_syncer.py schema.yaml --in-place --mode refresh

# Then manually restore any needed customizations
```

## Slot Naming Convention

| Enum Name | Generated Slot Name |
|-----------|-------------------|
| `StatusEnum` | `status` |
| `MineralogyFeedstockClass` | `mineralogy_feedstock` |
| `BioticInteractionType` | `biotic_interaction` |
| `ProcessPerformanceMetric` | `process_performance_metric` |

- Removes common suffixes: `Enum`, `Type`, `Class`, `Code`
- Converts CamelCase to snake_case
- Multivalued detection for: `target`, `feature`, `metric`, `constraint` patterns

## Integration with LinkML Ecosystem

The generated slots can be used in classes:

```yaml
classes:
  MiningOperation:
    description: A mining operation record
    slots:
      - mineralogy_feedstock    # References MineralogyFeedstockClass enum
      - beneficiation_pathway   # References BeneficiationPathway enum
      - extractable_target_element  # Multivalued, references ExtractableTargetElement enum
```

This provides type safety and validation while maintaining the flexibility of LinkML schemas.