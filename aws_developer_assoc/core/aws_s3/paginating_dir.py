import boto3
import boto3.session
from datetime import datetime,timedelta,timezone

today = datetime.now(timezone.utc)
two_weeks_dt = today - timedelta(days=14)

# Create your own session with temporary key 
#Note this key TTL is 1hr
my_session = boto3.session.Session(
  aws_access_key_id='',
  aws_secret_access_key='',
  aws_session_token= ''
)
s3 = my_session.client('s3')
bucket_name = ''
prefix  = 'key-path'


# Function to list all objects in a specific path
def list_s3_objects(bucket_name, prefix): 
   paginator = s3.get_paginator('list_objects_v2') 
   page_iterator = paginator.paginate(Bucket=bucket_name, Prefix=prefix) 
   for page in page_iterator: 
      if 'Contents' in page: 
         for obj in page['Contents']: 
            s3_last_modified = obj['LastModified'] 
            s3_last_modified_dt = s3_last_modified.replace(tzinfo=timezone.utc)
            # print(s3_last_modified_dt)
            # print(f"Key: {obj['Key']}") 
            # print(f"LastModified (datetime): {s3_last_modified_dt}") 
            # Example comparison with current time current_time = datetime.now(timezone.utc) 
            if s3_last_modified_dt > two_weeks_dt: 
                  print(f"Key: {obj['Key']}")
            # else: print("The object was modified in the past.") 
      else: print("No objects found in the specified path.") # List objects in the specified path list_s3_objects(bucket_name, prefix)

list_s3_objects(bucket_name, prefix)
