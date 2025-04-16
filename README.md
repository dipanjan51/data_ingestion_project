# Data Ingestion Project based on Airlines Data

This project is a complete end-to-end data engineering and visualization pipeline focused on U.S. domestic airline flight data. The pipeline extracts, transforms, and loads (ETL) data into Amazon Redshift using AWS Glue, uses Amazon Step Functions to orchestrate the process, EventBridge to track creation of new data and builds interactive dashboards using Microsoft Power BI.

## 📌 Project Overview

The goal of this project is to analyze domestic airline flight patterns to derive insights such as:

- Busiest flight routes
- Flight delay comparisons based on Flight carriers
- Busiest airports
- Least punctual airports

---

## Architecture:
![architecture](https://github.com/dipanjan51/data_ingestion_project/blob/main/architecture.jpeg?raw=true)


## Glue ETL flow:
![architecture](https://github.com/dipanjan51/data_ingestion_project/blob/main/Glue%20Pipeline.png?raw=true)

## Step Functions Execution:
![architecture](https://github.com/dipanjan51/data_ingestion_project/blob/main/orchestration%20outcome.png?raw=true)

## Visualisation:
https://app.powerbi.com/view?r=eyJrIjoiYjE3NTVkOGMtMDJmZi00MmY4LTkzNTYtOWZhZmNhYjQ4YTQ5IiwidCI6IjMyNWI1NDE5LTM2NmUtNGUxZS1hZTAyLWNjNWIzZDk1ZDk5MiJ9


