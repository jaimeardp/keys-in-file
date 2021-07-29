import os
from action import Action
from cryptography.fernet import Fernet
from helper import format_path_abs

from dotenv import load_dotenv

load_dotenv()

action = Action()

action.generate_key()



message = "some secret message"

encrypted = action.encrypt(message)


# print how it looks
print(encrypted)


decrypted_encrypted = action.decrypt(encrypted)

print(decrypted_encrypted)

action.specific_target = "file"

print(action.specific_target)


base_path = os.getenv('PATH_ABS_FILE')
filename = "data.json"


path_abs_file = format_path_abs(base_path, filename)

action.encrypt(path_abs_file)

action.decrypt(path_abs_file)



