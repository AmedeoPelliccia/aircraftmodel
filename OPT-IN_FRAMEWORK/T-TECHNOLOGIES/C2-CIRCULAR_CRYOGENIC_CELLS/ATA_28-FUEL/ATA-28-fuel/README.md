# ATA 28 — C² CELL Architecture

## Chemical Containment & Circulation · Prime Material Management

| Field | Value |
|---|---|
| **Doc ID** | AMPEL360-FAM-ATA28-C2-REF-001 |
| **Rev** | A |
| **Date** | 2026-02-22 |
| **Paradigm** | C² CELL — Chemical Containment & Circulation |
| **Sub-domain** | PMM — Prime Material Management |
| **Scope** | Q100 BWB · S2040/T1 · IDEALE family |
| **Regulatory** | ATA iSpec 2200 compliance preserved · CS-25 SC TBD |
| **Status** | ACTIVE — supersedes combustion-logistic framing |

---

## 0 · Paradigm Declaration

This document formally transitions ATA 28 from the **fuel paradigm** to the
**C² CELL paradigm** across all IDEALE hydrogen-electric programmes.

**Old paradigm (combustion logistics):**

```
Fuel Tank → Feed Line → Engine
```

Open-cycle. ATA 28 = fire-system liability. Primary hazard: flame.

**C² CELL paradigm (electrochemical state governance):**

```
Prime Material Reservoir ⇄ Conversion Stack ⇄ Regeneration / Storage
```

Bidirectional. Closed-loop capable. ATA 28 = chemical state custody.
Primary hazard: **phase instability**.

This is not a naming change. It is a **complete restructuring of system logic,
hazard model, design drivers, and ICD topology.**

---

## 1 · C² CELL Conceptual Framework

### 1.1 Definition

> **C² CELL** — Chemical Containment & Circulation:
> A bidirectional electrochemical architecture in which prime chemical potential
> is stored, conditioned, distributed, converted, and — where boundary
> conditions permit — regenerated within a defined system loop.

> **Prime Material (PM):** A chemically stored potential used in controlled
> electrochemical conversion. Not a combustion fuel.

### 1.2 State Vector

For aircraft node _i_, the state governed by ATA 28 is:

```
S_i = (M_i, P_i, T_i, G_i)

  M_i  = stored mass of prime material       [kg]
  P_i  = pressure state                      [bar]
  T_i  = thermal state                       [K]
  G_i  = phase / grade indicator             [–]
```

### 1.3 System Boundary

ATA 28 C² CELL owns everything between:

- **Upstream boundary:** fill/vent interface (ground or aerial)
- **Downstream boundary:** conversion-stack inlet manifold (ATA 47 interface)
- **Regeneration boundary:** recirculation return from ATA 47 (if closed-loop)

### 1.4 Prime Material Species

| Species | Formula | Role | Phase at STP | Storage Condition |
|---|---|---|---|---|
| Liquid Hydrogen | LH₂ | Primary PM | Gas | Cryogenic 20 K, 1–3 bar |
| Ammonia | NH₃ | Secondary PM / H₂ carrier | Liquid | Pressurised 10 bar / 298 K |
| Liquid Nitrogen | LN₂ | Inert blanket / purge | Liquid | Cryogenic 77 K |

---

## 2 · ATA 28 C² CELL Sub-Chapter Map

The legacy ATA 28 sub-chapters are re-mapped to C² CELL functions:

| ATA Sub-Chapter | Legacy Title | C² CELL Function | Directory |
|---|---|---|---|
| 28-10 | Storage | **PM Reservoir & Containment** | [`28-10-storage-reservoir/`](28-10-storage-reservoir/) |
| 28-20 | Distribution | **PM Conditioning & Distribution** | [`28-20-distribution/`](28-20-distribution/) |
| 28-30 | Dump / Jettison | **Emergency Discharge & Safe-State** | [`28-30-dump-jettison/`](28-30-dump-jettison/) |
| 28-40 | Indicating | **State Monitoring & Diagnostics** | [`28-40-indicating/`](28-40-indicating/) |

---

## 3 · Hazard Model Transition

### 3.1 Legacy Hazard (Combustion Paradigm)

| Hazard | Dominant Risk | Mitigation |
|---|---|---|
| Fire / explosion | Ignition of fuel vapour | Inerting, OBIGGS, fire suppression |

### 3.2 C² CELL Hazard Model

| Hazard | Dominant Risk | Mitigation |
|---|---|---|
| Phase instability | Uncontrolled boil-off, rapid vaporisation | Thermal management, pressure relief, cryo-insulation |
| Hydrogen embrittlement | Structural degradation of containment | Material selection (see ATA 51), inspection intervals |
| Cryogenic burn / asphyxiation | Personnel exposure during ground ops | PPE, ventilation, leak detection |
| NH₃ toxicity | Toxic release from secondary PM | Double containment, scrubber, warningRef per BREX |

### 3.3 Safety Classification

Per BREX rule BREX-005: all ATA 28 data modules shall carry
`safetyClass="SC1"` (safety-critical).

All LH₂ data modules shall include a `cautionRef` for hydrogen hazards.
All NH₃ data modules shall include a `warningRef` for toxicity hazards.

---

## 4 · ICD Topology

### 4.1 Inter-ATA Interfaces

```
ATA 21 (ECS)
    ↕ thermal bleed / cabin heat recovery
ATA 24 (Electrical)
    ↕ power bus for pumps, valves, sensors
ATA 26 (Fire Protection)
    ↕ leak detection, inerting, emergency shutdown
ATA 28 (C² CELL) ◄── this system
    ↕ PM delivery to conversion stack
ATA 47 (Inert Gas / N₂ System)
    ↕ blanket gas supply, purge sequences
ATA 47-40 (Fuel Cell Power Plant)
    ↕ PM inlet manifold, recirculation return
ATA 51 (Structures)
    ↕ reservoir mounting, cryo-structural interface
ATA 53 (Fuselage)
    ↕ integrated tank bay geometry (BWB / T&W variant)
```

### 4.2 Variant Fork — BWB vs T&W

ATA 28 is the **critical-path fork** between AMPEL360 BWB and AMPEL360 WTW
(ref: AMPEL360-FAM-IBD-001):

| Aspect | BWB (Q100) | WTW (T&W) |
|---|---|---|
| Reservoir geometry | Conformal bay in centre-body | Cylindrical pod (under-wing / aft) |
| PM species | LH₂ only | LH₂ + NH₃ + LN₂ (tri-species) |
| Recirculation | Partial (thermal recovery) | Full closed-loop (NH₃ cracking) |

---

## 5 · Design Drivers

| # | Driver | Metric | Target |
|---|---|---|---|
| DD-01 | Gravimetric index | kg_PM / kg_system | ≥ 0.40 |
| DD-02 | Boil-off rate | % mass / hour | ≤ 0.05 |
| DD-03 | Fill / drain time | minutes (full cycle) | ≤ 45 |
| DD-04 | Leak-before-break integrity | probability | ≥ 0.999 |
| DD-05 | Phase-transition response | seconds to safe-state | ≤ 2.0 |

---

## 6 · KNU / KNOT Traceability

<!-- KNU-ATA28-00-001 -->

| ID | Description | LC Phase | Status |
|---|---|---|---|
| KNU-ATA28-10-001 | PM Reservoir sizing trade study | LC04 | OPEN |
| KNU-ATA28-10-002 | Cryo-insulation material selection | LC04 | OPEN |
| KNU-ATA28-20-001 | Distribution manifold architecture | LC04 | OPEN |
| KNU-ATA28-20-002 | Tri-species flow control logic | LC05 | OPEN |
| KNU-ATA28-30-001 | Emergency discharge safe-state analysis | LC05 | OPEN |
| KNU-ATA28-40-001 | State-vector sensor suite definition | LC04 | OPEN |
| KNOT-ATA28-10-00-001 | LH₂ reservoir conformal vs cylindrical | LC04 | OPEN |
| KNOT-ATA28-20-00-001 | NH₃ distribution double-containment | LC04 | OPEN |

---

## 7 · References

| Ref | Document |
|---|---|
| [IBD-001] | AMPEL360-FAM-IBD-001 — Family Inheritance Boundary Declaration |
| [BREX] | BREX-IDA360-Q100-v0.1 — Project Business Rules Exchange |
| [TT] | TOKENOMICS_TT.yaml — Teknia Token allocation & spillover |
| [iSpec] | ATA iSpec 2200 — ATA Chapter 28 Fuel |
| [CS-25] | EASA CS-25 — Large Aeroplanes (SC for H₂ systems TBD) |

---

## 8 · Revision History

| Rev | Date | Author | Change |
|---|---|---|---|
| A | 2026-02-22 | IDEALE Programme | Initial C² CELL paradigm declaration |
