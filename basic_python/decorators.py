def con_upperCase(text: str) -> str:
    return text.upper()


def con_lowerCase(text: str) -> str:
    return text.lower()


# Calling a function from another function


def greeting(func) -> None:

    greeting = func("I am a programmer")
    print(greeting)

    greeting(con_upperCase)

    greeting(con_lowerCase)


# Using functions an obj, basically involve passing function as an obj/ creating an instance from it
lower_str = con_lowerCase

lower_str("My name is Samson")

"""
Return Function from a function Example 1
"""


def create_adder(x):  # step2
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)  # step1
add_15(10)

"----> return result----> 25  The first function calls in the inner function"

"""
Return Function from a function Example 2
"""


def create_adder():
    return print("Hello World")  # execution step8


def hello_decorator(func):  # execution step2
    print(" I am a decorator")  # execution step 3

    def inner():  # execution step4
        print("This is the wrappper")  # execution step 6

        func()  # execution step7

    return inner  # execution step5


decorator_function = hello_decorator(create_adder)  # execution step1

decorator_function()  # execution step9


"""
Decorator implementation for the above implementation
"""


@hello_decorator
def create_adder():
    return print("Hello World")


"""
Using A decorator
"""


def arithmetic_decorator(func):
    print("transform function to arithmetic progression")

    def inner(*args, **kwargs):
        print("inner wrapper for arithmetic function")

        _geometric_progression = func(*args, **kwargs) / (n - 1)

        return _geometric_progression

    return inner


@arithmetic_decorator
def arithmetic_progression(*args):

    aithmetric_progression = a + (n - 1) * d

    return aithmetric_progression


a, n, d = 5, 4, 2
arithmetic_progression(a, n, d)


"""
Executing Chain Decorator
"""


def decor1(func):
    def inner():
        x = func()
        return x * x

    return inner


def decor(func):
    def inner():
        x = func()
        return 2 * x

    return inner


@decor1
@decor
def num():
    return 10


print(num())
