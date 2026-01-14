# 🌦️ OpenWeather ETL Pipeline using Apache Airflow 🚀

![Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?logo=apacheairflow&logoColor=white)
![Postgres](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)

---

## 📌 Overview
This project is a **production-style Data Engineering ETL pipeline** built using **Apache Airflow**.  
It extracts real-time weather data from the **OpenWeather API**, transforms it, and loads it into **PostgreSQL** while preserving historical data using **Slowly Changing Dimension (SCD Type 2)**.

The project demonstrates real-world data engineering concepts such as orchestration, API ingestion, data transformation, and historical tracking.


---

## 🏗️ Architecture

<img width="911" height="493" alt="image" src="https://github.com/user-attachments/assets/76f5ecc1-40fb-4e4e-83cc-9d15fe38b742" />

---

## 🛠️ Tech Stack
- 🐍 Python  
- 🌀 Apache Airflow  
- 🐘 PostgreSQL  
- ☁️ OpenWeather API  
- 🐳 Docker  

---

## ✨ Key Features
- ⏱️ Automated data ingestion (runs every minute)
- 🌐 Real-time API integration
- 🧹 Data transformation & normalization
- 🕰️ Historical data tracking using **SCD Type 2**
- 🗃️ PostgreSQL as analytical storage
- 📊 Query-ready data model

---

## 🗃️ Database Design (SCD Type 2)

```sql
CREATE TABLE weather_data_scd (
    id SERIAL PRIMARY KEY,
    city TEXT,
    country TEXT,
    temperature_c FLOAT,
    humidity INT,
    pressure INT,
    wind_speed FLOAT,
    weather_description TEXT,
    valid_from TIMESTAMP,
    valid_to TIMESTAMP,
    is_current BOOLEAN
);
```
---
🧪 Sample SQL Queries
```
SELECT *
FROM weather_data_scd
WHERE is_current = true;
```
---
📁 Project Structure
```
openweather-airflow-etl/
│
├── dags/
│   └── openweather_etl_scd_dag.py
│
├── sql/
│   └── create_weather_table.sql
│
├── requirements.txt
└── README.md
```
---
## 🚀 How to Run

1. Set up **Apache Airflow**
2. Configure **PostgreSQL**
3. Add your **OpenWeather API Key**
4. Trigger the DAG from the **Airflow UI**
5. Query PostgreSQL to explore the data

---
## 🔐 Security Notes

- 🔑 API keys and credentials are **NOT committed**
- 🛡️ Sensitive files are excluded using `.gitignore`


---
## 🎯 What This Project Demonstrates

- Building real-world ETL pipelines
- Workflow orchestration with Apache Airflow
- Handling external APIs
- Data modeling using **SCD Type 2**
- Production-ready data engineering mindset

---
## 👤 Author

**Ziad Ashraf**  
Data Engineer | Software Instructor at iSchool  

🔗 GitHub: https://github.com/ZiadAshraf85  
🔗 LinkedIn: https://www.linkedin.com/in/ziad-ashraf-34391824b

---
## 📚 Useful Resources

- Apache Airflow Docs: https://airflow.apache.org/docs/
- OpenWeather API Docs: https://openweathermap.org/api
- PostgreSQL Docs: https://www.postgresql.org/docs/
- SCD Type 2 Explained: https://www.sqlshack.com/slowly-changing-dimensions-type-2/

---

