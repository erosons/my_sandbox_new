import pandas as pd
import configparser
import pymysql
from mysqlconfig import dbConfig
import urllib.parse
import struct
from sqlalchemy import create_engine, event


conn = pymysql.connect(**dbConfig)
print(conn)

cur = conn.cursor()
cur.execute("show tables;")
print(cur.fetchall())
cur.close()


"""Example DAG demonstrating the usage of the PythonOperator."""


pymysql.install_as_MySQLdb()


"""
Setup Connection using SqlAlchemy
"""
https: // docs.sqlalchemy.org/en/14/core/engines.html
# As the URL is like any other URL, special characters such as those that
# may be used in the password need to be URL encoded to be parsed correctly..
# Below is an example of a URL that includes the password "kx%jj5/g",
# where the percent sign and slash characters are represented as %25 and %2F, respectively:

password = urllib.parse.quote_plus("kx%jj5/g")

engine = create_engine("mysql://root:{}@localhost:3306/test".format(password))

with engine.begin() as conn:
    result = conn.execute("SELECT * FROM test.Customers;")
    for rows in result:
        print(rows)
    result.close()

# Trusted Connection
engine = create_engine(
    "mssql+pyodbc://server_name/database_name?driver=SQL Server?Trusted_Connection=yes")

engine = create_engine(
    "mysql+pymysql://some_user:some_pass@some_host/test?charset=utf8mb4")

args, kwargs = engine.dialect.create_connect_args(engine.url)

# Output
# ======
>> args, kwargs
([], {'host': 'some_host', 'database': 'test', 'user': 'some_user',
 'password': 'some_pass', 'charset': 'utf8mb4', 'client_flag': 2})


# UserName and Passwords
engine = create_engine(
    "mssql+pyodbc://scott:tiger@ms_2008",
    isolation_level="REPEATABLE READ"
)
connection = engine.connect()
connection = connection.execution_options(
    isolation_level="READ COMMITTED"
)
