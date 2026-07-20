from datetime import datetime, timedelta

import bcrypt
from typing import Union

import jwt
from models.user import User
SECRET_KEY=" MY SECRET KEY"
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
    if isinstance(h, str):#if h is a string
        ogByte = h.encode('utf-8')# change to bytes
    else:
        ogByte = h
    return bcrypt.checkpw(checkByte, ogByte)# returns true if the hashes are the same , else false

def create_token(user:User):
    card={
        "User id": user.unique_id,
        "Username": user.name,
        "exp": datetime.now()+timedelta(hours=2)
    }# creates a kind of signin card

    return jwt.encode(card, SECRET_KEY, algorithm="ES256")#creates a token

def verify_token(token):
    try:
        payload=jwt.decode(token, SECRET_KEY, algorithms=["ES256"])
        return payload
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):# if either the token has expired or if someone edits the token
        return None