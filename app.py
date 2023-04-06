# 1) Greeting
# 2) Context-menu
#   a) Register new user
#   q) Quit
# 3) Show products for user
# 4) User might buy something and that something must put into Cart
# 5) After every deal: "Do you want to buy something else?"
# 6) If No => Get user money and put products from Cart to Bag. If money < something => "Not enough money"
# 7) Do you want to Exit?
#   a) Yes => Goodbye
#   b) No => Return to 1
#
#
# class Store: products = []
#
# class User: bag, money => inherit User => SayHello() => print("Hello from User")
#
# class Admin: inherit User => SayHello() => print("Hello from Admin")
#
# class Product: price, label
#
# class Cart: sum_products = [] => getFullPrice(*args, **kwargs)
#
# class Bag: bag = []

# from Classes.admin import Admin
from Classes.bag import Bag
from Classes.cart import Cart
from Classes.product import Product
from Classes.store import Store
from Classes.user import User


store_name = Store("BOV")
# print(f"We glad to see you in our store {store_name.getName()}!")
# print(store_name.getProducts())

print(store_name.name)

# new_user = User('Kir', '232323', 24, 10_000, ())

# admin = Admin('Alex', '585858', 40, 8_000, (), True)
