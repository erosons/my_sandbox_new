# Appending items to a list
from audioop import reverse
import numbers
from pkgutil import extend_path
from turtle import position


thislist = ['apple', 'banana']

thislist.append('pawpaw') > append at the end of the list

# Insertt items to list as specify postion

thislist.insert(2, graple)

# Removing from list
thislist.pop(1) = > removes from a specific position and value
when nothing is in specified pop removes removes the last value

del thislist[0] = > removes the specified index
del thislist = > dele the entire list
clear() = > empty the list

List comprehension quick way to create a list base on numbers

mylist = [x for x in thislist if 'e' in x]


# Filter and expression based on
newlist[x if != x 'banana', else for x in fruits]

# Copy a list to another list

thislist2 = thislist.copy()

# Joing list
- append()
- extend
- list + list 2

# Reversing a list
thislist.reverse() = > ['e', 'd', 'n', 'u', 'T', ' ', 'o', 'l', 'l', 'e', 'H']


# Updating Value in List

thislist['e'] = 'y'

# Searching for a Value
newlist.index(4) = > return value in that position

# Sort a list
newlist.sort() ascending
newlist.sort(reverse=True)

# create a new list from a sorted list

newlist2 = sorted(old_list, reverse=True)


# Adding Array
y = np.array([4, 5, 7, 99, 3, 4, 5])

arr = np.array([1, 2, 3, 4, 5, 97, 7])

ax = np.add(y, arr)
= > array([5,   7,  10, 103,   8,  11,  11])
