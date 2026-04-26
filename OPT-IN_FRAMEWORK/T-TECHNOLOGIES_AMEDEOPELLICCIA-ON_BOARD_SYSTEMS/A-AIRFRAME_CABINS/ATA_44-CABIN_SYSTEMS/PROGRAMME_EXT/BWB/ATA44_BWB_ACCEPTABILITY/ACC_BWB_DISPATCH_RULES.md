# ACC-BWB-44-002 — BWB CMS Dispatch Rules (MEL Provisions)

**Doc ID:** T-A-ATA44-BWB-ACC-002
**Status:** DRAFT (LC01 — MEL details at LC05)
**Parent:** [Acceptability README](README.md)

---

## Scope

BWB-specific dispatch rules for ATA 44 Cabin Systems in degraded configurations.
These rules govern dispatch with one or more zone controllers, bay bridge units,
or IFE bay nodes inoperative.

> Δ BWB vs WTW:
> WTW dispatch rules cover single CMC/CAC failure.
> BWB requires per-bay ZC failure dispatch rules AND inter-bay BBU failure rules
> because the distributed architecture has more independent inoperative combinations.

---

## Zone Controller (ZC) Inoperative — One Bay

| Condition | Dispatch? | Rectification interval | Operational restriction |
|-----------|----------|----------------------|------------------------|
| ZC inoperative in 1 bay (redundant ZC OK) | YES | TBD [LC05] | None (redundant ZC covers bay) |
| Both ZCs inoperative in 1 bay | TBD [LC05] | TBD [LC05] | Crew advisory; affected bay PA from adjacent ZC via BBU |
| ZCs inoperative in 2 or more bays | TBD [LC05] | TBD [LC05] | Safety assessment required |

---

## Bay Bridge Unit (BBU) Inoperative

| Condition | Dispatch? | Rectification interval | Operational restriction |
|-----------|----------|----------------------|------------------------|
| Single BBU inoperative (1 inter-bay boundary) | YES | TBD [LC05] | Adjacent bays operate independently; PA sync degraded |
| Two adjacent BBUs inoperative | TBD [LC05] | TBD [LC05] | Bay isolation; crew advisory |

---

## IFE Bay Node (IBN) Inoperative — One Bay

| Condition | Dispatch? | Rectification interval | Operational restriction |
|-----------|----------|----------------------|------------------------|
| Single IBN inoperative | YES | TBD [LC05] | IFE not available in affected bay; passenger advisory |
| Two or more IBNs inoperative | YES | TBD [LC05] | Extended IFE outage; operator discretion |

---

## Open Actions

| Action | Owner | Target LC |
|--------|-------|-----------|
| Confirm per-bay MEL provisions with Safety team | Systems Safety | LC05 |
| Coordinate MEL references with ATA 44 operations team | Engineering / Operations | LC05 |
| Produce MEL procedures for AMO / crew | TechPubs | LC07 |

---

## Related Documents

- [REQ_BWB_44_100_CABIN_CORE.yaml](../ATA44_BWB_REQUIREMENTS/REQ_BWB_44_100_CABIN_CORE.yaml)
- [ANALYSIS_BWB_CMS_SAFETY_1309.md](../ATA44_BWB_VERIFICATION_EVIDENCE/ANALYSIS_BWB_CMS_SAFETY_1309.md)
- [WTW parallel dispatch rules](../../WTW/ATA44_WTW_ACCEPTABILITY/ACC_WTW_DISPATCH_RULES.md)
