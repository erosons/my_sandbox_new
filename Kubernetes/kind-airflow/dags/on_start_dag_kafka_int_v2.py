from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.utils.dates import days_ago
from kafka import KafkaProducer
import json

# Kafka Producer Function (to be used in the on_start callback)
def send_kafka_message(message: str, topic: str, broker: str):
    producer = KafkaProducer(
        bootstrap_servers=broker,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    producer.send(topic, {'message': message})
    producer.flush()
    print(f"Sent message: {message} to topic: {topic}")

# on_start callback function
def on_dag_start(context):
    broker = "localhost:9092"  # Replace with your Kafka broker
    topic = "airflow-tracking"  # Kafka topic name
    message = f"DAG {context['dag'].dag_id} started execution"
    
    # Send the Kafka message when DAG starts
    send_kafka_message(message, topic, broker)

# Define the default_args for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1,
}

# Define the DAG with on_start callback
with DAG(
    'dag_with_kafka_on_start_callback',
    default_args=default_args,
    schedule_interval=None,  # Manual or one-time execution
    catchup=False,
    on_start_callback=on_dag_start,  # Attach the callback here
) as dag:

    # Task 1: Some dummy task for demonstration (KubernetesPodOperator)
    dummy_task = KubernetesPodOperator(
        task_id="dummy_task",
        namespace="airflow",
        image="python:3.8",
        cmds=["bash", "-c"],
        arguments=["echo 'Running dummy task'"],
        name="dummy-task-pod",
        is_delete_operator_pod=True,
        in_cluster=True,
        resources={
            "request_cpu": "500m",
            "request_memory": "1Gi",
            "limit_cpu": "1",
            "limit_memory": "2Gi",
        },
    )
