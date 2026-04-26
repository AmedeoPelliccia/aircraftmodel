# TEST: WTW Rib Spacing Optimisation — Determinism and Reproducibility

**Evidence ID:** EVI-WTW-57-RIBOPT-003
**Type:** Test
**Doc ID:** T-A-ATA57-WTW-RIBOPT-TEST-DET-001
**Lifecycle gate:** LC57-03
**Status:** STUB — Test procedure defined; execution pending tool deployment

---

## 1. Objective
Verify that the rib spacing optimisation module produces bit-for-bit identical output
register vectors from identical inputs on multiple independent runs, platforms, and
interpreter versions (REQ-WTW-57-RIBOPT-002). Also verify 8-bit encoding round-trip
correctness (REQ-WTW-57-RIBOPT-001) and boundary condition enforcement (REQ-WTW-57-RIBOPT-005).

---

## 2. Applicable Requirements

| Requirement | Test Objective |
|------------|---------------|
| REQ-WTW-57-RIBOPT-001 | 8-bit encoding round-trip: encode → decode → compare |
| REQ-WTW-57-RIBOPT-002 | Determinism: two identical runs produce identical SHA-256 output hash |
| REQ-WTW-57-RIBOPT-005 | Boundary enforcement: fixed bays remain at prescribed values |

---

## 3. Test Cases

### TC-001: Encoding Round-Trip
**Objective:** Verify that for all 256 register values, physical spacing decoded from register matches the encoded value to within ±0.001 mm.

**Procedure:**
1. For r ∈ {0, 1, ..., 255}:
   a. Compute S_physical = S_min + r × Δs
   b. Compute r_back = round((S_physical − S_min) / Δs)
   c. Assert r_back == r
2. Record PASS/FAIL per register value

**Pass Criterion:** 256/256 values round-trip correctly (zero failures)

**Status:** TBD

---

### TC-002: Determinism — Single Platform
**Objective:** Verify two consecutive runs of the GA with identical config and random seed produce identical output.

**Procedure:**
1. Execute optimisation run A with `optimisation_config.yaml` (random_seed = 42)
2. Execute optimisation run B with identical config
3. Compute SHA-256 hash of output register YAML for runs A and B
4. Assert SHA-256(A) == SHA-256(B)

**Pass Criterion:** SHA-256 hashes are identical

**Status:** TBD

---

### TC-003: Determinism — Cross-Platform
**Objective:** Verify identical output on two different hardware/OS configurations.

**Procedure:**
1. Execute run on Platform X (reference) → record SHA-256
2. Execute run on Platform Y (alternate) → record SHA-256
3. Assert SHA-256(X) == SHA-256(Y)

**Platform Configurations:**
| Platform | OS | Python Version | Notes |
|---------|-----|--------------|-------|
| X | TBD | TBD | Reference |
| Y | TBD | TBD | Alternate |

**Pass Criterion:** SHA-256 hashes are identical

**Status:** TBD

---

### TC-004: Boundary Condition Enforcement
**Objective:** Verify that fixed rib bays (RB-001, RB-005, RB-008, RB-013, RB-016 per rib_bay_definition.yaml) retain their prescribed null/TBD values after optimisation.

**Procedure:**
1. Execute optimisation run with `rib_bay_definition.yaml` (6 fixed bays)
2. Extract register values for all fixed bays from output
3. Assert register_value == null for all bays where fixed: true

**Pass Criterion:** All 6 fixed bays retain null register_value (unchanged by GA)

**Status:** TBD

---

### TC-005: Constraint Violation Rejection
**Objective:** Verify that the optimisation does NOT return a register vector that violates the fatigue or divergence constraints when a valid solution exists.

**Procedure:**
1. Configure a test case where uniform maximum spacing (register = 255 all bays) violates both fatigue and divergence constraints
2. Execute optimisation
3. Verify output register vector satisfies both constraints

**Pass Criterion:** All constraints satisfied in output

**Status:** TBD

---

## 4. Test Execution Record (TBD)

| Test Case | Run Date | Platform | SHA-256 / Result | Pass/Fail |
|----------|---------|---------|-----------------|----------|
| TC-001 | TBD | TBD | TBD | TBD |
| TC-002 | TBD | TBD | TBD | TBD |
| TC-003 | TBD | TBD | TBD | TBD |
| TC-004 | TBD | TBD | TBD | TBD |
| TC-005 | TBD | TBD | TBD | TBD |

---

> **Status:** STUB. Test procedure is defined. Execution pending tool deployment at LC57-03.
> All test cases must PASS before LC57-03 exit gate (Detailed Design Review DDR-57).
