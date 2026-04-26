# ICD-005 — BWB Egress Clearance Envelopes

**ICD ID:** T-A-ATA25-BWB-ICD-005
**Delta Ref:** DELTA-BWB-25-005
**ATA Subchapter:** 25-60 Emergency Equipment
**Status:** DRAFT (LC01 — clearance data at LC03)
**Interfaces With:** ATA 52 (Exit Doors/Locations), ATA 33 (Emergency Lighting Path)

---

## 1) Purpose

Defines the BWB-specific emergency egress clearance envelopes required for CS-25.803
compliance. The BWB wide-body planform uses radial aisle flow to exits distributed
across the wide cabin; this differs fundamentally from the fore-aft single-aisle or
twin-aisle flow of conventional tube-and-wing aircraft.

---

## 2) BWB Egress Geometry Principles

| Feature | WTW (Reference) | BWB (Delta) |
|---------|----------------|-------------|
| Aisle direction | Fore-aft | Radial (towards nearest exit) |
| Exit distribution | Doors at fuselage sides | Exits distributed on leading/trailing edge |
| Evacuation flow | Linear, longitudinal | Fan-shaped, multi-directional |
| CS-25.803 analysis | Row-by-row blocking | Zone-by-zone blocking |

---

## 3) Egress Clearance Zones (placeholder — populate at LC03)

| Zone | Exit(s) served | Aisle width (min) | Clearance to floor fittings | Notes |
|------|--------------|-----------------|----------------------------|-------|
| FWD starboard | Exit 1S | TBD mm | TBD mm | CS-25 aisle min |
| FWD port | Exit 1P | TBD mm | TBD mm | CS-25 aisle min |
| MID starboard | Exit 2S | TBD mm | TBD mm | CS-25 aisle min |
| MID port | Exit 2P | TBD mm | TBD mm | CS-25 aisle min |
| AFT starboard | Exit 3S | TBD mm | TBD mm | CS-25 aisle min |
| AFT port | Exit 3P | TBD mm | TBD mm | CS-25 aisle min |

---

## 4) Equipment-Free Zones at Exits

> Δ BWB-specific: equipment-free zone fore/aft/lateral of each exit based on radial flow geometry.

- No floor fitting within TBD mm of exit sill (radial direction).
- Overhead bins shall not overhang exit sill by more than TBD mm.
- Monument corners in egress flow zone shall have minimum radius TBD mm (passenger injury mitigation).

---

## 5) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Define exit locations from Type Design / ATA 52 | Doors / Cabin | LC03 |
| Establish radial flow model for each zone | Certification | LC04 |
| Complete CS-25.803 evacuation demonstration plan | Certification | LC05 |

---

## Related Documents

- [ICD_LIST.yaml](ICD_LIST.yaml)
- [TEST_BWB_EGRESS_DEMONSTRATION.md](../ATA25_BWB_VERIFICATION_EVIDENCE/TEST_BWB_EGRESS_DEMONSTRATION.md)
- [REQ_BWB_25_600_EMERGENCY_EQUIPMENT.yaml](../ATA25_BWB_REQUIREMENTS/REQ_BWB_25_600_EMERGENCY_EQUIPMENT.yaml)
