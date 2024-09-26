mylist = [1, 2, 3, 4]
for letter in enumerate(mylist):
    print(letter[0], letter[1])

# This solution index the list start from 1 , starting point can also be zer
for index, letter in enumerate(mylist, start=1):
    print(index, letter)
