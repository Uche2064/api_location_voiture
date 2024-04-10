from fastapi import HTTPException, APIRouter, status, Depends
from .. import schemas, models, db, utils, oauth2
from sqlalchemy.orm import Session


route = APIRouter(
    prefix="/auth",
    tags=["Authentification"]
)

@route.post("/")
async def login(admin: schemas.LoginAdmin, db: Session = Depends(db.get_db)):
    get_user = db.query(models.User).filter(models.User.email == admin.email).first()
    if get_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Utilisateur non trouvé")
    
    if not utils.verify_password(admin.password, get_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Information invalide")
    
    access_token = oauth2.create_access_token({
        "id": get_user.id,
        "email": get_user.email
    })
    return {"Access token": access_token, "Token_type": "bearer"}