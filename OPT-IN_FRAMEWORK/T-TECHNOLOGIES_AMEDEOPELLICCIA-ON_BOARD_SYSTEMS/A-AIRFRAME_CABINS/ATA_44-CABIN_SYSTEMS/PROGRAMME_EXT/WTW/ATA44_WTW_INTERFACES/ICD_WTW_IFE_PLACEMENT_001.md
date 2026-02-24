# ICD-004 — WTW IFE Server and Satellite Unit Placement

**ICD ID:** T-A-ATA44-WTW-ICD-004
**Delta Ref:** DELTA-WTW-44-005
**ATA Subchapter:** 44-20 In-Flight Entertainment
**Status:** DRAFT (LC01 — placement coordinates at LC03)
**Parent:** [Interfaces README](README.md)

---

## 1) Purpose

Defines the placement envelope for the WTW IFE Media Server and the per-zone Cabin
Satellite Units (CSU) that distribute IFE content and passenger network connectivity.

---

## 2) IFE Media Server Placement

| Parameter | Value | Notes |
|-----------|-------|-------|
| Location | FWD avionics bay | Adjacent to CMC rack |
| Fuselage station | TBD | LC03 |
| Form factor | TBD (vendor-driven) | 1–2 ATR full-size or ARINC 600 |
| Mass (max) | TBD kg | LC03 |
| Power (max) | TBD W | LC03 |
| Cooling | From E/E bay forced-air duct | TBD m³/min |
| Connector face | Aft-facing | TBD at LC03 |
| Maintenance access | Via FWD E/E bay access panel | — |

---

## 3) Cabin Satellite Unit (CSU) Placement

| CSU | Zone | Overhead bin line | FS | BL | WL | Notes |
|-----|------|-------------------|----|----|----|-------|
| CSU-01 | Z1 | FWD overhead | TBD | TBD | TBD | LC03 |
| CSU-02 | Z2 | Mid-FWD overhead | TBD | TBD | TBD | LC03 |
| CSU-03 | Z3 | Mid-AFT overhead | TBD | TBD | TBD | LC03 |
| CSU-04 | Z4 | AFT overhead | TBD | TBD | TBD | LC03 |

---

## 4) WTW-Specific Constraints

> Δ WTW-only:

- IFE server in FWD avionics bay — no pressurised underfloor IFE equipment.
- CSUs mounted in overhead panel crown, aligned with cabin zone boundary; access via
  overhead panel removable sections per ATA 25 cabin lining procedure.
- IFE harness feeds from crown harness run (shared with AFDX backbone) — see ICD-002.
- All IFE LRUs shall meet CS-25.853 flammability requirements for materials.

---

## 5) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Select IFE supplier and confirm server form factor | Cabin Engineering | LC03 |
| Define CSU FS/BL/WL from cabin layout drawing | Cabin Engineering | LC03 |
| Conduct CS-25.853 flammability test on IFE LRU materials | Test | LC07 |

---

## Related Documents

- [REQ_WTW_44_200_IFE.yaml](../ATA44_WTW_REQUIREMENTS/REQ_WTW_44_200_IFE.yaml)
- [TEST_WTW_IFE_FLAMMABILITY_853.md](../ATA44_WTW_VERIFICATION_EVIDENCE/TEST_WTW_IFE_FLAMMABILITY_853.md)
