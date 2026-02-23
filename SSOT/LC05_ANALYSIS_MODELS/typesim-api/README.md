# TypeSim — TOP-LAP Consortium Digital Twin Function

<p align="center">
  <img src="https://img.shields.io/badge/Doc-TYPESIM--API--001%20Rev%20A-1B3A5C" alt="Doc ID">
  <img src="https://img.shields.io/badge/OpenAPI-3.0.0-85EA2D" alt="OpenAPI">
  <img src="https://img.shields.io/badge/Framework-TOP--LAP-0066cc" alt="TOP-LAP">
  <img src="https://img.shields.io/badge/Phase-LC05-blue" alt="LC05">
  <img src="https://img.shields.io/badge/Family-AMPEL360-purple" alt="AMPEL360">
  <img src="https://img.shields.io/badge/Governance-SHA--256%20Hash%20Chain-teal" alt="Governance">
</p>

---

| Field | Value |
|---|---|
| **Document ID** | AMPEL360-FAM-LC05-TYPESIM-API-001 Rev A |
| **Classification** | Engineering Process — API Contract |
| **Date** | 2026-02-22 |
| **Concept** | Amedeo Pelliccia / IDEALE |
| **Reference** | AMPEL360-FAM-LC05-TOPLAP-MDLSP-REF-001 §8 |
| **Status** | CONFIRMED |

---

## 1. Overview

**TypeSim** is the federated multi-domain simulation function for the AMPEL360
consortium Digital Twin. It implements the formal mapping:

```
TypeSim : (M, P, C, E, K) → (S, R, I)
```

| Symbol | Domain | Description |
|---|---|---|
| **M** | Model | Geometry, material state, recipe, SPSC class |
| **P** | Process | Manufacturing process set (AM-Π-{PROCESS}-{MAT}-v{N}) |
| **C** | Constraints | AM, structural, thermal, certification, system bounds |
| **E** | Environment | Load cases, mission profile, thermal boundary, production cell |
| **K** | Knowledge | SSOT version hash — the programme's current knowledge baseline |
| **S** | State | Simulated TOPLAP state, confidence, producibility index |
| **R** | Risk | Constraint margins, violations, horizon flags per domain |
| **I** | Impact | Mass, time, cost, CO₂, certification, FPAI/PFI indices |

---

## 2. Operational Modes

### 2.1 EXPLORATORY (Pre-PNRD)

Before the **Point of No Return for Design** (PNRD) is declared, TypeSim
operates in **EXPLORATORY** mode:

- Multi-objective optimisation is permitted
- Design topology may change between runs
- State vector dimensions may be added or removed
- Results inform trade studies (LC04) and TOP-LAP TOPO/OPER phases

### 2.2 PROPAGATION (Post-PNRD)

After PNRD lock, TypeSim switches to **PROPAGATION** mode:

- Design solution **x*** is frozen (`pnrd_solution_hash` required)
- Only **parametric** changes are permitted (no topological changes)
- Results feed TOP-LAP PROJ/LATCH phases
- Every run must produce a reproducible `governance_record`

---

## 3. API Endpoints

### `POST /typesim/run`

Execute a TypeSim simulation run.

**Input:** `TypeSimInput` — model state, constraints, environment, mode, knowledge baseline

**Output:** `TypeSimOutput` — simulated state evolution, risk vector, impact metrics, governance record

### `GET /typesim/status`

Query the current TOP-LAP state and FPAI for a given model.

**Parameters:** `model_hash` (SHA-256 of the model state)

**Output:** `ToplapStatus` — current state, confidence, horizon, PNRD status, gate progress

### `POST /typesim/pnrd`

Declare the Point of No Return for Design — freezes the solution topology.

**Input:** `PNRDDeclaration` — selected solution hash, objective hash, constraints hash, authority

**Output:** PNRD lock confirmation with timestamp

---

## 4. Governance Record

Every TypeSim run produces a `GovernanceRecord` that is appended to the
SHA-256 hash chain (same chain as the TT ledger in `finance/ledger.json`):

```yaml
governance_record:
  model_hash:       "sha256(...)"
  constraints_hash: "sha256(...)"
  solver_versions:
    AM:    "v2.1.0"
    STR:   "v3.4.1"
    THERM: "v1.8.0"
    SYS:   "v2.0.0"
    ESG:   "v1.2.0"
  mode:          "EXPLORATORY"
  PNRD_status:   false
  timestamp:     "2026-06-15T14:30:00Z"
  prev_hash:     "abc123..."
  hash:          "def456..."
```

This ensures full reproducibility and auditability of every simulation run
in the consortium Digital Twin.

---

## 5. State Vector Mapping

TypeSim's `SimulatedState.state_vector` maps to the TOP-LAP state vector
dimensions:

| TypeSim Field | TOP-LAP Dimension | Description |
|---|---|---|
| `G_geometry` | Structural / Aero | Part geometry state (hash or parametric) |
| `P_process` | Manufacturing | Process recipe and parameters |
| `M_material` | C² CELL / Structural | Material state (alloy, phase, properties) |
| `Q_quality` | Safety | Quality prediction (porosity, defects) |
| `V_viability` | All | Overall viability assessment |
| `T_traceability` | Governance | Full provenance chain |

---

## 6. Impact Metrics

TypeSim produces quantitative impact metrics that feed directly into the
TOP-LAP PROJ phase and TT distribution:

| Metric | Unit | Description | TT Mapping |
|---|---|---|---|
| `mass_kg` | kg | Component mass | — |
| `mass_delta_pct` | % | Mass delta vs. baseline | `delta_residual_primary` (structural KNOTs) |
| `manufacturing_time_hr` | hr | Production time estimate | — |
| `distortion_risk_idx` | — | AM distortion risk [0,1] | Risk factor for AM KNOTs |
| `cryo_fatigue_margin` | — | Cryogenic fatigue safety margin | `delta_residual_primary` (ATA 28-70) |
| `cert_flag` | bool | Certification compliance flag | Gate G-L prerequisite |
| `co2_lifecycle_kg` | kg CO₂ | Lifecycle carbon footprint | ESG reporting |
| `EEI` | [0,1] | Energy Efficiency Index | — |
| `HORIZON_FPAI_360` | [0,360] | Full Programme Assessment Index | Programme health metric |
| `PFI_360` | [0,360] | Programme Feasibility Index | Viability gate |
| `cost_delta_pct` | % | Cost delta vs. baseline | — |

---

## 7. SPSC Classification

TypeSim classifies structural parts using the **SPSC** (Structural Part
Safety Classification) system:

| Class | Description | Certification Requirement |
|---|---|---|
| **SPSC-1** | Primary structure, safety-critical | Full qualification + DO-178C/254 |
| **SPSC-2** | Secondary structure, damage-tolerant | Qualification with maintenance inspection |
| **CENTERBODY** | BWB centerbody (FORKED — BWB only) | Novel certification path |
| **WING** | Wing structure (SHARED foundation) | Standard CS-25 subpart C |
| **OTHER** | Non-structural components | Standard qualification |

---

## 8. Integration with TOP-LAP Cycle

```
TOP-LAP Phase    TypeSim Mode       TypeSim Endpoint
─────────────    ────────────       ────────────────
TOPO             —                  —
OPER             EXPLORATORY        POST /typesim/run
                 ↓ PNRD declared    POST /typesim/pnrd
OPER/PROJ        PROPAGATION        POST /typesim/run
PROJ             —                  GET  /typesim/status
LATCH            —                  (governance record → ledger)
```

---

## 9. Files

| File | Description |
|---|---|
| [`typesim-openapi.yaml`](typesim-openapi.yaml) | OpenAPI 3.0.0 specification |
| [`README.md`](README.md) | This document |

---

<p align="center">
  <strong>TypeSim — AMPEL360 Consortium Digital Twin</strong><br/>
  <em>Federated simulation. Governed evidence. Zero-CO₂ by design.</em>
</p>
<p align="center">
  <em>By Amedeo Pelliccia · AI-Assisted Engineering · aircraftmodel.eu</em>
</p>
