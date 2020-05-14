from cryptography.fernet import Fernet;
from key import key;
import json
# Cognitive key encryption
def encrypte_key(message):
    fernet = Fernet(key.encode())
    encoded = message.encode()
    encrypte = fernet.encrypt(encoded)

    return encrypte

# Cognitive key decryption
def decrypte_key(message):

    try:
        f2 = Fernet(key);
        decrypte = f2.decrypt(message.encode())
        return decrypte.decode()
    except Exception as e:
        print(e)

def writeToJson(message):
    data = {};
    