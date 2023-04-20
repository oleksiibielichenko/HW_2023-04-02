import re


def check_password(password):
    if len(password) <= 7:
        print("Password must be 8 simbols minimum!")
    regexp = r'^(?=.*[!@#$%^&*()_+=-].*)(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z!@#$%^&*()_+=-]{8,}$'
    password_check_pattern = re.compile(regexp)
    validation_result = "valid" if password_check_pattern.match(
        password) else "not valid"
    return (password, validation_result)


print(check_password("ADTqqq222!"))
print(check_password("As2-"))
print(check_password("WWWWWWWWWWW"))
print(check_password("1234567890"))
print(check_password("eeeeeeeeeeee"))
print(check_password("!_________-__"))
print(check_password("-f-f-f--f-f"))
print(check_password(" klvdsnfkl adsjlcbs"))
