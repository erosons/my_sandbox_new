

"""This helps reduce our line of codes using dag decorators."""
from asyncio import tasks
from datetime import datetime, timedelta
import logging
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from airflow.decorators import task,dag


logging.basicConfig(
    filename="new.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
)

args = {
    "owner": "Samson",
    "start_date": days_ago(1),
    "retries": 3,
    "retry_delay": timedelta(minutes=1),
    "owner": "Samson",
    "email": "test@gmail.com,
    "email_on_failure": True,
    "email_on retry": True,
}

@dag(
    dag_id="taskflow_API_to_reduce_code_line",
    schedule_interval=timedelta(1),
    tags=["Pulling data from function return and using it as args for another function"],
    default_args=args,
    catchup=False)


def greeting_etl_Operations():
        
        @task
        def greet():
           return "Samson"

        @task
        def age():
           return 20

        @task
        def greetings(age,name):
    
            return "My Name is {} and I am {}".format(name,age)

        name=greet()
        age=age()
        greetings=greetings(age=age,name=name)

    
greet_dag=greeting_etl_Operations()
