# Ternary operators
good_credit = True
High_score = True

message = "Eligible" if good_credit and High_score else "Not Eligible"
print(message)


# Example 2: 

def int_validation(value:int):
  #  value=int(input("Enter a value :"))
    return print(f'an integet {value} was inputted') if isinstance(value, int) else print(f'check value entered')

# Using Match Case Statement

"""
Assuming the variable below is geting variable paramaters or a column with multiple values
"""

Value = "One"
match Value:
    case "one":
        result = 1
    case "two":
        result = 2
    case "three":
        result = 3
    case "four":
        result = 4
    case "three" | "four":
        result = 5
    case _:  # This typically used for default
        result = 1
print(result)

"""
 Using regular If and Elif Statement
"""

# # chain operators
# age = int(input(">>"))
# if 18 <= age < 36:
#     print("Qualified for undergraduate")
# elif 36 < age < 45:
#     print("Qualified for graduate")
# else:
#     print("Face your biz development")
