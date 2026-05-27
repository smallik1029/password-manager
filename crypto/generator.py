import secrets
import string

DEFAULT_LENGTH = 16


def generate_password(length: int = DEFAULT_LENGTH) -> str:
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(alphabet) for _ in range(length))