# ICD-002 — WTW Seat / Monument Attach Points

**ICD ID:** T-A-ATA25-WTW-ICD-002
**Delta Ref:** DELTA-WTW-25-002
**ATA Subchapter:** 25-10 Flight Compartment / 25-20 Passenger Compartment
**Status:** DRAFT (LC01 — attach-point coordinates at LC03)
**Interfaces With:** ATA 53 (Floor Beams/Seat Tracks), ATA 24 (Electrical), ATA 38 (Plumbing)

---

## 1) Purpose

Defines WTW-specific seat track layout, floor beam attachment coordinates, and
monument (galley/lavatory) structural interface rules for the AMPEL360 WTW cabin.

The WTW variant uses **9-abreast (economy) / 6-abreast (business) seat-track configuration**
on a conventional fuselage floor. Track spacing, sill fitting locations, and load
introduction points differ from the BWB distributed floor plan.

---

## 2) Seat Track Layout (placeholder — populate at LC03)

| Zone | Track Pair ID | Y-coordinate (BL) | Fitting Type | Notes |
|------|--------------|-------------------|-------------|-------|
| Forward Economy | Track-A | TBD mm | 9-track NAS1381 compatible | — |
| Mid-cabin Economy | Track-B | TBD mm | 9-track NAS1381 compatible | — |
| Aft Economy | Track-C | TBD mm | 9-track NAS1381 compatible | — |
| Business Class | Track-D | TBD mm | 6-track wide pitch | — |
| Flight Deck | Track-FD | TBD mm | Mil-spec adjustable rail | — |

---

## 3) Monument Attach Rules

> Δ WTW-specific (supplement SHARED ATA 25 §[TBD]):

- Galley monuments: structural attach to floor sill fittings AND overhead spar (reaction point TBD).
- Lavatory monuments: floor attach only (overhead clearance to ECS/bins; no overhead attach unless mass >TBD kg).
- Crew-rest module (if installed): dedicated structural frame (ATA 53) — coordinates TBD.

---

## 4) Load Introduction (Preliminary)

| Monument / Seat | Vertical load (limit) | Forward load (limit) | Reference |
|----------------|----------------------|---------------------|-----------|
| Passenger seat | TBD kN | TBD kN | CS-25.561 |
| Flight deck seat | TBD kN | TBD kN | CS-25.562 |
| Galley unit | TBD kN | TBD kN | CS-25.561 + galley standard |
| Lavatory unit | TBD kN | TBD kN | CS-25.561 |

---

## 5) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Define track Y-coordinates from Type Design drawing | Structures | LC03 |
| Define sill fitting PN and load ratings | Structures | LC03 |
| Monument load verification analysis | Loads / Stress | LC05 |

---

## Related Documents

- [ICD_LIST.yaml](ICD_LIST.yaml)
- [REQ_WTW_25_100_FLT_COMPARTMENT.yaml](../ATA25_WTW_REQUIREMENTS/REQ_WTW_25_100_FLT_COMPARTMENT.yaml)
- [ANALYSIS_WTW_SEAT_LOADS_25_561.md](../ATA25_WTW_VERIFICATION_EVIDENCE/ANALYSIS_WTW_SEAT_LOADS_25_561.md)
