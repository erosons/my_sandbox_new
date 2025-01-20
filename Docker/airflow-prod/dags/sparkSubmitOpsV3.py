from airflow import DAG
from datetime import datetime, timedelta
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator
from dag_slackAlert import task_fail_slack_alert



default_args = {
    'owner': 'samson',
    'start_date': datetime.today(),
    'retries':2,
	'retry_delay': timedelta(hours=1),
    'on_failure_callback': task_fail_slack_alert
}
with DAG('ETL_sparkSubmitOperatorV3',
                  default_args=default_args,
                  schedule_interval='@daily',
                  tags=["SparkSubmitTutorial"],
                  catchup=False
                  
                ) as dag:

    # spark = SparkSession(SparkContext(conf=SparkConf()).getOrCreate()) 

    SparkSubmitOps= SparkSubmitOperator(
        task_id='sparkSubmitOps',
        conn_id='Sparkconn',
        application="/opt/airflow/dags/pyspark_csv_read.py",
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


    
    

