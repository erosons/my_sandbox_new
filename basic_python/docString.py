"""
Harnessing built documentation power in python  .__doc__
This can be called with method, function and classes
"""

import collections
from pdb import line_prefix
from xml.sax.handler import property_lexical_handler

"""
print(collections.__doc__)

returns 
=======
* namedtuple   factory function for creating tuple subclasses with named fields
* deque        list-like container with fast appends and pops on either end
* ChainMap     dict-like class for creating a single view of multiple mappings
* Counter      dict subclass for counting hashable objects
* OrderedDict  dict subclass that remembers the order entries were added
* defaultdict  dict subclass that calls a factory function to supply missing values
* UserDict     wrapper around dictionary objects for easier dict subclassing
* UserList     wrapper around list objects for easier list subclassing
* UserString   wrapper around string objects for easier string subclassing

"""

# Custom documentation


def myFunction(arg1, arg2):
    """
    MyFuction(arg1, agr2) does this xy and z process 

    Parameters:
    arg1 : the first argument . Does this x and y
    agr2 : second argument does this x, y and z

    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


# Docstring best practices  pep0257
   # Encloses docstring in triple quotes
   # First line should be summary sentence of functionality
   # Modules: list important classes , functions, exceptions
    # Classes: List important methods, statics, enums

  # For functions
    # -- list paratmeters and explain each , one per line
    # -- if there's a return value , then list it; otherwise
    # ---if the fuction raises exceptions , mention those


if __name__ == "__main__":
    main()
