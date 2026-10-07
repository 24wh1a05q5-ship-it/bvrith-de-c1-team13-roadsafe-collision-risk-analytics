# Week 09 Log — Dashboard Refinement and Insight Communication

**Week:** 9  
**Date range:** 02-10-2026 - 09-10-2026 
**Team:** 13  
**Project:** RoadSafe Collision Risk Analytics

---

## 1. Sprint Goal

Refine and validate the existing Week 8 Power BI dashboard without rebuilding it.

Test dashboard interactions, complete final Gold-to-Power BI reconciliation, document evidence-backed insights, and prepare the final Week 9 documentation and evidence.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Reviewed all four Power BI dashboard pages | Harshika | Done | `dashboard/powerbi_dashboard.pbix` |
| Reviewed dashboard visual clarity and hierarchy | Aishwarya | Done | Power BI dashboard |
| Tested Month slicer | Avishka| Done | Week 9 filter interaction screenshot |
| Tested Vehicle Type slicer | Harshika| Done | Week 9 filter interaction screenshot |
| Tested Age Group slicer | Aishwarya| Done | Week 9 filter interaction screenshot |
| Tested Propulsion Type slicer | Harshika | Done | Week 9 filter interaction screenshot |
| Completed final Gold-to-Power BI reconciliation | Avishka | Done | `week09_05_filtered_reconciliation.png` |
| Reconciled January Total Collisions | Harshika| Done | Power BI + Gold validation query |
| Created dashboard insight documentation | Harshika | Done | `docs/dashboard_insights.md` |
| Updated Power BI README | Aishwarya| Done | `dashboard/README.md` |

---

## 3. Key Decisions

- The existing Week 8 Power BI dashboard was retained because all four dashboard pages were already clean and readable.
- No unsupported relationships were added between the independent Gold tables.
- Existing KPI meanings and approved Gold sources were retained.
- Dashboard slicers were tested within their relevant reporting scope.
- A January filtered reconciliation was performed for Total Collisions.
- The January Power BI value of 8,153 matched the owning Gold table value of 8,153.
- Dashboard insights were written as evidence-backed observations without unsupported causal claims.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| No blocking issue identified | No impact on Week 9 completion | None |
| Independent Gold tables have separate reporting grains | Some slicers do not need to affect unrelated Gold-based visuals | Documented in README |
| Propulsion mapping is not project-approved | Propulsion values remain represented using propulsion codes | None |
| Casualty severity code 8 is not mapped | Code 8 remains explicitly unmapped | None |

---

## 5. Evidence Added to GitHub

- `dashboard/powerbi_dashboard.pbix`
- `dashboard/README.md`
- `docs/dashboard_insights.md`
- `screenshots/week09_01_final_model.png`
- `screenshots/week09_02_refined_page_01.png`
- `screenshots/week09_04_filter_interaction.png`
- `screenshots/week09_05_filtered_reconciliation.png`
- `screenshots/week09_06_insights_evidence.png`
- `weekly_logs/week09_log.md`

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI helped structure the Week 9 workflow, validation queries, README documentation, insight documentation, and weekly log. |
| What we changed after AI suggestion | Documentation and validation steps were adapted to the actual dashboard structure, Gold tables, slicers, and observed outputs. |
| What we verified manually | Dashboard pages, slicer behavior, Power BI values, Gold query results, and the January reconciliation were manually checked. |
| What we can explain without AI | The Gold table purposes and grains, dashboard page structure, slicer behavior, reconciliation process, and final validated values. |

---

## 7. Next Week Preparation

- Preserve the validated Week 9 Power BI dashboard as the batch-reporting baseline.
- Begin the Week 10 streaming branch according to the project requirements.
- Do not redesign the Week 9 dashboard around streaming before the approved streaming Gold design is available.
