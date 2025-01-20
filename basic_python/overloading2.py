from functools import cache
from typing import overload
from collections.abc import Sequence
from numbers import Number



@overload
def add(arg)-> int:
    return "Unknown type ."

@overload
def _(arg: Number)-> Number:
    return arg + arg

@overload
def _(arg: str)->str:
    return f' A collections of {len(arg)} elements'


def double(input_: int | Sequence[int]) -> int | list[int]:
    if isinstance(input_, Sequence):
        return [i * 2 for i in input_]
    return input_ * 2




print(add([1,2,3]))
print(add('Samson'))