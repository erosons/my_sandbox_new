myList = [4, 5, 7, 3, 9, 6]
myList.sort(reverse=True)
newlist = sorted(myList, reverse=True)
print(newlist)
print(myList)

#  items is a dictinary that coverted to a list tuple using function sorted()
items = [
    ("Product1", 10),
    ("Product2", 40),
    ("Product3", 20),
    ("Product4", 30)
]


def custom_item(item):
    return item[1]


items.sort(key=custom_item)
print(items)

# better solution to sort &# from lowest to highest

better_soting = items.sort(key=lambda kv: kv[1], reverse=True)
print(better_soting)
