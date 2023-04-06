class Store:
    def __init__(self, name, ):
        self.name = name

    def getName(self):
        print(self.name)


ATB = Store("ATB")
print(ATB.getName())


class Item:

    def __init__(self, name, description, price):
        self._name = name
        self._desc = description
        self._price = price


class Cart:
    def __init__(self, item):
        self._item = item


class Bag:
    def __init__(self, name):
        self._name = name
