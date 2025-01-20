# Tuples are
#  - ordered and immutable/unchangable and allow duplicates values

import this
from numpy import append


d = (1, 1, 2, 4)

# One item tuple has to always be ended with ,
# Without , python will not recognize as tuple

d = (1,)

# Access data from a tuple
y[:2] = > (1, 1)

y[:-1] = >(1, 1, 2)

# Changing Tuple values , by design Tuples are unchangable or immutable(Workaround change to list and back to Tuple)

y = list(d) = > A list

y[1] = 17 = > [17, 1, 2, 4]

x = tuple(y) = > Tuple

# Adding to tuple  using similiar pattern above of converting a list and usind Append()

thistuple = (1, 2, 3, 4)
newtuple = (5,)

thistuple += newtuple

# Unpacking tuples

a, b, c, d = (1, 2, 4, 5,)

# Join two tuples

thistuple = (1, 2, 3, 4)
newtuple = (5,)

thistuple + newtuple = > (1, 2, 3, 4, 5)


# Tuples has only two Methods
thistuple.count() = > how many times the value occured
thistuple.index() = > returns the position of the specified value
