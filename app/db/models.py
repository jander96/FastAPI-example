from app.db.database import Base
from sqlalchemy import Column, String, Integer, Boolean, DateTime
from datetime  import datetime
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase

class User(Base):
    __tablename__ = "usuario"
    
    id = Column(Integer(), primary_key=True,autoincrement=True)
    username = Column(String(),unique=True)
    password = Column(String()) 
    nombre = Column(String(),nullable=True)
    apellido = Column(String(), nullable=True)
    direccion = Column(String(),nullable=True)
    telefono = Column(Integer(),nullable=True)
    correo = Column(String(),unique=True,nullable=True)
    creacion = Column(DateTime(), default=datetime.now())
    estado = Column(Boolean(),default=False)
    venta = relationship("Venta",backref="usuario")

class Venta(Base):
    __tablename__ = "venta"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    usuario_id = Column(Integer(),ForeignKey("usuario.id", ondelete= "CASCADE"))
    venta = Column(Integer())
    ventas_productos = Column(Integer())