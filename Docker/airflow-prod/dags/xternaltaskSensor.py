"""This helps reduce our line of codes using dag decorators."""
from datetime import datetime, timedelta
from socket import timeout
from airflow.models.dag import DAG
from airflow.utils.dates import days_ago
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from airflow.operators.bash import BashOperator

args = {
    "owner": "Samson",
    "start_date": datetime(2022,8,16),
    "retries": 3,
    "retry_delay": timedelta(minutes=1),
    "owner": "Samson"
}

with DAG(

    dag_id="ExternaltaskSensor",
    schedule_interval="*,5 * * * *",
    tags=["ExternaltaskSensor"],
    default_args=args,
    catchup=False
    
) as dag:

    ExternalTaskSensorOps=ExternalTaskSensor(
        task_id="externaltaskSensor",
        external_dag_id="s3_MinIO", 
        external_task_id=None,
        mode="reschedule", # using default will lock worker up, and the worker will not get any other task.
        # allowed_states=None,# default is sucess
        execution_delta=timedelta(minutes=5), 
        #execution_date_fn=None, 
        timeout=3600,
        dag=dag,
     )


    BashOps=BashOperator(
        task_id="test_bash_Ops",
        bash_command="echo Hello World",
        dag=dag,
     )

    ExternalTaskSensorOps.set_downstream(BashOps)