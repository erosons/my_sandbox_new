from bcp import DB
import os
import logging
from typing import List
from bcp import logging

env = "TESTING"
USER: str = os.getenv('')
HOST: str = "localhost"
DBNAME: str = "AdventureWorks2019"
TARGET_DBNAME: str = "CockroackEDW"


SOURCE_SCHEMA: str = "Sales"
SOURCE_TABLE_MAPPING: tuple = (
    "customer",
    "creditcard",
    "SalesOrderDetail",
    "Store",
    "SalesTerritory",
    "SalesPerson",
    "CountryRegionCurrency",
    "SalesReason",


)


TARGET_SCHEMA: str = "Sales"
TARGET_TABLE_MAPPING: tuple = ("customer", "creditcard", "SalesOrderDetail")

password: str = os.getenv('')
loaded_table_list = []
error_loaded_table_list = []


# DB load caller
source_sqldb = DB(user=USER, db=DBNAME, host=HOST, password=password, env=env)
target_sqldb = DB(user=USER, db=TARGET_DBNAME, host=HOST, password=password, env=env)


def load_ops() -> list[list]:
    for table in SOURCE_TABLE_MAPPING:
        logging.info(f"Loading:{table}")
        df = source_sqldb.to_pandas(
            sql="SELECT * FROM {}.{}".format(SOURCE_SCHEMA, table)
        )

        if target_sqldb.to_sql(df=df, method="replace", name=table) == None:
            loaded_table_list.append(table)
        else:
            error_loaded_table_list.append(table)
        del df

    return logging.info(
        f"loaded list :{loaded_table_list},Error list: {error_loaded_table_list}"
    )


if __name__ == "__main__":
    load_ops()
