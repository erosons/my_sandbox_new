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


def glue():
    logging.info("Setting up glue connection")
    aws_glue = boto3.client('glue', aws_access_key_id=access_keys,
                            aws_secret_access_key=secret_key, region_name="")

    return aws_glue


glueConn = glue()


# Creating crawler : This helps populate the data catalogue with one or many table of the source(s)
def crawler_creation():
    logging.info("creating a crawler")
    try:
        response = glueConn.create_crawler(
            Name='S3Crawlers',
            Role='Glue_user',
            DatabaseName='marwen_analytics',
            # Description='string',
            Targets={
                'S3Targets': [
                    {
                        'Path': 's3://etlbucket/data folder/Bitcon/',
                        'Exclusions': [
                            'string',
                        ],
                        # 'ConnectionName': 'string',
                        'SampleSize': 1,
                        # 'EventQueueArn': 'string',
                        # 'DlqEventQueueArn': 'string'
                    },
                    {
                        'Path': 's3://etlbucket/data folder/Sales/',
                        'Exclusions': [
                            'string',
                        ],
                        # 'ConnectionName': 'string',
                        'SampleSize': 1,
                        # 'EventQueueArn': 'string',
                        # 'DlqEventQueueArn': 'string'
                    },
                    {
                        'Path': 's3://etlbucket/data folder/Neflix/',
                        'Exclusions': [
                            'string',
                        ],
                        # 'ConnectionName': 'string',
                        'SampleSize': 1,
                        # 'EventQueueArn': 'string',
                        # 'DlqEventQueueArn': 'string'
                    },
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

    except glueConn.exceptions.InvalidInputException:
        logging.debug("The input provided was not valid.")
    except glueConn.exceptions.AlreadyExistsException:
        logging.debug("A resource to be created or added already exists")
    except glueConn.exceptions.OperationTimeoutException:
        logging.debug("Operation could not be completed,operation timed out.")
    except glueConn.exceptions.ResourceNumberLimitExceededException:
        logging.debug("A resource numerical limit was exceeded..")


def starting_crawler():

    try:
        # List crawlers available on Glue.
        crawler_list_Response = glueConn.list_crawlers()
        print(crawler_list_Response)

        # Starting crawlers available on Glue.
        starting_response2 = glueConn.start_crawler(
            Name=crawler_list_Response['CrawlerNames'][0])
        logging.info("Start Crawler")

        print(json.dumps(starting_response2, indent=4, sort_keys=True, default=str))
    except glueConn.exceptions.OperationTimeoutException:
        print("Connection timeout")
    except glueConn.exceptions.EntityNotFoundException:
        print("List Crawler not found")
    except glueConn.exceptions.CrawlerRunningException:
        print("RunningException:")
    except glueConn.exceptions.OperationTimeoutException:
        print("OperationTimeoutException, connection issue probabaly")


if __name__ == "__main__":
    crawler_creation()
    starting_crawler()
