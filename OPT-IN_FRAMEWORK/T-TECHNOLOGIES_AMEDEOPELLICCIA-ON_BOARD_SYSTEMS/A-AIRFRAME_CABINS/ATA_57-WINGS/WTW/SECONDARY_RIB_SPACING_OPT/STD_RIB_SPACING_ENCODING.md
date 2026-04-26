# Wing Rib Spacing — 8-Bit Register Encoding Standard

**Module:** Wing Rib Spacing Optimisation
**Doc ID:** T-A-ATA57-WTW-RIBOPT-ENC-001
**Lifecycle gate:** LC57-03
**Status:** DRAFT

## 1. Purpose
Defines the standard 8-bit register encoding used to represent discrete rib spacing
values for the AMPEL360 WTW optimisation module. This encoding ensures deterministic,
reproducible, and integer-compatible representation of rib spacing for all optimisation runs.

## 2. Register Definition

| Field | Value |
|-------|-------|
| Register width | 8 bits (unsigned integer, 0–255) |
| Physical minimum spacing (register = 0) | S_min = TBD mm |
| Physical maximum spacing (register = 255) | S_max = TBD mm |
| Resolution (step size) | Δs = (S_max − S_min) / 255 mm/LSB |
| Bias | S_min (zero-offset) |

### 2.1 Encoding Formula
```
S_physical [mm] = S_min + register_value × Δs
```

### 2.2 Decoding Formula
```
register_value = round( (S_physical − S_min) / Δs )
```
Where `round()` is round-half-to-even (banker's rounding), consistent with IEEE 754.

## 3. Boundary Conditions

| Condition | Register Value | Physical Meaning |
|----------|---------------|-----------------|
| Minimum manufacturable spacing | 0 | S_min — limited by rib tooling pitch |
| Maximum allowable spacing | 255 | S_max — limited by skin buckling analysis |
| Fuel/LH₂ tank bay boundary constraint | Reserved range TBD | Certain register values reserved for tank boundary ribs |
| Access panel bay | Reserved range TBD | Minimum spacing enforced by access requirements |

## 4. Rib Bay Register Pack Format
Each rib bay is described by a YAML entry:
```yaml
rib_bay:
  bay_id: RB-XXX           # three-digit sequential from root
  spanwise_eta: 0.00–1.00  # non-dimensional span station of outboard rib face
  register_value: 0–255    # encoded spacing
  spacing_mm: TBD          # decoded physical spacing (auto-computed from register)
  notes: ""                # special designations (tank boundary, access, etc.)
```

## 5. Version Control
The register encoding parameters (S_min, S_max) are **frozen at LC57-03 exit gate** and
shall not be changed without a formal delta (CHG entry in ATA57_WTW_DELTA_LOG.yaml).
Any change to S_min or S_max invalidates all previously computed optimisation results and
requires rerun of the optimisation with the new encoding parameters.

## 6. Traceability
| Requirement | Register Encoding Rationale |
|------------|----------------------------|
| REQ-WTW-57-RIBOPT-001 (8-bit) | 256 levels provides < 1 mm resolution for typical wing rib pitch ranges of 200–455 mm |
| REQ-WTW-57-RIBOPT-002 (determinism) | Integer encoding eliminates floating-point non-determinism |
| REQ-WTW-57-RIBOPT-005 (boundary) | Reserved register values for structural discontinuities |
