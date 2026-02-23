# Contributing to AMPEL360 WTW

## KNU-Based Contributor Loop

1. Pick a **KNU** (Knowledge Need Unit) from `SSOT/LC01_PROBLEM_STATEMENT/KNU_PLAN.csv`
2. Create a branch: `knu/<KNU-ID>`
3. Produce evidence (analysis, test, model) — place in `SSOT/`
4. Produce deliverables (S1000D DM, export) — place in `PUB/`
5. Reference the **KNU ID** in every artifact longer than 5 lines (enforced by pre-commit hook)
6. Open a PR; CI validates structure, BREX, and KNU traceability

## Placement Rules

| Content Type | Directory | Format |
|---|---|---|
| Authoritative engineering evidence | `SSOT/` | Markdown, YAML, CSV, XML — **no binaries** |
| S1000D data modules | `PUB/CSDB/DM/` | XML |
| BREX rules | `PUB/CSDB/BREX/` | XML |
| Formatted deliverables | `PUB/EXPORT/` | PDF, HTML, DOCX |

## Pre-Commit Hook

Run `.github/hooks/setup-hooks.sh` once after cloning:

```bash
bash .github/hooks/setup-hooks.sh
```

The hook enforces:
- No binaries (.pdf, .html, .docx, .xlsx) in `SSOT/`
- KNU ID reference in LC02–LC14 artifacts longer than 5 lines

## Validation Commands

```bash
python tools/ci/optin_structure_validator.py --check
python tools/ci/brex_validator.py --dm-dir PUB/CSDB/DM
python tools/knu_distribution.py verify
```
