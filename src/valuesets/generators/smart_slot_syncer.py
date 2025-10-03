#!/usr/bin/env python3
"""
Smart slot synchronizer for LinkML schemas with enums.

Designed for periodic synchronization with --in-place option to:
1. Add new slots for newly added enums
2. Update slot ranges when enum names change
3. Preserve manual customizations to slots
4. Remove orphaned slots for deleted enums (optional)
5. Track changes for review
"""

import yaml
from pathlib import Path
from typing import Dict, Any, List, Optional, Set, Tuple
import re
import click
from collections import OrderedDict
from datetime import datetime
import json


class SmartSlotSyncer:
    """Intelligent slot synchronization for enum-based schemas."""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.changes = []  # Track all changes made

    @staticmethod
    def camel_to_snake(name: str) -> str:
        """Convert CamelCase to snake_case."""
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def generate_slot_name(self, enum_name: str) -> str:
        """Generate slot name from enum name."""
        slot_name = enum_name
        for suffix in ['Enum', 'Type', 'Class', 'Code']:
            if slot_name.endswith(suffix):
                slot_name = slot_name[:-len(suffix)]
                break
        return self.camel_to_snake(slot_name)

    def generate_slot_definition(self, enum_name: str,
                                enum_def: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a complete slot definition for an enum."""
        slot_name = self.generate_slot_name(enum_name)

        # Extract description from enum
        enum_desc = enum_def.get('description', '')
        if enum_desc:
            enum_desc = ' '.join(enum_desc.split())
            first_sentence = enum_desc.split('.')[0]
            slot_desc = first_sentence[:1].upper() + first_sentence[1:] if first_sentence else ''
        else:
            readable_name = slot_name.replace('_', ' ')
            slot_desc = f"The {readable_name} classification"

        slot_def = {
            'description': slot_desc,
            'range': enum_name
        }

        # Check if should be multivalued
        if any(keyword in slot_name for keyword in ['target', 'feature', 'metric', 'constraint']):
            slot_def['multivalued'] = True

        return slot_def

    def detect_changes(self, existing_slot: Dict[str, Any],
                      new_slot: Dict[str, Any]) -> List[str]:
        """Detect what changed between existing and new slot definitions."""
        changes = []

        # Check range change (enum rename)
        if existing_slot.get('range') != new_slot.get('range'):
            changes.append(f"range: {existing_slot.get('range')} → {new_slot.get('range')}")

        # Check multivalued change
        if existing_slot.get('multivalued') != new_slot.get('multivalued'):
            changes.append(f"multivalued: {existing_slot.get('multivalued')} → {new_slot.get('multivalued')}")

        # Check if description was auto-generated and enum description changed
        if (not existing_slot.get('_manual_description') and
            existing_slot.get('description') != new_slot.get('description')):
            changes.append("description updated from enum")

        return changes

    def has_manual_customizations(self, slot_def: Dict[str, Any]) -> bool:
        """
        Detect if a slot has manual customizations beyond auto-generation.

        Checks for:
        - Additional fields beyond basic ones
        - Comments indicating manual edit
        - Complex constraints
        """
        auto_fields = {'description', 'range', 'multivalued', 'comments'}
        manual_indicators = [
            'required', 'identifier', 'pattern', 'minimum_value', 'maximum_value',
            'equals_string', 'equals_number', 'minimum_cardinality', 'maximum_cardinality',
            'annotations', 'see_also', 'examples', 'in_subset', 'domain', 'subproperty_of',
            'symmetric', 'transitive', 'reflexive', 'locally_reflexive', 'irreflexive',
            'asymmetric', 'inverse', 'is_a', 'mixins'
        ]

        # Check for manual indicator fields
        for field in slot_def.keys():
            if field in manual_indicators:
                return True

        # Check for manual edit markers in comments
        if 'comments' in slot_def:
            for comment in slot_def['comments']:
                if any(marker in comment.lower() for marker in ['manual', 'custom', 'do not modify']):
                    return True

        return False

    def sync_slots(self, schema_path: Path,
                   mode: str = 'update',
                   remove_orphans: bool = False,
                   dry_run: bool = False) -> Dict[str, Any]:
        """
        Synchronize slots with enums in a schema.

        Args:
            schema_path: Path to the schema file
            mode: 'update' (preserve customizations), 'refresh' (regenerate all), 'conservative' (only add new)
            remove_orphans: Remove slots for deleted enums
            dry_run: Preview changes without modifying file

        Returns:
            Summary of changes made
        """
        # Load schema
        with open(schema_path, 'r') as f:
            schema_data = yaml.safe_load(f)

        if 'enums' not in schema_data:
            return {'status': 'no_enums', 'changes': []}

        # Initialize slots if needed
        if 'slots' not in schema_data:
            schema_data['slots'] = {}

        # Track changes
        summary = {
            'added': [],
            'updated': [],
            'preserved': [],
            'removed': [],
            'warnings': []
        }

        # Get current enum-based slots
        enum_names = set(schema_data['enums'].keys())
        expected_slots = {}
        enum_to_slot = {}

        # Generate expected slots from enums
        for enum_name, enum_def in schema_data['enums'].items():
            slot_name = self.generate_slot_name(enum_name)
            expected_slots[slot_name] = self.generate_slot_definition(enum_name, enum_def)
            enum_to_slot[enum_name] = slot_name

        # Process each expected slot
        for slot_name, new_slot_def in expected_slots.items():
            existing_slot = schema_data['slots'].get(slot_name)

            if not existing_slot:
                # New slot - add it
                schema_data['slots'][slot_name] = new_slot_def
                summary['added'].append(slot_name)
                self.log_change(f"ADD: {slot_name} (range: {new_slot_def['range']})")

            elif mode == 'conservative':
                # Conservative mode - only add new, never modify existing
                summary['preserved'].append(slot_name)

            elif mode == 'refresh':
                # Refresh mode - regenerate all
                schema_data['slots'][slot_name] = new_slot_def
                summary['updated'].append(slot_name)
                self.log_change(f"REFRESH: {slot_name}")

            else:  # mode == 'update' (default)
                # Smart update - preserve customizations
                if self.has_manual_customizations(existing_slot):
                    # Has manual customizations - only update range if enum renamed
                    if existing_slot.get('range') != new_slot_def['range']:
                        # Enum was renamed - update range but preserve other fields
                        old_range = existing_slot.get('range')
                        existing_slot['range'] = new_slot_def['range']
                        summary['updated'].append(f"{slot_name} (range only)")
                        summary['warnings'].append(
                            f"{slot_name}: Updated range {old_range} → {new_slot_def['range']}, preserved customizations"
                        )
                        self.log_change(f"UPDATE: {slot_name} range: {old_range} → {new_slot_def['range']}")
                    else:
                        summary['preserved'].append(slot_name)
                else:
                    # No manual customizations - safe to update
                    changes = self.detect_changes(existing_slot, new_slot_def)
                    if changes:
                        schema_data['slots'][slot_name] = new_slot_def
                        summary['updated'].append(f"{slot_name} ({', '.join(changes)})")
                        self.log_change(f"UPDATE: {slot_name} - {', '.join(changes)}")
                    else:
                        summary['preserved'].append(slot_name)

        # Handle orphaned slots (slots for deleted enums)
        if remove_orphans:
            current_slots = set(schema_data['slots'].keys())
            expected_slot_names = set(expected_slots.keys())

            for slot_name in current_slots:
                slot_def = schema_data['slots'][slot_name]
                # Check if this slot references an enum that no longer exists
                if (slot_def.get('range') in enum_names or
                    slot_name in expected_slot_names):
                    continue  # Slot is valid

                # Check if it might be enum-related
                if any(slot_def.get('range', '').endswith(suffix)
                       for suffix in ['Enum', 'Type', 'Class']):
                    if self.has_manual_customizations(slot_def):
                        summary['warnings'].append(
                            f"{slot_name}: Orphaned slot with customizations (range: {slot_def.get('range')})"
                        )
                    else:
                        del schema_data['slots'][slot_name]
                        summary['removed'].append(slot_name)
                        self.log_change(f"REMOVE: {slot_name} (orphaned, range: {slot_def.get('range')})")

        # Write changes if not dry run
        if not dry_run:
            self.write_schema(schema_data, schema_path)

        return summary

    def write_schema(self, schema_data: Dict[str, Any], output_path: Path):
        """Write schema preserving key order and formatting."""
        key_order = [
            'name', 'title', 'description', 'id', 'version', 'status',
            'imports', 'prefixes', 'default_prefix', 'default_curi_maps',
            'slots', 'classes', 'enums'
        ]

        ordered_data = OrderedDict()
        for key in key_order:
            if key in schema_data:
                ordered_data[key] = schema_data[key]

        for key in schema_data:
            if key not in ordered_data:
                ordered_data[key] = schema_data[key]

        with open(output_path, 'w') as f:
            yaml.dump(dict(ordered_data), f,
                     default_flow_style=False,
                     sort_keys=False,
                     allow_unicode=True,
                     width=120)

    def log_change(self, message: str):
        """Log a change for audit trail."""
        self.changes.append({
            'timestamp': datetime.now().isoformat(),
            'change': message
        })
        if self.verbose:
            print(f"  {message}")

    def save_changelog(self, path: Path):
        """Save the changelog to a file."""
        with open(path, 'w') as f:
            json.dump(self.changes, f, indent=2)


@click.command()
@click.argument('schema_path', type=click.Path(exists=True, path_type=Path))
@click.option('--in-place', '-i', is_flag=True,
              help='Modify schema file in place')
@click.option('--mode', '-m',
              type=click.Choice(['update', 'refresh', 'conservative']),
              default='update',
              help='Sync mode: update (smart), refresh (regenerate), conservative (only add)')
@click.option('--remove-orphans', '-r', is_flag=True,
              help='Remove slots for deleted enums')
@click.option('--dry-run', '-n', is_flag=True,
              help='Preview changes without modifying files')
@click.option('--verbose', '-v', is_flag=True,
              help='Show detailed change information')
@click.option('--changelog', '-c', type=click.Path(path_type=Path),
              help='Save detailed changelog to file')
@click.option('--batch', '-b', is_flag=True,
              help='Process all schemas in directory')
def main(schema_path: Path, in_place: bool, mode: str,
         remove_orphans: bool, dry_run: bool, verbose: bool,
         changelog: Optional[Path], batch: bool):
    """
    Smart synchronization of LinkML slots with enums.

    Designed for periodic updates with --in-place option.

    Modes:
    - update: Smart updates preserving manual customizations (default)
    - refresh: Regenerate all enum-based slots
    - conservative: Only add new slots, never modify existing

    Examples:

    \b
    # Preview changes for a single file
    smart_slot_syncer.py schema.yaml --dry-run -v

    \b
    # Update file in place, preserving customizations
    smart_slot_syncer.py schema.yaml --in-place

    \b
    # Refresh all slots and remove orphans
    smart_slot_syncer.py schema.yaml --in-place --mode refresh --remove-orphans

    \b
    # Batch process all schemas in directory
    smart_slot_syncer.py src/valuesets/schema --batch --in-place

    \b
    # Conservative update with changelog
    smart_slot_syncer.py schema.yaml --in-place --mode conservative --changelog changes.json
    """
    syncer = SmartSlotSyncer(verbose=verbose)

    if batch and schema_path.is_dir():
        # Batch process all schemas
        yaml_files = list(schema_path.rglob("*.yaml"))
        total_summary = {
            'files_processed': 0,
            'total_added': 0,
            'total_updated': 0,
            'total_removed': 0
        }

        for yaml_file in yaml_files:
            # Skip meta files
            if yaml_file.name in ['linkml-meta.yaml', 'types.yaml',
                                 'slot_mixins.yaml', 'generated_slots.yaml']:
                continue

            print(f"\nProcessing {yaml_file.relative_to(schema_path)}...")

            if in_place or dry_run:
                summary = syncer.sync_slots(yaml_file, mode=mode,
                                           remove_orphans=remove_orphans,
                                           dry_run=dry_run)

                if summary.get('added') or summary.get('updated') or summary.get('removed'):
                    total_summary['files_processed'] += 1
                    total_summary['total_added'] += len(summary.get('added', []))
                    total_summary['total_updated'] += len(summary.get('updated', []))
                    total_summary['total_removed'] += len(summary.get('removed', []))

                    print(f"  Added: {len(summary.get('added', []))}")
                    print(f"  Updated: {len(summary.get('updated', []))}")
                    print(f"  Preserved: {len(summary.get('preserved', []))}")
                    print(f"  Removed: {len(summary.get('removed', []))}")

                    if summary.get('warnings'):
                        print("  Warnings:")
                        for warning in summary['warnings']:
                            print(f"    - {warning}")

        print(f"\n{'='*50}")
        print(f"Batch Summary: {total_summary['files_processed']} files modified")
        print(f"  Total added: {total_summary['total_added']}")
        print(f"  Total updated: {total_summary['total_updated']}")
        print(f"  Total removed: {total_summary['total_removed']}")

    else:
        # Single file processing
        if not in_place and not dry_run:
            print("Error: Must use either --in-place or --dry-run")
            return

        summary = syncer.sync_slots(schema_path, mode=mode,
                                   remove_orphans=remove_orphans,
                                   dry_run=dry_run)

        # Print summary
        print(f"\n{'DRY RUN - ' if dry_run else ''}Summary for {schema_path.name}:")
        print(f"  Mode: {mode}")
        print(f"  Added: {len(summary.get('added', []))}")
        if verbose and summary.get('added'):
            for item in summary['added']:
                print(f"    + {item}")

        print(f"  Updated: {len(summary.get('updated', []))}")
        if verbose and summary.get('updated'):
            for item in summary['updated']:
                print(f"    ~ {item}")

        print(f"  Preserved: {len(summary.get('preserved', []))}")
        if verbose and summary.get('preserved'):
            for item in summary['preserved']:
                print(f"    = {item}")

        print(f"  Removed: {len(summary.get('removed', []))}")
        if verbose and summary.get('removed'):
            for item in summary['removed']:
                print(f"    - {item}")

        if summary.get('warnings'):
            print("\nWarnings:")
            for warning in summary['warnings']:
                print(f"  ⚠ {warning}")

    # Save changelog if requested
    if changelog and syncer.changes:
        syncer.save_changelog(changelog)
        print(f"\nChangelog saved to {changelog}")


if __name__ == '__main__':
    main()