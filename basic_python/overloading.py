from functools import singledispatch
from numbers import Number



@singledispatch
def add(arg):
    return "Unknown type ."

@add.register
def _(arg: Number):
    return arg + arg

@add.register
def _(arg: str):
    return f' A collections of {len(arg)} elements'

@add.register(list)
@add.register(tuple)
@add.register(set)
def _(arg):
    return f' Total {sum(arg)}'



print(add([1,2,3]))
print(add('Samson'))