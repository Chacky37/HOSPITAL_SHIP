from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status
from lib.Medicos.app.Schemas.medico_schemas import MedicoSchema
from lib.Medicos.config.Base_Mysql import engine
from lib.Medicos.app.Models.medico_models import medico_table


class Mysql_Medico:

    def Insertar_Medico_Repository(self, medico_data):
        try:
            with engine.connect() as conx:
                # Intentar insertar el nuevo médico en la base de datos
                conx.execute(medico_table.insert().values(medico_data))
                conx.commit()
                return medico_data

        except SQLAlchemyError as e:
            # Manejar errores de la base de datos
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al insertar médico: {str(e)}",
            )

    def Listado_Medico_Repository(self):
        try:
            with engine.connect() as conx:
                # Intentar obtener los médicos de la base de datos
                result = conx.execute(medico_table.select()).fetchall()
                return result

        except SQLAlchemyError as e:
            # Manejar errores de la base de datos
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al obtener médicos: {str(e)}",
            )

    def Actualizar_Medico_Repository(self, data_medico: MedicoSchema):
        try:
            with engine.connect() as conx:
                with conx.begin():
                    conx.execute(
                        medico_table.update()
                        .values(
                            Primer_Nombre=data_medico.Primer_Nombre,
                            Segundo_Nombre=data_medico.Segundo_Nombre,
                            Primer_Apellido=data_medico.Primer_Apellido,
                            Segundo_Apellido=data_medico.Segundo_Apellido,
                            Especialidad=data_medico.Especialidad,
                            Contraseña=data_medico.Contraseña,
                        )
                        .where(medico_table.c.Cedula == data_medico.Cedula)
                    )
                    validacion_medico = conx.execute(
                        medico_table.select().where(
                            medico_table.c.Cedula == data_medico.Cedula
                        )
                    ).first()
                    if not validacion_medico:
                        raise HTTPException(
                            status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Médico {data_medico.Cedula} no encontrado",
                        )
                    return validacion_medico

        except SQLAlchemyError as e:
            # Manejar errores de la base de datos
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al actualizar médico: {str(e)}",
            )

    def Eliminar_Medico_Repository(self, medico_cedula: int):
        try:
            with engine.connect() as conx:
                with conx.begin():
                    # Ejecutar la eliminación del médico
                    result = conx.execute(
                        medico_table.delete().where(
                            medico_table.c.Cedula == medico_cedula
                        )
                    )

                    # Verificar si alguna fila fue afectada
                    if result.rowcount == 0:
                        raise HTTPException(
                            status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Médico con ID {medico_cedula} no encontrado.",
                        )
        except HTTPException:
            raise
        except SQLAlchemyError as e:
            # Manejar errores de SQLAlchemy
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al eliminar el médico: {str(e)}",
            )
