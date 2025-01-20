import boto3
from Engineering.aws_developer_assoc.core.aws_s3.S3 import create_bucket

s3_resouce = boto3.resource("s3")

# Create your first bucket with resouce.meta.client
first_bucket_name, first_response = create_bucket(
    bucket_prefix="test", s3_connection=s3_resouce.meta.client
)


# Create your first bucket with resouce.meta.client
second_bucket_name, second_response = create_bucket(
    bucket_prefix="test", s3_connection=s3_resouce
)

print(first_response)
print(second_response)

"""
test881561e6-b7de-4162-83f3-1ed533c59895 ""
testda5c02a8-152f-447a-ae79-b24cba213f06 ""
"""
