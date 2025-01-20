#1. Hash table implementation
# Magic method: https://rszalski.github.io/magicmethods/

#hash function operations where we are getting ascii value for each key
def hash_value(key):
    h=0
    for char in key:
        h +=ord(char)
    return h %100



class hash_Table:
    def __init__(self):
        self.max=100
        self.arr=[None for i in range(self.max)]

    # Create the function that ascii value for each character and return 
    def hash_value(self,key):
        h=0
        for char in key:
            h +=ord(char)
        return h % self.max

    def hash_len_value(self,key):
    
        return len(key)
   
    # __setitem__ allows me to perform a native dictionary operation.
    def __setitem__(self, key, value):
        h=self.hash_value(key)
        self.arr[h]=value
    
    # __getitem__ allows me to perform a native dictionary operation of using a key like value ops.
    def __getitem__(self, key):
        h=self.hash_value(key)
        return self.arr[h]

     # __delitem__ allows me to perform a native dictionary operation of using a key like value ops.
    def __delitem__(self, key):
        h=self.hash_value(key)
        self.arr[h]= None
   


#test scenario
t=hash_Table()
t["samson"]=5
t["samson"] 





#2.  Another Approach

class hashMapps:
    def __init__(self) -> None:
        self.max=100
        self.arr=[None for x in range(self.max)]
    
    def key_index(self,key):
        h=0
        for i in str(key):
            h +=ord(i)
        return (h%10)

    
    def inset_prod(self,key,value):
        h=self.key_index(key)
        self.arr[h]=value

    def retrive_prod(self,key):
        key_number=self.key_index(key)
        return self.arr[key_number]



testCase=hashMapps()
testCase.inset_prod("Apple",5)
testCase.inset_prod("Orange",7)
testCase.inset_prod("Apple",5)
testCase.inset_prod("Onion",6)
testCase.inset_prod("Grap",8)


testCase.retrive_prod("Apple")