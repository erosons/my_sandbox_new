import logging
import boto3
import json
from botocore.retries import bucket
import configparser
from botocore.exceptions import ClientError
from pprint import pprint
import json


parser = configparser.ConfigParser()
parser.read("pipeline.conf")
print(parser.sections())
access_keys = parser.get("aws_credentials", "aws_access_key_id")
secret_key = parser.get("aws_credentials", "aws_secret_access_key")
region = parser.get("aws_credentials", "region")
bucket_name = parser.get("aws_credentials", "bucket_name")


logging.basicConfig(filename='new.log', filemode='w', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def glue():
    logging.info("Setting up glue connection")
    try:
            #These are temp keys from dbutils
            aws_session = boto3.session.Session(
            aws_access_key_id = access_keys,
            aws_secret_access_key = secret_key,
            region_name = region
                    )
            aws_glue = aws_session.client('glue')

            return aws_glue
    except ClientError as e:
            logging.error(e)
            return None

def get_databases(glue_connection):

    try:
        # List databases available on Glue.
        database_list_Response = glue_connection.get_databases()
        return database_list_Response
    
    except glue_connection.exceptions.OperationTimeoutException:
        print("Connection timeout")
    except glue_connection.exceptions.EntityNotFoundException:
        print("List Database not found")
    except glue_connection.exceptions.OperationTimeoutException:
        print("OperationTimeoutException, connection issue probabaly")
# Creating crawler : This helps populate the data catalogue with one or many table of the source(s)

def crawler_creation(glue_connection, databasename):
    logging.info("creating a crawler")
    try:
        response = glue_connection.create_crawler(
            Name='S3Crawlers',
            Role='Glue_user',
            DatabaseName = databasename,
            # Description='string',
            Targets={
                'S3Targets': [
                    {
                        'Path': 's3://amzn-s3-glue-poc/full-People.csv',
                        'Exclusions': [
                            'string',
                        ],
                        # 'ConnectionName': 'string',
                        'SampleSize': 100,
                        # 'EventQueueArn': 'string',
                        # 'DlqEventQueueArn': 'string'
                    },
                    # {
                    #     'Path': 's3://etlbucket/data folder/Sales/',
                    #     'Exclusions': [
                    #         'string',
                    #     ],
                    #     # 'ConnectionName': 'string',
                    #     'SampleSize': 1,
                    #     # 'EventQueueArn': 'string',
                    #     # 'DlqEventQueueArn': 'string'
                    # }
                ]
            },
            Schedule='cron(15 12 * * ? *)',
            # TablePrefix='string',
            SchemaChangePolicy={
                'UpdateBehavior': 'UPDATE_IN_DATABASE',
                'DeleteBehavior': 'DELETE_FROM_DATABASE'
            },
            RecrawlPolicy={
                'RecrawlBehavior': 'CRAWL_EVERYTHING'
            },
            LineageConfiguration={
                'CrawlerLineageSettings': 'ENABLE'
            }
        )

        print(json.dumps(response, indent=4, sort_keys=True))

    except glue_connection.exceptions.InvalidInputException:
        logging.debug("The input provided was not valid.")
    except glue_connection.exceptions.AlreadyExistsException:
        logging.debug("A resource to be created or added already exists")
    except glue_connection.exceptions.OperationTimeoutException:
        logging.debug("Operation could not be completed,operation timed out.")
    except glue_connection.exceptions.ResourceNumberLimitExceededException:
        logging.debug("A resource numerical limit was exceeded..")


def starting_crawler(glue_connection):

    try:
        # List crawlers available on Glue.
        crawler_list_Response = glue_connection.list_crawlers()
        print(crawler_list_Response)
    
        # # Starting crawlers available on Glue.
        # starting_response2 = glue_connection.start_crawler(
        #     Name=crawler_list_Response['CrawlerNames'][0])
        # logging.info("Start Crawler")

        # print(json.dumps(starting_response2, indent=4, sort_keys=True, default=str))
    except glue_connection.exceptions.OperationTimeoutException:
        print("Connection timeout")
    except glue_connection.exceptions.EntityNotFoundException:
        print("List Crawler not found")
    except glue_connection.exceptions.CrawlerRunningException:
        print("RunningException:")
    except glue_connection.exceptions.OperationTimeoutException:
        print("OperationTimeoutException, connection issue probabaly")


if __name__ == "__main__":
    glue_connection = glue()
    databasename = get_databases(glue_connection)['DatabaseList'][1]['Name']
    # pprint(
    #        starting_crawler(glue_connection),
    #        indent =4
    #        )
    # databasename = starting_crawler(glue_connection)['CrawlerNames'][2]
    print(crawler_creation(glue_connection, databasename))