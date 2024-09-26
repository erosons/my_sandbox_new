import random
import string

# To generate random number of x range for float
for i in range(2):
    print(random.random())

# To generate random number of x range for integers
for i in range(2):
    print(random.randint(1, 20))

# To generate one choice random number from this  list range
myList = [*range(30)]
print(random.choice(myList))

# To generate three choices random number from this  list range, k ---- can be 1 to nth value.
print(random.choices(myList, k=11))

# This can be used as password generator
mylist2 = "absbdunefysddgdbedncgdnc"
print("".join(random.choices(mylist2, k=4)))

# To reshuffle numbers
random.shuffle(myList)
print(myList)

# Generating a password  with alpha and Numeric
print("".join(random.choices(string.ascii_letters + string.digits, k=4)))

# Create a class that generate two random integers that change everytime you call it


class RandGen:
    def radomgenrator(self):
        FirstNum = random.randint(1, 5)
        SecondNum = random.randint(5, 7)
        print(FirstNum, SecondNum)


Myrand = RandGen()
Myrand.radomgenrator()
