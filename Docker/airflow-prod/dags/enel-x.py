from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
import pytz
import os
import logging
from airflow.models.dag import DAG
from airflow.utils.dates import days_ago
from airflow.providers.microsoft.azure.hooks.wasb import WasbHook
from azure.storage.file import FileService, ContentSettings
import pandas as pd
import boto3
from botocore.exceptions import ClientError
from azure.storage.blob import BlobServiceClient
from airflow.models import Variable
from glob import glob




logging.basicConfig(filename='new.log', level=logging.DEBUG,
                    format='(name)s:%(asctime)s:%(levelname)s:%(message)s')

args = {
    "owner": "Samson",
    "start_date": days_ago(1),
    "retries": 3,
    "retry_delay": timedelta(minutes=10),
    "owner": "Samson",
}


with DAG(
    dag_id="Casio_Battery_Extract_from_Azure_Ingestion_to_awsbucket",
    schedule_interval=timedelta(1),
    tags=["Load to A2 for CAISO Battery Customers"],
    default_args=args,
    catchup=False,
) as dag:

    container_name = "enelx"
    today = datetime.utcnow()
    yesterday = today - timedelta(days=1)
    dateRef = today.strftime('%Y%m%d')
    print(dateRef)
    thresholdTime = pytz.UTC.localize(yesterday)
    localPath="/tmp/"
    blobConn=WasbHook(wasb_conn_id="AzureBlob",public_read=False)
    bucketpath='prod-ses-product-implementation'
    blob_service_client =  BlobServiceClient.from_connection_string(Variable.get('conn-string'))


    # Creating a reference datetime for used by the files
    date=datetime.now()
    if date.day<10 and date.month >10 :
            todays_date=f'{date.year}{date.month}0{date.day-1}'
    elif date.day<10 and date.month <10:
            todays_date=f'{date.year}0{date.month}0{date.day-1}'
    elif date.day>10 and date.month <10:
            todays_date=f'{date.year}0{date.month}{date.day-1}'
    else:
            print(f'{date.year}{date.month}{date.day-1}')


    class azureConnection:
        def __init__(self) -> None:
            self.account_name="a2tahoeshelldev"
            self.sas_token="sv=2021-04-10&st=2022-09-27T16%3A40%3A38Z&se=2023-10-01T16%3A40%3A00Z&sr=s&sp=rcwdl&sig=m1nWuS2OjgbQdOsWcNOE76Usc0sRCRZbx1qEvRPtDis%3D"
            self.file_service=FileService(account_name=self.account_name, sas_token=self.sas_token)
            self.share_name="adapt2import"
            self.directory=None
        def writeAZ_fileshare(self,fileName,path):
            self.file_service.create_file_from_path(
                share_name=self.share_name,
                directory_name=self.directory,
                file_name=fileName,
                local_file_path=path,
                content_settings=ContentSettings(content_type='text/csv'))


    def conn_test():
     """
     Check azure blob connectivity
     """
     try:
        return print(blobConn.get_conn())        
     except:
        return logging.debug("COnnectivity to the blob storage cnuld not be established")


    
    def s3write(data,Bucket, key):
        try:
            s3_connection=boto3.client('s3', aws_access_key_id=Variable.get("aws_access_key_id"),aws_secret_access_key=Variable.get("aws_secret_access_key"))
            logging.info("Establishing Connectiion to s3 storage")
            s3_connection.upload_fileobj(data,Bucket=Bucket, Key=key)  
            logging.info("Upload successful")
        except ClientError as e:
            logging.error(e)
            return print("Failed connection and upload")
        return print("Upload successful")


    def getbloblist(container_name):
        """Getting Blob based on the date criteria
        Parameters
        - params container_name (str) – The name of the container
        - Params prefix (str | None) – Filters the results to return only blobs whose names begin with the specified prefix
        """
        #Read from Azure blob
        my_container = blob_service_client.get_container_client(container_name)
        my_blobs = my_container.list_blobs(name_starts_with='MeterData/uploads/')
        # Instantiate a BlobServiceClient using a connection string
        for blob in my_blobs:
            if thresholdTime < blob.creation_time:
                print(blob)
                num = blob.name.count('/')
                blobName = blob.name.split('/')[num]
                dateRef = blob.creation_time.strftime('%Y%m%d')
                bytes = my_container.get_blob_client(blob).download_blob().readall()
                download_file_path = os.path.join(localPath + dateRef, blobName)
                print(download_file_path)
                os.makedirs(os.path.dirname(download_file_path), exist_ok=True)
                with open(download_file_path, 'wb') as file:
                    file.write(bytes)
                    file.close()
                    # Write to s3 bucket
                    file_name=download_file_path
                    key='caiso/battery/enel-x/'+ blobName
                    print(key)
                    Bucket= bucketpath
                    try:
                        with open(file_name, 'rb') as data:
                            s3write(data,Bucket,key)
                    except ClientError as e:
                            logging.info(e,"Failed connection and upload")
        return logging.info("Blobs successful")

    def filewrangling():
        """
        reads from dremio and extract date field from the file written to the local file
        """
    
         # write blob to s3
        print('/tmp/{}'.format(todays_date))
        list_of_files = glob(os.path.join('/tmp/{}'.format(todays_date), '*.csv'))
        downloaded_file = max(list_of_files, key=os.path.getctime)
        print(downloaded_file)
        dfS3 = pd.read_csv(downloaded_file)
        print(dfS3.head(5))
        

        #df analysis
        dfS3['startTime_local'] = pd.to_datetime(dfS3['startTime_local'])
        dfS3MinOperatingDate = dfS3['startTime_local'].dt.strftime('%Y-%m-%d').min()
        dfS3MaxOperatingDate = dfS3['startTime_local'].dt.strftime('%Y-%m-%d').max()
        print(dfS3)
        print('Minimum Operating Date: ' + dfS3MinOperatingDate)
        print('Maximum Operating Date: ' + dfS3MaxOperatingDate)

        #read from dremio
        dfAZMinOperatingDate = dfS3['startTime_local'].dt.strftime('%Y%m%d').min()
        dfAZMaxOperatingDate = dfS3['startTime_local'].dt.strftime('%Y%m%d').max() 
        #fileNameB = "CAISO_CRLP_GENMTR_B" + dfAZMinOperatingDate + "-" + dfAZMaxOperatingDate + ".csv"
        fileNameB =str(os.abspath(localPath + "CAISO_CRLP_GENMTR_B" + dfAZMinOperatingDate + "-" + dfAZMaxOperatingDate + ".csv"))
        dfS3.to_csv(fileNameB,index=False)
        #fileNameB_path = os.path.join(fileNameB)
        #os.makedirs(os.path.dirname(fileNameB_path ), exist_ok=True)
        fileNameG = "CAISO_CRLP_GENMTR_G" + dfAZMinOperatingDate + "-" + dfAZMaxOperatingDate + ".csv"
        vdsB = '"Mp2-Reporting".CAISO.integrationScripts."CAISO_CRLP_GENMTR_B"'

        # sqlB=r"select * from " + vdsB + "where OperatingDate between '" + dfS3MinOperatingDate + "' and '" + dfS3MaxOperatingDate + "'"
        # dfB=dremio.to_pandas(sql=sqlB)
        # dfB.to_csv(createpath(fileNameB),index=False)
        # print(dfB)
        #fileNameB_path = os.path.join(fileNameG)
        #os.makedirs(os.path.dirname(fileNameB_path ), exist_ok=True)

        fileNameG = "CAISO_CRLP_GENMTR_G" + dfAZMinOperatingDate + "-" + dfAZMaxOperatingDate + ".csv"

        # vdsG = '"Mp2-Reporting".CAISO.integrationScripts."CAISO_CRLP_GENMTR_G"'
        # sqlG=r"select * from " + vdsG + "where OperatingDate between '" + dfS3MinOperatingDate + "' and '" + dfS3MaxOperatingDate + "'"
        # dfG = dremio.to_pandas(sql=sqlG)
        # dfG.to_csv(createpath(fileNameG),index=False)
        # print(dfG)

        # write to az fileshare 
        azureConnection.writeAZ_fileshare(fileNameB,localPath)
        azureConnection.writeAZ_fileshare(fileNameG,localPath)


    testblobConn= PythonOperator(
        task_id="conn_test",
        python_callable=conn_test,
        dag=dag
        )

    getBlob_writeBlob2_s3= PythonOperator(
        task_id="BlobList",
        python_callable=getbloblist,
        op_kwargs={"container_name":container_name},
        dag=dag
        )

    filewrangle= PythonOperator(
        task_id="filewrangling",
        python_callable=filewrangling,
        dag=dag
        )

    

    testblobConn >> getBlob_writeBlob2_s3 >> filewrangle
