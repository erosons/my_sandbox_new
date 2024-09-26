# This indicate multiple keyword argument can be passed into the parameter
# passing keyword argumnet
def user_info(**user):
    return user


myInfo = user_info(
    id=1, name="samson", phone=8030, email="eromonsei.o.samson@gmail.com"
)
print(myInfo)


# Passing multiple arguments
def user_info2(*args):
    result = 1
    for i in args:
        result = result * i
    return result


testingfunc = user_info2(1, 2, 3, 4, 5)

print(testingfunc)


# A proper way to pass argument with a default/kwarg value followed by a variable number of arguments to a function

def kwarg_default_value_args(b=1, **arr):
    return b + arr


# How to enforce a Kwarg and clearly separate it from args in a function.

def kwarg_args_sepa(arr1, arr2, *, b=1):
    return print(1, 2, b=1)
