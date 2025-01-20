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
    dag_id="Xcom_Operations_Multiple_values",
    schedule_interval=timedelta(1),
    tags=["Pulling  multiple data from a function return and using it *args in another function"],
    default_args=args,
    catchup=False,
) as dag:

  
    # push multiple xcom values
    def greet_name(ti):
        ti.xcom_push(key="first_Name",value='Samson')
        ti.xcom_push(key="last_Name",value='Eromonsei')


    # calling multiple xcom values
    def greetings(age,ti):
        firstname=ti.xcom_pull(task_ids="Name_extractor_task",key="first_Name")
        lastname=ti.xcom_pull(task_ids="Name_extractor_task",key="last_Name")
        return "My Name is {} {} and I am {}".format(firstname,lastname,age)



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