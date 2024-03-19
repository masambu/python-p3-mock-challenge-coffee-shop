# customer.py
class Customer:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    def orders(self):
        return [order for order in Order.orders if order.customer == self]

    def coffees(self):
        return set(order.coffee for order in self.orders())

# coffee.py
class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters long")
        self._name = name

    @property
    def name(self):
        return self._name

    def orders(self):
        return [order for order in Order.orders if order.coffee == self]

    def customers(self):
        return set(order.customer for order in self.orders())

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        total_price = sum(order.price for order in self.orders())
        num_orders = self.num_orders()
        if num_orders == 0:
            return 0
        return total_price / num_orders

# order.py
class Order:
    orders = []

    def __init__(self, customer, coffee, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self.__class__.orders.append(self)
