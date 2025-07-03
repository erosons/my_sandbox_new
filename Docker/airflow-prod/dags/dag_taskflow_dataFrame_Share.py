

"""This helps reduce our line of codes using dag decorators."""
from asyncio import tasks
from datetime import datetime, timedelta
from pathlib import Path
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from airflow.decorators import task,dag
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
import pandas as pd
from airflow.models import Variable


filepath=Path('/mnt/FILESVR!/TestGoal2022.csv').resolve()
Bucket="prod-smt-data-cache"
key='Test/'
dateRef=datetime.today().strftime('%Y-%m-%d')


args = {
    "owner": "Samson",
    "start_date": days_ago(1),
    "retries": 3,
    "retry_delay": timedelta(minutes=10),
    "owner": " ",
    "on_failure":""
}

filepath=Path('/mnt/FILESVR!/TestGoal2022.csv').resolve()
Bucket="prod-smt-data-cache"
key='Test/'
dateRef=datetime.today().strftime('%Y-%m-%d')

@dag(
    dag_id="taskflow__EOD_Price_Curves",
    schedule_interval=timedelta(1),
    tags=["Pulling data from function return and using it as args for another function"],
    default_args=args,
    catchup=False)




def greeting_etl_Operations():
        
        @task(multiple_outputs=True)
        def file_read_from_drive():
           
           if filepath.exists():
                df=pd.read_csv(filepath,encoded='utf8')
                return {
                  "dataframe":df    
                }
           else:
                raise Exception("File not found")

        @task
        def Transform_data(dataframe):
            
            """Transform your dataframe to something you want to"""

            processeddf=dataframe.head(5)
            processeddf.to_csv(f'/tmp/file{dateRef}.csv',encoded='utf8',index=False)

            return {
            "filepath":f'/tmp/file{dateRef}.csv'    
           }
        
        @task
        def load_to_s3(filepath):
                try:
                    s3_hook = S3Hook(aws_conn_id=S3_CONN_ID)
                    # Save processed data to CSV on S3
                    s3_hook.load_file(
                
                    filename=filepath,
                    bucket_name=Bucket,
                    key=key,
                    replace=True,
                    sncrypt=True
                    )
                    return logger.info("Process successfully")
                except:  
                    return logger.error("Failed to load")
            

        getData=file_read_from_drive()
        Transform_data=Transform_data(dataframe=getData["dataframe"])
        loadData=load_to_s3(processed_data=Transform_data["filepath"])

    
greet_dag=greeting_etl_Operations()
