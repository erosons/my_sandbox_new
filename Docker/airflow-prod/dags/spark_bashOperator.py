from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'samson',
    'start_date': datetime(2020, 11, 18),
    'retries': 10,
	'retry_delay': timedelta(hours=1)
}
with DAG('Spark_test_with_Bash_operator',
                  default_args=default_args,
                  schedule_interval='0 1 * * *'
                  
            ) as dag:


    starttime=datetime.now()

    task_elt_spark_with_bash = BashOperator(
        task_id='elt_bash_with_spark',
        bash_command="python ./dags/sparkjob.py",
    )
    
    endtime=datetime.now()

    print(endtime-starttime)

    task_elt_spark_with_bash 

#Caveat
"""
This operator you will have more log details from Spark job.

"""