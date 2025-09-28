
import boto3
from botocore.exceptions import ClientError

import logging

# s3_client = boto3.client('s3')

# s3_object_list =s3_client.list_objects(Bucket='acm-test-bucket')

# print(s3_object_list['Contents'][0])


def s3_write(
    aws_access_key=None,
    aws_secret_access_key=None,
    bucket_name=None,
    file_name=None,
    full_file_path=None,
    storage_class=None,
):
    try:
        aws_seesion = boto3.session.Session()
        s3 = aws_seesion.client("s3")
        res = s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=full_file_path
  )
        return res
    except ClientError as e:
        logging.error(e)
        return print("Failed connection and upload")