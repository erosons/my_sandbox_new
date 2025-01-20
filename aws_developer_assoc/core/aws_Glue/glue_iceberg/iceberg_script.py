
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkConf, SparkContext
from pyspark.sql import SparkSession
from awsglue.context import GlueContext
from awsglue.job import Job


args = getResolvedOptions(sys.argv, ['JOB_NAME'])

conf_list = [
    #Configs needed for Iceberg
    #file:/home/glue_user/workspace/spark-warehouse

    ("spark.sql.extensions", "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions"),
    ("spark.sql.catalog.glue_catalog", "org.apache.iceberg.spark.SparkCatalog"),
    ("spark.sql.catalog.glue_catalog.warehouse", "s3://dev-xys/stageZone_iceberg/iceber_repo/smt-data/"),
    ("spark.sql.catalog.glue_catalog.catalog-impl", "org.apache.iceberg.aws.glue.GlueCatalog"),
    ("spark.sql.catalog.glue_catalog.io-impl","org.apache.iceberg.aws.s3.S3FileIO")
    #"--datalake-formats","iceberg")
    ]

spark_conf = SparkConf().setAll(conf_list)
spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()
sc = spark.sparkContext
glue_context = GlueContext(sc)
job = Job(glue_context)
job.init(args['JOB_NAME'], args)
df = spark.read \
        .format('jdbc')\
        .option('url','jdbc:dremio:direct=dremio-cloud.com:443')\
        .option("encrypt", "true") \
        .option("dbtable", "schema.tablename")\
        .option("user", "?")\
        .option("password", "?")\
    .option("table", """ ? """)\
    .load()

# jdbcDF = spark.read \
#         .format("com.microsoft.sqlserver.jdbc.spark") \
#         .option("url", url) \
#         .option("dbtable", table_name) \
#         .option("user", username) \
#         .option("password", password).load()
# #df.printSchema()

df.createTempView("temp_table")

df2 = spark.sql("select * from temp_table")
df2.show(3) # Show data in temp_table


# Create new table and insert data from temp_table
if not spark.catalog.tableExists('glue_catalog.dremio.SMT_customer15'):
    sql = f'''
        create table if not exists glue_catalog.dremio.SMT_customer15
        using iceberg 
        tblproperties ('table_type'='ICEBERG','format-version'='2', 
        'write.delete.mode'='copy-on-write',
        'write.update.mode'='merge-on-read',
        'write.merge.mode'='merge-on-read',
        'write.object-storage.enabled'=true)
        location "s3://dev-/stageZone_iceberg/iceber_repo/smt-data/"
        AS 
        SELECT * FROM temp_table'''
    spark.sql(sql)    
else:   
#upsert
    sql = f''' 
        merge into  glue_catalog.dremio.SMT_customer15 target
        using (select * from from temp_table) source
        on target."Account_No" = source."Account_No"
        and target."ID" = source."ID"
        and target.UsageDate=source.UsageDate
        and target.filetrackid=source.filtrackid
        when matched then
        update set *
        when not matched then 
        insert * 
        ''' 
    spark.sql(sql)
job.commit()
 