import re


class Validator(object):

    def __init__(self, email):
        self.email = email

    def check_for_symbol(self):
        if re.search("[@gmail.com]", self.email) is None:
            return False
        else:
            return True

    def check_length(self):
        if len(self.email) >= 12:
            return True
        else:
            return False


def email_to_verify():
    return input('Enter your email address: ')


def check_email(email):
    validator = Validator(email)
    symbol = validator.check_for_symbol()
    if symbol is False:
        print ("Your email address is not valid. Failed symbols..")

    length = validator.check_length()
    if length is False:
        print ("Your email is not valid. Failed length")

    if length and symbol is True:
        print ("Email is a valid email address.")


if __name__ == '__main__':
    e = email_to_verify()
    check_email(e)
