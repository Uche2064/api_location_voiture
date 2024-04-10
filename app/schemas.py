from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

class BaseUser(BaseModel):
    nom: str
    email: EmailStr
    password: str
    verify_password: str
    
class BaseVoiture(BaseModel):
    couleur: str
    marque: str
    model: str
    prix: float
    is_disponible: bool


class ResponseCreateUser(BaseModel):
    id: int
    nom: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes = True

class VoitureResponse(BaseVoiture):
    created_at: datetime
    updated_at: datetime
    id: int

    class Config:
        from_attributes = True

class TokenData(BaseModel):
    id: Optional[int] = None
    email: EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str

class UpdateCar(BaseModel):
    marque: Optional[str] = None
    couleur: Optional[str] = None
    model: Optional[str] = None
    prix: Optional[float] = None
    is_disponible: Optional[bool] = None
    updated_at: Optional[datetime] = None


