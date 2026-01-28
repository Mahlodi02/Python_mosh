# Properties

"""At times we want to have control over our attributes so to do that we have to use property decorator """

class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can't be negative")
        self.__price = value
    
product = Product(-10)
print(product.price)
