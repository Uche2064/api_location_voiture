from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .config import setting

MYSQL_CONNEXION_STRING = f"mysql://{setting.db_username}:{setting.db_password}@{setting.db_host}:{setting.db_port}/{setting.db_name}"

engine = create_engine(MYSQL_CONNEXION_STRING)

session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)

base = declarative_base()

def get_db():
   db = session_local()
   try:
       yield db
   finally:
       db.close()
