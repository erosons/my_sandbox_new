# def factorial(n) -> int:
#     if n == 1:
#         return 1
#     print(n)
#     return factorial(n-1)


# factorial(5)

myseq = [0, 1]


def recursion_fib(n) -> list:
    for item in range(n-1):
        current_length = len(myseq)
        nextnumber = myseq[current_length-1]+myseq[current_length-2]
        myseq.append(nextnumber)
        print(myseq)
        return recursion_fib(n-1)


def fibonanci(n):
    if len(myseq) == 1 and n == 1:
        return "qualify for a fib series"
    elif len(myseq) >= 2:
        return recursion_fib(n)
    return None


fibonanci(3)
