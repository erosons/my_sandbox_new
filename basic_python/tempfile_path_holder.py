import tempfile
import pandas as pd
from datetime import datetime

with tempfile.TemporaryDirectory() as dir:
    df = pd.read_excel(r'C:\Users\S.Eromonsei\sampleSuperstore.xls')
    df["lastRefreshDate"] = datetime.now()
    parquet_path = f"{dir}/Unbilled.parquet"
    print(parquet_path)
    df.to_parquet(parquet_path,index=False)
    df2=pd.read_parquet(parquet_path)
    print(df2.head(5))


import os

filepath=os.path.join("C:/Users/S.Eromonsei/Downloads/Unbilled", "Unbilled.parquet")
os.makedirs(filepath, exist_ok=True)