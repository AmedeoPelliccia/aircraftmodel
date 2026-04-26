# ICD-005 — WTW External Communication Antenna Placement

**ICD ID:** T-A-ATA44-WTW-ICD-005
**Delta Ref:** DELTA-WTW-44-006
**ATA Subchapter:** 44-30 External Communication
**Status:** DRAFT (LC01 — antenna locations at LC03)
**Parent:** [Interfaces README](README.md)

---

## 1) Purpose

Defines the placement and structural envelope constraints for external communication
antennae associated with ATA 44-30 on the WTW variant (satcom, cabin Wi-Fi, cellular
passenger connectivity).

---

## 2) Antenna Inventory

| Antenna ID | Type | Frequency band | Fuselage location | Notes |
|-----------|------|---------------|-------------------|-------|
| ANT-44-01 | Satcom (Ka/Ku band) | 10.7–14.5 GHz | Fuselage crown (FS TBD) | Above CMS crown harness run |
| ANT-44-02 | Passenger Wi-Fi (2.4/5 GHz) | 2.4 GHz / 5 GHz | Overhead crown per zone | 1 per cabin zone (4 off) |
| ANT-44-03 | Cellular (ATG / 4G/5G) | 700 MHz – 2.6 GHz | Fuselage belly (FS TBD) | If fitted — TBD at LC03 |

---

## 3) Structural Interface

| Parameter | WTW Value | Notes |
|-----------|-----------|-------|
| Satcom antenna radome | Conformal radome, 3-bolt attach | Mass TBD kg — LC03 |
| Wi-Fi antenna form | Flush-mount ceiling panel unit | Hidden behind cabin crown liner |
| Structural penetration | Doubler required for satcom | Structural design: ATA 53 |
| RF transparency of structure | CFRP crown panels — RF window TBD | Confirm with antenna supplier LC03 |
| Cable routing | Through crown harness run | Joint ICD with ICD-002 |

---

## 4) WTW-Specific Constraints

> Δ WTW-only:

- Satcom antenna on fuselage crown — no interference with wing carry-through structure.
- Wi-Fi antennae distributed one per cabin zone at overhead crown position.
- WTW CFRP panels require RF transparency validation for satcom band — not applicable to BWB
  where composite outer skin geometry and curvature differ.
- Cellular ATG antenna on belly if installed — WTW belly fairing access panel applies.

---

## 5) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Select satcom supplier and confirm radome form factor | Avionics | LC03 |
| Conduct RF transparency test on WTW crown panel samples | Test | LC07 |
| Define satcom FS from cabin layout and antenna beam angle | Systems | LC03 |

---

## Related Documents

- [REQ_WTW_44_300_EXTERNAL_COMM.yaml](../ATA44_WTW_REQUIREMENTS/REQ_WTW_44_300_EXTERNAL_COMM.yaml)
- [TEST_WTW_RF_COMPLIANCE.md](../ATA44_WTW_VERIFICATION_EVIDENCE/TEST_WTW_RF_COMPLIANCE.md)
