import re


def check_email(email):
    email_regexp = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
    email_check_pattern = re.compile(email_regexp)
    validation_result = True if email_check_pattern.fullmatch(
        email) else False
    return validation_result
