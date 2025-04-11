from fastapi import APIRouter, HTTPException
from modelsPydantic import modeloPelicula, modeloPeliculaResponse
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from DB.conexion import Session
from models.peliculasDB import Pelicula

routerPelicula = APIRouter()


# ver todas

@routerPelicula.get('/peliculas', response_model=list[modeloPeliculaResponse], tags=['ver todas'])
def obtener_peliculas():
    db = Session()
    try:
        peliculas = db.query(Pelicula).all()
        return JSONResponse(content=jsonable_encoder(peliculas))
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "error al consultar peliculas", "excepcion": str(e)})
    finally:
        db.close()



# consultar

@routerPelicula.get('/pelicula/{id}', response_model=modeloPeliculaResponse, tags=['buscar solo 1'])
def obtener_pelicula(id: int):
    db = Session()
    try:
        pelicula = db.query(Pelicula).filter(Pelicula.id == id).first()
        if not pelicula:
            return JSONResponse(status_code=404, content={'message': 'Pelicula no encontrada'})
        return JSONResponse(content=jsonable_encoder(pelicula))
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "error al consultar pelicula", "excepcion": str(e)})
    finally:
        db.close()



# agregar

@routerPelicula.post('/peliculas', response_model=modeloPelicula, tags=['agregar nueva pelicula'])
def agregar_pelicula(pelicula: modeloPelicula):
    db = Session()
    try:
        nueva = Pelicula(**pelicula.model_dump())
        db.add(nueva)
        db.commit()
        return JSONResponse(status_code=201, content={"message": "Pelicula agregada", "pelicula": pelicula.model_dump()})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500, content={"message": "error al guardar pelicula", "excepcion": str(e)})
    finally:
        db.close()



# modificar

@routerPelicula.put('/peliculas/{id}', response_model=modeloPelicula, tags=['modificar Peliculas'])
def modificar_pelicula(id: int, pelicula_actualizada: modeloPelicula):
    db = Session()
    try:
        pelicula = db.query(Pelicula).filter(Pelicula.id == id).first()
        if not pelicula:
            raise HTTPException(status_code=404, detail="Pelicula no encontrada")

        for campo, valor in pelicula_actualizada.model_dump().items():
            setattr(pelicula, campo, valor)

        db.commit()
        db.refresh(pelicula)
        return pelicula
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "error al modificar pelicula", "excepcion": str(e)})
    finally:
        db.close()


# eliminar

@routerPelicula.delete('/peliculas/{id}', tags=['eliminar peliculas'])
def eliminar_pelicula(id: int):
    db = Session()
    try:
        pelicula = db.query(Pelicula).filter(Pelicula.id == id).first()
        if not pelicula:
            return JSONResponse(status_code=404, content={'message': 'Pelicula no encontrada'})

        db.delete(pelicula)
        db.commit()
        return JSONResponse(content={'message': 'Pelicula eliminada exitosamente'})
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "error al eliminar pelicula", "excepcion": str(e)})
    finally:
        db.close()