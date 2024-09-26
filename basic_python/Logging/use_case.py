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



@property
def email(self):
    return '{}{}@gmail.com'.format(self.firstname, self.lastname)


empl1 = Employees('Samson', 'Eromonsei')
emply1 = Employees('Esther, Eromonsei')
