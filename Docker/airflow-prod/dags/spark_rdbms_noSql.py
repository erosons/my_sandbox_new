import airflow
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from pyspark.sql import SparkSession, functions


def processo_etl_spark():
    spark = SparkSession \
        .builder \
        .appName("myApp") \
        .config("spark.mongodb.input.uri", "mongodb://mongodb:27017/ETL.test") \
        .config("spark.mongodb.output.uri", "mongodb://mongodb:27017/ETL.test") \
        .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.11:2.4.1")\
        .getOrCreate()

    spark.read \
        .format("com.mongodb.spark.sql.DefaultSource")\
        .option("uri", "mongodb://mongodb:27017/ETL.test") \
        .load()


    # writing to a Nosql-mongo
    df=  spark.write.format("com.mongodb.spark.sql.DefaultSource") \
        .mode("overwrite/append") \
        .option("database", "amperon") \
        .option("collection", "superOder") \
        .save()


default_args = {
    'owner': 'sam',
    'start_date': datetime(2020, 11, 18),
    'retries': 3,
    'retry_delay': timedelta(hours=1)
}
with airflow.DAG('Spark_Session_import_from_airflow_API',
                 default_args=default_args,
                 schedule_interval='0 1 * * *'
                 ) as dag:

    task_elt_airflow_sparkSession_API = PythonOperator(
        task_id='elt_documento_pagar_spark',
        python_callable=processo_etl_spark,
        dag=dag
    )

    task_elt_airflow_sparkSession_API
