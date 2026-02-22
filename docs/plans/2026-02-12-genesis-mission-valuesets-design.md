# Genesis Mission Valuesets Coverage Design

## Context

The DOE Genesis Mission defines 26 national science and technology challenges.
Four BER (Biological and Environmental Research) lighthouse concepts provide
deeper detail: GEO-AI, AI-Driven Living Mine, Change, and G2P.

This design adds valuesets coverage for all 26 challenges using a tiered
depth approach, organized into the existing domain-based directory structure.

## Tiering

### Tier 1 (Deep) - BER lighthouses + adjacent

| Challenge | New Schema Files |
|---|---|
| GEO-AI lighthouse | `earth_science/subsurface.yaml`, `earth_science/hydrogeology.yaml`, `earth_science/remote_sensing.yaml` |
| AI-Driven Living Mine lighthouse | `bio/biogeochemistry.yaml`, `industry/unconventional_resources.yaml` |
| Change lighthouse | `bio/stress_response.yaml`, `bio/microbial_ecology.yaml`, `bio/synthetic_biology.yaml` |
| G2P lighthouse | `bio/omics_data_types.yaml`, `bio/enzyme_function.yaml` |
| #3 Biotechnology Revolution | `bioprocessing/biomanufacturing.yaml` |
| #4 Critical Minerals Supply | (covered by Living Mine + existing mining enums) |
| #14 Autonomous Labs | `lab_automation/autonomous_labs.yaml` |
| #17 Water for Energy | `earth_science/water_resources.yaml` |
| #19 Subsurface Energy Assets | `energy/subsurface_energy.yaml` |

### Tier 2 (Moderate) - extensions to existing domains

| Challenge | New Schema Files |
|---|---|
| #1 Advanced Manufacturing | `industry/manufacturing.yaml` |
| #5 Nuclear Energy | (covered by existing 46 nuclear enums) |
| #6 Fusion Energy | `energy/nuclear/fusion.yaml` |
| #7 Nuclear Cleanup | `energy/nuclear/nuclear_cleanup.yaml` |
| #12 Materials Discovery | `materials_science/computational_materials.yaml` |
| #13 Materials Design | (covered by #12 + existing materials_science enums) |
| #18 Grid Scaling | `energy/grid.yaml` |

### Tier 3 (Light) - 1-2 enums each

| Challenge | New Schema Files |
|---|---|
| #2 Buildings | `industry/construction.yaml` |
| #8-9 Quantum | `computing/quantum.yaml` |
| #10 Microelectronics | `computing/microelectronics.yaml` |
| #11 Data Centers | `computing/data_centers.yaml` |
| #15-16 Physics | `physics/particle_physics.yaml` |
| #20-26 Nuclear Security | `energy/nuclear/nuclear_forensics.yaml` |

## Estimated New Enums

- Tier 1: ~40-50 new enums across 13 files
- Tier 2: ~15-20 new enums across 5 files
- Tier 3: ~8-12 new enums across 6 files
- Total: ~65-80 new enums

## Conventions

- Follow existing pattern: CamelCase enum names, UPPER_CASE permissible values
- Use `meaning:` with OBO CURIEs where possible (verify via OLS)
- All enums get `status: DRAFT`, contributor ORCID, and `valuesets_meta:ValueSetEnumDefinition`
- Schema IDs use `https://w3id.org/valuesets/{path}`
- New files must be added to `valuesets.yaml` imports
