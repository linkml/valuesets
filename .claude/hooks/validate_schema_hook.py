#!/usr/bin/env python3
"""
Hook to automatically validate LinkML schema files after they are written or edited.
This hook runs `just validate-schema PATH` and displays the results to provide immediate feedback.

**NOTE**

Be sure to exit with code 2 if you want to block the operation.
https://docs.claude.com/en/docs/claude-code/hooks#exit-code-2-behavior
"""

import sys
import json
import subprocess
import os
from pathlib import Path


def main():
    # Read the hook input from stdin
    data = json.load(sys.stdin)

    # Extract the file path from the tool input
    tool_name = data.get("tool_name", "")
    file_path = data.get("tool_input", {}).get("file_path", "")

    # Only process Write and Edit tool calls
    if tool_name not in ["Write", "Edit", "MultiEdit"]:
        sys.exit(0)

    # Check if this is a YAML file in the schema directory
    if not file_path.endswith(".yaml") or "schema" not in file_path:
        sys.exit(0)

    # Convert to Path object for easier manipulation
    file_path = Path(file_path)

    # Check if the file exists (it should after Write/Edit)
    if not file_path.exists():
        print(f"⚠️ File not found: {file_path}", file=sys.stderr)
        sys.exit(0)

    # Run the validation command
    try:
        # Build the validation command
        cmd = ["just", "validate-schema", str(file_path)]

        # Run the command and capture output
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=os.path.dirname(
                os.path.dirname(os.path.dirname(__file__))
            ),  # Project root
        )

        # Display the validation output
        print("\n" + "=" * 60, file=sys.stderr)
        print(f"🔍 Schema Validation Results for {file_path.name}", file=sys.stderr)
        print("=" * 60, file=sys.stderr)

        # Show stdout (the actual validation results)
        if result.stdout:
            # Filter out noise from warning messages
            lines = result.stdout.split("\n")
            filtered_lines = []
            for line in lines:
                # Filter out common noise patterns
                if any(pattern in line for pattern in [
                    "/eutils/__init__.py",
                    "UserWarning",
                    "pkg_resources is deprecated",
                    "RuntimeWarning: 'src.valuesets.validators.enum_evaluator'",
                    "found in sys.modules after import"
                ]):
                    continue
                else:
                    filtered_lines.append(line)

            output = "\n".join(filtered_lines).strip()
            if output:
                print(output, file=sys.stderr)

        # Show any errors
        if result.returncode != 0 and result.stderr:
            # Filter stderr similarly
            lines = result.stderr.split("\n")
            filtered_lines = []
            for line in lines:
                if not any(pattern in line for pattern in [
                    "/eutils/__init__.py",
                    "UserWarning",
                    "pkg_resources is deprecated"
                ]):
                    filtered_lines.append(line)

            error_output = "\n".join(filtered_lines).strip()
            if error_output:
                print("\n⚠️ Schema validation errors:", file=sys.stderr)
                print(error_output, file=sys.stderr)

        print("=" * 60 + "\n", file=sys.stderr)

        # Return non-zero exit code if validation failed
        if result.returncode != 0:
            print("❌ Schema validation failed - blocking file modification", file=sys.stderr)
            print("Fix validation errors before saving the file.", file=sys.stderr)
            sys.exit(2)  # Block the operation

    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to run schema validation: {e}", file=sys.stderr)
        sys.exit(2)  # Block on validation errors
    except Exception as e:
        print(f"❌ Unexpected error during schema validation: {e}", file=sys.stderr)
        # Block on hook failures to ensure schema integrity
        sys.exit(2)

    # Exit 0 if validation passed
    sys.exit(0)


if __name__ == "__main__":
    main()