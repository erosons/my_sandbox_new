import logging
import boto3
import pymysql
import psycopg2
import csv
import configparser
#from sql_extract import sqlcommand_r_s, sql_incremental_extract
import pandas as pd
from core.redshift-etl.copy_to_redshift import redshift_connection
from ingesting_to_S3 import upload_file, bucket_name


parser = configparser.ConfigParser()
parser.read("pipeline.conf")
hostname = parser.get("mysql_config", "hostname")
port = parser.get("mysql_config", "port")
username = parser.get("mysql_config", "username")
dbname = parser.get("mysql_config", "database")
password = parser.get("mysql_config", "password")


def mysql_conn():
    cxn = pymysql.connect(
        host=hostname,
        user=username,
        password=password,
        db=dbname,
        port=int(port)
    )
    return cxn


"""
Connections
"""
connectn_nw = mysql_conn()

connectn_rs = redshift_connection


# Error catching if connection is established

if connectn_rs is None:
    print(f'Error establishing connecting to the MySQL databasse')
else:
    print("connection {} established".format(connectn_rs))


"""
For incremental extract , This were we get the lastupdate date from the DW
"""

table2 = "my_schema.my_table"

sqlcommand_r_s = "select coalesce(max(lastupdated),'1900-01-01') from %s;"


rs_cursor = connectn_rs.cursor()
rs_cursor.execute(sqlcommand_r_s % (table2))
result = rs_cursor.fetchone()

# This expression below returns just one value since there is one column and row
#params1 = "test.Orders"
last_updated_warehouse = str(result[0])


"""
 This is where we extract the incremental data from the mysqldb using the last upload date in the DW
"""

sql_incremental_extract = "select * from test.Orders"
sql_incremental_extract = sql_incremental_extract + \
    " " + "where lastupdated >= %(value2)s;"

local_filename_incremental = "incremental_order_extract.csv"


df = pd.read_sql(sql_incremental_extract, connectn_nw,
                 params={"value2": last_updated_warehouse})
df.to_csv(local_filename_incremental, index=False, header=None)


"""
 This is where we upload the incremental data into S3 BUCKET.
"""
upload_file(local_filename_incremental, bucket_name,
            object_Name=local_filename_incremental)
