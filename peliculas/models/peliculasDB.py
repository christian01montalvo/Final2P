from DB.conexion import Base
from sqlalchemy import Column, Integer, String

class Pelicula(Base):
    __tablename__ = 'peliculas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    genero = Column(String, nullable=False)
    anio = Column(Integer, nullable=False)
    clasificacion = Column(String(1), nullable=False)