import re


test_list = [1, 2, 3, 4, 5, 6, 7, 8]


def filterFunc(x):
    if x % 2 == 0:
        return True
    else:
        return False


def filterAlpha(x):
    if x.isalpha():
        return True
    else:
        return False


def filterupperCase(x):
    if x.isupper():
        return True
    else:
        return False

# This can be implemented for a lot of scenarios, islower,isdigit etc...


# Implement False operations
result = list(filter(filterFunc, test_list))

print(result)


alpha_test = 'an9YK4ET7GjnPWmgjsyP2JNV0D'
result1 = list(filter(filterAlpha, alpha_test))

print(result1)


result2 = list(filter(filterupperCase, alpha_test))

print(result2)

"""=============================================================
Mapping Function Opetations
================================================================"""


def squareFunc(x):
    return x**2


def letterGrading(x):
    if x > 70:
        return "A"
    elif x < 70 & x > 60:
        return "B"
    elif x < 60 & x > 50:
        return "C"
    elif x < 50 & x > 40:
        return "E"
    else:
        return "F"


def main():
    result3 = list(map(squareFunc, test_list))

    print(result3)

    gradescore = [56, 78, 89, 34, 90, 23, 87, 98, 45]

    results4 = list(map(letterGrading, gradescore))

    print(results4)


if __name__ == "__main__":
    main()
