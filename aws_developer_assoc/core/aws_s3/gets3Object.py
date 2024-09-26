import boto3
import configparser
import logging
from botocore.exceptions import ClientError
import json


"""
loading the aws_boto credentials values for S3 uplaod
"""

parser = configparser.ConfigParser()
parser.read("pipeline.conf")
access_keys = parser.get("aws_boto_credentials", "access_keys")
secret_key = parser.get("aws_boto_credentials", "secret_key")
bucket_name = parser.get("aws_boto_credentials", "bucket_name")


def gets3Object():
    s3 = boto3.client('s3', aws_access_key_id=access_keys,
                      aws_secret_access_key=secret_key)
    try:
        # getting file from s3 by hardcoding the the key=> the file we are interested in
        response = s3.get_object(Bucket=bucket_name, Key='bin_log.csv')

        # fetch  and see file details from s3
        process_res = json.dumps(
            response, indent=4, sort_keys=True, default=str)
        print(process_res)

    except ClientError as e:
        logging.error(e)
        return print("Failed connection and upload")
    return print("Upload successful")


if __name__ == "__main__":
    gets3Object()
