<<<<<<< HEAD:Engineering/Personal_Implemenation/tutorial/Basic_python/map_dataframe.py
x=[x for x in range(10)]

def numbers(x)-> list:
  return x**2


=======
import re
# https://www.learnpython.org/en/Map%2C_Filter%2C_Reduce


<<<<<<<< HEAD:Engineering/Personal_Implemenation/tutorial/Basic_python/filter_map.py
test_list = [1, 2, 3, 4, 5, 6, 7, 8]


def filterFunc(x):
    if x % 2 == 0:
        return True
    else:
        return False


def filterAlpha(x):
    if x.isalpha():
        return True
    else:
        return False


def filterupperCase(x):
    if x.isupper():
        return True
    else:
        return False

# This can be implemented for a lot of scenarios, islower,isdigit etc...


# Implement False operations
result = list(filter(filterFunc, test_list))

print(result)
========
>>>>>>> 10086af96351d91d79ea73a49bfe26ae8db9fa75:Engineering/basic_python/map_dataframe.py
y=list(map(numbers,x)) '->' [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#  Takes input and apply a transformation to it, it can be used to apply a function to a series in a dataframe

import numpy as np
import pandas as pd
xy=pd.DataFrame(np.array([[x for x in range(4)],[3,5,7,6],[3,90,9,89]]),columns=['a', 'b', 'c','d'])

"""
Output
"""
a 	b	  c	  d
0	  0	  1	  2
1	  3	  5	  7
2	  3	  90	9	


#Call the function above and apply it to the series

xy['d']=xy['d'].apply(lambda x:numbers(x))
<<<<<<< HEAD:Engineering/Personal_Implemenation/tutorial/Basic_python/map_dataframe.py
xy['d']=xy['d'].map(lambda x:numbers(x))
=======
xy['d']=xy['d'].map(lambda x:numbers(x))
>>>>>>>> 10086af96351d91d79ea73a49bfe26ae8db9fa75:Engineering/basic_python/map_dataframe.py
>>>>>>> 10086af96351d91d79ea73a49bfe26ae8db9fa75:Engineering/basic_python/map_dataframe.py
