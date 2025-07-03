city = "My Name is Samson"

# Looping in STR
for i in city:
    print(i)

# Slicing through a string
city[-5:-2] = > 'ams'
city[2:] = > ' Name is Samson'
city[2:5] = > ' Na'
city[:5] = > 'My Na'
city[0] = > "M"
city[::-1] = > 'nosmaS si emaN yM'


# 1. Checking if word exits in a string
print("my" in city) = > True/False
print("My" not in city) = > True/False

# 2.
if "My" not in city:
    print("Not Found")

# Converting a string to List
city_list = list(city) = > ['M', 'y', ' ', 'N', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'S', 'a', 'm', 's', 'o', 'n']

# Length of string
city_list = len(city) = > 17


# Modify
city.upper() = > 'MY NAME IS SAMSON'
city.lower() = > 'MY NAME IS SAMSON'
city.strip() = > ' Remove White Space' = > 'Remove White Space'
city.replace("H", "J") = >input  'Hello, World' = >output 'Jello, World'
city.split(",") = >input  'Hello, World' = >output['Jello', 'World']

# concatenation
a = 's' + b = 'c' = > output 'sc'
a = 'a'
b = " "
c = 'b'
d = a+b+c

# 1. String Formatting
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# 2. String Formatting
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


# String replacement
txt = "Hello World"

txt.replace("Hello", "Yellow")


# Using this, the replacement character must have the same length as the to be replaced
# -- limitation
txt = "Hello World"
mytable = txt.maketrans("Hello", "Yello")
print(txt.translate(mytable))


# Dealing with WhiteSpace
txt = "How are you \"samsons\" "

# Removing WhiteSpace
newlist1 = []
a = 'Hello ,World'
for i in a.split(','):
    newlist1.append(i.strip())
newlist1

# Partion a word in a string base on a search
a = 'Hello World Samson'
a.partition('World') = > ('Hello ', 'World', ' Samson')
