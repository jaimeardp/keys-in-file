from file import encrypt, decrypt
from keys import write_key, load_key


# generate and write a new key
write_key()


# load the previously generated key
key = load_key()


message = "some secret message".encode()

# initialize the Fernet class
f = Fernet(key)


# encrypt the message
encrypted = f.encrypt(message)


# print how it looks
print(encrypted)


decrypted_encrypted = f.decrypt(encrypted)
print(decrypted_encrypted)


# uncomment this if it's the first time you run the code, to generate the key
# write_key()
# load the key
key = load_key()
# file name
file = "data.csv"
# encrypt it
encrypt(file, key)


# decrypt the file
decrypt(file, key)