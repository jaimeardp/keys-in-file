import sys
import uuid
import hmac, hashlib, base64
from pprint import pprint
from datetime import datetime



enviroment = "prod"
generate = False

status_application = dict()

def generate_RSA(bits=2048):
    '''
    Generate an RSA keypair with an exponent of 65537 in PEM format
    param: bits The key length in bits
    Return private key and public key
    '''
    from Crypto.PublicKey import RSA 
    new_key = RSA.generate(bits, e=65537) 
    public_key = new_key.publickey().exportKey("PEM") 
    private_key = new_key.exportKey("PEM") 
    return private_key, public_key

def simple_hashing(message):
    result = hashlib.sha1(message.encode()).hexdigest()
    print(result)
    return result




if __name__ == '__main__':

    status_application[enviroment] = dict()

    if generate:

        AccessKey = uuid.uuid4()

        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        keyDecoded = enviroment + 'companynamev2' + time
        print(keyDecoded)
        status_application[enviroment]["accessKey"] =  str(AccessKey)
        status_application[enviroment]["secretKey"] =  simple_hashing(keyDecoded)

        l_access_key = status_application[enviroment]["accessKey"]
        print(l_access_key)
        message = bytes(str(l_access_key),'utf-8')
        key = bytes(status_application[enviroment]["secretKey"],'utf-8')
        secret_hash = base64.b64encode(hmac.new(key, message, digestmod=hashlib.sha256).digest()).decode()
        print("SECRET HASH:",secret_hash)
        status_application[enviroment]["secretHash"] =  secret_hash


    else:

        message = bytes('','utf-8')
        key = bytes('','utf-8')
        secret_hash = base64.b64encode(hmac.new(key, message, digestmod=hashlib.sha256).digest()).decode()
        print("SECRET HASH:",secret_hash)




    pprint(status_application)

