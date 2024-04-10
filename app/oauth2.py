from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from pydantic import EmailStr
from .config import setting
from datetime import datetime as _dt, timedelta as _td
from . import schemas, models, db
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

secret_key = setting.secret_key
algorithm = setting.algorithm
expiration_time = setting.expiration_time

def create_access_token(payload: dict): 
    to_encode = payload

    expire = _dt.now() + _td(minutes=expiration_time)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, secret_key, algorithm=algorithm)


def verify_token(token, credentials_exception):
    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        id: int = payload.get("id")    
        email: EmailStr = payload.get("email")
        if id is None or email is None:
            raise credentials_exception
        return schemas.TokenData(id=id, email=email)
    except JWTError:
        raise credentials_exception

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Information invalide")

    return  verify_token(token, credentials_exception)


