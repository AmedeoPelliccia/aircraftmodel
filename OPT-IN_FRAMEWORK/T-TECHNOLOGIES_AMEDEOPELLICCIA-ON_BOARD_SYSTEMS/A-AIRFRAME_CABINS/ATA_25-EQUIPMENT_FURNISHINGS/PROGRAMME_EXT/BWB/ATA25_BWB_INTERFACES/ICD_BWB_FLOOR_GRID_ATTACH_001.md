# ICD-002 — BWB Floor Grid Attach Points

**ICD ID:** T-A-ATA25-BWB-ICD-002
**Delta Ref:** DELTA-BWB-25-002
**ATA Subchapter:** 25-20 Passenger Compartment
**Status:** DRAFT (LC01 — attach-point coordinates at LC03)
**Interfaces With:** ATA 53 (Distributed Floor Grid/Spars), ATA 24 (Electrical), ATA 38 (Plumbing)

---

## 1) Purpose

Defines BWB-specific floor grid attach philosophy for seats and monuments.

The BWB uses a **distributed composite floor grid** rather than conventional longitudinal
seat tracks. Seats and monuments attach to a 2D nodal grid rather than single-axis rails.
This fundamentally changes:
- Attachment hardware families
- Load introduction directions
- Fitting adjustment range
- Forward/aft repositioning flexibility

---

## 2) Floor Grid Philosophy

| Feature | WTW (Reference) | BWB (Delta) |
|---------|----------------|-------------|
| Seat attachment | Linear seat track (NAS1381) | 2D floor grid nodes (PN TBD) |
| Track direction | Fore-aft only | Fore-aft + lateral adjustment |
| Load path | Longitudinal to floor beam | Multi-directional to grid |
| Monument attach | Sill fittings (fore-aft rails) | Grid nodes + overhead reaction |
| CG adjustment | Pitch only | Pitch and lateral (span-wise) |

---

## 3) Floor Grid Layout (placeholder — populate at LC03)

| Zone | Grid ID | Node spacing (fore-aft) | Node spacing (lateral) | Fitting PN | Notes |
|------|---------|------------------------|----------------------|-----------|-------|
| Bay 1 (FWD) | GRID-B1 | TBD mm | TBD mm | TBD | — |
| Bay 2 (MID-FWD) | GRID-B2 | TBD mm | TBD mm | TBD | — |
| Bay 3 (MID-AFT) | GRID-B3 | TBD mm | TBD mm | TBD | — |
| Bay 4 (AFT) | GRID-B4 | TBD mm | TBD mm | TBD | — |

---

## 4) Load Introduction (Preliminary)

| Item | Vertical (limit) | Forward (limit) | Lateral (limit) | Reference |
|------|-----------------|-----------------|----------------|-----------|
| Passenger seat | TBD kN/node | TBD kN/node | TBD kN/node | CS-25.561 |
| Flight deck seat | TBD kN/node | TBD kN/node | TBD kN/node | CS-25.562 |
| Galley unit | TBD kN (distributed) | TBD kN | TBD kN | CS-25.561 |

---

## 5) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Define grid node coordinates from Type Design | Structures | LC03 |
| Qualify grid fitting PN for BWB load spectrum | Structures | LC04 |
| Monument load path analysis with grid model | Loads / Stress | LC05 |

---

## Related Documents

- [ICD_LIST.yaml](ICD_LIST.yaml)
- [ANALYSIS_BWB_SEAT_AND_RESTRAINTS_25_562.md](../ATA25_BWB_VERIFICATION_EVIDENCE/ANALYSIS_BWB_SEAT_AND_RESTRAINTS_25_562.md)
- [REQ_BWB_25_200_PASSENGER_COMPARTMENT.yaml](../ATA25_BWB_REQUIREMENTS/REQ_BWB_25_200_PASSENGER_COMPARTMENT.yaml)
