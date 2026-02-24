# ANALYSIS-EVI-002 — BWB Seat and Restraints Analysis (CS-25.561 / CS-25.562)

**Evidence ID:** T-A-ATA25-BWB-EVI-002
**Type:** Analysis
**Delta Refs:** DELTA-BWB-25-002, DELTA-BWB-25-006
**CS-25 Para:** CS-25.561, CS-25.562
**Status:** OPEN — target LC05
**Parent:** [Evidence README](README.md)

---

## 1) Objective

Demonstrate that BWB passenger and flight-deck seat installations meet CS-25.561
static emergency landing loads and CS-25.562 dynamic seat test requirements using
BWB floor-grid attach geometry and 2D node load introduction.

---

## 2) Analysis Method

| Analysis Type | Method | Tool | Reference |
|--------------|--------|------|-----------|
| CS-25.561 static loads | Linear static FE | TBD (NASTRAN or equivalent) | CS-25.561 load factors |
| CS-25.562 dynamic | Occupant dynamics (Hybrid III) | TBD (MADYMO or equivalent) | CS-25.562 + AMC 25.562 |
| Grid node bearing | Composite joint sub-model | TBD | Node fitting PN bearing data |

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

## 4) BWB-Specific Grid Geometry Inputs

| Parameter | Source | LC Target |
|-----------|--------|-----------|
| Grid node X/Y coordinates | ICD_BWB_FLOOR_GRID_ATTACH_001.md | LC03 |
| Node spacing (fore-aft + lateral) | ICD_BWB_FLOOR_GRID_ATTACH_001.md | LC03 |
| Seat PN and mass | Seat CMM / BOM | LC04 |
| Node fitting PN and rated load | Structures | LC03 |

---

## 5) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Define FE model geometry from ICD data | Stress | LC04 |
| Run CS-25.561/562 load cases with grid model | Stress | LC05 |
| Confirm compliance against limits | Certification | LC05 |

---

## Related Documents

- [ATA25_BWB_COMPLIANCE_MATRIX.md](../ATA25_BWB_COMPLIANCE_MATRIX.md)
- [ICD_BWB_FLOOR_GRID_ATTACH_001.md](../ATA25_BWB_INTERFACES/ICD_BWB_FLOOR_GRID_ATTACH_001.md)
- [REQ_BWB_25_200_PASSENGER_COMPARTMENT.yaml](../ATA25_BWB_REQUIREMENTS/REQ_BWB_25_200_PASSENGER_COMPARTMENT.yaml)
