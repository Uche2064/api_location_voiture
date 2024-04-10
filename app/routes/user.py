from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import EmailStr
from .. import schemas, db, models, utils
from sqlalchemy.orm import Session


route = APIRouter(
    prefix="/admin",
    tags=["Administrateur"],
)

@route.post("/", response_model=schemas.ResponseCreateUser)
async def save_admin(user: schemas.BaseUser, db: Session = Depends(db.get_db)):
    query = db.query(models.User).filter(models.User.email == user.email).first()
    if query:
        raise HTTPException(status_code=status.HTTP_306_RESERVED, detail="Email déjà pris")
    if user.password != user.verify_password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Les mots de passes ne correspondent pas")
    user.password = utils.hash_password(user.password)
    user_data = user.model_dump(exclude=["verify_password"], exclude_none=True)
    
    new_user = models.User(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

