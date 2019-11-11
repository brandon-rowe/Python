import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password_provided = "passwords" #This is the input in the form of a string
password = password_provided.encode() #Convert to bytes

salt = b'\x90\xf7\xc7\xddBE\x15&\xc2\xa5\xa0o\xf9\xa4\xcbF'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key=base64.urlsafe_b64encode(kdf.derive(password)

