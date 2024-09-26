from itertools import zip_longest
import numpy as np


mylist = [1, 2, 3, 4.5]
mylist2 = [6, 7, 9, 8, 10]
# This allow you to combined multiple list
combined_list = list(zip(mylist, mylist2))
print(combined_list)
# This allow you to convert a combined list to a dictionary
print(dict(combined_list))

""" Where list Arguments of Unequal Length
In these cases, the number of elements that zip() puts out will be equal to the length of the shortest iterable.
 The remaining elements in any longer iterables will be totally ignored by zip(), as you can see her
"""
my_new_list=list(zip(range(5),range(10)))
print(my_new_list)

"""
 If trailing or unmatched values are important to you, then you can use itertools.zip_longest() 
"""
my_new_list=list(zip_longest(range(5),range(10),fillvalue=np.nan))
print(my_new_list)
