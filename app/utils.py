from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(plaintext: str)-> str:
    return pwd_context.hash(plaintext)


def verify_password(plaintext: str, hashed_password: str)-> bool:
    return pwd_context.verify(plaintext, hashed_password)