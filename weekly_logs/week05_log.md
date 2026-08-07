# Week 05 Log — Silver Candidate Transformations

**Week:** 5  
**Date range:** August 7, 2026 – August 13, 2026  
**Team:** Team 13  
**Project:** RoadSafe — UK Road Safety Data Engineering & Safety Intelligence Dashboard

---

## 1. Sprint Goal

Develop the **Silver Candidate transformation layer** from the Bronze road-safety datasets. Convert raw string fields into appropriate data types, standardize important fields, create analytical keys and derived attributes, and validate that records are preserved during transformation.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Created Silver Candidate transformation for collision data | Harshika | Done | `03_silver_transformations.ipynb` |
| Converted collision fields from strings to appropriate numeric types | Avishka | Done | Notebook output / schema |
| Created `collision_timestamp` using tolerant timestamp parsing | Aishwarya | Done | Notebook output |
| Created collision time features such as month, hour, weekday and time band | Harshika | Done | Notebook output |
| Created severe-collision and urban/rural analytical flags | Avishka | Done | Notebook output |
| Created Silver Candidate transformation for vehicle data | Aishwarya | Done | `03_silver_transformations.ipynb` |
| Created `vehicle_key` using collision and vehicle references | Harshika | Done | Notebook output |
| Created Silver Candidate transformation for casualty data | Avishka | Done | `03_silver_transformations.ipynb` |
| Created `casualty_key` and casualty analytical fields | Aishwarya | Done | Notebook output |
| Compared Bronze and Candidate row counts | Harshika | Done | Validation output |
| Checked duplicate and missing key components | Aishwarya | Done | Notebook output |

---

## 3. Key Decisions

- Used `try_cast()` through Spark SQL expressions for numeric conversion so invalid values become `NULL` rather than causing the pipeline to fail.
- Used `try_to_timestamp()` for collision date/time parsing so invalid dates such as `31/02/2024 20:55` are retained as records with a `NULL` timestamp instead of being deleted.
- Preserved Bronze row counts during Candidate transformations.
- Created stable `vehicle_key` and `casualty_key` values using collision and reference identifiers.
- Kept potentially defective records in the Candidate layer for later **data-quality validation and quarantine**, rather than deleting them during transformation.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| Invalid date values were present in collision data | Standard timestamp parsing caused the notebook to fail | Used tolerant `try_to_timestamp()` parsing |
| Bronze source fields were stored largely as strings | Required explicit type conversion before analytical processing | Used `try_cast()` during Silver Candidate creation |
| Potential duplicate or incomplete vehicle/casualty keys | Could affect later joins and relationship validation | To be investigated during Silver data-quality checks |

---

## 5. Evidence Added to GitHub

- Updated `03_silver_transformations.ipynb`
- Added notebook outputs showing Bronze-to-Silver Candidate transformations
- Added schema validation screenshots
- Added row-count validation screenshots
- Added vehicle and casualty key validation evidence
- Added screenshots showing handling of invalid collision timestamps

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI helped structure the Silver Candidate transformation steps, suggest Spark/PySpark expressions, and explain validation approaches. |
| What we changed after AI suggestion | We changed timestamp parsing from standard `to_timestamp()` to tolerant `try_to_timestamp()` after encountering an invalid source date such as `31/02/2024 20:55`. |
| What we verified manually | We manually checked the Bronze schemas, column names, data types, row counts, transformed records, keys, and notebook outputs. |
| What we can explain without AI | We can explain the Bronze-to-Silver transformation process, why type conversion is required, why invalid records should be retained for later quality checks, how row-count validation works, and how vehicle/casualty keys are constructed. |

---

## 7. Next Week Preparation

- Implement Silver **data-quality rules** for invalid, missing, and inconsistent records.
- Identify and quarantine defective records without silently deleting them.
- Validate collision-to-vehicle and collision-to-casualty relationships.
- Create trusted Silver tables from the Candidate datasets.
- Prepare the cleaned Silver layer for Gold KPI and dashboard development.
