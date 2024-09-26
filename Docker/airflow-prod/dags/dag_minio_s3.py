"""This helps reduce our line of codes using dag decorators."""
from datetime import datetime, timedelta
from airflow.models.dag import DAG
from airflow.utils.dates import days_ago
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor  
   # Sensor allows you know when file lands in s3 bucket



args = {
    "owner": "Samson",
    "start_date": datetime(2022,8,16),
    "retries": 3,
    "retry_delay": timedelta(minutes=1),
    "owner": "Samson"
}

with DAG(

    dag_id="s3_MinIO",
    schedule_interval="@daily",
    tags=["s3 MinIO"],
    default_args=args,
    catchup=False
    
) as dag:

    s3_MinIO=S3KeySensor(
        task_id="MiniO_s3",
        bucket_key='Superstore.csv',
        bucket_name='airflow',
        aws_conn_id='awsminio_conn'
    )

    s3_MinIO