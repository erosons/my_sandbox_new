"""This helps reduce our line of codes using dag decorators."""
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago


args = {
    "owner": "Samson",
    "start_date": datetime(2022,8,1),
    "retries": 3,
    "retry_delay": timedelta(minutes=1),
    "owner": "Samson"
}

# We are trying to backfill the missed schedule run which was 2022-08-01
# IF using a container,exec in the container or run directly on CLI
# from cli -> airflow dags backfill -s 2022-08-01 -e 2022-08-16 <dag_id>

with DAG(
    dag_id="backfillOpsV2",
    schedule_interval=timedelta(1),
    tags=["Manual backfilling missing dates"],
    default_args=args,
    catchup=False
) as dag :


    back_filling=BashOperator(
        task_id="backfilling_ops",
        bash_command="echo this is back fillings ops",
        dag=dag,
    )

    back_filling