# DETERMINISM_CONTRACT.md
# Document ID: AMPEL360-FAM-ARCH-ELC-001-DET
# Revision: A
# Date: 2026-02-23
# Parent Document: AMPEL360-FAM-ARCH-ELC-001 Rev B (§4 ELC Compiler)

# ELC Compiler — Determinism Contract

**AMPEL360-FAM-ARCH-ELC-001-DET · Rev A · 2026-02-23**

---

## 1  Purpose

This document defines the **determinism contract** for the ELC Compiler —
the requirement that, given identical inputs, the compiler always produces
identical outputs. Determinism is a prerequisite for:

- **Auditability**: a regulatory body must be able to reproduce any
  compilation from archived inputs and verify the output matches the
  deployed SLC instance.
- **Drift detection**: any unintentional change to inputs is immediately
  detectable by comparing compile hashes.
- **Governance**: recompilation requires an ADR (§7 of ELC-001); without
  a determinism contract, "accidental recompilation" cannot be distinguished
  from deliberate architectural change.

> **Contract principle:** `compile(inputs_v1) = compile(inputs_v1)` always,
> regardless of execution time, environment, or operator. If this equality
> ever fails, it is a compiler defect, not an acceptable outcome.

---

## 2  Scope

This contract applies to all executions of `compiler.py` against any
system in the AMPEL360 WTW programme. It covers:

- The compilation of family templates into SLC instances
- The pruning and expansion of SLC phases
- The assignment of zones, concurrency maps, and gate criteria
- The generation of elasticity parameters

It does **not** cover:

- Runtime execution of SLC phases (governed by `scheduler.py`)
- Metrics computation (governed by `metrics.py`)
- Manual edits to ELC_INSTANCE.yaml files (these require an ADR per §7)

---

## 3  Input Versioning Policy

All inputs to the ELC Compiler **must** be version-controlled artefacts
with SHA-256 content hashes. The compiler **must** record the hash of
every input in the compilation manifest (§7).

### 3.1  Mandatory Inputs

| Input | Description | SSOT Location | Hash Field |
|-------|-------------|---------------|------------|
| Family Template | Phase definitions, pruning rules, extension model | `LC05_ANALYSIS_MODELS/ELC_COMPILER/family_templates/family_X_*.yaml` | `family_template_hash` |
| Architectural Drivers | Functional, physical, logical, operational properties | System's `ELC_INSTANCE.yaml` → `architectural_drivers` block | `architectural_drivers_hash` |
| Elasticity Targets | Programme-level η and TTO targets | `LC02_REQUIREMENTS/ELC_ELASTICITY_TARGETS.yaml` | `elasticity_targets_hash` |
| Pruning Rules | Phase collapse/expand rules | Embedded in family template | included in `family_template_hash` |

### 3.2  Input Hash Computation

Each input file's hash is computed as:

```
hash = SHA-256( canonical_form( file_content ) )
```

Where `canonical_form` is defined as:

- YAML files: serialised with sorted keys, no comments, no trailing whitespace
- CSV files: sorted by first column, UTF-8, LF line endings
- Python files: not used as compiler inputs (compiler code is versioned via Git)

The Python `hashlib.sha256` function on the canonical bytes is the
reference implementation.

### 3.3  Prohibited Inputs

The following **must not** be inputs to the compiler:

- Wall-clock timestamps (use programme milestone dates from architectural drivers)
- Environment variables (use explicit config files)
- Random number generators (use deterministic algorithms only)
- External API calls at compile time (fetch-then-compile pattern required)

---

## 4  Reproducibility Guarantee

### 4.1  Compile Hash Definition

The **compile hash** uniquely identifies a compilation and its inputs:

```
compile_hash = SHA-256(
    family_template_hash
    || architectural_drivers_hash
    || elasticity_targets_hash
    || pruning_rules_hash
)
```

Where `||` denotes byte-level concatenation of the 32-byte SHA-256 digests
(all digests concatenated as 128 bytes total, then hashed).

> `pruning_rules_hash` is derived from the pruning rules section of the
> family template. It is included separately to make pruning rule changes
> visible without changing the full template hash.

### 4.2  Guarantee Statement

Given `compile_hash_A = compile_hash_B`, the compiler **must** produce:

1. Identical `slc_phases[]` list (same phase IDs, zones, content, flags)
2. Identical `zone_map{}` (same phase-to-zone assignments)
3. Identical `concurrency_map{}` (same DAG of phase dependencies)
4. Identical `gate_criteria[]` (same entry/exit predicates)
5. Identical `elasticity_params{}` (same η targets, TTO, t_ops values)

The only fields permitted to differ between two compilations with the same
`compile_hash` are:

- `manifest.compiled_at` (timestamp — informational only, not a functional field)
- `manifest.compiler_version` (if the same hash is recomputed with a newer
  compiler, output identity must still hold; if it does not, this is a
  compiler regression)

### 4.3  Idempotency Requirement

Running the compiler twice on the same inputs **must** produce the same
`compile_hash`. If it does not, the compiler has a non-determinism defect
that must be resolved before the compilation is accepted.

---

## 5  Drift Detection

### 5.1  Mechanism

On every **gate evaluation** (SLC phase exit), the ELC runtime **must**:

1. Recompute the `compile_hash` from the current inputs in SSOT
2. Compare to the `compile_hash` stored in `ELC_INSTANCE.yaml`
3. If the hashes match → gate evaluation proceeds normally
4. If the hashes differ → **DRIFT DETECTED** event is raised

### 5.2  Drift Response Protocol

| Drift Severity | Condition | Required Action |
|----------------|-----------|-----------------|
| **CRITICAL** | `family_template_hash` changed | Halt gate. Mandatory recompile + ADR before proceeding. |
| **HIGH** | `architectural_drivers_hash` changed | Halt gate. Review with system architect. ADR required if driver change is intentional. |
| **MEDIUM** | `elasticity_targets_hash` changed | Log warning. Programme-level review required. ADR required if target change is intentional. |
| **LOW** | `pruning_rules_hash` changed (subset of template) | Log warning. Validate that pruning outcome is unchanged. ADR if phases differ. |

### 5.3  Drift Log Entry

Every drift detection event must produce a log entry stored in
`LC_MEMORIES/` with the following fields:

```yaml
drift_event:
  detected_at: "<ISO-8601 timestamp>"
  gate: "<gate ID, e.g. SLC06→SLC07>"
  system_id: "<ATA chapter and name>"
  stored_compile_hash: "<hex string>"
  recomputed_compile_hash: "<hex string>"
  hash_delta:
    family_template_hash: "<changed | unchanged>"
    architectural_drivers_hash: "<changed | unchanged>"
    elasticity_targets_hash: "<changed | unchanged>"
    pruning_rules_hash: "<changed | unchanged>"
  severity: "<CRITICAL | HIGH | MEDIUM | LOW>"
  adr_required: "<true | false>"
  resolution: "<pending | ADR-XXX | accepted-no-change>"
```

---

## 6  Audit Trail

### 6.1  Requirement

Every compilation **must** produce a **compilation manifest** that is:

1. Stored alongside the compiled `ELC_INSTANCE.yaml` in the system's SSOT
   directory
2. Immutable after creation (append-only; mutations require a new compilation)
3. Signed (or at minimum, hash-chained) so tampering is detectable

### 6.2  Compilation Manifest Schema

```yaml
# compilation_manifest.yaml — produced by compiler.py
# DO NOT EDIT MANUALLY. Generated artefact. Governed by DETERMINISM_CONTRACT.

compilation_manifest:
  manifest_version: "1.0"
  document_id: "AMPEL360-FAM-ARCH-ELC-001-DET"

  # Identity
  system_id: "<ATA chapter, e.g. ATA-28-10-00>"
  system_name: "<human-readable name>"
  family_code: "<A | B | C | D | E | F | G>"

  # Timing (informational only — not used in compile_hash)
  compiled_at: "<ISO-8601 UTC timestamp>"
  compiler_version: "<git tag or commit SHA of compiler.py>"

  # Input hashes
  input_hashes:
    family_template_hash: "<SHA-256 hex, 64 chars>"
    architectural_drivers_hash: "<SHA-256 hex, 64 chars>"
    elasticity_targets_hash: "<SHA-256 hex, 64 chars>"
    pruning_rules_hash: "<SHA-256 hex, 64 chars>"

  # Compile hash (deterministic identity)
  compile_hash: "<SHA-256 hex, 64 chars>"

  # Output summary
  output_summary:
    phase_count: <integer>
    phases_pruned: <integer>
    phases_added: <integer>
    zones_assigned:
      compress: <integer>
      transition: <integer>
      extend: <integer>
    gate_count: <integer>
    concurrency_factor: <float>

  # Output hash (hash of ELC_INSTANCE.yaml content)
  output_hash: "<SHA-256 hex, 64 chars>"

  # Manifest self-hash (hash of this manifest with output_manifest_hash set to all zeros)
  manifest_hash: "<SHA-256 hex, 64 chars>"
```

### 6.3  Hash Chain

The manifest is self-describing and hash-chained:

```
manifest_hash = SHA-256(
    manifest_content_with_manifest_hash_zeroed
)
```

This allows detection of post-creation tampering without requiring a
cryptographic signature infrastructure.

---

## 7  Governance Rules

### 7.1  Who May Trigger Recompilation

| Role | Permission | Condition |
|------|-----------|-----------|
| System Architect (SA) | May trigger recompilation | After ADR is drafted |
| ELC Programme Lead | May approve recompilation | Co-signs ADR |
| CI/CD Pipeline | May trigger recompilation | Only on merge to main; only if input hash has changed |
| Any contributor | May NOT trigger recompilation | May only propose via ADR draft |

### 7.2  Approval Workflow

```
1. Contributor identifies need for recompilation
2. Contributor drafts ADR in LC_MEMORIES/ with:
   - Change description
   - Affected inputs (which hashes will change)
   - Expected diff in SLC instance
   - Justification (why this is needed)
3. System Architect reviews ADR
4. ELC Programme Lead co-signs ADR
5. compiler.py is run by CI/CD on merge of the ADR + input changes
6. New compilation manifest is stored; drift detection threshold updated
7. ADR is closed with reference to new compile_hash
```

### 7.3  Emergency Recompilation

In cases where a safety finding requires immediate recompilation (e.g.,
a DAL escalation from SLC05 analysis), the following applies:

- An interim ADR (marked `urgency: HIGH`) may be approved by the System
  Architect alone, with ELC Programme Lead review within 5 working days
- The compilation proceeds under the interim ADR
- The full ADR process (§7.2) must be completed retrospectively

### 7.4  Compiler Version Control

- `compiler.py` is versioned in Git; the compiler version recorded in the
  manifest is the Git commit SHA or tag
- Compiler upgrades (new features, bug fixes) must be validated to produce
  identical output for all existing `compile_hash` values before deployment
- Any compiler change that alters output for an unchanged `compile_hash` is
  classified as a **compiler regression** and must be resolved before release

---

## 8  Non-Conformance

Any `ELC_INSTANCE.yaml` in the repository that lacks a corresponding
`compilation_manifest.yaml` is considered **non-conformant** and must
be remediated. The CI/CD pipeline will flag non-conformant instances.

Non-conformance does not invalidate the SLC instance content, but it does
prevent gate evaluation until the manifest is generated and stored.

---

<p align="center"><em>AMPEL360 WTW · ELC Compiler Determinism Contract · AMPEL360-FAM-ARCH-ELC-001-DET Rev A</em></p>
