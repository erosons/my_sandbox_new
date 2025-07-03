import logging
import boto3
from boto3 import Session
from botocore.retries import bucket
import csv
import configparser
from botocore.exceptions import ClientError
from core.mySQL_extract.extract_mysql_full import local_filename
from unittest.mock import patch, MagicMock
import os


"""
loading the aws_boto credentials values for S3 uplaod
"""

access_keys = os.getenv('aws_access_key_id')
secret_key = os.getenv('aws_secret_access_key')
bucket_name = os.getenv("BUCKET_NAME")


def upload_file(file_name, bucket_name, object_Name):

    s3_connection = boto3.client(
        "s3", aws_access_key_id=access_keys, aws_secret_access_key=secret_key
    )

    print(f"connection {s3_connection} was succesful")

    try:
        response = s3_connection.upload_file(file_name, bucket_name, object_Name)
    except ClientError as e:
        logging.error(e)
        return print("Failed connection and upload")
    return print("Upload successful")


def s3_write(
    aws_access_key,
    aws_secret_access_key,
    bucket_name,
    file_name,
    full_file_path,
    storage_class,
):
    try:
        aws_seesion = boto3.session.Session(
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_access_key,
            region_name="us-east-1",
        )

        s3: Session = aws_seesion.client("s3")
        with open(full_file_path, "rb") as data:
            s3.upload_obj(
                data,
                Bucket=bucket_name,
                key=file_name,
                ExtraArgs={"StorageClass": storage_class},
            )
            logging.info("upload was successful")

    except ClientError as e:
        logging.error(e)
        return print("Failed connection and upload")
