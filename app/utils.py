from passlib.context import CryptContext
from . import models

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(plaintext: str)-> str:
    return pwd_context.hash(plaintext)


def verify_password(plaintext: str, hashed_password: str)-> bool:
    return pwd_context.verify(plaintext, hashed_password)

def authentifier_user(username: str, password: str, db):
    get_user = db.query(models.User).filter(models.User.email == username).first()
    if get_user is None:
        return False
    if not verify_password(password, get_user.password):
        return False

    return get_user