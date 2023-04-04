
store = {
    'kit-kat': 20,
    'nuts': 15,
    'snickers': 25,
    'orbit': 10,
    'dirol': 11,
    'coca-cola': 40,
    'fanta': 41,
    'sprite': 42,
}

is_valid = None

user_name = input('Enter your name: ')
user_email = input('Enter your email: ')
user_password = input('Enter your password: ')


def name_validation():
    global user_name
    if len(user_name) < 2:
        return False
    else:
        return True


def email_validation():
    global user_email
    if '@' in user_email and '.' in user_email:
        return True
    else:
        return False


def password_validation():
    global user_password
    if len(user_password) > 6:
        return True
    else:
        return False


def registration():
    global is_valid

    is_valid_name = name_validation()
    is_valid_email = email_validation()
    is_valid_password = password_validation()

    if is_valid_name and is_valid_email and is_valid_password:
        is_valid = True
        print('It is valid data')
    else:
        is_valid = False
        print('It is invalid data')
        exit()


registration()


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
