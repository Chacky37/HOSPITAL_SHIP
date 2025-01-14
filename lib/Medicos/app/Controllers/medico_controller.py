from fastapi import HTTPException, status
from lib.Medicos.app.Schemas.medico_schemas import MedicoSchema
from lib.Medicos.app.Repository.medico_repository import Mysql_Medico

conexion_repositorio = Mysql_Medico()


class ControllerEndpoints:
    def create_doctor(self, doctor: MedicoSchema):
        try:
            # Convertir el esquema a un diccionario
            new_medico = doctor.model_dump()

            # Intentar insertar el nuevo médico en la base de datos
            inserted_medico = conexion_repositorio.insert_medico(new_medico)
            return inserted_medico
        except Exception as e:
            # Manejar cualquier otro error
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error inesperado: {str(e)}"
            )
            
                    
    def Listados_doctores(self):
       try:
          # Intentar obtener la lista de médicos desde el repositorio
          repositorio_listado = conexion_repositorio.Obtener_medicos()
          return repositorio_listado
    
       except Exception as e:
         # Manejar cualquier otro error inesperado
          raise HTTPException(
             status_code=status.HTTP_400_BAD_REQUEST,
             detail=f"Error inesperado al obtener el listado de médicos: {str(e)}" )