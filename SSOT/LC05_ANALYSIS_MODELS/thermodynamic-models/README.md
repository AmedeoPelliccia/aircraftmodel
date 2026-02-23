<<<<<<< HEAD
# Thermodynamic Models — LC05 Evidence

<!-- KNU-ATA28-10-002 -->

OpenModelica-based thermodynamic models for C² CELL subsystem analysis.

## KNU Evidence Template

Each model directory shall contain:

| File | Purpose |
|---|---|
| `model.mo` | OpenModelica source |
| `README.md` | Model description, assumptions, boundary conditions |
| `results/` | Simulation outputs (CSV, plots) |
| `validation.md` | Comparison against test data or literature |
=======
# Thermodynamic Simulation Baseline (LC05)

## ID-A360-Q100 — OpenModelica 1D Simulation Standard

This directory contains OpenModelica 1D simulation baselines for the
LH₂/NH₃/N₂ closed-loop propulsion ecosystem.

### Structure

One folder per KNOT, each containing:

- OpenModelica `.mo` model files
- `KNU_EVIDENCE.md` — evidence template with `delta_residual_primary` field
- Input/output parameter definitions
- Acceptance criteria for CI integration

### KNU Evidence Template

Each KNOT simulation folder must include a `KNU_EVIDENCE.md` with:

```yaml
knot_id: KNOT-ATAxx-xx-xx-xxx
knu_id: KNU-ATAxx-xx-xxx
delta_residual_primary: <value>
acceptance_criteria: <description>
status: PLANNED | IN_PROGRESS | COMPLETE | ACCEPTED
```

The `delta_residual_primary` field feeds directly into the TT distribution
formula for impact scoring.

### Planned Models

| KNOT | Model Description | Status |
|---|---|---|
| KNOT-ATA28-10-00-001 | LH₂ tank thermal/structural sizing | PLANNED |
| KNOT-ATA28-20-00-001 | NH₃ cryo-shield boil-off reduction | PLANNED |
| KNOT-ATA28-40-00-001 | NH₃ cracker conversion efficiency | PLANNED |
| KNOT-ATA47-10-00-001 | N₂ purity / contaminant model | PLANNED |
| KNOT-ATA47-40-00-001 | N₂ flood response time simulation | PLANNED |
| KNOT-ATA75-20-00-001 | Waste heat routing thermal model | PLANNED |
>>>>>>> origin/main
