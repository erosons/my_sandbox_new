# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""Example DAG demonstrating the usage of the PythonOperator."""
from asyncio import tasks
from datetime import datetime, timedelta
from airflow import DAG
import logging
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago


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


with DAG(
    dag_id="Xcom_Operations",
    schedule_interval=timedelta(1),
    tags=["Pulling data from function return and using it as args for another function"],
    default_args=args,
    catchup=False,
) as dag:

  

    def greet_name():
        
        return "Samson"

    
    def greetings(age,ti):
        name=ti.xcom_pull(task_ids="Name_extractor_task")
        return "My Name is {} and I am {}".format(name,age)



    greetname = PythonOperator(
        task_id="Name_extractor_task",
        python_callable=greet_name,
        dag=dag,
    )

    greeting= PythonOperator(
        task_id="greetings_task",
        python_callable=greetings,
        op_kwargs={"age":42},
        dag=dag,
    )

    

    greetname >> greeting