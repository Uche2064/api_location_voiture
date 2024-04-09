from .db import base
from sqlalchemy import Column, String, Integer, TIMESTAMP

class User(base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nom = Column(String(150), nullable=False, index=True)
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(255), nullable=False)

