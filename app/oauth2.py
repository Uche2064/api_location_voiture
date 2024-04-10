from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
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
        id = payload.get("id")

        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)

    except JWTError:
        raise credentials_exception
    
    return token_data

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(db.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    token = verify_token(token, credentials_exception)

    user = db.query(models.User).filter(models.User.id == token.id).first()

    return user

