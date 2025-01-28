from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status
from lib.Pacientes.app.Schemas.paciente_schemas import PacienteSchema
from lib.Pacientes.config.Base_Mysql import engine
from lib.Pacientes.app.Models.paciente_models import paciente_table


class Mysql_Paciente:

    def Insertar_Paciente_Repository(self, paciente_data):
        try:
            with engine.connect() as conx:
                conx.execute(paciente_table.insert().values(paciente_data))
                conx.commit()
                return paciente_data

        except SQLAlchemyError as e:
            # Manejar errores de la base de datos
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al insertar paciente: {str(e)}",
            )

    def Listado_Paciente_Repository(self):
        try:
            with engine.connect() as conx:
                # Intentar obtener los médicos de la base de datos
                result = conx.execute(paciente_table.select()).fetchall()
                return result

        except SQLAlchemyError as e:
            # Manejar errores de la base de datos
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al obtener paciente: {str(e)}",
            )

    def Actualizar_Paciente_Repository(self, paciente_data: PacienteSchema):
        try:
            with engine.connect() as conx:
                with conx.begin():
                    conx.execute(
                        paciente_table.update()
                        .values(
                            Cedula=paciente_data.Cedula,
                            Nombre=paciente_data.Nombre,
                            Edad=paciente_data.Edad,
                        )
                        .where(paciente_table.c.Cedula == paciente_data.Cedula)
                    )
                    validacion_paciente = conx.execute(
                        paciente_table.select().where(
                            paciente_table.c.Cedula == paciente_data.Cedula
                        )
                    ).first()
                    if not validacion_paciente:
                        raise HTTPException(
                            status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Paciente {paciente_data.Cedula} no encontrado",
                        )
                    return validacion_paciente

        except SQLAlchemyError as e:
            # Manejar errores de la base de datos
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al actualizar médico: {str(e)}",
            )

    def Eliminar_Paciente_Repository(self, paciente_cedula: int):
        try:
            with engine.connect() as conx:
                with conx.begin():
                    result = conx.execute(
                        paciente_table.delete().where(
                            paciente_table.c.Cedula == paciente_cedula
                        )
                    )

                    if result.rowcount == 0:
                        raise HTTPException(
                            status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Paciente con ID {paciente_cedula} no encontrado.",
                        )
        except SQLAlchemyError as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al eliminar el paciente: {str(e)}",
            )
