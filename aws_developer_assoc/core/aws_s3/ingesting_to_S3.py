import logging
import boto3
from botocore.retries import bucket
import csv
import configparser
from botocore.exceptions import ClientError
from core.mySQL_extract.extract_mysql_full import local_filename
from unittest.mock import patch, MagicMock


"""
loading the aws_boto credentials values for S3 uplaod
"""

parser = configparser.ConfigParser()
parser.read("pipeline.conf")
access_keys = parser.get("aws_boto_credentials", "access_keys")
secret_key = parser.get("aws_boto_credentials", "secret_key")
bucket_name = parser.get("aws_boto_credentials", "bucket_name")


def s3connection():
    s3 = boto3.client('s3', aws_access_key_id=access_keys,
                      aws_secret_access_key=secret_key)
    return s3


s3_connection = s3connection()

s3_file = local_filename


def upload_file(file_name, bucket_name, object_Name):
 
    s3_connection = boto3.client('s3', aws_access_key_id=access_keys,
                                 aws_secret_access_key=secret_key)

    print(f'connection {s3_connection} was succesful')

    try:
        response = s3_connection.upload_file(file_name, bucket_name, object_Name)
    except ClientError as e:
        logging.error(e)
        return print("Failed connection and upload")
    return print("Upload successful")
