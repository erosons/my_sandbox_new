import pyodbc
import os
import pandas as pd
from pathlib import Path
from script import sqlCommand
from openpyxl.workbook import workbook
import shutil

#  A Function for writing into path


def connect():
    server = ''
    database = 'test'
    username = 'test'
    password = ''
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                          server+';DATABASE='+database+';UID='+username+';PWD=' + password)
    return cnxn


df = pd.read_sql_query(sqlCommand, connect())
df = df.set_index("CES_LDC_ID")
print(df)
