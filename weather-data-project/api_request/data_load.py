import boto3
import os
from dotenv import load_dotenv

def upload_to_s3(**kwargs):
    load_dotenv()
    csv_path = kwargs['ti'].xcom_pull(key='csv_path', task_ids='transform_weather_data')
    bucket_name = "xiaonan-airflow-test"
    object_name = os.path.basename(csv_path)

    s3 = boto3.client("s3")
    try:
        s3.upload_file(csv_path, bucket_name, object_name)
        print(f"Uploaded to s3://{bucket_name}/{object_name}")
    except Exception as e:
        print(f"Upload failed: {e}")