# ICD-001 — WTW Cabin Geometry Envelope

**ICD ID:** T-A-ATA25-WTW-ICD-001
**Delta Ref:** DELTA-WTW-25-001
**ATA Subchapter:** 25-20 Passenger Compartment
**Status:** DRAFT (LC01 — geometry data at LC03)
**Interfaces With:** ATA 53 (Fuselage), ATA 21 (ECS), ATA 44 (Cabin Systems)

---

## 1) Purpose

Defines the WTW cabin cross-section envelope and installation clearance zones for all
passenger-area equipment (seats, overhead bins, sidewall panels, monuments).

The WTW variant uses a **conventional circular-section pressurised fuselage** with
frames and stringers. This differs from the BWB distributed-panel cabin and drives
unique installation constraints in this ICD.

---

## 2) Geometry Envelope (placeholder — populate at LC03)

| Parameter | Value | Reference |
|-----------|-------|-----------|
| Cabin interior width (at armrest level) | TBD mm | Fuselage ICD (ATA 53) |
| Cabin interior height (aisle centreline) | TBD mm | Fuselage ICD (ATA 53) |
| Floor-to-ceiling height (minimum) | TBD mm | CS-25 headroom min |
| Overhead bin depth (maximum) | TBD mm | Structural clearance |
| Seat track pitch (standard) | TBD mm | Drawing (ATA 53 floor beams) |
| Sidewall panel attachment zone | TBD mm from frame CL | ATA 53 stringer map |

---

## 3) Clearance and Access Rules

> Δ WTW-specific rules (supplement SHARED ATA 25 §[TBD]):

- Overhead bin clearance to emergency exit sill: minimum TBD mm.
- Aisle width at monument corners: minimum per CS-25 aisle width rule.
- ECS duct routing: coordinate with ATA 21 lateral duct zone (frame bay TBD to TBD).
- Window emergency exit row: equipment-free zone TBD mm fore/aft of exit frame.

---

## 4) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Define exact cabin cross-section dimensions from Type Design data | Structures | LC03 |
| Coordinate overhead bin envelope with ATA 53 ICD | Airframe / Cabin | LC03 |
| Verify aisle width compliance (CS-25) | Certification | LC04 |

---

## Related Documents

- [ICD_LIST.yaml](ICD_LIST.yaml)
- [REQ_WTW_25_200_PASS_COMPARTMENT.yaml](../ATA25_WTW_REQUIREMENTS/REQ_WTW_25_200_PASS_COMPARTMENT.yaml)
- ATA 53 Fuselage ICD (external reference)
