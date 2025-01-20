from fastapi import HTTPException, status
from lib.Medicos.app.Schemas.medico_schemas import MedicoSchema
from lib.Medicos.app.Repository.medico_repository import Mysql_Medico

conexion_repositorio = Mysql_Medico()


class ControllerEndpoints_Medico:

    def Insertar_Medico_Controllers(self, new_medico: MedicoSchema):
        try:
            # Convertir el esquema a un diccionario
            medico_escaneado = new_medico.model_dump()

            # Intentar insertar el nuevo médico en la base de datos
            Result_Insertar_Repository = (
                conexion_repositorio.Insertar_Medico_Repository(medico_escaneado)
            )
            return Result_Insertar_Repository
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error inesperado: {str(e)}",
            )

    def Listados_Medico_Controllers(self):
        try:
            # Intentar obtener la lista de médicos desde el repositorio
            Result_Listado_Repository = conexion_repositorio.Listado_Medico_Repository()
            return Result_Listado_Repository

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error al obtener el listado de médicos: {str(e)}",
            )

    def Actualizar_Medico_Controllers(self, data_medico: MedicoSchema):
        try:
            # Llamar a la función Actualizar_medico
            Result_Actualizar_Repository = (
                conexion_repositorio.Actualizar_Medico_Repository(data_medico)
            )
            return Result_Actualizar_Repository
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error inesperado al actualizar médico: {str(e)}",
            )

    def Eliminar_Medico_Controller(self, medico_id: int):
        try:
            # Llamar al repositorio para eliminar el médico
            conexion_repositorio.Eliminar_Medico_Repository(medico_id)
        except HTTPException:
            # Repropagar HTTPException sin modificarla
            raise
        except Exception as e:
            # Manejar cualquier otro error inesperado
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error inesperado al eliminar el médico: {str(e)}",
            )
