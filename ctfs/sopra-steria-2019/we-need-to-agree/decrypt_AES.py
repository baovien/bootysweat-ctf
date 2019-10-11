import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random

BLOCK_SIZE = 16
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

#enc type is bytes
#password type is string
#iv type is bytes
def decrypt(enc, password, iv):

    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc)).decode()


