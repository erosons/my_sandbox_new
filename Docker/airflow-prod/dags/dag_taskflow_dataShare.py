

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
    level=logging.INFO,
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
    dag_id="taskflow_API_multiple_return_feeds",
    schedule_interval=timedelta(1),
    tags=["Pulling data from function return and using it as args for another function"],
    default_args=args,
    catchup=False)


def greeting_etl_Operations():
        
        @task(multiple_outputs=True)
        def greet():
           return {
            "firstname":"Samson",
            "lastname":"Eromonsei"      
           }

        @task
        def age():
           return 20

        @task
        def greetings(age,firstname,lastname):
    
            return "My Name is {} {} and I am {}".format(firstname,lastname,age)

        name_dict=greet()
        age=age()
        greetings=greetings(firstname=name_dict["firstname"],lastname=name_dict["lastname"],age=age)

    
greet_dag=greeting_etl_Operations()
