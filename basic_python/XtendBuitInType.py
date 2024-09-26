class Text(str):
    def duplicate(self):  # This allows you to pass the inheritance of a built in type to a class and extend its functionality of str
        return self+self+self


class Integer(int):
    def summation(self):
        return self+self


class ListXtended(list):  # This allows you to pass the inheritance of a built in type to a class and extend its functionality of list
    def append(self, object):
        print("Append the List")
        super().append(object)


text = Text("python")
print(text.duplicate())

Inte = Integer(1)
print(Inte.summation())

mylist = ListXtended()
mylist.append("1")
