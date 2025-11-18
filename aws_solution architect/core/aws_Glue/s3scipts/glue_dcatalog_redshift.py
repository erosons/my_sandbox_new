
from awsglue import DynamicFrame
from awsglue.job import Job
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.utils import getResolvedOptions
from awsglue.transforms import *

import sys

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Add the S3 path to your custom module to the system path
sc.addPyFile("s3://redshift-stagingarea/src/archive_name.zip")
from my_class import MyClass  # Import your custom class

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1762411867824 = glueContext.create_dynamic_frame.from_catalog(
    database="samplesuperstor-db",
    table_name="samplefull_samplesuperstore_csv",
    transformation_ctx="AWSGlueDataCatalog_node1762411867824"
)

# Script generated for node Change Schema
ChangeSchema_node1762411878776 = ApplyMapping.apply(
    frame=AWSGlueDataCatalog_node1762411867824,
    mappings=[
        ("rowid", "long", "rowid", "long"), ("orderid", "string", "orderid", "string"), ("orderdate", "string", "orderdate", "string"), ("shipdate", "string", "shipdate", "string"), ("shipmode", "string", "shipmode", "string"), ("customerid", "string", "customerid", "string"), ("customername", "string", "customername", "string"), ("segment", "string", "segment", "string"), ("country", "string", "country", "string"), ("city", "string", "city", "string"), (
            "state", "string", "state", "string"), ("postalcode", "long", "postalcode", "long"), ("region", "string", "region", "string"), ("productid", "string", "productid", "string"), ("category", "string", "category", "string"), ("subcategory", "string", "subcategory", "string"), ("productname", "string", "productname", "string"), ("sales", "double", "sales", "double"), ("quantity", "long", "quantity", "long"), ("discount", "double", "discount", "double"), ("profit", "double", "profit", "double")], transformation_ctx="ChangeSchema_node1762411878776")

# Script generated for node Amazon Redshift
AmazonRedshift_node1762411889705 = glueContext.write_dynamic_frame.from_options(
    frame=ChangeSchema_node1762411878776,
    connection_type="redshift",
    connection_options={"redshiftTmpDir": "s3://aws-glue-assets-975049886938-us-east-1/temporary/",
                        "useConnectionProperties": "true",
                        "dbtable": "public.superstore_orders",
                        "connectionName": "s3_glue_connection",
                        "preactions": "CREATE TABLE IF NOT EXISTS public.superstore_orders (rowid BIGINT, orderid VARCHAR, orderdate VARCHAR, shipdate VARCHAR, shipmode VARCHAR, customerid VARCHAR, customername VARCHAR, segment VARCHAR, country VARCHAR, city VARCHAR, state VARCHAR, postalcode BIGINT, region VARCHAR, productid VARCHAR, category VARCHAR, subcategory VARCHAR, productname VARCHAR, sales DOUBLE PRECISION, quantity BIGINT, discount DOUBLE PRECISION, profit DOUBLE PRECISION);"}, transformation_ctx="AmazonRedshift_node1762411889705")
