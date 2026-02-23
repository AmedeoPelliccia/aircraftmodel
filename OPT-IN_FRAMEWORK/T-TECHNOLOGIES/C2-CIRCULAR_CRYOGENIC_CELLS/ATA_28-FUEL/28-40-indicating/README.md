# ATA 28-40 — State Monitoring & Diagnostics

<!-- KNU-ATA28-40-001 -->

| Field | Value |
|---|---|
| **C² CELL Function** | State Monitoring & Diagnostics |
| **Legacy Title** | ATA 28-40 Indicating |
| **Safety Class** | SC1 |

## Scope

This sub-chapter covers the sensor suite, data acquisition, and diagnostic
logic for real-time monitoring of the C² CELL state vector.

### Key Topics

- State-vector instrumentation: mass (M), pressure (P), thermal (T), grade (G)
- Cryogenic level sensing (capacitance, ultrasonic, optical)
- Hydrogen leak detection (catalytic, semiconductor, fibre-optic)
- NH₃ concentration monitoring (electrochemical, IR absorption — WTW variant)
- Data bus architecture (ARINC 664 / TTP integration)
- Prognostics and health management (PHM) for reservoir integrity
- Flight-deck displays and crew alerting (EICAS / CAS messages)

### State Vector Display

```
S_i = (M_i, P_i, T_i, G_i)

  M_i  = stored mass of prime material       [kg]   → fuel quantity gauge
  P_i  = pressure state                      [bar]  → pressure indicator
  T_i  = thermal state                       [K]    → temperature indicator
  G_i  = phase / grade indicator             [–]    → phase status lamp
```

### Design Drivers

| Driver | Metric | Target |
|---|---|---|
| Mass measurement accuracy | % full-scale | ≤ 1.0 |
| Leak detection response | seconds | ≤ 5.0 |
| Sensor redundancy | independent channels | ≥ 2 (dissimilar) |

### KNU Traceability

| KNU ID | Description | Status |
|---|---|---|
| KNU-ATA28-40-001 | State-vector sensor suite definition | OPEN |
