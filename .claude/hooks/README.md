# Claude Code Hooks

This directory contains hooks that integrate with Claude Code to provide automated validation and other features.

## validate_schema_hook.py

This hook automatically validates LinkML schema files when they are written or edited using Claude Code.

### Features
- Automatically runs validation when saving YAML files in the schema directory
- Blocks file modifications if validation fails
- Shows detailed validation output in the Claude Code interface
- Filters out noise from warning messages for cleaner output
- Uses the project's `just validate-schema PATH` command for validation

### How it works
1. Intercepts Write, Edit, and MultiEdit operations on YAML files containing "schema" in the path
2. Runs the validation command: `just validate-schema <file>`
3. Displays validation results with filtered output for readability
4. Returns exit code 2 to block the operation if validation fails

### Validation Command
The hook uses the existing `just validate-schema PATH` command which:
- Validates ontology mappings in enum definitions
- Checks for label mismatches between expected and actual ontology terms
- Uses the configured OAK adapters for strict validation of configured prefixes
- Treats label mismatches as errors for configured ontologies (NCIT, GO, CHEBI, etc.)

### Configuration
The hook is configured in `.claude/settings.json` as a PostToolUse hook that runs after Write, Edit, and MultiEdit operations.

### Testing
You can test the hook by editing any schema file and seeing if validation runs automatically. The hook will:
- ✅ Allow valid schema modifications
- ❌ Block invalid schema modifications with validation errors
- 📋 Show helpful validation output including ontology label mismatches

### Exit Codes
- **Exit 0**: Validation passed, allow operation
- **Exit 2**: Validation failed, block operation (see [Claude Code hooks documentation](https://docs.claude.com/en/docs/claude-code/hooks#exit-code-2-behavior))