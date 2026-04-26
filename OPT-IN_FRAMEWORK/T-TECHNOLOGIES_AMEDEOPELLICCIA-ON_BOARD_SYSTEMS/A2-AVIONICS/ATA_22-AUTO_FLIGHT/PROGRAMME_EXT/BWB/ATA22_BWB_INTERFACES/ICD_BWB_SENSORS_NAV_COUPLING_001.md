# ICD — BWB Autoflight to Navigation / ADIRS Sensor Coupling

**ICD ID:** ICD-BWB-22-002
**Doc ID:** T-A2-ATA22-BWB-ICD-002
**Delta Ref:** DELTA-BWB-22-004
**System A:** ATA 22 Auto Flight (FCC)
**System B:** ATA 34 Navigation / ADIRS
**Status:** STUB
**Lifecycle:** Standard (LC01–LC13)
**Baseline Ref:** `../../..` (ATA 22 SHARED)

---

## 1. Delta Statement

The SHARED baseline navigation/sensor coupling is assumed applicable to BWB with the following additions and modifications driven by:
- BWB NDI requiring higher-rate alpha/beta measurements (DELTA-BWB-22-002)
- BWB FMS VNAV requiring BWB-specific performance polar data from navigation database (DELTA-BWB-22-004)

---

## 2. Interface Additions and Modifications (Stub)

| Parameter | SHARED Baseline | BWB Delta | LC Gate |
|---|---|---|---|
| Alpha (AoA) measurement | Standard ADIRS | Higher rate required for NDI — TBD | LC03 |
| Beta (sideslip) measurement | Standard ADIRS | Higher rate required for NDI — TBD | LC03 |
| Performance polar data | SHARED FMS database | BWB L/D table separate partition in FMS nav database | LC03 |
| Optimum altitude schedule | SHARED | BWB-specific schedule — TBD | LC03 |
| ECON speed schedule | SHARED | BWB-specific schedule — TBD | LC03 |
| Step climb criteria | SHARED | BWB-specific crossover altitudes — TBD | LC04 |

---

## 3. Data Items — Delta Only (Stub)

| Signal Name | Direction | Units | Range | Notes | Status |
|---|---|---|---|---|---|
| ALPHA_HIGHRATE | ADIRS → FCC | deg | TBD (LC03) | For NDI inner loop | STUB |
| BETA_HIGHRATE | ADIRS → FCC | deg | TBD (LC03) | For NDI inner loop | STUB |
| BWB_PERF_POLAR_REF | FMS → FCC | Discrete table ID | N/A | BWB polar dataset active flag | STUB |
| OPTIMUM_FL_BWB | FMS → FCC | Flight Level | TBD | BWB-specific optimum altitude | STUB |
| ECON_MACH_BWB | FMS → FCC | Mach | TBD | BWB ECON speed | STUB |

---

## 4. Open Items

| Item | Description | LC Gate |
|---|---|---|
| OI-ICD002-001 | High-rate alpha/beta sample rate from NDI bandwidth requirement | LC03 |
| OI-ICD002-002 | Populate BWB performance polar tables in FMS database | LC03 |
| OI-ICD002-003 | Define optimum FL and ECON Mach schedule for BWB | LC03 |
