"""
Setting up sparkcontext in the admin UI page of airflow
  - set conn_id in UI in the admin page :
    Conn_id =spark
    connection Type=Spark
    Host spark://url 
    Port : portNumber

The Spark Session has to be called this way, the below line has to be added to your spark script

=> spark = SparkSession(SparkContext(conf=SparkConf()).getOrCreate()) <=

"""
import airflow
from datetime import datetime, timedelta
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from pyspark.sql import SparkSession, functions




default_args = {
    'owner': 'samson',
    'start_date': datetime(2020, 11, 18),
    'retries': 3,
	'retry_delay': timedelta(hours=1)
}
with airflow.DAG('ETL_sparkSubmitOperatorV2',
                  default_args=default_args,
                  schedule_interval='@daily'
                  
                ) as dag:

    # spark = SparkSession(SparkContext(conf=SparkConf()).getOrCreate()) 

    task_elt_documento_pagar = SparkSubmitOperator(
        task_id='elt_sparkSubmitOperator',
        conn_id='spark',
        application="./dags/sparkjob.py",
        application_args=["{{ds}}","sqlserver://127.0.0.1:1433;databaseName=Teste"],#if you need to send dag data to the airflow job use this property
        total_executor_cores=3,
        executor_memory="30g",
        conf={
            "spark.mongodb.input.uri": "mongodb://127.0.0.1:27017/collection",
            "spark.mongodb.output.uri": "mongodb://127.0.0.1:27017/Colleetion",
            "spark.network.timeout": 10000000,
            "spark.executor.heartbeatInterval": 10000000,
            "spark.storage.blockManagerSlaveTimeoutMs": 10000000,
            "spark.driver.maxResultSize": "20g"
        },
        packages="org.mongodb.spark:mongo-spark-connector_2.12:3.0.0,com.microsoft.sqlserver:mssql-jdbc:8.4.1.jre8"
    )
    
    

