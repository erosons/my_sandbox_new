#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports
import sqlalchemy
import bcpandas as bc
import dsnparse
import os
import logging
from bcpandas import SqlCreds
from sqlalchemy import create_engine, types
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
import tempfile

logging.basicConfig(level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")

# Create a logger instance (this uses the root logger with basicConfig settings)
logger = logging.getLogger()


# def auth(ENV) -> object:
def parse_params(env, db=None, host=None, user=None, password=None):

    if env == "TESTING":
        host: str = host
        user: str = user
        password: str = password
        db: str = db
        return f"mssql+pyodbc://{user}:{password}@{host}/{db}?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
    else:
        host: str = host
        user: str = user
        password: str = password
        db: str = db
        return f"mssql+pyodbc://{user}:{password}@{host}/{db}?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"


def get_engine(isolation: str, url):
    """
    Creates a connection using the parameters defined in ODBC connect string
    """
    engine = create_engine(url)
    engine.update_execution_options(isolation=isolation)
    return engine  #


def bccreds(url=None):
    """
    A SqlCreds connection object converted from params string.
    """
    d = dsnparse.parse(url)
    creds = SqlCreds(d.host, d.database, d.user, d.password, driver_version=18)
    return creds


class DB:
    """Simple SQL Server database class used to convert query results to
        different formats and also send sql statements to sql server
    Parameters:
        schema    database schema, defaults to dbo
        isolation      database isolation level, defaults to READ UNCOMMITTED
    """

    def __init__(
        self,
        schema="dbo",
        isolation="READ UNCOMMITTED",
        db=None,
        host=None,
        user=None,
        password=None,
        env=None,
    ):
        """initialize connection."""
        self.logger = logging.getLogger()
        self.isolation = isolation
        self.url = parse_params(env, db, host, user, password)
        self.logger.info(self.url)
        engine = get_engine(isolation=self.isolation, url=self.url)
        self.engine = engine
        self.conn = self.engine.connect()
        self.metadata = sqlalchemy.MetaData(schema=schema)
        # self.Base = declarative_base(self.engine)
        self.conn = self.engine.pool._creator()
        self.cursor = self.conn.cursor()

    def send_statement(self, sql: str):
        """Send Database Statement."""
        Session = sessionmaker(self.engine)
        self.logger.debug(f"Executing Query: {sql}")
        with Session() as session:
            session.execute(sql)
            session.commit()
            session.close()

    def fetch_all(self, sql: str) -> list:
        """Send Database Query and expect results."""
        self.logger.debug(f"Executing Query: {sql}")
        Session = sessionmaker(self.engine)
        with Session() as session:
            results = session.execute(sql).fetchall()
            session.close()
        return results

    def to_pandas(self, sql: str) -> pd.DataFrame:
        return pd.read_sql_query(sql, con=self.engine)

    def to_excel(self, df: pd.DataFrame, file_name: str) -> None:
        """
        Export dataframe to excel
        """
        tmp = tempfile.gettempdir()
        df.to_excel(tmp + os.sep + file_name, encoding="utf-8", index=False)

    def to_csv(self, df: pd.DataFrame, file_name: str) -> None:
        """
        Export dataframe to csv
        """
        tmp = tempfile.gettempdir()
        df.to_csv(tmp + os.sep + file_name, encoding="utf-8", index=False)

    def big_data_read(self, sql: str, chunking: int, log=True):
        """
        Save query results as a pandas dataframe.
        Parameters:
            sql     A SQL Query string.
            log     View logging output, default: True.

        """

        if log is True:
            self.logger.info(f"Querying Dremio: {sql}")
        return pd.read_sql_query(sql, con=self.stream_engine(), chunksize=chunking)

    def stream_engine(self):
        """
        Creates a connection using the parameters defined in ODBC connect string
        """
        if "DREMIO_CONNECTION_URL" not in os.environ:
            self.help()
            return
        try:
            engine = create_engine(self.url)
            conn = engine.connect().execution_options(stream_results=True)
            return conn
        except Exception as e:
            return self.logger.error(e)

    def to_sql(self, df, name, method="replace", bcp_path="/opt/mssql-tools/bin/bcp"):
        """
        Pandas Dataframe to SQL Server (via BCPANDAS)
        TODO: Add Generic Pandas to_sql functionality as well
        """
        # Ensure TrustServerCertificate is set to 'yes' in odbc_kwargs
        
        b = bccreds(self.url)
        creds = SqlCreds(
            b.server,
            b.database,
            b.username,
            b.password,
            odbc_kwargs={'TrustServerCertificate': 'yes'}
        )
        bc.to_sql(
            df=df,
            table_name=name,
            creds=creds,
            index=False,
            if_exists=method,
            bcp_path=bcp_path,
        )
