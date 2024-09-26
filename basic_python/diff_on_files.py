import pandas as pd


df1 = pd.DataFrame(
    {
        "Name": [
            "Jtestn",
            "Mike",
            "Smith",
            "Wale",
            "Marry",
            "Tom",
            "Menda",
            "Bolt",
            "Yuswa",
        ],
        "Age": [23, np.nan, 12, 34, 27, 44, 28, 39, 40],
    }
)
df2 = pd.DataFrame(
    {
        "Name": [
            "Jtestn",
            "Smith",
            "Wale",
            "Tom",
            "Menda",
            "Yuswa",
        ],
        "Age": [23, 12, 34, 44, 28, 40],
    }
)

"""
Getting difference between files

Implementation 1
"""

df_1notin2 = df1[
    ~(df1["Name"].isin(df2["Name"]) & df1["Age"].isin(df2["Age"]))
].reset_index(drop=True)

"""
Getting difference between files

Implementation 2
"""

df1[~df1.apply(tuple, 1).isin(df2.apply(tuple, 1))]
