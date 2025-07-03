items = [
    ("Product1", "orange", 2),
    ("Product2", "Banana", 40),
    ("Product3", "Grape", 3),
    ("Product4", "bread", 4)
]
items.sort(key=lambda item: item[2])
print(items)

# (lambda x:x**2)(2)

# itering over the list
prices = []
for item in items:
    prices.append(item[2])
print(prices)
# alternate solution Using Mapping
x = list(map(lambda item: item[2], items))
print(x)

# Using Filter function
price_filter = list(filter(lambda item: item[2] > 10, items))
print(price_filter)

# Using List Comprehension
# prices=[expression for item in items]
prices2 = [item[2] for item in items]
print(prices2)

prices2 = [item[2] > 3 for item in items]
print(prices2)

# case study
values = []
for x in range(5):
    values.append(x*2)
print(values)


# Uising mapping and lambda to repeat above solution
values = []
values = list(map(lambda x: x*2, range(5)))
print(values)

# Using comprehension List

price = [x*2 for x in range(5)]
print(price)
