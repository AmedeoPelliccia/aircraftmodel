# ANALYSIS — BWB Autoflight Safety Assessment (CS-25.1309)

**Evidence ID:** EV-BWB-22-001
**Doc ID:** T-A2-ATA22-BWB-ANALYSIS-001
**Delta Refs:** DELTA-BWB-22-001, DELTA-BWB-22-002, DELTA-BWB-22-003, DELTA-BWB-22-005
**CS-25 Ref:** CS-25.1309
**Method:** FHA + System Safety Assessment (SSA)
**Status:** STUB
**Lifecycle:** Standard (LC01–LC13)
**Content Deferred To:** LC04

---

## 1. Purpose

This analysis stub defines the scope and structure of the BWB Autoflight System Safety Assessment (SSA) in accordance with CS-25.1309 and AMC 25.1309. Full content is deferred to LC04, when the BWB FCC architecture and aerodynamic model are sufficiently mature.

---

## 2. Functional Hazard Assessment (FHA) Scope — BWB Delta

The FHA shall assess the following BWB-specific autoflight functions as additions to the SHARED baseline FHA:

| Function | Failure Condition | Expected Classification | Probability Target | LC Gate |
|---|---|---|---|---|
| NDI Inner Loop (DELTA-BWB-22-002) | Loss of NDI — reversion to degraded mode | Hazardous | ≤ 10⁻⁷ per FH | LC04 |
| NDI Divergence (DELTA-BWB-22-002) | Uncommanded aircraft excursion during AP engaged | Catastrophic | ≤ 10⁻⁹ per FH | LC04 |
| Control Allocation (DELTA-BWB-22-001) | All autoflight surface commands frozen/zeroed | Catastrophic | ≤ 10⁻⁹ per FH | LC04 |
| Envelope Protection (DELTA-BWB-22-003) | Failure to protect at buffet boundary | Hazardous | ≤ 10⁻⁷ per FH | LC04 |
| Auto-Thrust 4-engine (DELTA-BWB-22-005) | Uncontrolled full thrust asymmetry | Hazardous | ≤ 10⁻⁷ per FH | LC04 |

**Note:** Classification and probability targets are **TBD (LC04)**. Values above are preliminary engineering estimates only.

---

## 3. SSA Structure (Planned)

The SSA shall include:

1. **Fault Tree Analysis (FTA)** — top-down from FHA failure conditions to basic events for each BWB-specific function
2. **Failure Modes and Effects Analysis (FMEA)** — bottom-up for FCC NDI module, control allocation module, and FADEC 4-channel AT interface
3. **Common Cause Analysis (CCA)** — including:
   - Zonal Safety Analysis (ZSA) for FCC rack and FADEC installations
   - Particular Risks Analysis (PRA) for fire, lightning (composite planform — HIRF)
   - Common Mode Analysis (CMA) for NDI software/hardware dissimilarity

---

## 4. HIRF / Lightning Considerations (BWB Delta)

The composite flying-wing planform of the BWB may have different HIRF and lightning indirect effects characteristics compared to conventional metal fuselage aircraft. The SSA CCA shall assess:

- Composite skin shielding effectiveness for avionics bays: **TBD (LC03)**
- Lightning strike attachment points and current distribution: **TBD (LC03)**
- HIRF protection for NDI-bearing FCC: **TBD (LC04)**

---

## 5. Open Items

| Item | Description | LC Gate |
|---|---|---|
| OI-SA-001 | Complete FHA for all BWB-specific functions | LC04 |
| OI-SA-002 | FTA for NDI divergence (Catastrophic failure condition) | LC04 |
| OI-SA-003 | FMEA for control allocation module | LC04 |
| OI-SA-004 | HIRF/lightning assessment for composite planform | LC03 |
| OI-SA-005 | Submit FHA to certifying authority | LC04 |
