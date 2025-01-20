from datetime import datetime, timedelta
from airflow.decorators import dag, task
import sFTP_hook_connection

# [START dag_decorator_usage]
@dag(
    schedule_interval="01 11 * * *",
    start_date=datetime(2021, 1, 2),
    catchup=False,
    default_args={
        'description': 'Simple dag to execute amperon truncate and load in etl_db'
     },
    tags=["amperon"],
)

def sftpConn_dag():

   conn=sFTP_hook_connection.sftp_conn()
   @task
   def VerifyCon():
      conn.list_directory(f'/dremio-exelergy-sftp/pre/site-mp2/CAISO-LMP-EXTRACT/')
   
   @task
   def Tree():
      conn.get_tree_map(f'/dremio-exelergy-sftp/pre/site-mp2/CAISO-LMP-EXTRACT/DEV/Pick-up/')
   
   @task
   def put():
      conn.store_file(f'/dremio-exelergy-sftp/pre/site-mp2/CAISO-LMP-EXTRACT/DEV/Pick-up/test2.txt',f'/tmp/test2.txt', confirm=True)

   VerifyCon() >> Tree()>>put()

dag=sftpConn_dag()