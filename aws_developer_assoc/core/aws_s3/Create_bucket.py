import logging
import boto3
from botocore.retries import bucket
import csv
import configparser
import uuid


"""
loading the aws_boto credentials values for S3 uplaod
"""

parser = configparser.ConfigParser()
parser.read("pipeline.conf")
access_keys = parser.get("aws_boto_credentials", "access_keys")
secret_key = parser.get("aws_boto_credentials", "secret_key")
bucket_name = parser.get("aws_boto_credentials", "bucket_name")


def s3_connection():
    """
    You can use session instead of the connection configuration , I have below, but the script has to be the root level
    Connecting with resources
    """
    s3_conn = boto3.resource('s3', aws_access_key_id=access_keys,
                             aws_secret_access_key=secret_key)
    return s3_conn


def s3_connection1():
    """
    Connecting with client
    """

    s3_conn1 = boto3.client('s3', aws_access_key_id=access_keys,
                            aws_secret_access_key=secret_key)
    return s3_conn1


# List s3 buckets


"""
def bucketlist():
    bucketlist = []
    for bucket in s3_connection().buckets.all():
        bucketlist.append(bucket)
    return bucketlist

"""


def create_bucket_name(bucket_prefix):
    # this function generate unique id for the bucket name btw 3 and 63 characters long
    return "".join([bucket_prefix, str(uuid.uuid4())])


logging.basicConfig(filename='new.log', filemode='w', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def create_bucket(bucket_prefix):
    try:
        Bucket = create_bucket_name(bucket_prefix)
        s3_connection1().create_bucket(Bucket=create_bucket_name(bucket_prefix),
                                       CreateBucketConfiguration={"LocationConstraint": '""'})
        logging.info('Bucket creation was successful')
    except:
        logging.debug('Bucket creation failed check connection or ')

    return print("{} has been  created".format(Bucket))


if __name__ == '__main__':
    print(create_bucket('test_bucket'))
