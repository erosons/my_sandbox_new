"""
Finding duplicates in a list
"""

x = [3, 4, 5, 6, 5, 7, 8, 9, 7]
duplicate = None
for i in range(len(x)):
    # O(n^2)  Order of n square
    for j in range(i+1, len(x)):
        print(j)
        if x[i] == x[j]:
            duplicate = None
            print(str(x[i]) + "is a duplicate")
            break


for i in range(len(x)):
    # O(n)  Order of n which is Linear
    if duplicate == x[i]:
        print(i + "is a duplicate")
        break

"time = a*n^2 b*n + c"

"In which case the worse case scenario is considered => n^2"
