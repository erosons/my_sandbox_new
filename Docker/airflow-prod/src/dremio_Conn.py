from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
import pyodbc
from botocore.exceptions import ClientError
import logging


args = {
    "owner": "Samson",
    "start_date": days_ago(0),
    "retries": 1,
    "owner": "Samson",
    "email": "test@gmail.com,
    "email_on_failure": True,
    "email_on retry": True,
}


with DAG(
    dag_id="Dremio_Conn",
    schedule_interval="@daily",
    tags=["dremioConn"],
    default_args=args,
    catchup=False,
) as dag:

    def conn_util():
        try:
            host = ""
            port = ""
            uid = ""
            pwsd = ""
            # driver = '/Library/Dremio/ODBC/lib/libdrillodbc_sbu.dylib'
            # OR
            driver = "/opt/dremio-odbc/lib64/libdrillodbc_sb64.so"
            # OR
            # driver = "{Dremio Connector}" This is providing map in the odbcinst.ini
            cnxn = pyodbc.connect(
                "Driver={};ConnectionType=Direct;HOST={};PORT={};AuthenticationType=Plain;UID={};PWD={}".format(
                    driver, host, port, uid, pwsd
                ),
                autocommit=True,
            )
            logging.info(cnxn)
            return cnxn

        except:
            logging.debug("check connection variable")

    dremio_extract_pivotting = PythonOperator(
        task_id="TestdremioConn",
        python_callable=conn_util,
        # op_kwargs={},
        dag=dag,
    )

    test_bash = BashOperator(
        task_id="Testing_Dremio_Connection",
        bash_command="echo Operation was successful",
        dag=dag,
    )

    dremio_extract_pivotting >> test_bash
