import logging
from pydoc import Doc
from xml.dom.minidom import Attr
import boto3
import json
from botocore.retries import bucket
import configparser
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr
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


def query_table1(conn: str, Tablename: str,) -> str:
    try:
        response = conn.query(
            TableName=Tablename,
            KeyConditionExpression='Product ID = :Product ID  AND Sales > :Sales',
            ExpressionAttributeValues={':Product ID': {'S': 'TEC-PH-10003988'},
                                       ':Sales': {'N': '10'}}

        )

        for item in response:
            pprint(item['Items'])
    except ClientError as e:
        logging.error(e)


print('\n\n\n------------------------------------------------------------------\n\n\n')


if __name__ == '__main__':

    query_table1(
        dynamoConn, 'Sales')

 #   query_table2(
 #       dynamoConn, 'Sales')
