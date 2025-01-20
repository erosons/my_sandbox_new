# What is Array in python => Hold Homogenous/static collection similiar data types

# Python based array or numpy base array are Static or homogenous

# Using Python native array
# ============================

import array
import numpy as np
import random

my_array = np.array([x for x in range(10)])
my_array = > array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

my_array1 = np.arange(10)
my_array1 = >array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Stepping in array:
myarray = np.arange(0, 20, 2) = > array([0,  2,  4,  6,  8, 10, 12, 14, 16, 18])


my_array2 = np.random.randn(5)
my_array2 = > array([1.18962991, -0.96403018, -1.00648032, -0.09231352,  1.95320253])
np.random.random((2, 3)) = > array([[0.13091379, 0.85278236, 0.01980667],
       [0.55850634, 0.25155371, 0.89543369]])


# Working with Dimensional array
np.zeros((2, 2)) = > array([[0., 0.],
                           [0., 0.]])

np.full((2, 2), 5) = > array([[5., 5.],
                           [5., 5.]])

np.ones((2, 2)) = > array([[1., 1.],
                           [1., 1.]])

np.eye(3) = > Indentity matrix = > array([[1., 0., 0.],
                                         [0., 1., 0.],
                                           [0., 0., 1.]])

# Customs Dimensional

np.array([[1, 2, 3, 4, 5], [5, 5, 6, 67, 7]])


# deleting from Array

arr = np.array([1, 2, 3, 4])
arr
np.delete(arr, 1) = > array([1, 3, 4])

# Search in Numpy array returns the index of the search value.
y = np.array([[1, 2, 3, 4, 5], [5, 5, 6, 67, 7]])

np.where(y == 4)


# Sorting of Numpy array .
y = np.array([4, 5, 7, 99, 3, 4, 5])

np.sort(y)


# Using Python native array
# ============================


# Python Built Array
# TypeCodes available for array module for various data types :  https://docs.python.org/3/library/array.html
"""
i => integer type int 2 bytes
b => Signed char int 1 bytes
B => unsigned
f => float type float 4 bytes
d => float type  float  8 bytes
Q => unsigned long long int 8 bytes
L => unsigned long int 4 bytes
i => signed type int 2 bytes
H => unsigned short int 2 bytes
u => wchar_t  Unicode characters 2 bytes
"""

array2bytes = array.array('b', [x for x in range(10)])

print(array2bytes) = > array('b', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(array2bytes.itemsize) = > 1 bytes minimum
print(array2bytes.typecode) = > 'b'
print(len(array2bytes.typecode)) = > 10

for i in range(0, len(array2bytes):
    print(array2bytes[i], end=" ")= > array2bytes


array('d', [19999999.19, 1111111.23])
print(array2bytes.itemsize)=> 8 bytes minimum
print(array2bytes.typecode)=> 'd'
