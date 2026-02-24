# ARCH — BWB Envelope Protection Strategy

**Doc ID:** T-A2-ATA22-BWB-ARCH-003
**Delta Ref:** DELTA-BWB-22-003
**Variant:** AMPEL360 Q100 BWB
**Status:** DRAFT
**Lifecycle:** Standard (LC01–LC13)
**Baseline Ref:** `../../..` (ATA 22 SHARED)

---

## 1. Delta Statement

Envelope protection limits for the AMPEL360 Q100 BWB differ from the SHARED baseline and from WTW. The swept composite flying-wing planform exhibits different stall onset, buffet boundary, and structural load factor characteristics. All limit values are **TBD (LC03)** pending aerodynamic and structural model maturation. This document describes the protection architecture delta only.

---

## 2. Protection Functions — BWB Delta

The following protection functions require BWB-specific parameterisation:

| Protection Function | SHARED Baseline | BWB Delta Required | LC Gate |
|---|---|---|---|
| Alpha (AoA) high limit | Conventional stall angle | BWB buffet-onset alpha (TBD) | LC03 |
| Alpha (AoA) low limit | Stall warning onset | Same function; threshold TBD | LC03 |
| Beta (sideslip) limit | Symmetric — yaw damper | BWB has reduced fin contribution; beta limit TBD | LC03 |
| Load factor (nz) high | +2.5 g (CS-25.337) | Same regulation; structural analysis confirms value TBD | LC03 |
| Load factor (nz) low | −1.0 g (CS-25.337) | Same regulation; structural analysis confirms value TBD | LC03 |
| High-speed (VMO/MMO) | Conventional | BWB aeroelastic flutter boundary TBD at LC03 | LC03 |
| Structural stall boundary | N/A (conventional) | BWB composite panel load relief point — TBD | LC04 |
| Buffet onset margin | Standard AMC | BWB specific — wind-tunnel data required | LC03 |

---

## 3. Protection Architecture (Stub)

```
Air Data + Inertial Sensors
(ATA 34 / ADIRS)
        │
        ▼
┌─────────────────────────────────┐
│   Envelope Monitor              │
│   Inputs: α, β, nz, V, M, h    │
│   Limits: All TBD (LC03)        │
└─────────┬───────────────────────┘
          │ Soft limit warning
          │ Hard limit demand
          ▼
┌─────────────────────────────────┐
│   Protection Demand Generator   │
│   (Modifies NDI pseudo-control) │
│   Priority: Hard > Soft > Auto  │
└─────────┬───────────────────────┘
          │
          ▼
   NDI Inner Loop / Control Allocation
   (DELTA-BWB-22-001, DELTA-BWB-22-002)
```

**Protection architecture integration method with NDI** (limit integration vs. reference model governor): **TBD (LC03)**.

---

## 4. Alerting and Mode Reversion

Envelope exceedance alerting and autoflight mode reversion strategies are addressed in:
- `../ATA22_BWB_ACCEPTABILITY/ACC_BWB_MODE_REVERSION_AND_ALERTING.md`

---

## 5. CS-25 Compliance Hooks

| Regulation | Topic | Status |
|---|---|---|
| CS-25.143(f) | Flight envelope protection | STUB — thresholds TBD (LC03) |
| CS-25.253 | High-speed characteristics | STUB — aeroelastic analysis TBD (LC03) |
| CS-25.337 | Limit manoeuvring load factors | STUB — structural confirmation TBD (LC03) |
| CS-25.1309 | Safety assessment for protection failure | STUB — FHA TBD (LC04) |

---

## 6. Open Items

| Item | Description | LC Gate |
|---|---|---|
| OI-ENV-001 | Alpha buffet-onset boundary from wind-tunnel/CFD | LC03 |
| OI-ENV-002 | Beta limit for BWB reduced-fin configuration | LC03 |
| OI-ENV-003 | Aeroelastic flutter clearance for VMO/MMO | LC03 |
| OI-ENV-004 | Protection integration method with NDI | LC03 |
| OI-ENV-005 | Composite structural stall load relief point | LC04 |
