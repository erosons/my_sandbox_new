from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import pyodbc
import pandas as pd
import boto3
import os
from botocore.exceptions import ClientError
import logging


args = {
    "owner": "Samson",
    "start_date": days_ago(1),
    "retries": 3,
    "owner": "Samson",
}


with DAG(
    dag_id="Dremio_S3",
    schedule_interval="@daily",
    tags=["S3Ingestion_fromDremio"],
    default_args=args,
    catchup=False,
) as dag:

    sql = """SELECT * FROM "Mp2-Reporting"."Customer List"."odin_Customer_list_extract"."unpivot passthrough" """

    local_filename = "passthrough_pivot.csv"

    s3_file = local_filename

    bucketName = "prod-smt-data-cache"

    logging.basicConfig(
        filename="new.log",
        filemode="w",
        level=logging.DEBUG,
        format="%(asctime)s:%(levelname)s:%(message)s",
    )

    def conn_util():
        try:
            host = os.getenv("url",None)
            port = "31010"
            uid = os.getenv("username",None)
            pwd = os.getenv("pwd",None)
            driver = "/opt/dremio-odbc/lib64/libdrillodbc_sb64.so"
            # driver = "{Dremio Connector}" This is providing map in the odbcinst.ini
            cnxn = pyodbc.connect(
                "Driver={};ConnectionType=Direct;HOST={};PORT={};AuthenticationType=Plain;UID={};PWD={}".format(
                    driver, host, port, uid, pwd
                ),
                autocommit=True,
            )
            logging.debug("Connection to dremio was Successful")
            return cnxn

        except:
            logging.debug("check connection variable")

    dremioCaller = conn_util()

    """
    Extraction of passthrough data from dremio and parsing to pivot
    """

    def pivotCaller(sqlcommand, cxn):
        try:
            data = pd.read_sql(sqlcommand, cxn)
            data["values"] = 1
            data = data.pivot(index="id", columns="Passthroughs", values="values")
            data = data.fillna(0)
            data.to_csv(local_filename, index=True)
            return logging.info("csv file extract was successful")

        except ValueError as v:
            logging.debug("Index contains duplicate entries, cannot reshape", v)

    """
    Connection to the s3 bucket
    """

    def s3connection():
        try:
            s3 = boto3.client(
                "s3",
                aws_access_key_id="",
                aws_secret_access_key="",
                region_name="us-east-2",
            )
            logging.info("S3 connection was succesfully established".format(s3))
            return s3
        except:
            logging.debug("Chk acces_key_id , aws_secet_access_key are valid")

    s3connection = s3connection()

    """
    File upload into S3 bucket
    """

    def upload_file(file_name, bucket_name, object_Name):
        # s3_connection.upload_file(local_filename,bucket,s3_file)
        # if object_Name is None:
        # object_Name = s3_file
        try:
            s3connection.upload_file(file_name, bucket_name, object_Name)
        except ClientError as e:
            logging.error(e)
            return print("Failed connection and upload")
        return print("Upload successful")

    """
    Task Execution 
    """

    dremio_extract_pivotting = PythonOperator(
        task_id="dremio_extract_pivotting",
        python_callable=pivotCaller,
        op_kwargs={"sqlcommand": sql, "cxn": dremioCaller},
        dag=dag,
    )

    S3_ingestion = PythonOperator(
        task_id="Uploading_file_s3",
        python_callable=upload_file,
        op_kwargs={
            "fileName": local_filename,
            "bucketName": bucketName,
            "Object": local_filename,
        },
        dag=dag,
    )

    dremio_extract_pivotting >> S3_ingestion
