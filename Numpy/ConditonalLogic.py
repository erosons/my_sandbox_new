import numpy as np

# This check the array, for the logic of x%2==0 id true and return 1 and false returns 0

x = np.array([np.arange(11, 20, 1), np.arange(
    1, 10, 1), np.arange(21, 30, 1)])
print(x)
y = np.where(x % 2 == 0, 1, 0)
z = np.where(x // 2 == 1, 1, 0)
print(y, z, sep="\t")
