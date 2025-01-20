from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow import DAG
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2021, 1, 1),
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
}

dag = DAG(
    'example_spark_operator',
    default_args=default_args,
    description='A simple tutorial DAG to submit Spark job.',
    schedule_interval='0 12 * * *',
    catchup=False,
    tags=["test"]
)

submit_spark_job = SparkSubmitOperator(
    application='/home/app_spark_file_reader.py', # path to your Spark application
    conn_id='spark_default', # connection ID registered in Airflow
    task_id='submit_spark_job',
    dag=dag
)