# import pypyodbc as pyconn
import pyodbc
# from dbConfig import config
import pandas as pd
from pathlib import Path
from script import sqlCommand
from openpyxl.workbook import workbook

server = '' 
database = 'test' 
username = 'test' 
password = '' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

df=pd.read_sql_query(sqlCommand,cnxn)
path= Path('06012020_CustomerDetails.xlsx')
if  path.exists==False:
			path.mkdir()
			excell_writer=pd.ExcelWriter(path)
			df.to_excel(excell_writer,sheet_name="data")
			excell_writer.save()
else:
			excell_writer=pd.ExcelWriter(path)
			df.to_excel(excell_writer,sheet_name="data")
			excell_writer.save()
	    
