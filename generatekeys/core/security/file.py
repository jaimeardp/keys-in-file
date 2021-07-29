from security.generic import Generic
from cryptography.fernet import Fernet

class File(Generic):

    def __init__(self, key) -> None:
        Generic.__init__(self, key)

    def encrypt(self, filename):
        """
        Given a filename (str) and key (bytes), it encrypts the file and write it
        """

        with open(filename, "rb") as file:
            # read all file data
            file_data = file.read()
                # encrypt data
            encrypted_data = self.f.encrypt(file_data)


            # write the encrypted file
            with open(filename, "wb") as file:
                file.write(encrypted_data)


    def decrypt(self, filename):
        """
        Given a filename (str) and key (bytes), it decrypts the file and write it
        """
        with open(filename, "rb") as file:
            # read the encrypted data
            encrypted_data = file.read()
        # decrypt data
        decrypted_data = self.f.decrypt(encrypted_data)
        # write the original file
        with open(f"{filename}001", "wb") as file:
            file.write(decrypted_data)
