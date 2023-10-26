# Dos formas actualmente de correr el servidor
    1. Desde la terminal uvicorn main:app
    2. Agregar este codigo:
        ~
        if __name__ == "__main__":
            uvicorn.run("main:app",port =8000)
        ~