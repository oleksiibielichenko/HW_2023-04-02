import re


def check_password(password):
    if len(password) <= 7:
        print("Password must be 8 simbols minimum!")
    regexp = r'^(?=.*[!@#$%^&*()_+=-].*)(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z!@#$%^&*()_+=-]{8,}$'
    password_check_pattern = re.compile(regexp)
    validation_result = True if password_check_pattern.match(
        password) else False
    return validation_result
