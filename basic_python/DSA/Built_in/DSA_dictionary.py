
# Changes in version 3.7 Dictionary is now ordered before it use to unordered and changeable

# 1. Duplicate not Allowed
from email.errors import InvalidBase64CharactersDefect
from pandas import value_counts


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
# Latest will override
= > {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# Get item from a dictionary

thisdict.get("modeller", None) returns None if it doesn't find the key
thisdict["model"]

# Change item in Dictionary or Add item
thisdict["year"] = 2018
thisdict.update({"year": 2020}) = > Either method will change the year values

# Removing items
thisdict.pop('model') / del thisdict['model'] = > removes key and value
del thisdict = > delete the entire dictionary
thisdict.popitem() = > removes the last Inserted


# Get keys and Values()
for x in thisdict.values():
    = > values
    print(x)

for x in thisdict.keys():
    = > keys
    print(x)

# Copy dictionarys

mydict = thisdict.copy() = > a new dictonary
mydict = dict(thisdict)
