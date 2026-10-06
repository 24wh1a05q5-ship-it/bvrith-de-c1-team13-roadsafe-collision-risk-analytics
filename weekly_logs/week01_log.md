# Week 01 Log — Project Framing & Setup

**Week:** 1  
**Date Range:** July 10, 2026 – July 16, 2026  
**Team:** 13  

**Project:** RoadSafe: Collision Risk Analytics

## 1. Sprint Goal

The goal for this week was to initialize the project by setting up the GitHub repository using the official template and establishing the project foundation. This included defining the project mission, identifying stakeholders, documenting the engineering problem, and outlining the project scope. The objective was to create a clear roadmap for transforming raw road collision data into a trusted lakehouse pipeline.

## 2. Work Completed

| Task | Owner | Status | Evidence |
|------|-------|--------|----------|
| Create team repository from the ZENAIZ template | Akkepally Aishwarya | Done | GitHub Repository |
| Update `README.md` with the project summary and tools used | Raikode Avishka | Done | `README.md` |
| Complete `docs/problem_charter.md` | Harshika K. | Done | `docs/problem_charter.md` |
| Conduct initial team alignment on the project brief | All Team Members | Done | Weekly Log |

## 3. Key Decisions

- **Adopt Medallion Architecture:** Use the **Bronze → Silver → Gold** architecture to support data quality, traceability, and structured data processing.
- **Gold-Only Visualization:** Connect **Power BI** exclusively to **Gold** tables so that dashboard metrics are based on validated and trusted data.
- **Documentation-First Approach:** Maintain weekly documentation and GitHub evidence throughout the project to ensure transparency and progress tracking.
- **Data Quality as a Core Requirement:** Plan validation and quarantine rules for identifying invalid, incomplete, or inconsistent records during the data processing stages.

## 4. Blockers / Risks

| **Blocker** | **Impact** | **Mitigation / Help Needed** |
|--------------|------------|------------------------------|
| **Databricks Free Edition Setup** | Possible delays in accessing clusters or configuring the development environment. | Team troubleshooting and setup verification before development begins. |
| **Data Quality Complexity** | Raw datasets may contain orphan records, invalid codes, missing values, or inconsistent relationships. | Define and implement appropriate validation rules during the data processing stages. |
| **Large Dataset Handling** | Processing a large number of records may require careful optimization and testing. | Plan efficient ingestion and transformation strategies during implementation. |

## 5. Evidence Added to GitHub

- **`README.md`** – Updated with the project summary, project overview, and technical stack.
- **`docs/problem_charter.md`** – Completed the problem context, engineering problem, stakeholder mapping, scope inclusions, scope exclusions, assumptions, and success criteria.
- **`weekly_logs/week01_log.md`** – Added the Week 01 sprint log documenting the sprint goal, completed tasks, key decisions, risks, and next-week preparation.

## 6. AI Transparency Note

| **Question** | **Response** |
|--------------|--------------|
| **Where AI helped** | AI assisted in organizing the project documentation, improving the project summary, refining stakeholder descriptions, and structuring the problem charter in Markdown format. |
| **What we changed after AI suggestion** | The team reviewed and adapted the suggested content to match the RoadSafe project requirements, scope, architecture, and academic objectives. |
| **What we verified manually** | We manually reviewed the project brief, scope, stakeholder requirements, architecture decisions, and documentation before adding the files to GitHub. |
| **What we can explain without AI** | We can explain the RoadSafe problem, Medallion Architecture, planned data flow, stakeholder requirements, project scope, and the purpose of the Bronze, Silver, and Gold layers. |

## 7. Next Week Preparation

- Download and inspect the official **UK Department for Transport (STATS19)** collision, vehicle, and casualty CSV datasets.
- Explore the dataset structure, identify primary and foreign keys, and understand the relationships between the files.
- Create a **Data Dictionary** documenting columns, data types, keys, assumptions, and source descriptions.
- Record initial data quality observations, such as missing values, invalid codes, and inconsistent records.
- Organize the datasets in the project workspace to prepare for Bronze layer ingestion in Week 02.
