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
| Create team repository from the ZENAIZ template | Akkepally Aishwarya| Done | GitHub Repository |
| Update `README.md` with the project summary and tools used | Avishka Raikode |  Done | `README.md` |
| Complete `docs/problem_charter.md`  | Harshika.k| `docs/problem_charter.md` |
| Conduct initial team alignment on the project brief | All Team Members |  Done | Weekly Log |
## 3. Key Decisions

- **Adopt Medallion Architecture:** Use the **Bronze → Silver → Gold** architecture to ensure data quality, traceability, and a structured data pipeline.
- **Gold-Only Visualization:** Connect **Power BI** exclusively to **Gold** tables so that all dashboard metrics are based on validated and trusted data.
- **Documentation-First Approach:** Maintain weekly documentation and GitHub evidence throughout the project to ensure transparency and progress tracking.

## 4. Blockers / Risks

| **Blocker** | **Impact** | **Mitigation / Help Needed** |
|--------------|------------|------------------------------|
| **Databricks Free Edition Setup** | Possible delays in accessing clusters or configuring the development environment. | Team troubleshooting and setup verification before development begins. |
| **Data Quality Complexity** | Raw datasets may contain orphan records, invalid codes, missing values, or inconsistent relationships. | Review the Data Quality guidelines and implement validation rules during Week 06. |
| **Large Dataset Handling** | Processing approximately **120,000** records may require careful optimization and testing. | Plan efficient data ingestion and transformation strategies during implementation. |

## 5. Evidence Added to GitHub

- **`README.md`** – Updated with the project summary, project overview, and technical stack.
- **`docs/problem_charter.md`** – Completed the problem context, engineering problem, stakeholder mapping, scope inclusions, scope exclusions, and success criteria.
- **`weekly_logs/week01_log.md`** – Added the Week 01 sprint log documenting the sprint goal, completed tasks, and project progress.

## 6. AI Transparency Note

| **Question** | **Response** |
|--------------|--------------|
| **Where AI helped** | AI assisted in organizing the project documentation, improving the project summary, refining stakeholder mapping, and structuring the problem charter in clear Markdown format. |
| **What we changed after AI suggestion** | We refined the engineering problem, simplified the project scope, improved the success criteria, and enhanced the readability and structure of the documentation. |
| **What we verified manually** | We manually reviewed the project brief, verified the scope inclusions and exclusions, confirmed the stakeholder requirements, and ensured the documentation accurately reflected the project objectives. |
| **What we can explain without AI** | We can clearly explain the RoadSafe architecture, Medallion (Bronze–Silver–Gold) pipeline, Data Quality rules, Power BI dashboard design, streaming simulation, and how each project component addresses stakeholder needs. |

## 7. Next Week Preparation

- Download and inspect the official **UK Department for Transport (STATS19)** collision, vehicle, and casualty CSV datasets.
- Explore the dataset structure, identify primary and foreign keys, and understand the relationships between the files.
- Create a **Data Dictionary** documenting columns, data types, keys, assumptions, and source descriptions.
- Record initial data quality observations, such as missing values, invalid codes, and inconsistent records.
- Organize the datasets in the project workspace to prepare for Bronze layer ingestion in Week 02.
