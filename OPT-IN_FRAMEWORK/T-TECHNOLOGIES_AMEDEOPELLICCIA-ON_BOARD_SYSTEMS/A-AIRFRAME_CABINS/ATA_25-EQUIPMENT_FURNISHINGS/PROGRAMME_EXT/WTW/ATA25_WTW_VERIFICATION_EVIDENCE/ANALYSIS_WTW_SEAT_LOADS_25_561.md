# ANALYSIS-EVI-002 — WTW Seat Load Analysis (CS-25.561 / CS-25.562)

**Evidence ID:** T-A-ATA25-WTW-EVI-002
**Type:** Analysis
**Delta Refs:** DELTA-WTW-25-001, DELTA-WTW-25-002
**CS-25 Para:** CS-25.561, CS-25.562
**Status:** OPEN — target LC05
**Parent:** [Evidence README](README.md)

---

## 1) Objective

Demonstrate that WTW passenger and flight-deck seat installations meet CS-25.561
static emergency landing loads and CS-25.562 dynamic seat test requirements using
WTW-variant seat track geometry and floor load introduction points.

---

## 2) Analysis Method

| Analysis Type | Method | Tool | Reference |
|--------------|--------|------|-----------|
| CS-25.561 static loads | Linear static FE | TBD (NASTRAN or equivalent) | CS-25.561 load factors |
| CS-25.562 dynamic | Occupant dynamics (Hybrid III dummy) | TBD (MADYMO or equivalent) | CS-25.562 + AMC 25.562 |

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

## 4) WTW-Specific Geometry Inputs

| Parameter | Source | LC Target |
|-----------|--------|-----------|
| Seat track Y-coordinates | ICD_WTW_ATTACH_POINTS_001.md | LC03 |
| Floor beam spacing | ATA 53 fuselage ICD | LC03 |
| Seat PN and mass | Seat CMM / BOM | LC04 |
| Sill fitting PN and rated load | ATA 53 | LC03 |

---

## 5) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Define FE model geometry from ICD data | Stress | LC04 |
| Run analysis and document results | Stress | LC05 |
| Review against CS-25.561/562 limits | Certification | LC05 |

---

## Related Documents

- [ATA25_WTW_COMPLIANCE_MATRIX.md](../ATA25_WTW_COMPLIANCE_MATRIX.md)
- [ICD_WTW_ATTACH_POINTS_001.md](../ATA25_WTW_INTERFACES/ICD_WTW_ATTACH_POINTS_001.md)
- [REQ_WTW_25_100_FLT_COMPARTMENT.yaml](../ATA25_WTW_REQUIREMENTS/REQ_WTW_25_100_FLT_COMPARTMENT.yaml)
- [REQ_WTW_25_200_PASS_COMPARTMENT.yaml](../ATA25_WTW_REQUIREMENTS/REQ_WTW_25_200_PASS_COMPARTMENT.yaml)
