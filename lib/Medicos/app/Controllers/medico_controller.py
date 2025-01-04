from fastapi import  HTTPException, status
from lib.Medicos.app.Schemas.medico_schemas import MedicoSchema
from lib.Medicos.app.Repository.medico_repository import Mysql_Medico

conexion_repositorio = Mysql_Medico()
class ControllerEndpoints:
    
    conexion_repositorio = Mysql_Medico()
    def create_doctor(self, doctor: MedicoSchema):
        try:
            # Convertir el esquema a un diccionario
            new_medico = doctor.model_dump()

            # Intentar insertar el nuevo médico en la base de datos
            inserted_medico = conexion_repositorio.insert_medico(new_medico)
           
            return {"message": "Médico creado exitosamente", "data": inserted_medico}


        except Exception as e:
            # Manejar cualquier otro error
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error inesperado: {str(e)}"
            )
