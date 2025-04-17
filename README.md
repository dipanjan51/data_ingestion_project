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
![architecture](https://github.com/dipanjan51/data_ingestion_project/blob/main/images/architecture.jpeg?raw=true)


## Glue ETL flow:
![architecture](https://github.com/dipanjan51/data_ingestion_project/blob/main/images/Glue%20Pipeline.png?raw=true)

## Step Functions Execution:
![stepfunctions](https://github.com/dipanjan51/data_ingestion_project/blob/main/images/orchestration%20outcome.png?raw=true)

---
## Walkthrough:
### 1. Schema and Buckets
As S3 bucket is created with objects to store airports details and fight details separately.
![image](https://github.com/dipanjan51/data_ingestion_project/blob/main/images/buckets.png)

"airlines" schema is created in Redshift, alongwith two tables based on the required structure:
- airports_dim: Dimension table for airport details
- daily_flights_fact: Fact table for storing flight details from source to destination

airports_dim table is populated with the data from airports.csv file since its structured perfectly for dimension table

![image](https://github.com/dipanjan51/data_ingestion_project/blob/main/images/redshift%20schema.png)

### 2. Glue Crawler Config:
Glue Crawlers are configured to automatically extract the schema of the target databases, and to discover and catalog the raw flights data stored in the S3 bucket, thereby creating three Data Catalog tables.

![image](https://github.com/dipanjan51/data_ingestion_project/blob/main/images/crawlers.png)

![image](https://github.com/dipanjan51/data_ingestion_project/blob/main/images/catalog%20tables.png)

### 3. Glue ETL job:
An ETL process is developed using Glue to transform the raw flights data into a structured format.
This includes extracting essential fields like airport carrier, origin airport, destination airport, source and destination city, state, origin delay, and arrival delay.

### 4. Step Functions Orchestration:
The entire workflow is orchestrated using Step Functions which automates the trigger of Crawlers, Glue Job, sending notifications via SNS upon completion of flow.

![image](https://github.com/dipanjan51/data_ingestion_project/blob/main/images/orchestration%20outcome.png)

### 5. Event Bridge trigger rule:
An Event Bridge rule is set which triggers the Step Functions State Machine upon creation of an S3 object.

![image](https://github.com/dipanjan51/data_ingestion_project/blob/main/images/event%20bridge.png)

### 6. Output:
We can check the data in the dimension and fact table which have been populated upon creation of the process:

![image](https://github.com/dipanjan51/data_ingestion_project/blob/main/images/dim%20table.png)
![image](https://github.com/dipanjan51/data_ingestion_project/blob/main/images/facttable.png)

## Visualisation:
https://app.powerbi.com/view?r=eyJrIjoiYjE3NTVkOGMtMDJmZi00MmY4LTkzNTYtOWZhZmNhYjQ4YTQ5IiwidCI6IjMyNWI1NDE5LTM2NmUtNGUxZS1hZTAyLWNjNWIzZDk1ZDk5MiJ9

![image](https://github.com/user-attachments/assets/32df47df-be98-4f1a-a7be-31963ec75653)

