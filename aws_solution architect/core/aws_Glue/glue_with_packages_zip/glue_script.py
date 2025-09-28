# glue_job_script.py
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Add the S3 path to your custom modules to the system path
sys.path.insert(0, 's3://your-bucket/path-to-your-repo/src/')
sys.path.insert(0, 's3://your-bucket/path-to-packages/requests_package.zip')

# Import your custom functions and any installed packages
from my_functions import function_one, function_two
from utils import helper_function
import requests

# Initialize Glue context and job
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Use the requests package
response = requests.get('https://api.github.com')
print(response.status_code)

# Call your custom functions
function_one()
function_two()
helper_function()

job.commit()
