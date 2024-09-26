import logging
import boto3
from botocore.retries import bucket
import configparser
import psycopg2
import pyodbc


# credential for both redshift , iam and bucketname
parser = configparser.ConfigParser()
parser.read("pipeline.conf")
dbname = parser.get("aws_cred_dw", "database")
user = parser.get("aws_cred_dw", "username")
password = parser.get("aws_cred_dw", "password")
host = parser.get("aws_cred_dw", "host")
port = parser.get("aws_cred_dw", "port")
account_id = parser.get("aws_boto_credentials", "account_id")
iam_role = parser.get("aws_cred_dw", "iam_role")
bucketname = parser.get("aws_boto_credentials", "bucket_name")


# connect to redishift cluster
redshift_connection = psycopg2.connect(
    "dbname=" + dbname
    + " user=" + user
    + " password=" + password
    + " host=" + host
    + " port=" + port
)
"""
redshift_connection = psycopg2.connect(database=dbname,
                                       host=host,
                                       port=port,
                                       user=user,
                                       password=password)

"""

if redshift_connection is None:
    print('Error establishing connecting to the MySQL databasse')
else:
    print(f'connection {redshift_connection} established')

# run the  Copy commad to load the file into Redshift


S3_URI = ("s3://" + bucketname + "/order_extract.csv")
role_string = ("arn:aws:iam::" + account_id + ":role/" + iam_role)


"""
SQl query for copying from S3 into DW
"""

sql = "COPY my_schema.my_table"
sql = sql + " FROM %s "
sql = sql + " iam_role %s"
sql = sql + "delimiter ',';"


# create a cursor object and execute the COPY

r_s = redshift_connection.cursor()
r_s.execute(sql, (S3_URI, role_string))

# Close the cursor and commit the transaction
r_s.close()
redshift_connection.commit()

# Close connection
# redshift_connection.close()
