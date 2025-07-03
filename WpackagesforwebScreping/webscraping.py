import pandas as pd

df = pd.read_csv(
    "https://www.cdc.gov/coronavirus/2019-ncov/map-data-cases.csv", encoding="latin1")
print(df)
print(df[1:5])
