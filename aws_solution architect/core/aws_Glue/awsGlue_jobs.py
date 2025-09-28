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


def job_creation():
    logging.info("creating a crawler")
    try:
        response = glueConn.create_job(
            Name='Edi_1',
            Role='AWSGlueServiceRole-Demo',
            Command={
                'Name': 'glueetl',
                'ScriptLocation': 's3://glue-source-hoc/iris_onboarder.py',
                'PythonVersion': '3'
            },
            DefaultArguments={
                '--TempDir': 's3://glue-source-hoc/temp_dir',
                '--job-bookmark-option': 'job-bookmark-disable'
            },
            MaxRetries=1,
            GlueVersion='3.0',
            NumberOfWorkers=2,
            WorkerType='Standard'
        )

        print(json.dumps(response, indent=4, sort_keys=True, default=str))

    except glueConn.exceptions.InvalidInputException:
        logging.debug("The input provided was not valid.")
    except glueConn.exceptions.AlreadyExistsException:
        logging.debug("A resource to be created or added already exists")
    except glueConn.exceptions.OperationTimeoutException:
        logging.debug("Operation could not be completed,operation timed out.")
    except glueConn.exceptions.ResourceNumberLimitExceededException:
        logging.debug("A resource numerical limit was exceeded..")
