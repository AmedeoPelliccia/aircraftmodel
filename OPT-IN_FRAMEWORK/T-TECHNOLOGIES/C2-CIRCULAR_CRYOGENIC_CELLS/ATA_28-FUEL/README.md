# ATA 28 — Fuel System

ATA Chapter 28 covers the fuel system, including fuel storage, distribution, indication, and jettison systems.

## Overview

This directory contains the specifications, designs, and documentation for the aircraft fuel system according to ATA iSpec 2200 Chapter 28.

## Scope

The fuel system encompasses:

1. **Fuel Storage** (ATA 28-10)
   - Fuel tanks
   - Tank structure and sealing
   - Cryogenic containment systems

2. **Fuel Distribution** (ATA 28-20)
   - Fuel pumps
   - Fuel lines and manifolds
   - Fuel valves and controls

3. **Fuel Indication** (ATA 28-30)
   - Fuel quantity indicating system
   - Fuel temperature monitoring
   - Fuel pressure indication

4. **Fuel Jettison** (ATA 28-40)
   - Jettison system
   - Emergency fuel dump

5. **Refueling/Defueling** (ATA 28-50)
   - Ground refueling systems
   - In-flight refueling (if applicable)

## Technology Considerations

### Cryogenic Fuel Systems

The C2-CIRCULAR_CRYOGENIC_CELLS implementation supports:
- **LH2** (Liquid Hydrogen): Stored at -253°C
- **NH3** (Ammonia): Stored at -33°C
- **N2** (Nitrogen): Used for purging and inerting

### Safety Requirements

Critical safety considerations per repository memories:
- Safety-critical DMs (Data Modules) require `safetyClass="SC1"` designation
- ATA 28 DMs require `cautionRef` elements for hydrogen handling
- NH3 DMs require `warningRef` elements for toxicity concerns

## Documentation Structure

The `ATA-28-fuel/` subdirectory contains detailed specifications and implementation documents.

## References

- ATA iSpec 2200 Chapter 28
- AMPEL360 FAM IBD-001 (Inheritance Boundary Definition)
- BREX validation rules for ATA 28 documentation
