from airflow.providers.sftp.hooks.sftp import SFTPHook


def sftp_conn():
   conn=SFTPHook(ssh_conn_id = "Stfp_conn")
   return conn

