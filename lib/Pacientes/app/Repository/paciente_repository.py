from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status
from lib.Pacientes.config.Base_Mysql import conx
from lib.Pacientes.app.Models.paciente_models import enlace_paciente


class Mysql_Paciente:

    def insert_paciente(self, paciente_data):
        try:
            # Intentar insertar el nuevo médico en la base de datos
            conx.execute(enlace_paciente.insert().values(paciente_data))
            conx.commit()
            return paciente_data

        except SQLAlchemyError as e:
            # Manejar errores de la base de datos
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al insertar médico: {str(e)}",
            )
        except Exception as e:
            # Manejar cualquier otro error
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error inesperado al insertar médico: {str(e)}",
            )
