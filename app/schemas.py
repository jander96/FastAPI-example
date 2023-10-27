from pydantic  import BaseModel # Para crear modelos de datos con validaciones y serializacion
from typing import Optional   #Para  crear propiedades nullables o opcionales
from datetime import datetime

class UserBody(BaseModel): #Schema
    username:str
    password: str
    nombre: str
    apellido: str
    direccion: Optional[str]
    telefono: int
    correo: str
    
class UserId(BaseModel):
    id: int
    