import logging
import pymysql
import os
from pathlib import Path
import configparser
from sql import sqlcommand
import pandas as pd


parser = configparser.ConfigParser()
parser.read("/opt/airflow/src/pipeline.conf")
hostname = parser.get("mysql_config", "hostname")
port = parser.get("mysql_config", "port")
username = parser.get("mysql_config", "username")
dbname = parser.get("mysql_config", "database")
password = parser.get("mysql_config", "password")


logging.basicConfig(
    filename="new.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


def mysql_conn():
    cxn = pymysql.connect(
        host=hostname, user=username, password=password, db=dbname, port=int(port)
    )
    return cxn


connectn = mysql_conn()
logging.info("Connectionis {} is establised".format(connectn))

"""
Error catching if connection is established
"""
if connectn is None:
    print("Error establishing connecting to the MySQL databasse")
else:
    print("connection %s established" % (mysql_conn()))


"""
Calling of the sqlquery and defining of file where the extract will be loaded into
"""
sqlcommand = "SELECT * FROM test.Orders;"

query = str(sqlcommand)
local_filename = "order_extract.csv"


df = pd.read_sql(query, connectn)
df.to_csv(local_filename, index=False, header=None)


"""

Calling cursor object from pymsql library to sql query


cursor = connectn.cursor()
cursor.execute(query)
result = cursor.fetchall()


Writing to a csv file

with open(local_filename, 'w') as fp:
    csv_file = csv.writer(fp, delimiter='|')
    csv_file.writerow(result)
    fp.close()


Closing of the session for cursor and pymsql

cursor.close()
connectn.close()
"""
