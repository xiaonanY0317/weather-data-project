from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator
import sys
sys.path.append('/opt/airflow/weather-data-project')

from api_request.api_request import fetch_data
from api_request.data_transform import clean_weather_data
from api_request.data_load import upload_to_s3

default_args = {
    'description': 'Weather Data Orchestrator',
    'start_date': datetime(2025,7, 21),
    'catchup': False,
}

dag = DAG(
    dag_id='weather_data_orchestrator',
    default_args=default_args,
    schedule=timedelta(minutes=5),
)

with dag:
    task_1 = PythonOperator(
        task_id='fetch_weather_data',
        python_callable=fetch_data)
    
    task_2 = PythonOperator(
        task_id = 'transform_weather_data',
        python_callable=clean_weather_data)
    

    task_3 = PythonOperator(
        task_id='upload_weather_data_to_s3',
        python_callable=upload_to_s3)
    
task_1 >> task_2 >> task_3