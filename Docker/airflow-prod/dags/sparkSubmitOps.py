import airflow
from datetime import datetime, timedelta
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator



default_args = {
    'owner': 'samson',
    'start_date': datetime(2022, 8, 20),
    'retries':2,
	'retry_delay': timedelta(hours=1),
}
with airflow.DAG('ETL_sparkSubmitOperatorV1',
                  default_args=default_args,
                  schedule_interval='@daily',
                  tags=["SparkSubmitTest"],
                  catchup=False
                  
                ) as dag:

    # spark = SparkSession(SparkContext(conf=SparkConf()).getOrCreate()) 

    SparkSubmitOps= SparkSubmitOperator(
        task_id='sparkSubmitOps',
        conn_id='spark_sumbit',
        application="/home/samson/my_sandbox/Engineering/DataEngineering/airflow/src/spark-sumbit.py",
        total_executor_cores=3,
        executor_memory="2G",
        executor_cores=1,
        driver_memory="2G",
        num_executors=6,
        #spark_binary="$SPARK_HOME/bin/pyspark",
        env_vars=None,
        dag=dag
    )

    SparkSubmitOps


    
    

