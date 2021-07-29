from cryptography.fernet import Fernet

class Generic:

    def __init__(self, key) -> None:
        self.f = Fernet(key)