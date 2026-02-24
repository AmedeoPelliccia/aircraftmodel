# ANALYSIS — BWB Control Law Stability (CS-25.1329, CS-25.143)

**Evidence ID:** EV-BWB-22-002
**Doc ID:** T-A2-ATA22-BWB-ANALYSIS-002
**Delta Ref:** DELTA-BWB-22-002
**CS-25 Ref:** CS-25.1329, CS-25.143
**Method:** Analytical (NDI stability analysis + robustness margins)
**Status:** STUB
**Lifecycle:** Standard (LC01–LC13)
**Content Deferred To:** LC03

---

## 1. Purpose

This analysis stub defines the scope and methodology for demonstrating stability and performance of the BWB Non-Linear Dynamic Inversion (NDI) control law under CS-25.1329 and CS-25.143. Full analysis is deferred to LC03, when the non-linear aerodynamic model is available.

---

## 2. Analysis Scope

### 2.1 NDI Inner Loop Stability

The analysis shall demonstrate that the NDI inner loop achieves stable closed-loop response for all conditions within the BWB operational flight envelope (OFE):

| Parameter | Range | Values | LC Gate |
|---|---|---|---|
| Mach number | TBD to TBD | TBD | LC03 |
| Altitude (ft) | TBD to TBD | TBD | LC03 |
| Aircraft weight (kg) | TBD to TBD | TBD | LC03 |
| CG range (%MAC) | TBD to TBD | TBD | LC03 |
| Flap/slat configuration | All | All defined configs | LC03 |

### 2.2 Robustness Analysis

The robustness augmentation controller shall be analysed for:

| Analysis Item | Method | Acceptance Criterion | LC Gate |
|---|---|---|---|
| Gain margin | Frequency domain (TBD) | ≥ TBD dB (LC03) | LC03 |
| Phase margin | Frequency domain | ≥ TBD deg (LC03) | LC03 |
| Aerodynamic model uncertainty | μ-analysis or Monte Carlo | Stability maintained for TBD % uncertainty (LC03) | LC03 |
| Structural mode coupling | Notch filter analysis | Aeroservoelastic clearance TBD (LC04) | LC04 |

**Robustness method (H∞ vs μ-synthesis vs other):** TBD (LC03).

### 2.3 Pilot-Induced Oscillation (PIO) Assessment

BWB pitch-to-flight-path coupling ratio may increase PIO susceptibility. The analysis shall assess:
- Category I PIO susceptibility per ADS-33 criteria (adapted for fixed-wing): **TBD (LC04)**
- Flight director cue scaling interaction with manual control: **TBD (LC04)**

---

## 3. CS-25.1329 Compliance Basis (Stub)

| CS-25.1329 Paragraph | Compliance Method | Notes |
|---|---|---|
| (a) System design | Analysis + Review | NDI architecture review at LC03 |
| (b) Override forces | Test | Iron-bird at LC05 |
| (c) Engagement/disengagement | Test | Simulator at LC05 |
| (d) Warnings | Test | FCC software test at LC05 |
| (i) Failure modes | Analysis (FHA/SSA) | EV-BWB-22-001 |

Special Condition SC-FCS-001 applicability to be determined at LC03.

---

## 4. Non-Linear Aerodynamic Model Requirements

The analysis depends on a validated BWB non-linear aerodynamic model providing:
- Full 6-DOF force and moment coefficients across OFE
- High-alpha behaviour including buffet onset
- Aeroelastic effects (structural deformation effects on aerodynamics)

**Model availability:** TBD (LC03) — dependent on wind-tunnel campaign completion.

---

## 5. Open Items

| Item | Description | LC Gate |
|---|---|---|
| OI-CL-001 | NDI inner loop design completion | LC03 |
| OI-CL-002 | Robustness augmentation method selection | LC03 |
| OI-CL-003 | Non-linear aerodynamic model availability | LC03 |
| OI-CL-004 | Acceptance criteria for gain/phase/uncertainty margins | LC03 |
| OI-CL-005 | Aeroservoelastic clearance | LC04 |
| OI-CL-006 | PIO susceptibility assessment | LC04 |
