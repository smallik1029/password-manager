import os
import json
from crypto.cipher import encrypt, decrypt

VAULT_PATH = "vault.enc"
SALT_SIZE = 16


def vault_exists() -> bool:
    return os.path.exists(VAULT_PATH)


def save_vault(data: dict, key: bytes, salt: bytes) -> None:
    plaintext = json.dumps(data).encode()
    token = encrypt(plaintext, key)
    with open(VAULT_PATH, "wb") as f:
        f.write(salt + token)


def load_salt() -> bytes:
    with open(VAULT_PATH, "rb") as f:
        return f.read(SALT_SIZE)


def load_vault(key: bytes) -> dict:
    with open(VAULT_PATH, "rb") as f:
        f.read(SALT_SIZE)
        token = f.read()
    return json.loads(decrypt(token, key))