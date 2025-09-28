import uuid
import boto3
from boto3 import session

s3_client = boto3.client("s3")
"""
the client ouput is a dictionay which requires additional programming to be parse
"""
s3_resources = boto3.resource("s3")
"""
The client resource parse the dictionary layer, without any intervention but sometimes return unreadable output
Calling the client from the resources with meta,This allows you to use client and call any of its function within
resouces as shown below
"""
# s3_resources.meta.client.generate_presigned_url()
"""
The function call below will allow user access to object in S3 bucket for a period of time without AWS access credentials.
"""


def create_bucket_name(bucket_prefix):
    # this function generate a bucket name btw 3 and 63 characters long
    return "".join([bucket_prefix, str(uuid.uuid4())])


def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    # calling the funcion above
    bucket_name = create_bucket_name(bucket_prefix)
    if current_region == "":
        bucket_response = s3_connection.create_bucket(Bucket=bucket_name)
    else:
        bucket_response = s3_connection.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={"LocationConstraint": current_region},
        )
    print(bucket_name, current_region)
    return bucket_name, bucket_response
