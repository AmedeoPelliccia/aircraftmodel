# TDF 8-Bit Register Encoding Standard — BWB Blend Zone

**Doc ID:** T-A-ATA57-BWB-BLEND-ENC-001  
**Status:** DRAFT  
**Applies to:** AMPEL360 BWB — ATA 57 Wings — Blend Zone TDF

---

## 1. Purpose

This document defines the encoding standard for the Topological Design Field (TDF) used in the
BWB blend zone. Each TDF patch is assigned an 8-bit integer register (value 0–255) that encodes
a normalised structural parameter. This encoding enables discrete optimisation of the continuous
structural field using a Genetic Algorithm (GA) with integer chromosome representation.

---

## 2. Physical Parameter Mapping

The 8-bit register encodes a **normalised structural thickness parameter** `t_norm`:

```
t_norm = t_min + r × Δt
```

Where:
- `r` — register value (integer, 0–255)
- `t_min` — minimum patch thickness (TBD mm, to be defined at DDR-57-BWB)
- `Δt` — step size = (t_max − t_min) / 255

**Resolution:** 256 discrete values → approximately 0.4% of the full range per step.

For composites, the physical parameter is the **nominal laminate thickness** (sum of ply thicknesses).
An aliasing table maps register values to standard ply-count combinations from the approved material
database (see ATA 20 `STANDARDS_MATERIALS.md`).

---

## 3. Boundary Conditions

The following patch registers are **FIXED** (not subject to optimisation):

| Register Class          | Constraint            | Reason                                          |
|-------------------------|-----------------------|-------------------------------------------------|
| `HARD_POINT_SPAR`       | r = 255 (t_max)       | Spar carry-through load introduction            |
| `HARD_POINT_PRESSURE`   | r = 255 (t_max)       | Pressure floor attach region                    |
| `HARD_POINT_SYSTEMS`    | r ≥ 128               | Systems routing hard-point clearance envelope   |
| `BOUNDARY_EDGE`         | r = r_adjacent ± 32   | Compatibility with adjacent structural zone     |

---

## 4. Version-Freeze Rule

When the TDF register map is released at DDR-57-BWB gate (LC57-03), the register values are
version-frozen. Subsequent changes require a delta change entry in `../ATA57_BWB_BLEND_DELTA_LOG.yaml`
and Engineering approval. Each frozen register map version is identified by a SHA-256 hash.

---

## 5. Register Map Format

The register map is stored as a YAML file (see `MODELS/tdf_register_map.example.yaml`).
Machine-readable fields per patch:

```yaml
patch_id: string       # unique patch identifier (e.g. BZ-P001)
region: string         # blend_zone | spar_carry_through | systems_bay
register: integer      # 0–255
fixed: boolean         # true if boundary condition applies
hash_input: boolean    # true if included in SHA-256 governance hash
```
