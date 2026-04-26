# ANALYSIS: WTW Wing Rib Spacing — Aeroelastic Divergence Margin Check

**Evidence ID:** EVI-WTW-57-RIBOPT-002
**Type:** Analysis
**Doc ID:** T-A-ATA57-WTW-RIBOPT-ANA-DIV-001
**Lifecycle gate:** LC57-05
**Status:** STUB — Content TBD pending aeroelastic FEM/DLM model definition

---

## 1. Objective
Verify that the optimised rib spacing register vector satisfies the aeroelastic divergence
constraint (REQ-WTW-57-RIBOPT-004): wing torsional divergence speed ≥ 1.15 × VD at all altitudes.

---

## 2. Applicable Requirements

| Requirement | Constraint |
|------------|-----------|
| REQ-WTW-57-RIBOPT-004 | V_divergence ≥ 1.15 × VD (CS-25.629(d)) |

---

## 3. Regulatory Basis
- CS-25.629 — Aeroelastic Stability Requirements
- CS-25.629(d) — Divergence: "The divergence speed must not be less than 1.15 VD at all altitudes."
- AMC 25.629 — Aeroelastic Stability Substantiation

---

## 4. Method (TBD)
1. **Structural model**: Parameterised FEM with torsional stiffness GJ as function of rib spacing register vector **R**
2. **Aerodynamic model**: Doublet Lattice Method (DLM) subsonic unsteady aerodynamics, matched to CFD corrections at transonic regime (TBD)
3. **Coupled aeroelastic model**: Nastran SOL 144 (static aeroelastic) or equivalent; divergence computed as minimum eigenvalue of (K − q·A)
4. **Speed sweep**: Evaluate divergence eigenvalue from M = 0.0 to M = 1.05 at sea level, cruise altitude, and ceiling
5. **Margin evaluation**: Divergence margin = (V_divergence − VD) / VD × 100%
6. **Parameter sensitivity**: Verify divergence margin for ±10% variation in optimised register values (robustness check)

---

## 5. Acceptance Criteria
| Check | Criterion | Status |
|-------|----------|--------|
| Divergence speed margin | ≥ 15% above VD at all altitudes | TBD |
| Margin at most critical altitude | TBD % | TBD |
| Sensitivity robustness | Margin ≥ 10% under ±10% register perturbation | TBD |

---

## 6. Analysis Inputs (TBD)

| Input | Reference | Availability |
|-------|-----------|-------------|
| Optimised register vector | MODELS/rib_spacing_registers.example.yaml | Pending optimisation run |
| FEM torsional stiffness parameterisation | TBD (Nastran model) | LC57-04/05 |
| DLM aerodynamic model | TBD | LC57-05 |
| VD (design dive speed) | Performance spec (TBD) | LC57-02 |
| CFD transonic corrections | TBD | LC57-05 |

---

## 7. Key Physical Relationships
The divergence speed for a uniform swept wing approximation:
```
q_divergence = GJ / (e × a × c_bar)
```
Where:
- `GJ` = torsional stiffness of wing cross-section (function of rib spacing)
- `e` = distance from aerodynamic centre to elastic axis
- `a` = lift-curve slope
- `c_bar` = mean aerodynamic chord

Wider rib spacing reduces the constraint on skin panel torsional buckling mode,
effectively lowering GJ and thus lowering q_divergence. The optimisation must
find spacing values that maintain GJ above the minimum required for 15% margin.

---

> **Status:** STUB. This analysis will be completed at LC57-05 exit gate.
> Completion of this evidence object is required before LC57-05 gate review (Aeroelastic Clearance Review).
