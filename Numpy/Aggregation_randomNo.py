#  when dealing large data array with efficient memory usage
#  Numpy is more effient than list in the sense that its datatype are unique and memory allocation is unique and data are accessed faster
import numpy as np

#  This operations cannot be performed in a regular list except by iterating or using a lambda function
array = np.arange(4)*2
print(array)

# These both returns a unit 4x4 identity matrix
print(np.eye(4))
print(np.identity(4))

# This returns an arange of 8 and change it into a 2x4 matrix
print(np.arange(8).reshape(2, 4))

# This return zeros or ones in watever shape and their datatype is det by the input
print(np.zeros((3, 4), dtype=float))
print(np.ones((3, 4), dtype=float))
print(np.ones((5), dtype=float))

# This allows you to return fill have of yours
print(np.full((3, 4), 4, dtype=float))

# To create 2D  array
print(np.array([(1, 2, 3), (2, 3, 4)]))

# To create 3D  array
print(np.array([(1, 2, 3), (2, 3, 4), (5, 6, 7)]))

# This return randoms array in watever shape and their datatype is det by the input
print(np.random.randint((3, 4)))

# This return randoms array in watever shape and their datatype is det by the input
print(np.random.random((3, 4)))

#  To get randomly normal distributed values with a spread or std as shown below
y = np.random.normal(size=10, scale=0.5)
print(y)

# indexing through
array = np.random.random((3, 4))
print(array[0, 0])  # Returns first row first column
print(array[0, 1])  # Returns first row second column

# converting a data type of a data read off from or extracted from a data source
data = [1, 2, 3, 4, 5, 6, 7]
data1 = np.array([data, data, data])
array1 = np.array(data, dtype=int)
array2 = np.array(data, dtype=float)
array3 = np.array(data, dtype=str)
print(array1, array2, array2, sep="\n")
print(array1.sum(), array2.mean(), array2.std(), sep="\n")
# When axis=1 this column calculations
print(data1.sum(axis=1), data1.mean(axis=1), data1.std(axis=1), sep="\n")
"""[28 28 28]
[4. 4. 4.]
[2. 2. 2.]"""
# When axis=0 this column calculations
data1 = np.array([data, data, data])
print(data1.sum(axis=0), data1.mean(axis=0), data1.std(axis=0), sep="\t")
"""[[1 2 3 4 5 6 7]
 [1 2 3 4 5 6 7]
 [1 2 3 4 5 6 7]]
[3  6  9 12 15 18 21][1. 2. 3. 4. 5. 6. 7.][0. 0. 0. 0. 0. 0. 0.]"""
data = np.array([1, 2, 3, 4, 5, 6, 7])
print(data.sum(axis=0))

# to generate random matrix  of any size, and remember the scale is the std
y = np.random.normal(size=(10, 10), scale=0.5)
print(y)

# To generate random matrix of integer of any size
y = np.random.randint(-8, 10, size=(10, 10))
print(y)
