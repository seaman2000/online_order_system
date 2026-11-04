from product import Product
from customer import Customer
from shipping import ShippingPolicy

class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.items = [self.product, self.quantity]

    @property
    def product(self):
        return self._product
    @product.setter
    def product(self, value):
        if not isinstance(value, Product):
            raise TypeError('product is not an object')
        self._product = value

    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int):
            raise TypeError('quantity should be an integer')
        if value <= 0:
            raise ValueError('quantity should be a positive number')
        self._quantity = value

    def subtotal(self):
        return self.quantity * self.product.price

class Order:
    def __init__(self, customer, item_order, shipping_policy, status=None):
        self.customer = customer
        self.item_order = item_order
        self.shipping_policy = shipping_policy
        self.status = status

    @property
    def customer(self):
        return self._customer
    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise TypeError('customer is not an object')
        self._customer = value

    @property
    def shipping_policy(self):
        return self._shipping_policy
    @shipping_policy.setter
    def shipping_policy(self, value):
        if not isinstance(value, ShippingPolicy):
            raise TypeError('shipping policy is not an object')
        self._shipping_policy = value

    def add_item(self, product, quantity):
        new_item = OrderItem(product, quantity)
        self.item_order.append(new_item)

    def remove_item(self, item):
        if not isinstance(item, OrderItem):
            raise TypeError
        if item in self.item_order:
            self.item_order.remove(item)

    def calculate_products_total(self):
        subtotal = 0

        if not self.item_order:
            raise ValueError('there are not orders')
        for item in self.item_order:
            subtotal += item.subtotal()
        return subtotal

    def calculate_total_weight(self):
        total_weight = 0
        for item in self.item_order:
            if item.product.weight:
                total_weight += item.product.weight * item.quantity
            else:
                pass
        return total_weight

    def calculate_total(self):
        return self.calculate_products_total() + self.shipping_policy.calculate_shipping(self.calculate_total_weight())

    def change_shipping_policy(self, new_policy):
        self.shipping_policy = new_policy

    def create(self):
        if self.status is None:
            self.status = 'created'

    def pay(self):
        if self.status == 'created':
            self.status = 'paid'

    def ship(self):
        if self.status == 'paid':
            self.status = 'shipped'

    def completed(self):
        if self.status == 'shipped':
            self.status = 'completed'

    def cancel(self):
        if self.status != 'completed':
            self.status = 'canceled'