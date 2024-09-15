import string
import random
import secrets


class GeneratorHash:

    def __init__(self, _len: int = 10):
        self.__len = _len

    def get_hash(self):
        password = []
        characters = string.ascii_letters + string.digits

        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.ascii_uppercase))
        password.append(random.choice(string.digits))

        while len(password) < self.__len:
            password.append(secrets.choice(characters))

        random.shuffle(password)
        password = "".join(password)
        return password
