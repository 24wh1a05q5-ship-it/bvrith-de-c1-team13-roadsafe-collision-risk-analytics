# Week 06 Log — Data Quality & Trusted Silver Routing

**Week:** 6  
**Date range:** August 14, 2026 – August 20, 2026  
**Team:** Team 13  
**Project:** RoadSafe — Road Safety Data Engineering & Intelligence Pipeline

---

## 1. Sprint Goal

Implement and validate DQ-01 to DQ-08 on the Collision, Vehicle, and Casualty Silver Candidate datasets. Classify records as PASS or FAIL and route them into Trusted Silver and Quarantine tables with complete reconciliation.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Implemented DQ-01 to DQ-08 validation checks | Team 13 | Done | Databricks DQ notebook |
| Created PASS/FAIL status views | Team 13 | Done | DQ result screenshots |
| Created Trusted Silver and Quarantine tables | Team 13 | Done | Databricks tables |
| Completed final record reconciliation | Team 13 | Done | Reconciliation output |

### Final Record Routing

| Entity | Candidate | Trusted Silver | Quarantine |
|---|---:|---:|---:|
| Collision | 101,527 | 99,047 | 2,480 |
| Vehicle | 183,514 | 181,655 | 1,859 |
| Casualty | 128,272 | 124,817 | 3,455 |

**Validation:** Candidate = Trusted Silver + Quarantine for all three entities.

---

## 3. Key Decisions

- Used `PASS` and `FAIL` statuses to make DQ results easier to understand and validate.
- Routed records that passed all applicable DQ checks to Trusted Silver and records with failures to Quarantine.
- Used tolerant date/time parsing for invalid values so bad records could be identified instead of stopping the pipeline.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| Invalid date value such as `31/02/2024` | DQ-05 initially produced a date parsing error | Used tolerant date parsing with `try_to_date()` / `try_to_timestamp()` |
| Temporary DQ views were not persistent | Some DQ views needed to be recreated | Recreated required views before final routing |

---

## 5. Evidence Added to GitHub

- `weekly_logs/week06_log.md` — Week 06 progress log.
- `week06_dq_rules.png` — DQ-01 to DQ-08 implementation.
- `week06_dq_results.png` — PASS/FAIL DQ results.
- `week06_trusted_quarantine.png` — Trusted Silver and Quarantine tables.
- `week06_reconciliation.png` — Final Candidate vs Trusted + Quarantine reconciliation.
- Databricks DQ notebook — DQ validation and routing logic.

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI helped structure SQL DQ checks, explain Databricks errors, and organize PASS/FAIL routing. |
| What we changed after AI suggestion | SQL was modified according to the actual RoadSafe columns, tables, and Databricks outputs. |
| What we verified manually | DQ counts, table counts, PASS/FAIL results, Trusted Silver counts, Quarantine counts, and final reconciliation were manually verified in Databricks. |
| What we can explain without AI | We can explain the DQ rules, PASS/FAIL classification, Trusted Silver and Quarantine routing, and the reconciliation process. |

---

## 7. Next Week Preparation

- Validate the Trusted Silver datasets for downstream use.
- Prepare Collision, Vehicle, and Casualty data for integration.
- Begin preparation of KPI-ready datasets for the Gold layer.
