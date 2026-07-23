from pwdlib import PasswordHash



def generate_hash(password: str) -> str:
    return PasswordHash.recommended().hash(password)

def verify_password(plain_password: str, hashed_password: str)-> bool:
    return PasswordHash.recommended().verify(plain_password, hashed_password)