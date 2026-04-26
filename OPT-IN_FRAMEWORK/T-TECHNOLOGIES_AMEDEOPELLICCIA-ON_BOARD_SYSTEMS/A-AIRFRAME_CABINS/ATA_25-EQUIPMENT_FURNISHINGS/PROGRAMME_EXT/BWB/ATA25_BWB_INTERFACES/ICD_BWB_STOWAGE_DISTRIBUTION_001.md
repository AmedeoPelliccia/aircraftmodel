# ICD-004 — BWB Stowage Distribution Zones

**ICD ID:** T-A-ATA25-BWB-ICD-004
**Delta Ref:** DELTA-BWB-25-004
**ATA Subchapter:** 25-20 Passenger Compartment
**Status:** DRAFT (LC01 — zone data at LC03)
**Interfaces With:** ATA 53 (Crown/Soffit Attach), ATA 44 (Cabin Management — weight feed)

---

## 1) Purpose

Defines the BWB-specific overhead stowage distribution zones and the CG management
constraints that result from distributed stowage loading across the wing body span.

In a conventional tube-and-wing aircraft, overhead bin loading has a minor effect on
aircraft CG. In the BWB, bins span multiple structural bays across a wide planform;
selective loading of lateral bins creates lateral CG offsets that must be managed
by the cabin crew or weight-and-balance system.

---

## 2) Stowage Zone Map (placeholder — populate at LC03)

| Zone ID | Bay | BL Range | Max stow load | CG arm (FS) | CG arm (BL) | Notes |
|---------|-----|----------|--------------|------------|------------|-------|
| STOW-Z1 | Bay 1 | 0 to +TBD | TBD kg | TBD mm | ±TBD mm | Symmetric loading preferred |
| STOW-Z2 | Bay 2 | +TBD to +TBD | TBD kg | TBD mm | ±TBD mm | — |
| STOW-Z3 | Bay 3 | +TBD to +TBD | TBD kg | TBD mm | ±TBD mm | — |
| STOW-Z4 | Bay 4 | +TBD to +TBD | TBD kg | TBD mm | ±TBD mm | — |

---

## 3) CG Management Rules

> Δ BWB-specific:

- Lateral bin asymmetry ≥ TBD kg-m shall be flagged to cabin management system (ATA 44).
- Maximum per-bin load: TBD kg (structural limit per crown soffit attach, ATA 53).
- Stowage plan shall be documented in the Weight and Balance Manual (see ATA 06 reference).
- Crew briefing shall include lateral load balance requirement (Operations documentation).

---

## 4) Crown Soffit Attach (preliminary)

| Attach type | Structural interface | Max load per fitting | PN |
|-------------|---------------------|--------------------|----|
| Crown soffit hanger | ATA 53 composite crown frame | TBD kN | TBD |
| Spar crown saddle | ATA 53 spar cap top flange | TBD kN | TBD |

---

## 5) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Define zone BL boundaries from Type Design | Structures | LC03 |
| Quantify per-zone CG arm contributions | Weights / Loads | LC04 |
| Interface with ATA 44 cabin management for lateral CG alert | Systems | LC04 |

---

## Related Documents

- [ICD_LIST.yaml](ICD_LIST.yaml)
- [REQ_BWB_25_200_PASSENGER_COMPARTMENT.yaml](../ATA25_BWB_REQUIREMENTS/REQ_BWB_25_200_PASSENGER_COMPARTMENT.yaml)
