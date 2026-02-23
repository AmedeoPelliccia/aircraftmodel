# AMPEL360 PROGRAMME FAMILY — INHERITANCE BOUNDARY DECLARATION

## WTW vs BWB Airframe Feasibility for LH₂ Cryogenic Systems

<p align="center">
  <strong>AMPEL360 WTW</strong>&ensp;(Wide Tube & Wing — Near-Term Certifiable)<br/>
  <strong>AMPEL360 BWB</strong>&ensp;(Blended Wing Body — Quantum-Enhanced)
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Doc-IBD--001%20Rev%20B-1B3A5C" alt="Doc ID">
  <img src="https://img.shields.io/badge/Status-CONFIRMED-brightgreen" alt="Status">
  <img src="https://img.shields.io/badge/Framework-OPT--IN%20v1.1-purple" alt="Framework">
  <img src="https://img.shields.io/badge/Tokenomics-TT%20v3.14-gold" alt="TT">
  <img src="https://img.shields.io/badge/Quantum-BWB%20Enhanced-6A1B9A" alt="Quantum">
  <img src="https://img.shields.io/badge/Publications-S1000D-teal" alt="S1000D">
</p>

---

| Field | Value |
|---|---|
| **Document ID** | AMPEL360-FAM-IBD-001 Rev B |
| **Classification** | Programme Governance — Concept Baseline |
| **Date** | 2026-02-22 |
| **Author** | Amedeo Pelliccia / AI-Assisted Engineering |
| **Domains** | aircraftmodel.eu (both programmes) |
| **Framework** | OPT-IN v1.1 / LC01 Uncertainty Orchestration |
| **Supersedes** | Rev A (ID-A360-Q100 → AMPEL360 WTW) |
| **Status** | CONFIRMED — Dual-Path Development Approved |

> This document declares the shared-spine and forked-content boundary between
> the AMPEL360 BWB (Quantum-Enhanced Blended Wing Body) and AMPEL360 WTW
> (Wide Tube & Wing) programmes, supported by a first-principles volumetric
> analysis of LH₂ + NH₃ tank integration feasibility in a conventional
> wide-tube-and-wing airframe.

---

## 1. Executive Summary

The AMPEL360 family currently comprises two sibling programmes targeting
100-passenger zero-CO₂ short-haul operations. AMPEL360 BWB explores a
blended wing body with PEM fuel cell primary propulsion and quantum-enhanced
design optimisation. AMPEL360 WTW explores a conventional wide tube-and-wing
with a tri-species closed-loop architecture (LH₂ / NH₃ / N₂).

Before the programmes accumulate divergent engineering artifacts, this
declaration establishes which content is shared (the spine) and which must fork.

The central technical question is whether the WTW configuration can physically
accommodate the cryogenic tank volumes demanded by LH₂ plus the supplementary
NH₃ inventory required by the AMPEL360 WTW tri-species architecture.

**Verdict:** At 100 passengers and ≤ 1,500 km design range, WTW is viable but
marginal. The NH₃ dual-species addition tightens the margin further but does
not break it. The programmes should not collapse. They serve complementary
roles: the BWB explores the upper performance envelope, the WTW explores the
certifiable-near-term envelope.

---

## 2. The Volumetric Problem: LH₂ in a Tube

### 2.1 First Principles

Liquid hydrogen has a density of 70.8 kg/m³ and a lower heating value of
120 MJ/kg, yielding a volumetric energy density of approximately 8.5 MJ/L.
Kerosene (Jet A-1) delivers 34.7 MJ/L. The ratio is roughly 4:1 — to carry
the same energy, LH₂ requires four times the tank volume of kerosene, before
accounting for insulation, vacuum jackets, and structural margins.

This ratio is the single most consequential number in hydrogen aviation. It
means LH₂ cannot be stored in conventional wet wings. Cylindrical or
sphero-cylindrical pressure vessels, thermally optimal for minimizing
surface-to-volume ratio, must be housed inside the fuselage — either aft of
the cabin, fore and aft, or in a caudal (tail-cone) arrangement.

### 2.2 Tank Sizing for 100 Pax / 1,500 km

| Parameter | Conservative | Optimistic |
|---|---|---|
| Design range | 1,500 km | 1,200 km |
| Mission LH₂ burn (incl. reserves) | 1,400 kg | 1,050 kg |
| LH₂ volume (pure, at 70.8 kg/m³) | 19.8 m³ | 14.8 m³ |
| Gravimetric index (GI = m_fuel / m_tank+fuel) | 0.25 | 0.35 |
| Tank envelope volume (with insulation + structure) | ~30 m³ | ~20 m³ |
| NH₃ co-load (cryo-shield + cracker feed) | 350 kg / 0.51 m³ | 200 kg / 0.29 m³ |
| Total cryogenic volume envelope | ~31 m³ | ~21 m³ |

> NH₃ density is ~682 kg/m³ at −33 °C (pressurized liquid), so its volume
> contribution is small relative to LH₂. The challenge is overwhelmingly
> driven by hydrogen.

### 2.3 Fuselage Geometry Constraints

For a 100-seat WTW aircraft in the ATR 72 to Embraer E190 class, the
reference fuselage diameter is 3.0–3.5 m (external). A cylindrical LH₂ tank
filling the full cross-section aft of the cabin (the "caudal" layout) occupies
a fuselage slice with an effective cross-section area of approximately
7–9.6 m² depending on structural deductions.

| Fuselage Ø (ext) | Effective tank Ø | Length for 25 m³ envelope |
|---|---|---|
| 3.0 m | 2.6 m | 4.7 m |
| 3.5 m (FlyZero-class) | 3.1 m | 3.3 m |
| 4.0 m (widened) | 3.6 m | 2.5 m |

At 3.5 m diameter, housing ~25 m³ of cryogenic tankage aft of the cabin
requires approximately 3.3–4.0 m of additional fuselage length beyond the
kerosene-equivalent airframe. This is the "fuselage stretch penalty."

### 2.4 Consequences of the Stretch

**Wetted area and drag.** An additional 3–4 m of fuselage increases wetted
area by roughly 8–12 %, adding parasitic drag. Published estimates place the
cruise L/D penalty at 3–7 % for a caudal tank layout relative to the kerosene
baseline.

**Centre of gravity management.** Aft-heavy tankage shifts the CG rearward as
fuel burns off. The AMPEL360 WTW must oversize the horizontal tail or introduce
canards/active CG management. The NH₃ cracker, positioned mid-fuselage between
the cabin and LH₂ tanks, may act as a beneficial ballast mass.

**Landing gear integration.** Aft-mounted tanks interfere with the main landing
gear yehudi. This requires either an elongated wing root fairing or a gear
architecture change.

**Crashworthiness and certification.** Caudal LH₂ tanks behind the cabin are
inherently separated from passengers, which is favourable for CS-25 emergency
survivability. The NH₃ inventory (toxic, REACH/CLP classified) requires an
additional containment and purge zone between the cabin bulkhead and the
cracker bay.

---

## 3. BWB as the Upper Bound

The AMPEL360 BWB resolves the volumetric problem structurally. A BWB
provides approximately 20–30 % more usable internal volume for the same
planform span.

| Factor | BWB (AMPEL360 BWB) | WTW (AMPEL360 WTW) |
|---|---|---|
| Tank volume integration | Native advantage | Stretch penalty |
| Cruise L/D | ~25–28 (higher) | ~18–22 (lower) |
| Pressure cabin certification | Non-circular: novel | Circular: established |
| CS-25 precedent | None for passenger BWB | Full precedent |
| Airport gate compatibility | Wider span: Code C stress | Standard span |
| Manufacturing readiness | TRL 3–4 | TRL 6–7 |
| Passenger evacuation | Novel egress paths | Conventional |
| Quantum design optimisation | Active (topology + aero) | Classical methods |
| Time to EIS (est.) | 2042–2048 | 2035–2040 |

**Verdict:** The two configurations are not competitors — they are
complementary risk postures. The WTW trades aerodynamic efficiency for
certification confidence and speed to market. The BWB trades certification
risk for volumetric and aerodynamic superiority, enhanced by quantum
optimisation of topology and aerodynamic surfaces.

---

## 4. Industry Signal: Airbus ZEROe Trajectory

Airbus's ZEROe programme evolution is instructive. In 2020, Airbus presented
three concepts: a turbofan WTW, a turboprop WTW, and a BWB. By 2025, Airbus
down-selected to a fuel-cell-powered turboprop for the first hydrogen
aircraft, while retaining the BWB as a longer-horizon concept.

The lesson: even the largest OEM concluded that a WTW is the viable near-term
vehicle for hydrogen, while the BWB represents the next-generation
configuration. The AMPEL360 family's dual-programme structure mirrors this
logic.

---

## 5. The Tri-Species Complication

The AMPEL360 WTW's NH₃ cracker architecture adds complexity unique to the
WTW variant. The BWB variant uses PEM fuel cells without ammonia. This means
ATA 28 content forks significantly between the two programmes.

**Volume impact:** NH₃ stored as pressurized liquid at ~−33 °C has a density
of ~682 kg/m³ — nearly 10× denser than LH₂. A 200–350 kg NH₃ load occupies
only 0.3–0.5 m³, a minor addition to the total tank envelope.

**Thermal integration benefit:** The NH₃ cryo-shield function may reduce LH₂
boil-off by the targeted ≥ 30 %, which in turn reduces the required LH₂ load
for a given range — partially offsetting the fuselage stretch. This must be
quantified by KNOT-ATA28-20-00-001.

**Bay allocation:** The NH₃ cracker requires a dedicated thermally-managed bay
between the aft cabin pressure bulkhead and the forward LH₂ tank. In the WTW
caudal layout, this bay can be accommodated within the fuselage stretch zone.

---

## 6. Verdict: Do Not Collapse

The WTW configuration is viable but not comfortable for the AMPEL360 WTW
design point. The physics requires:

1. A widened fuselage diameter of ≥ 3.5 m (vs. standard 2.8 m turboprop
   class), following the FlyZero FZR-1E precedent.
2. A fuselage stretch of 3–5 m aft of the cabin for caudal LH₂ tankage plus
   the NH₃ cracker bay.
3. An oversized horizontal tail or canard system for CG management as LH₂
   depletes.
4. A landing gear integration solution that accommodates the aft-heavy mass
   distribution.

None of these are physics-breaking. All are engineering problems with
published solution paths.

**Collapsing the WTW into the BWB would:**

- (a) eliminate the certifiable-near-term pathway;
- (b) double down on BWB certification risk;
- (c) discard the tri-species propulsion architecture entirely;
- (d) remove programme diversity that de-risks the AMPEL360 family's path to
  market.

Both programmes survive. Neither absorbs the other.

---

## 7. Inheritance Boundary Declaration

The following table declares the shared spine and forked content across the
OPT-IN 5-axis topology. **SHARED** content is maintained once and inherited by
both programmes. **FORKED** content diverges and is maintained independently.

| OPT-IN Axis / ATA | Scope | Designation | Rationale |
|---|---|---|---|
| O – Organizations | ATA 00–05 | SHARED | Governance, maintenance policy, airworthiness limitations identical |
| P – Programs | ATA 06–12 | SHARED | Dimensions, servicing, ground handling common |
| T/A – Airframe | ATA 20, 51 | SHARED | Standard practices, materials library |
| T/A – Structures | ATA 52–57 | FORKED | Fuselage geometry, wing planform, door placement diverge |
| T/A – Furnishings | ATA 25, 44, 50 | SHARED (cabin) / FORKED (layout) | Cabin spec common; seat maps and egress paths differ |
| T/M – Flight Controls | ATA 27 | FORKED | BWB: elevons/split surfaces; WTW: conventional ailerons/elevator |
| T/M – Hydraulics | ATA 29 | SHARED | Electro-hydraulic architecture common to both |
| T/M – Landing Gear | ATA 32 | FORKED | WTW aft-heavy CG changes gear loads and retraction geometry |
| T/E1 – ECS | ATA 21 | SHARED | Air conditioning architecture common |
| T/E1 – Fire Protection | ATA 26 | FORKED | WTW: H₂+NH₃ dual-species zones; BWB: H₂-only zones |
| T/E1 – Ice/Rain | ATA 30 | SHARED | Anti-ice systems common |
| T/E1 – Inerting | ATA 47 | FORKED | WTW: N₂ from cracker; BWB: conventional NEA/OBIGGS |
| T/E2 – Electrical | ATA 24 | FORKED | BWB: FC primary power; WTW: generator + FC auxiliary |
| T/E2 – APU | ATA 49 | FORKED | Different architectures |
| T/C2 – Fuel | ATA 28 | FORKED (critical path) | LH₂ tank geometry, NH₃ subsystem, distribution all differ |
| T/P – Propulsion | ATA 60–80 | FORKED | BWB: distributed electric; WTW: turbine combustion + open fan |
| T/D – Data | ATA 31, 45, 46 | SHARED | Indicating, CMS, info systems common framework |
| T/A2 – Avionics | ATA 22, 34, 42 | SHARED (core) / FORKED (FBW laws) | Navigation/IMA shared; flight control laws differ |
| T/C1 – Comms | ATA 23 | SHARED | Communications architecture identical |
| T/I2 – AI/ML | ATA 95, 97 | SHARED | Model governance and synthetic data frameworks common |
| I – Infrastructure | ATA 03/08/10/12 INFRA | SHARED (H₂ GSE) / FORKED (NH₃ GSE) | LH₂ ground infra common; NH₃ handling unique to WTW |
| I – H₂ Supply | IN-10 to IN-90 | SHARED (production) / FORKED (NH₃ sourcing) | Green H₂ supply chain common; NH₃ procurement separate |
| N – Governance | ATA 96, 98 | SHARED | Traceability, DPP, ledger, tokenomics framework identical |

**Summary:** Of 23 boundary entries, 12 are SHARED (maintained once), 8 are
FORKED (maintained independently), and 3 are MIXED (shared foundation with
programme-specific extensions). The critical-path fork is **ATA 28 (Fuel)** —
the locus where the tri-species architecture and the fuel cell architecture
diverge irrecoverably.

---

## 8. Implementation Rules

### 8.1 Repository Structure

SHARED content resides in a common spine repository (`AMPEL360-COMMON`) that
both programme repos inherit via Git submodule or monorepo path. FORKED
content resides exclusively in the programme-specific repo (`AMPEL360-BWB`
for BWB, `AMPEL360-WTW` for WTW).

### 8.2 BREX Inheritance

A family-level BREX file (`BREX-AMPEL360-FAM-v0.1`) encodes shared business
rules. Each programme extends it with programme-specific rules:
`BREX-AMPEL360-BWB-v0.1` (BWB-specific) and `BREX-AMPEL360-WTW-v0.1`
(WTW-specific, including the `respTime` extension). CI validates against the
family BREX first, then the programme BREX.

### 8.3 KNOT Cross-References

Where a KNOT in one programme produces evidence that reduces residual
uncertainty in a sibling KNOT, the spillover is captured in
`TOKENOMICS_TT.yaml` via the `a_k_to_j` adjacency coefficient. This ensures
cross-programme contributions are rewarded through the existing TT distribution
formula without requiring shared KNOT ownership.

### 8.4 Change Control Gate

Any proposal to reclassify a SHARED entry as FORKED (or vice versa) requires
an Inheritance Boundary Change Request (IBCR) reviewed by both programme Chief
Engineers and approved by the AMPEL360 Family Programme Manager. IBCRs are
logged in `N-NEURAL_NETWORKS/ATA_96/96-70-governance-policies-and-rules/`.

---

## 9. Open Items for LC04 Trade Study

> **⚠ Configuration Selection Trade Study:** The formal multi-criterion trade
> study justifying WTW selection over BWB is documented in
> **[`AMPEL360-WTW-TS-001 Rev A`](AMPEL360-WTW-TS-001-Config-Selection.md)**.
> BWB has an inherent volumetric advantage for LH₂ accommodation; WTW is
> selected on certification-pathway and TRL grounds. TS-001 status: OPEN
> pending closure of KNOT-CONF-00-00-001 and KNOT-CONF-00-00-002.

| Item | Question | Resolving KNOT | Target |
|---|---|---|---|
| OI-0 | Is WTW the correct near-term configuration? (WTW vs BWB weighted trade) | KNOT-CONF-00-00-001 | 2027-Q1 |
| OI-0a | LH₂ stretch penalty: what is the actual WTW L/D and range impact vs BWB? | KNOT-CONF-00-00-002 | 2026-Q3 |
| OI-1 | Exact fuselage Ø for WTW: 3.5 m vs 3.76 m (6-abreast vs 5-abreast)? | KNOT-ATA53-10-00-001 | 2026-Q3 |
| OI-2 | NH₃ cryo-shield boil-off reduction: does ≥ 30 % hold at cruise altitude? | KNOT-ATA28-20-00-001 | 2027-Q1 |
| OI-3 | Landing gear yehudi interference: main gear relocation mass penalty? | KNOT-ATA32-10-00-001 | 2026-Q4 |
| OI-4 | CG envelope: T-tail vs canard for aft-tank CG management? | KNOT-ATA55-10-00-001 | 2026-Q4 |
| OI-5 | Crashworthiness: NH₃ containment zone length between bulkhead and LH₂ tank? | KNOT-ATA25-50-00-001 | 2027-Q2 |

> Resolution of OI-0 and OI-0a (via TS-001 and its KNOTs) is a **precondition
> for design freeze**. OI-1 through OI-5 feed into OI-0. If OI-0a quantifies
> an L/D penalty > 10 % of the kerosene-equivalent baseline, or if OI-1 through
> OI-4 collectively indicate WTW cannot close its performance case, an IBCR
> must be filed to reassess the programme boundary.

---

## 10. Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| AMPEL360 Family PM | A. Pelliccia | | |
| CE – AMPEL360 BWB | [TBD] | | |
| CE – AMPEL360 WTW | [TBD] | | |
| STK_CERT Lead | [TBD] | | |

---

<p align="center">
  <strong>AMPEL360 WTW × AMPEL360 BWB</strong><br/>
  <em>Two paths. One family. Reshaping the sky.</em>
</p>
<p align="center">
  <em>By Amedeo Pelliccia · AI-Assisted Engineering · aircraftmodel.eu</em>
</p>
