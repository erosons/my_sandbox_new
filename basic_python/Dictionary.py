mydict = dict(y=1, x=2, z=3)
print(mydict)
# looping over a dictionary returns the keys
for key in mydict:
    print(key)
# Looping over dictionary to return the key and value
for key in mydict.items():
    print(key)  # this returns a tuple

# Unpacking the tuple
for key, value in mydict.items():
    print(key, value)

# Case study1
# Map a each number in a phone number to its alphabetical
Phone = "8326144931"
Alpha_Map = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
             "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}
"""Output = ""
for single_digit in Phone:
    Output += Alpha_Map.get(single_digit, "Number not found") + " "
print(Output)"""

# Using a comprehension t solve this issue
Output = [Alpha_Map.get(single_digit, "Number not found") +
          " " for single_digit in Phone]
print(Output)

# Using a dictionary Comprehension
values = {}
for x in range(5):
    values[x] = x*2
print(values)

# Using a dictionary Comprehension
value = {x: x*2 for x in range(5)}
print(value)
