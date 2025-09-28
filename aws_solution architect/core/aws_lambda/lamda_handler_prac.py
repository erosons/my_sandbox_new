import json
import boto3
import urllib
from botocore.retries import bucket
import configparser
import logging
from botocore.exceptions import ClientError
from core.testing import test
import os
import codecs


# Not required on AWS lambda console
parser = configparser.ConfigParser()
parser.read("pipeline.conf")
access_keys = parser.get("aws_boto_credentials", "access_keys")
secret_key = parser.get("aws_boto_credentials", "secret_key")
bucket_name = parser.get("aws_boto_credentials", "bucket_name")


def lambda_handler(event, context):

    # Not required on AWS lambda console
    s3 = boto3.client('s3', aws_access_key_id=access_keys,
                      aws_secret_access_key=secret_key)
    # 1. getting bucket name
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(
        event['Records'][0]['s3']['object']['key'])

    try:
        # getting file from s3 by hardcoding the the key=> the file we are interested in
        response = s3.get_object(Bucket=bucket_name, Key=key)

        # fetch file content details from s3
        text = response['Body'].read().decode('utf-8-sig').replace('\0', '')
        print(text)
        #data = json.loads(text)

        # copying file to another bucket
        try:
            copySource = {'Bucket': bucket_name, 'Key': key}
            response = s3.copy_object(
                CopySource=copySource, Bucket='lambda-ingestion', Key=key)
        except ClientError as s:
            logging.error(s)
            return print("Failed connection and upload")

    except ClientError as e:
        logging.error(e)
        return print("Failed connection and upload")

    return print("Upload successful")


if __name__ == "__main__":
    event = test
    context = ''
    lambda_handler(event, context)
