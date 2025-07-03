from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
import os
from amperon.s3_loader import s3_file_upload
from MP2360Tools.MP2360Tools.database.dremio import Dremio
from airflow.models.dag import DAG
from airflow.utils.dates import days_ago
from MP2360Tools.MP2360Tools.utils import logz
import pandas as pd
from airflow.models import Variable
from MP2360Tools.observability.msteamCallback import success_callback, failure_callback


logger = logz.create_logger()
today = datetime.utcnow()
dateRef = today.strftime('%Y%m%d')
dremio = Dremio(host="dremio-internal.prod.ep.my360",
                user=Variable.get("UID"), password=Variable.get("PWD"))
key = 'pulsePower_uat/' + 'pulsePowerbak' + dateRef
bucketpath = 'prod-smt-data-cache'
path = '/tmp/'

args = {
    "owner": "Plymell Philip, Samson",
    "retries": 3,
    "retry_delay": timedelta(minutes=10),
    "owner": "Samson",
    'on_failure_callback': failure_callback
}


with DAG(
    dag_id="puslePower_bakUP",
    schedule_interval="* 06 * * *",
    start_date=datetime(2023, 3, 3),
    tags=["Loading customer Obligation bakup file"],
    default_args=args,
    catchup=False,

) as dag:

    sqlB = """
            SELECT * FROM "Mp2-Reporting"."Customer Obligation List".finalOutput.b2c.ercot."customerObligationList_pulsePower_uat"
           """

    def readDremio_WriteS3():

        # reads from dremio and extract date field from the file written to the local file
        # Parameters
        # - params container_name (str) – The name of the container
        # - Params prefix (str | None) – Filters the results to return only blobs whose names begin with the specified prefix

        try:
            dfB = dremio.to_pandas(sql=sqlB)
            dfB['Effective_Date'] = dateRef
            print(dfB.head(5))
            file_path = '/tmp/puslePowerbak' + dateRef + '.parquet'
            dfB.to_parquet(file_path, index=False)
            s3_file_upload(file_name, Bucket, key)
            for i in os.listdir(path):
                os.remove(file_name)
            return print("Upload was successful")
        except:
            return logger.error("File read and upload not successful")

    # Task execution and flow

    dremios3API = PythonOperator(
        task_id="dremioRead_s3Load",
        python_callable=readDremio_WriteS3,
        dag=dag,
    )


dremios3API
