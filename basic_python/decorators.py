
"""
Using A decorator
"""


def arithmetric_geometric(func):

    def inner(*arg):
        _geometric = func(*arg) / (arg[1] - 1)

        return _geometric
     
    return inner


@arithmetric_geometric
def arithmetic_progression(*args):

    arithmetic_progression = a + (n - 1) * d

    return arithmetic_progression


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
