import numpy as np

array = np.array([["samsung", "Microsoft", "IBM", "Spotify"],
                  [1900, 1991, 1992, 1993], [
                 "$431billion", "$631billion", "$731billion", "120billion"]])

# This will only index and slice through row and returns 1st row
print(array[0:1])

# Note the comma this will slice through the row and column returns Microsft
print(array[0:2, 1:4])

#  to return a specific value
print(array[2, 3])
print(array[:, 2:])  # returns
"""
[['IBM' 'Spotify']
 ['1992' '1993']
 ['$731billion' '120billion']]"""

# Reshaping a shape into another shape
newShape = array.reshape(6, 2)
print(newShape)
"""[['IBM' 'Spotify']
 ['1992' '1993']
 ['$731billion' '120billion']]
[['samsung' 'Microsoft']
 ['IBM' 'Spotify']
 ['1900' '1991']
 ['1992' '1993']
 ['$431billion' '$631billion']
 ['$731billion' '120billion']]"""
