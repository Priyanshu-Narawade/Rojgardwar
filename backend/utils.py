import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(given, stored):
    return hash_password(given) == stored
