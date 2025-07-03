import numpy as np

array = (np.array(np.arange(8)))**2
"""[ 0  1  4  9 16 25 36 49]"""

array1 = np.array([array, array*2])
"""[[ 0  1  4  9 16 25 36 49]
 [ 0  2  8 18 32 50 72 98]]"""

# performing a dot operations
array3 = np.dot(array1, array1.reshape(8, 2))
print(array3)
"""[[ 5272  7634]
 [10544 15268]]"""
#  Alternative perorming a dot opeartions 2
print(array1.dot(array1.reshape(8, 2)))

#  performing aggreation on 1D and 2D array
4
