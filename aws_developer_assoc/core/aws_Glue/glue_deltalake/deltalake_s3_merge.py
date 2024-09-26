#%pip install idps_sdk -i https://artifact.intuit.com/artifactory/api/pypi/pypi-intuit/simple
from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import concat_ws, md5
from functools import singledispatch
from delta.tables import *
import pandas as pd
import boto3
import os
import uuid
from pandas import DataFrame
import logging
from os.path import abspath
import botocore
import subprocess
import numpy as np
import gspread
from pathlib import Path
import json
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from oauth2client.service_account import ServiceAccountCredentials
from idps_sdk import idps_client
from idps_client.exceptions import IdpsSecretException, IdpsKeyException
from googleapiclient.http import MediaIoBaseDownload
import re
from dateutil import parser

# Define the warehouse location
#warehouse_location = abspath('spark-warehouse')

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

env='TESTING'
#initialize all dbutils library
dbutils.library.restartPython()

SUPERGLUE_RUN = False
if not SUPERGLUE_RUN:
    print(dbutils.credentials.showRoles())
    cred = dbutils.credentials.getCurrentCredentials()
    print(cred)
    AWS_ACCESS_KEY_ID :str = cred["aws_access_key_id"]
    AWS_SECRET_ACCESS_KEY:str =cred["aws_secret_access_key"]
    AWS_SESSION_TOKEN :str =cred["aws_session_token"]
    os.environ['AWS_ACCESS_KEY_ID']=cred["aws_access_key_id"]
    os.environ['AWS_SECRET_ACCESS_KEY']=cred["aws_secret_access_key"]
    os.environ['AWS_SESSION_TOKEN']=cred["aws_session_token"]
    os.environ['AWS_DEFAULT_REGION']="us-west-2"
    os.environ['AWS_EC2_METADATA_DISABLED']='true'
    print("Not Running through Superglue")
else:
      SUPERGLUE_RUN = True

my_role = "arn:aws:iam::00000000000:role/marketing"
if not SUPERGLUE_RUN:
    logger.info(f'local role assumed: {dbutils.credentials.assumeRole(my_role)}')
    logger.info("Running locally")
else:
    logger.info('Running supleGlue runtime')


    
# The function is used to get rescored model data, yet to be concluded
def list_s3_objects_deltas(bucket_name, prefix,filter:None) -> list:
    from datetime import datetime, timedelta, timezone

    today:datetime = datetime.now(timezone.utc)
    previous_dt:datetime = today - timedelta(days=2)

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
                if s3_last_modified_dt > previous_dt:
                    logger.info(f"Key: {obj['Key']}")
                    print("s3://{}/{}".format(bucket_name, obj['Key']))
                    objectpath.append("s3://{}/{}".format(bucket_name, obj['Key']))
        else:
            raise Exception (logger.error(f"No objects found in the page: {page_counter}."))
    return objectpath

## The function is used to get objects ROIfiles
def list_s3_bucketfiles(bucket_name, prefix,filter_value:str) -> list:
    from datetime import datetime, timedelta, timezone

    today = datetime.now(timezone.utc)
    yesterday_dt = today - timedelta(days=1)

    s3_conn = aws_authentication(env)
    objectpath = []
    page_counter = 0
    paginator = s3_conn.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=bucket_name, Prefix=prefix)
    for page in page_iterator:
        print(page)
        page_counter += 1
        if 'Contents' in page:
            for obj in page['Contents']:
                print(obj)
                if filter_value in obj['Key']:
                    logger.info(f"Key: {obj['Key']}")
                    print("s3://{}/{}".format(bucket_name, obj['Key']))
                    objectpath.append("s3://{}/{}".format(bucket_name, obj['Key']))
                    print(objectpath)
        else:
            raise Exception (logger.error(f"No objects found in the page: {page_counter}."))
    return objectpath


def aws_authentication(env) -> boto3.client:
    if env == 'TESTING':
        try:
            #These are temp keys from dbutils
            aws_session = boto3.session.Session(
            aws_access_key_id = AWS_ACCESS_KEY_ID,
            aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
            aws_session_token = AWS_SESSION_TOKEN,
                    )
            s3_connection = aws_session.client('s3')

            # Alternative:
            #  boto3.client(
            #      "s3",
            #      AWS_ACCESS_KEY_ID
            #      AWS_SECRET_ACCESS_KEY,
            #      AWS_SESSION_TOKEN,
            #  )
            return s3_connection
        except botocore.exceptions.ClientError as error:
            logger.error(error)
    else:
        try:
            sts = boto3.client("sts")
            response = sts.assume_role(
                RoleArn="arn:aws:iam::00000000000:role/marketing",
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
    Checks if the base delta table exists in the s3 bucket
    """
    return DeltaTable.isDeltaTable(spark, bucketpath['path'])


def base_table_creator(tablename, bucketpath, schema,filter_value,env) -> None:
    """
    Creatin a delta lake table  and merge with with incremental data through md5 hashing of each role
    Parameters:
    filter_value (str): A str used to filter for ROI files in the s3 bucket
    Returns: is a None
    """
    s3_conn = aws_authentication(env)
    print(f'delta table already exists: {basetable_checker(bucketpath)}')
    if not basetable_checker(bucketpath):
        objects =list_s3_bucketfiles(bucket_name, prefix,filter_value)
        filtered_paths:list = [path for path in objects if filter_value in path]
        print(filtered_paths)
        df_initial= spark.read \
            .format("csv")\
            .option("inferSchema","true")\
            .option("header", True) \
            .csv(filtered_paths)

        # Hash the row contents to create a unique identifier for a merge operations
        df_initial_hashed = df_initial.withColumn("row_hash", md5(concat_ws(",", *df_initial.columns)))

        # Write the DataFrame to a Delta table
        df_initial_hashed .write \
            .format("delta") \
            .mode("overwrite") \
            .save(bucketpath['path'])
        sqldf = spark.sql(f"CREATE TABLE {schema}.{tablename} USING DELTA LOCATION '{bucketpath['path']}'")
        if not sqldf.isEmpty():
            raise Exception(logger.error('empty dataframe'))
        else:
            logger.info('Operation complete Tale has been created', quit())
        return 0
    else:
        logger.info('Merging records to the Base table exists, were records from a new files exists')
        if not list_s3_objects_deltas(bucket_name, prefix,filter_value):
            return 1
        else:
            df_count_b4 = spark.sql(f" SELECT count(1) from {schema}.{tablename}")
            for s3_path in list_s3_objects(bucket_name, prefix,filter_value):
                incremental_df = spark.read \
                    .format("csv")\
                    .option("inferSchema","true")\
                    .option("header", True) \
                    .csv(s3_path)
                # Hash the row contents to create a unique identifier
                df_incremental_hashed = incremental_df.withColumn("row_hash", md5(concat_ws(",", *df_incremental.columns)))
                #incremental_df.write.format("delta").mode("append").save(bucketpath['path'])

                # Call exixting delta table for a merge operation
                delta_table = DeltaTable.forPath(spark, bucketpath['path'])
                delta_table.alias("tgt") \
                    .merge(
                        df_incremental_hashed.alias("src"),
                        "tgt.row_hash = src.row_hash"
                    ) \
                    .whenMatchedUpdateAll() \
                    .whenNotMatchedInsertAll() \
                    .execute()
            df_count_after = spark.sql(f" SELECT count(1) from {schema}.{tablename}")
            if df_count_after <= df_count_b4:
                raise Exception('Merge Operation was not successful')
            else:
                logger.info('Operation Merge operation was successful')
            return 0

"""
This section of the script connects to GDrive and combine the extracted 
with the ROIdashboard delta lake table
"""
# configure parameters 
IDPS_END_POINT:str = "vkm.ps.idps.a.intuit.com"  #production end point
IDPS_POLICY:Path = "p-w7vhgp74h80z" # machine policy - AWS Generic
SECRET:str = "keys/sbseg_ghseet_key_pshah8"
AWS_REGION:str = "us-west-2"
scope:list = ['https://www.googleapis.com/auth/drive.readonly']


def connect_idps(endpoint, policyID,secretName, awsRegion = 'us-west-2',awsProfile=None):

    idpsClient = idps_client.IdpsClientFactory.get_instance(
        endpoint=endpoint,
        policy_id=policyID,
        force_generic_policies=True
    )
    try:
        mySecret = idpsClient.get_secret(name=secretName).get_string_value() ## returns the latest version of the secret
        #print(mySecret)
        return mySecret
    except IdpsSecretException:
        return " Secret does not exist"
    
def output_roidashboard_calendar_tbl(tablename1,tablename2,schema,final_tablename_store,IDPS_END_POINT,IDPS_POLICY,SECRET,scope)->None:
    logger.info('Initiating Google connections')
    client_secret = connect_idps(IDPS_END_POINT, IDPS_POLICY,SECRET)
    # path to your save service account key file
    filename=str(uuid.uuid4())
    SERVICE_ACCOUNT_FILE = f"/tmp/{filename}.json"
    with open(SERVICE_ACCOUNT_FILE, "w") as text_file:
        text_file.write(client_secret)
        subprocess.run(['chmod','777',SERVICE_ACCOUNT_FILE],check=True)
    credentials = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_ACCOUNT_FILE, scope)
    client = gspread.authorize(credentials)

    #Open the Google Sheet by name or by URL
    sheet = client.open('LiftLab Mapping')
    worksheet = sheet.get_worksheet(2)
    print(worksheet)

    # Get all values from the sheet
    data = worksheet.get_all_values()
    columns=data[0]
    df_cal=spark.createDataFrame(data[1:],columns)
    df_cal.createOrReplaceTempView("model_calendar")
    spark.sql(f"DROP TABLE IF EXISTS {schema}.{tablename1}")
    spark.sql(f"CREATE TABLE IF NOT EXISTS {schema}.{tablename1} USING PARQUET AS SELECT tbl.*,cdl.training_start_dt,cdl.training_end_dt,cdl.update_dt FROM {schema}.{tablename2} as tbl LEFT JOIN model_calendar as cdl ON cdl.category = tbl.category AND cdl.category_id = tbl.category_id  ")
    
    # create the final roi table
    df_cal.show()

# Call the base_table_creator function
if env=='TESTING':
    logger.info('In testing environment')

    stg_tablename:str = 'roidashboard_stg'
    final_tablename:str = 'roidashboard'
    schema:str = 'sbg_sandbox_marketing'
    bucket_name = ''
    final_tablename_store = "s3://placeholder/finaltable/"
    prefix:str = 'input/LiftLab_Weekly_Input/ROIDasboard/'
    deltalake_bucketpath = {"path": "s3://placeholder/delta_table1/"}

    if base_table_creator(stg_tablename, deltalake_bucketpath, schema,'ROIDash',env) == 0:
        output_roidashboard_calendar_tbl(final_tablename,
                                        stg_tablename,
                                        schema,
                                        final_tablename_store,
                                        IDPS_END_POINT,
                                        IDPS_POLICY,SECRET,
                                        scope
                                        )

else:
    stg_tablename:str = 'roidashboard_stg'
    final_tablename:str = 'roidashboard'
    schema:str = ''
    bucket_name = 'placeholder'
    final_tablename_store = "s3://{}/finaltable/".format(bucket_name)
    prefix:str = 'ROIDasboard/'
    deltalake_bucketpath = {"path": "s3://{}/delta_paid_media/".format(bucket_name)}

    base_table_creator(stg_tablename, deltalake_bucketpath, schema,'ROIDash',env)
    output_roidashboard_calendar_tbl(schema,final_tablename_store,tablename1=final_tablename,tablename2=stg_tablename)