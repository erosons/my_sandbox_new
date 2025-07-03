#In Python, a generator is a function that returns an iterator that produces a sequence of values when iterated over.
#Generators are useful when we want to produce a large sequence of values, but we don't want to store all of them in memory at once.

from sys import getsizeof  # use to get the byte size of an object

# these performs lazy evaluation, i.e it only returns and evaluate require values.
value = (x * 2 for x in range(1000000000000))
print(value)
print(getsizeof(value))
for values in value:
    print(values)
    if values == 100000:
        break

#Another Scenario use Case for genrator
x={'col':[1,2],'col2':[2,3]}
df=pd.DataFrame(x)
def gen(x):
    for i,rows in x.iterrows():
       yield rows

closure=gen(df)

#Each time this function is called is yield a new row
next(closure)