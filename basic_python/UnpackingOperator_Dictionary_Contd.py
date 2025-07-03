from pprint import pprint
number = [1, 2, 3, 4]
numbers = [*range(5), *"hello"]
num = [*range(4)]
print(numbers)
print(num)

# Unpacking a dictionary and combining the dictionaries
mydic = dict(h=1, s=2, k=4)
mydic2 = dict(w=1, b=3, c=5)
print({**mydic, **mydic2})

# Looping through a senetence and returning a dictionary
sentences = "This is a common interview questions"
mydict = {}
words = sentences.rstrip()
words = words.lower()
for word in words:
    mydict[word] = mydict.get(word, 0) + 1
print(mydict)


def keywithmaxval(d):  # function to return key with the max values:
    """ a) create a list of the dict's keys and values;
        b) return the key with the max value"""
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]


print(keywithmaxval(mydict))


# Mosh solution for looping through a senetence and returning a dictionary with the highest value.
char_frequency_finder = {}
for char in sentences:
    if char in char_frequency_finder:
        char_frequency_finder[char] += 1
    else:
        char_frequency_finder[char] = 1

# pprint allows you to print better but you have to import

pprint(char_frequency_finder, width=1)

# to sort a dictionary first covert dictionary items() to tuple and pass into a list

ListTupleform = sorted(char_frequency_finder.items(),
                       key=lambda kv: kv[1],
                       reverse=True)

# To print the Max from  the List
print(ListTupleform[0])
