# ATA 28 — Fuel System

<!-- ============================================================
     Path:    OPT-IN_FRAMEWORK/T-TECHNOLOGIES/
              C2-CIRCULAR_CRYOGENIC_CELLS/ATA_28-FUEL/ATA-28-fuel/
     Doc ID:  AMPEL360-T-C2-ATA28-REF-001 Rev A
     Date:    2026-02-22
     OPT-IN:  T / C2 — Circular Cryogenic Cells
     ATA:     28 — Fuel System
     Class:   PRIMARY CUT — IBD-001 Rev B (IRRECOVERABLE)
     BREX:    BREX-AMPEL360-WTW-v0.1 / BREX-AMPEL360-BWB-v0.1
     ============================================================ -->

| Field | Value |
|---|---|
| **Doc ID** | AMPEL360-T-C2-ATA28-REF-001 |
| **Rev** | A |
| **Date** | 2026-02-22 |
| **OPT-IN Axis** | T — Technologies / C2 — Circular Cryogenic Cells |
| **ATA** | 28 — Fuel System |
| **Inheritance** | ⚠️ PRIMARY CUT — IBD-001 Rev B |
| **Cut Severity** | IRRECOVERABLE |
| **WTW Path** | `AMPEL360-WTW/T/C2-CIRCULAR_CRYOGENIC_CELLS/ATA_28-FUEL/` |
| **BWB Path** | `AMPEL360-BWB/T/C2/ATA_28-FUEL/` |
| **AMPEL360-COMMON** | ∅ — zero content here |
| **Status** | ACTIVE · OPEN KNOTs |

---

## 1 · Why ATA 28 Is the Primary Cut

ATA 28 is the **irrecoverable divergence point** of the AMPEL360 programme family.
Every WTW-exclusive system traces its root dependency to the NH₃ cracker at **ATA 28-40**:

```
ATA 28-40  NH₃ Catalytic Cracker  (WTW only — absent in BWB)
    │
    ├──▶ ATA 47   N₂ from cracker exhaust → closed-loop inerting
    ├──▶ ATA 75   Engine waste heat 400–600 °C → cracker endothermic feed
    ├──▶ ATA 26   NH₃ toxicity zone → dual-hazard fire protection
    ├──▶ ATA 24   Cracker parasitic loads → power budget
    └──▶ IN-INFRA NH₃ GSE · couplings · safety drills · decontamination
```

The BWB carries **no NH₃**. LH₂ feeds PEM fuel cell stacks directly.
The two fuel architectures are physically incompatible — no DM, requirement, ICDs, or
safety analysis from WTW ATA 28 can be reused by BWB ATA 28, and vice versa.

Cross-programme **knowledge** (not content) flows only via the TT spillover mechanism
(`λ = 0.50`) when a resolved KNOT reduces residual uncertainty in a sibling KNOT.

---

## 2 · Architecture Summary

### 2.1 AMPEL360-WTW — Tri-Species Architecture

```
Species 1 — LH₂  (Liquid Hydrogen)
    Storage:      Vacuum-jacketed cryogenic tanks · caudal position
    Material:     Al-Li 2195 candidate (MAT-001)
    Temperature:  20 K (–253 °C) · Pressure: ~3–6 bar ullage
    Function:     Primary combustion fuel → ATA 72 turbine
                  + NH₃ cracker H₂ product blended to burner

Species 2 — NH₃  (Liquid Ammonia)
    Storage:      Cryo-shield wrapped tank · aft of LH₂ tank
    Material:     Hastelloy C-276 candidate (MAT-003)
    Temperature:  –33 °C at 1 bar / pressurised ~10 bar
    Function:     Cracker feedstock  →  H₂ + N₂

Species 3 — N₂   (Nitrogen — cracker by-product, not stored)
    Source:       NH₃ cracker exhaust at ATA 28-40
    Function:     LH₂/NH₃ ullage inerting → ATA 47

Cracker (ATA 28-40)
    Reaction:     2 NH₃  →  N₂  +  3 H₂   (endothermic: +46 kJ/mol)
    Catalyst:     Ru/Al₂O₃ candidate — KNOT-ATA28-40-00-001
    Temperature:  400–600 °C
    Heat source:  Engine exhaust / turbine waste heat → ATA 75-20
    Target:       ≥95 % conversion efficiency at cruise
```

### 2.2 AMPEL360-BWB — FC-Feed Architecture (LH₂ only)

```
Species 1 — LH₂  (Liquid Hydrogen — sole species)
    Storage:      Conformal tanks · integrated into BWB centerbody structure
    Geometry:     Topology-optimised at QRG-2 (2032)
    Material:     TBD pending QRG-2 topology output
    Temperature:  20 K (–253 °C)
    Function:     Direct feed to PEM fuel cell stacks → ATA 24

FC Feed (ATA 28-50)
    Metering:     Cryogenic LH₂ metering valves → FC stack inlet manifold
    Pressure:     Regulated to FC operating pressure (~3–10 bar)
    Scheduling:   Quantum-optimised FC load at QRG-3 (2038)
    No combustion · no cracker · no N₂ generation · no NH₃ anywhere
```

---

## 3 · Section Breakdown

### 3.1 WTW Section Map

| Section | Title | Content Summary | Key Interfaces | Status |
|---------|-------|----------------|----------------|--------|
| `28-00` | General | System overview · design philosophy · safety classification | IBD-001 · BREX-WTW | ACTIVE |
| `28-10` | LH₂ Storage | Tank design · vacuum-jacket insulation · boil-off · venting · ground fill/defuel | ATA 12 · ATA 47 · ATA 75 | OPEN KNOTs |
| `28-20` | NH₃ Storage & Cryo-Shield | NH₃ tank · cryo-shield architecture · NH₃ boil-off management (OI-2) | ATA 26 · ATA 47 | OPEN KNOTs |
| `28-30` | Boil-Off Recovery | LH₂ boil-off routing: FC auxiliary / purge / NH₃ sub-cooling | ATA 24 · ATA 49 | OPEN KNOTs |
| `28-40` | NH₃ Catalytic Cracker | Cracker assembly · Ru/Al₂O₃ catalyst · heat exchanger · H₂/N₂ separation | ATA 47 · ATA 73 · ATA 75 | ⚠️ OPEN — CRITICAL |
| `28-50` | Reserved | — | — | Reserved |
| `28-60` | Reserved | — | — | Reserved |
| `28-70` | Indicating & Monitoring | H₂ embrittlement monitoring · NH₃ contamination detection · leak · quantity | ATA 31 · ATA 45 | OPEN KNOTs |
| `28-80` | Reserved | — | — | Reserved |
| `28-90` | Tables · Schemas · Index | Material index · pressure schedule · DM cross-reference | MAT-INDEX | ACTIVE |

### 3.2 BWB Section Map

| Section | Title | Content Summary | Key Interfaces | Status |
|---------|-------|----------------|----------------|--------|
| `28-00` | General | System overview · FC-feed philosophy · safety classification | IBD-001 · BREX-BWB | ACTIVE |
| `28-10` | LH₂ Storage | Conformal tank design · centerbody integration · fill/defuel | ATA 12 · ATA 57 · QRG-2 | OPEN — QRG-2 gate |
| `28-20` | LH₂ Distribution | Low-loss transfer lines · tank-to-FC manifold routing | ATA 24 · ATA 49 | PLANNED |
| `28-30` | Reserved | No boil-off recovery — FC direct feed architecture | — | Reserved |
| `28-40` | Reserved | No cracker — NH₃-free architecture | — | Reserved |
| `28-50` | FC Feed Metering & Pressure Regulation | Cryogenic metering valves · pressure control · flow demand | ATA 24 · ATA 76 | PLANNED |
| `28-60` | Reserved | — | — | Reserved |
| `28-70` | Indicating & Monitoring | H₂ embrittlement monitoring · leak detection · quantity | ATA 31 · ATA 45 | PLANNED |
| `28-80` | Reserved | — | — | Reserved |
| `28-90` | Tables · Schemas · Index | Conformal tank index · pressure schedule · DM cross-reference | MAT-INDEX | PLANNED |

---

## 4 · LC Bucket Assignments (both programmes)

All 14 LC folders are instantiated at each sub-subject node.

| LC | Title | WTW Primary Artifacts | BWB Primary Artifacts | AoR |
|----|-------|-----------------------|----------------------|-----|
| **LC01** | Problem Statement | KNOTS.csv · KNU_PLAN.csv · TIMELINE.csv · RACI.csv · TOKENOMICS_TT.yaml · AWARDS_TT.csv | Same structure | STK_PMO |
| **LC02** | System Requirements | SYS-REQ-28-WTW-xxx · trace CS-25 / SC-H₂ | SYS-REQ-28-BWB-xxx | STK_SE |
| **LC03** | Safety & Reliability | FMEA-ATA28-WTW · FTA-LH₂-LEAK · FTA-NH₃-LEAK · hazard log | FMEA-ATA28-BWB · FTA-LH₂-LEAK-BWB | STK_SAF |
| **LC04** | Design Definition | DD + ICD artifacts — §5 | DD + ICD artifacts — §5 | STK_SE |
| **LC05** | Analysis Models | Cracker · thermal · DTA models — §6 | Topology · DTA · FC-feed models — §6 | STK_SE |
| **LC06** | Verification | Test reports · compliance matrix · ground test evidence · BREX pass | Same | STK_TEST |
| **LC07** | Validation | Integration V&V: fuel + propulsion + inerting | FC-feed integration V&V | STK_TEST |
| **LC08** | Configuration | P/N · drawing refs · effectivity (ACT) · MAT-ID traceability | Same | STK_CM |
| **LC09** | Production | Tank welding · insulation bonding · cracker assembly | Conformal tank: CFRP layup · bonding · inspection | STK_SE |
| **LC10** | Operations | Pre-flight H₂/NH₃ checks · fuelling sequence (FCOM source) | Pre-flight H₂ checks · FC pre-conditioning | STK_OPS |
| **LC11** | Maintenance | H₂ seal inspection · cracker catalyst replacement · vacuum-jacket check | H₂ seal · conformal tank inspection | STK_MRO |
| **LC12** | Customer Care | SB/AD interface · operator H₂/NH₃ safety training ref | SB/AD interface | STK_CM |
| **LC13** | Training | H₂/NH₃ safety · fuelling crew · cracker system ops | H₂ safety · FC-feed operation | STK_OPS |
| **LC14** | Retirement & Circularity | LH₂ tank decommission · NH₃ disposal · DPP EoL record | LH₂ conformal tank decommission · DPP | STK_DATA |

---

## 5 · LC04 — Design Definition

### 5.1 WTW

| Artifact ID | Title | Section | Status |
|-------------|-------|---------|--------|
| `DD-ATA28-WTW-001` | LH₂ tank assembly design definition — vacuum-jacketed, caudal | 28-10 | OPEN |
| `DD-ATA28-WTW-002` | NH₃ tank and cryo-shield design definition | 28-20 | OPEN |
| `DD-ATA28-WTW-003` | Boil-off recovery system architecture ICD | 28-30 | OPEN |
| `DD-ATA28-WTW-004` | NH₃ catalytic cracker assembly design definition | 28-40 | ⚠️ OPEN — CRITICAL |
| `DD-ATA28-WTW-004a` | Catalyst selection rationale: Ru/Al₂O₃ vs Fe-based candidates | 28-40 | OPEN |
| `DD-ATA28-WTW-004b` | Cracker heat exchanger ICD — ATA 75 waste heat interface | 28-40 | OPEN |
| `DD-ATA28-WTW-004c` | H₂/N₂ separation and delivery ICD — ATA 47 and ATA 73 | 28-40 | OPEN |
| `DD-ATA28-WTW-005` | H₂ embrittlement + NH₃ contamination monitoring architecture | 28-70 | OPEN |
| `ICD-ATA28-WTW-ATA47` | ICD: ATA 28-40 cracker N₂ → ATA 47 inerting system | 28-40/47 | OPEN |
| `ICD-ATA28-WTW-ATA75` | ICD: ATA 75 waste heat → ATA 28-40 cracker feed | 28-40/75 | OPEN |
| `ICD-ATA28-WTW-ATA73` | ICD: ATA 28-40 H₂ product → ATA 73 engine fuel control | 28-40/73 | OPEN |
| `ICD-ATA28-WTW-ATA24` | ICD: ATA 28-30 boil-off H₂ → ATA 24 FC auxiliary power | 28-30/24 | OPEN |
| `MAT-SEL-ATA28-WTW` | Material selection: MAT-001 (Al-Li 2195) LH₂ tank · MAT-003 (Hastelloy C-276) NH₃ tank | 28-10/20 | OPEN |

### 5.2 BWB

| Artifact ID | Title | Section | Status |
|-------------|-------|---------|--------|
| `DD-ATA28-BWB-001` | LH₂ conformal tank design definition — centerbody integration | 28-10 | OPEN — pending QRG-2 |
| `DD-ATA28-BWB-001a` | Conformal tank topology optimisation input specification | 28-10 | OPEN |
| `DD-ATA28-BWB-001b` | Tank–structure integration ICD — ATA 57 centerbody attachment | 28-10/57 | OPEN |
| `DD-ATA28-BWB-002` | LH₂ distribution manifold design definition | 28-20 | PLANNED |
| `DD-ATA28-BWB-003` | FC feed metering and pressure regulation design definition | 28-50 | PLANNED |
| `ICD-ATA28-BWB-ATA24` | ICD: ATA 28-50 LH₂ feed → ATA 24 FC stack inlet manifold | 28-50/24 | PLANNED |
| `ICD-ATA28-BWB-ATA57` | ICD: ATA 28-10 conformal tank → ATA 57 centerbody structure | 28-10/57 | OPEN |
| `MAT-SEL-ATA28-BWB` | Material selection: conformal tank TBD — pending QRG-2 topology | 28-10 | OPEN |

---

## 6 · LC05 — Analysis Models

### 6.1 WTW

| Artifact ID | Title | Method | Status |
|-------------|-------|--------|--------|
| `ANA-ATA28-WTW-001` | LH₂ tank pressure-cycle fatigue analysis | FEM / fracture mechanics | OPEN |
| `ANA-ATA28-WTW-002` | LH₂ boil-off rate model — cruise / ground / emergency venting | Thermodynamic simulation | OPEN |
| `ANA-ATA28-WTW-003` | NH₃ cryo-shield thermal effectiveness — boil-off reduction ≥30 % | Thermal FEM | OPEN · OI-2 · KNOT-ATA28-20-00-001 |
| `ANA-ATA28-WTW-004` | NH₃ cracker conversion efficiency — ≥95 % at cruise (Ru/Al₂O₃) | Catalytic kinetic model | OPEN · KNOT-ATA28-40-00-001 |
| `ANA-ATA28-WTW-004a` | Cracker heat balance — ATA 75 waste heat availability vs endothermic demand | Energy balance model | OPEN · KNOT-ATA28-40-00-002 |
| `ANA-ATA28-WTW-004b` | Cracker cold-start transient — time to operating temperature | Transient thermal model | OPEN · KNOT-ATA28-40-00-003 |
| `ANA-ATA28-WTW-004c` | Catalyst deactivation model — Ru sintering and NH₃ poisoning rate | Accelerated ageing + literature | OPEN · KNOT-ATA28-40-00-004 |
| `ANA-ATA28-WTW-005` | H₂ embrittlement susceptibility — Al-Li 2195 at 20 K | Materials testing / literature | OPEN · KNOT-ATA28-70-00-001 |
| `ANA-ATA28-WTW-006` | NH₃ contamination detection threshold — sensor type and placement | CFD / sensor sensitivity model | OPEN · KNOT-ATA28-70-00-002 |
| `ANA-ATA28-WTW-007` | Tri-species mass budget and CG envelope model (LH₂ + NH₃ depletion) | Trajectory simulation | OPEN |
| `ANA-ATA28-WTW-008` | Leak and dispersion model — LH₂ and NH₃ in aft fuselage zone | CFD / PHAST | OPEN |
| `ANA-ATA28-WTW-009` | FMEA-driven failure rate model — cracker pellet bed assembly | Reliability analysis | OPEN |
| `ANA-ATA28-WTW-010` | LH₂ tank structural life limit analysis — DTA input to ATA 04 ALI | Fracture mechanics | OPEN |

### 6.2 BWB

| Artifact ID | Title | Method | Status |
|-------------|-------|--------|--------|
| `ANA-ATA28-BWB-001` | Conformal tank topology optimisation — centerbody integration | NISQ surrogate at QRG-1; full MDO at QRG-2 | OPEN · gates QRG-1/2 |
| `ANA-ATA28-BWB-001a` | Quantum benchmark: NISQ vs classical topology result (OI-6) | Quantum / classical comparison | OPEN · QRG-1 (2027-Q4) |
| `ANA-ATA28-BWB-002` | LH₂ conformal tank pressure-cycle fatigue analysis | FEM / fracture mechanics | OPEN — pending geometry |
| `ANA-ATA28-BWB-003` | LH₂ boil-off rate model — conformal geometry | Thermodynamic simulation | OPEN |
| `ANA-ATA28-BWB-004` | H₂ embrittlement susceptibility — conformal tank material (TBD) | Materials testing | OPEN — material TBD at QRG-2 |
| `ANA-ATA28-BWB-005` | Leak and dispersion model — LH₂ in BWB centerbody zone | CFD / PHAST | OPEN |
| `ANA-ATA28-BWB-006` | FC feed demand model — LH₂ flow rate vs FC stack power schedule | Electrochemical + QRG-3 optimisation | OPEN |
| `ANA-ATA28-BWB-007` | Conformal tank DTA — structural life limit input to ATA 04 ALI | Fracture mechanics | OPEN — pending geometry |

---

## 7 · KNOT Register

### 7.1 WTW KNOTs

| KNOT ID | Title | R_before | R_target | Status | AoR | Target |
|---------|-------|:--------:|:--------:|--------|-----|--------|
| `KNOT-ATA28-10-00-001` | LH₂ tank geometry and ground interface (GI) definition | 100 | 10 | OPEN | STK_SE | 2027-Q1 |
| `KNOT-ATA28-10-00-002` | LH₂ tank material qualification — Al-Li 2195 at 20 K | 95 | 10 | OPEN | STK_SE | 2027-Q3 |
| `KNOT-ATA28-20-00-001` | NH₃ cryo-shield boil-off reduction ≥30 % at cruise (OI-2) | 100 | 10 | OPEN | STK_SE | 2027-Q1 |
| `KNOT-ATA28-20-00-002` | NH₃ tank material qualification — Hastelloy C-276 at –33 °C | 90 | 10 | OPEN | STK_SE | 2027-Q3 |
| `KNOT-ATA28-30-00-001` | Boil-off routing trade: FC aux / purge / NH₃ sub-cooling | 90 | 15 | OPEN | STK_SE | 2026-Q4 |
| `KNOT-ATA28-40-00-001` | NH₃ cracker conversion efficiency ≥95 % at cruise | **100** | 10 | OPEN | STK_SE | 2027-Q4 |
| `KNOT-ATA28-40-00-002` | Cracker heat balance — ATA 75 availability vs endothermic demand | **100** | 10 | OPEN | STK_SE | 2027-Q2 |
| `KNOT-ATA28-40-00-003` | Cracker cold-start time — operational readiness requirement | 95 | 10 | OPEN | STK_SE | 2027-Q3 |
| `KNOT-ATA28-40-00-004` | Catalyst service life — Ru/Al₂O₃ deactivation model and ATA 05 interval | **100** | 15 | OPEN | STK_MRO | 2028-Q1 |
| `KNOT-ATA28-70-00-001` | H₂ embrittlement monitoring — sensor type and architecture | 95 | 10 | OPEN | STK_SE | 2027-Q1 |
| `KNOT-ATA28-70-00-002` | NH₃ contamination detection limit — sensor sensitivity | 90 | 10 | OPEN | STK_SE | 2027-Q2 |

### 7.2 BWB KNOTs

| KNOT ID | Title | R_before | R_target | Status | AoR | Target |
|---------|-------|:--------:|:--------:|--------|-----|--------|
| `KNOT-ATA28-BWB-10-00-001` | Conformal tank geometry — topology optimisation output (gates QRG-2) | **100** | 10 | OPEN | STK_SE | 2032-Q4 |
| `KNOT-ATA28-BWB-10-00-002` | Conformal tank material selection — pending QRG-2 geometry | **100** | 10 | OPEN | STK_SE | 2033-Q2 |
| `KNOT-ATA28-BWB-10-Q-001` | NISQ surrogate benchmark for tank topology (OI-6) | **100** | 20 | OPEN | STK_AI | 2027-Q4 |
| `KNOT-ATA28-BWB-50-00-001` | FC feed metering valve cryogenic qualification | 90 | 10 | OPEN | STK_SE | 2030-Q2 |

---

## 8 · KNU Plan — Selected Examples

### 8.1 KNOT-ATA28-40-00-001 (NH₃ cracker efficiency — WTW)

| KNU ID | Type | Class | Artifact | AoR | Due | Status |
|--------|------|-------|----------|-----|-----|--------|
| `KNU-ATA28-40-REQ-001` | REQ | SSOT | `LC02/SYS-REQ-28-WTW-CRACK-001.md` | STK_SE | 2026-Q3 | PLANNED |
| `KNU-ATA28-40-SAF-001` | SAF | SSOT | `LC03/FMEA-CRACKER-001.xlsx` | STK_SAF | 2026-Q4 | PLANNED |
| `KNU-ATA28-40-DD-001` | ICD | SSOT | `LC04/DD-ATA28-WTW-004.md` | STK_SE | 2026-Q4 | PLANNED |
| `KNU-ATA28-40-DD-002` | ICD | SSOT | `LC04/ICD-ATA28-WTW-ATA75.md` | STK_SE | 2026-Q4 | PLANNED |
| `KNU-ATA28-40-ANA-001` | ANA | SSOT | `LC05/ANA-ATA28-WTW-004.pdf` | STK_SE | 2027-Q1 | PLANNED |
| `KNU-ATA28-40-ANA-002` | ANA | SSOT | `LC05/ANA-ATA28-WTW-004a.pdf` | STK_SE | 2027-Q2 | PLANNED |
| `KNU-ATA28-40-ANA-003` | ANA | SSOT | `LC05/ANA-ATA28-WTW-004b.pdf` | STK_SE | 2027-Q3 | PLANNED |
| `KNU-ATA28-40-TEST-001` | TEST | SSOT | `LC06/TEST-CRACKER-BENCH-001.pdf` | STK_TEST | 2027-Q4 | PLANNED |
| `KNU-ATA28-40-PUB-001` | PUB | CSDB | `PUB/AMM/CSDB/DM/AMPEL360-W-28-40-00-00A-040A-A.xml` | STK_CM | 2027-Q4 | PLANNED |
| `KNU-ATA28-40-PUB-002` | PUB | CSDB | `PUB/AMM/CSDB/DM/AMPEL360-W-28-40-00-00A-522A-A.xml` | STK_CM | 2027-Q4 | PLANNED |

> ⚠️ Closure criterion for this KNOT: bench test data at representative altitude conditions
> must be included in `LC06/`. Kinetic model alone (ANA-001) is **insufficient** for closure.

### 8.2 KNOT-ATA28-BWB-10-Q-001 (NISQ benchmark — BWB)

| KNU ID | Type | Class | Artifact | AoR | Due | Status |
|--------|------|-------|----------|-----|-----|--------|
| `KNU-ATA28-BWB-Q-REQ-001` | REQ | SSOT | `LC02/SYS-REQ-28-BWB-CONF-001.md` | STK_SE | 2026-Q4 | PLANNED |
| `KNU-ATA28-BWB-Q-DD-001` | ICD | SSOT | `LC04/DD-ATA28-BWB-001a.md` | STK_SE | 2026-Q4 | PLANNED |
| `KNU-ATA28-BWB-Q-ANA-001` | ANA | SSOT | `LC05/ANA-ATA28-BWB-001a.pdf` (NISQ run) | STK_AI | 2027-Q3 | PLANNED |
| `KNU-ATA28-BWB-Q-ANA-002` | ANA | SSOT | `LC05/ANA-ATA28-BWB-001a-BENCHMARK.md` | STK_AI | 2027-Q4 | PLANNED |
| `KNU-ATA28-BWB-Q-PUB-001` | PUB | CSDB | `PUB/AMM/CSDB/DM/AMPEL360-B-28-10-00-00A-040A-A.xml` | STK_CM | 2028-Q1 | PLANNED |

---

## 9 · BREX Rules — ATA 28

### 9.1 Family Rules — `BREX-AMPEL360-FAM-v0.1` (both programmes)

| Rule ID | Scope | Requirement | Severity |
|---------|-------|-------------|----------|
| `BREX-FAM-H2-001` | All ATA 28 DMs | `safetyClass="SC1"` mandatory on every DM | ERROR |
| `BREX-FAM-H2-002` | Procedural DMs with metallic wetted parts | `cautionRef id="CAUTION-IDA360-H2-EMBRITTLEMENT"` required | ERROR |
| `BREX-FAM-UNIT-001` | All DMs | SI units primary (K · Pa · kg) · imperial only where authority mandates | WARNING |

### 9.2 WTW Rules — `BREX-AMPEL360-WTW-v0.1`

| Rule ID | Scope | Requirement | Severity |
|---------|-------|-------------|----------|
| `BREX-IDA360-001` | WTW 28-10/20/30/40/70 | `cautionRef id="CAUTION-IDA360-H2-EMBRITTLEMENT"` in all procedural DMs | ERROR |
| `BREX-IDA360-002` | WTW 28-20 · 28-40 | `warningRef id="WARNING-IDA360-NH3-TOXICITY"` mandatory on all NH₃-handling DMs | ERROR |
| `BREX-IDA360-004` | WTW 28-40 | `cracker-state` attribute mandatory on procedural steps: values `HOT\|COLD\|PURGE` | ERROR |
| `BREX-IDA360-005` | WTW 28-40/47/26 | `speciesScope` element mandatory listing active species `(LH2\|NH3\|N2)` | ERROR |
| `BREX-IDA360-006` | WTW 28-20 | `nh3-containment-zone="TRUE"` attribute mandatory on NH₃ zone access DMs | ERROR |

### 9.3 BWB Rules — `BREX-AMPEL360-BWB-v0.1`

| Rule ID | Scope | Requirement | Severity |
|---------|-------|-------------|----------|
| `BREX-BWB-H2-001` | BWB 28-10 | `quantumProvenance` element mandatory on DMs referencing QRG-2 topology outputs | ERROR |
| `BREX-BWB-H2-002` | BWB 28-10 | `qrg-gate="QRG-2"` attribute mandatory on conformal tank design DMs | ERROR |
| `BREX-BWB-H2-003` | BWB 28-50 | `fc-stack-id` attribute mandatory in FC feed metering procedural steps | ERROR |
| `BREX-IDA360-001` | BWB 28-10/20/70 | `cautionRef id="CAUTION-IDA360-H2-EMBRITTLEMENT"` in procedural DMs | ERROR |

### 9.4 Cross-Branch Contamination — CI FATAL

WTW ATA 28 DMs must not contain:
```
quantum · NISQ · QRG- · conformal tank · centerbody
FC-primary · fuel cell stack feed · topology optimization
```

BWB ATA 28 DMs must not contain:
```
NH3 · NH₃ · ammonia · cracker · tri-species
N2 inerting · cryo-shield · Ru/Al₂O₃ · BREX-IDA360-002
```

Both violations: severity **FATAL** — blocks merge.

---

## 10 · DM Naming Convention

```
AMPEL360 - [VARIANT] - [ATA] - [SECTION] - [SUBJECT] - [UNIT] - [INFOCODE] - [ITEMLOC]
  VARIANT:   W (WTW) · B (BWB)
  INFOCODE:  040A description · 520A maintenance check · 522A removal/installation · 040B operation
```

### 10.1 WTW DM Examples

| DMC | Infocode | Title |
|-----|----------|-------|
| `AMPEL360-W-28-10-00-00A-040A-A` | 040A | LH₂ storage tank — description and operation |
| `AMPEL360-W-28-20-00-00A-040A-A` | 040A | NH₃ storage and cryo-shield — description and operation |
| `AMPEL360-W-28-40-00-00A-040A-A` | 040A | NH₃ catalytic cracker — description and operation |
| `AMPEL360-W-28-40-00-00A-040B-A` | 040B | NH₃ catalytic cracker — operation procedures |
| `AMPEL360-W-28-40-00-00A-520A-A` | 520A | NH₃ catalytic cracker — maintenance check |
| `AMPEL360-W-28-40-00-00A-522A-A` | 522A | NH₃ catalyst (Ru/Al₂O₃) — replacement procedure |
| `AMPEL360-W-28-70-00-00A-040A-A` | 040A | H₂ and NH₃ monitoring system — description and operation |

### 10.2 BWB DM Examples

| DMC | Infocode | Title |
|-----|----------|-------|
| `AMPEL360-B-28-10-00-00A-040A-A` | 040A | LH₂ conformal storage tank — description and operation |
| `AMPEL360-B-28-20-00-00A-040A-A` | 040A | LH₂ distribution manifold — description and operation |
| `AMPEL360-B-28-50-00-00A-040A-A` | 040A | FC feed metering and pressure regulation — description and operation |
| `AMPEL360-B-28-50-00-00A-040B-A` | 040B | FC feed metering — operating procedures |
| `AMPEL360-B-28-70-00-00A-040A-A` | 040A | H₂ monitoring system — description and operation |

---

## 11 · TT Tokenomics — ATA 28

ATA 28 carries the **highest TT reward pools** in the programme, reflecting the
maximum uncertainty density and critical-path status of both architectures.
Family defaults: `α = 0.30` (effort) · `(1–α) = 0.70` (impact) · `λ = 0.50` (spillover).

### 11.1 WTW KNOT Pools

| KNOT ID | Pool (TT) | Rationale |
|---------|----------:|-----------|
| `KNOT-ATA28-10-00-001` | 200 | Tank geometry — gates all caudal system layout |
| `KNOT-ATA28-10-00-002` | 150 | Al-Li 2195 at 20 K — novel material regime |
| `KNOT-ATA28-20-00-001` | 250 | NH₃ cryo-shield (OI-2) — gates NH₃ architecture viability |
| `KNOT-ATA28-20-00-002` | 120 | Hastelloy C-276 at –33 °C qualification |
| `KNOT-ATA28-30-00-001` | 100 | Boil-off routing trade — three candidate solutions |
| `KNOT-ATA28-40-00-001` | **500** | Cracker efficiency — highest-value KNOT in programme |
| `KNOT-ATA28-40-00-002` | 300 | Cracker heat balance — gates ATA 75 ICD |
| `KNOT-ATA28-40-00-003` | 200 | Cracker cold-start — operational readiness |
| `KNOT-ATA28-40-00-004` | 180 | Catalyst life model — gates ATA 05 MRO interval |
| `KNOT-ATA28-70-00-001` | 150 | H₂ embrittlement monitoring architecture |
| `KNOT-ATA28-70-00-002` | 130 | NH₃ contamination detection threshold |
| **WTW Total** | **2,280** | |

### 11.2 BWB KNOT Pools

| KNOT ID | Pool (TT) | Rationale |
|---------|----------:|-----------|
| `KNOT-ATA28-BWB-10-00-001` | **400** | Conformal tank geometry — gates entire BWB C2 architecture |
| `KNOT-ATA28-BWB-10-00-002` | 200 | Tank material selection — depends on QRG-2 geometry |
| `KNOT-ATA28-BWB-10-Q-001` | **350** | NISQ benchmark — gates QRG-1 programme decision |
| `KNOT-ATA28-BWB-50-00-001` | 150 | FC feed valve cryogenic qualification |
| **BWB Total** | **1,100** | |

### 11.3 Cross-Programme Spillover Links

```yaml
spillover_links:
  - source: WTW · KNOT-ATA28-40-00-001   # cracker kinetic model
    target: BWB · KNOT-ATA24-24-00-FC-001 # FC stack heat rejection
    coeff:  0.50
    note:   "Cracker thermal efficiency data reduces uncertainty in BWB FC heat rejection model"

  - source: WTW · KNOT-ATA28-40-00-002   # cracker heat balance
    target: BWB · KNOT-ATA24-24-00-FC-001
    coeff:  0.30

  - source: WTW · KNOT-ATA28-10-00-002   # Al-Li 2195 at 20 K
    target: BWB · KNOT-ATA28-BWB-10-00-002 # BWB conformal tank material
    coeff:  0.50
    note:   "Cryogenic Al-Li material data directly applicable to BWB tank candidate evaluation"
```

---

## 12 · RACI

| Activity | R | A | C | I |
|----------|---|---|---|---|
| LH₂ tank design and analysis (WTW + BWB) | STK_SE | STK_SE | STK_SAF; STK_CERT | STK_PMO |
| NH₃ cracker design and analysis (WTW) | STK_SE | STK_SE | STK_SAF; STK_TEST | STK_PMO |
| Conformal tank quantum topology (BWB) | STK_AI | STK_SE | STK_SE; STK_CERT | STK_PMO |
| FMEA / FTA — ATA 28 systems | STK_SAF | STK_SE | STK_CERT; STK_TEST | STK_PMO |
| LC04 DD / ICD authorship | STK_SE | STK_SE | STK_SAF; STK_CM | STK_CERT |
| LC05 analysis model peer review | STK_SE | STK_SE | STK_SAF | STK_CERT |
| BREX validation — WTW branch | STK_CM | STK_CM | STK_SE | STK_CERT |
| BREX validation — BWB branch | STK_CM | STK_CM | STK_AI; STK_SE | STK_CERT |
| KNOT closure signoff | Per KNOT AoR | STK_PMO | STK_CERT; STK_SAF | All |
| TT award distribution | STK_DATA | STK_PMO | STK_CM | All |
| ATA 04 ALI input — tank structural life | STK_SE | STK_CERT | STK_SAF; STK_TEST | STK_PMO |
| ATA 05 MRO interval — catalyst replacement | STK_MRO | STK_CERT | STK_SE; STK_SAF | STK_PMO |

---

## 13 · Closure Criteria — ATA 28 KNOTs

A KNOT in ATA 28 is **CLOSED** when all of the following are satisfied:

1. ✅ All planned KNUs reach `COMPLETE` or `ACCEPTED`
2. ✅ Residual drops to or below target (`R_before → R_target`)
3. ✅ All PUB DMs pass programme BREX validation (WTW or BWB BREX respectively)
4. ✅ Full trace chain resolves: `LC02 REQ ↔ LC04 DD ↔ LC05 ANA ↔ LC06 TEST ↔ CSDB DM`
5. ✅ LC04 design definition artifact approved by programme Chief Engineer
6. ✅ LC05 analysis model peer-reviewed and signed off by STK_SAF
7. ✅ Signoffs captured in LC06 evidence pack with SHA-256 hash
8. ✅ TT rewards distributed and logged in `finance/ledger.json` (ATA 96 hash-chain)

> ⚠️ **KNOT-ATA28-40-00-001 additional criterion:**
> Bench-test data at representative altitude conditions required in `LC06/`.
> Kinetic model `ANA-ATA28-WTW-004.pdf` alone is **not sufficient** for closure.

---

## 14 · Open Items Cross-Reference

| OI ID | Description | Resolving KNOT | Programme | Target |
|-------|-------------|----------------|-----------|--------|
| OI-2 | NH₃ cryo-shield boil-off reduction ≥30 % — achievable at cruise conditions? | `KNOT-ATA28-20-00-001` | WTW | 2027-Q1 |
| OI-6 | BWB quantum benchmark: does NISQ topology outperform classical optimiser for conformal tank? | `KNOT-ATA28-BWB-10-Q-001` | BWB | 2027-Q4 |

---

## 15 · Folder Structure (canonical pattern)

```
ATA_28-FUEL/
└── ATA-28-fuel/
    ├── 28-00-general/
    │   └── 28-00-00-00-general/
    │       ├── README.md            ← this document (chapter root)
    │       ├── SSOT/
    │       │   ├── LC01_PROBLEM_STATEMENT/
    │       │   │   ├── KNOTS.csv
    │       │   │   ├── KNU_PLAN.csv
    │       │   │   ├── TIMELINE.csv
    │       │   │   ├── RACI.csv
    │       │   │   ├── TOKENOMICS_TT.yaml
    │       │   │   └── AWARDS_TT.csv
    │       │   ├── LC02_SYSTEM_REQUIREMENTS/
    │       │   ├── LC03_SAFETY_RELIABILITY/
    │       │   ├── LC04_DESIGN_DEFINITION/
    │       │   ├── LC05_ANALYSIS_MODELS/
    │       │   ├── LC06_VERIFICATION/
    │       │   ├── LC07_VALIDATION/
    │       │   ├── LC08_CONFIGURATION/
    │       │   ├── LC09_PRODUCTION/
    │       │   ├── LC10_OPERATIONS/
    │       │   ├── LC11_MAINTENANCE/
    │       │   ├── LC12_CUSTOMER_CARE/
    │       │   ├── LC13_TRAINING/
    │       │   └── LC14_RETIREMENT_CIRCULARITY/
    │       └── PUB/
    │           └── AMM/
    │               ├── CSDB/
    │               │   ├── DM/
    │               │   ├── PM/
    │               │   ├── DML/
    │               │   ├── BREX/
    │               │   ├── ICN/
    │               │   └── APPLICABILITY/
    │               ├── EXPORT/
    │               └── IETP/
    ├── 28-10-storage/             ← LH₂ (both) · NH₃ (WTW only)
    ├── 28-20-distribution/        ← boil-off/NH₃ (WTW) · LH₂ manifold (BWB)
    ├── 28-30-dump/                ← boil-off recovery (WTW) · Reserved (BWB)
    ├── 28-40-indicating/          ← NH₃ cracker (WTW) · Reserved (BWB)
    ├── 28-50-reserved/            ← Reserved (WTW) · FC feed metering (BWB)
    ├── 28-70-monitoring/          ← H₂ + NH₃ monitoring (WTW) · H₂ only (BWB)
    └── 28-90-tables-schemas-index/
```

---

## 16 · Related Documents

| Document | Path |
|----------|------|
| Inheritance Boundary Declaration | `AMPEL360-FAM-IBD-001-RevB.md` |
| Boundary YAML (CI) | `inheritance_boundary.yaml` |
| AMPEL360-COMMON README | `AMPEL360-COMMON/README.md` |
| ATA 47 — Inert Gas System (WTW cracker N₂) | `T/E1-ENVIRONMENT/ATA_47-INERT_GAS_SYSTEM/` |
| ATA 75 — Engine Air (WTW waste heat feed) | `T/P-PROPULSION/ATA_75-AIR/` |
| ATA 26 — Fire Protection (forked) | `T/E1-ENVIRONMENT/ATA_26-FIRE_PROTECTION/` |
| ATA 24 — Electrical Power (forked) | `T/E2-ENERGY/ATA_24-ELECTRICAL_POWER/` |
| ATA 57 — Wings / BWB centerbody (forked) | `T/A-AIRFRAME_CABINS/ATA_57-WINGS/` |
| ATA 04 — Airworthiness Limitations | `O-ORGANIZATIONS/ATA_04-AIRWORTHINESS_LIMITATIONS/` |
| ATA 05 — Time Limits (catalyst interval) | `O-ORGANIZATIONS/ATA_05-TIME_LIMITS_MAINT_CHECKS/` |
| NH₃ GSE Infrastructure (WTW only) | `AMPEL360-WTW/I-INFRASTRUCTURES/NH3-GSE/` |
| WTW BREX | `AMPEL360-WTW/PUB/AMM/CSDB/BREX/BREX-AMPEL360-WTW-v0.1.xml` |
| BWB BREX | `AMPEL360-BWB/PUB/AMM/CSDB/BREX/BREX-AMPEL360-BWB-v0.1.xml` |
| ATA 96 Governance / IBCR Log | `N-NEURAL_NETWORKS/ATA_96/96-70/IBCR_LOG.csv` |
| TT Ledger | `finance/ledger.json` |

---

## Revision History

| Rev | Date | Change | Author |
|-----|------|--------|--------|
| A | 2026-02-22 | Initial issue. Dual-branch WTW + BWB documentation: architecture summary, section maps (§3), LC01–LC14 assignments (§4), LC04 DD artifacts (§5), LC05 analysis models (§6), KNOT register 11 WTW + 4 BWB (§7), KNU plan examples (§8), BREX rules with cross-contamination CI guards (§9), DM naming (§10), TT pools 2280 WTW + 1100 BWB (§11), RACI (§12), closure criteria (§13). | A. Pelliccia |

---

*AMPEL360 · T-TECHNOLOGIES / C2-CIRCULAR_CRYOGENIC_CELLS / ATA 28 — Fuel System*
*⚠️ PRIMARY CUT · IBD-001 Rev B · OPT-IN v1.1 · 2026-02-22*
