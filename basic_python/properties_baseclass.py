# Implementation 1
class Product:
    # attribute instantiation  returns the method set_price and price as argument.
    def __init__(self, price):
        self.__set_price(price)

    def __get_price(self):
        return self.__price

# A method is defined and used to control the price attributes
    def __set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be -ve")
        self.__price = value
# the property attribute is used to assign Xters/ poerties to the price
    price = property(__get_price, __set_price)


# Implementation 2
# Testing out the price attributes.
product = Product(-1)
print(product.price)


class Product1:
    # attribute instantiation  returns the method set_price and price as argument.
    def __init__(self, price):
        self.price = price

    @property   # This replaces the get_price above {DECORATORS}
    def price(self):
        return self.__price

    @price.setter  # This setters the price
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be -ve")
        self.__price = value


# Testing out the price attributes.
product = Product1(-1)
print(product.price)


# BY DEFAULT ALL CLASS HAS THE ATTRIBUTES AND METHOD OF OBJECT CLASS------ OBJEVT CLASS IS THE BASE CLASS
print(isinstance(product, object))
print(issubclass(Product1, object))
