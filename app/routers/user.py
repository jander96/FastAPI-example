from fastapi import APIRouter
from app.schemas import User, UserId

router = APIRouter(prefix='/user', tags= ["Users"])

usuarios : list[User] = []

@router.get('/ruta1')
async def ruta1():
    return {'mensaje':'Bienvenido a tu primer servidor FastApi'}



@router.get('/{user_id}/')
async def get_user(user_id: int):
    for user in usuarios:
        if user.id == user_id:
            return {"usuario": user}
    return {"response": "Usuario no encontrado"}

@router.post('/')
async def get_user_by_body(user_id: UserId):
    for user in usuarios:
        if user.id == user_id.id:
            return {"usuario": user}
    return {"response": "Usuario no encontrado"}

@router.get('/')
async def get_users():
    return usuarios

@router.post('/crear_usuario/')
async def crear_usuario(user: User):
    usuarios.append(user)
    return {"respuesta": "Usuario creado correctamente"}


@router.delete('/')
async def delete_user(user_id: int):
    for index, user in enumerate(usuarios):
        if user.id == user_id:
            usuarios.remove(user)
            return {"usuario_eliminado": user.id}
    return {"response": "Usuario no encontrado"}

@router.put('/{user_id}/')
async def delete_user(user_id: int, new_user: User):
    for index, user in enumerate(usuarios):
        if user.id == user_id:
            usuarios[index] = new_user
            return {"usuario_actualizado": usuarios[index]}
    return {"response": "Usuario no encontrado"}



