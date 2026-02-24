# ICD-003 — BWB Monument Structural Interfaces

**ICD ID:** T-A-ATA25-BWB-ICD-003
**Delta Ref:** DELTA-BWB-25-003
**ATA Subchapter:** 25-30 Galleys, 25-40 Lavatories
**Status:** DRAFT (LC01 — interface data at LC03)
**Interfaces With:** ATA 53 (Composite Torque-Box Attach), ATA 38 (Water/Waste), ATA 26 (Fire)

---

## 1) Purpose

Defines BWB-specific structural interfaces for galleys, lavatories, and other monuments.

In the BWB, monuments cannot attach to a conventional cylindrical fuselage wall or overhead
strongback running along a tube axis. Instead, monuments must load into:
- **Floor grid nodes** (primary vertical/forward load)
- **Spar web fittings** (lateral reaction for lateral load events)
- **Crown soffit fittings** (overhead reaction for large galleys, where applicable)

---

## 2) Monument Attach Options

| Attach Type | Condition | Structure Interface | Notes |
|-------------|-----------|---------------------|-------|
| Floor grid only | Monument mass ≤ TBD kg | Grid node fittings (ICD-002) | Preferred for lavatory units |
| Floor + overhead soffit | Monument mass > TBD kg | Grid nodes + crown soffit PN TBD | Required for full galleys |
| Floor + spar lateral | Wide monument spanning bay boundary | Grid nodes + spar-web fitting PN TBD | Coordinate with ATA 53 |

---

## 3) Load Introduction (Preliminary — CS-25.561)

| Monument | Floor vertical | Floor forward | Overhead vertical | Spar lateral | Reference |
|----------|---------------|--------------|------------------|-------------|-----------|
| Standard galley | TBD kN | TBD kN | TBD kN | TBD kN | CS-25.561 |
| Lavatory | TBD kN | TBD kN | — | — | CS-25.561 |
| Crew rest module | TBD kN | TBD kN | TBD kN | TBD kN | CS-25.561 |

---

## 4) Fire Zone Boundary

Each spar bay is a separate fire zone. Monument installation SHALL NOT compromise fire
zone separation (ATA 26 coordination required for any penetrations through spar structure).

---

## 5) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Define spar-web fitting PN and locations | Structures | LC03 |
| Monument load path analysis with FE model | Loads / Stress | LC05 |
| Fire zone penetration sign-off (ATA 26) | Systems / Certification | LC04 |

---

## Related Documents

- [ICD_LIST.yaml](ICD_LIST.yaml)
- [ANALYSIS_BWB_MONUMENT_LOADPATHS_25_561.md](../ATA25_BWB_VERIFICATION_EVIDENCE/ANALYSIS_BWB_MONUMENT_LOADPATHS_25_561.md)
- [REQ_BWB_25_300_GALLEYS.yaml](../ATA25_BWB_REQUIREMENTS/REQ_BWB_25_300_GALLEYS.yaml)
