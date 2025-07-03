# 1. Hash table implementation part for Handing Collision:

# In this situation where we have Collision => which means harshing key are the same for and input value
# Solution :
# - We can use chaning whereby we create on hash key and use a  Linear list to append the additional values  with their specific keys
# - Or we can either go the approach of Linear Probing, where we check for open space in the list and fill if up with value resulting from , and were no empty we check for the next available space.

# Hash function operations where we getts ascii value for each key passed
def hash_value(key):
    h = 0
    for char in key:
        h += ord(char)
    return h % 100


class Hashtable:
    def __init__(self):
        self.max = 100
        self.arr = [[] for i in range(self.max)]

    # Create the function that ascii value for each character and return
    def hash_value(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    # __setitem__ allows me to perform a native dictionary operation.
    def __setitem__(self, key, value):
        h = self.hash_value(key)
        found = False
        # Collision Handing
        # This Operations checks key match and index match
        # Where key exist Updates and where hash key function index/number are the same
        # But the hash key are different it append to the list match hash index. 
        for idx, elements in enumerate(self.arr[h]):
            if len(elements) == 2 and elements[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    # __getitem__ allows me to perform a native dictionary operation of using a key like value ops.

    def __getitem__(self, key):
        h = self.hash_value(key)
        if len(self.arr[h])>1:
          for i,j in enumerate(self.arr[h]):
            if key==j[0]:
              return j
            else:
               return None

        return self.arr[h]

     # __delitem__ allows me to perform a native dictionary operation of using a key like value ops.
    def __delitem__(self, key):
        h = self.hash_value(key)
        self.arr[h] = None


if __name__=="__main__":
    # test scenario for collision and non Collision
    t = Hashtable()
    t["Rice"] = 45
    t["Cire"] = 78

    #
    t["Cire"]  
