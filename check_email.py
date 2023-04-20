import re


def check_email(email):
    email_regexp = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
    email_check_pattern = re.compile(email_regexp)
    validation_result = "valid" if email_check_pattern.fullmatch(
        email) else "not valid"
    return (email, validation_result)


print(check_email("bielichenko@gmail.com"))
print(check_email("bielichenko_oleksii@gmail.com"))
print(check_email("bielichenko.o@gmail.com"))
print(check_email("bielichenko@gmail.com.ua"))
print(check_email("bielichenko@gmailcom"))
print(check_email("@gmail.com"))
print(check_email("bielichenkogmail.com"))
print(check_email("bielichenko@gm+ail.com"))
