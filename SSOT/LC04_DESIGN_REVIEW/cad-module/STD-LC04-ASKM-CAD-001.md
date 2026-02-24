# STD-LC04-ASKM-CAD-001 — CAD Module Observer / Delineant Standard

    doc_id: AMPEL360-FAM-LC04-ASKM-CAD-001 Rev A
    knot_id: KNOT-ATA96-70-00-001
    knu_id: KNU-ATA96-70-003
    title: CAD Module — Observer/Delineant Roles, Output Contracts & Gates
    lifecycle_stage: LC04
    version: 1.0
    date: 2026-02-24
    status: PLANNED
    program: ID-A360-Q100
    parent_spec: LC05-GEN-MODEL-ROLE-SPEC-v0.1 (KNU-ATA96-70-001)

---

## 1 — Purpose & Scope

This standard extends the GEN-MODEL observer/delineant separation
(LC05-GEN-MODEL-ROLE-SPEC §2–§3) to the **CAD domain**, enabling
ML-assisted geometry extraction (observer) and parametric synthesis
(delineant) for 3D models and 2D drawings.

Training leverages **public MTL (Media Token Libraries)** — curated
datasets of geometric primitives, feature intents, fabrication tokens,
and documentation conventions sourced from open-licence CAD repositories.

The module operates under the same governance framework as the parent
GEN-MODEL specification: observer is read-only; delineant produces
candidate artifacts that must pass deterministic gates before promotion
to SSOT.

---

## 2 — Definitions

| Term | Definition |
|---|---|
| **MTL** | Media Token Library — curated dataset of geometric, semantic, fabrication, and documentation tokens extracted from public CAD sources |
| **FeatureGraph** | Canonical graph representation of a CAD model's features, constraints, and parametric relationships |
| **IntentSpec** | Declarative specification of geometric intent (what to build, not how to draw it) |
| **CAD Semantics** | Structured metadata: units, tolerances, datums, materials, processes, versions |
| **Candidate Artifact** | Delineant output that has not yet passed deterministic gates; never written to SSOT directly |
| **WDG** | Widget — deterministic validation gate for CAD artifacts |

---

## 3 — `.askm/operator/observer` — CAD Extension

### 3.1 Objective

Extract geometric state and design semantics from CAD files **without
mutating** the source model. The CAD observer is a specialisation of the
GEN-MODEL observer ($O: (KG, B) \rightarrow S_t$) applied to geometry.

### 3.2 Ingestion Formats

| Category | Formats |
|---|---|
| Solid exchange | STEP (AP203/AP214), IGES |
| 2D drawing | DXF, DWG (read-only via OCCT/LibreCAD) |
| Mesh | STL, OBJ |
| Scene | glTF 2.0 |
| Annotation | PMI (if embedded), raster images of drawings |

### 3.3 Output Contract

The observer produces **exactly three** canonical artifact types:

| Artifact | Format | Schema | Placement |
|---|---|---|---|
| `feature_graph.json` | JSON | `feature_graph.schema.json` | `SSOT/LC04_DESIGN_REVIEW/cad-module/` |
| `geometry_params.yaml` | YAML | Inline (§3.4) | Same |
| `cad_semantics.yaml` | YAML | Inline (§3.5) | Same |

All three are **read-only projections** and must satisfy INV-O1 through
INV-O4 from the parent spec.

### 3.4 `geometry_params.yaml` Structure

```yaml
# Parametric values extracted from the source model
source_file: "example.step"
source_hash: "sha256:..."
units: "mm"
parameters:
  - name: "wall_thickness"
    value: 2.5
    unit: "mm"
    tolerance: "±0.1"
    datum_ref: "A"
  - name: "bore_diameter"
    value: 12.0
    unit: "mm"
    tolerance: "+0.025 / −0.000"
    datum_ref: "B"
```

### 3.5 `cad_semantics.yaml` Structure

```yaml
# Design-level metadata extracted by the observer
source_file: "example.step"
source_hash: "sha256:..."
units: "mm"
coordinate_system: "right-hand, Z-up"
tolerancing_standard: "ISO 1101"
materials:
  - id: "MAT-001"
    designation: "Al 7075-T6"
    source: "public-mtl"
datums:
  - id: "A"
    type: "plane"
    description: "Primary mounting face"
  - id: "B"
    type: "axis"
    description: "Bore centreline"
processes:
  - id: "PROC-001"
    type: "CNC_MILLING"
    surface_finish: "Ra 1.6"
version: "1.0"
```

### 3.6 Observer Invariants (CAD-specific)

In addition to INV-O1 through INV-O4, the CAD observer must satisfy:

| ID | Name | Rule |
|---|---|---|
| INV-CAD-O1 | Conservative Parse | If geometry is ambiguous or incomplete → report `status: "missing/unknown"`, never invent geometry |
| INV-CAD-O2 | Unit Preservation | Output units must match source units; no implicit conversion |
| INV-CAD-O3 | Hash Integrity | `source_hash` in every output artifact must match SHA-256 of the ingested file |
| INV-CAD-O4 | No Feature Invention | Observer may only report features present in the source; no inferred features |

---

## 4 — `.askm/operator/delineant` — CAD Extension

### 4.1 Objective

Generate **candidate** 3D models and 2D drawings from an IntentSpec
plus FeatureGraph baseline. Delineant outputs are proposals — they are
never written directly to SSOT.

### 4.2 Output Contract

| Artifact | Format | Description |
|---|---|---|
| `cad_build_script.py` | Python (OCCT/FreeCAD macro) | Deterministic parametric build script |
| `drawing_2d.dxf` | DXF | 2D drawing with title block, layers, dimensions |
| `drawing_meta.yaml` | YAML | Drawing metadata (scale, sheet size, revision) |
| `validation_report.json` | JSON | Results from all WDG gates |
| `heading.yaml` | YAML | Provenance record (PATH → MTL) |

All outputs carry `candidate` status until promoted by the gate pipeline
(§5).

### 4.3 Delineant Constraints (CAD-specific)

| ID | Name | Rule |
|---|---|---|
| ADM-CAD-1 | Script Determinism | Same `feature_graph.json` + `geometry_params.yaml` → identical geometry (bit-reproducible within FP tolerance) |
| ADM-CAD-2 | No SSOT Direct Write | All outputs are `candidate artifacts`; promotion requires gate passage |
| ADM-CAD-3 | Observer Baseline Required | Build script must reference a committed `feature_graph.json` as input |
| ADM-CAD-4 | Drawing Compliance | 2D drawings must use approved title block template, layer naming, and unit convention |
| ADM-CAD-5 | Export Control | No geometry derived from restricted sources may enter the public MTL pipeline |

---

## 5 — Deterministic Gate Pipeline (DWGE)

### 5.1 Gate Sequence

Candidate artifacts pass through the following **ordered** gate
sequence. All gates must pass before promotion to SSOT + ledger entry.

| Gate ID | Name | Check |
|---|---|---|
| WDG-GEOM-SCHEMA-VALIDATE | Geometry Schema | `feature_graph.json` validates against `feature_graph.schema.json` |
| WDG-CONSTRAINT-ENVELOPE | Constraint Envelope | All parametric values within declared tolerance envelopes |
| WDG-DIMENSIONAL-CHECK | Dimensional Check | Key dimensions match IntentSpec ± tolerance |
| WDG-DRAWING-COMPLIANCE | Drawing Compliance | Layers, title block, units, tolerance callouts per template |
| WDG-DIFF-BASELINE | Baseline Diff | Delta against previous baseline is explicitly enumerated |
| WDG-EXPORT-CONTROL-IP | Export/IP Check | No restricted or unlicensed geometry in candidate |

### 5.2 Gate Verdict

```yaml
gate_verdict:
  all_pass:
    action: "Promote → SSOT + ledger_tx"
    delta_class: STRUCTURAL
  any_fail:
    action: "Reject → candidate remains draft; escalation if WDG-EXPORT-CONTROL-IP fails"
    delta_class: NONE
```

### 5.3 Promotion Flow

```
Observer ──► FeatureGraph ──► Delineant ──► Candidate Artifacts
                                                    │
                                        ┌───────────┤
                                        │ WDG gates  │
                                        └───────────┤
                                              PASS ──► SSOT + ledger_tx.json
                                              FAIL ──► Draft (escalate if IP)
```

---

## 6 — MTL Training Pipeline

### 6.1 Phase A — Observer Pre-training (Public-Only)

| Item | Value |
|---|---|
| **Objective** | Robust CAD reading + feature extraction |
| **Dataset** | Public CAD repositories, educational models, standard part libraries |
| **Licence** | Only open-licence data (MIT, CC-BY, CC0, public domain) |
| **Task** | Parsing + feature intent reconstruction (self-supervised / contrastive) |
| **Output** | FeatureGraph + CADSemantics |
| **Product** | `.askm/operator/observer` trained for CAD ingestion |

### 6.2 Phase B — Delineant Training (Controlled Synthesis)

| Item | Value |
|---|---|
| **Objective** | Generate geometry/drawing from IntentSpec with CAD grammar |
| **Training targets** | CAD build scripts (OCCT/FreeCAD), explicit constraints, 2D drawings with title block templates |
| **Product** | `.askm/operator/delineant` that proposes parametric builds |

### 6.3 Phase C — Deterministic Envelope (DWGE + Gates)

| Item | Value |
|---|---|
| **Objective** | Qualify generated artifacts for SSOT promotion |
| **Mechanism** | WDG gate pipeline (§5) |
| **Product** | Certification-ready governance layer |

---

## 7 — Canonical Artifact Set (Minimum)

For auditability and reproducibility, every CAD module operation must
produce the following minimum artifact set:

| Artifact | Producer | Purpose |
|---|---|---|
| `feature_graph.json` | Observer | Canonical feature/constraint representation |
| `geometry_params.yaml` | Observer | Parametric values |
| `cad_semantics.yaml` | Observer | Design metadata |
| `cad_build_script.py` | Delineant | Deterministic build |
| `drawing_2d.dxf` | Delineant | 2D drawing |
| `drawing_meta.yaml` | Delineant | Drawing metadata |
| `validation_report.json` | Gate pipeline | Gate results |
| `heading.yaml` | System | Provenance (PATH → MTL) |
| `ledger_tx.json` | System | Teknia ledger entry |

---

## 8 — Monotonic Safety Metrics

For the CAD module to satisfy "only improves" semantics:

| Metric | Rule |
|---|---|
| **No Degradation** | Tolerances, masses, structural margins, and interface geometry must not degrade between baselines |
| **Traceability** | Every dimension and feature must map to a requirement or constraint |
| **No Ambiguity** | Missing data → `missing/unknown` status and escalation, never assumption |
| **Reproducibility** | Same IntentSpec + same build script → identical geometry (hash-verifiable) |

---

## 9 — Lifecycle Integration

| Role | Function |
|---|---|
| Observer | Produces state and semantic model → LC04 design models |
| Delineant | Produces candidate artifacts → LC04 synthesis candidates |
| Promotion | SSOT update occurs at LC08/LC09 per programme governance |

---

## 10 — Risks

| Risk | Mitigation |
|---|---|
| CAD as opaque binary | Prioritise scripts + canonical JSON/YAML over native binary files |
| Drawing standard drift | Strict title block and layer templates; validated by WDG-DRAWING-COMPLIANCE |
| Intellectual property | Public MTL curated by licence; WDG-EXPORT-CONTROL-IP gate |
| LLM provider drift | Provider change only affects Phase A/B training; gates (Phase C) and canonical artifacts are provider-agnostic |

---

## 11 — Traceability

| Artifact | Reference |
|---|---|
| This standard | AMPEL360-FAM-LC04-ASKM-CAD-001 Rev A |
| Parent specification | LC05-GEN-MODEL-ROLE-SPEC-v0.1 (KNU-ATA96-70-001) |
| Topology invariance proof | KNU-ATA96-70-002 |
| FeatureGraph schema | `feature_graph.schema.json` (this module) |
| Build procedure | `PROC-CAD-BUILD-DET-v1.0.yaml` (this module) |
| Observer config | `.askm/observer/config.yaml` |
| Delineant config | `.askm/delineant/config.yaml` |
| Parent KNOT | KNOT-ATA96-70-00-001 |

---

*Document ID: AMPEL360-FAM-LC04-ASKM-CAD-001 Rev A*
*Programme: ID-A360-Q100 · AMPEL360*
*Classification: Engineering Governance — LC04 Design Review / CAD Module*
*Applicable Standards: CS-25 Amdt 28, ISO 1101, ASME Y14.5, ATA iSpec 2200*
