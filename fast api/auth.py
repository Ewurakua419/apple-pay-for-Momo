import bcrypt

def encodere(password:str):
    # converting password to array of bytes
    bytes = password.encode('utf-8')

    # generating the salt
    salt = bcrypt.gensalt()

    # Hashing the password
    hash = bcrypt.hashpw(bytes, salt)

    return hash

def decodere(password:str,h:str):
    checkByte=password.encode('utf-8')
    ogByte=h.encode('utf-8')
    return bcrypt.checkpw(checkByte,ogByte)
