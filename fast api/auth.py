import bcrypt
from typing import Union

def encodere(password:str):
    # converting password to array of bytes
    bytes = password.encode('utf-8')

    # generating the salt
    salt = bcrypt.gensalt()

    # Hashing the password
    hash = bcrypt.hashpw(bytes, salt)
    string_hash=hash.decode('utf-8')

    return string_hash

def decodere(password:str, h: Union[str, bytes]):
    checkByte = password.encode('utf-8')
    if isinstance(h, str):
        ogByte = h.encode('utf-8')
    else:
        ogByte = h
    return bcrypt.checkpw(checkByte, ogByte)
