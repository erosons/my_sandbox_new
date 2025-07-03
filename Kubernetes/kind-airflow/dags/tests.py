from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago



args = {
    "owner": "Samson",
    "start_date": days_ago(1),
    "retries": 1,
    'retry_delay': timedelta(hours=1),
    "owner": "Samson",
    "email": "test@gmail.com"
}


with DAG(
    dag_id="Bash_Test",
    schedule_interval=timedelta(1),
    tags=["Mysql_Ingestion"],
    default_args=args,
    catchup=False,
) as dag:

    extract_orders_task = BashOperator(
        task_id="Bash_Ops",
        bash_command="echo this is Operations",
        dag=dag,
    )

    extract_orders_task2 = BashOperator(
        task_id="Bash_Ops1",
        bash_command="echo this is a test",
        dag=dag,
    )

    extract_orders_task >> extract_orders_task2