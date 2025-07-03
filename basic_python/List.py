# mylist = [0]*100
# mylist = list(range(20))
# print(mylist[::2])

# myList = [1, 2, 3]
# first, second, third = myList
# print(f"{first} and {second} and {third}")
mylist = tuple(range(5))
print(mylist)
first, second, *third = mylist
print(third)
print(first)
print(second)
