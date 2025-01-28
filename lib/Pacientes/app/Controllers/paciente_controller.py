from fastapi import HTTPException, status
from lib.Pacientes.app.Schemas.paciente_schemas import PacienteSchema
from lib.Pacientes.app.Repository.paciente_repository import Mysql_Paciente

conexion_repositorio = Mysql_Paciente()


class ControllerEndpoints_Paciente:

    def Validar_paciente(self, new_paciente: PacienteSchema):
        # Validar Cedula: entre 7 y 12 dígitos
        if not (7 <= len(str(new_paciente.Cedula)) <= 12):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="La cédula debe tener entre 7 y 12 dígitos.",
            )

        # Validar Nombre: entre 3 y 15 caracteres
        if not (3 <= len(new_paciente.Nombre) <= 15):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El nombre debe tener entre 3 y 15 caracteres.",
            )

        # Validar Edad: entre 0 y 99 años
        if not (0 < new_paciente.Edad <= 99):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="La edad debe estar entre 0 y 99 años.",
            )

    def Insertar_Paciente_Controllers(self, new_paciente: PacienteSchema):
        self.Validar_paciente(new_paciente)
        paciente_escaneado = new_paciente.model_dump()

        Result_Insertar_Repository = conexion_repositorio.Insertar_Paciente_Repository(
            paciente_escaneado
        )
        return Result_Insertar_Repository

    def Listados_Paciente_Controllers(self):
        try:
            Result_Listado_Repository = (
                conexion_repositorio.Listado_Paciente_Repository()
            )
            return Result_Listado_Repository

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error al obtener el listado de pacientes: {str(e)}",
            )

    def Actualizar_Paciente_Controllers(self, data_paciente: PacienteSchema):

        self.Validar_paciente(data_paciente)

        # Llamar a la función Actualizar_medico
        Result_Actualizar_Repository = (
            conexion_repositorio.Actualizar_Paciente_Repository(data_paciente)
        )
        return Result_Actualizar_Repository

    def Eliminar_Paciente_Controller(self, paciente_id: int):

        conexion_repositorio.Eliminar_Paciente_Repository(paciente_id)
