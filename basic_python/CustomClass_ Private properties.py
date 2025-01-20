class TagCloud:
    def __init__(self):
        self.__tags = {}

# This allows you to create keys and append values to the dictionary
    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

# This allows you to index the key t return the value

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    # This allows you to assign a new value to th key
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

# This allows you to know the number of key in the dictionary

    def __len__(self):
        return len(self.__tags)

# This allows you to iterare /loop over the dictionary

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()   # This is the instance of the class
cloud.add("Python")  # This allows you to append key and vlue to the dictionary
cloud.add("python")
cloud.add("python")
cloud.add("python")
print(cloud['python'])  # This allows you to index the key t return the value
cloud['python'] = 10    # This allows you to assign a new value to th key
# This allows you to know the number of key in the dictionary
print(cloud['python'])
print(len(cloud))      # This allows you to iterare /loop over the dictionary
for tag in cloud:
    print(tag)
