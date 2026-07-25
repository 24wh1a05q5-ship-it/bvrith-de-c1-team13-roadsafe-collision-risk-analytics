# Week 03 Log — Data Quality Validation & Pipeline Preparation Sprint

**Week:** 3  
**Date range:** 23-07-2026  
**Team:** 13  
**Project:** RoadSafe: Collision Risk Analytics  

---

# 1. Sprint Goal

The goal of this week was to validate the RoadSafe datasets, identify data quality issues, and improve the data preparation workflow.

The team focused on dataset inspection, schema validation, missing value analysis, duplicate record detection, and resolving query issues before performing collision risk analysis.

---

# 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Reviewed RoadSafe source datasets and verified file structure | Harshika.k | Done | `W03_01_Dataset_Inspection.jpg` |
| Performed schema validation for collision and vehicle datasets | A.Aishwarya | Done | `W03_02_Schema_Validation.jpg` |
| Checked missing values present in datasets | Avishka Raikode | Done | `W03_03_Missing_Value_Analysis.jpg` |
| Identified duplicate records and analyzed duplicate IDs | Harshika.k | Done | `W03_04_Duplicate_Record_Check.jpg` |
| Validated collision dataset using SQL queries | A.Aishwarya | Done | `W03_05_Collision_Data_Validation.jpg` |
| Validated vehicle dataset and checked relationship with collision data | A.Aishwarya | Done | `W03_06_Vehicle_Data_Validation.jpg` |
| Fixed query issues and verified corrected results using Python/SQL validation | Harshika.k | Done | `W03_07_python_Query_Fix_Result.jpg` |

---

# 3. Key Decisions

- Followed the defined source contract before performing data analysis.
- Performed data quality checks before joining collision and vehicle datasets.
- Decided to validate missing values and duplicate records before generating insights.
- Used improved query handling methods to resolve datatype and join-related issues.
- Maintained proper evidence naming conventions for GitHub documentation.

---

# 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| Some collision IDs contained inconsistent formats | Join operations between datasets failed | Need validation rules for incorrect identifier formats |
| Duplicate records found in datasets | May affect accuracy of collision analysis | Need proper duplicate handling strategy |
| Missing values in some attributes | May impact analytics results | Need data cleaning decisions before final analysis |

---

# 5. Evidence Added to GitHub

Week 03 evidence screenshots added:

Additional updates:

- Added dataset inspection evidence.
- Added schema validation screenshots.
- Added missing value and duplicate record analysis evidence.
- Added collision and vehicle validation results.
- Added query correction and validation evidence.
- Updated Week 03 sprint documentation.

---

# 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | AI helped in understanding SQL errors, improving query logic, and suggesting better approaches for handling data validation problems. |
| What we changed after AI suggestion | Updated queries, improved datatype handling, and organized documentation and evidence files properly. |
| What we verified manually | Dataset structure, schema details, missing values, duplicate records, query outputs, and validation results were manually checked. |
| What we can explain without AI | The team can explain dataset inspection, data quality validation, SQL queries, cleaning decisions, and GitHub workflow. |

---

# 7. Next Week Preparation

- Complete remaining data cleaning activities.
- Finalize cleaned and validated datasets.
- Start exploratory data analysis (EDA) on collision patterns.
- Identify important collision risk factors.
- Prepare initial visualizations and insights.
- Continue updating GitHub documentation.

---

