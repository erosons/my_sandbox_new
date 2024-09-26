import re
# https://www.learnpython.org/en/Map%2C_Filter%2C_Reduce


test_list = [1, 2, 3, 4, 5, 6, 7, 8]


def filterFunc(x):
    if x % 2 == 0:
        return True
    else:
        return False


def filterAlpha(x):
    if x.isalpha():
        return True
    else:
        return False


def filterupperCase(x):
    if x.isupper():
        return True
    else:
        return False

# This can be implemented for a lot of scenarios, islower,isdigit etc...


# Implement False operations
result = list(filter(filterFunc, test_list))

print(result)