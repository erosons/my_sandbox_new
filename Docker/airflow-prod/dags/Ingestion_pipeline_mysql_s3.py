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
from sqlalchemy import create_engine
import configparser
import pandas as pd


# defining configuration parameters
parser = configparser.ConfigParser()
parser.read("/home/samson/my_sandbox/Engineering/DataEngineering/airflow/src/pipeline.conf")
hostname = parser.get("mysql_config", "hostname")
port = parser.get("mysql_config", "port")
username = parser.get("mysql_config", "username")
dbname = parser.get("mysql_config", "database")
password = parser.get("mysql_config", "password")


logging.basicConfig(
    filename="new.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
)

# cxn = pymysql.connect(
#     host=hostname, user=username, password=password, db=dbname, port=int(port)
# )

#Alternatively to Setup Connection using SqlAlchemy, pip install SQLAlchemy

pymysql.install_as_MySQLdb()



conn = create_engine("mysql://root:airflow@localhost:33306/test")

# with engine.begin() as conn:
#     result = conn.execute("SELECT * FROM test.Customers;")
#     for rows in result:
#         print(rows)



args = {
    "owner": "Samson",
    "start_date": days_ago(1),
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
    "owner": "Samson",
    "email": "test@gmail.com,
    "email_on_failure": True,
    "email_on retry": True,
}


with DAG(
    dag_id="ELT2_Ingestion",
    schedule_interval=timedelta(1),
    tags=["Mysql_Ingestion"],
    default_args=args,
    catchup=False,
) as dag:

    sqlcommand = "SELECT * FROM test.Customers;"

    query = str(sqlcommand)
    local_filename = "order_extract.csv"


    def extract_data(contn):
        df = pd.read_sql(query, contn)
        df.to_csv(local_filename, index=False, header=None)



    extract_orders_task = PythonOperator(
        task_id="extract_order_from_mysql",
        python_callable=extract_data,
        op_kwargs={"contn": conn},
        dag=dag,
    )

    test_bash = BashOperator(
        task_id="Ingestion_to_S3",
        bash_command="echo Operation was successful",
        dag=dag,
    )

    email_task = EmailOperator(
        task_id="send_email",
        to="test@gmail.com,
        subject="Airflow Alert",
        html_content=""" <h3> Email for test airflow </h3> """,
    )
    # Dependency definition v1 
        # extract_orders_task >> test_bash 
        # extract_orders_task >> email_task

    # Dependency definition v2 
       # extract_orders_task >> [test_bash ,email_task]

    # Dependency definition v3 
    extract_orders_task.set_downstream(test_bash)
    extract_orders_task.set_downstream(email_task)
