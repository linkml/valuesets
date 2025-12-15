"""Classifier utilities for enum values based on numeric range annotations."""

import re
from enum import Enum
from typing import Any, Dict, List, Optional, Set, Tuple, Type, Union


# Patterns for detecting classifier fields from annotation names
_RANGE_PATTERN = re.compile(r"^(.+)_range$")
_MIN_PATTERN = re.compile(r"^minimum_(.+)$")
_MAX_PATTERN = re.compile(r"^maximum_(.+)$")


def detect_classifier_fields(enum_class: Type[Enum]) -> Set[str]:
    """
    Detect classifiable fields from an enum's annotations.

    Scans all enum members' annotations for patterns like:
    - {field}_range (e.g., probability_range -> "probability")
    - minimum_{field} (e.g., minimum_score -> "score")
    - maximum_{field} (e.g., maximum_score -> "score")

    Args:
        enum_class: A RichEnum class with range annotations

    Returns:
        Set of detected field names

    Examples:
        >>> from valuesets.generators.rich_enum import RichEnum

        >>> class TestEnum(RichEnum):
        ...     A = "A"
        ...     B = "B"
        >>> TestEnum._metadata = {
        ...     "A": {"annotations": {"probability_range": "0.9-1.0"}},
        ...     "B": {"annotations": {"minimum_score": "0.5", "maximum_score": "0.9"}}
        ... }

        >>> sorted(detect_classifier_fields(TestEnum))
        ['probability', 'score']

        Empty enum returns empty set:
        >>> class EmptyAnnotations(RichEnum):
        ...     X = "X"
        >>> EmptyAnnotations._metadata = {"X": {"annotations": {}}}
        >>> detect_classifier_fields(EmptyAnnotations)
        set()
    """
    fields: Set[str] = set()

    for member in enum_class:
        annotations: Dict[str, Any] = {}
        if hasattr(member, 'get_annotations'):
            annotations = member.get_annotations() or {}

        for key in annotations:
            # Check for {field}_range pattern
            match = _RANGE_PATTERN.match(key)
            if match:
                fields.add(match.group(1))
                continue

            # Check for minimum_{field} pattern
            match = _MIN_PATTERN.match(key)
            if match:
                fields.add(match.group(1))
                continue

            # Check for maximum_{field} pattern
            match = _MAX_PATTERN.match(key)
            if match:
                fields.add(match.group(1))

    return fields


def get_classifier_config(enum_class: Type[Enum]) -> Dict[str, Any]:
    """
    Get enum-level classifier configuration.

    Looks for classifier config in enum's _enum_metadata attribute.
    The config can specify:
    - classifier_field: default field name for classification
    - annotation_mappings: map non-standard annotation names to fields/bounds

    Args:
        enum_class: A RichEnum class

    Returns:
        Dict with classifier configuration, or empty dict if none

    Examples:
        >>> from valuesets.generators.rich_enum import RichEnum

        >>> class ConfiguredEnum(RichEnum):
        ...     A = "A"
        >>> ConfiguredEnum._enum_metadata = {
        ...     "classifier_field": "probability",
        ...     "annotation_mappings": {
        ...         "min_prob": {"field": "probability", "bound": "minimum"},
        ...         "max_prob": {"field": "probability", "bound": "maximum"}
        ...     }
        ... }

        >>> config = get_classifier_config(ConfiguredEnum)
        >>> config["classifier_field"]
        'probability'

        No config returns empty dict:
        >>> class PlainEnum(RichEnum):
        ...     X = "X"
        >>> get_classifier_config(PlainEnum)
        {}
    """
    return getattr(enum_class, '_enum_metadata', {})


def parse_range(range_str: str) -> Tuple[Optional[float], Optional[float]]:
    """
    Parse a range string into (min, max) tuple.

    Supports formats:
    - Standard ranges: "0.99-1.00", "18.5-24.9"
    - Unbounded below: "<18.5", "<=18.5"
    - Unbounded above: ">40.0", ">=40.0"
    - Negative numbers: "-5-62" (means -5 to 62)
    - With units (ignored): ">10000 L", "0.1-10 %"

    Args:
        range_str: A string representing a numeric range

    Returns:
        Tuple of (minimum, maximum) floats. None indicates unbounded.

    Examples:
        Standard ranges:
        >>> parse_range("0.99-1.00")
        (0.99, 1.0)

        >>> parse_range("18.5-24.9")
        (18.5, 24.9)

        >>> parse_range("0.00-0.33")
        (0.0, 0.33)

        Unbounded ranges:
        >>> parse_range("<18.5")
        (None, 18.5)

        >>> parse_range("<=18.5")
        (None, 18.5)

        >>> parse_range(">40.0")
        (40.0, None)

        >>> parse_range(">=40.0")
        (40.0, None)

        With units (stripped):
        >>> parse_range(">10000 L")
        (10000.0, None)

        >>> parse_range("0.1-10 %")
        (0.1, 10.0)

        Edge cases:
        >>> parse_range("")
        (None, None)

        >>> parse_range("invalid")
        (None, None)

        >>> parse_range("abc-def")
        (None, None)

        Negative numbers:
        >>> parse_range("-5-62")
        (-5.0, 62.0)

        >>> parse_range("-10--5")
        (-10.0, -5.0)
    """
    if not range_str or not isinstance(range_str, str):
        return (None, None)

    range_str = range_str.strip()

    # Handle prefix operators: <=, <, >=, >
    if range_str.startswith("<="):
        match = re.match(r"<=\s*(-?[\d.]+)", range_str)
        if match:
            try:
                return (None, float(match.group(1)))
            except ValueError:
                pass
        return (None, None)
    elif range_str.startswith("<"):
        match = re.match(r"<\s*(-?[\d.]+)", range_str)
        if match:
            try:
                return (None, float(match.group(1)))
            except ValueError:
                pass
        return (None, None)
    elif range_str.startswith(">="):
        match = re.match(r">=\s*(-?[\d.]+)", range_str)
        if match:
            try:
                return (float(match.group(1)), None)
            except ValueError:
                pass
        return (None, None)
    elif range_str.startswith(">"):
        match = re.match(r">\s*(-?[\d.]+)", range_str)
        if match:
            try:
                return (float(match.group(1)), None)
            except ValueError:
                pass
        return (None, None)

    # Handle range format: min-max
    # Pattern: optional negative, digits with optional decimal, hyphen,
    # optional negative, digits with optional decimal
    # Use lookahead to handle negative second number: -10--5
    match = re.match(r"(-?[\d.]+)\s*-\s*(-?[\d.]+)", range_str)
    if match:
        try:
            min_val = float(match.group(1))
            max_val = float(match.group(2))
            return (min_val, max_val)
        except ValueError:
            return (None, None)

    return (None, None)


def get_range_annotations(
    enum_member: Enum,
    field: str,
    annotation_mappings: Optional[Dict[str, Dict[str, str]]] = None
) -> Tuple[Optional[float], Optional[float]]:
    """
    Extract numeric range from an enum member's annotations.

    Looks for annotations in this order of precedence:
    1. Custom annotation_mappings (if provided)
    2. Separate min/max: minimum_{field} and maximum_{field}
    3. Combined range: {field}_range

    Args:
        enum_member: A RichEnum member with annotations
        field: The field name (e.g., "probability", "bmi", "age_years")
        annotation_mappings: Optional dict mapping annotation names to
            {"field": str, "bound": "minimum"|"maximum"} for non-standard names

    Returns:
        Tuple of (minimum, maximum) floats. None indicates unbounded.

    Examples:
        >>> from enum import Enum
        >>> from valuesets.generators.rich_enum import RichEnum

        >>> class TestEnum(RichEnum):
        ...     VALUE1 = "VALUE1"
        ...     VALUE2 = "VALUE2"
        >>> TestEnum._metadata = {
        ...     "VALUE1": {"annotations": {"probability_range": "0.66-1.00"}},
        ...     "VALUE2": {"annotations": {"minimum_score": "0.5", "maximum_score": "0.9"}}
        ... }

        Combined range annotation:
        >>> get_range_annotations(TestEnum.VALUE1, "probability")
        (0.66, 1.0)

        Separate min/max annotations:
        >>> get_range_annotations(TestEnum.VALUE2, "score")
        (0.5, 0.9)

        Missing annotation:
        >>> get_range_annotations(TestEnum.VALUE1, "nonexistent")
        (None, None)

        Standard enum without annotations:
        >>> from enum import Enum
        >>> class PlainEnum(Enum):
        ...     A = "A"
        >>> get_range_annotations(PlainEnum.A, "field")
        (None, None)

        Custom annotation mappings:
        >>> class CustomEnum(RichEnum):
        ...     X = "X"
        >>> CustomEnum._metadata = {
        ...     "X": {"annotations": {"lo": "10", "hi": "20"}}
        ... }
        >>> mappings = {
        ...     "lo": {"field": "value", "bound": "minimum"},
        ...     "hi": {"field": "value", "bound": "maximum"}
        ... }
        >>> get_range_annotations(CustomEnum.X, "value", annotation_mappings=mappings)
        (10.0, 20.0)
    """
    annotations: Dict[str, Any] = {}
    if hasattr(enum_member, 'get_annotations'):
        annotations = enum_member.get_annotations() or {}

    # Check custom annotation mappings first
    if annotation_mappings:
        min_val: Optional[float] = None
        max_val: Optional[float] = None
        for annot_name, mapping in annotation_mappings.items():
            if mapping.get("field") != field:
                continue
            if annot_name in annotations:
                try:
                    val = float(annotations[annot_name])
                    if mapping.get("bound") == "minimum":
                        min_val = val
                    elif mapping.get("bound") == "maximum":
                        max_val = val
                except (ValueError, TypeError):
                    pass
        if min_val is not None or max_val is not None:
            return (min_val, max_val)

    # Try separate min/max annotations
    min_key = f"minimum_{field}"
    max_key = f"maximum_{field}"
    if min_key in annotations or max_key in annotations:
        try:
            min_val = float(annotations[min_key]) if min_key in annotations else None
            max_val = float(annotations[max_key]) if max_key in annotations else None
            return (min_val, max_val)
        except (ValueError, TypeError):
            pass

    # Fall back to combined range annotation
    range_key = f"{field}_range"
    if range_key in annotations:
        return parse_range(str(annotations[range_key]))

    return (None, None)


def classify(
    obj: Union[Dict[str, Any], Any],
    enum_class: Type[Enum],
    field: Optional[str] = None,
    inclusive: bool = True
) -> List[Enum]:
    """
    Classify an object to matching enum permissible values based on numeric ranges.

    Given an object with a numeric field value and an enum with range annotations,
    returns all permissible values whose ranges contain the object's value.

    Args:
        obj: A dict or object with the field to classify. If an object (like pydantic),
             uses getattr to access the field.
        enum_class: A RichEnum class with range annotations on its members
        field: The field name to use for classification (e.g., "probability", "bmi").
               If None, auto-detects from:
               1. Enum's _enum_metadata["classifier_field"]
               2. First field detected from annotation patterns
        inclusive: If True (default), range bounds are inclusive (<=, >=).
                   If False, bounds are exclusive (<, >).

    Returns:
        List of enum members whose ranges contain the object's field value.
        Returns empty list if:
        - Object doesn't have the field
        - Field value is None or not numeric
        - No enum members have matching range annotations
        - No field could be detected

    Examples:
        >>> from valuesets.generators.rich_enum import RichEnum

        Create a test enum with range annotations:
        >>> class ScoreLevel(RichEnum):
        ...     HIGH = "HIGH"
        ...     MEDIUM = "MEDIUM"
        ...     LOW = "LOW"
        >>> ScoreLevel._metadata = {
        ...     "HIGH": {"annotations": {"score_range": "0.7-1.0"}},
        ...     "MEDIUM": {"annotations": {"score_range": "0.3-0.7"}},
        ...     "LOW": {"annotations": {"score_range": "0.0-0.3"}}
        ... }

        Basic classification with explicit field:
        >>> classify({"score": 0.8}, ScoreLevel, field="score")
        [<ScoreLevel.HIGH: 'HIGH'>]

        Auto-detect field from annotations (field is optional):
        >>> classify({"score": 0.8}, ScoreLevel)
        [<ScoreLevel.HIGH: 'HIGH'>]

        >>> classify({"score": 0.5}, ScoreLevel)
        [<ScoreLevel.MEDIUM: 'MEDIUM'>]

        >>> classify({"score": 0.1}, ScoreLevel)
        [<ScoreLevel.LOW: 'LOW'>]

        Boundary value (inclusive by default - matches both):
        >>> classify({"score": 0.7}, ScoreLevel)
        [<ScoreLevel.HIGH: 'HIGH'>, <ScoreLevel.MEDIUM: 'MEDIUM'>]

        Boundary value with exclusive bounds:
        >>> classify({"score": 0.7}, ScoreLevel, inclusive=False)
        []

        Missing field returns empty list:
        >>> classify({"other": 0.8}, ScoreLevel, field="score")
        []

        Non-numeric field returns empty list:
        >>> classify({"score": "high"}, ScoreLevel)
        []

        None value returns empty list:
        >>> classify({"score": None}, ScoreLevel)
        []

        Object attribute access (pydantic/dataclass style):
        >>> class Measurement:
        ...     def __init__(self, score):
        ...         self.score = score
        >>> classify(Measurement(0.8), ScoreLevel)
        [<ScoreLevel.HIGH: 'HIGH'>]

        Create enum with separate min/max annotations:
        >>> class BMICategory(RichEnum):
        ...     UNDERWEIGHT = "UNDERWEIGHT"
        ...     NORMAL = "NORMAL"
        ...     OVERWEIGHT = "OVERWEIGHT"
        >>> BMICategory._metadata = {
        ...     "UNDERWEIGHT": {"annotations": {"maximum_bmi": "18.5"}},
        ...     "NORMAL": {"annotations": {"minimum_bmi": "18.5", "maximum_bmi": "25.0"}},
        ...     "OVERWEIGHT": {"annotations": {"minimum_bmi": "25.0"}}
        ... }

        >>> classify({"bmi": 17.0}, BMICategory)
        [<BMICategory.UNDERWEIGHT: 'UNDERWEIGHT'>]

        >>> classify({"bmi": 22.0}, BMICategory)
        [<BMICategory.NORMAL: 'NORMAL'>]

        >>> classify({"bmi": 30.0}, BMICategory)
        [<BMICategory.OVERWEIGHT: 'OVERWEIGHT'>]

        Boundary includes both categories:
        >>> classify({"bmi": 18.5}, BMICategory)
        [<BMICategory.UNDERWEIGHT: 'UNDERWEIGHT'>, <BMICategory.NORMAL: 'NORMAL'>]

        Enum with classifier_field in _enum_metadata:
        >>> class ProbEnum(RichEnum):
        ...     HIGH = "HIGH"
        ...     LOW = "LOW"
        >>> ProbEnum._metadata = {
        ...     "HIGH": {"annotations": {"p_range": "0.5-1.0"}},
        ...     "LOW": {"annotations": {"p_range": "0.0-0.5"}}
        ... }
        >>> ProbEnum._enum_metadata = {"classifier_field": "p"}
        >>> classify({"p": 0.8}, ProbEnum)
        [<ProbEnum.HIGH: 'HIGH'>]

        Custom annotation mappings via _enum_metadata:
        >>> class CustomEnum(RichEnum):
        ...     A = "A"
        ...     B = "B"
        >>> CustomEnum._metadata = {
        ...     "A": {"annotations": {"lo": "0", "hi": "50"}},
        ...     "B": {"annotations": {"lo": "50", "hi": "100"}}
        ... }
        >>> CustomEnum._enum_metadata = {
        ...     "classifier_field": "value",
        ...     "annotation_mappings": {
        ...         "lo": {"field": "value", "bound": "minimum"},
        ...         "hi": {"field": "value", "bound": "maximum"}
        ...     }
        ... }
        >>> classify({"value": 25}, CustomEnum)
        [<CustomEnum.A: 'A'>]
        >>> classify({"value": 75}, CustomEnum)
        [<CustomEnum.B: 'B'>]
    """
    # Get enum-level config
    enum_config = get_classifier_config(enum_class)
    annotation_mappings = enum_config.get("annotation_mappings")

    # Determine field to use
    if field is None:
        # Try enum-level classifier_field first
        field = enum_config.get("classifier_field")

        # Fall back to auto-detection from annotations
        if field is None:
            detected_fields = detect_classifier_fields(enum_class)
            if detected_fields:
                # Use first detected field that exists in obj
                for candidate in detected_fields:
                    if isinstance(obj, dict):
                        if candidate in obj:
                            field = candidate
                            break
                    elif hasattr(obj, candidate):
                        field = candidate
                        break

                # If no match in obj, just use first detected
                if field is None and detected_fields:
                    field = next(iter(detected_fields))

    if field is None:
        return []

    # Extract value from object
    if isinstance(obj, dict):
        value = obj.get(field)
    else:
        value = getattr(obj, field, None)

    # Validate value is numeric
    if value is None:
        return []
    if not isinstance(value, (int, float)):
        return []

    results = []
    for member in enum_class:
        min_val, max_val = get_range_annotations(member, field, annotation_mappings)

        # Skip members without range annotations
        if min_val is None and max_val is None:
            continue

        # Check if value is in range
        in_range = True
        if inclusive:
            if min_val is not None and value < min_val:
                in_range = False
            if max_val is not None and value > max_val:
                in_range = False
        else:
            if min_val is not None and value <= min_val:
                in_range = False
            if max_val is not None and value >= max_val:
                in_range = False

        if in_range:
            results.append(member)

    return results


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
