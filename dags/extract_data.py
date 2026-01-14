import requests
import pandas as pd
import psycopg2
from airflow.decorators import dag, task
from pendulum import datetime


@dag(
    dag_id="openweather_etl_scd_dag",
    start_date=datetime(2026, 1, 5),
    schedule="*/1 * * * *",        
    catchup=False,
    max_active_runs=1,
    default_args={"retries": 0}
)
def openweather_etl():

    # --------------------
    # 1️⃣ Extract
    # --------------------
    @task
    def fetch_data_from_api() -> dict:
        api_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": "Cairo",
            "appid": "b10a50868f1c110e6190544caa5a4628",  
            "units": "metric"
        }

        response = requests.get(api_url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    # --------------------
    # 2️⃣ Transform
    # --------------------
    @task
    def transform_data(raw_data: dict) -> dict:
        return {
            "city": raw_data["name"],
            "country": raw_data["sys"]["country"],
            "temperature_c": raw_data["main"]["temp"],
            "humidity": raw_data["main"]["humidity"],
            "pressure": raw_data["main"]["pressure"],
            "wind_speed": raw_data["wind"]["speed"],
            "weather_description": raw_data["weather"][0]["description"],
            "timestamp": pd.Timestamp.now().isoformat()
        }

    # --------------------
    # 3️⃣ Load (SCD Type 2)
    # --------------------
    @task
    def load_data(data: dict):
        conn = psycopg2.connect(
            host="postgres",
            database="WeatherDB",
            user="airflow",
            password="airflow"
        )
        cur = conn.cursor()

        # Close previous current record
        cur.execute("""
            UPDATE weather_data_scd
            SET valid_to = NOW(), is_current = false
            WHERE city = %s AND is_current = true
        """, (data["city"],))

        # Insert new record
        cur.execute("""
            INSERT INTO weather_data_scd (
                city, country, temperature_c, humidity,
                pressure, wind_speed, weather_description,
                valid_from, valid_to, is_current
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,NOW(),NULL,true)
        """, (
            data["city"],
            data["country"],
            data["temperature_c"],
            data["humidity"],
            data["pressure"],
            data["wind_speed"],
            data["weather_description"]
        ))

        conn.commit()
        cur.close()
        conn.close()

    # --------------------
    # Pipeline
    # --------------------
    raw = fetch_data_from_api()
    clean = transform_data(raw)
    load_data(clean)


openweather_etl()
