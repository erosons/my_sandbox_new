from timeit import timeit

code1 = """
def coversion(age):
    if age <= 0:
        # Do not raise unneccessary error becos of execution time
        raise ValueError("Age can not be 0 or less") 
    return 10/age


try:
    coversion(0)
except ValueError as error:
    pass
"""
print("firstcode:", timeit(code1, number=10000))

code2 = """

# Another level of implementation, instead of raising value Error

def coversion(age):
    if age <= 0:
       return None
    return 10/age


xfactor=coversion(0)
if xfactor==None:
    pass
"""
print("firstcode:", timeit(code2, number=10000))
