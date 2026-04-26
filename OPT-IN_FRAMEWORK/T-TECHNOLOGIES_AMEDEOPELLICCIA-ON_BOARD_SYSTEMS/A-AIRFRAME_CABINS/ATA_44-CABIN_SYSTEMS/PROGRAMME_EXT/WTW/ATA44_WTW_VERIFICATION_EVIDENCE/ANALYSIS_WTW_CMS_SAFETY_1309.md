# EVI-001 — WTW CMS System Safety Analysis (CS-25.1309)

**EVI ID:** T-A-ATA44-WTW-EVI-001
**Delta Refs:** DELTA-WTW-44-001, DELTA-WTW-44-002
**Req Refs:** WTW-44-100-001, WTW-44-100-002, WTW-44-000-002
**Standard:** CS-25.1309
**Status:** OPEN — Target LC05
**Parent:** [Evidence README](README.md)

---

## 1) Objective

Demonstrate by analysis that the WTW CMS architecture (CMC + CAC redundant pair) meets
CS-25.1309 failure condition classification and probability requirements.

---

## 2) Scope

| Item | Description |
|------|-------------|
| Function | Cabin Management: lighting control, monitoring, PA interface, IFE control |
| Failure condition category | Loss of CMS — TBD (provisional: Minor to Major — no safety effect on flight) |
| Architecture | CMC primary + CAC failover, no single point of failure for safety-essential functions |
| Tool | TBD (CAFTA / ISOGRAPH / FHA + FTA) |

---

## 3) WTW-Specific Analysis Inputs

> Δ WTW inputs:

- CMC in FWD E/E bay: failure modes include power supply loss, LRU internal fault, overheating.
- CAC in AFT bay: same failure modes, independent power feed assumed.
- Failover time to CAC: TBD s (requirement WTW-44-100-002).
- Combined CMC + CAC loss: provisional classification TBD — only affects passenger comfort
  and non-safety cabin functions.

---

## 4) Evidence Template

| Evidence element | Content | Status |
|-----------------|---------|--------|
| Functional Hazard Assessment (FHA) | CMS function list + failure conditions | TBD at LC04 |
| Fault Tree Analysis (FTA) — CMC loss | Probability of CMC unavailability | TBD at LC05 |
| Fault Tree Analysis (FTA) — both CMC+CAC loss | Combined probability | TBD at LC05 |
| Common Cause Analysis (CCA) | Physical separation / independence of CMC and CAC | TBD at LC05 |

---

## 5) Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Complete FHA for CMS function list | Systems Safety | LC04 |
| Perform FTA for CMC and CAC | Systems Safety | LC05 |
| Confirm failure condition category with authority | Certification | LC05 |
