
#  Module provided to be reusable by other must be well documented see pattern below
import random


class RandGen:
    """ this class generates random numbers.    """

    def radomgenrator(self):
        """ has two variables that generates random integer between """
        FirstNum = random.randint(1, 5)
        SecondNum = random.randint(5, 7)
        print(FirstNum, SecondNum)


# Note that """ this a new project""" is used to provide a documentation
# When the project is imported as a module in other project the documentation will tell alot about the projects
randNum = RandGen()
randNum.radomgenrator()
