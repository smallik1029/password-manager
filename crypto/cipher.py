from cryptography.fernet import Fernet, InvalidToken

def encrypt(data: bytes, key: bytes) -> bytes:
    f = Fernet(key)
    return f.encrypt(data)

def decrypt(token: bytes, key: bytes) -> bytes:
    f = Fernet(key)
    try:
        return f.decrypt(token)
    except InvalidToken:
        raise ValueError("Decryption Failed.")