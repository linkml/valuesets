"""Command-line interface for valuesets."""

import csv
import json
import sys
from contextlib import nullcontext
from enum import Enum
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional, Type

import typer

from valuesets.utils.classifier import classify, detect_classifier_fields

app = typer.Typer(
    name="valuesets",
    help="Command-line tools for working with common value sets.",
    no_args_is_help=True,
)


def load_enum_class(enum_name: str, module: str = "valuesets.enums") -> Type[Enum]:
    """
    Dynamically load an enum class by name.

    Args:
        enum_name: Name of the enum class (e.g., "IPCCLikelihoodScale")
        module: Module path to import from (default: "valuesets.enums")

    Returns:
        The enum class

    Raises:
        typer.BadParameter: If enum cannot be found
    """
    import importlib

    try:
        mod = importlib.import_module(module)
        # Try direct attribute access
        if hasattr(mod, enum_name):
            return getattr(mod, enum_name)

        # Try searching submodules recursively
        for attr_name in dir(mod):
            attr = getattr(mod, attr_name)
            if isinstance(attr, type) and issubclass(attr, Enum) and attr.__name__ == enum_name:
                return attr

        raise typer.BadParameter(f"Enum '{enum_name}' not found in module '{module}'")
    except ImportError as e:
        raise typer.BadParameter(f"Cannot import module '{module}': {e}")


def read_input(
    input_path: Optional[Path],
    input_format: Optional[str]
) -> Iterator[Dict[str, Any]]:
    """
    Read input data from file or stdin.

    Args:
        input_path: Path to input file, or None for stdin
        input_format: Format hint ("csv", "json", "jsonl") or None for auto-detect

    Yields:
        Dict objects from the input
    """
    if input_path is None:
        # Read from stdin
        content = sys.stdin.read()
        if not content.strip():
            return

        # Auto-detect format
        if input_format is None:
            if content.strip().startswith("[") or content.strip().startswith("{"):
                input_format = "json"
            else:
                input_format = "csv"
    else:
        # Read from file
        content = input_path.read_text()
        if input_format is None:
            suffix = input_path.suffix.lower()
            if suffix == ".csv":
                input_format = "csv"
            elif suffix == ".jsonl":
                input_format = "jsonl"
            else:
                input_format = "json"

    if input_format == "csv":
        reader = csv.DictReader(content.splitlines())
        for row in reader:
            # Convert numeric strings to floats where possible
            converted = {}
            for k, v in row.items():
                try:
                    converted[k] = float(v)
                except (ValueError, TypeError):
                    converted[k] = v
            yield converted
    elif input_format == "jsonl":
        for line in content.splitlines():
            line = line.strip()
            if line:
                yield json.loads(line)
    else:  # json
        data = json.loads(content)
        if isinstance(data, list):
            yield from data
        else:
            yield data


def write_output(
    results: List[Dict[str, Any]],
    output_path: Optional[Path],
    output_format: Optional[str],
    input_format: str
) -> None:
    """
    Write output data to file or stdout.

    Args:
        results: List of result dicts
        output_path: Path to output file, or None for stdout
        output_format: Format ("csv", "json", "jsonl") or None to match input
        input_format: Original input format (used if output_format is None)
    """
    if output_format is None:
        if output_path:
            suffix = output_path.suffix.lower()
            if suffix == ".csv":
                output_format = "csv"
            elif suffix == ".jsonl":
                output_format = "jsonl"
            else:
                output_format = "json"
        else:
            output_format = input_format

    if output_format == "csv":
        if not results:
            return
        fieldnames = list(results[0].keys())
        cm = nullcontext(sys.stdout) if output_path is None else open(output_path, "w", newline="")
        with cm as output:
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
    elif output_format == "jsonl":
        cm = nullcontext(sys.stdout) if output_path is None else open(output_path, "w")
        with cm as output:
            for row in results:
                output.write(json.dumps(row) + "\n")
    else:  # json
        content = json.dumps(results, indent=2)
        if output_path:
            output_path.write_text(content)
        else:
            print(content)


@app.command("classify")
def classify_cmd(
    enum_name: str = typer.Argument(
        ...,
        help="Name of the enum to classify against (e.g., 'IPCCLikelihoodScale')"
    ),
    input_file: Optional[Path] = typer.Option(
        None,
        "--input", "-i",
        help="Input file path. Reads from stdin if not provided."
    ),
    output_file: Optional[Path] = typer.Option(
        None,
        "--output", "-o",
        help="Output file path. Writes to stdout if not provided."
    ),
    field: Optional[str] = typer.Option(
        None,
        "--field", "-f",
        help="Field name to classify on. Auto-detects if not provided."
    ),
    output_field: str = typer.Option(
        "enum_value",
        "--output-field",
        help="Name of the output field for classification results."
    ),
    module: str = typer.Option(
        "valuesets.enums",
        "--module", "-m",
        help="Python module containing the enum class."
    ),
    input_format: Optional[str] = typer.Option(
        None,
        "--input-format",
        help="Input format: csv, json, jsonl. Auto-detects if not provided."
    ),
    output_format: Optional[str] = typer.Option(
        None,
        "--output-format",
        help="Output format: csv, json, jsonl. Matches input if not provided."
    ),
    all_matches: bool = typer.Option(
        True,
        "--all-matches/--first-match",
        help="Return all matching values (default) or just the first."
    ),
    inclusive: bool = typer.Option(
        True,
        "--inclusive/--exclusive",
        help="Use inclusive (default) or exclusive range bounds."
    ),
) -> None:
    """
    Classify objects against an enum's range annotations.

    Reads objects from CSV, JSON, or JSONL input, classifies each object
    against the specified enum, and outputs the objects with an added
    classification field.

    Examples:

        # Classify probabilities using IPCCLikelihoodScale
        echo '[{"probability": 0.95}]' | valuesets classify IPCCLikelihoodScale

        # From CSV file, output to JSON
        valuesets classify BMICategory -i data.csv -o results.json -f bmi

        # Use custom enum from different module
        valuesets classify MyEnum -m mypackage.enums -i data.jsonl
    """
    # Load the enum class
    enum_class = load_enum_class(enum_name, module)

    # Determine detected format for matching output
    detected_format = input_format or "json"
    if input_file and input_format is None:
        suffix = input_file.suffix.lower()
        if suffix == ".csv":
            detected_format = "csv"
        elif suffix == ".jsonl":
            detected_format = "jsonl"
        else:
            detected_format = "json"

    # If field not provided, try to detect from enum
    if field is None:
        detected_fields = detect_classifier_fields(enum_class)
        if detected_fields:
            typer.echo(
                f"Auto-detected classifier field(s): {', '.join(sorted(detected_fields))}",
                err=True
            )

    # Process input
    results = []
    for obj in read_input(input_file, input_format):
        matches = classify(obj, enum_class, field=field, inclusive=inclusive)

        if matches:
            if all_matches:
                # Store all match names as comma-separated or list
                match_names = [m.name for m in matches]
                if detected_format == "json" or detected_format == "jsonl":
                    obj[output_field] = match_names
                else:
                    obj[output_field] = ",".join(match_names)
            else:
                obj[output_field] = matches[0].name
        else:
            obj[output_field] = None if detected_format != "csv" else ""

        results.append(obj)

    # Write output
    write_output(results, output_file, output_format, detected_format)


@app.command()
def list_enums(
    module: str = typer.Option(
        "valuesets.enums",
        "--module", "-m",
        help="Python module to search for enums."
    ),
    classifiable_only: bool = typer.Option(
        False,
        "--classifiable-only", "-c",
        help="Only show enums with classifier annotations."
    ),
) -> None:
    """
    List available enums in a module.

    Shows all enum classes available for classification, optionally
    filtering to only those with range annotations.
    """
    import importlib

    try:
        mod = importlib.import_module(module)
    except ImportError as e:
        typer.echo(f"Cannot import module '{module}': {e}", err=True)
        raise typer.Exit(1)

    enums_found = []
    for attr_name in dir(mod):
        attr = getattr(mod, attr_name)
        if isinstance(attr, type) and issubclass(attr, Enum) and attr is not Enum:
            if classifiable_only:
                fields = detect_classifier_fields(attr)
                if fields:
                    enums_found.append((attr_name, sorted(fields)))
            else:
                fields = detect_classifier_fields(attr)
                enums_found.append((attr_name, sorted(fields) if fields else None))

    if not enums_found:
        typer.echo("No enums found.", err=True)
        raise typer.Exit(1)

    for name, fields in sorted(enums_found):
        if fields:
            typer.echo(f"{name} (fields: {', '.join(fields)})")
        else:
            typer.echo(name)


@app.command()
def inspect(
    enum_name: str = typer.Argument(
        ...,
        help="Name of the enum to inspect"
    ),
    module: str = typer.Option(
        "valuesets.enums",
        "--module", "-m",
        help="Python module containing the enum class."
    ),
) -> None:
    """
    Inspect an enum's classifier configuration.

    Shows the enum's permissible values and their range annotations.
    """
    from valuesets.utils.classifier import get_classifier_config, get_range_annotations

    enum_class = load_enum_class(enum_name, module)

    # Show enum-level config
    config = get_classifier_config(enum_class)
    if config:
        typer.echo("Enum configuration:")
        typer.echo(f"  {json.dumps(config, indent=2)}")
        typer.echo()

    # Detect fields
    fields = detect_classifier_fields(enum_class)
    if fields:
        typer.echo(f"Detected classifier fields: {', '.join(sorted(fields))}")
        typer.echo()

    # Show each member's ranges
    typer.echo("Permissible values:")
    for member in enum_class:
        typer.echo(f"  {member.name}:")
        if fields:
            for field in sorted(fields):
                min_val, max_val = get_range_annotations(member, field)
                if min_val is not None or max_val is not None:
                    min_str = str(min_val) if min_val is not None else "-inf"
                    max_str = str(max_val) if max_val is not None else "+inf"
                    typer.echo(f"    {field}: [{min_str}, {max_str}]")


def main():
    """Entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()
