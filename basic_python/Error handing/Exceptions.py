from timeit import timeit

try:
    age = int(input("Enter your age\n"))
    factor = 10 / age
    print("Happy Birthday")
    print(factor)
#  Dealing with multiple possible errors
# You can input as many possible errors that can occur in your program and catch them ahead of time
# except (ValueError, ZeroDivisionError):
#     print("You entered an invalid input")
except (ValueError, ZeroDivisionError) as e:
    print("You entered an invalid input".format(e))
finally:
    print("Your input was succesful")
