# import pypyodbc as pyconn
import pyodbc
# from dbConfig import config
import pandas as pd
from pathlib import Path
from DbConn import msSQlconn


cursor = msSQlconn().cursor()

command = "IF OBJECT_ID('[dbo].[SMT_TEST]', 'U') IS NOT NULL\
          DROP TABLE [dbo].[SMT_TEST]\
          CREATE TABLE SMT_TEST(ESIID varchar(max), REP_DUNS varchar(max), GenerationCode varchar(max),\
          UsageDate varchar(max), HE1 varchar(max), HE2 varchar(max), HE3 varchar(max), HE4 varchar(max), HE5 varchar(max), HE6 varchar(max),\
          HE7 varchar(max), HE8 varchar(max), HE9 varchar(max), HE10 varchar(max), HE11 varchar(max), HE12 varchar(max), HE13 varchar(max), \
          HE14 varchar(max), HE15 varchar(max), HE16 varchar(max), HE17 varchar(max), HE18 varchar(max), HE19 varchar(max), HE20 varchar(max),\
          HE21 varchar(max), HE22 varchar(max), HE23 varchar(max), HE24 varchar(max), HE25 varchar(max), LoadDate varchar(max))"

sql = "INSERT INTO SMT_TEST VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"

data = pd.read_csv(
    '/Users/samsoneromonsei/csvfiles/100000rowsfiles.csv', cache_dates=True, nrows=2)

#  Defining column header for intersion
cols = ",".join([str(i) for i in data.columns.tolist()])

cursor.execute(command)

for i, row in data.iterrows():
    print(tuple(row))
    cursor.execute(sql, tuple(row))

    cursor.commit()


"""

cur = conn.cursor()
cur.execute("Select* from test.Customers")
for rows in cur.fetchall():
    cur1.execute(Command2, rows)
    print(cur.fetchall())
    cur1.commit()
cur.close()

"""
