# Week 07 Log — Trusted Silver to Gold

**Week:** 7  
**Date range:** 04-09-2026 to 09-09-2026  
**Team:** 13  
**Project:** Road Accident Data Engineering Project - RoadSafe Collision Risk Analytics

---

## 1. Sprint Goal

The goal of Week 7 was to transform mentor-approved Trusted Silver data into
validated, dashboard-ready Gold tables.

The team defined KPI contracts, declared table grains and scope, created Gold
Delta tables, and performed validation and controlled rerun checks to ensure
that the Gold outputs were reliable and reproducible.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Defined Gold KPI contracts and table grains | Harshika | Done | `docs/gold_metrics_definition.md` |
| Profiled and validated Trusted Silver collision data before Gold aggregation | Aishwarya | Done | `notebooks/05_gold_aggregations.ipynb` |
| Created `gold_collision_monthly_summary` | Harshika | Done | `notebooks/05_gold_aggregations.ipynb` |
| Validated collision monthly summary grain, keys, measures and scope | Aishwarya | Done | `notebooks/05_gold_aggregations.ipynb` |
| Created `gold_vehicle_type_summary` | Harshika | Done | `notebooks/05_gold_aggregations.ipynb` |
| Validated vehicle type summary measures, scope and rerun consistency | Aishwarya | Done | `notebooks/05_gold_aggregations.ipynb` |
| Created `gold_casualty_severity_summary` | Harshika | Done | `notebooks/05_gold_aggregations.ipynb` |
| Validated casualty severity summary measures, scope and rerun consistency | Aishwarya | Done | `notebooks/05_gold_aggregations.ipynb` |
| Performed controlled rerun comparisons for Gold outputs | Harshika | Done | `notebooks/05_gold_aggregations.ipynb` |
| Updated Gold metric documentation | Avishka | Done | `docs/gold_metrics_definition.md` |

---

## 3. Key Decisions

- Gold tables were built only from the approved Trusted Silver tables:
  `trusted_silver_collisions`, `trusted_silver_vehicles`, and
  `trusted_silver_casualties`.

- Candidate and Quarantine data were not used as Gold inputs.

- The team used explicit scope conditions based on the project data-quality
  keys:
  - `collision_index IS NOT NULL`
  - `vehicle_key IS NOT NULL`
  - `casualty_key IS NOT NULL`

- No joins were required for the three selected Gold KPIs, avoiding join
  amplification and lookup-matching risks.

- `collision_ref_no` was not used as the unique Gold collision key because
  duplicate reference numbers were present in the Trusted Silver data while
  representing different collision records.

- The Gold tables use declared business grains:
  - One row per `collision_year + collision_month + urban_rural_group`
  - One row per `collision_year + vehicle_type`
  - One row per `collision_year + casualty_age_group + casualty_severity`

- Audit timestamps such as `gold_created_at` are treated separately from
  business values during controlled rerun comparisons.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| Some `collision_ref_no` values occurred more than once in Trusted Silver | Required additional key investigation before deciding the Gold grain | No additional help required after validation |
| 100 Trusted Silver collision rows had a null `collision_index` | Required an explicit Gold scope decision | No additional help required after scope validation |
| Gold outputs must remain reproducible across reruns | Required controlled rerun and two-way comparison checks | No additional help required |

---

## 5. Evidence Added to GitHub

- `notebooks/05_gold_aggregations.ipynb` updated with the Week 7 Gold
  aggregation workflow and validation queries.
- `docs/gold_metrics_definition.md` updated with the approved Gold table
  catalog and KPI definitions.
- `weekly_logs/week07_log.md` updated with Week 7 work, decisions,
  validation approach, AI transparency, and next-week preparation.
- Genuine execution screenshots for Week 7 should be added under:
  `screenshots/week07_*`

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI was used to help structure the Week 7 Gold KPI contracts, suggest validation queries, organize the Gold notebook workflow, and draft documentation. |
| What we changed after AI suggestion | The suggested generic Gold design was adapted to the actual road-accident project tables, fields, business grains, and Trusted Silver scope. The generic starter metric and unrelated example tables were removed. |
| What we verified manually | The team manually checked the available Trusted Silver tables and schemas, investigated duplicate `collision_ref_no` values and null `collision_index` rows, executed the Gold creation queries, checked keys and measures, reconciled Gold totals with the eligible Trusted Silver population, and performed controlled rerun comparisons. |
| What we can explain without AI | The team can explain the purpose, KPI formula, grain, source table, scope condition, validation checks, and business meaning of each Gold table created during Week 7. |

---

## 7. Next Week Preparation

- Review the validated Gold tables and prepare them for the next approved
  project stage.

- Preserve the documented KPI definitions, table grains, scope rules, and
  validation evidence for downstream consumption.

- Ensure the Week 7 notebook, documentation, execution evidence, and weekly
  log are complete before the mentor review.

- Do not modify the Gold business definitions without documenting and
  validating any approved changes.
