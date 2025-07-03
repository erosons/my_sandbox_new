import pyodbc
import os
import pandas as pd
from pathlib import Path
from script import sqlCommand
from openpyxl.workbook import workbook
import shutil

#  A Function for writing into path


def pathwriter(path):
    excell_writer = pd.ExcelWriter(path)
    df.to_excel(excell_writer, sheet_name="data")
    excell_writer.save()
    print(type(excell_writer))
    print("successful")
    shutil.copy(mypath,
                Path(r"\\Ecdccesms01\bu\CES\Choice\Analytics\Monthly Customer Detail"))
    exit()


def connect():
    server = 'centerpointdb.excelergy.com'
    database = 'RMPROD'
    username = 'abpdatareader'
    password = ''
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                          server+';DATABASE='+database+';UID='+username+';PWD=' + password)
    return cnxn


df = pd.read_sql_query(sqlCommand, connect())
df = df.set_index("CES_LDC_ID")

mypath = Path(
    r"C:\Users\00936124\Desktop\07012020_CustomerDetails.xlsx")
try:
    print("Iam not here")
    pathwriter(mypath)
except(TypeError):
    print("Check your logic")
