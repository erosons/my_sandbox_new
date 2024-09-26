

class Employee:
    def __init__(self, Name, lastname, level, yrsService):
        self.Name = Name
        self.Name = lastname
        self.level = level
        self.yrsService = yrsService

    # Converting to string

    def __str__(self):
        return f"Point({self.Name}.{self.lastName},{self.level},{self.yrsService})"

    # Converting to representing in string

    def __repr__(self):
        return "<Employee Profile Name:{0},lastName:{1},Level:{self.level},yrsOfService{self.yrService}>".format(self.Name, self.lastName, self.level, self.yrService)

    # Comparing instance equality

    def __eq__(self, other):
        if (self.level == other.level):
            self.yrsService >= other.yrsService
        return self.level >= other.level

    # Comparing instance greater than or less than

    def __gt__(self, other):
        return self.level > other.level and self.yrsService > other.yrsService

    def __lt__(self, other):
        if (self.level == other.level):
            self.yrsService < other.yrsService
        return self.level < other.level

    def __lte__(self, other):
        if (self.level == other.level):
            self.yrsService <= other.yrsService
        return self.level <= other.level

    # Performig addition oprations with instances of a class

    def __add__(self, other):
        return self.level + other.level and self.yrsService + other.yrsService

    # Performig in-place addition
    def __iadd__(self, other):
        self.level += other.level
        self.yrsService += other.yrsService
        return self


employeeList = []

employeeList.append(Employee("Sam", "Ero", 1, 3))
employeeList.append(Employee("Esther", "Erom", 1, 2))
employeeList.append(Employee("Pros", "Eros", 5, 7))
employeeList.append(Employee("Peace", "Romo", 2, 3))
employeeList.append(Employee("Precious", "Osuare", 4, 5))
employeeList.append(Employee("Prayer", "testo", 3, 8))


# Comparing instances equality
print(employeeList[0] == employeeList[1])

# # Comparing instance greater than or less than
print(employeeList[2] + employeeList[3])

# # adding object instances together
# grt3 = grt + grt1
# print(grt3)

# # printing in place object
# point += other
# print(point)
