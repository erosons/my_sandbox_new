from sqlalchemy import create_engine
import pandas as pd
from time import sleep

class PostgresDB:
    def __init__(self, dbname, user, password, host, port):
        # Creating the connection string
        self.engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')

    def df_read_from(self, sql, chunksize=None):
        """Reads data from the database in chunks and processes it."""
        try:
            for chunk in pd.read_sql(sql, self.engine, chunksize=chunksize):
                sleep(2)  # Delay for demonstration; typically not advisable in production code
                print(chunk)
                # Example of reloading data to the database, needs clear definition
                self.pandas_data_loader(chunk, "invoices", schema="public", chunksize=1, mode="replace")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.close()

    def pandas_data_loader(self, dataframe, table_name, schema=None, chunksize=None, mode=None):
        """Loads data from a DataFrame back into a database table."""
        if dataframe.empty:
            print("Empty DataFrame, nothing to load to the database.")
            return
        try:
            dataframe.to_sql(table_name, con=self.engine, schema=schema, chunksize=chunksize, if_exists=mode, index=False)
        except Exception as e:
            print(f"Failed to write to table {table_name}: {e}")

# Usage example
if __name__ == "__main__":
    sql="SELECT * from public.invoices;"
    pg = PostgresDB("Dbt", "sa", "test", "172.25.0.1", "5432")
    df= pg.df_read_from(sql, chunksize=10)
    #pg.pandas_data_loader(df, schema="public",batch=1,mode="replace")