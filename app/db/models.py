from app.db.database import Base
from sqlalchemy import Column, String, Integer, Boolean, DateTime
from datetime  import datetime

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True,autoincrement=True)
    nombre = Column(String)
    apellido = Column(String)
    direccion = Column(String)
    telefono = Column(Integer)
    correo = Column(String)
    creacion = Column(DateTime, default=datetime.now())
    estado = Column(Boolean)