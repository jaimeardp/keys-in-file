from cryptography.fernet import Fernet

from helper import create_folder_temp

class Key:

    def __init__(self, key_filename = "key", key_foldername = "") -> None:
        self.key_filename = key_filename
        self.key_foldername = key_foldername
        self.folder_working = create_folder_temp("temp")

    def write_key(self) -> None:
        """
        Generates a key and save it into a file
        """
        key = Fernet.generate_key()
        with open(f"{self.folder_working}/{self.key_filename}.key", "wb") as key_file:
            key_file.write(key)

    def load_key(self) -> str:
        """
        Loads the key from the current directory named `key.key`
        """
        return open(f"{self.folder_working}/{self.key_filename}.key", "rb").read()
