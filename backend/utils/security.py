# utils/security.py
from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(plain: str) -> str:
    return generate_password_hash(plain, method="pbkdf2:sha256", salt_length=16)

def verify_password(hash_value: str, plain: str) -> bool:
    return check_password_hash(hash_value, plain)
