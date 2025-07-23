import pandas as pd
from pathlib import Path

def clean_weather_data(**kwargs):
    raw_data = kwargs['ti'].xcom_pull(key='raw_data', task_ids='fetch_weather_data')
    df = pd.json_normalize(raw_data, sep="_")
    output_dir = "/opt/airflow/data"
    Path(output_dir).mkdir(parents=True, exist_ok=True) 
    csv_path = f"{output_dir}/weather_data.csv"
    df.to_csv(csv_path, index=False)
    kwargs['ti'].xcom_push(key='csv_path', value=csv_path)

