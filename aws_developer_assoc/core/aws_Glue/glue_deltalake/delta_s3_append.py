from pyspark.sql import SparkSession, Row
from functools import singledispatch
from delta.tables import *
import pandas as pd
import boto3
import os
from pandas import DataFrame
import logging
from os.path import abspath
import botocore

# Define the warehouse location
warehouse_location = abspath('spark-warehouse')

# Set up our logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Initialize Spark session with Delta Lake and Hive Support
# spark = SparkSession.builder \
#     .appName('LiftLab Project') \
#     .config("spark.sql.warehouse.dir", warehouse_location) \
#     .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
#     .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
#     .enableHiveSupport() \
#     .getOrCreate()

# Set up Hive configurations
# spark=spark
# spark.conf.set("spark.sql.warehouse.dir", warehouse_location) \
# spark.conf.set("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
# spark.conf.set("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
# spark.conf.set('hive.exec.dynamic.partition', 'true')
# spark.conf.set('hive.exec.dynamic.partition.mode', 'nonstrict')
# spark.conf.set('hive.groupby.orderby.position.alias', 'true')
# spark.conf.set('hive.exec.parallel', 'true')

# Defining global variables
env = 'TESTING'
tablename:str = 'roidashboard'
schema:str = ''
bucket_name = ''
prefix:str = ''
deltalake_bucketpath = {"path": "s3://{}/delta_paid_media/".format(bucket_name)}
path = 's3://{}/{}/'.format(bucket_name, prefix)

# The function is used to get rescored model data, yet to be concluded
@singledispatch
def list_s3_objects(bucket_name, prefix,filter:None) -> list:
    from datetime import datetime, timedelta, timezone

    today:datetime = datetime.now(timezone.utc)
    yesterday_dt:datetime = today - timedelta(days=1)

    s3_conn = aws_authentication(env)
    objectpath = []
    page_counter = 0
    paginator = s3_conn.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=bucket_name, Prefix=prefix)
    for page in page_iterator:
        page_counter += 1
        if 'Contents' in page:
            for obj in page['Contents']:
                s3_last_modified = obj['LastModified']
                s3_last_modified_dt = s3_last_modified.replace(tzinfo=timezone.utc)
                if s3_last_modified_dt > yesterday_dt:
                    logger.info(f"Key: {obj['Key']}")
                    objectpath.append("s3://{}/{}".format(bucket_name, obj['Key']))
        else:
            logger.error(f"No objects found in the page: {page_counter}.")
    return objectpath

## The function is used to get objects ROIfiles
@list_s3_objects.register
def list_s3_objects(bucket_name, prefix,filter_value:str) -> list:
    from datetime import datetime, timedelta, timezone

    today = datetime.now(timezone.utc)
    yesterday_dt = today - timedelta(days=1)

    s3_conn = aws_authentication(env)
    objectpath = []
    page_counter = 0
    paginator = s3_conn.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=bucket_name, Prefix=prefix)
    for page in page_iterator:
        page_counter += 1
        if 'Contents' in page:
            for obj in page['Contents']:
                if filter_value in obj['Key']:
                    logger.info(f"Key: {obj['Key']}")
                    objectpath.append("s3://{}/{}".format(bucket_name, obj['Key']))
        else:
            logger.error(f"No objects found in the page: {page_counter}.")
    return objectpath


def aws_authentication(env) -> boto3.client:
    if env == 'TESTING':
        try:
            #These are temp keys and expires after 1 hour, generate yours for testing
            aws_session = boto3.session.Session(
                aws_access_key_id='',
                aws_secret_access_key='',
                aws_session_token=''
            s3_connection = aws_session.client('s3')
            return s3_connection
        except botocore.exceptions.ClientError as error:
            logger.error(error)
    else:
        try:
            sts = boto3.client("sts")
            response = sts.assume_role(
                RoleArn="",
                #RoleArn="arn:aws:iam::887888612666:role/emr-ec2-profile-sbg-analyst-marketing-prd",
                RoleSessionName="liftlab-session"
            )
            credentials = response['Credentials']
            aws_session = boto3.session.Session(
                aws_access_key_id=credentials['AccessKeyId'],
                aws_secret_access_key=credentials['SecretAccessKey'],
                aws_session_token=credentials['SessionToken']
            )
            s3_connection = aws_session.client('s3')
            return s3_connection
        except botocore.exceptions.ClientError as error:
            logger.error(error)

# Delta table path validator
def basetable_checker(bucketpath) -> bool:
    """
    Checks if the base delta table exists
    """
    return DeltaTable.isDeltaTable(spark, bucketpath['path'])

# Write the DataFrame to a Delta table
def base_table_creator(tablename, bucketpath, schema,filter_value) -> None:
    env = 'TESTING'
    files_names='list'
    s3_conn = aws_authentication(env)
    print(basetable_checker(bucketpath))
    if not basetable_checker(bucketpath):
        objects =list_s3_objects(bucket_name, prefix,filter_value)
        filtered_paths:list = [path for path in objects if files_names in path]
        print(filtered_paths)
        df = spark.read \
            .option("inferSchema", "true") \
            .option("header", True) \
            .csv(filtered_paths)
        df.write \
            .format("delta") \
            .mode("overwrite") \
            .save(bucketpath['path'])
        spark.sql(f"CREATE TABLE {schema}.{tablename} USING DELTA LOCATION '{bucketpath['path']}'")
    else:
        logger.info('Base table exists. Appending new data.')
        for s3_path in list_s3_objects(bucket_name, prefix,filter_value):
            incremental_df = spark.read \
                .option("inferSchema", "true") \
                .option("header", True) \
                .csv(s3_path)
            incremental_df.write.format("delta").mode("append").save(bucketpath['path'])

# Call the base_table_creator function
base_table_creator(tablename, deltalake_bucketpath, schema,'list')