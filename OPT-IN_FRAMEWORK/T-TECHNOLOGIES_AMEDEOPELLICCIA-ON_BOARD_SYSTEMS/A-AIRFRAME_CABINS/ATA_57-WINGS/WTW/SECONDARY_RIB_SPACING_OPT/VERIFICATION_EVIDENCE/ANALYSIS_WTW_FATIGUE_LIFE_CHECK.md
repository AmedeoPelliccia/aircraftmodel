# ANALYSIS: WTW Wing Rib Spacing — Fatigue Life Check

**Evidence ID:** EVI-WTW-57-RIBOPT-001
**Type:** Analysis
**Doc ID:** T-A-ATA57-WTW-RIBOPT-ANA-FAT-001
**Lifecycle gate:** LC57-04
**Status:** STUB — Content TBD pending FEM L2 and gust spectrum definition

---

## 1. Objective
Verify that the optimised rib spacing register vector satisfies the fatigue life constraint
(REQ-WTW-57-RIBOPT-003): predicted fatigue life ≥ 80,000 flight cycles for all rib bays.
Also verify buckling load factor ≥ 1.0 at DLL for all skin panels (REQ-WTW-57-RIBOPT-006).

---

## 2. Applicable Requirements

| Requirement | Constraint |
|------------|-----------|
| REQ-WTW-57-RIBOPT-003 | Fatigue life ≥ 80,000 cycles |
| REQ-WTW-57-RIBOPT-006 | Skin panel buckling LF ≥ 1.0 at DLL |

---

## 3. Regulatory Basis
- CS-25 Appendix J — Damage-Tolerance and Fatigue Evaluation of Structure
- CS-25.305 — Strength and Deformation

---

## 4. Method (TBD)
1. **Load spectrum**: Derive rib bay stress spectrum from global FEM L2 under AMPEL360 WTW gust load spectrum (standard ESDU 74031 derivation or programme-specific — TBD at LC57-04)
2. **Stress concentration factor**: Apply CFRP rib-to-spar joint Kt from coupon test data (TBD — LC57-09)
3. **Cycle counting**: Rainflow cycle counting per ASTM E1049 on each rib bay critical location
4. **Damage accumulation**: Miner's rule D = Σ(nᵢ/Nᵢ) where Nᵢ from S-N curve (CFRP B-basis, hot/wet environmental knockdown γ = 2.0)
5. **Life assessment**: N_fatigue = minimum cycles to D = 1.0 at critical bay
6. **Buckling check**: Skin panel classical plate buckling analysis (CFRP orthotropic plate) or FEM submodel per approved method

---

## 5. Acceptance Criteria
| Check | Criterion | Status |
|-------|----------|--------|
| Fatigue life (all bays) | N_fatigue ≥ 80,000 cycles | TBD |
| Minimum margin (most critical bay) | TBD % | TBD |
| Skin panel buckling (all bays) | LF ≥ 1.0 at DLL | TBD |

---

## 6. Analysis Inputs (TBD)

| Input | Reference | Availability |
|-------|-----------|-------------|
| Optimised register vector | MODELS/rib_spacing_registers.example.yaml | Pending optimisation run |
| FEM L2 wing stress results | TBD | LC57-04 |
| CFRP S-N data (B-basis) | TBD material qualification | LC57-04 |
| Gust spectrum | TBD AMPEL360 WTW spectrum | LC57-02/03 |
| Joint Kt | TBD coupon test | LC57-09 |

---

> **Status:** STUB. This analysis will be completed at LC57-04 exit gate.
> Completion of this evidence object is required before LC57-04 gate review.
