from kafka import KafkaProducer
from kafka.errors import KafkaError
import socket
import time

# pip install aws-msk-iam-sasl-signer-python
from aws_msk_iam_sasl_signer import MSKAuthTokenProvider
from botocore.credentials import CredentialProvider, RefreshableCredentials
from botocore.session import get_session
from aws_msk_iam_sasl_signer import MSKAuthTokenProvider
from pprint import pprint
import boto3
from dotenv import load_dotenv
import os
import botocore
import logging
import json
import pandas as pd


logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")
# Create a logger instance (this uses the root logger with basicConfig settings)
logger = logging.getLogger()

# Example usage
logger.info("This is an info message")
load_dotenv()


aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key = os.getenv("aws_key_secret")
print(aws_secret_access_key)
topic = "awskafkatopic1"


# class CustomCredentialProvider(CredentialProvider):
#     METHOD = "custom-method"

#     def __init__(self, access_key, secret_key, session_token=None):
#         self.access_key = access_key
#         self.secret_key = secret_key
#         self.session_token = session_token

#     def load(self):
#         return RefreshableCredentials(
#             access_key=self.access_key,
#             secret_key=self.secret_key,
#             token=None,
#             expiry_time=None,
#             refresh_using=None,
#             method=self.METHOD,
#         )


class MSKTokenProvider:
    def __init__(self, region):
        self.region = region

    def token(self):
        # Generate the auth token using the MSKAuthTokenProvider
        token, _ = MSKAuthTokenProvider.generate_auth_token(self.region)
        return token

# Initialize the MSK token provider with your AWS region
region = 'us-west-2'  # Replace with your actual region
tp = MSKTokenProvider(region=region)
print(tp)


# custom_provider = CustomCredentialProvider(aws_access_key_id, aws_secret_access_key)
region = "us-west-2"


# Example usage
logger.info("This is an info message")
topic = "awskafkatopic1"


def aws_authentication() -> boto3.client:
    try:
        # These are temp keys and expires after 1 hour, generate yours for testing
        aws_session = boto3.session.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name="us-east-1",
        )
        s3_connection = aws_session.client("kafka")
        logger.info("connection return", s3_connection)
        return s3_connection
    except botocore.exceptions.ClientError as error:
        logger.error(error)


def get_msk_boostrap_server():
    conn = aws_authentication()
    response = conn.get_bootstrap_brokers(
        ClusterArn="arn:aws:kafka:us-east-1:975049886938:cluster/demo-cluster-1/fe7e59e2-f0d9-4189-bb3a-49a64a9f5f29-18"
    )

    pprint(response, indent=3)
    bs = response["BootstrapBrokerStringSaslIam"]
    logger.info(bs.split(",")[0])
    return bs.split(",")[0]


bootstrap_servers = get_msk_boostrap_server()
#tp = generate_auth_token_custom_provider(region, bootstrap_servers, custom_provider)


producer = KafkaProducer(
    bootstrap_servers="{}".format(get_msk_boostrap_server()),
    security_protocol="SASL_SSL",
    api_version=(0, 10, 1),
    sasl_mechanism="OAUTHBEARER",
    sasl_oauth_token_provider=tp,
    # client_id=socket.gethostname(),
    client_id="samsple-superstor-stream",
    acks="all",
    compression_type="snappy",
)


# # Delivery callback function (optional)
# def delivery_report(err, msg):
#     """Called once for each message produced to indicate delivery result."""
#     if err is not None:
#         print(f"Message delivery failed: {err}")
#     else:
#         print(
#             f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}"
#         )


# def data_serialization_to_Producer():
#     if producer.bootstrap_connected():
#         df = pd.read_csv(os.path.expanduser("~/Downloads/Sample - Superstore.csv"))
#         df = df.head(1)
#         records_rows = df.shape[0]
#         for row in df.itertuples(index=False, name=None):
#             logger.info(row)
#             # row is a tuple, convert it to a dictionary manually if needed
#             row_dict = {df.columns[i]: row[i] for i in range(len(row))}
#             print(row_dict)
#             # Convert JSON object to string
#             json_value = json.dumps(row_dict).encode("utf-8")

#             # Produce a message to a Kafka topic
#             while records_rows > 0:
#                 try:
#                     producer.send(topic, json.dumps(json_value).encode("utf-8"))
#                     producer.flush()
#                     print("Produced!")
#                 except Exception as e:
#                     print("Failed to send message:", e)
#                 records_rows = -1

#     else:
#         logger.error("Bootstrap Server Connection failure")


# producer.close()

if __name__ == "__main__":
    pass
    #data_serialization_to_Producer()
