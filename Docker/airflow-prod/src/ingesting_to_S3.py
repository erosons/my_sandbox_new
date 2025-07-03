import logging
import boto3
from botocore.retries import bucket
import configparser
from botocore.exceptions import ClientError
from extract_mysql_full import local_filename



"""
loading the aws_boto credentials values for S3 uplaod
"""

parser = configparser.ConfigParser()
parser.read("pipeline.conf")
access_keys = parser.get("aws_boto_credentials", "access_keys")
secret_key = parser.get("aws_boto_credentials", "secret_key")
bucket_name = parser.get("aws_boto_credentials", "bucket_name")



logging.basicConfig(filename='new.log', filemode='w', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def s3connection():
    s3 = boto3.client('s3', aws_access_key_id=access_keys,
                      aws_secret_access_key=secret_key)
    return s3


s3_connection = s3connection()
logging.info('connection {} was succesful'.format(s3_connection))

#File to be loaded
s3_file = local_filename


def upload_file(file_name, bucket_name, object_Name):
    # s3_connection.upload_file(local_filename,bucket,s3_file)
    # if object_Name is None:
    #object_Name = s3_file

    try:
        response = s3_connection.upload_file(
            file_name, bucket_name, object_Name)
        logging.info("File uploaded into {} successfully".format(bucket_name))
        return response
    except ClientError as e:
        logging.error(e)
        return print("Failed connection and upload")

if __name__=='__main__':
    upload_file(s3_file , bucket_name, 'Order_extract.csv')
