from itertools import cycle, dropwhile
import itertools
import itertool

gradescore = [56, 78, 89, 34, 90, 23, 87, 98, 45]


cycle1 = itertools.cycle(gradescore)
"""
Cycle1 returns an iterable objects which can be called using next
"""
# print(cycle1)

# This will return every next itemin the obj and when the end is reached it starts all over again
print(next(cycle1))
print(next(cycle1))
print(next(cycle1))
print(next(cycle1))
print(next(cycle1))
print(next(cycle1))
print(next(cycle1))
print(next(cycle1))
print(next(cycle1))
print(next(cycle1))
print(next(cycle1))
print(next(cycle1))

# Repeats and increment/decrement th number by the step value
cycle2 = itertools.count(10, -1)
print(next(cycle2))
print(next(cycle2))
print(next(cycle2))
print(next(cycle2))


# The itertools method aggregate values cumulatively  and if max argumnet is passed as well, it returns the max value after conparing against next value

cycle3 = itertools.accumulate(gradescore)

print(list(cycle3))

# where max is passed, checks for the max value comparing  to the next value in the sequence

cycle4 = itertools.accumulate(gradescore, max)

print(list(cycle4))

# The itertool method Chian(), is used to crete a list from the combination of two arguments

cycle5 = itertools.chain('1234', 'ABCD')

print(list(cycle5))

# #The itertool method islice(), is used slice an argument based on the slice point

cycle6 = itertools.islice('1234', 2, None)

print(list(cycle6))

# #The itertool method dropwhile(), is used to drop prior member/elements of when the predicate is False

cycle7 = itertools.dropwhile(lambda x: x < 90, gradescore)

print(list(cycle7))


# #The itertool method dropwhile(), remove preceeding elements once a predicate True

cycle7 = itertools.takewhile(lambda x: x < 90, gradescore)

print(list(cycle7))
