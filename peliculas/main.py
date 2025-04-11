from fastapi import FastAPI
from DB.conexion import engine, Base
from routers.pelicula import routerPelicula

app = FastAPI(
    title="API de Peliculas ",
    description="Christian MONTALVO - Proyecto FastAPI 3er Parcial",
    version="examen3p"
)


Base.metadata.create_all(bind=engine)


@app.get('/', tags=['inicio'])
def home():
    return {'message': 'bienvenido a mi final '}


app.include_router(routerPelicula)