from cryptography.fernet import Fernet


from security.file import File
from security.text import Text
from keys import Key

class Action:

    _key = None
    _running_instance = {"text":Text, "file": File}

    def __init__(self, key="", specific_target = "text") -> None:
        self.f : Fernet = None # deprecated
        self.specific_target = specific_target

    def _generate_fernet_instance(self, key : str) -> Fernet:
        """
            initialize the Fernet class (deprecated)
        """
        f = Fernet(key)
        return f

    def generate_key(self):
        manager_key = Key()
        manager_key.write_key()
        self._key = manager_key.load_key()

    def clear_key(self):
        self._key = None

    def encrypt(self, payload):
        """
            encrypt message o file based on filter
        """
        if self.specific_target == "text":
            t = Text(self._key)
            encrypted = t.encrypt(payload)
            return encrypted
        elif self.specific_target == "file":
            f = File(self._key)
            f.encrypt(payload)
            return True

    def decrypt(self, payload):
        """
            decrypt message o file based on filter
        """
        if self.specific_target == "text":
            t = Text(self._key)
            decrypted = t.decrypt(payload)
            return decrypted
        elif self.specific_target == "file":
            f = File(self._key)
            f.decrypt(payload)
            return True
    




