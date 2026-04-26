# ATA 22 — Auto Flight | BWB Programme Extension Overlay

**Doc ID:** T-A2-ATA22-BWB-OVERLAY-001
**Variant:** AMPEL360 Q100 BWB (Blended Wing Body)
**Overlay Type:** Delta-only over ATA 22 SHARED baseline
**Baseline Ref:** `../..` (ATA_22-AUTO_FLIGHT root)
**Status:** DRAFT
**Lifecycle:** Standard (LC01–LC13)

---

## Purpose

This overlay captures **BWB-specific deltas** to the ATA 22 Auto Flight SHARED baseline. It SHALL NOT duplicate SHARED baseline content. All entries reference the SHARED baseline and document only deviations, additions, or constraints arising from the BWB flying-wing planform of the AMPEL360 Q100.

---

## BWB Aerodynamic & Systems Context

The AMPEL360 Q100 BWB is a swept flying-wing design introducing the following ATA 22 deltas versus the SHARED baseline:

| Delta ID | Topic | Key Driver |
|---|---|---|
| DELTA-BWB-22-001 | Effector allocation | Distributed elevon/spoileron array replaces conventional elevator/aileron |
| DELTA-BWB-22-002 | Non-linear control laws | Non-linear pitch-heave coupling requires NDI + robustness augmentation |
| DELTA-BWB-22-003 | Envelope protection strategy | Swept composite planform stall/buffet boundaries differ from WTW |
| DELTA-BWB-22-004 | FMS performance polar | Different L/D optimum speeds and flight levels vs WTW |
| DELTA-BWB-22-005 | Propulsion guidance coupling | 4× distributed engines require asymmetric thrust management in autoflight |

---

## Certification Basis

| Regulation | Topic |
|---|---|
| CS-25.1329 | Automatic Pilot System |
| CS-25.1302 | Installed Equipment |
| CS-25.143 | Controllability and Manoeuvrability |
| CS-25.253 | High-Speed Characteristics |
| DO-178C DAL-B | Auto-flight software |
| DO-254 | Complex electronics (FCC hardware) |

Special Condition SC-FCS-001 applies where NDI control laws exceed the scope of conventional CS-25.1329 means of compliance. TBD confirmation at LC03.

---

## Overlay File Index

| File / Folder | Description |
|---|---|
| `ATA22_BWB_INDEX.yaml` | Machine-readable overlay manifest |
| `ATA22_BWB_DELTA_LOG.yaml` | Change log for all deltas |
| `ATA22_BWB_COMPLIANCE_MATRIX.md` | CS-25 compliance traceability |
| `ATA22_BWB_ARCHITECTURE/` | BWB autoflight topology, control allocation, envelope strategy |
| `ATA22_BWB_INTERFACES/` | ICDs between autoflight and BWB-specific subsystems |
| `ATA22_BWB_REQUIREMENTS/` | Delta requirements by ATA 22 sub-chapter |
| `ATA22_BWB_ACCEPTABILITY/` | Dispatch, degraded mode, and alerting acceptability |
| `ATA22_BWB_VERIFICATION_EVIDENCE/` | Analysis, test, and inspection evidence stubs |

---

## Related Documents

- [ATA 22 SHARED Baseline](../..)
- [ATA 27 — Flight Controls BWB](../../../ATA_27-FLIGHT_CONTROLS/) *(pointer)*
- [ATA 34 — Navigation BWB](../../../ATA_34-NAVIGATION/) *(pointer)*
- [ATA 42 — IMA BWB](../../../ATA_42-IMA/) *(pointer)*
