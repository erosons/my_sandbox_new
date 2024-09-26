import numpy as np

array = np.arange(8).reshape(2, 4)
#  This returns booleans for values greater 6 in the array
index_boolean = array < 3
print(index_boolean)

# while this returns the values that are/is >6
print(array[index_boolean])
# This returns sum of the values in array  above
array1 = np.sum(array)
print(array1)

# This returns sum of True values in array  above, Note the True vales are regarded as 1 and False as 0
array1 = np.sum(index_boolean)
print(array1)

array1 = np.median(index_boolean)
print(array1)

array1 = np.average(index_boolean)
print(array1)
