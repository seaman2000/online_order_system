class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise TypeError('id should contain a number')
        if value <= 0:
            raise ValueError('id cannot be a negative number')
        self._id = value

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('name should be a string')
        if not value.strip():
            raise ValueError('name cannot be empty string')
        self._name = value

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if not isinstance(value, int | float):
            raise TypeError('price should contain a number')
        if value <= 0:
            raise ValueError('price cannot be a negative number')
        self._price = value

    @property
    def stock(self):
        return self._stock
    @stock.setter
    def stock(self, value):
        if not isinstance(value, int):
            raise TypeError('stock should be an integer number')
        if value < 0:
            raise ValueError('stock cannot be a negative number')
        self._stock = value

class PhysicalProduct(Product):
    def __init__(self, id, name, price, stock, weight):
        super().__init__(id, name, price, stock)
        self.weight = weight

class DigitalProduct(Product):
    def __init__(self, id, name, price, stock, file_size):
        super().__init__(id, name, price, stock)
        self.file_size = file_size
        
class SubscriptionProduct(Product):
    def __init__(self, id, name, price, stock, duration_months):
        super().__init__(id, name, price, stock)
        self.duration_months = duration_months

