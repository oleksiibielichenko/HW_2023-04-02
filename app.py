
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


print("We glad to see you in our Store!!!")


ATB = Store("ATB")
print(ATB.getName())
