from .db import base
from sqlalchemy import Column, Float, String, Integer, TIMESTAMP, Boolean
from sqlalchemy.sql.expression import text

class User(base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nom = Column(String(150), nullable=False, index=True)
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))


class Car(base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    marque = Column(String(150), nullable=False, index=True)
    couleur = Column(String(150), nullable=False, index=True)
    model = Column(String(60))
    prix = Column(Float, nullable=False)
    is_disponible = Column(Boolean, nullable=False, index=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text("now()"))