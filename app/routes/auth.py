from fastapi import HTTPException, APIRouter, status, Depends
from .. import schemas, models, db, utils, oauth2
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm


route = APIRouter(
    prefix="/login",
    tags=["Authentification"]
)

@route.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Token)
async def login_for_access_token(admin: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(db.get_db)):
   user = utils.authentifier_user(admin.username, admin.password, db)

   if not user:
      raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Validation échouée")
   
   token = oauth2.create_access_token({"id": user.id,"email":user.email})
   
   return {"access_token": token, "token_type": "bearer"}