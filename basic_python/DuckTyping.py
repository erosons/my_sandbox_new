# Ducking creation does need an abstract class creation as long as the classes has the method similarities
# Easlier way to define polymorphism


class RadioLst:
    def showlist(self):     # form 1
        print("This is a radiolist")


class Droplist:
    def showlist(self):  # form 2
        print("This is a DropList")


class Sliderbar:
    def showlist(self):  # form 3
        print("This is a Sliderbar")

# Implementation 1


def ButtonType(button):  # This functions take all the different forms of abstractmethod excuted in the subclasses and implment them as they are passed
    button.showlist()   # This called polymorphism

# Implementation 2


def ButtonTypes(buttons):  # This functions take all the different forms of abstractmethod excuted in the subclasses and implment them as they are passed
 # *button  will only return a tuple
 # buttons can return a list
    for buttom in buttons:
        buttom.showlist()   # This called polymorphism


button1 = RadioLst()
button2 = Droplist()
button3 = Sliderbar()

ButtonType(button1)
ButtonType(button2)
ButtonType(button3)
ButtonTypes([button1, button2, button3])
