import numpy as np
array = np.array([1, 2, 3])
print(array)
print(array.shape)
print(array.reshape(3, 1))
print(array.sum(axis=0))

y = np.array([1, 2, 3, 4, 5])
x = np.array([1, 2, 3, 4, 5])
yx = np.array([x, y])
print(yx.transpose())
""""
y = [x*2 for x in range(5)]
x = [x**3 for x in range(5)]
ax = [y, x]
print(ax)
yz = [list(i) for i in zip(*ax)]
print(yz)"""
