import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


path=Path('Monthly reports/ratings.csv')
rating_df=pd.read_csv(path)
# to check memory usage
memoryusage1=rating_df["userId"].memory_usage()
memoryusage2=rating_df["movieId"].memory_usage()
memoryusage3=rating_df["rating"].memory_usage()
memoryusage4=rating_df["timestamp"].memory_usage()
memoryusgae=rating_df.memory_usage().sum()

print(rating_df.shape)
# to check memory usage
print(memoryusgae)
print(memoryusage1)
print(memoryusage2)
print(memoryusage3)
print(memoryusage4)

# Working with iter() and Next()
"""x=[1,2,3,4]
x=iter(x)
print(next(x))
print(next(x))"""

rating_scores=list(rating_df["rating"].unique())
print(sorted(rating_scores, reverse=True))

# creating a rating keys above dictionary
rating_dict={}
rating_dict={x:0 for x in sorted(rating_scores)}
print(rating_dict)

average_bytes=0
counter=0
#  Sizing through a large datasets
for index,chunks in enumerate(pd.read_csv(path,chunksize=1000000),start=1):
    average_bytes+=chunks.memory_usage().sum()
    for i in rating_scores:
        counter=len(chunks[chunks["rating"]==i])
        rating_dict[i]+=counter
        aver_bytes=average_bytes/index
print(f'Total number of chunks:{index}')
print(f'Average bytes per loop :{aver_bytes}')
print(rating_dict)

print(sum(list(rating_dict.values()))==len(rating_df))

