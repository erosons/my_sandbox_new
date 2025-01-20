"""
Iterating over a list
"""
x = [x for x in range(1, 50)]
divisiby_2 = []
# This is a Linear Operations, the time and space complexity increases linearly
for i in range(len(x)):
    if i % 2 == 0:
        divisiby_2.append(i)

"time = a*n + c"

"In which case the worse case scenario is considered => n^2"
