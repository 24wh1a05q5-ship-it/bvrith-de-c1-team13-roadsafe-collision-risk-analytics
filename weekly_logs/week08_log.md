# Week 08 Log — Power BI Dashboard and Gold Hand-off

**Week:** 8  
**Date range:** 18-09-2026 - 02-10-2026  
**Team:** 13  
**Project:** Roadsafe Collision Risk Analytics 


---

## 1. Sprint Goal

Complete the first working Power BI dashboard using the approved Week 7 Gold-layer tables.  
Validate the Gold-to-Power-BI hand-off, build the required dashboard pages and measures, and document the model, validation, and evidence for the Week 8 submission.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Reviewed and selected approved Gold tables for Power BI | Harshika | Done | `notebooks/05_gold_aggregations.ipynb` |
| Created dashboard-ready monthly collision Gold table | Aishwarya| Done | `gold_monthly_collision_trends` |
| Created readable vehicle type Gold table | Avishka| Done | `gold_vehicle_type_readable` |
| Created readable casualty severity Gold table | Harshika| Done | `gold_casualty_severity_readable` |
| Created vehicle propulsion Gold table | Aishwarya| Done | `gold_vehicle_propulsion_readable` |
| Prepared Power BI export/handoff notebook | Harshika| Done | `notebooks/06_powerbi_export.ipynb` |
| Built Collision Trends dashboard page | Avishka| Done | Power BI screenshot |
| Built Vehicle Type Analysis dashboard page | Harshika| Done | Power BI screenshot |
| Built Casualty Severity Analysis dashboard page | Aishwarya| Done | Power BI screenshot |
| Built Vehicle Propulsion Analysis dashboard page | Harshika| Done | Power BI screenshot |
| Added Power BI measures and KPI cards | Harshika| Done | Power BI report |
| Validated dashboard fields and Gold-table grain | Avishka| Done | Databricks / Power BI evidence |

---

## 3. Key Decisions

- Power BI uses approved Gold-layer tables as the report-facing source rather than Silver or raw data.
- Four Gold tables were selected for the dashboard:
  - `gold_monthly_collision_trends`
  - `gold_vehicle_type_readable`
  - `gold_casualty_severity_readable`
  - `gold_vehicle_propulsion_readable`
- The selected Gold tables are kept separate because they represent different reporting grains.
- The monthly collision trend uses `period_label` sorted by `month_sort`.
- Severe collision rates are calculated from the approved Gold measures using DAX.
- No unsupported business meaning was assigned to propulsion codes.
- Casualty severity code 8 was retained as `Code 8 - Not mapped` rather than assigning an unsupported label.
- Week 8 focuses on building and validating the first working dashboard; further visual refinement and insight storytelling are left for Week 9.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| Propulsion-code mapping was not available in the approved Week 7 source material | Propulsion values are displayed using their codes instead of unsupported business labels | No immediate help required; retain the code-based representation |
| Gold-to-Power-BI export/connection must remain controlled and traceable | Dashboard refresh depends on the approved Gold hand-off | Verify the final export/connection before submission |
| Power BI and Databricks evidence must be genuine | Screenshots must represent the actual completed work | Capture and add the required screenshots |

---

## 5. Evidence Added to GitHub

- `notebooks/06_powerbi_export.ipynb`
- `dashboard/README.md`
- `dashboard/powerbi_dashboard.pbix`
- `screenshots/week08_01_gold_source_register.png`
- `screenshots/week08_02_export_reconciliation.png`
- `screenshots/week08_03_powerbi_model.png`
- `screenshots/week08_04_dashboard_page_01.png`
- `screenshots/week08_05_dashboard_page_*.png`
- `screenshots/week08_06_measure_reconciliation.png`
- `weekly_logs/week08_log.md`

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI was used for implementation support, including notebook structure, validation logic, Power BI DAX measure drafting, dashboard documentation, and troubleshooting. |
| What we changed after AI suggestion | Suggestions were adapted to the actual Gold tables, fields, dashboard pages, and project requirements. Unsupported mappings and assumptions were not added. |
| What we verified manually | Gold table names, table grains, report-facing fields, dashboard visuals, DAX measures, page structure, and Power BI configuration were manually checked against the actual project work. |
| What we can explain without AI | We can explain the Gold-to-Power-BI flow, selected Gold tables, their grains and purposes, dashboard pages, KPI measures, visual configuration, and the validation decisions made during Week 8. |

---

## 7. Next Week Preparation

- Continue with the same Power BI PBIX and Week 8 model.
- Refine visual hierarchy, interactions, and explanatory context.
- Develop the dashboard insight story using the validated Gold data.
- Avoid rebuilding the Gold layer or replacing the validated Week 8 model unnecessarily.
