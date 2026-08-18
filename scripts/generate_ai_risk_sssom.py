#!/usr/bin/env python3
"""Generate an SSSOM mapping set crosswalking the encoded AI risk taxonomies.

Berman et al. (2026), "Death by a thousand taxonomies?", recommend that
Sociotechnical Outcome Taxonomy (SOT) development "produce explicit mappings to
adjacent SOT (e.g., noting a category maps to X in another scheme or stating it
has no direct equivalent)", supported by stable semantic identifiers and by the
Simple Standard for Sharing Ontological Mappings (SSSOM; Matentzoglu et al.
2022). This script emits exactly that artefact for the taxonomies encoded under
src/valuesets/schema/ai_governance/.

Mappings are declared inline on the permissible values, as annotations:

  mit_air_subdomain:      the MIT AI Risk Repository subdomain code (e.g. "4.2")
  mit_air_mapping_status: a TaxonomyMappingStatusEnum value (e.g. CLOSE_MATCH)
  jigsaw_label:           the corresponding ToxicityClassificationEnum value

Declaring them on the values rather than in a side file keeps the correspondence
with the category it describes, which is the point of the recommendation: the
mapping is part of the artefact, not an accompanying note.

Usage:
    uv run python scripts/generate_ai_risk_sssom.py
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

from linkml_runtime.utils.schemaview import SchemaView

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = REPO_ROOT / "src" / "valuesets" / "schema" / "ai_governance"
OUTPUT = REPO_ROOT / "src" / "valuesets" / "mappings" / "ai_risk_crosswalk.sssom.tsv"

BASE = "https://w3id.org/valuesets"

# TaxonomyMappingStatusEnum -> SSSOM/SKOS predicate.
PREDICATE = {
    "EXACT_MATCH": "skos:exactMatch",
    "CLOSE_MATCH": "skos:closeMatch",
    "BROAD_MATCH": "skos:broadMatch",
    "NARROW_MATCH": "skos:narrowMatch",
    "RELATED_MATCH": "skos:relatedMatch",
    "NO_DIRECT_EQUIVALENT": "sssom:NoTermFound",
}

COLUMNS = [
    "subject_id",
    "subject_label",
    "predicate_id",
    "object_id",
    "object_label",
    "mapping_justification",
    "subject_source",
    "object_source",
    "mapping_tool",
    "confidence",
    "subject_type",
    "object_type",
    "comment",
]

HEADER = """\
#curie_map:
#  skos: "http://www.w3.org/2004/02/skos/core#"
#  sssom: "https://w3id.org/sssom/"
#  semapv: "https://w3id.org/semapv/vocab/"
#  dcterms: "http://purl.org/dc/terms/"
#
#mapping_set_id: https://w3id.org/valuesets/mappings/ai_risk_crosswalk
#mapping_set_title: AI Risk Taxonomy Crosswalk
#mapping_set_description: >-
#  Crosswalk between the AI risk taxonomies encoded in
#  src/valuesets/schema/ai_governance/ - Weidinger et al. (2022), the MIT AI Risk
#  Repository Domain Taxonomy, the content harm categories, and the Jigsaw
#  toxicity label set. Generated from mapping annotations declared inline on the
#  permissible values; do not edit by hand, edit the schemas and regenerate with
#  scripts/generate_ai_risk_sssom.py.
#license: https://creativecommons.org/publicdomain/zero/1.0/
#creator_id: https://github.com/linkml/valuesets
#
"""


def annotation(pv, key: str) -> str | None:
    """Return the string value of a permissible value annotation, or None."""
    annotations = getattr(pv, "annotations", None)
    if not annotations:
        return None
    ann = annotations.get(key)
    if ann is None:
        return None
    value = getattr(ann, "value", ann)
    return str(value) if value is not None else None


def load(module: str) -> SchemaView:
    return SchemaView(str(SCHEMA_DIR / f"{module}.yaml"))


def main() -> int:
    mit = load("mit_ai_risk_repository")
    weidinger = load("weidinger_lm_risks")
    harms = load("content_harms")

    # Index MIT subdomains and domains by their numeric code, so mapping
    # annotations can refer to "4.2" rather than restating the value name.
    mit_by_code: dict[str, tuple[str, str]] = {}
    mit_enum = mit.get_enum("MITAIRiskDomainEnum")
    for name, pv in mit_enum.permissible_values.items():
        code = annotation(pv, "domain_code")
        if code:
            mit_by_code[code] = (name, pv.title or name)

    rows: list[dict[str, str]] = []
    unresolved: list[str] = []

    def emit_mit_mappings(sv_module: str, enum_name: str, enum, default_status: str) -> None:
        for name, pv in enum.permissible_values.items():
            code = annotation(pv, "mit_air_subdomain")
            if not code:
                continue
            target = mit_by_code.get(code)
            if target is None:
                unresolved.append(f"{enum_name}.{name} -> MIT subdomain {code}")
                continue
            status = annotation(pv, "mit_air_mapping_status") or default_status
            predicate = PREDICATE.get(status)
            if predicate is None:
                unresolved.append(f"{enum_name}.{name} -> unknown status {status}")
                continue
            object_name, object_label = target
            rows.append(
                {
                    "subject_id": f"{BASE}/ai_governance/{sv_module}/:{enum_name}.{name}",
                    "subject_label": name,
                    "predicate_id": predicate,
                    "object_id": (
                        f"{BASE}/ai_governance/mit_ai_risk_repository/"
                        f":MITAIRiskDomainEnum.{object_name}"
                    ),
                    "object_label": object_label,
                    "mapping_justification": "semapv:ManualMappingCuration",
                    "subject_source": f"{BASE}/ai_governance/{sv_module}",
                    "object_source": f"{BASE}/ai_governance/mit_ai_risk_repository",
                    "mapping_tool": "linkml-valuesets",
                    "confidence": "",
                    "subject_type": "enum_value",
                    "object_type": "enum_value",
                    "comment": f"MIT AI Risk Repository subdomain {code}",
                }
            )

    emit_mit_mappings(
        "weidinger_lm_risks",
        "WeidingerLMRiskEnum",
        weidinger.get_enum("WeidingerLMRiskEnum"),
        default_status="RELATED_MATCH",
    )

    harm_enum = harms.get_enum("ContentHarmCategoryEnum")
    emit_mit_mappings(
        "content_harms",
        "ContentHarmCategoryEnum",
        harm_enum,
        default_status="NARROW_MATCH",
    )

    # Content harm -> Jigsaw toxicity labels. These are exact by construction:
    # each annotated value is the counterpart of that Jigsaw label.
    for name, pv in harm_enum.permissible_values.items():
        label = annotation(pv, "jigsaw_label")
        if not label:
            continue
        rows.append(
            {
                "subject_id": (
                    f"{BASE}/ai_governance/content_harms/:ContentHarmCategoryEnum.{name}"
                ),
                "subject_label": name,
                "predicate_id": "skos:exactMatch",
                "object_id": (
                    f"{BASE}/data_science/text_classification/"
                    f":ToxicityClassificationEnum.{label}"
                ),
                "object_label": label,
                "mapping_justification": "semapv:ManualMappingCuration",
                "subject_source": f"{BASE}/ai_governance/content_harms",
                "object_source": f"{BASE}/data_science/text_classification",
                "mapping_tool": "linkml-valuesets",
                "confidence": "",
                "subject_type": "enum_value",
                "object_type": "enum_value",
                "comment": "Jigsaw toxic-comment label set counterpart",
            }
        )

    if unresolved:
        for problem in unresolved:
            print(f"ERROR: unresolved mapping: {problem}", file=sys.stderr)
        return 1

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="") as handle:
        handle.write(HEADER)
        writer = csv.DictWriter(handle, fieldnames=COLUMNS, delimiter="\t")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    print(f"Wrote {len(rows)} mappings to {OUTPUT.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
