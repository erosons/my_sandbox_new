import pyodbc
import pandas as pd
import boto3
from botocore.exceptions import ClientError
import logging


sql = """SELECT * FROM "Mp2-Reporting"."Customer List"."odin_Customer_list_extract"."unpivot passthrough" """

local_filename = "passthrough_pivot.csv"

s3_file = local_filename

logging.basicConfig(filename='new.log', filemode='w', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

bucketName = "prod-smt-data-cache"


def conn_util():
    try:
        host = ""
        port = "'31010'"
        uid = ""
        pwd = ""
        driver = '/Library/Dremio/ODBC/lib/libdrillodbc_sbu.dylib'
        cnxn = pyodbc.connect("Driver={};ConnectionType=Direct;HOST={};PORT={};AuthenticationType=Plain;UID={};PWD={}".format(
            driver, host, port, uid, pwd), autocommit=True)

        return cnxn

    except:
        logging.debug("check connection variable")


def pivotCaller():
    try:
        data = pd.read_sql(sql, conn_util())
        data['values'] = 1
        data = data.pivot(index='id', columns='Passthroughs', values='values')
        data = data.fillna(0)
        data.to_csv(local_filename, index=False)
        return logging.info("file extract was successful")

    except ValueError as v:

        logging.debug("Index contains duplicate entries, cannot reshap", v)


def s3connection():
    try:
        s3 = boto3.client('s3', aws_access_key_id=""
                          aws_secret_access_key="")
        logging.info('connection was succesful'.format(s3))
        return s3
    except:
        logging.debug('Chk acces_key_id , aws_secet_access_key are valid')


s3connection = s3connection()


def upload_file(file_name, bucket_name, object_Name):
    # s3_connection.upload_file(local_filename,bucket,s3_file)
    # if object_Name is None:
    # object_Name = s3_file
    try:
        response = s3connection.upload_file(
            file_name, bucket_name, object_Name)
    except ClientError as e:
        logging.error(e)
        return print("Failed connection and upload")
    return print("Upload successful", response)


if __name__ == '__main__':
    conn_util()
    pivotCaller()
    upload_file(s3_file, bucketName, 'object_Name')
