# ARCH — BWB Autoflight Topology Overview

**Doc ID:** T-A2-ATA22-BWB-ARCH-001
**Delta Ref:** DELTA-BWB-22-002
**Variant:** AMPEL360 Q100 BWB
**Status:** DRAFT
**Lifecycle:** Standard (LC01–LC13)
**Baseline Ref:** `../../..` (ATA 22 SHARED)

---

## 1. Delta Statement

The SHARED baseline autoflight topology assumes a conventional linear control law architecture with direct pitch/roll/yaw channel decomposition. The BWB planform introduces non-linear pitch-heave coupling that renders the SHARED linear architecture insufficient for stable automated flight. This document describes the BWB topology delta only.

---

## 2. BWB Autoflight Topology Overview (Stub)

The AMPEL360 Q100 BWB autoflight architecture is structured as follows:

```
Pilot Input / FMS Guidance Target
         │
         ▼
┌─────────────────────────────────────┐
│   Outer Loop Guidance Manager       │
│   (VNAV / LNAV / Speed modes)       │
│   [BWB L/D polar — DELTA-BWB-22-004]│
└───────────────┬─────────────────────┘
                │ Commanded: γ, χ, V_TAS
                ▼
┌─────────────────────────────────────┐
│   Non-Linear Dynamic Inversion      │
│   (NDI) Inner Loop                  │
│   [Explicit model-following]        │
│   [DELTA-BWB-22-002]                │
└───────────────┬─────────────────────┘
                │ Pseudo-control: p, q, r demands
                ▼
┌─────────────────────────────────────┐
│   Robustness Augmentation           │
│   (H∞ / μ-synthesis — TBD LC03)     │
└───────────────┬─────────────────────┘
                │ Surface demand vector
                ▼
┌─────────────────────────────────────┐
│   Control Allocation                │
│   (Elevon/Spoileron array)          │
│   [DELTA-BWB-22-001]                │
└───────────────┬─────────────────────┘
                │ Individual surface deflections
                ▼
┌─────────────────────────────────────┐
│   Envelope Protection Monitor       │
│   (α/β, nz, structural limits)      │
│   [DELTA-BWB-22-003]                │
└───────────────┬─────────────────────┘
                │ Limited/monitored commands
                ▼
       Actuator Interface (ATA 27)
```

**Note:** Block parameters, loop gains, and bandwidth requirements are all **TBD (LC03)**.

---

## 3. Key BWB-Specific Design Choices

| Item | SHARED Baseline | BWB Delta | LC Gate |
|---|---|---|---|
| Control law architecture | Linear PID / classical | Non-linear dynamic inversion (NDI) | LC03 |
| Pitch-heave decoupling | Assumed negligible | Explicit NDI inversion required | LC03 |
| Robustness method | Classical gain/phase margins | H∞ or μ-synthesis (TBD) | LC03 |
| FCC processing load | Baseline estimate | Increased for NDI — TBD | LC04 |
| Mode annunciation | SHARED | Identical unless new BWB modes added (TBD) | LC04 |

---

## 4. FCC Platform

Flight Control Computer (FCC) hosting autoflight functions: **TBD (LC02)**.

Software classification: **DO-178C DAL-B**.

Hardware classification: **DO-254** (complex electronics — FCC FPGA/ASIC TBD at LC02).

---

## 5. Open Items

| Item | Description | LC Gate |
|---|---|---|
| OI-ARCH-001 | Robustness augmentation method selection (H∞ vs μ-synthesis) | LC03 |
| OI-ARCH-002 | FCC processing margin with NDI real-time execution | LC04 |
| OI-ARCH-003 | New guidance mode additions specific to BWB (if any) | LC04 |
| OI-ARCH-004 | SC-FCS-001 applicability confirmation | LC03 |
