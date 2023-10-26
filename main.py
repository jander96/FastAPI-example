from fastapi import FastAPI
import uvicorn
from app.routers  import user
from app.db.database import Base, engine

def create_tables():
    Base.metadata.create_all(bind= engine)
create_tables()
app = FastAPI(
    title= 'Proyecto para valorar peliculas', 
    description= 'En este protyecto seremos capaces de valorar peliculas',
    version=  '1'
    )
app.include_router(user.router)

@app.on_event('startup')
def startup():
    print('El servidor se esta iniciando')
    
    
@app.on_event('shutdown')
def shutdown():
    print('El servidor se esta finalizando')
    
    



if __name__ == "__main__":
    uvicorn.run("main:app",port = 8000, reload=True)