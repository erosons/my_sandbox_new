
#  The *number indicate the function the parameter can take multiple attributes


def return_value(*numbers):
    # *number will only return a tuple
    # numbers can return a list
    total = 1
    for number in numbers:
        total *= number
    return total


print(return_value(1, 2, 3, 4, 5, 7))

print("xxargs initialized", __name__)
