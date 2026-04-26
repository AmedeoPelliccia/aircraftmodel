# ICD-002 — WTW Cabin Harness Wiring Route Envelopes

**ICD ID:** T-A-ATA44-WTW-ICD-002
**Delta Ref:** DELTA-WTW-44-003
**ATA Subchapter:** 44-10 Cabin Core System
**Status:** DRAFT (LC01 — routing coordinates at LC03)
**Parent:** [Interfaces README](README.md)

---

## 1) Purpose

Defines the spatial routing envelopes for the two main ATA 44 cabin harness runs on the
WTW variant:

1. **Crown run** — ARINC 664 AFDX backbone spine (CMC → CSU fore-to-aft)
2. **Sidewall run** — PA/crew-call audio bus + auxiliary power feeds

These envelopes establish the no-encroachment zones for ATA 25 monument installation,
ATA 26 fire detection loops, and ATA 38 water/waste plumbing.

---

## 2) Crown Run Envelope (ATA 44 AFDX Backbone)

| Parameter | WTW Value | Notes |
|-----------|-----------|-------|
| FS start | TBD (FWD of CMC) | LC03 |
| FS end | TBD (AFT of CAC) | LC03 |
| BL (lateral) | BL 0 ± TBD mm (crown centreline) | LC03 |
| WL (vertical) | Fuselage crown inside radius − TBD mm | LC03 |
| Cross-section envelope | TBD mm × TBD mm | LC03 |
| Separation to structure | Min TBD mm (ATA 53 skin frames) | LC04 |
| Separation to ATA 26 loop | Min TBD mm (CS-25.1353 zone B) | LC04 |

---

## 3) Sidewall Run Envelope (PA / Audio / Aux)

| Parameter | WTW Value | Notes |
|-----------|-----------|-------|
| FS start | TBD | LC03 |
| FS end | TBD | LC03 |
| BL (LH and RH symmetrical) | TBD BL each side | LC03 |
| WL | Sidewall panel attach rail + TBD mm | LC03 |
| Cross-section envelope | TBD mm × TBD mm | LC03 |
| Separation to fuel/hydraulic | N/A (no fuel/hyd in cabin sidewall) | — |

---

## 4) WTW-Specific Constraints

> Δ WTW-only:

- **Continuous run** from FS_start to FS_end — no structural bay interruption.
- Routing through bulkhead grommets at zone boundaries Z1/Z2, Z2/Z3, Z3/Z4.
- No routing through pressure floors or underfloor compartments for ATA 44 cabin signals.

---

## 5) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Define harness envelope coordinates from 3D model (CATIA) | Avionics Inst. Eng | LC03 |
| Define bulkhead grommet locations and sizes | Structures / Avionics | LC03 |
| Confirm separation distances from structure/systems | Avionics / Certification | LC04 |

---

## Related Documents

- [ICD_WTW_CONTROLLER_PLACEMENT_001.md](ICD_WTW_CONTROLLER_PLACEMENT_001.md)
- [REQ_WTW_44_100_CABIN_CORE.yaml](../ATA44_WTW_REQUIREMENTS/REQ_WTW_44_100_CABIN_CORE.yaml)
