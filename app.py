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

from classes import Admin
from classes import Bag
from classes import Cart
from classes import Product
from classes import Store
from classes import User


store_name = Store("BOV")
print(f"We glad to see you in our store {store_name.name}!")
print(f'''There are our products:
{store_name.product}''')


new_user = User('Kir', '232323', 24, 10_000, ())
admin = Admin('Alex', '585858', 40, 8_000, (), True)


cash = int(
    input(f"Hello, {user_name.capitalize()}!"
          f"\nHow much money do you have? "))


if not cash:
    print(f"Good bye, {user_name.capitalize()}!"
          f"Come in with money next time!")
else:
    print("Our goods: ", store)
    print(f"What do you want to buy, {user_name.capitalize()}? ")

while cash > 0:
    order = input("Enter product name: ")

    if order in store:
        cash = cash - store[order]
        print(f"You have {cash} left")
    else:
        print(f"Sorry, {user_name.capitalize()}, "
              f"but we don't have the {order}")
print(f"Good bye, {user_name.capitalize()}!")
