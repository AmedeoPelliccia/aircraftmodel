# LC05 — GEN-MODEL Role Formal Specification

    knot_id: KNOT-ATA96-70-00-001
    knu_id: KNU-ATA96-70-001
    title: GEN-MODEL Role Formal Specification
    lifecycle_stage: LC05
    version: 0.1
    date: 2026-02-22
    status: PLANNED
    program: ID-A360-Q100

---

## 1 — Model Primitives

Let:

- $KG$ = Aircraft Knowledge Graph — the complete structured representation
  of the programme's engineering model, including ATA chapters, interface
  contracts, certification bindings, and traceability links.
- $\Sigma$ = Structural Grammar — the union of ATA iSpec 2200 taxonomy,
  OPT-IN 5-axis topology, and SSOT lifecycle schema (LC01–LC14).
- $C$ = Certification Constraint Set — CS-25 Amdt 28, DAL classifications
  (DO-178C / DO-254), CMR items, CDCCL entries, and airworthiness
  limitations (ATA 04).
- $B$ = SSOT Baseline — the versioned, hash-authenticated state of all
  authoritative engineering artifacts at a given commit.
- $\Delta$ = Proposed Structural Delta — a set of node/edge additions,
  modifications, or (gated) deletions submitted by a delineant operation.

---

## 2 — `.askm/observer` — Formal Properties

### 2.1 Functional Form

$$
O: (KG, B) \rightarrow S_t
$$

Where:

- $S_t \subset KG$
- $S_t$ is a projection of graph state at time $t$
- $O$ extracts but never mutates

### 2.2 Invariants

The Observer must satisfy all of the following:

**INV-O1 — Idempotence**

$$
O(O(KG, B), B) = O(KG, B)
$$

Repeated observation produces the same state-capture. No accumulation
of side-effects.

**INV-O2 — No Topology Mutation**

$$
\text{Nodes}(KG)_{after} = \text{Nodes}(KG)_{before}
$$

$$
\text{Edges}(KG)_{after} = \text{Edges}(KG)_{before}
$$

The observer cannot add, remove, or reclassify nodes or edges.

**INV-O3 — No Schema Drift**

$$
\Sigma_{after} = \Sigma_{before}
$$

The structural grammar is invariant under observation. No new ATA
chapters, OPT-IN axes, or lifecycle stages can be introduced by
observer operations.

**INV-O4 — Ledger Write Constraint**

Observer is permitted to emit only the following artifact classes:

| Artifact Class               | Description                          |
|------------------------------|--------------------------------------|
| `LC05_ANALYSIS_STATE_CAPTURE`| Snapshot of current model state      |
| `LC05_MARGIN_REPORT`         | Computed margins from existing data  |
| `LC05_TRACE_SNAPSHOT`        | Traceability graph extraction        |

The following artifact class is **forbidden** for observer mode:

| Forbidden Class | Reason                                 |
|-----------------|----------------------------------------|
| `MODEL_DELTA`   | Implies topology mutation (§3 domain)  |

---

## 3 — `.askm/delineant` — Formal Properties

### 3.1 Functional Form

$$
D: (S, C, \Sigma) \rightarrow (KG', \Delta)
$$

Where:

- $KG' = KG \cup \Delta$
- $\Delta$ respects grammar $\Sigma$
- $S$ must be a valid observer output (see §9)

### 3.2 Admissibility Condition

A delineation is admissible if and only if:

$$
\text{Invariant}(KG') = \text{Invariant}(KG)
$$

Where the invariant set includes:

| ID    | Invariant                          | Description                                          |
|-------|------------------------------------|------------------------------------------------------|
| ADM-1 | ATA Taxonomy Compliance            | All nodes map to valid ATA chapters per iSpec 2200   |
| ADM-2 | Interface Contract Completeness    | Every interface node has defined inputs and outputs   |
| ADM-3 | Requirement Trace Continuity       | Every LC05 artifact traces to an LC02 requirement    |
| ADM-4 | Certification Mapping Preservation | No certified mapping is broken or orphaned           |
| ADM-5 | No Orphan Nodes                    | Every node is reachable from the graph root          |

### 3.3 Delta Classification

| Delta Class  | Description                                  | Gate Required |
|--------------|----------------------------------------------|---------------|
| `STRUCTURAL` | Adds/modifies nodes or edges in $KG$         | Yes           |
| `PARAMETRIC` | Modifies values within existing node envelope | No            |
| `NONE`       | No change to $KG$ (observer-only output)     | No            |

---

## 4 — Model Topology Invariance Condition

### 4.1 Topological Signature

Define:

$$
\mathcal{T}(KG) = (\mathcal{N}, \mathcal{E}, \mathcal{C}_b)
$$

Where:

- $\mathcal{N}$ = Set of node types (ATA chapter, interface, requirement,
  certification item, KNU evidence)
- $\mathcal{E}$ = Set of edge classes (traces-to, implements, certifies,
  depends-on, inherits-from)
- $\mathcal{C}_b$ = Certification bindings (DAL assignments, CMR linkages,
  CDCCL cross-references)

### 4.2 Invariance Criterion

$$
\mathcal{T}(KG') \sim \mathcal{T}(KG)
$$

Topological similarity $\sim$ holds if and only if:

1. **Extension** — New nodes extend grammar $\Sigma$ without redefining
   existing node types.
2. **Preservation** — All existing invariants (ADM-1 through ADM-5) hold
   in $KG'$.
3. **No Uncertified Deletion** — No deletion of nodes with active
   certification bindings unless accompanied by a lifecycle transition
   record (IBCR per ATA 96-70).

Violation of any of these conditions constitutes **structural
hallucination** and the delta must be rejected.

### 4.3 Formal Proof Reference

See companion document: `LC05-TOPOLOGY-INVARIANCE-PROOF.md`
(KNU-ATA96-70-002).

---

## 5 — Governance Separation Constraint

### 5.1 Mode Enumeration

```yaml
gen_model_modes:
  - OBSERVER    # read-only state extraction
  - DELINEANT   # structural write (gated)
```

### 5.2 Forbidden Cross-Mode Operations

| Rule ID | Constraint                                         |
|---------|----------------------------------------------------|
| GOV-1   | OBSERVER cannot emit `MODEL_DELTA`                 |
| GOV-2   | DELINEANT cannot emit `STATE_CAPTURE` without      |
|         | citing a prior observer baseline as source         |
| GOV-3   | No mode can modify $\Sigma$ (grammar is frozen     |
|         | within a baseline version)                         |

### 5.3 Enforcement Points

| Layer       | Mechanism                              | Reference              |
|-------------|----------------------------------------|------------------------|
| Pre-commit  | `.github/hooks/pre-commit` Rule 4–5    | §7 of this document    |
| CI          | `gen-model-validation.yml` workflow    | `.github/workflows/`   |
| Validator   | `optin_structure_validator.py`         | `tools/ci/`            |
| Config      | `.askm/observer/config.yaml`          | §2 config binding      |
| Config      | `.askm/delineant/config.yaml`         | §3 config binding      |
| Agent       | `.asit/agents/gen-model-agent.yaml`   | Agent registry         |
| Operator    | `.asit/operator/enforcement-rules.yaml`| Enforcement registry  |

---

## 6 — Certification Coupling Rule

If a delineant proposal affects any of the following:

| Node Category                        | Identifier Pattern          |
|--------------------------------------|-----------------------------|
| Airworthiness Limitations            | ATA 04 nodes                |
| Certification Maintenance Req.       | CMR items                   |
| Critical Design Config. Control List | CDCCL entries               |
| DAL A/B Safety Paths                 | DO-178C/DO-254 DAL A or B   |
| Load-Bearing Topology                | Structural ATA chapters     |

Then the following gates apply:

```yaml
qualification_required: true
certification_gate: LC08
risk_class: HIGH
review_authority: Chief Engineer
```

Deltas that do not affect these categories may proceed with standard
review under `risk_class: STANDARD`.

---

## 7 — Structural Entropy Principle

### 7.1 Definition

Let $H(KG)$ represent the model entropy, defined as the aggregate of:

- Boundary ambiguity (interfaces with undefined directionality)
- Orphan nodes (unreachable from graph root)
- Trace breaks (LC05 artifacts without LC02 requirement linkage)
- Certification gaps (nodes in safety-critical paths without DAL binding)

### 7.2 Entropy Behavior

Without observer/delineant separation:

$$
H(KG) \uparrow \quad \text{(monotonically increasing with unstructured edits)}
$$

With separation enforced:

$$
H(KG) \downarrow \quad \text{under governance constraints (§5)}
$$

This is not a philosophical claim. It is an operational graph stability
property: structured governance reduces the rate of boundary ambiguity
and orphan accumulation.

---

## 8 — DWGE Procedure Registry Binding

### 8.1 Delineant Procedure Template

```yaml
procedure_id: PROC-ATA28-REFINE-TOPO-v1
lifecycle_stage: LC05
allowed_mode: DELINEANT
delta_class: STRUCTURAL
invariance_test_required: true
certification_impact_scan: true
observer_baseline_required: true
```

### 8.2 Observer Procedure Template

```yaml
procedure_id: PROC-ATA28-MARGIN-SNAPSHOT-v2
lifecycle_stage: LC05
allowed_mode: OBSERVER
delta_class: NONE
invariance_test_required: false
certification_impact_scan: false
observer_baseline_required: false
```

### 8.3 Procedure Validation Rule

Every procedure registered under `lifecycle_stage: LC05` must declare
`allowed_mode` as exactly one of `OBSERVER` or `DELINEANT`. Mixed-mode
procedures are inadmissible.

---

## 9 — No Delineation Without Observer Baseline

### 9.1 Formal Constraint

$$
D \text{ is valid only if } S = O(KG, B)
$$

This means:

- You cannot transform what you have not explicitly observed.
- Every structural delta must cite a prior `LC05_ANALYSIS_STATE_CAPTURE`
  or `LC05_TRACE_SNAPSHOT` artifact as its input baseline.
- The cited artifact must be committed and hash-verifiable against the
  current SSOT baseline $B$.

### 9.2 Rationale

This closes the epistemic loop: delineation operates on observed state,
not on assumptions. It prevents:

- Deltas based on stale or imagined model states
- Structural changes without auditable provenance
- Divergence between the perceived and actual knowledge graph

---

## 10 — Structural Analogy

The observer/delineant separation is equivalent to:

| Domain              | Observer                   | Delineant                        |
|---------------------|----------------------------|----------------------------------|
| Physics             | Measurement operator       | Manifold reparameterization      |
| Category Theory     | Forgetful functor          | Schema-preserving transformation |
| Software Arch.      | Query (read-only)          | Type-safe refactoring            |
| Database            | `SELECT` (no side-effects) | `ALTER TABLE` (DDL, gated)       |

These carry different epistemic weight and must not be conflated.

---

## 11 — Traceability

| Artifact                                | Reference            |
|-----------------------------------------|----------------------|
| This specification                      | KNU-ATA96-70-001     |
| Topology Invariance Proof Sketch        | KNU-ATA96-70-002     |
| Parent KNOT                             | KNOT-ATA96-70-00-001 |
| Governance policies (ATA 96-70)         | ATA_96/96-70         |
| Inheritance Boundary Declaration        | AMPEL360-FAM-IBD-001-RevA |
| Observer config                         | `.askm/observer/config.yaml` |
| Delineant config                        | `.askm/delineant/config.yaml` |
| Agent registry                          | `.asit/agents/gen-model-agent.yaml` |
| Enforcement rules                       | `.asit/operator/enforcement-rules.yaml` |

---

*Document ID: LC05-GEN-MODEL-ROLE-SPEC-v0.1*
*Programme: ID-A360-Q100 · AMPEL360*
*Classification: Engineering Governance — LC05 Analysis Models*
*Applicable Standards: CS-25 Amdt 28, DO-178C, DO-254, ATA iSpec 2200, S1000D Issue 5.0*
