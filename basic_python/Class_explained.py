#https://rszalski.github.io/magicmethods/

"""
Class and inheritance and inheriting artibutes from Base Class Paerent by subclass Child

"""


from operator import length_hint


class Parent:
    def __init__(self, eyecolor, height, haircolor, bodyshape) -> str:
        self.color = eyecolor
        self.height = height
        self.haircolor = haircolor
        self.bodyshape = bodyshape


class Child(Parent):
    def __init__(self, eyecolor, height, haircolor, bodyshape, tedills) -> str:
        super().__init__(eyecolor, height, haircolor, bodyshape)

        if tedills:
            self.tedills = "female_child"

        else:
            self.tedills = "male_child"
        self.eating_habit = "eating_habit"


# myparent = Parent("brown", 5.11, "black", "slim")

myChild = Child("brown", 5.11, "black", "slim", False)

print(myChild.tedills)
print(myChild.bodyshape)


"""
Advance Class implementation 2
"""


class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * (self.width * self.length)


"""
Calling base method in a function subclass 3
"""


class Square(Rectangle):
    def __init__(self, length, width) -> None:
        super().__init__(length, width)

    def surfaceArea(self):
        area = super().area()
        return area * self.length


squreCal = Square(4, 4)
print(squreCal.surfaceArea())


"""
Class Inheritance implementation in subclass4
"""


class Mammal:
    def __init__(self):
        self.color = "brown"

    def eat(self):
        print("mammal can eat")


class Dog(Mammal):
    def __init__(
        self,
    ):  # Constructor created inside a child class /or inheritance class, over rides the base method/attributes
        # to arrest this type of issue, create the custom constructor super()__init__(). this does not allow the base constructor to be overriden.
        super().__init__()
        self.eyecolor = "green"


animal = Dog()
print(animal.color)


"""
Advance Class implementation 3
"""
