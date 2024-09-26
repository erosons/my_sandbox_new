
from pyspark.sql import SparkSession, Row
from delta.tables import *
import pandas as pd
import boto3
from pandas import DataFrame

# Create a sample DataFrame
data = [
    Row(id=1, name="Alice", age=29),
    Row(id=2, name="Bob", age=35),
    Row(id=3, name="Catherine", age=26)
]

env:str = 'TESTING'
# "sbg_sandbox_marketing.roidashboard"
roidashboard:str = 'roidashboard'
schema:str = 'sbg_sandbox_marketing'
bucket_name = 'idl-sbgayt-uw2-sandbox-sbgayt-prd'
prefix:str = 'paid_media'
deltalake_bucketpath:dict = {"path":"s3://{}/delta_paid_media/".format(bucket_name)}
path:str = 's3://{}/{}/'.format(bucket_name,prefix)

# The function is used to get objects greater then specified date
def list_s3_objects(bucket_name, prefix)->str: 
   objectpath=[]
   page_counter = 0
   paginator = s3.get_paginator('list_objects_v2') 
   page_iterator = paginator.paginate(Bucket=bucket_name, Prefix=prefix) 
   for page in page_iterator:
      counter +=1
      if 'Contents' in page: 
         for obj in page['Contents']: 
            s3_last_modified = obj['LastModified'] 
            s3_last_modified_dt = s3_last_modified.replace(tzinfo=timezone.utc)
            # Example comparison with current time current_time = datetime.now(timezone.utc) 
            if s3_last_modified_dt > two_weeks_dt: 
                  print(f"Key: {obj['Key']}")
                  objectpath.append(obj['Key'])
      else: print(f"No objects found in the page :{page_counter}.") 
    return objectpath

def aws_authentication() -> str:
    if env == 'TESTING':
        # when testing get temporary  credential from devportal
        aws_session = boto3.session.Session(
        aws_access_key_id='',
        aws_secret_access_key='',
        aws_session_token= ''
        )
        s3_connection = aws_session.client('s3')
        return s3_connection 
    else :
        # In production for every job a temporary credentials will obtain using IAM role from sts
        session = boto3.client("sts")
        response = sts.assume_role(
            RoleArn="arn:aws:iam::052517444781:role/marketing",
            RoleSessionName="liftlab-session"
        )
        credentials:dict = response['Credentials']
        my_session = boto3.session.Session(
        aws_access_key_id= credential['AccessKeyId'],
        aws_secret_access_key=credential['SecretAccessKey'],
        aws_session_token= credential['SessionToken']
        )
        s3_connection = aws_session.client('s3')
        return s3_connection 


df = spark.createDataFrame(data)
# delta_table_path = "s3://idl-sbgayt-uw2-sandbox-sbgayt-prd/delta_paid_media/ROIDashboard"

#  ROI dashboard data
def basetable_checker(schema,tablename)-> bool:
      """
      Checks if the base delta table exist
      """
       sqldf=spark.sql("SELECT * from {}.{} LIMIT 1".format(schema,tablename))
       return bool(sqldf.empty)

# Write the DataFrame to a Delta table
# df.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(delta_table_path)
def base_table_creator(tablename,bucketpath,schema) -> None :
    # create base delta table on the validation
    if basetable_checker(schema,tablename) == True:
        df = spark.read\
                .option("inferSchema","true")\
                .option("header", True)\
                .csv(path)
        df.write \
            .format("delta") \
            .options(**bucketpath) \
            .mode("overwrite") \
            .saveAsTable("{}.{}".format(schema=schema,bucketpath=deltalake_bucketpath))
    else:
        sqldf=spark.sql("SELECT * from {}.{} LIMIT 1".format(schema,tablename))
        # Initializing empty sparkDF
        df:DataFrame = spark.createDataFrame([],sqldf.schema)
        for bucketpath in list_s3_objects(bucket_name, prefix):
           df_spark = spark.read\
            .option("inferSchema","true")\
            .option("header", True)\
            .csv(bucketpath)
           df_spark.write.format("delta").mode("append").save(bucketpath)
        df.show(2)

base_table_creator(roidashboard,delta_table_path,sbg_sandbox_marketing)