"""=========================
Implementing Enumeration
========================="""
# This class allows you to assign  readable names to constant in your program

from enum import Enum, unique, auto


@unique
class Fruits(Enum):
    # To ensure key values are are unique, because there could be scenario where the same
    # values passed to the key which is aloows we can can call @unique decorator and use it to wrap the class
    # tomato and banana get flagged  because of thier values and Note because of the decorator that was passed
    Orange = 1
    Mango = 2
    Guava = 3
    tomato = 4
    # banana = 4
    pear = auto()  # This method allows you to automatically assign values to enums


def main():

    # TODO: enums allows us to have human readable values and types
    print(Fruits.Orange)
    print(type(Fruits.Orange))
    print(Fruits.Orange.value)
    print(repr(Fruits.Orange))

    # TODO: enums have names and values
    print(Fruits.Orange.name, Fruits.Orange.value)

    # TODO: print the auto generated values
    print(Fruits.pear.value)

    # TODO: enums are hashable - can be used as keys
    myFruits = {}
    myFruits[Fruits.pear] = "Testing key value with enums"

    print(myFruits[Fruits.pear])


if __name__ == "__main__":
    main()
