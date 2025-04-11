from pydantic import BaseModel, Field

class modeloPelicula(BaseModel):
    titulo: str = Field(
        ...,
        min_length=2,
        max_length=100,
        description="Título de la película (mínimo 2 caracteres)"
    )
    genero: str = Field(
        ...,
        min_length=4,
        max_length=50,
        description="Género de la película (mínimo 4 caracteres)"
    )
    anio: int = Field(
        ...,
        ge=1000,
        le=9999,
        description="Año de lanzamiento en formato AAAA"
    )
    clasificacion: str = Field(
        ...,
        min_length=1,
        max_length=1,
        pattern="^[ABC]$",
        description="Clasificación permitida: A, B o C"
    )

class modeloPeliculaResponse(modeloPelicula):
    id: int

    class Config:
        orm_mode = True