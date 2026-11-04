from products import PhysicalProduct, DigitalProduct, SubscriptionProduct
from shipping import StandardShipping, ExpressShipping, PickupShipping
from order import Order
from customer import Customer

laptop = PhysicalProduct(
    1,
    "Laptop",
    1200,
    10,
    2.5
)

book = DigitalProduct(
    2,
    "Python eBook",
    30,
    100,
    250
)

subscription = SubscriptionProduct(
    3,
    "Premium Plan",
    100,
    50,
    12
)

george = Customer(
    "George Angelov",
    "george@mail.com",
    "Plovdiv"
)

standard = StandardShipping()
express = ExpressShipping()
pickup = PickupShipping()

order = Order(george, standard)

order.add_item(laptop, 2)
order.add_item(book, 3)

#calculations test
print(order.calculate_total())

#statе behavior
print(order.status)

order.pay()
print(order.status)

order.ship()
print(order.status)

order.completed()
print(order.status)

order.cancel()
print(order.status)
