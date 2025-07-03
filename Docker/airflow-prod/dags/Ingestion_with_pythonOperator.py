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
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.operators.email_operator import EmailOperator
import pymysql
import configparser
import pandas as pd


args = {
    "owner": "Samson",
    "start_date": days_ago(1),
    "retries": 1,
    "owner": "Samson",
    "email": "test@gmail.com,
    "email_on_failure": True,
    "email_on retry": True,
}


with DAG(
    dag_id="Bash_to_execute_python_ELT_Ingestion",
    schedule_interval=timedelta(1),
    tags=["Mysql_Ingestion"],
    default_args=args,
    catchup=False,
) as dag:

    extract_orders_task = BashOperator(
        task_id="extract_order_from_mysql",
        bash_command="python  Engineering/DataEngineering/airflow/src/extract_mysql_full.py ",
        dag=dag,
    )

    ingestion_data_task = BashOperator(
        task_id="Ingestion_to_S3",
        bash_command="python /home/samson/my_sandbox/Engineering/DataEngineering/airflow/src/ingesting_to_S3.py ",
        dag=dag,
    )

    email_task = EmailOperator(
        task_id="send_email",
        to="test@gmail.com,
        subject="Airflow Alert",
        html_content=""" <h3> Email for test airflow </h3> """,
    )

    extract_orders_task >> ingestion_data_task >> email_task
