# Week 04 Log — Bronze Layer Data Ingestion
 

**Week:** 4  
**Date range:** July 31, 2026 – August 6, 2026    
**Team:** Team 13
**Project:** RoadSafe – Road Accident Data Engineering Pipeline 

---

## 1. Sprint Goal

The goal of this sprint was to ingest the raw road accident datasets into the Bronze layer of the Medallion Architecture using Databricks. We loaded the source CSV files, validated their structure, added ingestion metadata, and stored them as Delta tables for further processing.

---

## 2. Work Completed

| Task | Owner | Status | Evidence |
|---|---|---|---|
| Created Week 4 Bronze ingestion notebook | Team 13 | Done | 02_bronze_ingestion.ipynb |
| Uploaded raw datasets to Unity Catalog Volume | Team 13 | Done | Volume pg-13 |
| Loaded collisions dataset | Team 13 | Done | Notebook output |
| Loaded casualties dataset | Team 13 | Done | Notebook output |
| Loaded vehicles dataset | Team 13 | Done | Notebook output |
| Loaded collision code lookup dataset | Team 13 | Done | Notebook output |
| Verified schemas and record counts | Team 13 | Done | Notebook screenshots |
| Added ingestion timestamp metadata | Team 13 | Done | Bronze DataFrames |
| Created Bronze Delta tables | Team 13 | Done | Databricks Catalog |
| Verified Bronze tables and row counts | Team 13 | Done | Notebook output |


---

## 3. Key Decisions

- Adopted the Medallion Architecture by storing raw datasets in the Bronze layer before any transformations.
- Used Unity Catalog Volumes instead of DBFS because DBFS root is disabled in Databricks Free Edition.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| DBFS root access was disabled | Could not read files from /FileStore | Resolved by using Unity Catalog Volumes |
| input_file_name() not supported in Unity Catalog | Could not capture source file metadata | Used supported metadata approach and ingestion timestamp |
---

## 5. Evidence Added to GitHub

- Updated 02_bronze_ingestion.ipynb
- Added Week 4 notebook screenshots
- Updated weekly_logs/week04_log.md

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | Assisted in writing PySpark code for reading CSV files, adding metadata, creating Bronze tables, and troubleshooting Databricks errors. |
| What we changed after AI suggestion | Updated file paths to Unity Catalog Volumes and modified the ingestion process to work with Unity Catalog. |
| What we verified manually | Verified dataset previews, schemas, record counts, and successful creation of Bronze Delta tables in Databricks. |
| What we can explain without AI | The Bronze layer ingestion workflow, Medallion Architecture, Unity Catalog Volumes, Delta tables, and the notebook implementation. |

---

## 7. Next Week Preparation

- Clean and standardize Bronze data to create Silver tables.

- Apply data quality checks, joins, and transformations required for analytical processing.
