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
| Created Week 4 Bronze ingestion notebook | Akkepally Aishwarya | Done | week04_bronze_ingestion.png |
| Uploaded raw datasets to Unity Catalog Volume | Raikode Avishka | Done | week04_unity_catalog_volume.png|
| Loaded collisions dataset | Akkepally Aishwarya | Done | week04_collisions_loaded.png |
| Loaded casualties dataset | Harshika K. | Done |  week04_casualties_loaded.png|
| Loaded vehicles dataset | Raikode Avishka | Done | week04_vehicles_loaded.png |
| Loaded collision code lookup dataset | Akkepally Aishwarya | Done | week04_collision_lookup_loaded.png |
| Verified schemas and record counts | Harshika K. | Done | week04_schema_record_counts.png |
| Added ingestion timestamp metadata | Akkepally Aishwarya | Done |week04_ingestion_metadata.png|
| Created Bronze Delta tables | Raikode Avishka | Done | week04_bronze_delta_tables.png |
| Verified Bronze tables and row counts | Harshika K. | Done | week04_bronze_verification.png |

---

## 3. Key Decisions

- Adopted the Medallion Architecture by storing raw datasets in the Bronze layer before applying transformations.
- Used Unity Catalog Volumes instead of DBFS because DBFS root access is disabled in Databricks Free Edition.
- Added ingestion timestamp metadata to improve traceability of Bronze records.
- Stored the ingested datasets as Delta tables for reliable downstream processing.

---

## 4. Blockers / Risks

| Blocker | Impact | Help Needed |
|---|---|---|
| DBFS root access was disabled | Could not read files from `/FileStore` | Resolved by using Unity Catalog Volumes |
| `input_file_name()` was not supported in the Unity Catalog environment | Could not capture source file metadata using the original approach | Used a supported metadata approach and ingestion timestamp |
| Multiple related road accident datasets required validation | Schema and record-count mismatches could affect downstream processing | Validated schemas and record counts before creating Bronze tables |

---

## 5. Evidence Added to GitHub

- Updated `02_bronze_ingestion.ipynb`
- Added Week 04 Bronze ingestion screenshots under `screenshots/`
- Updated `weekly_logs/week04_log.md`

---

## 6. AI Transparency Note

| Question | Response |
|---|---|
| Where AI helped | Assisted in writing PySpark code for reading CSV files, adding ingestion metadata, creating Bronze tables, and troubleshooting Databricks errors. |
| What we changed after AI suggestion | Updated file paths to Unity Catalog Volumes and modified the ingestion process to work with Unity Catalog. |
| What we verified manually | Verified dataset previews, schemas, record counts, ingestion metadata, and successful creation of Bronze Delta tables in Databricks. |
| What we can explain without AI | The Bronze layer ingestion workflow, Medallion Architecture, Unity Catalog Volumes, Delta tables, ingestion metadata, and the notebook implementation. |

---

## 7. Next Week Preparation

- Clean and standardize Bronze data to create Silver tables.
- Apply data quality checks to identify invalid or missing records.
- Join the required datasets using appropriate keys.
- Apply the transformations required for analytical processing.
- Prepare the cleaned data for the Silver layer.
