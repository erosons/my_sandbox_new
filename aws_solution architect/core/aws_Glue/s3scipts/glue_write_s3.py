from awsglue import DynamicFrame
from awsglue.job import Job
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.utils import getResolvedOptions
from awsglue.transforms import *

import sys

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Add the S3 path to your custom module to the system path
# sc.addPyFile("s3://redshift-stagingarea/src/archive_name.zip")
# from my_class import MyClass  # Import your custom class
sample_mappings= ([
        ("rowid", "long", "rowid", "long"), \
        ("orderid", "string", "orderid", "string"), \
        ("orderdate", "string", "orderdate", "string"), \
        ("shipdate", "string", "shipdate", "string"), \
        ("shipmode", "string", "shipmode", "string"), \
        ("customerid", "string", "customerid", "string"), \
        ("customername", "string", "customername", "string"),("segment", "string", "segment", "string"), ("country", "string", "country", "string"), ("city", "string", "city", "string"), ("state", "string", "state", "string"), ("postalcode", "long", "postalcode", "long"), ("region", "string", "region", "string"), ("productid", "string", "productid", "string"), ("category", "string", "category", "string"), ("subcategory", "string", "subcategory", "string"), ("productname", "string", "productname", "string"), ("sales", "double", "sales", "double"), ("quantity", "long", "quantity", "long"), ("discount", "double", "discount", "double"), ("profit", "double", "profit", "double")])

# Script generated for node AWS Glue Data Catalog
dfy_trxn = glueContext.create_dynamic_frame.from_catalog(
      database="samplesuperstor-db",
      table_name="samplefull_samplesuperstore_csv"
)

dfy_retunrd = glueContext.create_dynamic_frame.from_catalog(
      database="samplesuperstor-db",
      table_name="samplefull_returned_csv"
)


# Schema changing
dfymapping= ApplyMapping.apply(
    frame=dfy_trxn ,
    mappings=sample_mappings,
    transformation_ctx="mappingapply"
)

dfyfilter = dfymapping.filter(
    f=lambda x: x["shipmode"] in ["Second Class"]
    and x["state"] in ["Kentucky"]
)

# Joining frame by ID
trxn_person = dfyfilter.join(
    paths1=["OrderID"], paths2=["OrderID"], frame2=dfy_retunrd 
)

# Compare record counts
print("Unfiltered record count: ", dfymapping.count())
print("Filtered record count:  ", dfyfilter.count())
print("person",dfy_retunrd.count())
print("person",trxn_person.count())

glueContext.write_dynamic_frame.from_options(\
frame = trxn_person,
connection_options = {'path': 's3://redshift-stagingarea/src/regular/'},
connection_type = 's3',
format = 'parquet',
transformation_ctx="sink"
)


# write to a catalog table
glueContext.write_dynamic_frame.from_catalog(
frame = dfyfilter,
database = "samplesuperstor-db",
table_name = "sample_glue_redshift_superstore_orders",
transformation_ctx="sink"
)

# convert to pyspark -> This can be memory intense better to keep in dynamicFrame if possible
trxn_person.toDF()

trxn_person2 = trxn_person1.select("OrderID", "city","country")
trxn_person2.show()

job.commit()
