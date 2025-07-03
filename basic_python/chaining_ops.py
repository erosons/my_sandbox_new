def and_then(value, func):
    """
    Applies function `func` to `value` if `value` is not None.
    Returns None if `value` is None.
    """
    if value is None:
        return None
    else:
        return func(value)

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

# Usage example
result = and_then("42", parse_int)
result = and_then(result, double_if_even)
print(result)  # Output will be 84

# Another usage with string that fails to parse as int
result = and_then("hello", parse_int)
result = and_then(result, double_if_even)
print(result)  # Output will be None because parse_int fails
