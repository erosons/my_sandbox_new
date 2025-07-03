import logging
import boto3
import json
from botocore.retries import bucket
import configparser
from botocore.exceptions import ClientError
from pprint import pprint

parser = configparser.ConfigParser()
parser.read("pipeline.conf")
access_keys = parser.get("aws_boto_credentials", "access_keys")
secret_key = parser.get("aws_boto_credentials", "secret_key")
bucket_name = parser.get("aws_boto_credentials", "bucket_name")


logging.basicConfig(filename='new.log', filemode='w', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def dynamodb():
    logging.info("Setting up DynamoDB connection")
    aws_dynamo = boto3.client('dynamodb', aws_access_key_id=access_keys,
                              aws_secret_access_key=secret_key, region_name="")

    return aws_dynamo


dynamoConn = dynamodb()


def get_item(conn: str, TableName) -> str:
    try:
        response = conn.get_item(
            Key={
                'Product ID': {
                    'S': 'FUR-BO-10001798',
                },
                'Sales': {
                    'N': '261.96',
                }
            },
            ReturnConsumedCapacity='TOTAL',
            TableName=TableName,
        )

        pprint(response)
    except conn.exceptions.ConditionalCheckFailedException:
        logging.debug('ConditionalcheckFailException')


if __name__ == '__main__':
    get_item(dynamoConn, "Sales")
