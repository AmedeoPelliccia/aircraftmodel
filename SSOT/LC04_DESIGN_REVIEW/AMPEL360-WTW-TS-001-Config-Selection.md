# Configuration Selection Trade Study: WTW vs BWB for LH₂-Powered 100-Pax Short-Haul

**AMPEL360-WTW-TS-001 · Rev A · 2026-02-23**

---

| Field | Value |
|---|---|
| **Document ID** | AMPEL360-WTW-TS-001 Rev A |
| **Classification** | Programme Governance — LC04 Design Review |
| **Date** | 2026-02-23 |
| **Author** | Amedeo Pelliccia / AI-Assisted Engineering |
| **Domain** | aircraftmodel.eu |
| **Framework** | OPT-IN v1.1 / LC04 Trade Study |
| **Status** | OPEN — KNOTs KNOT-CONF-00-00-001 and KNOT-CONF-00-00-002 pending closure |
| **Related documents** | `AMPEL360-FAM-IBD-001 Rev B` (boundary declaration), `AMPEL360-FAM-ARCH-ELC-001 Rev B` (ELC) |

> **Purpose of this document:** to provide the formal structured trade justification
> for selecting the Wide Tube & Wing (WTW) configuration as the AMPEL360 near-term
> programme path, given that the Blended Wing Body (BWB) configuration has an
> inherent volumetric advantage for LH₂ accommodation. This trade study
> supersedes any implicit assumption that WTW is "obviously" the right choice.
> It records the weighted criteria, scoring, residual risks, and open KNOTs
> that must be closed before the selection is confirmed as a design baseline.

---

## 1. Problem Statement

Liquid hydrogen has a volumetric energy density of approximately 8.5 MJ/L, compared
to 34.7 MJ/L for Jet-A1 — a ratio of roughly 1:4. This means a 100-pax, 1,500 km
LH₂-powered aircraft requires tank volumes approximately four times larger than
its kerosene equivalent, **before** accounting for insulation and structural margins.

The two candidate AMPEL360 configurations respond to this constraint differently:

| Configuration | LH₂ Accommodation Strategy | Consequence |
|---|---|---|
| **BWB** (Blended Wing Body) | Native: large pressurised centerbody provides integral tank volume | Volumetric advantage; no stretch penalty |
| **WTW** (Wide Tube & Wing) | Compensatory: widened fuselage + aft-fuselage caudal tank extension | 3–5 m stretch penalty; parasitic drag increase |

The physics unambiguously favours BWB for LH₂ storage. **This trade study must
justify WTW selection on other grounds, or recommend BWB.** An implicit
selection without explicit justification is a governance deficiency — which
this document addresses.

---

## 2. Trade Scope and Boundaries

### 2.1 What this trade decides

The selection of the **primary near-term AMPEL360 programme configuration**:
the vehicle that targets EIS 2035–2040 and is the first to enter service.

> This trade does **not** eliminate BWB. AMPEL360 is a dual-programme family.
> The outcome is which configuration is the **near-term EIS vehicle**. The
> other configuration continues in parallel as the long-horizon vehicle.

### 2.2 Design point

| Parameter | Value |
|---|---|
| Passengers | 100 nominal (50–120 range) |
| Design range | 1,500 km (primary), verified at 1,200 km (optimistic) |
| EIS target | 2035–2040 |
| Propulsion | LH₂ combustion + on-board NH₃ cracking (WTW specific) / LH₂ + PEM fuel cell (BWB specific) |
| Certification basis | EASA CS-25 Amendment 28 / FAA Part 25 |

### 2.3 Candidates evaluated

- **Candidate A — AMPEL360 WTW**: Conventional circular-section fuselage (Ø ≥ 3.5 m),
  caudal LH₂ tanks, tri-species closed loop (LH₂ + NH₃ + N₂ inerting).
- **Candidate B — AMPEL360 BWB**: Non-circular blended-wing-body centerbody,
  integral conformal LH₂ tanks, LH₂ + PEM fuel cell primary propulsion.

---

## 3. Evaluation Criteria and Weights

The trade criteria are derived from the programme's primary objectives:
decarbonisation, certification confidence, and time-to-market.

| # | Criterion | Weight | Rationale |
|---|---|---|---|
| C1 | **LH₂ volumetric accommodation** | 20% | Determines tank sizing, fuselage geometry, range margin |
| C2 | **Certification pathway maturity** | 25% | Single largest programme risk; special conditions and precedent availability |
| C3 | **Airframe TRL (2026 baseline)** | 20% | Technology readiness at programme start determines compression zone depth |
| C4 | **Time to EIS** | 15% | Commercial urgency and carbon reduction timeline |
| C5 | **Cruise aerodynamic efficiency (L/D)** | 10% | Fuel efficiency and range margin |
| C6 | **Manufacturing and supply chain readiness** | 10% | Industrial risk to entry into service |

> **Weight rationale:** Certification pathway (C2) carries the highest weight
> because a configuration that cannot be certified within the EIS window provides
> zero carbon reduction benefit regardless of aerodynamic or volumetric merit.

---

## 4. Candidate Assessment

### 4.1 C1 — LH₂ Volumetric Accommodation

**BWB advantage is unambiguous and must not be understated.**

| Sub-criterion | WTW (A) | BWB (B) |
|---|---|---|
| Native tank integration | ✗ Requires aft-fuselage caudal extension (3–5 m stretch) | ✓ Centerbody provides native integral volume |
| Tank form efficiency | Cylindrical/sphero-cylindrical — thermally near-optimal, but geometrically constrained | Conformal — can be optimised for planform |
| Volume at 100 pax / 1,500 km | ~25–31 m³ envelope required; marginal at Ø 3.5 m | 20–30% more usable volume for same planform span |
| NH₃ co-load impact | +0.3–0.5 m³ (minor vs LH₂ volume) | N/A (BWB uses LH₂ only) |
| Boil-off and insulation | Vacuum-jacketed double wall; boil-off management via C² CELL | Similar requirement; potentially more surface area |

**Scoring:** WTW = **3/5** · BWB = **5/5**

> ⚠ **Acknowledged risk:** KNOT-CONF-00-00-002 is open. The exact L/D and range
> impact of the WTW fuselage stretch has NOT been quantified. Published industry
> estimates place the cruise L/D penalty at 3–7% for a caudal tank layout.
> If the range impact exceeds 10% relative to the kerosene-equivalent baseline,
> this scoring and the overall selection must be re-evaluated.

### 4.2 C2 — Certification Pathway Maturity

**WTW advantage is decisive under current regulatory landscape.**

| Sub-criterion | WTW (A) | BWB (B) |
|---|---|---|
| Pressure cabin shape | Circular — CS-25 §25.365 has established methodology | Non-circular — NO CS-25 precedent for passenger BWB |
| Structural certification | Well-precedented semi-monocoque fuselage methods | Novel: structural substantiation methodology TBD |
| Emergency evacuation | CS-25 §25.807–25.813: conventional door placement | Non-standard egress geometry — requires special condition |
| Special conditions needed | SC-H₂ (hydrogen fuel — draft, actively being developed by EASA) | SC-H₂ **plus** SC-BWB (novel pressure cabin) — two simultaneous novel SCs |
| EASA engagement precedent | Multiple H₂-powered WTW programmes in dialogue with EASA (ZEROe turboprop, etc.) | No precedent for CS-25 passenger BWB; certification risk is additive |
| DAL allocation precedent | Well-established for tube-and-wing architecture | Must be derived from scratch for BWB system architecture |

**Scoring:** WTW = **5/5** · BWB = **2/5**

### 4.3 C3 — Airframe TRL (2026 Baseline)

| Sub-criterion | WTW (A) | BWB (B) |
|---|---|---|
| Fuselage structural concept TRL | 6–7 (mature: circular semi-monocoque with LH₂ adaptation) | 3–4 (conceptual: BWB structural concept unvalidated at this scale) |
| Manufacturing process TRL | 6–7 (established composite/metallic techniques) | 3–4 (novel integrated centerbody manufacturing) |
| System integration TRL | 5–6 (LH₂/NH₃ novel, but airframe integration methods established) | 2–3 (system routing in centerbody is conceptual only) |

**Scoring:** WTW = **4/5** · BWB = **2/5**

### 4.4 C4 — Time to EIS

Industry and internal programme data:

| Configuration | Estimated EIS | Basis |
|---|---|---|
| **WTW** | 2035–2040 | Airbus ZEROe trajectory; FlyZero H₂ WTW data; TRL 6-7 start |
| **BWB** | 2042–2048 | BWB TRL 3-4 start; dual special conditions; no manufacturing precedent |

The ~8-year difference has a direct carbon-reduction impact: a WTW EIS of 2038
vs BWB EIS of 2046 means 8 additional years of fleet retirement acceleration
in the 100-pax short-haul market.

**Scoring:** WTW = **4/5** · BWB = **1/5**

### 4.5 C5 — Cruise Aerodynamic Efficiency (L/D)

| Configuration | Estimated cruise L/D | Source |
|---|---|---|
| **WTW** with LH₂ stretch | 18–22 (reduced vs kerosene baseline by 3–7% stretch penalty) | IBD-001 Rev B §2.4; published estimates |
| **BWB** | 25–28 (intrinsic aerodynamic advantage) | Published BWB aerodynamic studies |

BWB's aerodynamic superiority is real and significant. However, at the 100-pax
short-haul design point, the WTW L/D penalty is partially offset by:
- The NH₃ cryo-shield reducing LH₂ boil-off by ≥ 30% (target — unconfirmed, KNOT-ATA28-20-00-001)
- Shorter mission profile (≤ 1,500 km) limiting cumulative drag penalty impact

**Scoring:** WTW = **3/5** · BWB = **5/5**

> ⚠ The L/D penalty quantification is OPEN (see KNOT-CONF-00-00-002).

### 4.6 C6 — Manufacturing and Supply Chain Readiness

| Sub-criterion | WTW (A) | BWB (B) |
|---|---|---|
| Fuselage tooling | Established circular-section tooling supply chain | Novel integrated tooling — no supplier base |
| Material maturity | CFRP / metallic: qualified processes available | Same materials; novel geometry increases qualification burden |
| FAI and ramp-up | Precedented timeline | Extended first-article schedule |

**Scoring:** WTW = **4/5** · BWB = **2/5**

---

## 5. Weighted Trade Score

| Criterion | Weight | WTW Score | WTW Weighted | BWB Score | BWB Weighted |
|---|---|---|---|---|---|
| C1 — LH₂ Volumetric Accommodation | 20% | 3/5 | **0.60** | 5/5 | **1.00** |
| C2 — Certification Pathway Maturity | 25% | 5/5 | **1.25** | 2/5 | **0.50** |
| C3 — Airframe TRL | 20% | 4/5 | **0.80** | 2/5 | **0.40** |
| C4 — Time to EIS | 15% | 4/5 | **0.60** | 1/5 | **0.15** |
| C5 — Cruise L/D Efficiency | 10% | 3/5 | **0.30** | 5/5 | **0.50** |
| C6 — Manufacturing Readiness | 10% | 4/5 | **0.40** | 2/5 | **0.20** |
| **TOTAL** | **100%** | — | **3.95 / 5.00** | — | **2.75 / 5.00** |

**Conclusion:** WTW scores 3.95/5.00 vs BWB 2.75/5.00 on this weighted basis.
BWB wins on C1 (volumetric) and C5 (L/D) — the two criteria where the physics
inherently favour its geometry. WTW wins on all four remaining criteria.

> **The selection of WTW as the near-term programme vehicle is justified, but
> it is NOT because WTW is better at accommodating LH₂ — it is not. The
> selection rests entirely on certification and TRL grounds. Any degradation
> of the certification path confidence (e.g., CS-25 LH₂ special conditions
> not progressing) or evidence that the L/D penalty exceeds programme
> tolerance must trigger a re-evaluation via IBCR.**

---

## 6. Sensitivity Analysis

The selection is robust to reasonable weight perturbations EXCEPT in two scenarios:

| Scenario | Impact |
|---|---|
| C2 (Certification) weight reduced to ≤ 15% | Scores converge; selection becomes marginal |
| C1 (Volumetric) weight increased to ≥ 35% | BWB wins if volumetric constraint is binding |
| WTW L/D penalty > 10% of kerosene baseline | C5 score drops to 2/5; total WTW score → 3.65 (still WTW but margin narrows) |
| EASA SC-H₂ stalls beyond 2030 | C2 advantage evaporates for both candidates; re-evaluate jointly |

**The most dangerous scenario** is a combination of (a) EASA LH₂ special conditions
progress slower than expected AND (b) the WTW L/D penalty comes in at the
pessimistic end (7%). In that scenario the selection should be revisited.
This is captured in KNOT-CONF-00-00-001 (viability gate).

---

## 7. Residual KNOTs and Selection Preconditions

This trade study is OPEN pending the following evidence items:

| KNOT ID | Title | Closes | Impact on selection |
|---|---|---|---|
| **KNOT-CONF-00-00-001** | WTW Configuration Viability Gate | 2027-Q1 | Master gate: aggregates OI-1 to OI-5 from IBD-001; must CLOSE before design freeze |
| **KNOT-CONF-00-00-002** | LH₂ Volumetric Accommodation — WTW Stretch Penalty Quantification | 2026-Q3 | Quantifies L/D and range impact; if > 10% penalty, re-score C1 and C5 |
| KNOT-ATA53-10-00-001 | Fuselage Diameter Trade (3.5 m vs 3.76 m) | 2026-Q3 | Determines actual caudal tank envelope |
| KNOT-ATA32-10-00-001 | Landing Gear Yehudi Interference | 2026-Q4 | Mass penalty from aft-heavy CG |
| KNOT-ATA55-10-00-001 | CG Envelope T-tail vs Canard | 2026-Q4 | Stability solution for aft-tank depletion |
| KNOT-ATA25-50-00-001 | NH₃ Containment Zone Crashworthiness | 2027-Q2 | Safety certification scope for cracker bay |
| KNOT-ATA28-20-00-001 | NH₃ Cryo-Shield Boil-Off Reduction | 2026-Q4 | Validates 30% target; if not achieved, LH₂ volume increases |

**Precondition for design freeze:** KNOT-CONF-00-00-001 must be CLOSED (residual ≤ 10).
If any sub-KNOT (OI-1 to OI-5) resolves unfavourably, the viability gate is
held open and an IBCR must be filed to reassess the programme boundary.

---

## 8. Decision Record

| Decision | WTW selected as AMPEL360 near-term (EIS 2035–2040) programme vehicle |
|---|---|
| **Basis** | Weighted multi-criterion trade score: 3.95 vs 2.75 (WTW over BWB) |
| **Primary driver** | Certification pathway maturity (C2) — WTW has established CS-25 precedent; BWB requires two simultaneous novel special conditions |
| **Acknowledged weakness** | LH₂ volumetric accommodation: BWB is inherently superior. WTW requires 3–5 m fuselage stretch with 3–7% estimated L/D penalty (not yet quantified — see KNOT-CONF-00-00-002) |
| **Reversibility** | IBCR required if KNOT-CONF-00-00-001 closes with residual > 10, or if L/D penalty > 10%, or if EASA SC-H₂ timeline slips beyond 2030 |
| **BWB status** | Continues as long-horizon programme (AMPEL360 BWB, EIS 2042–2048). Not cancelled. |
| **DUAL PROGRAMME RATIONALE** | Preserves both the certifiable-near-term pathway (WTW) and the performance-superior long-horizon pathway (BWB). Programme diversity de-risks the AMPEL360 family's path to market. |

---

## 9. Approval

| Role | Name | Signature | Date |
|---|---|---|---|
| AMPEL360 Family PM | A. Pelliccia | | |
| CE — AMPEL360 WTW | [TBD] | | |
| CE — AMPEL360 BWB | [TBD] | | |
| STK_CERT Lead | [TBD] | | |

---

<p align="center">
  <strong>AMPEL360 WTW × AMPEL360 BWB</strong><br/>
  <em>Two paths. One family. Reshaping the sky.</em>
</p>
<p align="center">
  <em>By Amedeo Pelliccia · AI-Assisted Engineering · aircraftmodel.eu</em>
</p>
