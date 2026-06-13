import bcrypt
import hashlib
import secrets
import string
import random
from argon2 import PasswordHasher


ph = PasswordHasher()


def secure_hash(plain: str) -> str:
    return ph.hash(plain)


def secure_check(hashed: str, plain: str) -> bool:
    return ph.verify(hashed, plain)


def fast_hash(plain:str) -> str:
    encoded = plain.encode()
    sha256 = hashlib.sha256()
    sha256.update(encoded)
    return sha256.hexdigest()


def fast_check(hashed:str, plain:str) -> bool:
    encoded_plain = plain.encode()
    sha256 = hashlib.sha256()
    sha256.update(encoded_plain)
    p = sha256.hexdigest()
    return p == hashed


def generate_password(length=6):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(length))
