#!/bin/bash
for i in {1..10}; do
    echo "=== Pass $i ==="
    python scripts/add_ncbitaxon_aliases.py 2>&1 | tail -2
    count=$(uv run python -m src.valuesets.validators.enum_evaluator src/valuesets/schema --no-cache 2>/dev/null | grep -c "uniprot_species.yaml")
    echo "Remaining errors: $count"
    if [ "$count" -eq 0 ]; then
        echo "All validation errors fixed!"
        break
    fi
done