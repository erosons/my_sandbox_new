import logging
from os import name
"""Writing logs into a file"""
logging.basicConfig(filename='new.log', level=logging.DEBUG,
                    format='(name)s:%(asctime)s:%(levelname)s:%(message)s')


def add(x, y):
    """
    :param x value1
    :params y value2
    """
    return x+y


def sub(x, y):
    """
    :param x value1
    :params y value2
    """
    return x-y


def multiply(x, y):
    """
    :param x value1
    :params y value2
    """
    return x*y

    # USING PRINT LOGGING to display on the console
x: int = 10
y: int = 2

add_result = add(x, y)
print('{}+ {} = {}'.format(x, y, add_result))

add_sub = sub(x, y)
print('{}- {} = {}'.format(x, y, add_sub))

add_multiply = multiply(x, y)
print('{} * {} = {}'.format(x, y, add_multiply))

# USING DEBUG LOGGING

add_result = add(x, y)
logging.debug('{}+ {} = {}'.format(x, y, add_result))

add_sub = sub(x, y)
logging.debug('{}- {} = {}'.format(x, y, add_sub))

add_multiply = multiply(x, y)
logging.debug('{} * {} = {}'.format(x, y, add_multiply))

# USING WARNING LOGGING
add_result = add(x, y)
logging.warning('{}+ {} = {}'.format(x, y, add_result))

add_sub = sub(x, y)
logging.warning('{}- {} = {}'.format(x, y, add_sub))

add_multiply = multiply(x, y)
logging.warning('{} * {} = {}'.format(x, y, add_multiply))
