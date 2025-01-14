from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status
from lib.Medicos.config.Base_Mysql import engine
from lib.Medicos.app.Models.medico_models import medico

class Mysql_Medico:
    
    def insert_medico(self, medico_data):
        try:
            with engine.connect() as conx:
            # Intentar insertar el nuevo médico en la base de datos
             conx.execute(medico.insert().values(medico_data))
             conx.commit()
             return medico_data
        
        except SQLAlchemyError as e:
            # Manejar errores de la base de datos
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al insertar médico: {str(e)}"
            )
        except Exception as e:
            # Manejar cualquier otro error
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error inesperado al insertar médico: {str(e)}"
            )
    
    def Obtener_medicos(self):
        try:
            with engine.connect() as conx:
              # Intentar obtener los médicos de la base de datos
              result = conx.execute(medico.select()).fetchall()
              return result
        
        except SQLAlchemyError as e:
        # Manejar errores de la base de datos
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
               detail=f"Error al obtener médicos: {str(e)}"
        )
        except Exception as e:
        # Manejar cualquier otro error
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error inesperado al obtener médicos: {str(e)}"
            )
            