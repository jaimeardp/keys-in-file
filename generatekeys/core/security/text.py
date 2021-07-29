
from security.generic import Generic
from cryptography.fernet import Fernet


class Text(Generic):

    def __init__(self, key) -> None:
        Generic.__init__(self, key)


    def encrypt(self, message_decrypted) -> str:
        """
            encrypt the message
        """
        message_prepared = message_decrypted.encode()
        encrypted = self.f.encrypt(message_prepared)
        return encrypted

    def decrypt(self, message_encrypted) -> str:
        """
            decrypt the message
        """
        decrypted_encrypted = self.f.decrypt(message_encrypted)
        return decrypted_encrypted