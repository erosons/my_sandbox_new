import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job


# https: // docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-samples-legislators.html
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)


# Read Data from crawled database
persons = glueContext.create_dynamic_frame.from_catalog(
    database="legislators",
    table_name="persons_json")
print("Count: ", persons.count())
persons.printSchema()

persons2 = glueContext.create_dynamic_frame.from_catalog(
    database="legislators",
    table_name="persons_jsos2")
print("Count: ", persons.count())
persons.printSchema()


# Joined Table
Joinedtable = persons2.apply(persons, "Order ID", "Order ID")

# Droping a Table

persons.drop_fields(["Order ID"])


# Writing the data back to s3 bucket or any other datastore


glueContext.write_dynamic_frame.from_options(persons, connection_type="s3",
                                             connection_options={"path": "s3://etldata01/person"}, format="parquet")

job.commit()
