# List below is how classes attributes are called and their uses

#  -  Object.__getattr__(self,attr)         called as    => object.attr  This is called only when the called attributes cannot be found.

#  -  Object.__getattribute__(self,attr)    called as    => object.attr   This is also called unconditionally any time an attribute is requested for,
#     Note: It is also called by python anytime python is calling an a class mothod.

# -  Object.__setattr__(self,attr,value)        called as  =>  object.attr=val  The setattr is called the val of an attribute is set
# -  Object.__delattr__(self)       called as  =>  del object.attr=val  The deltattr is called the val of an attribute is deleted
#  -  Object.__dirattr__(self)       called as  =>  del object.attr=val  The dirtattr is called when dir is used


"""
The above helps developers understand the attributes supported by a class
"""


class Color:
    def __init__(self) -> None:
        self.red = 20
        self.blue = 34
        self.green = 30

    # TODO: Use gettattr to dynamically return a value
    def __getattr__(self, attr):
        if attr == "rgbcolors":
            return (self.red, self.green, self.blue)

        elif attr == "hexcolors":
            return "#{0:02x}{1:02x}{2:02x}".format(self.red, self.green, self.blue)

        else:
            raise AttributeError

    # Setting of Values
    def __setattr__(self, attr, val):
        if attr == "rgbcolors":
            self.red = val[0]
            self.blue = val[1]
            self.green = val[2]
        else:
            super().__setattr__(attr, val)

    # use dir to list the available properties of class
    def __dir__(self):
        return ("red", "green", "blue", "hexcolors", "rgbcolors")
    

    class Employees:
        """ This class is used to create an Employee"""

        def __init__(self, firstname, lastname) -> None:
            self.first = firstname
            self.lastname = lastname

            print('Created Employee {} - {}'.format(self.fullname, self.email))


        @property
        def fullname(self):
            return '{} {} '. format(self.firstname, self.lastname)

        @fullname.setter
        def email(self,firstname,lastname):
            self.firstname = firstname
            self.lastname = lastname

        @fullname.deleter
        def email(self,firstname,lastname):
            del self.firstname
        del self.lastname 


def main():

    cls1 = Color()

    print(cls1.rgbcolors)
    print(cls1.hexcolors)

    # Allow the setting of value of a computed attribute
    cls1.rgbcolors = (10, 20, 30)
    print(cls1.rgbcolors)

    # calling the dir see above for more details
    print(dir(cls1))


if __name__ == "__main__":
    main()
