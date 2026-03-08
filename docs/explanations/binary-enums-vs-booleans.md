# Prefer Binary Enums Over Booleans

When modeling data that has two possible states, it may be tempting to use a boolean type (`true`/`false`). However, in many cases, a two-element enumeration (binary enum) is the better choice. This document explains why and when to prefer binary enums over booleans in your LinkML schemas.

## The Case for Binary Enums

The [Tidy Design Principles](https://design.tidyverse.org/boolean-strategies.html) from the tidyverse project articulate several compelling reasons to prefer enums even when there are only two choices.

### 1. Extensibility

If you later discover a third (or fourth, or fifth) option, you'll need to change the interface. With an enum, adding new values is straightforward. With a boolean, you face a breaking change.

**Example:** Consider a data submission status. You might initially think "submitted" or "not submitted" covers it:

```yaml
# Boolean approach - seems simple at first
slots:
  is_submitted:
    range: boolean
```

But what about "pending review", "rejected", or "withdrawn"? With a boolean, you're stuck. With an enum, you simply add new values:

```yaml
# Enum approach - extensible
enums:
  SubmissionStatus:
    permissible_values:
      SUBMITTED:
      NOT_SUBMITTED:
      PENDING_REVIEW:   # Easy to add later
      REJECTED:         # Easy to add later
```

### 2. Clarity of Intent

Boolean values often have asymmetric clarity. `something = TRUE` tells you what *will* happen, but `something = FALSE` only tells you what *won't* happen, not what will happen instead.

**Example from tidyverse:** The `sort()` function uses `decreasing = TRUE/FALSE`. Reading `decreasing = FALSE` leaves ambiguity:
- Does it mean "sort in increasing order"?
- Or does it mean "don't sort at all"?

Compare this with `vctrs::vec_sort()` which uses `direction = "asc"` or `direction = "desc"`. Both options are explicit and self-documenting.

### 3. Avoiding Cryptic Negations

Boolean parameters often require mental gymnastics to interpret, especially with negated names.

**Example from tidyverse:** The `cut()` function has a `right` parameter:
- `right = TRUE`: right-closed, left-open intervals `(a, b]`
- `right = FALSE`: right-open, left-closed intervals `[a, b)`

A clearer design would be `open_side = c("right", "left")` or `bounds = c("[)", "(]")`.

### 4. Self-Documenting Code

Enums make data and code more readable without needing to consult documentation.

```yaml
# What does this mean? Need to check docs.
sample:
  is_control: false

# Self-explanatory
sample:
  sample_type: EXPERIMENTAL
```

### 5. The "Name the Scale" Pattern

When converting booleans to enums, consider naming the scale with values that represent points on it. This signals that intermediate values could be added.

**Example:** Instead of `verbose = TRUE/FALSE`, use:

```yaml
enums:
  VerbosityLevel:
    permissible_values:
      NONE:
        description: No output
      MINIMAL:
        description: Errors only
      NORMAL:
        description: Standard output
      VERBOSE:
        description: Detailed output
      DEBUG:
        description: All available information
```

## When Booleans Are Acceptable

Booleans remain appropriate in certain cases:

1. **Truly binary states**: The states are fundamentally and permanently binary (e.g., physical properties like "alive/dead" in certain contexts)

2. **Well-named parameters**: The parameter name makes both states crystal clear (e.g., `include_header` where `false` clearly means "exclude header")

3. **Toggle operations**: When the operation is clearly about enabling/disabling something (`enabled = true/false`)

## LinkML Examples

### Binary Enum Pattern

```yaml
enums:
  SortDirection:
    permissible_values:
      ASCENDING:
        description: Sort from lowest to highest
        meaning: SIO:001395  # ascending order
      DESCENDING:
        description: Sort from highest to lowest
        meaning: SIO:001396  # descending order

  StrandOrientation:
    permissible_values:
      FORWARD:
        description: Forward/plus strand
        meaning: SO:0000853  # forward_strand
      REVERSE:
        description: Reverse/minus strand
        meaning: SO:0000854  # reverse_strand

  PresenceStatus:
    permissible_values:
      PRESENT:
        description: The entity is present
      ABSENT:
        description: The entity is absent
      NOT_DETERMINED:
        description: Presence could not be determined
```

### Applying to Slots

```yaml
slots:
  sort_direction:
    range: SortDirection
    description: Direction for sorting results

  strand:
    range: StrandOrientation
    description: DNA strand orientation

  presence:
    range: PresenceStatus
    description: Whether the feature was detected
```

## Summary

| Aspect | Boolean | Binary Enum |
|--------|---------|-------------|
| Extensibility | Poor - breaking change to add states | Good - add new values easily |
| Clarity | Often asymmetric | Both values explicit |
| Documentation | Requires external docs | Self-documenting |
| Ontology mapping | Not possible | Supports `meaning` annotations |
| Future-proofing | Risky | Safe |

When in doubt, prefer a two-element enum. The small additional effort pays dividends in clarity, maintainability, and extensibility.

## References

- [Tidy Design Principles: Prefer an enum, even if only two choices](https://design.tidyverse.org/boolean-strategies.html)
- [Tidy Design Principles: Explicit Strategies](https://design.tidyverse.org/explicit-strategies.html)
- [Tidy Design Principles: Extract strategies into objects](https://design.tidyverse.org/strategy-objects.html)
