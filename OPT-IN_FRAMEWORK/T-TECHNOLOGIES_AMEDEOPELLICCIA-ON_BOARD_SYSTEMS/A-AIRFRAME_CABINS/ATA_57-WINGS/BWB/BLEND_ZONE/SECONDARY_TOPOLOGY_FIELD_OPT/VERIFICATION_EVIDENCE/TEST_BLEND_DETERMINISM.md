# Test: Blend Zone TDF Optimisation Determinism and Reproducibility

**Evidence ID:** EVI-BWB-57-BZ-003  
**Doc ID:** T-A-ATA57-BWB-BLEND-TST-DET-001  
**Requirement:** BWB-57-TDF-005  
**Regulation:** CS-25.571, CS-25.629  
**Status:** OPEN (stub)  
**LC Gate:** LC57-11  

---

## Objective
Demonstrate that the TDF optimisation solver is deterministic and reproducible:
identical inputs produce identical register maps on repeated runs.

## Test Configuration
- Solver: GA integer (see `MODELS/optimisation_config.yaml`)
- Fixed seed: 42
- Inputs: `MODELS/tdf_patch_definition.yaml` + load spectrum + constraint bounds (all frozen at LC57-03)

## Test Procedure
1. Run optimisation solver with configuration version V1 → record register map M1 + SHA-256 hash H1
2. Re-run optimisation solver with identical configuration → record register map M2 + SHA-256 hash H2
3. Run on alternative compute environment (different OS/hardware) with identical inputs → record M3 + H3
4. Verify: M1 == M2 == M3 (bitwise) and H1 == H2 == H3

## Pass Criterion
SHA-256 hashes H1 = H2 = H3 (identical register maps across all runs)

## Expected Result
TBD — to be executed at LC57-11 certification gate.

## Traceability
- Input: `MODELS/optimisation_config.yaml` (frozen version at LC57-03)
- Output: Test report with hash records (TBD)
- Requirement: `REQ_BWB_57_BLEND_TDF_OPT.yaml` BWB-57-TDF-005
