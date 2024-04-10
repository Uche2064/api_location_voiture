from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

class BaseUser(BaseModel):
    nom: str
    email: EmailStr
    password: str
    verify_password: str
    
class BaseVoiture(BaseModel):
    marque: str
    model: str
    prix: float
    is_disponible: bool

class LoginAdmin(BaseModel):
    email: EmailStr
    password: str


class ResponseCreateUser(BaseUser):
    created_at: datetime
    updated_at: datetime
    id: int
    class Config:
        from_attributes = True

class VoitureResponse(BaseVoiture):
    created_at: datetime
    updated_at: datetime
    id: int

    class Config:
        from_attributes = True

class TokenData(BaseModel):
    id: Optional[str] = None