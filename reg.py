
from check_email import check_email
from check_password import check_password


def user(email, password):
    return {
        'email': email,
        'password': password,
    }


def registration():
    return []


def validation(user, list):
    email, password, *args = user.values()
    if check_email(email) or check_password(password):
        list.append(user)
        return True
    else:
        return False


registred = registration()

user_email = input('Enter your email: ')
user_password = input('Enter your password: ')


new_user = user(user_email, user_password)

is_valid = validation(new_user, registred)

if is_valid:
    print(registred)
    for user in registred:
        print(user['email'])
