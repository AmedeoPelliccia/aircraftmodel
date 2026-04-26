# ARCH — BWB Control Allocation and Effectors

**Doc ID:** T-A2-ATA22-BWB-ARCH-002
**Delta Ref:** DELTA-BWB-22-001
**Variant:** AMPEL360 Q100 BWB
**Status:** DRAFT
**Lifecycle:** Standard (LC01–LC13)
**Baseline Ref:** `../../..` (ATA 22 SHARED)

---

## 1. Delta Statement

The SHARED baseline assumes conventional elevator and aileron surfaces with direct pitch and roll channel mapping. The AMPEL360 Q100 BWB replaces these with a distributed trailing-edge array of elevons and spoilerons. Autoflight surface demands must be resolved through a **control allocation matrix** before being sent to individual actuators. This document describes the delta architecture only.

---

## 2. Effector Array Description (Stub)

The BWB trailing-edge array is divided into spanwise segments. Exact segment count and geometry are **TBD (LC02)** pending structural and aerodynamic model maturation.

| Effector Group | Type | Primary Function | Secondary Function |
|---|---|---|---|
| Inboard Elevons (IE) | Elevon | Pitch moment | *(TBD)* |
| Mid Elevons (ME) | Elevon | Pitch + roll | *(TBD)* |
| Outboard Elevons (OE) | Elevon | Roll moment | *(TBD)* |
| Spoilerons (SP) | Spoileron | Roll augmentation | Speed brake |
| Segment count | TBD | TBD | TBD |

Refer to `MODELS/effector_map.yaml` for machine-readable geometry stub.

---

## 3. Control Allocation Architecture (Stub)

The control allocation module receives generalised force/moment demands from the NDI inner loop (DELTA-BWB-22-002) and distributes them across available effectors:

```
NDI Pseudo-Control Vector:
  [ΔL_demand, ΔM_demand, ΔN_demand, ΔFz_demand]
            │
            ▼
  Control Allocation Solver
  (Weighted pseudo-inverse or constrained optimisation — TBD LC03)
            │
            ▼
  Individual Surface Deflections:
  [δ_IE_L, δ_IE_R, δ_ME_L, δ_ME_R, δ_OE_L, δ_OE_R, δ_SP_L, δ_SP_R, ...]
```

**Allocation method** (pseudo-inverse vs constrained optimisation vs priority-based): **TBD (LC03)**.

**Actuator rate and deflection limits per surface**: **TBD (LC03)** — see `MODELS/effector_map.yaml`.

---

## 4. Autoflight-Specific Considerations

| Topic | Description | LC Gate |
|---|---|---|
| Saturation management | Individual surface saturation must not destabilise autoflight loop | LC03 |
| Failure reconfiguration | Loss of one or more surfaces — autoflight must degrade gracefully | LC04 |
| Cross-axis coupling | Elevon pitch/roll coupling managed by allocation solver | LC03 |
| Spoileron in autoflight | Spoilerons used for roll in autoflight — interaction with speed-brake logic TBD | LC04 |

---

## 5. Interface with ATA 27

Control allocation outputs are passed to the ATA 27 Flight Control System as position demands. Refer to:
- `../ATA22_BWB_INTERFACES/ICD_BWB_EFFECTOR_MAP_001.md`

---

## 6. Open Items

| Item | Description | LC Gate |
|---|---|---|
| OI-CA-001 | Effector segment count and spanwise geometry | LC02 |
| OI-CA-002 | Allocation algorithm selection and performance criteria | LC03 |
| OI-CA-003 | Actuator deflection and rate limits per surface | LC03 |
| OI-CA-004 | Reconfiguration logic for failed surfaces in autoflight | LC04 |
