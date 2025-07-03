import logging
from urllib import response
import boto3
import json
from botocore.retries import bucket
import configparser
from botocore.exceptions import ClientError
from decimal import Decimal
import pandas as pd


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


def get_dataFrame(filepath: str) -> str:
    df = pd.read_csv(str(filepath))
    return df


def batch_write_item(conn: str, TableName: str, filepath: str) -> str:
    """
    maximum item is 400kb
    number of request -> 25
    total request size -> 16MB
    Parallel processing reduces latency, but each specified put and delete request 
    consumes the same number of write capacity units whether it is processed in parallel or not
    """
    table = conn.Table(TableName)
    try:
        with table.batch_writer() as batch:
            for index, rows in get_dataFrame(filepath).iterrows():
                # print(rows)
                iter = json.loads(rows.to_json(orient="columns"))
                response = batch.put_item(Item={
                    'Postal Code': str(iter['Postal Code']),
                    'Product Name': str(iter['Product Name']),
                    'Profit': int(iter['Profit']),
                    'Quantity': int(iter['Quantity']),
                    'Region': str(iter['Region']),
                    'Segment': str(iter['Segment']),
                    'Ship Date': str(iter['Ship Date']),
                    'Ship Mode': str(iter['Ship Mode']),
                    'State': str(iter['State']),
                    'Sub-Category': str(iter['Sub-Category']),
                    'Product ID': str(iter['Product ID']),
                    'Sales': int(iter['Sales']),
                    'Category': str(iter['Category']),
                    'City': str(iter['City']),
                    'Country': str(iter['Country']),
                    'Customer ID': str(iter['Customer ID']),
                    'Customer Name': str(iter['Customer Name']),
                    # 'Discount': int(iter['Discount']),
                    'Order Date': str(iter['Order Date']),
                    'Order ID': str(iter['Order ID']),

                }
                )
                return print(response)
    except ClientError as e:
        logging.error(e)


if __name__ == '__main__':

    batch_write_item(
        dynamoConn, 'Sales', '/Users/samsoneromonsei/Downloads/SampleSuperstore.csv')
