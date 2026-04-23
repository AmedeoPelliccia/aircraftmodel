---
# PCT-28 — Product Conditions / Applicability for ATA-28
#
# Source of truth for BWB vs WTW applicability split in
# OPT-IN_FRAMEWORK/T-TECHNOLOGIES/AMPEL360/COMMON/C2-CIRCULAR_CRYOGENIC_CELLS/ATA_28-FUEL/
#
# Each subsection-level data module (DM) and KNOT under ATA-28 must declare
# one of the PCTs below in its applicability metadata.
#
# Conformance: iSpec 2200 §3.9 (applicability), BREX-IDA360-Q100-v0.1.

schema_version: "1.0"
chapter: "ATA-28"
revision: "A"
date: "2026-04-22"

product_conditions:

  PCT-28-BWB:
    description: "BWB hydrogen-hybrid architecture"
    applies_to:
      - "28-00-10"   # prime-material philosophy
      - "28-10-20"   # LH2 vacuum-insulated tank
      - "28-10-30"   # NH3 cryo-shield vessel (CONDITIONAL — LC04)
      - "28-20-20"   # LH2 transfer and valves
      - "28-20-30"   # NH3 cracker H2 feed (CONDITIONAL — LC04)
      - "28-40-20"   # P/T indicating (H2 extended range portion)
      - "28-40-30"   # NH3 level and purity (CONDITIONAL — LC04)
      - "28-50-20"   # inerting and purge
      - "28-60"      # thermal management & cryogenics (entire slot)
      - "28-70"      # embrittlement monitoring (entire slot)

  PCT-28-WTW:
    description: "WTW near-term certifiable architecture (SAF / Jet-A path where applicable)"
    applies_to:
      - "28-10-10"   # conventional tank
      - "28-20-10"   # fuel feed lines (WTW portion)
      - "28-30-10"   # fuel jettison
      - "28-40-10"   # quantity indicating (WTW portion)

  PCT-28-COMMON:
    description: "Common to both BWB and WTW architectures"
    applies_to:
      - "28-00"      # general (chapter overview)
      - "28-00-00"   # chapter overview
      - "28-20-10"   # fuel feed lines (common manifold topology)
      - "28-40-10"   # quantity indicating (common gauging)
      - "28-40-20"   # P/T indicating (common base)
      - "28-50-10"   # hydrogen leak sensors (any H2 path)
      - "28-90"      # tables, schemas, index

conditional:
  # Subsections gated on LC04 trade study outcome.
  # If the trade rejects the NH3 path, these subsections are removed
  # and their slots returned to the reserved/unallocated state.
  pending_lc04_trade_study:
    - "28-10-30-nh3-cryo-shield-vessel"
    - "28-20-30-nh3-cracker-h2-feed"
    - "28-40-30-nh3-level-and-purity"

reserved_slot_extensions:
  # Slots used beyond their canonical ATA-100 allocation. Each must be
  # declared in BREX-IDA360-Q100-v0.1 with extension justification per
  # iSpec 2200 §3.9.5.
  - slot: "28-50"
    name: "H2 Safety and Leak Detection"
    justification: "H2-specific safety function with no analogue in legacy ATA-28"
  - slot: "28-60"
    name: "Thermal Management & Cryogenics"
    justification: "Cryogenic thermal management has no analogue in legacy ATA-28"
  - slot: "28-70"
    name: "Embrittlement Monitoring"
    justification: "H2 embrittlement is a structural-degradation phenomenon with no analogue in legacy ATA-28"

# Cross-references
references:
  ata_chapter_root: "OPT-IN_FRAMEWORK/T-TECHNOLOGIES/AMPEL360/COMMON/C2-CIRCULAR_CRYOGENIC_CELLS/ATA_28-FUEL"
  brex: "PUB/CSDB/BREX/BREX-IDA360-Q100-v0.1.xml"
  ibd: "AMPEL360-FAM-IBD-001 Rev B"
---

# ATA 28 — C² CELL Architecture

## Chemical Containment & Circulation · Prime Material Management

| Field | Value |
|---|---|
| **Doc ID** | AMPEL360-FAM-ATA28-C2-REF-001 |
| **Rev** | A |
| **Date** | 2026-02-22 |
| **Paradigm** | C² CELL — Chemical Containment & Circulation |
| **Sub-domain** | PMM — Prime Material Management |
| **Scope** | Q100 BWB & WTW · S2040/T1 · IDEALE family |
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
| Hydrogen (stored as liquid, LH₂) | LH₂ | Primary PM | Gas | Cryogenic 20 K, 1–3 bar |
| Ammonia | NH₃ | Secondary PM / H₂ carrier | Liquid | Pressurised 10 bar / 298 K |
| Liquid Nitrogen | LN₂ | Inert blanket / purge | Liquid | Cryogenic 77 K |

---

## 2 · ATA 28 C² CELL Sub-Chapter Map

The legacy ATA 28 sub-chapters are re-mapped to C² CELL functions while
preserving canonical ATA-100 / iSpec 2200 slot semantics. H₂-specific
content lives as **named subsections under the correct slot**, not as a
re-label of the slot itself. Reserved slots `28-50`–`28-70` are used for
genuinely new functions and are declared in the project BREX with
extension justification.

| ATA Sub-Chapter | Canonical Label | C² CELL Function | Directory |
|---|---|---|---|
| 28-00 | General | Chapter overview & PM philosophy | [`28-00-general/`](28-00-general/) |
| 28-10 | Storage | **PM Reservoir & Containment** | [`28-10-storage-reservoir/`](28-10-storage-reservoir/) |
| 28-20 | Distribution | **PM Conditioning & Distribution** | [`28-20-distribution/`](28-20-distribution/) |
| 28-30 | Dump / Jettison | **Emergency Discharge & Safe-State** | [`28-30-dump-jettison/`](28-30-dump-jettison/) |
| 28-40 | Indicating | **State Monitoring & Diagnostics** | [`28-40-indicating/`](28-40-indicating/) |
| 28-50 | Reserved → ext. | **H₂ Safety & Leak Detection** | [`28-50-h2-safety-and-leak-detection/`](28-50-h2-safety-and-leak-detection/) |
| 28-60 | Reserved → ext. | **Thermal Management & Cryogenics** | [`28-60-thermal-management-cryogenics/`](28-60-thermal-management-cryogenics/) |
| 28-70 | Reserved → ext. | **Embrittlement Monitoring** | [`28-70-embrittlement-monitoring/`](28-70-embrittlement-monitoring/) |
| 28-80 | Reserved | Reserved as required | [`28-80-reserved-as-required/`](28-80-reserved-as-required/) |
| 28-90 | Tables / Schemas | Cross-cutting reference data | [`28-90-tables-schemas-index/`](28-90-tables-schemas-index/) |

### 2.1 Subsection Allocation (BWB vs WTW)

Each subsection declares an applicability tag (PCT) defined in
[`PUB/CSDB/APPLICABILITY/PCT-28.yaml`](../../../../../../PUB/CSDB/APPLICABILITY/PCT-28.yaml):

| Subsection | PCT | Notes |
|---|---|---|
| `28-00-00-chapter-overview` | COMMON | |
| `28-00-10-prime-material-philosophy` | BWB | H₂ as prime material |
| `28-10-10-conventional-tank` | WTW | SAF / Jet-A |
| `28-10-20-lh2-vacuum-insulated-tank` | BWB | Cryogenic vessel |
| `28-10-30-nh3-cryo-shield-vessel` | BWB | **CONDITIONAL — pending LC04** |
| `28-20-10-fuel-feed-lines` | COMMON | |
| `28-20-20-lh2-transfer-and-valves` | BWB | Cryogenic lines |
| `28-20-30-nh3-cracker-h2-feed` | BWB | **CONDITIONAL — pending LC04** |
| `28-30-10-fuel-jettison` | WTW | Where applicable |
| `28-40-10-quantity-indicating` | COMMON | |
| `28-40-20-pressure-temperature` | COMMON | H₂ extended range |
| `28-40-30-nh3-level-and-purity` | BWB | **CONDITIONAL — pending LC04** |
| `28-50-10-hydrogen-leak-sensors` | COMMON | Any H₂ path |
| `28-50-20-inerting-and-purge` | BWB | |
| `28-60-10-vacuum-jacket-monitoring` | BWB | |
| `28-60-20-pre-cool-and-conditioning` | BWB | |
| `28-60-30-boil-off-recovery-routing` | BWB | Relocated from 28-30 |
| `28-70-10-sensor-network` | BWB | |
| `28-70-20-inspection-criteria` | BWB | |
| `28-70-30-lifecycle-degradation-model` | BWB | |

### 2.2 Resolution Principle

> **ATA-100 slots `28-10` through `28-40` are semantically binding** —
> their label defines the functional class of all content within, regardless
> of technology. H₂-specific content lives as a *named subsection* under the
> correct slot. Reserved slots (`28-50` → `28-80`) are the legitimate space
> for functions without an ATA analogue, declared explicitly in the project
> BREX with extension justification.

### 2.3 Boil-off Recovery — Semantic Correction

Boil-off recovery is a **closed-loop thermal-management** function
(recover → reuse → vent only as fallback), not a jettison (controlled
discard) function. It lives under `28-60-30-boil-off-recovery-routing/`,
not under `28-30`. See that subsection's README for the full rationale.

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
    ↕ integrated tank bay geometry (BWB / WTW variant)
```

### 4.2 Variant Fork — BWB vs WTW

ATA 28 is the **critical-path fork** between AMPEL360 BWB and AMPEL360 WTW
(ref: AMPEL360-FAM-IBD-001):

| Aspect | BWB (Q100) | WTW |
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
| [IBD-001] | AMPEL360-FAM-IBD-001 Rev B — Family Inheritance Boundary Declaration |
| [BREX] | BREX-IDA360-Q100-v0.1 — Project Business Rules Exchange |
| [TT] | TOKENOMICS_TT.yaml — Teknia Token allocation & spillover |
| [iSpec] | ATA iSpec 2200 — ATA Chapter 28 Fuel |
| [CS-25] | EASA CS-25 — Large Aeroplanes (SC for H₂ systems TBD) |

---

## 8 · Revision History

| Rev | Date | Author | Change |
|---|---|---|---|
| A | 2026-02-22 | IDEALE Programme | Initial C² CELL paradigm declaration |
