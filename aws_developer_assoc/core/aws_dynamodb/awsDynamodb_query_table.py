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
    aws_dynamo = boto3.resource('dynamodb', aws_access_key_id=access_keys,
                                aws_secret_access_key=secret_key, region_name="")

    return aws_dynamo


dynamoConn = dynamodb()


def query_table1(conn: str, TableName: str,) -> str:
    try:
        table = conn.Table(TableName)
        """
        The keyconditionConditionexpression can only be used with the primary
        a combination of both partitin and sort Key
        it can return on or more item
        it can also be passed as a parameter/placeholder
        """
        response = table.query(

            KeyConditionExpression=Key('Product ID').eq(
                'TEC-PH-10003988') & Key("Sales").gt(10)
        )
        for item in response['Items']:
            pprint(item)
    except ClientError as e:
        logging.error(e)


print('\n\n\n------------------------------------------------------------------\n\n\n')

# Query a table base on specified attributes with the primary key


def query_table2(conn: str, TableName: str,) -> str:
    try:
        table = conn.Table(TableName)

        response = table.query(

            KeyConditionExpression=Key('Product ID').eq(
                'TEC-PH-10003988') & Key("Sales").gt(20),
            ProjectionExpression='Category, Quantity, Profit,Country',
            FilterExpression=Attr('Segment').eq('Consumer')
        )
        for item in response['Items']:
            pprint(item)
    except ClientError as e:
        logging.error(e)


# Scan the dynamodb a with Filter
def query_table3(conn: str, TableName: str,) -> str:
    """
    Batch size max ->16MB
    Total items -> 100items

    """

    try:
        table = conn.Table(TableName)

        response = table.scan(
            # Select='COUNT',
            ProjectionExpression='Category, Quantity, Profit,Country, Sales',
            FilterExpression=Attr('Segment').eq(
                'Consumer') & Attr('Sales').gt(1000)
        )
        # print(response['Count'])
        for item in response['Items']:
            pprint(item)
    except ClientError as e:
        logging.error(e)


if __name__ == '__main__':

    query_table3(
        dynamoConn, 'Sales')
