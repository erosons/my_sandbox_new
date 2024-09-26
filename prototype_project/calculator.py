"""
Calculator library containing baisic math operations
"""


from typing import List


def add(first_term: int, second_term: int) -> int:
    return first_term + second_term


def subtract(first_term: int, second_term: int) -> int:
    return first_term - second_term


def multiply(first_term: int, second_term: int) -> int:
    return first_term * second_term


def joiner(xs: List[int], delimiter: str) -> str:
    generated_string: str = ""
    for item in xs:
        if generated_string == "":
            generated_string = str(item)
        else:
            generated_string += delimiter + str(item)
    return generated_string
