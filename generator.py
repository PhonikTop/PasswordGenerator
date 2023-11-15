import random
import string


class Generator:
    def __init__(self):
        self.number_of_symbols = input("Enter the password length:\n")

    def symbols(self):
        symbols = string.ascii_letters + "".join([chr(1040 + i) for i in range(32)])
        password = "".join(
            random.choice(symbols) for _ in range(int(self.number_of_symbols))
        )
        return password

    def all_sym(self):
        symbols = (
            string.ascii_letters
            + string.digits
            + string.punctuation
            + "".join([chr(1040 + i) for i in range(32)])
        )
        password = "".join(
            random.choice(symbols) for _ in range(int(self.number_of_symbols))
        )
        return password

    def signs(self):
        symbols = string.punctuation
        password = "".join(
            random.choice(symbols) for _ in range(int(self.number_of_symbols))
        )
        return password
