import psycopg2
import pandas as pd
from sqlalchemy import create_engine


class PostgresDB:
    def __init__(self, dbname, user, password, host, port):
        self.engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')



def read_postgres(self):
    try:
        with self.engine.cursor() as cursor:
            cursor.execute("SELECT * FROM public.invoices")
            records = cursor.fetchall()
            for row in records:
                print(row)
    finally:
        self.engine.close()


def df_read_from(self, sql, batch=None):
    for chunk in pd.read_sql(sql, self.conn, chunksize=batch):
        return chunk


def insert_postgres(self, table: str, tableschema):
    try:
        with self.engine.cursor() as cursor:
            columns = ",".join(column for column in tableschema)
            rows = "?" * len(columns)
            sql_command = "INSERT INTO {} ({}) VALUES({})".format(table,columns, rows)
            cursor.execute(sql_command)
    finally:
        self.engine.close()

def pandas_data_loader(self, table, schema=None,batch=None,Chunksize=None,mode=None):
    pd.to_sql(table,self.conn,schema=schema,chunksize=Chunksize,if_exists=mode)