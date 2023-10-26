from fastapi import FastAPI
import uvicorn
from pydantic  import BaseModel # Para crear modelos de datos con validaciones y serializacion
from typing import Optional   #Para  crear propiedades nullables o opcionales
from datetime import datetime
#User Model
class User(BaseModel): #Schema
    id:int
    nombre: str
    apellido: str
    direccion: Optional[str]
    telefono: int
    creacion_user: datetime = datetime.now()
    
app = FastAPI(
    title= 'Proyecto para valorar peliculas', 
    description= 'En este protyecto seremos capaces de valorar peliculas',
    version=  '1'
    )
usuarios = []

@app.on_event('startup')
def startup():
    print('El servidor se esta iniciando')
    
@app.on_event('shutdown')
def shutdown():
    print('El servidor se esta finalizando')
    
    
@app.get('/ruta1')
async def ruta1():
    return {'mensaje':'Bienvenido a tu primer servidor FastApi'}

@app.post('/crear_usuario')
async def crear_usuario(user: User):
    print(user.dict())
    return True



if __name__ == "__main__":
    uvicorn.run("main:app",port = 8000, reload=True)