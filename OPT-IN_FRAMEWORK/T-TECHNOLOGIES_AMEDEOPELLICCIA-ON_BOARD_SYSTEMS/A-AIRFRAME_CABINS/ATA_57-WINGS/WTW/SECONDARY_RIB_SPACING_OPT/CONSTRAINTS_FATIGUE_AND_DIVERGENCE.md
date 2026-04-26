# Wing Rib Spacing — Constraints: Fatigue Life and Aeroelastic Divergence

**Module:** Wing Rib Spacing Optimisation
**Doc ID:** T-A-ATA57-WTW-RIBOPT-CON-001
**Lifecycle gate:** LC57-03
**Status:** DRAFT

## 1. Scope
Defines the two binding constraints governing the WTW rib spacing optimisation:
1. **Fatigue life constraint** — driven by CS-25 Appendix J (damage-tolerance requirements)
2. **Aeroelastic divergence constraint** — driven by CS-25.629 (aeroelastic stability)

---

## 2. Fatigue Life Constraint (C-FATIGUE)

### 2.1 Regulatory basis
CS-25 Appendix J — Damage-Tolerance and Fatigue Evaluation of Structure
> "The aeroplane must be designed so that catastrophic failure due to fatigue, corrosion,
> manufacturing defects, or accidental damage will be avoided throughout the operational
> life of the aeroplane."

### 2.2 Constraint Definition
For each rib bay i:
```
N_fatigue(rᵢ) ≥ N_min = 80,000 flight cycles
```
Where:
- `N_fatigue(rᵢ)` = predicted fatigue life of rib bay i at the critical stress hot-spot, computed from the stress spectrum as a function of rib spacing register value rᵢ
- `N_min` = 80,000 flight cycles (AMPEL360 WTW design service objective, TBC at LC57-04)

### 2.3 Physical Mechanism
Rib spacing affects fatigue life through:
- **Rib pitch → skin panel aspect ratio → skin bending stress amplitude**: wider spacing increases skin panel deflection amplitude under gust loading
- **Rib-to-spar joint stress concentration**: optimal spacing balances load path length vs. joint bearing load

### 2.4 Analysis Method
Fatigue life evaluated via:
1. Rainflow cycle counting on standardised AMPEL360 gust spectrum (TBD — based on ESDU 74031)
2. Miner's rule summation: D = Σ(nᵢ/Nᵢ) ≤ 1.0
3. Fatigue knockdown factors for CFRP: environmental (hot/wet), scatter (B-basis, γ = 2.0)
4. Reference: `VERIFICATION_EVIDENCE/ANALYSIS_WTW_FATIGUE_LIFE_CHECK.md`

---

## 3. Aeroelastic Divergence Constraint (C-DIVERGENCE)

### 3.1 Regulatory basis
CS-25.629 — Aeroelastic Stability Requirements
> "The aeroplane must be free from aeroelastic instability for all configurations and
> design conditions within the envelope defined in CS-25.629."

CS-25.629(d) — Divergence:
> "The divergence speed must not be less than 1.15 VD at all altitudes."

### 3.2 Constraint Definition
```
V_divergence ≥ 1.15 × VD  (margin ≥ 15% above VD/MD)
```
Where:
- `V_divergence` = wing torsional divergence speed, as a function of rib spacing register vector **R**
- `VD` = design dive speed (TBD at LC57-02)

### 3.3 Physical Mechanism
Rib spacing affects divergence speed through:
- **Torsional rigidity GJ**: wider rib spacing reduces the constraint on skin panel torsional buckling → lower effective GJ → lower divergence speed
- **Coupled bending-torsion stiffness (EIb–GJ interaction)**: CFRP layup and rib pitch determine the coupled stiffness matrix K in the aeroelastic flutter/divergence equations

### 3.4 Analysis Method
Divergence speed evaluated via:
1. Strip theory / DLM (Doublet Lattice Method) aeroelastic model
2. Structural stiffness matrix from FEM (parameterised by register vector R)
3. Divergence speed solution from eigenvalue analysis: det(K − q·A) = 0
4. Reference: `VERIFICATION_EVIDENCE/ANALYSIS_WTW_DIVERGENCE_MARGIN_CHECK.md`

---

## 4. Constraint Interaction
The two constraints are in tension:
- **Wider spacing** → lower mass BUT lower fatigue life AND lower divergence speed
- **Tighter spacing** → higher mass BUT longer fatigue life AND higher divergence speed

The optimisation finds the Pareto-efficient rib spacing register vector that satisfies both constraints
while minimising structural mass. The optimisation is expected to be **divergence-constrained** in the
outer wing and **fatigue-constrained** in the inner wing (subject to analysis confirmation at LC57-04).

---

## 5. Constraint Parameter Summary

| Parameter | Value | Source | LC Gate |
|-----------|-------|--------|---------|
| N_min (fatigue cycles) | 80,000 | AMPEL360 Design Service Objective | LC57-02 |
| V_divergence margin | ≥ 15% above VD | CS-25.629(d) | Programme |
| Miner's rule limit | 1.0 | CS-25 Appendix J | Programme |
| CFRP scatter factor | B-basis, γ = 2.0 | Material data qualification | LC57-04 |
| VD | TBD | Performance spec freeze | LC57-02 |
