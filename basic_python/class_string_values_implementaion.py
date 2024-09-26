# Customizing string representations of objects in class

# There are four types function                             called When
"""                
object.__str__(self)                                        str(object)            
object.__repr__(self)                                       repr(object)
object.__format__(self,format_spec)                         format(object,format_spec)
object.__bytes__(self)                                      bytes(object)

"""


class Person:
    def __init__(self) -> None:
        self.fname = "Joe"
        self.age = 25
        self.lname = "Martins"

    # The instantiated method below are use to over how default String are represented by over riding them.

    # : Use for debugging
    def __repr__(self) -> str:
        return "< Person Class - fname:{0},age:{2},lname{1}".format(self.fname, self.age, self.lname)

    # : Use for a more human readable str
    def __str__(self) -> str:
        return "< Person ({0},{1},{2})".format(self.fname, self.age, self.lname)

    # : For bytes conversion
    def __btyes__(self) -> str:
        val = "Person:{0}:{1}:{2}".format(
            self.fname, self.age, self.lname
        )
        return bytes(val.encode('utf-8'))


def main():
    # create object person

    cls1 = Person()

    # Use the different Python function to convert it to string
    print(str(cls1))
    print(repr(cls1))
    print("Formatted {0}:".format(cls1))
    # print(bytes(cls1))


if __name__ == "__main__":
    main()
