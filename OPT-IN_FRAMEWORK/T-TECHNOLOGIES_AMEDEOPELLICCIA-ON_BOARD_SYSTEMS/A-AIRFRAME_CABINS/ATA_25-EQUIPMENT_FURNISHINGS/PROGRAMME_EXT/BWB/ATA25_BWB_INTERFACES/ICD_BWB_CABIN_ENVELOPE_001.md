# ICD-001 — BWB Cabin Envelope

**ICD ID:** T-A-ATA25-BWB-ICD-001
**Delta Ref:** DELTA-BWB-25-001
**ATA Subchapter:** 25-20 Passenger Compartment
**Status:** DRAFT (LC01 — geometry data at LC03)
**Interfaces With:** ATA 53 (Torque-Box Structure), ATA 21 (ECS), ATA 44 (Cabin Systems)

---

## 1) Purpose

Defines the BWB cabin cross-section envelope and installation clearance zones for all
passenger-area equipment. The BWB uses a **non-circular pressure vessel integrated into
the wing body** — the planform is wide, the crown is relatively low, and the cabin
spans multiple bays separated by structural spars.

This drives fundamentally different installation constraints compared to WTW conventional
circular fuselage.

---

## 2) BWB Cabin Geometry (placeholder — populate at LC03)

| Parameter | Value | Reference |
|-----------|-------|-----------|
| Maximum cabin width (across bays) | TBD mm | Type Design (ATA 53 BWB) |
| Central aisle height (minimum) | TBD mm | CS-25 headroom min |
| Crown-to-floor height at spar centreline | TBD mm | ATA 53 torque-box ICD |
| Spar location (lateral, BL) | TBD mm BL | ATA 53 structural drawing |
| Overhead bin depth available (crown zone) | TBD mm | ATA 53 crown structure ICD |
| Sidewall panel attach zone (from spar cap) | TBD mm | ATA 53 spar cap map |

---

## 3) Bay-to-Bay Installation Rules

> Δ BWB-specific (no equivalent in WTW):

- Cabin bays separated by structural spars: equipment shall not bridge spar bays without
  an approved structural penetration or floating interface scheme.
- Overhead bins at spar crown: clearance to spar cap inner surface ≥ TBD mm.
- ECS ducting path: BWB cross-flow ducting in flat floor zone (ATA 21 ICD reference).
- Fire zone boundary: spar bays define distinct fire zone boundaries (ATA 26 coordination required).

---

## 4) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Define cabin bay envelope from Type Design | Structures | LC03 |
| Coordinate overhead bin envelope with ATA 53 spar ICD | Airframe / Cabin | LC03 |
| Verify aisle width per CS-25 (BWB multi-aisle) | Certification | LC04 |

---

## Related Documents

- [ICD_LIST.yaml](ICD_LIST.yaml)
- [REQ_BWB_25_200_PASSENGER_COMPARTMENT.yaml](../ATA25_BWB_REQUIREMENTS/REQ_BWB_25_200_PASSENGER_COMPARTMENT.yaml)
- ATA 53 BWB structural ICD (external reference)
