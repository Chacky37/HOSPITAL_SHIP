from fastapi import  HTTPException, status
from lib.Pacientes.app.Schemas.paciente_schemas import PacienteSchema
from lib.Pacientes.app.Repository.paciente_repository import Mysql_Paciente

conexion_repositorio = Mysql_Paciente()

class ControllerEndpoints:

    conexion_repositorio = Mysql_Paciente()
    def create_enfermo(self, enfermo: PacienteSchema):
        try:
            # Convertir el esquema a un diccionario
            new_paciente = enfermo.model_dump()

            # Intentar insertar el nuevo médico en la base de datos
            inserted_paciente = conexion_repositorio.insert_paciente(new_paciente)
           
            return {"message": "Médico creado exitosamente", "data": inserted_paciente}


        except Exception as e:
            # Manejar cualquier otro error
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error inesperado: {str(e)}"
            )
