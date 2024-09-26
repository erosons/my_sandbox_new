
"""
Collections is an extention of default data structure in python
Default:
 - List => which immutable
 - Tople => which fixed and immutable
 - return unique values unorderable
 - dictionary key-value unodered list
"""

# 1. NameTuple : Helps give meaning to values within a tuple compare to tradition that calls values with indexes

# Example of Traditional Tuple

from collections import OrderedDict
from collections import Counter
from collections import defaultdict
from collections import namedtuple
from itertools import tee


trad_tuple = (1, 2)
print(trad_tuple)

# to call values within the tuple with indexes, might really not be helpful in complex scenario or when transferring
# project to someone else as shown below,

print(trad_tuple[0], trad_tuple[1])


# Using NamedTuple

location = namedtuple("location", "longitude latitude")
"""
Note => the tuple here is Location, but we have named the values in the tuple, this is a class instantiation
"""
# Calling object of that class

Location_1 = location(17, 18)

print(Location_1)
print(Location_1.latitude, Location_1.longitude)


# Another example

# This is comparism of Objects
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
p3 = Point(x=4, y=3)
p4 = Point(x=1, y=2)
print(p1 == p2)
print(p3 > p4)

""
""

"""=================================================================================================
2. # defaultdict : this can help initialize default value to key even when they have not been initialized
================================================================================================="""


fruits = ["apple", "grape", "orange", "apple", "orange", "apple", "banana"]

fruitCounter = {}

# Initializing a counter on this list without putting a check control in place with result in error


# count the elements in the list
# This will produce an error, If the statement is applied , reason because the dictionary key is not let initialized
for fruit in fruits:
    if fruit in fruitCounter.keys():
        fruitCounter[fruit] += 1
    else:
        fruitCounter[fruit] = 1

# print the result
for (k, v) in fruitCounter.items():
    print(k + ";" + str(v))


"""
Alternatively to initializing a default value instead of using, 
IF statement a shown above we can use a defaultdict
"""
fruitCounter2 = defaultdict(int)
# We can also use a lambda :1 or anyvalue can be passed as default value  as the factory default value
# This will initialize default key  value to zero, care has be taken here

for fruit in fruits:
    fruitCounter2[fruit] += 1

# print the result
for (k, v) in fruitCounter2.items():
    print(k + ";" + str(v))


"""=================================================================================================
COUNTER from colllections: can is a superb way to count instead going through all the process above
================================================================================================="""


class1 = ["sam", "bob", "jenny", "kunle", "sam", "jenny", "bob", "sam"]

class2 = ["samson", "bobby", "jenny", "kunle", "samson",
          "jenny", "bobby", "samson", "mario", "peace", "prosper"]


# count item in the list

c1 = Counter(class1)
c2 = Counter(class2)
w= 'Mississippi'

print(Counter(sorted(w)))

print(c1, c2)
print(f'there is {c1["bob"]} Bob in class of', sum(c1.values()))

# TODO combining dictionaries using the update method

c1.update(c2)

print(f'there is {c1["bob"]} Bob in class of', sum(c1.values()))

# TODO Finding the most common key in the dictionary and return the top three in desc order

print(c1.most_common(3))


# TODO Substracting from the counter class, this method takes an iterable => list or mapping

c1.subtract(class1)
print(c1.most_common(3))


# TODO :comparing the counter class to return what is common
print(c1 & c2)

""
""
""
"""=================================================================================================
ORDERED DICTIONARY  => OrderedDict: The regular dictionary in python doesn't keep the order items , OrderedDict helps solve the issue
================================================================================================="""


# list of a sport teams with wins and losses

sportTeams = [
    ("Royals", (18, 12)), ("Sky", (14, 12)), ("Athelo", (17, 9)),
    ("Mikey", (19, 12)), ("Flyer", (25, 12)), ("Dianamo", (12, 13)),
]

sorteditem = sorted(sportTeams, key=lambda x: x[1][0], reverse=True)
print(sorteditem)

# TODO : To create an ordered dictionary of items

teams = OrderedDict(sorteditem)
print(teams)

# TODO : Use popitem to remove item from the dictionary ,FIFO when set to False and LIFO when set to True

wl, ls = teams.popitem()

print("Top team", wl, ls)


# TODO : Equality testing of OrderedDict vs regularDict

a = OrderedDict({"a": 1, "b": 2, "c": 3, "d": 4})
b = {"a": 1, "b": 2, "d": 4, "c": 3}
c = OrderedDict({"a": 1, "b": 2, "c": 3, "d": 4})
d = OrderedDict({"a": 1, "b": 2, "d": 4, "c": 3})

print("Equality Test", a == b)
print("Equality Test", a == c)
print("Equality Test", a == d)
