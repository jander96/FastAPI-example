from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Obteniendo la url de mi base de datos 
#                           esquema   :   usuario:contrasena@servidor:puerto/nombre de base de datos
SQLALCHEMY_DATABASE_URL =  'postgresql://postgres:postgres@localhost:5432/fastapi_database'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()
    