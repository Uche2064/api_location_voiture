from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

MYSQL_CONNEXION_STRING = "mysql://uche:KD7eMgYx@localhost:3310/location_voiture"

engine = create_engine(MYSQL_CONNEXION_STRING)

session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)

base = declarative_base()

def get_db():
   db = session_local()
   try:
       yield db
   finally:
       db.close()
