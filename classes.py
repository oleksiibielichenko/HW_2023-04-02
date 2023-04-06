class Store:
    def __init__(self, name, product=[]):
        self.name = name
        self.product = product

    def getName(self):
        print(self.name)

    def getProducts(self):
        print(self.product)


class User:
    def __init__(self, name, password, age, money, bag):
        self._name = name
        self._password = password
        self._age = age
        self._money = money
        self._bag = bag


class Admin (User):
    def __init__(self, name, password, age, money, bag, isAdmin):
        super().__init__(name, password, age, money, bag)
        self._isAdmin = isAdmin


class Bag:
    def __init__(self, name):
        self._name = name


class Cart:
    def __init__(self, item):
        self._item = item


class Product:

    def __init__(self, name, description, price):
        self._name = name
        self._desc = description
        self._price = price
