from pydantic  import BaseModel # Para crear modelos de datos con validaciones y serializacion
from typing import Optional   #Para  crear propiedades nullables o opcionales
from datetime import datetime

class User(BaseModel): #Schema
    id:int
    nombre: str
    apellido: str
    direccion: Optional[str]
    telefono: int
    correo: str
    creacion_user: datetime = datetime.now()
    
class UserId(BaseModel):
    id: int
    