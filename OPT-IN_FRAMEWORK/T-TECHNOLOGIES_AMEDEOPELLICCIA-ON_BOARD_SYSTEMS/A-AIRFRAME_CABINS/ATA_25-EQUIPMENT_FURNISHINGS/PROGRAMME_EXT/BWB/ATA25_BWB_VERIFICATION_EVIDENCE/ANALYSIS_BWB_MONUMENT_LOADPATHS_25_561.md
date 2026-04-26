# ANALYSIS-EVI-001 — BWB Monument Load Path Analysis (CS-25.561)

**Evidence ID:** T-A-ATA25-BWB-EVI-001
**Type:** Analysis
**Delta Ref:** DELTA-BWB-25-003
**CS-25 Para:** CS-25.561
**Status:** OPEN — target LC05
**Parent:** [Evidence README](README.md)

---

## 1) Objective

Demonstrate that BWB galley, lavatory, and other monument installations meet CS-25.561
static emergency landing loads using BWB composite torque-box structural model and
floor-grid/soffit attach geometry.

BWB monument attach philosophy (grid nodes + overhead soffit reaction) differs from
WTW sill fitting and overhead strongback. The load paths must be separately analysed
for the BWB configuration.

---

## 2) Analysis Method

| Analysis Type | Method | Tool | Reference |
|--------------|--------|------|-----------|
| CS-25.561 static emergency loads | Linear static FE | TBD (NASTRAN or equivalent) | CS-25.561 load factors |
| Floor grid node local stress | Composite joint FE | TBD | Grid fitting PN bearing/pull-through |
| Overhead soffit fitting | Linear static FE sub-model | TBD | Soffit fitting PN TBD |

---

## 3) Load Cases (CS-25.561)

| Direction | Load Factor | Condition |
|-----------|------------|-----------|
| Forward | 9g | Emergency landing |
| Sideward | 3g | Emergency landing |
| Downward | 6g | Emergency landing |
| Upward | 3g | Emergency landing |
| Rearward | 1.5g | Emergency landing |

---

## 4) BWB-Specific Geometry Inputs

| Parameter | Source | LC Target |
|-----------|--------|-----------|
| Floor grid node coordinates | ICD_BWB_FLOOR_GRID_ATTACH_001.md | LC03 |
| Spar-web fitting coordinates (lateral) | ICD_BWB_MONUMENT_INTERFACES_001.md | LC03 |
| Overhead soffit fitting coordinates | ICD_BWB_MONUMENT_INTERFACES_001.md | LC03 |
| Monument mass and CG | Monument CMM / BOM | LC04 |

---

## 5) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Build FE sub-model with BWB grid/soffit geometry | Stress | LC04 |
| Run CS-25.561 load cases | Stress | LC05 |
| Review compliance — confirm limits met | Certification | LC05 |

---

## Related Documents

- [ATA25_BWB_COMPLIANCE_MATRIX.md](../ATA25_BWB_COMPLIANCE_MATRIX.md)
- [ICD_BWB_MONUMENT_INTERFACES_001.md](../ATA25_BWB_INTERFACES/ICD_BWB_MONUMENT_INTERFACES_001.md)
