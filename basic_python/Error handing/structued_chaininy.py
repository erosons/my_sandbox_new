from typing import Optional,Generic,TypeVar,Callable

T=TypeVar('T')
U=TypeVar('U')

class Maybe(Generic[U,T]) :
    def __init__(self, value: T)->U:
        self.value = value

    def and_then(self, func):
        if self.value is None:
            return Maybe(None)
        else:
            return Maybe(func(self.value))

# Example functions
def parse_int(s):
    try:
        return int(s)
    except ValueError:
        return None

def double_if_even(n):
    if n % 2 == 0:
        return n * 2
    else:
        return None

# Usage example using Maybe class
result = Maybe("42").and_then(parse_int).and_then(double_if_even)
print(result.value)  # Output will be 84

# Chaining with a non-integer input
result = Maybe("hello").and_then(parse_int).and_then(double_if_even)
print(result.value)  # Output will be None
