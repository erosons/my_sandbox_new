from datetime import datetime as dt
from datetime import timedelta as td
import requests
import boto3
from botocore.errorfactory import ClientError
import os
from upload import s3_write


# Read objects from the buckets
def get_prev_file_name(bucket_name, file_prefix, bookmark_file, baseline_file)->str:

    try:
        aws_seesion = boto3.session.Session()
        s3 = aws_seesion.client("s3")
        bookmark_filed = s3.get_object(Bucket=bucket_name, Key=f"{file_prefix}/{bookmark_file}")
        prev_file = bookmark_filed["Body"].read().decode('utf-8')
        return prev_file
    except ClientError as e:
        # if e.response['Error']['Code']=='NoSuckey':
        prev_file = baseline_file
        return prev_file

def get_next_file_name(prev_file_name):
        dt_part = prev_file_name.split(".")[0]
        next_file = f"{dt.strftime(dt.strptime(dt_part, '%Y-%M-%d-%H') + td(hours=1), '%Y-%M-%d-%-H')}.json.gz"
        return next_file
