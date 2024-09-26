import numpy as np
import time

# Timing a transpose operations with regular numpy array


def dot_operations(n):
    start_time = time.time()
    y = np.array(np.arange(n))  # watch the brackets can result in an error
    x = np.array(np.arange(n))
    yx = np.array([x, y])
    print(yx)
    zx = yx.transpose()
    print(zx)
    print(yx.dot(zx))
    print(np.dot(yx, zx))
    end_time = time.time()
    duration = start_time-end_time
    return duration


""""
dot_operations(10)

start_time = time.time()
# Timing a performing transpose operations with regular list
y = [x**2 for x in range(30)]
x = [x**3 for x in range(30)]
ax = [y, x]
print(ax)
yz = [list(i) for i in zip(*ax)]
print(yz)
end_time = time.time()
duration1 = start_time-end_time
print(dot_operations(5), duration1)"""

for n in [10, 100, 1000, 100000]:
    list_result = dot_operations(n)
    print(list_result, sep="\t")
