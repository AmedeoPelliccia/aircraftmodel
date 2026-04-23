# ATA 28-00-00 — Chapter Overview

<!-- KNU-ATA28-00-001 -->

| Field | Value |
|---|---|
| **Doc ID** | AMPEL360-FAM-ATA28-00-OVR-001 |
| **Rev** | A |
| **Date** | 2026-04-23 |
| **Chapter** | ATA 28 — Fuel (re-paradigm: **C² CELL**) |
| **Section / Subject** | 00 / 00 — Chapter Overview |
| **C² CELL Function** | Chapter introduction & navigation entry point |
| **Legacy Title** | ATA 28-00 General |
| **Safety Class** | SC1 |
| **Status** | ACTIVE |

---

## 1 · Purpose

This data module is the **ATA 28-00-00 chapter overview** entry point for the
AMPEL360 hydrogen-electric programme. It re-frames legacy ATA 28 ("Fuel") under
the **C² CELL — Chemical Containment & Circulation** paradigm and provides the
canonical map to all sub-chapter data modules (28-10, 28-20, 28-30, 28-40).

The full paradigm declaration, hazard model, ICD topology, design drivers,
references and revision history are maintained in the parent chapter README:
[`../README.md`](../README.md). This file is the iSpec 2200-compliant
`28-00-00` landing module that other documents and IETP viewers can deep-link
into.

---

## 2 · Scope

ATA 28 (C² CELL) owns the chemical-state custody of all **prime materials (PM)**
on board the aircraft, between the following boundaries:

- **Upstream:** ground or aerial fill / vent interface
- **Downstream:** conversion-stack inlet manifold (interface to ATA 47-40)
- **Regeneration:** recirculation return from the conversion stack (closed-loop
  WTW variant)

| Domain | In Scope | Out of Scope |
|---|---|---|
| LH₂ cryogenic storage, conditioning, distribution | ✅ | — |
| NH₃ pressurised storage and distribution (WTW) | ✅ | — |
| LN₂ inert blanket reservoir | ✅ | — |
| Boil-off recovery and routing | ✅ | — |
| Embrittlement monitoring of containment materials | ✅ | — |
| Conversion electrochemistry (fuel-cell stack) | — | ATA 47-40 |
| Inert gas generation | — | ATA 47 |
| Fire detection / suppression | — | ATA 26 |
| Structural mounting (load path) | — | ATA 51 |

---

## 3 · Paradigm Summary

> **C² CELL** — *Chemical Containment & Circulation.*
> A bidirectional electrochemical architecture in which prime chemical potential
> is stored, conditioned, distributed, converted, and — where boundary
> conditions permit — regenerated within a defined system loop.

Legacy combustion view:

```
Fuel Tank → Feed Line → Engine
```

C² CELL view:

```
Prime Material Reservoir ⇄ Conversion Stack ⇄ Regeneration / Storage
```

ATA 28 is therefore re-classified from "fire-system liability" to
**chemical-state custody**. Primary hazard shifts from **flame** to
**phase instability**.

For the full transition rationale see [`../README.md`](../README.md) §0–§1.

---

## 4 · Prime Material Species

| Species | Formula | Role | Phase at STP | Storage Condition |
|---|---|---|---|---|
| Hydrogen (liquid) | LH₂ | Primary PM | Gas | Cryogenic 20 K, 1–3 bar |
| Ammonia | NH₃ | Secondary PM / H₂ carrier (WTW) | Liquid | Pressurised 10 bar / 298 K |
| Liquid Nitrogen | LN₂ | Inert blanket / purge | Liquid | Cryogenic 77 K |

---

## 5 · Sub-Chapter Map

Legacy ATA 28 sub-chapters re-mapped to C² CELL functions:

| ATA Sub-Chapter | Legacy Title | C² CELL Function | Directory |
|---|---|---|---|
| 28-00 | General | **Chapter Overview** *(this module)* | [`./`](./) |
| 28-10 | Storage | PM Reservoir & Containment | [`../28-10-storage-reservoir/`](../28-10-storage-reservoir/) |
| 28-20 | Distribution | PM Conditioning & Distribution | [`../28-20-distribution/`](../28-20-distribution/) |
| 28-30 | Dump / Jettison | Emergency Discharge & Safe-State | [`../28-30-dump-jettison/`](../28-30-dump-jettison/) |
| 28-40 | Indicating | State Monitoring & Diagnostics | [`../28-40-indicating/`](../28-40-indicating/) |

Variant-specific extensions (WTW closed-loop, embrittlement monitoring, tables
& schemas) live under
[`../ATA-28-fuel/`](../ATA-28-fuel/) — see 28-70 and 28-90.

---

## 6 · State Vector

For aircraft node *i*, the state governed by ATA 28 is:

```
S_i = (M_i, P_i, T_i, G_i)

  M_i  = stored mass of prime material       [kg]
  P_i  = pressure state                      [bar]
  T_i  = thermal state                       [K]
  G_i  = phase / grade indicator             [–]
```

This four-tuple is the canonical signal set exchanged across all ATA 28
sub-chapter data modules and across the ICD boundary to ATA 47-40.

---

## 7 · Hazard Model (Summary)

| Hazard | Dominant Risk | Primary Mitigation |
|---|---|---|
| Phase instability | Uncontrolled boil-off / rapid vaporisation | Thermal management, pressure relief, cryo-insulation |
| Hydrogen embrittlement | Structural degradation of containment | Material selection (ATA 51), inspection intervals (28-70) |
| Cryogenic burn / asphyxiation | Personnel exposure during ground ops | PPE, ventilation, leak detection |
| NH₃ toxicity | Toxic release from secondary PM | Double containment, scrubber, `warningRef` per BREX |

Per BREX rule **BREX-005**, all ATA 28 data modules carry
`safetyClass="SC1"`. LH₂ modules include a `cautionRef`; NH₃ modules include a
`warningRef`. Full hazard model: [`../README.md`](../README.md) §3.

---

## 8 · Inter-ATA Interfaces (ICD)

```
ATA 21 (ECS)              ↕ thermal bleed / cabin heat recovery
ATA 24 (Electrical)       ↕ power bus for pumps, valves, sensors
ATA 26 (Fire Protection)  ↕ leak detection, inerting, emergency shutdown
ATA 28 (C² CELL) ◄── this chapter
ATA 47    (Inert Gas / N₂)        ↕ blanket gas supply, purge sequences
ATA 47-40 (Fuel Cell Power Plant) ↕ PM inlet manifold, recirculation return
ATA 51 (Structures)       ↕ reservoir mounting, cryo-structural interface
ATA 53 (Fuselage)         ↕ integrated tank-bay geometry (BWB / WTW variant)
```

Variant fork (BWB vs WTW) — ATA 28 is the critical-path divergence point of
the AMPEL360 family per [AMPEL360-FAM-IBD-001]:

| Aspect | BWB (Q100) | WTW |
|---|---|---|
| Reservoir geometry | Conformal bay in centre-body | Cylindrical pod (under-wing / aft) |
| PM species | LH₂ only | LH₂ + NH₃ + LN₂ (tri-species) |
| Recirculation | Partial (thermal recovery) | Full closed-loop (NH₃ cracking) |

---

## 9 · Design Drivers (Chapter-Level)

| # | Driver | Metric | Target |
|---|---|---|---|
| DD-01 | Gravimetric index | kg_PM / kg_system | ≥ 0.40 |
| DD-02 | Boil-off rate | % mass / hour | ≤ 0.05 |
| DD-03 | Fill / drain time | minutes (full cycle) | ≤ 45 |
| DD-04 | Leak-before-break integrity | probability | ≥ 0.999 |
| DD-05 | Phase-transition response | seconds to safe-state | ≤ 2.0 |

Sub-chapters MAY introduce additional local drivers but MUST NOT relax the
chapter-level targets above without an approved deviation per BREX.

---

## 10 · KNU / KNOT Traceability (Chapter-Level)

| ID | Description | LC Phase | Status |
|---|---|---|---|
| KNU-ATA28-00-001 | Chapter overview & paradigm declaration | LC04 | OPEN |
| KNU-ATA28-10-001 | PM Reservoir sizing trade study | LC04 | OPEN |
| KNU-ATA28-10-002 | Cryo-insulation material selection | LC04 | OPEN |
| KNU-ATA28-20-001 | Distribution manifold architecture | LC04 | OPEN |
| KNU-ATA28-20-002 | Tri-species flow control logic | LC05 | OPEN |
| KNU-ATA28-30-001 | Emergency discharge safe-state analysis | LC05 | OPEN |
| KNU-ATA28-40-001 | State-vector sensor suite definition | LC04 | OPEN |
| KNOT-ATA28-10-00-001 | LH₂ reservoir conformal vs cylindrical | LC04 | OPEN |
| KNOT-ATA28-20-00-001 | NH₃ distribution double-containment | LC04 | OPEN |

---

## 11 · Applicability

This module applies to all AMPEL360 IDEALE configurations:

- **PCT-28-COMMON** — common PM custody logic (LH₂ baseline, monitoring,
  safe-state)
- **PCT-28-BWB** — conformal bay, single-species (LH₂)
- **PCT-28-WTW** — cylindrical pod, tri-species (LH₂ + NH₃ + LN₂),
  closed-loop NH₃ cracking

Refer to the canonical Product Cross-Reference Table `PCT-28.yaml` in
`PUB/CSDB/APPLICABILITY/` (per repository PCT convention) for the resolved
applicability conditions and reserved-slot extension declarations linked to
BREX.

---

## 12 · References

| Ref | Document |
|---|---|
| [IBD-001] | AMPEL360-FAM-IBD-001 Rev B — Family Inheritance Boundary Declaration |
| [BREX]    | BREX-IDA360-Q100-v0.1 — Project Business Rules Exchange |
| [TT]      | TOKENOMICS_TT.yaml — Teknia Token allocation & spillover |
| [iSpec]   | ATA iSpec 2200 — ATA Chapter 28 Fuel |
| [CS-25]   | EASA CS-25 — Large Aeroplanes (SC for H₂ systems TBD) |
| [PARENT]  | [`../README.md`](../README.md) — ATA 28 C² CELL chapter README |

---

## 13 · Revision History

| Rev | Date | Author | Change |
|---|---|---|---|
| A | 2026-04-23 | IDEALE Programme | Initial 28-00-00 chapter-overview module |
