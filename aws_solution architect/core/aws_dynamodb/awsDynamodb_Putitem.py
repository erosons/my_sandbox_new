import logging
import boto3
import json
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
    aws_dynamo = boto3.client('dynamodb', aws_access_key_id=access_keys,
                              aws_secret_access_key=secret_key, region_name="")

    return aws_dynamo


dynamoConn = dynamodb()


def put_item(conn: str, TableName) -> str:
    try:
        response = conn.put_item(
            Item={
                'OrderID': {
                    'S': 'Somewhat Famous',
                },
                'OrderDate': {
                    'S': '2016-08-11',
                },
                'Ship Date': {
                    'S': '2016-11-11',
                },
                'Ship Mode': {
                    'S': 'First Class',
                },
                'Customer ID': {
                    'S': 'CH-13520',
                },
                'Customer Name': {
                    'S': 'Maria tex',
                },
                'Segment': {
                    'S': 'Coporate',
                },
                'Country': {
                    'S': 'United States',
                },
                'City': {
                    'S': 'Houston',
                },
                'State': {
                    'S': 'Twxas',
                },
                'Postal Code': {
                    'S': '42421',
                },
                'Region': {
                    'S': 'North',
                },
                'Product ID': {
                    'S': 'YUR-BI-99991798',
                },
                'Category': {
                    'S': 'Office Supplier',
                },
                'Sub-Category': {
                    'S': 'Storage',
                },
                'Product Name': {
                    'S': 'Stur-D-Stor Shelving, Vertical 5-Shelf: 72"H x 36"W x 18 1/2"D',
                },
                'Sales': {
                    'N': '665.88',
                },
                'Quantity': {
                    'N': '5',
                },
                'Discount': {
                    'N': '0',
                },
                'Profit': {
                    'N': '41.9136',
                },
            },
            ReturnConsumedCapacity='TOTAL',
            TableName=TableName,
        )

        print(response)
    except conn.exceptions.ConditionalCheckFailedException:
        logging.debug('ConditionalcheckFailException')


if __name__ == '__main__':

    put_item(dynamoConn, "Sales")
