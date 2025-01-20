from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime
from kafka import KafkaProducer
import json

# Function to push event telemetry when DAG starts
def push_telemetry_to_kafka(context):
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    dag_run = context['dag_run']
    telemetry_event = {
        "event": "dag_started",
        "dag_id": dag_run.dag_id,
        "execution_date": str(dag_run.execution_date),
        "start_date": str(dag_run.start_date),
        "run_id": dag_run.run_id
    }
    producer.send('ns_subscription_topic', telemetry_event)
    producer.flush()

# Define your DAG
default_args = {
    'on_start_callback': push_telemetry_to_kafka
}

with DAG('example_telemetry_dag',
         default_args=default_args,
         schedule_interval='@daily',
         start_date=datetime(2023, 1, 1),
         catchup=False) as dag:

    start_task = DummyOperator(task_id='start')
    end_task = DummyOperator(task_id='end')

    start_task >> end_task
