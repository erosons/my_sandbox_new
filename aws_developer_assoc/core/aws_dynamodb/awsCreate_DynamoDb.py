import logging
import boto3
import json
from pprint import pprint
from botocore.retries import bucket
import configparser
from botocore.exceptions import ClientError


parser = configparser.ConfigParser()
parser.read("pipeline.conf")
access_keys = parser.get("aws_boto_credentials", "access_keys")
secret_key = parser.get("aws_boto_credentials", "secret_key")
bucket_name = parser.get("aws_boto_credentials", "bucket_name")


logging.basicConfig(filename='new.log', filemode='w', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def dynamodb():
    logging.info("Setting up DynamoDB connection")
    aws_dynamodb = boto3.client('dynamodb', aws_access_key_id="",
                                aws_secret_access_key="", region_name="")

    return aws_dynamodb


dynamoConn = dynamodb()


def create_table(conn, tableName):
    try:
        logging.info("Creating the dynamo table")
        response = conn.create_table(
            AttributeDefinitions=[
                {
                    'Product ID': 'string',
                    'AttributeType': 'S'
                },
                {
                    'Sales': 'string',
                    'AttributeType': 'N'
                },
                {
                    'Profit': 'string',
                    'AttributeType': 'N'
                },
                {
                    'Region': 'string',
                    'AttributeType': 'S'
                },
            ],
            TableName=tableName,
            KeySchema=[
                {
                    'Product ID': 'string',
                    'KeyType': 'HASH',
                },
                {
                    'Sales': 'string',
                    'KeyType': 'RANGE'
                }
            ],
            LocalSecondaryIndexes=[
                {
                    'ProductID-profit': 'string',
                    'KeySchema': [
                        # Partition Key
                        {
                            'Product ID': 'string',
                            'KeyType': 'HASH',
                        },
                        # Sort key
                        {
                            'Profit': 'string',
                            'KeyType': 'RANGE'
                        },
                    ],
                    'Projection': {
                        'ProjectionType': 'KEYS_ONLY'
                    }
                },
            ],
            GlobalSecondaryIndexes=[
                {
                    'productName-region': 'string',
                    'KeySchema': [
                        # Partition Key
                        {
                            'Region': 'string',
                            'KeyType': 'HASH'
                        },
                        # Sort key
                        {
                            'Sales': 'string',
                            'KeyType': 'RANGE'
                        }
                    ],
                    'Projection': {
                        'ProjectionType': 'KEYS_ONLY'
                    },
                    'ProvisionedThroughput': {
                        # read capacity equal 1 strong consistence per second  for item up to 4kb in size
                        # 2 eventually consistent reads per seconds per second for an item up to 4kb in size
                        'ReadCapacityUnits': 5,
                        'WriteCapacityUnits': 5
                        # equals 1 write per second for an item up to 1 kb in size
                    }
                },
            ],
            BillingMode='PAY_PER_REQUEST',
            ProvisionedThroughput={
                # If read/write capacity mode is PAY_PER_REQUEST the value is set to 0.
                'ReadCapacityUnits': 0,
                'WriteCapacityUnits': 0
            },
            StreamSpecification={
                'StreamEnabled': True,
                'StreamViewType': 'NEW_AND_OLD_IMAGES'
            },
            SSESpecification={
                'Enabled': True,
                'SSEType': 'KMS',
                # 'KMSMasterKeyId': 'string'
            }
            # TableClass='STANDARD'
        )
        pprint(json.dumps(response, indent=4, sort_keys=True, default=str))

    except conn.exceptions.ParamValidationError:
        logging.debug(
            "Parameter validation failed, check inoutted parameters.")


if __name__ == '__main__':

    create_table(dynamoConn, "Sales")
