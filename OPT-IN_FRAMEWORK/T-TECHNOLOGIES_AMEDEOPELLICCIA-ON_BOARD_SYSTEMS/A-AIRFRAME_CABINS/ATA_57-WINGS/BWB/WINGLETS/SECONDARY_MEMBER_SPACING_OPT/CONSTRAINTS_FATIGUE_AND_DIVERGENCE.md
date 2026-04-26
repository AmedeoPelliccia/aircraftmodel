# Fatigue and Aeroelastic Divergence Constraints — BWB Winglets

**Doc ID:** T-A-ATA57-BWB-WGLT-CNST-001  
**Status:** DRAFT  
**Regulatory basis:** CS-25.571 (fatigue/damage tolerance), CS-25.629 (flutter/divergence)

---

## 1. Fatigue Life Constraint (C-FATIGUE)

### 1.1 Statement
Every winglet member bay SHALL sustain a minimum of **80,000 flight cycles** at the AMPEL360 BWB
winglet design load spectrum without fatigue crack initiation or delamination exceeding
the damage tolerance threshold.

### 1.2 Methodology
- **Fatigue law:** Miner's cumulative damage rule (Σ n_i / N_i ≤ 1.0)
- **Material property:** CFRP B-basis fatigue allowables with scatter factor γ = 2.0
- **Load spectrum:** AMPEL360 BWB winglet spectrum — note: tip load spectrum has higher
  bending amplitude relative to chord than main wing due to winglet dihedral and local gust response
- **Bay-level evaluation:** Each member bay evaluated as a unit

### 1.3 Constraint expression (for GA optimiser)
```
C_FATIGUE(r) = D_Miner(r) ≤ 1.0 / γ = 0.5
```

### 1.4 Physical mechanism
Wider bay spacing (higher register values) reduces member count and increases bay span loads →
shorter fatigue life. The optimiser is constrained to keep bay spacing below a fatigue-derived
upper bound `r_max_fatigue(location)`.

---

## 2. Aeroelastic Divergence Constraint (C-DIVERGENCE)

### 2.1 Statement
The winglet member spacing register map SHALL produce a divergence speed V_div ≥ **1.15 × VD**
per CS-25.629(d), evaluated on the winglet bending/torsion stiffness matrix.

### 2.2 Methodology
- **Analysis method:** DLM eigenvalue analysis of winglet aeroelastic stiffness
- **Inboard boundary condition:** Blend zone outboard stiffness from `../BLEND_ZONE/`
- **Stiffness parameterisation:** EI(r) ∝ 1 / (member spacing)² for plate-like winglet structure
- **Divergence eigenvalue:** λ_div evaluated on winglet torsion stiffness matrix
- **Margin:** M_div = V_div / VD − 1.0 ≥ 0.15

### 2.3 Constraint expression (for GA optimiser)
```
C_DIVERGENCE(r) = V_div(r) / VD ≥ 1.15
```

### 2.4 Physical mechanism
Wider member spacing (higher registers) reduces local bending/torsion stiffness of the winglet
→ lower divergence speed. The optimiser must maintain minimum aggregate stiffness in the
torsion-critical outboard bays.

---

## 3. Constraint Interaction
- **C-FATIGUE** → upper bound on register (max spacing allowed before fatigue damage accumulates)
- **C-DIVERGENCE** → upper bound on register (max spacing before divergence margin is violated)
Both constraints typically set upper bounds on register values; the optimiser pushes toward
higher registers to minimise mass but is bounded from above by both constraints.
