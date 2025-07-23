from api_request.api_request import mock_fetch_data
from api_request.data_transform import clean_weather_data
from dotenv import load_dotenv
import boto3
import os
load_dotenv()
# # print("ACCESS_KEY:", os.getenv("AWS_ACCESS_KEY_ID"))
# print("SECRET_KEY:", os.getenv("AWS_SECRET_ACCESS_KEY"))

# Step 1: Fetch
raw_data = mock_fetch_data()

# Step 2: Transform
df = clean_weather_data(raw_data)
csv_path = "airflow-docker/repos/data/weather_data.csv"
df.to_csv(csv_path, index=False)

# Step 3: Upload to S3
bucket_name = "xiaonan-airflow-test"
object_name = os.path.basename(csv_path)

s3 = boto3.client("s3")
try:
    s3.upload_file(csv_path, bucket_name, object_name)
    print(f"Uploaded to s3://{bucket_name}/{object_name}")
except Exception as e:
    print(f"Upload failed: {e}")