from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.sftp.operators.sftp import SFTPOperator
from airflow.providers.sftp.sensors.sftp import SFTPSensor
from dag_slackAlert import task_fail_slack_alert


default_args = {
    'owner': 'samson',
    'start_date': datetime.today(),
    'retries':2,
	'retry_delay': timedelta(minutes=5),
    'on_failure_callback': task_fail_slack_alert
}
with DAG('sFTP_File_write',
                  default_args=default_args,
                  schedule_interval='@daily',
                  tags=["STP ops"],
                  catchup=False
                  
                ) as dag:
    
    wait_for_input_file =SFTPSensor(
        task_id="check-for-file-status",
        sftp_conn_id="Stfp_conn",
        path="/dremio-exelergy-sftp/pre/site-mp2/CAISO-LMP-EXTRACT/DEV/Pick-up/test.text",
        poke_interval=10
    )
    """
    put_file = SFTPOperator(
        task_id="test_sftp",
        ssh_conn_id="Stfp_conn",
        local_filepath="/tmp/file2{{ds}}.txt",
        remote_filepath="/prod-smt-data-cache/stfp/file2{{ds}}.txt",
        operation="put",
        dag=dag
    )

    download_file = SFTPOperator(
        task_id="test_sftp2",
        ssh_conn_id="Stfp_conn",
        local_filepath="/tmp/file3{{ds}}.txt",
        remote_filepath="/prod-smt-data-cache/stfp/file2{{ds}}.txt",
        operation="get",
        dag=dag
    )
    """
    #put_file >> 
    wait_for_input_file
    #>> download_file