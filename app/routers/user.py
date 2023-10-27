from fastapi import APIRouter,Depends
from app.schemas import UserBody, UserId
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models

router = APIRouter(prefix='/user', tags= ["Users"])



@router.get('/{user_id}/')
async def get_user(user_id: int):
    return {"response": f"{user_id} recuperado"}



@router.get('/')
async def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.post('/')
async def crear_usuario(user: UserBody, db: Session = Depends(get_db)):
    new_user= models.User(
        username = user.username,
        password = user.password,
        nombre = user.nombre,
        apellido = user.apellido,
        direccion = user.direccion,
        telefono= user.telefono,
        correo = user.correo
        )
    db.add(new_user)
    db.commit()
    
    return {"respuesta": "Usuario creado correctamente"}


@router.delete('/')
async def delete_user(user_id: int):
  return {"response": f"Usuario {user_id} eliminado"}

@router.put('/{user_id}/')
async def delete_user(user_id: int, new_user: UserBody):
    return {"response": f"Usuario {user_id} no encontrado"}



